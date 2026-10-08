import hashlib
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from governor import workflow as w


SOURCE = Path(__file__).resolve().parents[1]


def tree_hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / "governor"
        self.root.mkdir()
        config = json.loads((SOURCE / "governor/config.json").read_text())
        self.config = config
        for relative in w.local_inputs(SOURCE, config) + ["templates/review.md", "templates/allocation.md"]:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / relative, target)
        self.paths = {}
        for p in config["projects"]:
            repo = self.base / p["id"]
            repo.mkdir()
            self.git(repo, "init", "--initial-branch=main")
            self.git(repo, "remote", "add", "origin", f"https://github.com/{p['repository']}.git")
            status = repo / p["status_path"]
            status.parent.mkdir(parents=True, exist_ok=True)
            status.write_text("# Authoritative handoff\n\n## Current approved work packet\n\n"
                              "`specs/SPEC-001.md`\nStatus: `APPROVED_FOR_IMPLEMENTATION`\n"
                              "Human gate: `OWNER_REVIEW`\n\n## Current gate\n\n"
                              "Recovery complete. No incident action authorized.\n")
            self.git(repo, "add", ".")
            self.git(repo, "commit", "--no-gpg-sign", "-m", "Initial evidence")
            self.paths[p["id"]] = repo
        self.overrides = {key: str(path) for key, path in self.paths.items()}

    def git(self, repo, *args):
        return subprocess.run(
            ["git", "-c", "init.templateDir=", "-c", "core.hooksPath=/dev/null",
             "-c", "user.name=Governor test", "-c", "user.email=test@example.invalid",
             "-C", str(repo), *args], check=True, capture_output=True,
            env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"),
        ).stdout.decode().strip()

    def assemble(self, packet="test"):
        return w.assemble(self.root, packet, self.overrides)

    def verify(self, packet="test"):
        return w.verify(self.root, packet, self.overrides)

    def write_config(self):
        (self.root / "governor/config.json").write_text(w.json_text(self.config))

    def test_authority_full_governed_tree_is_byte_unchanged(self):
        # Includes every fixture file, .git/index, refs, objects and configuration.
        before = {key: tree_hashes(path) for key, path in self.paths.items()}
        manifest = self.assemble()
        self.assertEqual(self.verify()["result"], "FRESH_AT_CHECK_ONLY")
        self.assertEqual(before, {key: tree_hashes(path) for key, path in self.paths.items()})
        self.assertEqual(manifest["external_capabilities"]["governed_mutation_commands"], [])
        self.assertEqual(manifest["external_capabilities"]["network_calls"], 0)

    def test_head_movement_fails_closed_and_marks_state_stale(self):
        self.assemble()
        repo = self.paths["knowledge-compiler"]
        (repo / "new.txt").write_text("new work")
        self.git(repo, "add", ".")
        self.git(repo, "commit", "--no-gpg-sign", "-m", "New work packet")
        report = self.verify()
        self.assertEqual(report["result"], w.STALE)
        self.assertIn("knowledge-compiler: evaluated_head changed", report["mismatches"])
        state = json.loads((self.root / "state/portfolio.yaml").read_text())
        self.assertEqual(state["freshness"], w.STALE)

    def test_uncommitted_status_change_fails_even_with_same_head(self):
        self.assemble()
        repo = self.paths["opportunity-radar"]
        path = repo / "docs/STATUS.md"
        path.write_text(path.read_text() + "\nOwner gate changed\n")
        report = self.verify()
        self.assertEqual(report["result"], w.STALE)
        self.assertIn("opportunity-radar: status_sha256 changed", report["mismatches"])

    def test_governor_constitution_change_fails_closed(self):
        self.assemble()
        path = self.root / "CONSTITUTION.md"
        path.write_text(path.read_text() + "\nchanged\n")
        self.assertIn("Governor input changed: CONSTITUTION.md", self.verify()["mismatches"])

    def test_packet_tampering_fails_closed(self):
        self.assemble()
        path = self.root / "evidence/test/projects/knowledge-compiler/STATUS.md"
        path.write_text("corrupt")
        self.assertEqual(self.verify()["result"], w.STALE)

    def test_derived_state_tampering_fails_closed(self):
        self.assemble()
        path = self.root / "state/portfolio.yaml"
        state = json.loads(path.read_text())
        state["projects"][0]["governor_verdict"]["text"] = "RUN UNAUTHORIZED WORK"
        path.write_text(w.json_text(state))
        self.assertEqual(self.verify()["result"], w.STALE)

    def test_missing_authoritative_status_requires_owner_review(self):
        (self.paths["opportunity-radar"] / "docs/STATUS.md").unlink()
        with self.assertRaises(OSError):
            self.assemble()
        self.assertFalse((self.root / "state/portfolio.yaml").exists())

    def test_change_during_assembly_is_stale(self):
        actual = w.check_freshness

        def move(root, manifest, paths):
            path = paths["asymmetry-engine"] / "STATUS.md"
            path.write_text(path.read_text() + "\nnew gate\n")
            return actual(root, manifest, paths)

        with patch.object(w, "check_freshness", side_effect=move):
            self.assertEqual(self.assemble()["freshness"], w.STALE)
        self.assertEqual(self.verify()["result"], w.STALE)

    def test_packet_immutable_and_traversal_rejected(self):
        self.assemble()
        before = tree_hashes(self.root / "evidence/test")
        with self.assertRaises(w.GovernorError):
            self.assemble()
        self.assertEqual(before, tree_hashes(self.root / "evidence/test"))
        for packet in ("../escape", "/tmp/escape", "name/child", "-option"):
            with self.assertRaises(w.GovernorError):
                self.assemble(packet)

    def test_write_symlink_to_governed_repo_is_rejected(self):
        (self.root / "state").symlink_to(self.paths["knowledge-compiler"], target_is_directory=True)
        before = tree_hashes(self.paths["knowledge-compiler"])
        with self.assertRaises(w.GovernorError):
            self.assemble()
        self.assertEqual(before, tree_hashes(self.paths["knowledge-compiler"]))

    def test_status_symlink_outside_repo_is_rejected(self):
        path = self.paths["knowledge-compiler"] / "STATUS.md"
        path.unlink()
        path.symlink_to(self.root / "CONSTITUTION.md")
        with self.assertRaises(w.GovernorError):
            self.assemble()

    def test_unknown_baseline_is_never_fabricated(self):
        project = self.assemble()["projects"][0]
        self.assertIsNone(project["history"]["baseline"])
        self.assertEqual(project["history"]["scope"], "RECENT_CONTEXT_ONLY_BASELINE_UNKNOWN")
        self.assertNotIn("HEAD_MOVEMENT_SINCE_ACCEPTED_REVIEW", project["review_due"]["facts"])
        self.assertTrue(project["review_due"]["unknowns"])

    def test_literal_historical_gate_and_recovery_are_only_candidates(self):
        candidates = self.assemble()["projects"][0]["review_due"]["candidates"]
        self.assertEqual({c["classification"] for c in candidates}, {"REVIEW_CANDIDATE"})
        self.assertIn("INCIDENT_RECOVERY_TEXT", {c["code"] for c in candidates})

    def test_known_baseline_history_is_bounded_and_not_experiment_count(self):
        repo = self.paths["knowledge-compiler"]
        self.config["projects"][0]["previous_evaluated_head"] = self.git(repo, "rev-parse", "HEAD")
        self.config["projects"][0]["previous_status_sha256"] = w.digest((repo / "STATUS.md").read_bytes())
        self.write_config()
        for i in range(6):
            self.git(repo, "commit", "--no-gpg-sign", "--allow-empty", "-m", f"Work {i}")
        with patch.object(w, "MAX_COMMITS", 5):
            project = self.assemble()["projects"][0]
        self.assertTrue(project["history"]["truncated"])
        self.assertEqual(len(project["history"]["commits"]), 5)
        self.assertEqual(project["history"]["scope"], "SINCE_ACCEPTED_REVIEW")
        self.assertIn("HEAD_MOVEMENT_SINCE_ACCEPTED_REVIEW", project["review_due"]["facts"])
        self.assertIn("FIVE_COMMITS_REQUIRE_MATERIALITY_REVIEW",
                      {c["code"] for c in project["review_due"]["candidates"]})

    def test_identity_mismatch_and_checkout_overlap_rejected(self):
        repo = self.paths["knowledge-compiler"]
        self.git(repo, "remote", "set-url", "origin", "https://github.com/other/project.git")
        with self.assertRaises(w.GovernorError):
            self.assemble()
        with self.assertRaises(w.GovernorError):
            w.repository_paths(self.root, self.config, {"knowledge-compiler": str(self.root)})

    def test_remote_identity_ssh_supported(self):
        repo = self.paths["knowledge-compiler"]
        self.git(repo, "remote", "set-url", "origin", "git@github.com:CIF84/knowledge-compiler.git")
        self.assertEqual(self.assemble()["freshness"], "MATCHED_AT_ASSEMBLY_ONLY")

    def test_followup_must_be_evidence_not_invented_authority(self):
        self.config["projects"][0]["follow_up"] = "Automatically activate new work"
        self.write_config()
        with self.assertRaises(w.GovernorError):
            self.assemble()

    def test_conditional_followup_is_not_proof_of_review_due(self):
        self.assertEqual(self.assemble()["projects"][0]["review_due"]["state"], "REVIEW_CANDIDATE")

    def test_explicit_prior_review_requirement_is_detected(self):
        path = self.root / self.config["previous_review"]
        quote = "Governor review is required before any further work."
        path.write_text(path.read_text().replace("## Opportunity Radar", quote + "\n\n## Opportunity Radar"))
        self.config["projects"][0]["follow_up"] = quote
        self.config["projects"][0]["follow_up_kind"] = "EXPLICIT_REVIEW_REQUIRED"
        self.write_config()
        project = self.assemble()["projects"][0]
        self.assertIn("PRIOR_GOVERNOR_EXPLICIT_REVIEW_REQUIREMENT", project["review_due"]["facts"])
        self.assertEqual(project["review_due"]["state"], "REVIEW_DUE")

    def test_bounded_reads_and_missing_status_sections(self):
        path = self.paths["knowledge-compiler"] / "STATUS.md"
        path.write_bytes(b"x" * (w.MAX_BYTES + 1))
        with self.assertRaises(w.GovernorError):
            self.assemble()
        path.write_text("# No coordination information")
        with self.assertRaises(w.GovernorError):
            self.assemble()

    def test_reconstruction_and_templates_preserve_evidence_dimensions(self):
        first = self.assemble("first")
        second = self.assemble("second")
        for a, b in zip(first["projects"], second["projects"]):
            # Timestamp records the invocation, not an input-derived judgment.
            self.assertEqual({k: v for k, v in a.items() if k != "evidence_timestamp"},
                             {k: v for k, v in b.items() if k != "evidence_timestamp"})
        self.assertEqual(first["governor_input_sha256"], second["governor_input_sha256"])
        for name in ("GOV-DRAFT.md", "CYCLE-DRAFT.md"):
            text = (self.root / f"evidence/second/{name}").read_text()
            self.assertNotIn("{{", text)
            for project in second["projects"]:
                self.assertIn(project["evaluated_head"], text)
                self.assertIn(project["status_sha256"], text)
        text = (self.root / "evidence/second/GOV-DRAFT.md").read_text()
        for label in ("Purpose", "Truth", "Safety", "Capital", "Strategic debt", "Trajectory", "Verdict"):
            self.assertIn(f"### {label}", text)
        # Older evidence remains intact, but may not certify the latest derived state.
        self.assertEqual(self.verify("first")["result"], w.STALE)
        self.assertEqual(self.verify("second")["result"], "FRESH_AT_CHECK_ONLY")

    def test_duplicate_status_sections_are_preserved(self):
        text = "# Status\n\n## Current gate\nOld gate\n\n## Current gate\nNew gate\n"
        self.assertEqual([s["text"] for s in w.status_excerpts(text)[1:]], ["Old gate", "New gate"])

    def test_missing_repository_at_verification_fails_closed(self):
        self.assemble()
        shutil.rmtree(self.paths["knowledge-compiler"])
        self.assertEqual(self.verify()["result"], w.STALE)

    def test_nonancestor_baseline_is_not_silently_used(self):
        repo = self.paths["knowledge-compiler"]
        initial = self.git(repo, "rev-parse", "HEAD")
        self.git(repo, "commit", "--no-gpg-sign", "--allow-empty", "-m", "Abandoned work")
        self.config["projects"][0]["previous_evaluated_head"] = self.git(repo, "rev-parse", "HEAD")
        self.git(repo, "checkout", "--detach", initial)
        self.write_config()
        project = self.assemble()["projects"][0]
        self.assertEqual(project["history"]["scope"], "BASELINE_NOT_ANCESTOR")
        self.assertIn("BASELINE_NOT_ANCESTOR_REVIEW_REQUIRED", project["review_due"]["facts"])

    def test_cli_stale_exit_code_is_two(self):
        self.assemble()
        path = self.paths["knowledge-compiler"] / "STATUS.md"
        path.write_text(path.read_text() + "\nchanged\n")
        args = ["verify", "--packet", "test"]
        for key, path in self.paths.items():
            args += ["--repo", f"{key}={path}"]
        with patch.object(w, "__file__", str(self.root / "governor/workflow.py")):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(w.main(args), 2)
        self.assertIn(w.STALE, output.getvalue())


if __name__ == "__main__":
    unittest.main()
