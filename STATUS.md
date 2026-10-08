# Portfolio Governor — Current Status

Recorded: 2026-10-08

Branch: `main`

Operational state: `READY_FOR_IMPLEMENTATION`

## Mission

Portfolio Governor is the operational governance and allocation layer for Roman's AI-assisted project portfolio.

It remains observational and advisory toward governed projects.

## Current approved work packet

`specs/SPEC-001-minimum-operational-governor.md`

Status: `APPROVED_FOR_IMPLEMENTATION`

Authority: `GOVERNOR_REPO_ONLY`

Human gate: `OWNER_REVIEW`

Promotion: `NOT_AUTHORIZED`

## Objective

Operationalize only the proven manual loop:

fresh project evidence → review-due detection → evidence assembly → Purpose / Truth / Safety / Capital → strategic debt / trajectory → allocation → durable Governor record.

## Authority now

Allowed:
- inspect Governor files;
- read governed repository evidence;
- implement Governor-local derived state/evidence assembly/freshness/trigger/template machinery required by SPEC-001;
- add tests/documentation inside this repository;
- prepare a dogfood rehearsal evidence packet;
- commit Governor-repository implementation for owner review.

Not authorized:
- modify Knowledge Compiler, Opportunity Radar, or Asymmetry Engine;
- activate/stop/preempt/reprioritize governed-project work;
- change Portfolio Constitution or project constitutions;
- authorize external actions or spending;
- grant Governor governed-repo write authority;
- deploy daemon/service;
- build dashboard/UI;
- publish a new Governor review verdict from dogfood rehearsal without separate authority.

## Frozen governance baseline

- Constitution: `CONSTITUTION.md` v0.1
- Latest accepted review: `reviews/GOV-004.md`
- Latest accepted allocation: `allocations/CYCLE-009.md`
- Governed projects: `PROJECTS.md`

Historical reviews and allocations are immutable evidence for SPEC-001.

## Next operation

`Implement SPEC-001 within the Governor repository only.`

Stop at owner review. Passing implementation does not authorize autonomous operation.
