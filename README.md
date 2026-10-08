# Portfolio Governor

Durable governance memory for Roman's AI-assisted project portfolio.

## Purpose

Portfolio Governor preserves the bigger picture across projects:

- **Governor:** are projects still pursuing the right objectives, within acceptable operating boundaries?
- **Allocator:** where should scarce human attention, compute, and money go next?
- **Projects:** independently determine the cheapest valid experiment that advances their objectives.

This repository is the **operational governance and allocation layer** for the portfolio. It remains observational and advisory by default; governed projects remain sovereign execution systems.

## Authority boundary

Portfolio Governor is read-only with respect to governed project repositories. It does not modify project repos, activate work packets, stop/preempt work, authorize external actions, spend money, deploy software, or change project constitutions automatically.

Any recommendation to preempt active project work requires explicit owner approval.

## Governed projects

- Knowledge Compiler — `CIF84/knowledge-compiler`
- Opportunity Radar — `CIF84/opportunity-radar`
- Asymmetry Engine — `CIF84/-asymmetry-engine`

## Operating model

```text
OWNER
  ↓
PORTFOLIO CONSTITUTION
  ↓
GOVERNOR
  ├─ strategic alignment
  ├─ constitutional assurance
  └─ cross-project learning
  ↓
ALLOCATOR
  ↓
independent project operating systems
```

The Governor protects **purpose, truth, safety, and capital**.

Controls are proportional to consequence. Resources are allocated in proportion to expected value.

## Status

Four manual review/allocation cycles have validated the governance function.
`SPEC-001 — Minimum Operational Governor` is implemented for owner review:
bounded read-only evidence assembly, derived portfolio state, freshness guards,
trigger observations and review/allocation drafts **inside this repository only**.

```sh
python3 -m governor assemble --packet my-rehearsal
python3 -m governor verify --packet my-rehearsal
python3 -m unittest discover -s tests -v
```

Python 3.10+ and Git suffice. See [operating instructions](docs/OPERATIONS.md)
and the [implementation/rehearsal report](docs/SPEC-001-IMPLEMENTATION.md).

Operationalization does not grant write authority over governed projects,
autonomous spending, preemption, or external-action authority. Canonical use and
autonomous operation remain unapproved pending owner review.
