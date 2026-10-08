# SPEC-001 operating instructions

The workflow prepares read-only evidence for owner review. Python 3.10+ and Git
are the only dependencies. It has no network, provider, project write, review
publication, scheduling, or execution command.

From the Governor repository:

```sh
python3 -m governor assemble --packet rehearsal-20261008-v2
python3 -m governor verify --packet rehearsal-20261008-v2
python3 -m unittest discover -s tests -v
```

Use a new packet ID each time. Existing packets are never overwritten by
assembly. Verification writes a separate check receipt and, on failure, marks
the corresponding derived state stale. A stale packet must be replaced by a new
assembly, even if a checkout is later restored to its old HEAD.

`governor/config.json` declares the three repository identities, local sibling
paths, authoritative status paths, accepted review/allocation, and exact
follow-up quotations. A checkout elsewhere can be selected using, for example,
`--repo knowledge-compiler=/absolute/path/to/knowledge-compiler` on both commands.
Configured origin identity must match; no remote connection is made. Governor
and project checkouts cannot overlap. Outputs are confined to Governor's
`evidence/` and `state/` directories; output symlinks are rejected.

Assembly produces:

- `state/portfolio.yaml`: derived portfolio evidence, in JSON syntax (a YAML 1.2
  subset), readable with Python's `json` module without an extra dependency;
- `evidence/<packet>/manifest.json`: evaluated HEADs, status hashes, verbatim
  coordination sections, last accepted verdict/debt, triggers, bounded history,
  input hashes, capability inventory and assembly freshness;
- frozen copies of declared Governor inputs and the three authoritative status
  files, including the workflow source and templates for reconstruction;
- `GOV-DRAFT.md` and `CYCLE-DRAFT.md`: review/allocation templates with evaluated
  inputs filled in; strategic judgments remain TODO;
- `assembly-receipt.json`: hashes of the manifest and derived state;
- `freshness-check.json`: latest explicit check result when verification runs.

These files are evidence, not project coordination authority. No new review
appears in `reviews/`, and no allocation appears in `allocations/`.

## Freshness and scope

Assembly rereads evidence before completion. Verification checks HEADs,
authoritative status bytes, tracked worktree status, Governor inputs, frozen
packet bytes and derived state. Any HEAD movement is conservatively treated as
material for freshness. A mismatch returns exit code 2 and
`STALE_REVIEW_REFRESH_REQUIRED`. Missing/unreadable inputs and invalid identity
also fail closed with exit code 2. Successful verification returns exit code 0
and `FRESH_AT_CHECK_ONLY`.

Run verification immediately before representing evidence as current for owner
acceptance/freezing. A result is point-in-time and explicitly
`LOCAL_WORKTREE_ONLY`; it never claims authoritative GitHub currentness. No fetch
is used because it would mutate project Git metadata. Remote state remains
`NOT_CHECKED_OFFLINE`. A future separately bounded remote observation can be
added if the owner needs remote currentness; this implementation requires none.

Uncommitted authoritative status is deliberately captured and marked as
working-copy evidence. HEAD alone cannot establish its content. The tracked
worktree-status hash detects dirty/clean and path/status transitions, but does
not prove that every dirty source file's bytes stayed constant. Those bytes are
not read or evaluated. Untracked/private files are not scanned or retained.
No experiment result, private database, candidate profile or private recovery
artifact is automatically ingested. Reviewers must inspect any necessary
additional evidence under its own privacy/authority boundary.

File hashes detect accidental change, not malicious rewriting of both evidence
and receipts. Governor Git history supplies durable versioning after owner
review. Observation does not lock projects; concurrent changes require refresh.

## Triggers and accepted judgment

Facts include movement from a known accepted HEAD, status-hash change from a
known accepted status, divergent ancestry, and an exact prior-review quotation
manually annotated `EXPLICIT_REVIEW_REQUIRED`. Those observations can make
review due, but cannot activate project work. Constraints, next boundaries and
conditional follow-ups remain candidates. A prior follow-up is not assumed
satisfied, overdue or unresolved merely because its text exists; review must
assess it. Follow-up kinds are explicit configuration annotations, not inferred
strategic judgments.

Literal gate/recovery/work-packet text and five-or-more commits are only
`REVIEW_CANDIDATE`. Historical, conditional and prohibition text can match.
Commits are not material experiments. No model judgment, materiality scoring,
automatic gate resolution, new verdict or debt retirement occurs. Duplicate
coordination headings and contradictory text are retained for review.

GOV-004 did not record evaluated HEADs or status hashes. Its baseline values are
therefore null. The first rehearsal captures up to 100 recent commits per
project as context, labels that scope `RECENT_CONTEXT_ONLY_BASELINE_UNKNOWN`,
and never calls those commits movement since GOV-004. Once the owner separately
accepts a review with exact HEADs/hashes, manually update the configuration to
that accepted evidence and its exact follow-up quotations. Never use a rehearsal
or the latest filename as an accepted baseline. If the new accepted review's
format lacks the named project / Verdict / Strategic debt sections, stop for
owner review rather than building project-specific parsers.

## Bounds and authority

Each file/read output is limited to 256 KiB; history is limited to 100 commits
plus a truncation probe. Git subprocesses have a 15-second timeout. One assembly
performs 21 read-only Git commands for three projects with unknown baselines
(24 with known baselines); one verification performs 12. Thus the Git timeout
ceiling is 315/360 seconds for assembly and 180 for verification. No retries,
daemon, paid calls or spending occur. Unexpectedly large/unreadable status stops
for owner review. Status parsing is generic Markdown section extraction.

Git capabilities are limited to repository-root/HEAD observation, configured
origin identity reads, bounded log/ancestry reads and tracked status observation.
`GIT_OPTIONAL_LOCKS=0` prevents optional index refreshes; filesystem-monitor and
untracked-cache integration are disabled. No hooks, shell evaluation, fetch,
checkout, reset, add, commit, push, merge, diff drivers or project file writes
are called by the workflow. Tests mutate only disposable repositories under
the OS temporary directory and verify their complete trees are byte-identical
across assembly/verification.

SPEC-001 stops at owner review. The owner separately decides whether the
mechanism becomes canonical. Publishing GOV-005/CYCLE-010, promotion, project
preemption, spending and external action remain outside this implementation.
