# Opportunity Radar — Current Status

This is the authoritative repository handoff. Operational counts are derived by
`opportunity-radar-status`; this file records current direction, frozen policy,
and the next approved work packet.

## Current approved work packet

```text
specs/phase4/SPEC-025-epoch2-bootstrap-and-kraken-ashby.md
```

Status: `APPROVED_FOR_IMPLEMENTATION`.

Latest bounded continuation (2026-10-08):
`LOCAL_REPAIRS_READINESS_PASS_AWAITING_OWNER_REVIEW`. Owner authorized only the
Kiwi/Schneider/Keboola diagnosis and local generic repair/readiness. Attempt 003
is privately classified `ABORTED_BASELINE_THREE_SOURCE_FAILURES`, byte-unchanged
at `a003ac6d34bc8d498f9d00930a5d1385542b9cd6a48d496e9fe50e81a0a4155a`;
it cannot be resumed, migrated, overwritten or used for reuse/lifecycle.
Kiwi's secondary detail UUID incorrectly replaced URL identity; locally repaired
generic extraction passes 5/5. Schneider relevance pagination repeats two exact
boundary rows; source-advertised date sorting plus strict generic duplicate/count
guards passes 3,605 unique identities and an empty terminal probe. Keboola's stale
title selector hides two existing Lever jobs; the unfiltered public JSON feed
and complete section projection pass 2/2. These are local source-window findings,
not promoted runtime policy or an atomic inventory guarantee.
One hundred bounded GETs; zero operational/manifest writes, models or actions.
All surviving pre-existing evidence remains byte-identical; durability unchanged.
No Attempt 004, bootstrap continuation, Snapshot 2, commit/push or canonicalization
is authorized. Stop for review. See `docs/remaining_source_diagnosis.md` and
`output/epoch2_recovery/spec025-remaining-sources-20261008/aggregate_summary.json`.

Previous execution (2026-10-08): `ATTEMPT_003_COLLECTED_PARTIAL_AWAITING_OWNER_REVIEW`.
All 23 employers / 24 required surfaces were attempted: 20 complete baseline
passes and three failures. Kiwi has complete inventory but five identity-guard
detail failures; Schneider inventory failed duplicate-identity validation;
Keboola failed unvalidated-empty extraction. Twenty-two required inventories
pass; two fail. No employer/surface was dropped or waived.
The private schema-4 candidate contains 15,488 first-observed identities and
3,744 fresh details (3,749 attempts / five failures; 423 local / 3,326 network
detail operations). Integrity/foreign keys and partial-state reconciliation pass;
full baseline fails. Zero imports/reuse/cross-gap closures/changes/models/actions.
SAP passes 755 legacy + 125 public feed = 880 namespaced postings. EY converges
on pair 1/2 at 8,754 identities each, delta 0/0, 706 requests / 233.900 seconds;
all 2,102 selected details succeed. Kraken has 83 identities and 33 jobs preserving
explicit Czech Republic evidence. Overall 4,361 HTTP attempts / 1,423.186 seconds.
Attempt 003 remains noncanonical diagnostic evidence, run `PARTIAL`; it was not
registered as future canonical state. The primary manifest is byte-unchanged
and durability stays `BLOCKED`. All 4,021 pre-existing private/local files match
their before-run hashes, including both aborted candidates and the historical DB.
Stop for owner review of the three failures. No repair, new attempt, further
source calls, Snapshot #2 or canonicalization is authorized by this result.
Evidence: `output/epoch2_recovery/spec025-attempt003-20261008/aggregate_summary.json`;
handoff: `docs/epoch2_recovery_handoff.md`.

Owner continuation (2026-10-08): `ATTEMPT_003_AUTHORIZED` on canonical
base `69dececcfa78276731a07fabab63e504cd7392c5`. Reconcile/test bootstrap remnants,
then collect all 23 employers / 24 required surfaces into a new empty private
schema-4 candidate, with isolated failures and no historical/aborted imports.
Continue independent collection after failure, but fail full baseline and
canonicalization unless every required employer/surface and integrity gate passes.
Successful full validation alone permits private candidate registration requiring
new durability verification; failure preserves diagnostic evidence without
manifest changes. Stop before Snapshot #2/canonicalization, with zero models or
application actions and no commit/push. Earlier execution/readiness notices below
describe their historical authority; they do not override this continuation.

Phase A status: `IMPLEMENTED_OWNER_REVIEWED_ACCEPTED` (2026-10-07).
The independently approved implementation `ee2150c04846d200eee0d621c335297d6496cfeb`
was fast-forwarded from `review/spec-025-ashby-kraken-readiness` into `main`
without implementation changes.

SAP source-contract status: `IMPLEMENTED_OWNER_REVIEWED_ACCEPTED` (2026-10-07).
Approved implementation `27967d903f0cec2f0cee737a43f4301ec5628348` was
fast-forwarded unchanged from `review/spec-025-multisurface-source-contract`
into `main`; schema 4 source-surface identity is accepted.
Execution state: `ATTEMPT_002_STOPPED_SOURCE_COMPLETENESS_GATE`.
Latest continuation: `EY_ACTIVATION_READINESS_IMPLEMENTED_OWNER_REVIEWED_ACCEPTED` (2026-10-08).
Owner authority separately activates the accepted mechanism for EY only using
three attempts, 1,100 requests and 360 seconds, then validates one bounded
production listing invocation. No other source is activated; no new epoch
attempt, details, operational/manifest writes or durability transition is
authorized. See `docs/ey_convergence_production_readiness.md` (DR-034).
Executed result: `CONVERGENCE_VALIDATED`, exact pair 1/2, 8,721 advertised/unique
identities on both passes, zero identity delta and stable boundaries. Total
702 requests / 222.598 seconds; traversal 3 not started. All existing guards
passed. Protected hashes and all 2,601 pre-existing private/local files are
unchanged. Full offline suite: 568 passed, 8 skipped, 23 deselected. Owner review
accepts EY activation/readiness; commit/push only the associated safe change set,
then stop. No attempt 003, details, operational/manifest write, durability change
or source/model/application action follows.

Preserved mechanism-acceptance and experimental baseline:
The owner-authorized bounded experiment used the immutable October 7 diagnosis
as its baseline. Two consecutive independently reconciled EY traversals each
returned 8,637 identities with the same advertised total and stable immediate
boundary rechecks; full identity-set delta was zero. It stopped after pair 1/2,
696 listing requests and 201.334 seconds, before a third traversal. The pure
experimental validator passed 25 focused tests; the full offline suite passed
520 tests (8 skipped, 23 live tests deselected). All 1,185 pre-existing private/
local files and both aborted candidates remain byte-identical. No operational/
manifest writes, detail/model calls or runtime policy promotion occurred.
See `docs/mutable_inventory_convergence_validation.md` and its sanitized receipt.
Independent review is owner-approved, including `5bad455a74ccd1ecbe6534304caadd21dab76cf6`. The
review branch was fast-forwarded unchanged into `main`; the generic opt-in
mechanism is accepted, not source activation. Existing single-pass guards,
exact adjacent total/set equality and stable boundaries remain mandatory.
Elapsed time is an evidence-admission boundary, with immediate post-response
checks; retries/redirects are disabled during convergence and transport restored.
At that closure, source activation and any new candidate strategy remained
separate gates and no configured source was activated. The subsequent EY-only
authorization above permits bounded listing readiness, not a new candidate.
Durability remains `BLOCKED`; no model or operational writes.

Preserved October 7 diagnosis:
The owner permanently classified attempt 002 `ABORTED_SOURCE_COMPLETENESS_EY`;
its original bytes/metadata remain unchanged. Two bounded listing-only traversals
reproduced public inventory-view churn (8,618 to 8,589); later boundary probes
reported 8,619 then 8,589. Totals and native identity sets changed, with no numeric
range gaps/duplicates or demonstrated parser error. Actual publication mutation
versus backend/index inconsistency remains unresolved. The existing production
guard correctly rejects the unstable pass. At that historical gate the generic
bounded convergence contract was proposed, not implemented/promoted. Total requests: 705; zero details, SQLite/
manifest writes or model calls. See `docs/ey_mutable_inventory_diagnosis.md`.
The owner has accepted the fresh-candidate strategy on canonical base
`08d8fc97aadd68dbff2cec3aa1e4f0b556c57d70`. Attempt 001 is permanently
`ABORTED_EPOCH2_BOOTSTRAP_PRE_SCHEMA4` / `OPERATIONAL_EPOCH_2_ATTEMPT_001`:
preserve its bytes and never migrate, resume, import or use it operationally.
The authorized fresh `OPERATIONAL_EPOCH_2_ATTEMPT_002` starts empty in schema 4
at a distinct nonexistent external path, with no historical imports or detail
reuse. Reconciled bootstrap machinery passed 484 offline tests before live work.
The fresh run stopped at EY: `CountMismatchError`, advertised total changed
during pagination. Eleven employers / twelve required surfaces passed; one
employer / surface failed; eleven employers / surfaces were not attempted.
Attempt 002 is `PARTIAL`, with 3,692 fresh identities and 1,194 successful details.
SAP passed both required surfaces (758 legacy + 110 public feed = 868 postings);
Kraken passed with 85 identities and 34 jobs preserving Czech Republic evidence.
Local integrity/reconciliation passes; the full 23-employer / 24-surface baseline
does not. The partial database is noncanonical and must not be resumed without
separate authority. The primary manifest is unchanged and its gate is `BLOCKED`;
attempt 002 was not registered because full validation did not pass.
This continuation authorizes no model calls, application actions, commit/push,
backup or canonicalization. See the latest continuation in SPEC-025.
Generic Ashby/Kraken readiness passed with 86 stable unique identities, 86 local
detail normalizations, 51 multi-location jobs and 34 jobs preserving explicit
Czech Republic evidence. At Phase A acceptance the portfolio was 23 sources /
eight families; the accepted SAP continuation now represents 23 employers /
24 required surfaces / nine adapter families.
The owner-selected external private root now contains nine byte-verified copies
and the rewritten canonical durability manifest. All seven human-irreplaceable
artifacts and the historical database retain Snapshot #1 restore provenance.
Read-only Phase B preflight passes with no blockers; all old copies remain
byte-identical recovery duplicates. Private paths are recorded only privately.
Phase B is owner-reviewed/accepted. Historically, under C–F-only authorization,
an empty schema-v3 `OPERATIONAL_EPOCH_2` candidate was created. Bootstrap stopped
immediately at SAP's unvalidated empty extraction: ten sources passed, one failed,
and twelve were not attempted. The partial candidate contains 2,794 identities
and 1,137 fresh detailed observations; SQLite integrity/reconciliation and zero
cross-gap closure/change checks pass, but the full baseline gate fails.
The candidate is not canonical, and its required new recovery evidence makes
the durability gate `BLOCKED`. No historical/candidate/semantic state was imported.
Required handoff:
`docs/epoch2_recovery_handoff.md`.

SPEC-025 remains active. Convergence mechanism review is accepted, EY-only
declarative activation/readiness is separately authorized, and any fresh-candidate
continuation remains gated. No new bootstrap is authorized by this continuation.
Owner-authorized bounded SAP diagnosis (2026-10-07) found a migration redirect:
the configured legacy Czech-category URL now serves a new Next.js listing, while
SAP explicitly retains jobs on its old SuccessFactors site. This is not a confirmed
empty inventory. A generic listing-route pagination repair was locally tested.
At that diagnosis, SAP production configuration remained unchanged because
legacy-only coverage was unproven. Eight public HTTP requests, zero details/model/operational writes;
the partial candidate and all protected evidence remain byte-identical.
Diagnosis receipt: `output/epoch2_recovery/spec025-sap-diagnosis-20261007/aggregate_summary.json`.
The subsequent owner-authorized coverage investigation reproduced current website
counts 94 / 756 and found that the new English website omits 12 public feed postings.
Unfiltered new publishing feed 106 + complete retained-session legacy 756 yields
862 exact posting identities, without a proven shared cross-system requisition key.
The failed fresh-session legacy probe is retained as incomplete evidence. Generic
multi-surface composition and stronger source-count guards were proposed at that gate.
See `docs/sap_complete_coverage_validation.md` and its sanitized receipt. Eighty-eight
source HTTP requests, zero operational writes/model calls; all prior evidence remains
unchanged. Its implementation-review gate and fresh-strategy owner gate have
since passed. The failed attempt was never resumed; attempt 002 is a fresh baseline.
The subsequent owner-authorized source-contract implementation/readiness now passes:
legacy SuccessFactors 756/756, unfiltered SmartRecruiters 106/106, union 862 exact
namespaced postings, three normalized detail probes and one ID-route URL probe.
Thirty-seven HTTP requests, zero retries/operational writes/model calls. The generic
pagination repair passes both configured pagination modes and retained-session
regressions. Schema 4 is owner-reviewed/accepted for surface-scoped identity and
JSON surface receipts; the protected partial schema-3 candidate is unchanged at
`63cb7e3924da701fe2ac6bb318f6a03766eedb25fdd0af31aeaf44b3ee7d4b4c`.
It is **aborted evidence**, not a migration/resumption target. SAP's required
surfaces are legacy SuccessFactors plus the unfiltered SmartRecruiters public
feed; real-world cross-system opportunity overlap remains unresolved. No
requisition/title/location fuzzy deduplication is authorized. At source-contract
closure, fresh-strategy authority was still pending; it is now separately granted
for attempt 002 only, not by source readiness itself.
At source-contract closure durability remained `BLOCKED` by attempt 001.
The approved fresh strategy allowed in-memory preflight supersession only;
attempt 002 failed, so no primary-manifest supersession or candidate registration
was performed. No old-candidate migration/resumption or source removal is authorized.
Do not weaken/drop a source, rerun against either existing candidate, create Snapshot #2,
canonicalize, or make further source/model calls without a bounded continuation.
Phase G/H were not entered. Historical/private evidence and Phase B receipts
remain unchanged; the prior external manifest is retained byte-for-byte.

SPEC-025 is the only active implementation packet. It first adds and validates
a generic Ashby source contract with Kraken as a declarative source, then may
establish an Operational Epoch 2 candidate database from complete fresh
inventories after all preflight gates pass. Kraken source readiness is a hard
precondition: Epoch 2 must not knowingly bootstrap without Kraken coverage.

SPEC-025 explicitly authorizes the bounded live-source calls and operational
writes described by its gates. It authorizes zero semantic/model calls and zero
application actions. Epoch 2 must preserve the permanent unobserved gap and
must infer no lifecycle continuity, closure, or change across it. A successfully
bootstrapped Epoch 2 database remains non-canonical until its integrity,
completeness, and accepted off-device backup/restore evidence pass independent
review.

## Latest closed work packet

```text
specs/phase4/SPEC-024-private-state-durability.md
```

Status: `IMPLEMENTED_OWNER_REVIEWED_ACCEPTED`.

SPEC-024's durability mechanism and encrypted multi-artifact container extension
are canonical. Snapshot #1 verifies all nine inventoried artifacts, including
7/7 HUMAN_IRREPLACEABLE and the HISTORICAL_READ_ONLY database; the durability
gate passed for the nine surviving artifacts. That accepted Snapshot #1 evidence
is unchanged. SPEC-025 has since created a partial non-canonical Epoch 2 candidate;
its additional required artifact is `NOT_DURABLE`, so the current gate is `BLOCKED`.

SPEC-023 was independently reviewed and owner-accepted on 2026-10-06. The
private candidate boundary in
`specs/phase4/SPEC-023-private-candidate-boundary.md` is now canonical:
tracked candidate profiles are synthetic, real candidate intelligence remains
outside tracked Git, and candidate-relative operational workflows fail closed
without explicit private candidate selection. This acceptance authorizes no
additional runtime behavior, semantic calls, Git-history rewrite, or subsequent
work packet.

The SPEC-023 merge transition caused a confirmed operational-state loss. The
former canonical SQLite with SHA-256 `a07d5300...` is classified
`LOST_OPERATIONAL_STATE`; its bytes are unavailable. The recovered older
`66dba4...` database is `HISTORICAL_READ_ONLY`: it is not canonical/current,
must never drive closure, and must never be placed at the operational database
path. Human judgments and frozen experiment evidence survived and remain
authoritative. Lifecycle continuity across the missing interval is unknown and
must not be synthesized. Future recovery requires a separately authorized new
operational epoch.

SPEC-022 was owner-reviewed and accepted after commit
`27565da3ecf5be4944b1a42b3009da2374429832`. Architecture B — credential
compatibility separated from capability stretch — is accepted as the correct
architectural boundary. Its corrected stretch behavior remains shadow/diagnostic;
no runtime stretch, ranking, recommendation, filtering, or semantic-allocation
promotion is authorized by that acceptance.

Implementation/operations agents must follow this pointer rather than infer work
from file recency. Before starting, explicitly fetch `origin` and verify the local
`origin/main` tracking ref matches the authoritative GitHub `main` branch. Intentionally
retained local operational/private evidence is not itself an error; unexplained
code/config divergence is.

The development authority boundary remains:

- agents may inspect, analyze, implement, validate, and perform explicitly approved bounded internal operations;
- implementation changes remain uncommitted while awaiting human/ChatGPT review;
- after explicit approval, the implementation agent may commit and push;
- humans approve decisions and promotion boundaries rather than perform Git plumbing manually;
- repository-safe aggregate evidence may be tracked, while detailed candidate- and human-judgment-derived evidence remains private/local unless explicitly authorized for disclosure.

## Mission

Monitor relevant public employer vacancies, maintain trustworthy lifecycle state,
and explain which active opportunities deserve a candidate's attention.

## Current phase

Phases 1–3 are implemented. Phase 4 has validated market routing, clustering,
preferences, source breadth, semantic compute-worthiness, and a diagnostic stretch
evidence boundary. Runtime stretch/rejection remains intentionally unpromoted.

Frozen recent milestones:

- SPEC-013 source portfolio audit: `a4ebba825e80256ad55ed6bfcaf973a2df37d413`
- SPEC-014 Wave A preflight: `11e000825e339de8c772d5bd7a66e2567469f1b2`
- SPEC-015 production onboarding: `541685ce40e959a66d2ec443b6ef748190713bb1`
- SPEC-016 nested feeds + Mews: `556fd7aec5d77874f56d7a5b5137a06a75fbfbca`
- SPEC-017 partial-geography semantics: `1871a082874f27db606796fc06e348fbee71776c`
- SPEC-018 candidate direction: `34fdd1b601309a025ec72af6a4275f1dcfc72dde`
- SPEC-019 stretch evidence audit: `559144258608825bdbc746691c37da041bb2fc82`
- SPEC-020 terminated credential validation: `676647bb24a7f88b23c334d74e904cd8444f840c`

SPEC-021 is a completed and committed protocol identity. It redesigned credential
validation around immutable captured evidence so later source disappearance does
not automatically invalidate a trustworthy observation. Its 36-case human review
and diagnostic replay are complete; no runtime rule was promoted.

SPEC-022 has now been executed in shadow only. Credential compatibility is a
separate evidence object and shadow stretch-v2 removes generic academic
credential absence as an independent capability-distance reason. Production
stretch/ranking/recommendation behavior remains frozen. Owner review accepted the
architectural separation and diagnostic evidence, but explicitly did not promote
shadow stretch-v2 into runtime policy.

## SPEC-022 shadow result

The exact 144 SPEC-019 degree-driven cases were reconstructed by observation
identity and joined to immutable SPEC-021 evidence. Their shadow transitions are:

```text
EXCESSIVE_STRETCH -> CURRENT_FIT          2
EXCESSIVE_STRETCH -> MANAGEABLE_STRETCH  14
EXCESSIVE_STRETCH -> UNRESOLVED          128
EXCESSIVE_STRETCH -> EXCESSIVE_STRETCH     0
```

`MANDATORY_CREDENTIAL_ABSENT` appears zero times in shadow capability reasons.
The 128 unresolved cases are the intended conservative result of refusing to
invent independent capability gaps. Across the full frozen 3,935-case SPEC-019
corpus, excessive classifications fall from 171 to 27; those 27 are supported
by pre-existing independent professional-depth rules. All eight safety gates
pass, all three frozen SPEC-019 WORTH cases remain protected, and all six
SPEC-021 strong/partial-substitution cases avoid degree-only excessive stretch.
The 144-case potential deeper-reasoning ceiling is 142 calls / about $0.3762,
with no compatible cache hits in this frozen snapshot. This is a diagnostic
ceiling, not authorized spend.

## SPEC-019 diagnostic result

Frozen 60-item sample:

```text
CURRENT_FIT          7
MANAGEABLE_STRETCH  24
EXCESSIVE_STRETCH    9
UNRESOLVED           20
```

Safety/validation result:

- human WORTH protection: 3/3;
- excessive-stretch directional precision: 100%;
- human-evident excessive coverage: 39.1%;
- market-only false excessive: 0;
- preference-only false excessive: 0.

Current-corpus diagnostic replay:

```text
clusters              3935
CURRENT_FIT            191
MANAGEABLE_STRETCH     281
EXCESSIVE_STRETCH      171
UNRESOLVED            3292
```

The critical finding is that 144 of 171 current-corpus excessive results were driven
by mandatory-degree evidence. This concentration is too large to promote runtime
stretch semantics without better credential reasoning.

## SPEC-020 terminal result

SPEC-020 is permanently frozen as `TERMINATED_SOURCE_DECAY_CONFOUNDED` after
20/50 reviews.

```text
reviewed                          20
INVALID_OR_STALE_EVIDENCE        12
substantively interpretable       8
HARD_CREDENTIAL                   8
EXPERIENCE_PLAUSIBLY_SUBSTITUTES  6
DEGREE_GAP_DECISIVE               2
```

These are exploratory observations only, not population estimates or validated
rule precision. Preferred, equivalent-experience, generic, and ambiguous credential
semantics were not validated. Human notes repeatedly distinguished independent
capability/domain gaps from the formal degree gap.

SPEC-020's frozen sample/reserves, 20 private append-only judgments, and detailed
evidence remain unchanged. It must not be resumed or silently resampled.

## Core lesson motivating SPEC-021

A trustworthy observation should remain analyzable after the external source changes.

```text
PUBLIC SOURCE AT T0
        ↓
exact evidence + provenance + timestamp + hash
        ↓
IMMUTABLE EVIDENCE SNAPSHOT
        ↓
human / AI reasoning later

source disappears at T1
        ≠
evidence automatically invalid
```

Source currentness and evidence validity are separate objects.

## SPEC-021 objective

SPEC-021 validates the credential-reasoning **rule space**, not population prevalence.
It should deliberately cover semantic diversity rather than reproduce the employer-
balanced 50-case design that failed under source decay.

Target classes include:

- explicit hard degree requirements;
- degree-or-equivalent-experience wording;
- preferred/ideal/desirable degree wording;
- mixed mandatory/preferred context;
- generic/template credential mentions;
- ambiguous wording;
- constitutive/regulated credential controls where available;
- hard wording with strong experiential substitute;
- hard wording with weak/no experiential substitute;
- cases where an independent capability/domain gap is more consequential than the degree.

Rare semantic classes should be intentionally oversampled.

## SPEC-021 preparation result

The zero-call, read-only v2 preparation is frozen locally as:

```text
spec021-credential-evidence-preparation-20260916-v2
```

It searched 4,514 detailed observation rows covering 4,164 job identities and
4,206 distinct job/content versions, including 42 historical versions. It
reconstructed 1,762 valid immutable evidence snapshots. Current source
availability was deliberately not checked; all snapshots retain
`SOURCE_CURRENTNESS_NOT_CHECKED` independently of evidence validity.

The proposed review set has 36 cases plus 14 same-class invalid-capture
reserves:

```text
EXPLICIT_HARD                         6
DEGREE_OR_EQUIVALENT_EXPERIENCE       6
PREFERRED_OR_IDEAL                    5
MIXED_MANDATORY_PREFERRED             5
GENERIC_OR_TEMPLATE                   5
AMBIGUOUS                             5
CONSTITUTIVE_OR_REGULATED             4
```

Seventeen employers are represented. Constitutive/regulated evidence is rare
and concentrated: three selected controls come from EY and one from Johnson &
Johnson. That is an explicit semantic-coverage limitation, not a prevalence
claim. The private manifest, blind packet, append-only judgments, and detailed
result are Git-ignored. Only sanitized aggregate receipts are repository-safe.

## SPEC-021 completed diagnostic result

The deliberately class-oversampled review completed at 36/36. It produced 22
`HARD_CREDENTIAL`, 11 `DEGREE_OR_EQUIVALENT_EXPERIENCE`, and three
`PREFERRED_CREDENTIAL` interpretations. Experiential substitution was strong in
one case, partial in five, absent in 23, and constitutive/non-substitutable in
seven. Independent capability gaps were recorded in 34/36 cases.

These are reasoning-coverage proportions, not population-prevalence estimates.
The result supports separating credential compatibility from capability stretch
(Architecture B), with constitutive-only hard treatment (Architecture C) as the
narrowest candidate for any future deterministic rule. Neither architecture is
promoted. The deterministic SPEC-019 replay preserves the verified 144-case
identity and reports only bounded diagnostic movement and call ceilings.

Repository-safe result:

```text
output/credential_evidence_validation/
  spec021-credential-evidence-preparation-20260916-v2/aggregate_result.json
```

## Improved human questions

Question A — captured credential semantics:

```text
HARD_CREDENTIAL
DEGREE_OR_EQUIVALENT_EXPERIENCE
PREFERRED_CREDENTIAL
GENERIC_OR_NONDECISIVE_CREDENTIAL
AMBIGUOUS_CREDENTIAL
EVIDENCE_CAPTURE_INVALID
```

Question B — experiential substitution:

```text
EXPERIENCE_STRONGLY_SUBSTITUTES
EXPERIENCE_PARTIALLY_SUBSTITUTES
NO_CREDIBLE_EXPERIENTIAL_SUBSTITUTE
CREDENTIAL_CONSTITUTIVE_OR_NON_SUBSTITUTABLE
NEED_MORE_INFORMATION
```

Independent capability gaps are recorded separately rather than being attributed
to the missing degree.

## Candidate-data boundary

Tracked `config/candidate*.yaml` files and candidate-intelligence test bundles
are synthetic. Real candidate profiles, identity, evidence, judgments, and
application artifacts belong under a selected private candidate root and are
excluded from Git. Runtime selection uses an opaque candidate ID and requires
no candidate-specific Python branch. The existing semantic-v1 input shape is
preserved by a deterministic minimum-disclosure projection that excludes
identity and non-authorized records.

Historical candidate fingerprints in frozen experiment receipts remain valid
provenance for those experiments. The tracked synthetic default is not a new
interpretation of that historical human evidence, and private experiments must
fail closed rather than silently replay against it.

## Reasoning-saturation design

SPEC-021 targets approximately 30–40 reviews, but planned count is not itself the
scientific objective.

After each 10 substantive reviews, a blind-safe pattern inventory may support an
explicit human decision to stop for `COMPLETED_REASONING_SATURATION` only when:

- all available target semantic classes have been observed;
- the last 10 substantive reviews add no new reasoning pattern;
- major patterns have cross-context support where available;
- no intentionally targeted rare class remains unseen.

No silent early stopping is allowed.

## Current gate

> Generic convergence and EY-only declarative activation/readiness are
> owner-reviewed/accepted. Stop after the authorized activation closure.
> Separate fresh-candidate authority and updated configuration/portfolio
> preflight remain required. Do not start another work packet or activate
> another source. Preserve both aborted databases, historical evidence and
> classifications. Do not resume either attempt, create attempt 003, perform
> operational/manifest writes, change durability, create Snapshot #2, call a
> source/model or perform an application action. Durability remains `BLOCKED`.
> Observed-window convergence is not server atomicity.

Frozen operational-recovery statuses:

- real private-state durability: `RESTORE_VERIFIED` for all nine inventoried artifacts;
- attempt 001: `ABORTED_EPOCH2_BOOTSTRAP_PRE_SCHEMA4`, historical-only partial baseline;
- attempt 002: `ABORTED_SOURCE_COMPLETENESS_EY`, original noncanonical `PARTIAL` evidence preserved;
- current durability gate: `BLOCKED`; accepted owner strategy may supersede only
  the obsolete attempt-001 candidate requirement, never grant restore verification;
- real off-device backup/restore: `CONTAINER_AND_ARTIFACT_RECOVERY_VERIFIED`;
- recovered `66dba4...` database: `HISTORICAL_READ_ONLY`;
- lost `a07d5300...` state: `LOST_OPERATIONAL_STATE`.

Snapshot #1 is an owner-authorized age-encrypted iCloud container whose
encrypted hash survived a remote round trip and whose isolated restore was
owner-confirmed. The retained restored Documents tree allowed Opportunity Radar
to independently verify all nine private-manifest artifacts: seven
`HUMAN_IRREPLACEABLE`, one `MACHINE_EXPENSIVE`, and the `HISTORICAL_READ_ONLY`
database. All eight gate-required artifacts pass. Container containment alone
remains insufficient; each passing artifact has its own restored SHA-256 match.

The encrypted multi-artifact container extension and bounded Snapshot #1
verification are owner-reviewed and accepted. They authorize no new
operational behavior and do not reopen or create another work packet.

No runtime credential/stretch policy change, semantic spend, autonomous application
action, Git-history rewrite, or hosted multi-user infrastructure is authorized.

## Protected boundaries

Do not change:

- SPEC-019 diagnostic stretch behavior;
- SPEC-020 frozen termination evidence;
- historical candidate profile/capabilities/preferences and frozen experiment
  fingerprints;
- market policy/status semantics;
- hard eligibility;
- source configuration/adapters;
- semantic-v1 model/prompt/reasoning/contract;
- semantic cache;
- Phase 3 scoring;
- clustering/seniority/lifecycle behavior;
- ranking/recommendation/semantic allocation.

No external semantic calls are authorized. No canonical operational SQLite
currently exists. Do not initialize, reconstruct, replace, or write one until a
new operational epoch and durable backup/recovery have been separately approved.
The recovered `66dba4...` database is historical evidence only.

## Architecture under investigation

```text
CAPABILITY FIT
      +
CREDENTIAL COMPATIBILITY
      ↓
APPLICATION COMPETITIVENESS / DECISION REASONING
```

Constitutive credentials may ultimately require separate non-substitutable treatment,
but this is a hypothesis for validation, not a runtime rule.

## Direction after SPEC-022

1. Architecture B is accepted as the architectural boundary, but runtime promotion remains deferred;
2. keep Architecture C constitutive-only treatment shadow/diagnostic until its boundary is stronger;
3. preserve conservative unresolved handling and an exploration/control path before suppressing semantic work;
4. keep semantic-v1 frozen until upstream allocation architecture is validated;
5. preserve the canonical SPEC-023 private boundary before any future expansion of candidate intelligence;
6. later use richer private candidate evidence to test whether capability uncertainty can be reduced without reintroducing credential proxies.

## Known open decisions

- Credential semantic/substitution architecture.
- Whether SPEC-019 stretch can later support runtime boundaries after credential correction.
- Deterministic rejection architecture.
- Exploration/control rate for future compute allocation.
- Semantic-call budget for later prospective ranking validation.
- Future source-contract work for Erste/Zentiva/Wave B.
- Phase B external private root, future DB path and verified manifest selection/
  placement are resolved. Snapshot #1 remains valid for the nine unchanged
  artifacts but cannot cover a future newly created database.
- SAP source-contract implementation/readiness and schema 4 acceptance are resolved.
- Fresh-candidate strategy under schema 4 and the 23-employer/24-surface portfolio
  is owner-approved for attempt 002. The protected schema-3 candidate is permanently
  aborted historical evidence, never a migration/resumption target.
- **BLOCKER:** EY inventory-view churn is reproduced; the generic convergence
  mechanism and EY-only activation/readiness are owner-reviewed/accepted. Fresh-candidate authority and updated
  configuration/portfolio preflight remain required. No automatic
  retry/resumption or source removal/waiver is allowed.
- **GATE:** all required sources/details/integrity must pass before candidate
  registration. Attempt 002 did not pass; the primary manifest remains unchanged.
- Complete baseline/integrity review, then separately authorized new backup/
  restore before canonicalization; the lost lifecycle interval must never be synthesized.
- Whether historical Git purge or exposure remediation is warranted for the
  previously tracked real candidate profile.
- Durable private backup/export/retention for private candidate intelligence.

## Explicitly do not build/tune yet

- runtime stretch filtering/rejection;
- combined deterministic rejection;
- credential-policy correction before v2 validation;
- AI imitation/training from human labels;
- autonomous preference learning;
- semantic prompt/model/weight tuning;
- cheap secondary LLM routing;
- embeddings/vector search;
- learned ranking/ML infrastructure;
- broad fuzzy clustering;
- new source integrations;
- UI/feed/control panel;
- application automation;
- external actions inferred from `APPLY`.
- Operational Epoch 2, a bootstrap, or any other work packet that writes or
  transitions private state without separate explicit authorization.
