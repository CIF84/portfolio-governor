# SPEC-001 — Minimum Operational Governor

Status: `APPROVED_FOR_IMPLEMENTATION`

Authority: `GOVERNOR_REPO_ONLY`

Human gate: `OWNER_REVIEW`

Promotion: `NOT_AUTHORIZED`

## Problem

Four Governor reviews and subsequent allocation cycles demonstrated material portfolio value, but the workflow still depends on manual reconstruction and owner/assistant memory.

The operational problem is repeatability: detecting that review is due; proving evidence freshness; assembling authoritative cross-project state; comparing trajectory against prior review; applying Purpose / Truth / Safety / Capital consistently; preserving accepted evidence; and avoiding stale or forgotten governance.

## Objective

Demonstrate a minimum operational Governor that can prepare the evidence and state required to reproduce the proven manual governance/allocation loop while preserving the constitutional authority boundary.

## Primary question

> Can Governor detect that a review is due, assemble fresh authoritative evidence across governed projects, expose the portfolio state needed for Purpose/Truth/Safety/Capital review and allocation, and preserve the result without gaining write authority over any governed project?

## Non-goals

SPEC-001 must not build:

- dashboard or GUI;
- generic multi-agent orchestration;
- autonomous project management;
- governed-repo write integration;
- project work-packet generation/activation;
- autonomous preemption or spending;
- autonomous constitutional amendment;
- database unless file state is proven insufficient;
- continuous daemon;
- complex scheduling;
- predictive portfolio scoring;
- monetization infrastructure.

## Protected boundaries

Do not modify:
- `CONSTITUTION.md`;
- project constitutions;
- historical reviews/allocations;
- KC, OR, or AE repositories or their branches/issues/PRs/state/authority.

Do not grant Governor capabilities permitting governed-repo mutation.

## Required deliverables

### D1 — Derived portfolio state
Implement `state/portfolio.yaml` representing for each project:
- repository identity;
- constitution path;
- evaluated HEAD;
- authoritative status path;
- current project/gate state;
- last Governor review/allocation;
- current Governor verdict;
- material strategic debt;
- review-due state and trigger;
- evidence timestamp/freshness metadata.

This is derived state, not project authority.

### D2 — Evidence assembly
Provide a reproducible bounded workflow reading the Constitution, project constitutions, authoritative project status, governed HEAD/history since prior review, and prior Governor review/allocation, then emitting a Governor-local review evidence packet.

It prepares evidence; it does not claim strategic judgment automatically.

### D3 — Freshness guard
Before a review is represented as current, verify governed HEADs still match evidence assembly. On material mismatch fail closed:

`STALE_REVIEW_REFRESH_REQUIRED`

### D4 — Review-trigger detection
Deterministically detect where possible:
- material commit/work-packet movement;
- prior Governor follow-up requirement;
- material status/gate transition;
- explicit incident/recovery state;
- human/owner gate visible in authoritative status.

Heuristic/semantic triggers may be `REVIEW_CANDIDATE`, not proven facts.

### D5 — Review/allocation templates
Provide templates for `reviews/GOV-NNN.md` and `allocations/CYCLE-NNN.md` preserving evaluated HEADs, Constitution version, previous review/allocation, Purpose/Truth/Safety/Capital, strategic debt, trajectory, verdict, Roman queue, machine queue, capital findings, and preemption status.

### D6 — Authority test
Demonstrate that SPEC-001 requires no governed-repo writes. Inventory every external capability used and show no governed-project mutation occurred.

### D7 — Dogfood rehearsal
Using current repos, prepare—but do not publish as a new governance verdict unless separately authorized—a rehearsal evidence packet for the next review.

Compare with manual GOV-004/CYCLE-009 and report evidence omitted/added, stale-state risks caught, repeated manual steps eliminated, false triggers, and unresolved judgment requiring human/LLM reasoning.

## Acceptance criteria

Pass only if:
1. governed evidence is read-only;
2. HEADs and authoritative status are explicit;
3. stale review state fails closed;
4. derived state is reconstructable;
5. trigger detection is useful without pretending semantic judgment is deterministic;
6. templates reproduce proven governance dimensions;
7. no governed repo is modified;
8. no consequential Governor authority is introduced;
9. dogfood materially reduces reconstruction effort or freshness risk;
10. added machinery remains simpler than the manual problem.

## Stop conditions

Stop for owner review if governed-repo write access or a database appears necessary; trigger logic requires large project-specific parsers; automation starts making strategic judgments; resource cost is materially uncertain; project status cannot be read authoritatively; or scope expands into dashboard/orchestration.

## Resource envelope

Local/offline by default except bounded read-only GitHub access to establish authoritative remote state.

No paid model/provider calls, external spend, or autonomous background process are authorized.

## Expected result

One of:
- `PASS_MINIMUM_OPERATIONAL_GOVERNOR_EARNED`
- `PARTIAL_MANUAL_GOVERNANCE_REMAINS_PREFERRED`
- `FAIL_OPERATIONALIZATION_ADDS_MORE_COMPLEXITY_THAN_VALUE`

## Promotion boundary

Passing SPEC-001 does not authorize autonomous Governor operation. Owner review separately decides whether the mechanism becomes canonical and whether further automation is justified.
