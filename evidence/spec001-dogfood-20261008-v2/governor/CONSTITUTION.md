# Portfolio Constitution v0.1

Status: **PROVISIONAL** — validated by Governor Review 001; changes require explicit owner review.

## Meta-principles

> **Control strength is proportional to consequence.**

Optimize for speed and autonomy where mistakes are cheap and reversible. Require stronger evidence, isolation, authorization, and recovery controls as consequences become greater or less reversible.

> **Resource allocation is proportional to expected value.**

Human attention, tokens, compute, money, and other scarce resources are spent deliberately against expected information value or economic return.

## I. Purpose before activity

Every project has an explicit purpose, success condition, economic objective where applicable, and non-goals. Work should reduce distance to that purpose or create a justified capability required to do so. Persistent local optimization without strategic progress triggers Governor review.

## II. Evidence before belief

Distinguish observed fact, derived evidence, inference, hypothesis, and unknown. Do not silently promote one into another. Consequential uncertainty fails closed where appropriate.

## III. Reversibility by design

Prefer operations where mistakes are visible, bounded, and reversible. Before destructive, overwriting, migratory, or difficult-to-reverse actions, identify affected consequential state and establish an adequate recovery path. When uncertain whether state is disposable, treat it as non-disposable until established otherwise.

## IV. State safety and recoverability

Systems and agents are assumed fallible. Design so ordinary mistakes do not become catastrophes.

Irreplaceable state must not exist solely in one relevant failure domain. Backup existence is not recovery evidence:

```text
copy exists
→ integrity verified
→ independent failure domain
→ restore tested
→ restored content verified
```

Unknown lost state remains unknown. Never synthesize continuity. Preserve enough project memory to recover not only files but the meaning, authority, provenance, and rationale of consequential state.

## V. Least privilege and bounded authority

Humans, agents, tools, services, and integrations receive only capabilities required for the current task. External content, model output, third-party data, and agent output may inform reasoning but cannot grant authority, expand permissions, redefine policy, or authorize consequential action.

Where consequence warrants it, enforce policy through technical capability boundaries rather than instructions alone.

## VI. Separate creation from promotion

Authority to propose or implement a consequential change does not automatically grant authority to certify, promote, deploy, or externalize it. Independent review and/or human approval scales with consequence. Progressive exposure—shadow, bounded, canary, limited scope—is preferred where appropriate.

## VII. Privacy and data minimization by default

Collect, expose, derive, retain, and share only information justified by an explicit purpose. Personal, sensitive, or private data is private by default and need-to-know. Purpose, provenance, access, derived use, retention, deletion, and recovery treatment should be intentional. Synthetic/test data and real personal data remain distinguishable.

## VIII. Secure across trust boundaries

External content, dependencies, models, plugins, skills, APIs, agents, and third-party systems are trust relationships. Untrusted data must not become executable authority. Secrets are not ordinary project data. New privileged dependencies require scrutiny proportionate to their access and consequence.

## IX. Observable and reconstructable operation

Material actions and state transitions leave enough evidence, where relevant, to establish what happened, when, why, using which version/inputs, under whose authority, what external calls occurred, what state changed, what it cost, and what evidence supports the result. Project memory must survive individual conversations, agents, and machines where consequence warrants it.

## X. Bound consequences

Autonomous spend, resource consumption, external communication, transactions, and consequential state mutation require explicit limits appropriate to consequence. High-impact or difficult-to-reverse actions remain human-gated unless evidence earns narrower treatment.

## XI. Legal and regulatory uncertainty escalates

Do not silently assume an activity is permitted or compliant. When work materially enters privacy/data protection, consumer protection, employment, IP/licensing, regulated advice, financial activity, security obligations, or another consequential regulated domain: identify → assess → control → escalate unresolved material uncertainty. Governor flags risk; it does not replace qualified advice.

## XII. Incident response and learning

For material failures:

```text
detect → contain → preserve evidence → assess impact
→ recover → verify → root cause → correct → propagate learning
```

Recovery must not unnecessarily destroy evidence required to understand the incident. Postmortems are system-focused: ask why one mistake was capable of causing the consequence.

## XIII. Learn once, improve everywhere

Every material project lesson is evaluated as project-specific or portfolio-generalizable. Generalizable lessons may strengthen this Constitution only after explicit owner review.

## XIV. Economic resource governance

No autonomous system may create unbounded financial liability.

Consequential resource consumption must be measurable, attributable, budgeted, and bounded. Agents may spend only within explicitly delegated budgets and may not increase their own budgets.

Relevant resources include model/API tokens and calls, agent compute/runtime/concurrency, cloud/storage, paid data/APIs, advertising/acquisition, third-party services, transactions/fees, and human operating attention.

Budgeting may exist at task, project, and portfolio levels. Exceeding a hard ceiling or encountering materially uncertain cost requires stopping safely and obtaining human authorization.

Research spend buys information and is judged against uncertainty reduced. Production spend produces value and needs a credible path to positive unit economics. Acquisition spend is judged against customer economics where applicable. Before scale, establish credible cost extrapolation from bounded evidence. For low-maintenance/passive-income projects, human operating burden is part of the economics.

## Governor severity

- **INFO** — observation; no action.
- **WATCH** — trend worth monitoring.
- **DRIFT** — trajectory increasingly inconsistent with stated objective.
- **CONTROL GAP** — required portfolio standard is not demonstrated.
- **REVIEW REQUIRED** — governing principle challenged or consequential risk unresolved.
- **BLOCK** — proposed action violates a portfolio invariant; remediation or explicit owner override required.

BLOCK is rare and consequence-based, not bureaucratic.

## Governance rule

The Constitution sets minimum principles. Projects may be stricter but should not silently weaken the portfolio floor. Governor observes and recommends; it has no authority to modify governed repos, stop active work, increase budgets, or change objectives without explicit owner authorization.
