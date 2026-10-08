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

Four manual review/allocation cycles have validated the governance function. `SPEC-001 — Minimum Operational Governor` is now approved to operationalize evidence freshness, review-trigger detection, evidence assembly, derived state, and durable review workflow **inside this repository only**.\n\nOperationalization does not grant write authority over governed projects, autonomous spending, preemption, or external-action authority. Automation must continue to earn authority through evidence.
