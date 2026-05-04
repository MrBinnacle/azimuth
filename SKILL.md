---
name: azimuth
description: "Decision-quality pre-commitment analysis for initiative-level go/no-go calls with meaningful downside and limited reversibility — launches, rewrites, key hires, partnerships, strategic bets, timelines. Invoke when the user explicitly asks to pressure test, validate, or evaluate such a decision (e.g. 'should we do this,' 'pressure test,' 'go/no-go,' 'are we ready'). Do NOT invoke for routine code review, sub-task planning, reversible tactical choices, or pure ideation."
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

## Mode Selection — Use These Signals

Pick mode from the strongest applicable signal. When in doubt, ask one clarifying question rather than guessing.

**Use FAST when:**
- Decision is single-team, reversible, scope < 2 weeks of effort
- Sparse context — user supplied only a one-line plan
- User asked for a "quick check," "sanity check," or "gut check"
- No headcount, vendor contract, public commitment, or capital outlay involved

**Use STANDARD (default) when:**
- Cross-team or multi-stakeholder decision
- Scope between 2 weeks and 1 quarter
- Reversal is possible but costly (rework, re-planning, schedule cost)
- User supplied a structured plan with timeline, scope, and owners

**Use DEEP when ANY of the following are true:**
- Decision is irreversible or has high reversal cost (vendor contract signed, public announcement made, headcount changes, data migrations)
- Capital outlay above the user's stated decision-authority threshold
- Public-facing launch with brand/reputation exposure
- Headcount changes (hire / layoff / org restructure)
- Multi-quarter timeline
- User explicitly says "high stakes," "we can't afford to be wrong," or equivalent

If signals conflict, escalate (FAST → STANDARD, STANDARD → DEEP). Never silently downgrade.

---

## Mode Behaviors

### FAST

Run:
- Objective Check
- Assumption Audit (top 3 assumptions only)
- Top 3 Failure Paths
- Verdict

Do not load diagnostics or references.

### STANDARD

Default. Run all 10 core modules.

**Diagnostic loading in STANDARD is conditional, not automatic.** Load a diagnostic file only when the corresponding module surfaces a high-severity finding the user would benefit from drilling into:

- Module 2 surfaces 3+ unsupported assumptions or any contradicted assumption → load `diagnostics/assumption-audit.md`
- Module 4 surfaces a governance-level incentive conflict → load `diagnostics/incentive-conflicts.md`
- Module 5 surfaces a critical SPOF or concentration risk → load `diagnostics/dependency-map.md`
- Module 8 surfaces high irreversibility + late detectability → load `diagnostics/fragility-scan.md`

Load `references/base-rates.md` only when the user's plan involves a category covered by the file (software project, startup, launch, hire, M&A, migration, org change) AND the user's stated estimates appear to deviate from typical historical ranges.

### DEEP

Use for high-stakes / expensive / irreversible decisions per signals above.

Run all 10 modules + load:
- `gotchas.md`
- `references/base-rates.md`
- All four `diagnostics/` files

Also load the relevant domain reference:
- Tech / engineering → `references/software-failure-patterns.md`
- Product / launch → `references/launch-risks.md`
- Startup / venture → `references/startup-failures.md`

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

Diagnostic load: see Operating Modes for when to load `diagnostics/assumption-audit.md`.

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

Diagnostic load: see Operating Modes for when to load `diagnostics/incentive-conflicts.md`.

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

Diagnostic load: see Operating Modes for when to load `diagnostics/dependency-map.md`.

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

Reference load: see Operating Modes for when to load `references/base-rates.md` and the relevant domain pattern file.

If no data available, state uncertainty.

---

## 8. Detectability & Recovery

For top risks assess:

- early warning signs
- detection difficulty
- recovery difficulty
- reversibility

Risks detected late and hard to reverse are priority risks.

Diagnostic load: see Operating Modes for when to load `diagnostics/fragility-scan.md`.

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

# Module Output Reduction

Modules 2, 5, 6, 7, and 8 share an underlying register of assumptions, dependencies, and risks. They are not independent reports — they are passes that contribute to the same register and surface different facets of it.

Rules:

1. Maintain a single internal register across modules. Each entry includes: source module(s), severity, evidence classification, dominant constraint touched, and reversibility.
2. When the same assumption or risk is surfaced by more than one module, do **not** repeat it in the output. Cite it once in the most relevant section and reference it elsewhere by short tag (e.g. "see Critical Risk #2") if needed.
3. The Critical Risks section is the deduplicated, severity-ordered output of the register. It is not a per-module dump.
4. The Weak Assumptions section is the subset of the register classified UNSUPPORTED or CONTRADICTED in Module 2, ordered by Risk Score.
5. The Likely Failure Paths section reuses register entries — it does not introduce new risks not already in the register.

If the register has fewer than 3 critical risks, do not pad to three. State the register honestly.

---

# Output Format (Default)

**Two non-negotiable output rules:**

1. **Lead with the verdict.** The first three lines of every output must be the verdict line, the recommended decision, and the confidence level. Anything else comes after. The reader must be able to act on the first paragraph alone.
2. **Omit empty sections.** Do not emit a section header with no substantive content under it. If "Structural Strengths" has nothing genuine to put in it, cut the section entirely. A short, sharp output is correct. A padded output is a failure of the skill.

```
## Azimuth Verdict
(one line — clear position, no hedging)

## Recommended Decision
(PROCEED / PROCEED WITH SAFEGUARDS / PILOT FIRST / REDUCE SCOPE / DELAY PENDING EVIDENCE / REJECT)
Rationale: (one to two sentences)

## Confidence Level
Low / Medium / High + why

---

## Critical Risks
(Severity-ordered, from the register. 1–5 entries. Do not pad.)
1. ...
2. ...
3. ...

## Weak Assumptions
(UNSUPPORTED or CONTRADICTED entries from Module 2. Omit section if none.)
- ...

## Likely Failure Paths
(Trigger → Cascade → Visible Failure → Business Cost. Reuses register entries; no new risks.)
- ...

## Highest-Leverage Fixes
(Structural changes only. Weak mitigations rejected.)
- ...

## Early Warning Indicators
(What to monitor that would signal a risk activating. Omit if not applicable.)
- ...

## Structural Strengths
(Optional. Include only if genuine and material to the decision.)
- ...
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
