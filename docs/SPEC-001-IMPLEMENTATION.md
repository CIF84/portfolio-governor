# SPEC-001 implementation and dogfood evidence

Recorded: 2026-10-08. Owner acceptance: **PENDING**.

Proposed implementation outcome: `PASS_MINIMUM_OPERATIONAL_GOVERNOR_EARNED`,
subject to owner review. This is an implementation assessment, not a portfolio
verdict, canonical promotion or autonomous-operation authorization. The manual
Purpose / Truth / Safety / Capital and allocation judgments remain human/LLM work.

Reviewable packet: [spec001-dogfood-20261008-v3](../evidence/spec001-dogfood-20261008-v3/manifest.json).
Derived state: [portfolio.yaml](../state/portfolio.yaml).
Usage and limitations: [OPERATIONS.md](OPERATIONS.md).

Current evidence freshness: **`STALE_REVIEW_REFRESH_REQUIRED`**. The final
snapshot passed at assembly, then OR's working-copy status changed; verification
caught that movement. Implementation review can use the preserved rehearsal.
A current governance review requires a new assembly, followed by verification.

## Implementation scope, files and architecture

The completed change implements only SPEC-001's Governor-local observation,
evidence preparation, deterministic signals and draft generation. It adds no
automatic strategic judgment or project execution capability.

| Files changed relative to the frozen main baseline | Role |
|---|---|
| `.gitignore` | Excludes Python bytecode/cache artifacts |
| `README.md`, `STATUS.md` | Usage and implementation handoff; original implementation coordination is preserved |
| `governor/__init__.py`, `governor/__main__.py`, `governor/workflow.py`, `governor/config.json` | Python entry point, bounded read-only workflow and declared input/baseline configuration |
| `tests/test_workflow.py` | Complete 25-test suite using disposable Git fixtures |
| `templates/review.md`, `templates/allocation.md` | Review/allocation drafts with evaluated inputs and owner gates |
| `state/portfolio.yaml` | Preserved derived state, explicitly stale |
| `evidence/spec001-dogfood-20261008/`, `evidence/spec001-dogfood-20261008-v2/`, `evidence/spec001-dogfood-20261008-v3/` | All original rehearsal manifests, receipts, drafts, status/input/source copies and stale checks, byte-preserved |
| `docs/OPERATIONS.md`, `docs/SPEC-001-IMPLEMENTATION.md`, `docs/spec001-authority-check.json` | Operations, implementation assessment and original live authority receipt |
| `docs/spec001-review-validation.json` | Separate publication-time test, preservation and authority verification receipt |

The exact file list is the Git diff from baseline
`07ae5c9cd3c037ffb17d9504f29163c548100ca5` to the published review commit.
Frozen top-level reviews, allocations, constitutions, protocol, project registry
and approved specification are unchanged. Copies inside evidence packets are
new snapshot files, not edits to those protected originals.

Architecture: a single standard-library CLI reads the declared configuration,
validates three distinct nonoverlapping repository identities, extracts generic
Markdown coordination sections, captures HEAD/status/worktree-status and bounded
history, and carries forward accepted review judgments with provenance. It then
rereads the evaluated inputs, writes the Governor-local manifest/state and
evidence copies, and fills two drafts. The separate `verify` command compares
input and packet/state hashes against assembly receipts and marks corresponding
derived state stale on mismatch. There is no database, network runtime, model
provider, background process, UI, scheduler or project command executor.

## Deliverables

| Requirement | Implementation and evidence |
|---|---|
| D1 — derived state | Repository identity, constitution/status paths, exact evaluated HEAD/status hashes, verbatim gate/state sections, accepted GOV-004/CYCLE-009 pointers, accepted verdict/debt, triggers and freshness metadata in `state/portfolio.yaml`. State is observation, never project authority. |
| D2 — evidence assembly | `python3 -m governor assemble --packet <new-id>` freezes declared local inputs, status files, workflow source/templates and bounded Git history into a Governor-local packet. Unknown prior HEADs are explicit; recent context is never mislabeled as since-review history. |
| D3 — freshness | Assembly rereads project inputs. `verify` checks HEAD/status/worktree-status, Governor input hashes, packet integrity and derived state. Mismatch returns exit code 2, `STALE_REVIEW_REFRESH_REQUIRED`, and marks corresponding derived state stale. |
| D4 — triggers | Known baseline movement, ancestry divergence, known status hash transition and manually annotated explicit review requirements are deterministic observations. Conditional follow-up, gate/recovery/work-packet text and commit materiality remain `REVIEW_CANDIDATE`. |
| D5 — templates | `templates/review.md` and `templates/allocation.md`; drafts preserve evaluated inputs, Constitution version, prior review/allocation, four lenses, debt/trajectory/verdict, Roman/machine queues, capital findings, freshness, preemption and owner gates. |
| D6 — authority | Full-tree byte equality in disposable project fixtures; live before/after HEAD/status/tracked-status/index equality and capability inventory in [authority check](spec001-authority-check.json). No governed mutation capability is used. |
| D7 — dogfood | Current local repositories captured in v3, compared below with frozen GOV-004/CYCLE-009. No GOV-005 or CYCLE-010 was published. |

## Rehearsal evaluated state

At 11:31:33 Europe/Prague, v3 verified `FRESH_AT_CHECK_ONLY`. This is a
point-in-time local check; authoritative remote GitHub state remains unverified.
At 11:33:19 Europe/Prague, a subsequent check detected OR's changed status and
tracked-worktree status and failed closed. This snapshot remains historical
rehearsal evidence; assemble a new packet before accepting a current review.
The packet contains exact status
SHA-256 values as well as these HEADs:

| Project | Evaluated HEAD | Authoritative status | Tracked working-copy changes |
|---|---|---|---|
| Knowledge Compiler | `7b83d8d4361d02dfbe1c8b5c0a7ae0d79fd4758a` | `STATUS.md` | No; untracked implementation files are not evaluated |
| Opportunity Radar | `69dececcfa78276731a07fabab63e504cd7392c5` | `docs/STATUS.md` | Yes |
| Asymmetry Engine | `caa0a322adcd90ebc2f90830d866afab7cdbe95d` | `STATUS.md` | Yes |

Accepted strategic judgments and debt are copied from GOV-004 and labeled
`LAST_ACCEPTED_NOT_REEVALUATED`. Current trigger state for all three is
`REVIEW_CANDIDATE`; no since-GOV-004 movement can be proven without its missing
HEAD/status baseline. The workflow does not invent that baseline from dates,
current HEADs or the apparent latest work-packet number.

## Comparison with GOV-004 / CYCLE-009

Added evidence:

- Exact repository HEADs, authoritative status paths, status-byte hashes,
  timestamps, captured input/source hashes, working-copy divergence warnings,
  bounded commit context and explicit check receipts. GOV-004 recorded no HEADs.
- KC's current approved BENCH-001 pointer and owner gate are directly visible.
  Its later prohibition section also says there is no active approved packet;
  the full status preserves that contradiction for reviewer resolution.
- OR's latest status records Attempt 003 as aborted after three source failures,
  followed by bounded local repairs/readiness awaiting owner review. Older gate
  sections still prohibit Attempt 003; the workflow preserves rather than
  resolves historical versus latest coordination text.
- AE's refreshed status records that independent review has not approved Q and
  that C04-only admission remediation 059R is active. R1 wedge consequence and
  R2 qualified-audience access are now explicit uncertainties. That differs from
  GOV-004's expectation that Experiment 059 search was the next work; it does
  not by itself establish a new Governor verdict or launch authority.

Omitted from automatic evaluation:

- Independent reading/adjudication of experiment results, architecture audit,
  source evidence, economic treatment, test reports and actual durability
  artifacts. Existing GOV-004/CYCLE-009 analysis is retained verbatim, not newly
  verified by copying it. Status claims are observations, not independent proof.
- Private candidate intelligence, databases, private recovery artifacts,
  untracked experiment/implementation bytes and live source/provider calls.
  Authoritative status is the sole governed-file input. No private paths or
  candidate records are newly discovered or copied by a filesystem scan.
- Exact material experiments since GOV-004, because no evaluated HEAD baseline
  exists. The recent-context cap is visible when truncated.

Freshness risks caught:

- The [first rehearsal's check](../evidence/spec001-dogfood-20261008/freshness-check.json)
  actually failed when AE's HEAD, status hash and tracked worktree status changed
  during this implementation session. Result: `STALE_REVIEW_REFRESH_REQUIRED`.
  Its frozen evidence is retained, and current derived state was refreshed using
  a new packet. The workflow performed no action on AE in response.
- v2 is also retained as superseded evidence: verification rejects it after
  changes to the Governor workflow/configuration. The final code/configuration
  are captured in v3. Input-version movement cannot silently certify old state.
- The [v3 check](../evidence/spec001-dogfood-20261008-v3/freshness-check.json)
  caught OR status movement without a HEAD change after its initial successful
  check. Current derived state is explicitly stale. No repeated refresh loop or
  attempt to lock/preempt another project's work was introduced.
- Tests separately demonstrate same-HEAD uncommitted status changes, missing
  evidence, changed Constitution, changed derived state, changed frozen packet,
  assembly-time movement and divergent baseline ancestry failing closed.

Repeated manual steps eliminated: locate three declared checkouts/status files;
collect their exact HEADs and bounded history; gather Constitution/project
constitutions and accepted review/allocation; copy status and baseline evidence;
carry forward accepted debt/verdict with provenance; identify candidate trigger
text; fill evaluated-input tables in both drafts; and check input consistency.
One assembly command performs these steps, and one verification command checks
them again. The final measured assembly took 0.314 seconds; assembly plus
verification took 0.477 seconds on this machine (21 + 12 read-only Git commands).
No manual timing comparison or economic-savings estimate was performed.

False-trigger risks: KC's benchmark owner gate is already reflected in GOV-004;
OR recovery/aborted text mixes current and historical evidence; prohibition text
can mention a gate or packet without granting authority; conditional follow-up
does not establish that its condition happened. Those hits remain candidates.
Five commits, when a baseline is known, are never counted as five experiments.

Unresolved judgment: whether AE's remediation closes the economic admission
gaps; whether OR's repairs justify another separately authorized complete
candidate; BENCH-001 readiness/fairness; whether any strategic debt has actually
decreased; and whether the Roman/machine allocation should change. The workflow
has no authority or semantic evaluator that decides those questions.

## Validation and authority

`python3 -m unittest discover -s tests -v`: **25 passed**. The suite uses isolated
temporary Git repositories. It verifies stale/missing/tampered evidence,
unknown/divergent history, trigger classification, reconstruction, evaluated
templates, CLI exit status, repository identity, read/write containment and
full governed-fixture tree byte equality including `.git`.

Publication validation reran the unchanged full suite:

```text
Command: python3 -m unittest discover -s tests -v
Ran 25 tests in 13.795s
OK
Exit code: 0
```

The publication-time receipt records the Python/Git versions and hashes of all
89 original files other than this explicitly expanded report. Code, tests,
configuration, templates, derived state and every original evidence byte were
preserved. Tests generated only ignored Governor bytecode and temporary fixtures;
no live rehearsal command was rerun, so stale-check receipts were not overwritten.

External capabilities used during implementation and rehearsal:

| Capability | Scope / effect |
|---|---|
| Local shell / Python standard library | Governor-local files, validation, and disposable temporary fixtures only |
| Governed filesystem reads | Declared authoritative status; the authority measurement also reads each Git index |
| Read-only Git | Repository root, configured origin identity, HEAD, bounded history/ancestry and tracked status; initial inspection also read untracked names |
| Governor Git inspection | Status/log/diff and protected-baseline comparison; no publication |
| Network / GitHub / model/provider / messaging / spend | None |
| Governed mutation / packet activation / preemption / external action | None |

The live authority receipt shows unchanged evaluated HEADs, status bytes,
tracked-status signals and Git indices during the final rehearsal. The test
demonstrates complete byte equality in fixtures; the live receipt does not claim
global surveillance of private/untracked files or deny concurrent work by other
actors. Optional Git index writes and filesystem-monitor integration are disabled.
Constitution, project constitutions, historical reviews/allocations and the
approved specification remain unchanged.

Acceptance evidence covers all ten SPEC-001 criteria: read-only observation,
explicit evaluated inputs, stale failure, reconstructable state, candid trigger
classification, complete templates, no project mutations or consequential
authority, a real stale-state catch, and a small standard-library workflow with
no database/UI/daemon/orchestration. Limits remain visible rather than being
hidden behind an automated verdict.

## Acceptance criteria and remaining review questions

| SPEC-001 criterion | Evidence for independent assessment |
|---|---|
| 1 — governed evidence read-only | Fixed Git read callers, output containment, full fixture-tree equality and live authority receipts |
| 2 — HEADs/status explicit | All three manifest entries, SHA-256 status values and populated draft tables |
| 3 — stale state fails closed | Real AE/OR movement receipts; stale/missing/tampered input tests and CLI exit-code test |
| 4 — state reconstructable | Captured configuration/source/inputs, accepted baseline pointers and reconstruction test |
| 5 — useful candid trigger detection | Known baseline/ancestry tests, explicit prior-review requirement test, conditional/literal candidate tests and null GOV-004 baseline |
| 6 — proven governance dimensions | Template coverage test and complete four-lens, trajectory/debt/verdict, attention/machine/capital/preemption fields |
| 7 — no governed mutation | Fixture byte equality, selected live metadata/index equality and no governed mutation command used |
| 8 — no consequential authority | Two observation commands only; no activation, preemption, spend, external action or governance publication command |
| 9 — less reconstruction/freshness risk | Single-command evidence assembly and actual live stale-state catches; no claim of measured manual time savings |
| 10 — simpler than manual problem | One standard-library module/configuration, two commands, files/Git and no service/database/orchestration |

These are evidence for the proposed outcome, not independent owner acceptance.
Open questions include trigger usefulness in repeated real reviews, treatment of
missing accepted HEAD/status baselines, conflicting historical gate text and the
manual economic/strategic judgments listed above. Local checks do not establish
remote project currentness or the content of all dirty/untracked/private files.
Hashes/receipts do not defend against an actor rewriting both. Output writes are
not a transaction across the entire packet/state, and aggregate manifest size is
not preflighted against the per-read 256 KiB bound; large-input and interrupted or
concurrent-output behavior remain review questions. No implementation change was
made to address those questions as part of review publication.

## Dedicated review publication

Owner authorization is limited to publication of the completed implementation
and preserved evidence to `https://github.com/CIF84/portfolio-governor.git`,
review ref `refs/heads/codex/spec-001-owner-review`. The pre-publication remote
`main` baseline is `07ae5c9cd3c037ffb17d9504f29163c548100ca5`, equal to local
`main`. The publication agent checks remote review-tip equality and unchanged
remote `main` after pushing and reports the exact immutable endpoint separately;
a commit cannot contain its own SHA.

Publication uses Governor-local branch/commit operations, authenticated remote
ref reads and one explicit review-ref push. This human-authorized publication
adds no network or mutation capability to the Governor implementation and touches
no governed project. Existing evidence and STATUS are preserved as implementation
handoff records; STATUS's original `main` field is not a promotion declaration.

An independent reviewer should fetch the review ref into a separate clone,
verify its exact SHA against the endpoint supplied in the publication handoff,
check out that SHA detached, read SPEC-001 and this report, inspect the baseline
diff, and rerun the full suite. Do not run `assemble`/`verify` in the frozen review
checkout because they write evidence/state; rehearse in a disposable copy if
needed. Return findings against all ten acceptance criteria, authority boundaries,
stale behavior and limitations. Do not modify frozen evidence, publish a new
Governor verdict/allocation, or merge/push/promote `main` as part of review.

## Owner review boundary

Review this implementation, final packet, tests and authority receipt. Owner
acceptance separately decides canonical use and any future automation. No
Governor verdict, project reprioritization, budget increase, spending, remote
publication, deployment or autonomous operation is authorized by passing tests.

Publishing this review branch does not approve the proposed PASS outcome. A
successful independent review also does not authorize promotion: the owner must
explicitly approve publication/promotion of the exact reviewed endpoint.
