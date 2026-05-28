# Fragility Scan Diagnostic

This file is an observational catalog. It describes patterns to look for when conducting a Module 8 detectability & recovery assessment. It does not assign verdicts, cap confidence, or define when to load — decision authority for those lives in `BEHAVIOR_SPEC.md`.

## Purpose

Determine whether the plan's structure amplifies or absorbs failure. Fragile systems fail catastrophically from small perturbations; robust systems degrade gracefully and surface problems early enough to correct.

Fragility is structural. It is not about the probability of a bad event — it's about the magnitude and reversibility of consequences when anything goes wrong.

---

## Fragility Indicators

### Indicator 1: Tight Coupling

**Definition**: When components, timelines, or teams must succeed in precise sequence with no slack, a single failure cascades immediately and broadly.

**Signs**:
- All phases must complete before the next can begin
- No buffer time between milestones
- One team's output is another team's direct input, with no decoupling layer
- Plan has no parallel tracks that could absorb a delay

**Assessment question**: If Phase A is 2 weeks late, what happens to Phase B and beyond?

---

### Indicator 2: Single Point of Failure

**Definition**: One node — a person, system, approval, or service — whose failure stops the entire plan.

**Signs**:
- Key knowledge or capability concentrated in one person
- No backup system for a critical integration
- One approval authority with no escalation path
- One vendor for a non-substitutable service

**Assessment question**: What is the one removal that stops the plan cold? Is there a mitigation?

---

### Indicator 3: Late Detectability

**Definition**: Failures that can only be detected at — or after — the point where they become expensive or irreversible to correct.

**Signs**:
- Testing or validation happens at the end of a phase, not throughout
- No continuous integration or ongoing signal on plan health
- Key metrics are only assessed at milestone reviews
- Errors in foundational work (data, schema, requirements) are discovered in later phases

**Assessment question**: If a critical assumption is wrong, at what point in the plan does that become visible? What is the cost at that point?

---

### Indicator 4: Asymmetric Reversibility

**Definition**: Going forward is cheap; going backward is expensive. Commitments are made before the full picture is available.

**Signs**:
- Vendor contracts signed before technical validation
- Data migrations with no rollback path
- Public announcements made before execution is de-risked
- Hiring or org structure changes that are expensive to undo

**Assessment question**: What decisions, once made, are practically irreversible? Have those been made before the high-risk elements are validated?

---

### Indicator 5: Amplification Loops

**Definition**: Failure in one area creates conditions that make subsequent failures more likely or more severe. Problems compound rather than stabilize.

**Signs**:
- Team morale or cohesion is load-bearing (one departure triggers others)
- Customer trust is a key asset (early problems disproportionately damage later adoption)
- Budget is tight (cost overrun in early phases starves later phases)
- Reputation is at stake publicly (visible failure makes course correction harder)

**Assessment question**: Where does a moderate failure in this plan make the next failure more likely?

---

### Indicator 6: High Operational Load

**Definition**: The plan requires sustained, high-intensity effort from people who are also managing existing obligations. High operational load degrades quality, judgment, and communication over time.

**Signs**:
- Key people are on multiple high-priority projects simultaneously
- Plan timeline extends beyond 90 days without recovery periods built in
- "Crunch" or overtime is implicitly part of the plan
- No contingency for personnel changes (departure, illness, parental leave)

**Assessment question**: What happens to this plan's quality and timeline if two key contributors are at 50% capacity for 4 weeks?

---

## Robustness Indicators (positive signals to note)

- Modular phases where early phases produce useful output regardless of later phase completion
- Defined circuit breakers: conditions under which work stops and is reassessed
- Multiple early feedback signals (not just end-of-phase reviews)
- Backup owners for critical roles
- Rolling scope: ability to ship a smaller version if full scope isn't achievable
- Explicit rollback procedures that have been tested

---

## Fragility Score

After assessing each indicator, assign a composite fragility level:

**LOW**: 0–1 fragility indicators present; plan has meaningful absorptive capacity.

**MEDIUM**: 2–3 indicators present; plan will survive small failures but not multiple simultaneous failures.

**HIGH**: Findings in the HIGH range typically show 4+ indicators or any SPOF + Late Detectability combination. Plan is brittle. A single significant failure likely cascades.

**CRITICAL**: SPOF + Late Detectability + Asymmetric Reversibility present. Plan has locked in irreversible commitments before high-risk elements are validated.

---

## Output Format

### Fragility Assessment

**Fragility Score**: [LOW / MEDIUM / HIGH / CRITICAL]

**Fragility Indicators Present**:
- [indicator] — Evidence: [what in the plan triggers this]

**Robustness Factors Present**:
- [factor] — Evidence: [what in the plan demonstrates this]

### Top Structural Fragility
[The single most dangerous fragility in this plan, stated plainly.]

### Recommended Structural Changes
1. [change] — Addresses: [fragility indicator] — Feasibility: [High/Medium/Low]
