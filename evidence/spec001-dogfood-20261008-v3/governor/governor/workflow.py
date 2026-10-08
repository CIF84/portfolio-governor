"""SPEC-001: standard-library-only, file/Git observation with bounded reads.

JSON output in portfolio.yaml is a YAML 1.2 subset. Strategic fields are copied
from the accepted review, never inferred from project activity.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

MAX_BYTES = 256 * 1024
MAX_COMMITS = 100
TIMEOUT = 15
STALE = "STALE_REVIEW_REFRESH_REQUIRED"
STATUS_SECTIONS = {
    "Current approved work packet", "Current gate", "Current state", "Active work",
    "Authority", "Next operation",
}


class GovernorError(Exception):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(path):
    with Path(path).open("rb") as stream:
        data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise GovernorError(f"Input exceeds {MAX_BYTES} bytes: {path}")
    return data


def read_text(path):
    return read_bytes(path).decode("utf-8")


def contained(root, relative):
    """Reject traversal and symlinks that cross the declared read/write root."""
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise GovernorError(f"Unsafe relative path: {relative}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise GovernorError(f"Path escapes root: {relative}")
    return path


def output_path(root, relative):
    # Writes also reject symlinks within the root, including dangling links.
    path = root
    for part in Path(relative).parts:
        path = path / part
        if path.is_symlink():
            raise GovernorError(f"Output symlink rejected: {path}")
    return contained(root, relative)


def write_text(root, relative, content):
    path = output_path(root, relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def json_text(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def git(repo, *args):
    # Only callers below choose commands. No shell, fetch, checkout, hooks,
    # remote operations, diff drivers, or user-selected Git command exists.
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    result = subprocess.run(
        ["git", "--no-pager", "-c", "core.fsmonitor=false", "-c",
         "core.untrackedCache=false", "-C", str(repo), *args],
        capture_output=True, timeout=TIMEOUT, env=env,
    )
    if result.returncode:
        raise GovernorError(f"Read-only Git {args[0]} failed in {repo}")
    if len(result.stdout) > MAX_BYTES:
        raise GovernorError(f"Git {args[0]} output exceeds bound")
    return result.stdout.decode("utf-8")


def section_blocks(text, level):
    pattern = rf"(?m)^{'#' * level} (.+)$"
    matches = list(re.finditer(pattern, text))
    return [
        (match.group(1), text[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)].strip())
        for i, match in enumerate(matches)
    ]


def sections(text, level):
    return dict(section_blocks(text, level))


def status_excerpts(text):
    """Keep declared sections verbatim; do not resolve contradictory authority."""
    selected = [{"heading": "Preamble", "text": text.split("\n## ", 1)[0].strip()}]
    selected += [{"heading": name, "text": body}
                 for name, body in section_blocks(text, 2) if name in STATUS_SECTIONS]
    if len(selected) == 1:
        raise GovernorError("Authoritative status has no recognized coordination section; owner review required")
    return selected


def load_config(root):
    config = json.loads(read_text(contained(root, "governor/config.json")))
    if len(config["projects"]) != 3 or len({p["id"] for p in config["projects"]}) != 3:
        raise GovernorError("Exactly three distinct governed projects are required")
    return config


def repository_paths(root, config, overrides=None):
    overrides = overrides or {}
    unknown = set(overrides) - {p["id"] for p in config["projects"]}
    if unknown:
        raise GovernorError(f"Unknown project overrides: {sorted(unknown)}")
    paths = {}
    for project in config["projects"]:
        repo = Path(overrides.get(project["id"], root / project["local_path"])).resolve()
        if repo.is_relative_to(root) or root.is_relative_to(repo):
            raise GovernorError("Governor and governed checkouts must not overlap")
        if Path(git(repo, "rev-parse", "--show-toplevel").strip()).resolve() != repo:
            raise GovernorError(f"Expected a repository root: {repo}")
        remote = git(repo, "remote", "get-url", "origin").strip()
        identity = re.fullmatch(r"(?:https://github\.com/|git@github\.com:)([^\s]+?)(?:\.git)?/?", remote)
        if not identity or identity.group(1) != project["repository"]:
            raise GovernorError(f"Repository identity mismatch: {project['id']}")
        paths[project["id"]] = repo
    if len(set(paths.values())) != len(paths):
        raise GovernorError("Governed repository paths must be distinct")
    return paths


def snapshot(repo, status_path):
    head = git(repo, "rev-parse", "HEAD").strip()
    status = read_bytes(contained(repo, status_path))
    changes = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=no")
    return {
        "evaluated_head": head,
        "status_sha256": digest(status),
        "tracked_worktree_dirty": bool(changes),
        "tracked_worktree_status_sha256": digest(changes.encode()),
    }, status.decode("utf-8")


def history(repo, baseline, head):
    if baseline is not None and not re.fullmatch(r"[a-f0-9]{40}", baseline):
        raise GovernorError("Baseline must be an exact 40-character evaluated HEAD")
    if baseline is not None:
        result = git(repo, "merge-base", baseline, head).strip()
        if result != baseline:
            return {"scope": "BASELINE_NOT_ANCESTOR", "baseline": baseline, "commits": [], "truncated": False}
    revision = f"{baseline}..{head}" if baseline else head
    rows = git(repo, "log", f"--max-count={MAX_COMMITS + 1}", "--format=%H%x09%s", revision, "--").splitlines()
    return {
        "scope": "SINCE_ACCEPTED_REVIEW" if baseline else "RECENT_CONTEXT_ONLY_BASELINE_UNKNOWN",
        "baseline": baseline,
        "commits": [{"head": line.split("\t", 1)[0], "subject": line.split("\t", 1)[1]} for line in rows[:MAX_COMMITS]],
        "truncated": len(rows) > MAX_COMMITS,
    }


def triggers(project, observed, excerpts, log):
    facts, candidates, unknown = [], [], []
    if project["previous_evaluated_head"] is None:
        unknown.append("ACCEPTED_REVIEW_HEAD_UNKNOWN: movement since GOV-004 cannot be counted")
    elif project["previous_evaluated_head"] != observed["evaluated_head"]:
        facts.append("HEAD_MOVEMENT_SINCE_ACCEPTED_REVIEW")
    if log["scope"] == "BASELINE_NOT_ANCESTOR":
        facts.append("BASELINE_NOT_ANCESTOR_REVIEW_REQUIRED")
    if project["previous_status_sha256"] is None:
        unknown.append("ACCEPTED_STATUS_UNKNOWN: transition since accepted review cannot be proven")
    elif project["previous_status_sha256"] != observed["status_sha256"]:
        facts.append("AUTHORITATIVE_STATUS_CHANGED")
    if project.get("follow_up"):
        if project["follow_up_kind"] == "EXPLICIT_REVIEW_REQUIRED":
            facts.append("PRIOR_GOVERNOR_EXPLICIT_REVIEW_REQUIREMENT")
        else:
            candidates.append({"code": "PRIOR_GOVERNOR_FOLLOW_UP_REQUIRES_ASSESSMENT",
                               "classification": "REVIEW_CANDIDATE",
                               "kind": project["follow_up_kind"], "evidence": project["follow_up"],
                               "limitation": "A constraint, next boundary or conditional follow-up is not proof that review is due now"})
    # Literal observations are not semantic conclusions about current authority.
    patterns = {
        "HUMAN_GATE_TEXT": r"(?i)owner.review|human.gate|awaiting.owner|human.approval|human.authorization",
        "INCIDENT_RECOVERY_TEXT": r"(?i)\brecovery\b|\baborted\b|\bstate.loss\b|\blost.operational.state\b",
        "WORK_PACKET_TEXT": r"\b(?:SPEC|BENCH|Experiment)[- ]\d+",
    }
    for code, pattern in patterns.items():
        hits = [{"heading": s["heading"], "line": line.strip()}
                for s in excerpts for line in s["text"].splitlines() if re.search(pattern, line)]
        if hits:
            candidates.append({"code": code, "classification": "REVIEW_CANDIDATE", "evidence": hits[:10],
                               "truncated": len(hits) > 10,
                               "limitation": "Literal text may be historical, conditional, contradictory, or a prohibition"})
    if len(log["commits"]) >= 5 and log["scope"] == "SINCE_ACCEPTED_REVIEW":
        candidates.append({"code": "FIVE_COMMITS_REQUIRE_MATERIALITY_REVIEW", "classification": "REVIEW_CANDIDATE",
                           "limitation": "Commits are not proven material experiments or completed work packets"})
    if observed["tracked_worktree_dirty"]:
        unknown.append("UNCOMMITTED_EVIDENCE: HEAD does not describe all working-copy evidence")
    return {"state": "REVIEW_DUE" if facts else "REVIEW_CANDIDATE" if candidates else "NO_DETECTED_TRIGGER",
            "facts": facts, "candidates": candidates, "unknowns": unknown,
            "follow_up_evidence": project.get("follow_up")}


def local_inputs(root, config):
    return ["governor/config.json", "governor/workflow.py", "governor/__main__.py", "governor/__init__.py",
            "templates/review.md", "templates/allocation.md",
            "CONSTITUTION.md", "GOVERNOR_PROTOCOL.md", "PROJECTS.md",
            config["previous_review"], config["previous_allocation"],
            *[p["constitution"] for p in config["projects"]]]


def check_freshness(root, manifest, paths):
    mismatches = []
    for relative, expected in manifest["governor_input_sha256"].items():
        try:
            if digest(read_bytes(contained(root, relative))) != expected:
                mismatches.append(f"Governor input changed: {relative}")
        except (OSError, GovernorError):
            mismatches.append(f"Governor input unavailable: {relative}")
    for project in manifest["projects"]:
        try:
            current, _ = snapshot(paths[project["id"]], project["authoritative_status_path"])
            for key in ("evaluated_head", "status_sha256", "tracked_worktree_status_sha256"):
                if current[key] != project[key]:
                    mismatches.append(f"{project['id']}: {key} changed")
        except (OSError, GovernorError, subprocess.TimeoutExpired):
            mismatches.append(f"{project['id']}: evidence unavailable")
    return mismatches


def template(root, name, manifest):
    text = read_text(contained(root, f"templates/{name}.md"))
    values = {
        "EVIDENCE_PACKET": manifest["packet_id"], "ASSEMBLED_AT": manifest["assembled_at"],
        "CONSTITUTION_VERSION": manifest["constitution_version"],
        "PREVIOUS_REVIEW": manifest["previous_review"],
        "PREVIOUS_ALLOCATION": manifest["previous_allocation"],
        "HEAD_TABLE": "\n".join(f"| {p['name']} | `{p['evaluated_head']}` | `{p['authoritative_status_path']}` | `{p['status_sha256']}` |"
                               for p in manifest["projects"]),
    }
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def assemble(root, packet_id, overrides=None):
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}", packet_id):
        raise GovernorError("Packet ID must be 1–80 letters, digits, underscores or hyphens")
    config = load_config(root)
    paths = repository_paths(root, config, overrides)
    packet_relative = f"evidence/{packet_id}"
    if output_path(root, packet_relative).exists():
        raise GovernorError("Evidence packet already exists; choose a new ID (packets are not overwritten)")
    # Validate destinations before reading project evidence or writing anything.
    output_path(root, "state/portfolio.yaml")
    inputs = {p: read_bytes(contained(root, p)) for p in local_inputs(root, config)}
    review = sections(inputs[config["previous_review"]].decode(), 2)
    constitution = inputs["CONSTITUTION.md"].decode().splitlines()[0]
    version = re.search(r"v\d+\.\d+", constitution)
    if not version:
        raise GovernorError("Constitution version is not explicit")
    observed_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    manifest = {
        "schema_version": 1, "packet_id": packet_id, "assembled_at": observed_at,
        "authority": "GOVERNOR_REPO_ONLY", "promotion": "NOT_AUTHORIZED",
        "mode": "REHEARSAL_EVIDENCE_ONLY", "freshness": "UNVERIFIED",
        "evidence_scope": "LOCAL_WORKTREE_ONLY", "remote_state": "NOT_CHECKED_OFFLINE",
        "constitution_version": version.group(), "previous_review": config["previous_review"],
        "previous_allocation": config["previous_allocation"],
        "governor_input_sha256": {p: digest(b) for p, b in inputs.items()}, "projects": [],
    }
    copies = {}
    for project in config["projects"]:
        observed, status = snapshot(paths[project["id"]], project["status_path"])
        excerpts = status_excerpts(status)
        prior = sections(review[project["name"]], 3)
        if not prior.get("Verdict") or not prior.get("Strategic debt"):
            raise GovernorError("Accepted review lacks verdict/strategic debt; owner review required")
        if project.get("follow_up") and project["follow_up"] not in review[project["name"]]:
            raise GovernorError("Configured follow-up is not an exact accepted-review quotation")
        if project.get("follow_up") and project.get("follow_up_kind") not in {
            "EXPLICIT_REVIEW_REQUIRED", "CONDITIONAL", "CONSTRAINT", "NEXT_BOUNDARY",
        }:
            raise GovernorError("Follow-up kind must be explicitly annotated from the accepted review")
        log = history(paths[project["id"]], project["previous_evaluated_head"], observed["evaluated_head"])
        entry = {
            "id": project["id"], "name": project["name"], "repository": project["repository"],
            "constitution_path": project["constitution"], "authoritative_status_path": project["status_path"],
            **observed, "evidence_timestamp": observed_at,
            "project_gate_state": {"classification": "VERBATIM_OBSERVATION_REQUIRES_REVIEW", "excerpts": excerpts},
            "last_governor_review": config["previous_review"], "last_allocation": config["previous_allocation"],
            "governor_verdict": {"source": config["previous_review"], "status": "LAST_ACCEPTED_NOT_REEVALUATED",
                                 "text": prior["Verdict"]},
            "material_strategic_debt": {"source": config["previous_review"], "status": "LAST_ACCEPTED_NOT_REEVALUATED",
                                        "text": prior["Strategic debt"]},
            "history": log, "review_due": triggers(project, observed, excerpts, log),
        }
        manifest["projects"].append(entry)
        copies[f"projects/{project['id']}/STATUS.md"] = status
    mismatches = check_freshness(root, manifest, paths)
    manifest["freshness"] = STALE if mismatches else "MATCHED_AT_ASSEMBLY_ONLY"
    manifest["freshness_mismatches"] = mismatches
    manifest["external_capabilities"] = {
        "filesystem": "Bounded reads of declared Governor inputs and project status only; Governor-local output writes",
        "git": ["rev-parse --show-toplevel", "remote get-url origin", "rev-parse HEAD",
                "status --porcelain=v1 -z --untracked-files=no", "merge-base (when baseline known)", "log --max-count=101 --format=..."],
        "network_calls": 0, "model_calls": 0, "spend": 0, "governed_mutation_commands": [],
        "limitations": "No scan of private/ignored files; no global proof against writes by concurrent actors",
    }
    for relative, data in inputs.items():
        copies[f"governor/{relative}"] = data.decode()
    copies["GOV-DRAFT.md"] = template(root, "review", manifest)
    copies["CYCLE-DRAFT.md"] = template(root, "allocation", manifest)
    manifest["packet_file_sha256"] = {p: digest(text.encode()) for p, text in copies.items()}
    for relative, content in copies.items():
        write_text(root, f"{packet_relative}/{relative}", content)
    write_text(root, f"{packet_relative}/manifest.json", json_text(manifest))
    write_text(root, "state/portfolio.yaml", json_text(manifest))
    # Seal state against the manifest for later verification.
    receipt = {"manifest_sha256": digest(json_text(manifest).encode()),
               "portfolio_sha256": digest(json_text(manifest).encode())}
    write_text(root, f"{packet_relative}/assembly-receipt.json", json_text(receipt))
    return manifest


def verify(root, packet_id, overrides=None):
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}", packet_id):
        raise GovernorError("Invalid packet ID")
    packet = contained(root, f"evidence/{packet_id}")
    manifest_bytes = read_bytes(packet / "manifest.json")
    manifest = json.loads(manifest_bytes)
    receipt = json.loads(read_text(packet / "assembly-receipt.json"))
    mismatches = []
    if digest(manifest_bytes) != receipt["manifest_sha256"]:
        mismatches.append("Evidence manifest changed")
    for relative, expected in manifest["packet_file_sha256"].items():
        try:
            if digest(read_bytes(contained(packet, relative))) != expected:
                mismatches.append(f"Packet evidence changed: {relative}")
        except (OSError, GovernorError):
            mismatches.append(f"Packet evidence unavailable: {relative}")
    try:
        config = load_config(root)
        paths = repository_paths(root, config, overrides)
        mismatches += check_freshness(root, manifest, paths)
        if digest(read_bytes(contained(root, "state/portfolio.yaml"))) != receipt["portfolio_sha256"]:
            mismatches.append("Derived portfolio state changed or belongs to another packet")
    except (OSError, GovernorError, subprocess.TimeoutExpired):
        mismatches.append("Inputs, repositories, or derived state unavailable")
    if manifest["freshness"] == STALE:
        mismatches.append("Packet was stale at assembly; reassemble")
    report = {"packet_id": packet_id, "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "result": STALE if mismatches else "FRESH_AT_CHECK_ONLY",
              "evidence_scope": "LOCAL_WORKTREE_ONLY", "mismatches": mismatches,
              "authority": "OWNER_REVIEW_REQUIRED_NO_VERDICT_PUBLISHED"}
    write_text(root, f"evidence/{packet_id}/freshness-check.json", json_text(report))
    if mismatches:
        # Mark derived state stale without rewriting frozen packet evidence.
        state_path = contained(root, "state/portfolio.yaml")
        if state_path.exists():
            state = json.loads(read_text(state_path))
            if state.get("packet_id") == packet_id:
                state["freshness"] = STALE
                state["freshness_mismatches"] = mismatches
                write_text(root, "state/portfolio.yaml", json_text(state))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("assemble", "verify"))
    parser.add_argument("--packet", required=True, help="New packet ID, or existing ID for verify")
    parser.add_argument("--repo", action="append", default=[], metavar="PROJECT_ID=PATH",
                        help="Read-only checkout override; nothing is written there")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    try:
        overrides = dict(value.split("=", 1) for value in args.repo)
        result = assemble(root, args.packet, overrides) if args.command == "assemble" else verify(root, args.packet, overrides)
        state = result.get("result", result.get("freshness"))
        print(json_text({"packet": args.packet, "result": state,
                         "output": f"evidence/{args.packet}", "promotion": "NOT_AUTHORIZED"}), end="")
        return 2 if state == STALE else 0
    except (GovernorError, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as exc:
        print(f"EVIDENCE_UNAVAILABLE_OWNER_REVIEW_REQUIRED: {exc}", file=sys.stderr)
        return 2
