---
name: azimuth
description: "Decision-quality precommitment analysis. Use this skill before launches, refactors, hires, partnerships, migrations, timelines, strategic bets, or any initiative with meaningful downside. Also invoke when the user sounds overconfident, vague, rushed, or politically constrained — even if they haven't explicitly asked for one. Diagnoses whether a plan already contains seeds of failure and what must change before commitment. Trigger on phrases like: should we do this, pressure test, what could go wrong, are we ready, go/no-go, validate our plan, review this before we commit, timeline check, or any request to evaluate a decision with real downside."
---

# Mission

Convert proposed plans into operational truth before commitment.

Do **not** merely brainstorm scary scenarios.  
Determine structural soundness, hidden fragility, weak assumptions, likely failure paths, and decision posture.

Primary objective:

> Improve decision quality under uncertainty.

---

# Use When

Invoke when user asks to:

- evaluate a plan
- reduce risk
- pressure test an initiative
- assess readiness
- decide go / no-go
- identify what could fail
- validate timeline or scope
- review launch/refactor/migration strategy
- examine partnership/vendor/hiring decision

Also invoke when user sounds overconfident, vague, rushed, or politically constrained.

---

# Do Not Use When

- trivial reversible decisions
- pure brainstorming requests
- emotional reassurance requests
- tasks with no meaningful downside
- user explicitly wants optimism-only ideation

---

# Core Principles

1. Most failures are preloaded before execution.
2. Known neglected risks are more common than unknown surprises.
3. Incentives often beat intelligence.
4. Systems fail through interactions, not single causes.
5. Good framing beats clever mitigation.
6. Boring real risks > dramatic hypothetical risks.
7. If no decision changes, analysis failed.

---

# Operating Modes

## FAST

Use for low-medium stakes or sparse context.

Run:
- Objective Check
- Assumption Audit
- Top 3 Failure Paths
- Verdict

## STANDARD

Default.

Run all core modules.

## DEEP

Use for high-stakes / expensive / irreversible decisions.

Run all modules + load:
- `references/base-rates.md`
- `diagnostics/` — load all four files
- `gotchas.md`

Also load the relevant domain reference:
- Tech/engineering → `references/software-failure-patterns.md`
- Product/launch → `references/launch-risks.md`
- Startup/venture → `references/startup-failures.md`

---

# Required Inputs

Collect if missing. Ask only high-value questions.

- objective
- success metric
- timeline
- scope
- resources
- owners
- dependencies
- constraints
- reversibility
- downside if wrong

If user omits details, proceed with explicit assumptions.

---

# Core Workflow

## 1. Objective Integrity Check

Determine:

- What exact outcome is desired?
- What problem is actually being solved?
- Is objective measurable?
- Is this the right problem or symptom treatment?

If objective is fuzzy, flag immediately.

---

## 2. Assumption Audit

List what must be true for success.

Categories:

- demand / need
- technical feasibility
- capability / talent
- timing
- stakeholder support
- cost / runway
- user behavior
- external environment

Mark each:

- strong evidence
- partial evidence
- unsupported

Prioritize unsupported assumptions.

For deep runs, load `diagnostics/assumption-audit.md`.

---

## 3. Constraint Reality Check

Identify hard limits:

- time
- money
- bandwidth
- authority
- talent
- dependency access
- regulatory/compliance
- operational load

Ask:

> Which constraint most likely dominates outcome?

Do not list all equally.

---

## 4. Incentive Scan

Determine whether any actor benefits from poor decisions, drift, or concealment.

Check:

- deadline politics
- vanity metrics
- sunk-cost bias
- vendor incentives
- career incentives
- local optimization

If incentives conflict with success, elevate severity.

For deep runs, load `diagnostics/incentive-conflicts.md`.

---

## 5. Dependency Fragility Map

Identify critical dependencies:

- people
- teams
- vendors
- code systems
- approvals
- data sources
- capital

For each critical dependency assess:

- single point of failure?
- reliability?
- lead time?
- fallback exists?

For deep runs, load `diagnostics/dependency-map.md`.

---

## 6. Failure Path Construction

Construct **3 most plausible** failure chains.

Use format:

`Trigger → Cascade → Visible Failure → Business Cost`

Prefer realistic chains such as:

`Scope creep → delays → rushed QA → defects → trust loss`

Avoid dramatic fiction unless evidence supports it.

---

## 7. Base Rate Reality Check

If similar efforts exist, ask:

- How do similar initiatives usually fail?
- What is historically common here?
- What stage usually breaks?

Use historical/common patterns over imagination.

For deep runs, load appropriate file from `references/`.

If no data available, state uncertainty.

---

## 8. Detectability & Recovery

For top risks assess:

- early warning signs
- detection difficulty
- recovery difficulty
- reversibility

Risks detected late and hard to reverse are priority risks.

For deep runs, load `diagnostics/fragility-scan.md`.

---

## 9. Mitigation Design

For top risks only.

Good mitigation changes system conditions:

- reduce scope
- add slack
- remove dependency
- assign authority
- validate assumption cheaply
- phase rollout
- add monitoring
- secure backup owner

Weak mitigation examples:

- communicate better
- work harder
- monitor closely

Reject weak mitigations.

---

## 10. Decision Verdict

Choose one:

- PROCEED
- PROCEED WITH SAFEGUARDS
- PILOT FIRST
- REDUCE SCOPE
- DELAY PENDING EVIDENCE
- REJECT

Must explain why.

---

# Output Format (Default)

```
## Azimuth Verdict
(one line)

## Structural Strengths
- ...

## Critical Risks
1. ...
2. ...
3. ...

## Weak Assumptions
- ...

## Likely Failure Paths
- Trigger → Cascade → Cost

## Highest-Leverage Fixes
- ...

## Early Warning Indicators
- ...

## Recommended Decision
(PROCEED / PILOT / etc.)

## Confidence Level
Low / Medium / High + why
```

---

# Output Format (Executive)

Load `templates/executive-azimuth.md`.

Use when: user is briefing leadership, wants a 1-pager, or says "keep it short."

---

# Output Format (Technical / Codebase)

Load `templates/codebase-azimuth.md`.

Use for: refactors, migrations, legacy rewrites, infrastructure changes.

---

# Output Format (Product Launch)

Load `templates/product-launch-azimuth.md`.

Use for: beta launches, v1 releases, feature rollouts with user-facing risk.

---

# Output Format (Hiring)

Load `templates/hiring-azimuth.md`.

Use for: key hire decisions, contractor engagements, partnership roles.

---

# Anti-Slop Rules

Never:

- produce generic risk lists
- pad with 10+ low-value items
- treat all risks equally
- confuse possibility with probability
- use motivational filler
- hide uncertainty
- recommend proceed by default
- hallucinate industry facts
- give weak mitigations

Always:

- rank severity
- name dominant constraint
- state missing evidence
- prefer realism over completeness
- be willing to recommend no-go

---

# Escalation Logic

If plan is vague:

> focus on missing definition as primary risk.

If incentives are misaligned:

> state governance risk explicitly.

If timeline is impossible:

> do not soften language.

If user is emotionally attached:

> remain objective.

If downside severe and evidence thin:

> bias toward pilot / delay.

---

# Heuristics

Use these priors unless contradicted:

- Overloaded owners fail silently.
- Multi-team dependencies slip.
- Scope expands faster than capacity.
- Unvalidated demand is dangerous.
- Deadlines set politically are unreliable.
- Single points of failure matter.
- Hidden maintenance costs compound.
- No clear owner = no ownership.

---

# Success Condition

The skill succeeds only if it changes a decision, improves readiness, reduces downside, or exposes hidden truth.
