# Assumption Audit Diagnostic

Load when running a full Assumption Audit (Module 2) in STANDARD or DEEP mode, or when the plan has thin evidence behind its core premises.

---

## Purpose

Surface and classify what must be true for the plan to succeed. Distinguish between validated beliefs and wishful thinking masquerading as evidence.

The goal is not to find every assumption — it's to find the **unsupported assumptions with the highest leverage on outcomes**.

---

## Step 1: Extract Assumptions by Category

For each category, ask: "What does this plan assume is true?"

### Demand / Need
- Is there proven demand, or assumed demand?
- Have customers expressed this as a top-priority problem, or is the team inferring it?
- Is the demand addressable by this solution, or is it diffuse?

### Technical Feasibility
- Has the core technical approach been validated, or is it still theoretical?
- Are there known unknowns the team hasn't investigated?
- Does the plan depend on achieving performance or scale that hasn't been demonstrated?

### Capability and Talent
- Does the team have the skills required at the level required?
- Are key people available for the full duration, not just the start?
- Are estimates made by the people doing the work, or by people managing it?

### Timing
- Why is now the right time?
- What does the plan assume about the window of opportunity?
- Is the timeline estimate derived from analogous work, or from expectation?

### Stakeholder Support
- Who must approve, fund, or enable this work?
- Has that support been confirmed, or assumed based on prior signals?
- Who could block this, and what would prompt them to?

### Cost and Runway
- Are cost estimates based on detailed line-item scoping, or rough order of magnitude?
- What does the plan assume about cost behavior over time?
- Is there a contingency buffer, and is it sized to realistic variance?

### User or Customer Behavior
- What change in behavior does the plan require from users?
- Has that behavior been observed, or is it assumed?
- What is the historical rate of behavior change in comparable contexts?

### External Environment
- What does the plan assume about regulatory, competitive, or market conditions?
- Are those conditions likely to hold for the plan's duration?
- What external events would most likely invalidate the plan?

---

## Step 2: Classify Each Assumption

For each identified assumption, assign a classification:

**STRONG** — Backed by direct evidence: data, customer interviews, prior results, contracts, confirmed commitments.

**PARTIAL** — Some supporting evidence exists, but it's indirect, dated, or from a limited sample. Reasonable but not confirmed.

**UNSUPPORTED** — Based on intuition, analogy, or optimism without direct evidence. High inference, low verification.

**CONTRADICTED** — There is actual evidence that this assumption may be false. Red flag; requires immediate attention.

---

## Step 3: Prioritize for Scrutiny

Not all unsupported assumptions have equal impact. Prioritize based on:

**Impact** — If this assumption is wrong, how badly does the plan fail? (Scale: 1–5)

**Reversibility** — If the assumption is wrong mid-execution, can the plan adapt? (1 = easy to adapt; 5 = locked in)

**Verifiability** — Can this assumption be cheaply validated before commitment? (1 = easy; 5 = requires full execution to find out)

**Risk Score** = Impact × (Reversibility + Verifiability) / 2

Focus scrutiny on assumptions with high Risk Scores.

---

## Step 4: Validation Actions

For each high-Risk unsupported assumption, define the minimum viable validation:

| Assumption | Risk Score | Validation Method | Cost | Timeline |
|------------|------------|-------------------|------|----------|
| [assumption] | [score] | [how to validate] | [effort] | [when] |

**Preferred validation methods (low cost):**
- Customer conversation (5–10 interviews)
- Prototype or mockup test
- Small-scale pilot
- Expert interview
- Historical data review
- Competitive research
- Reference check

**Reject** validation methods that require full execution to return signal.

---

## Step 5: Validation Gating

Define which assumptions must be validated **before commitment** versus **during execution**.

**Pre-commitment validation** (must complete before greenlighting):
- List the 2–3 highest-Risk unsupported assumptions
- Define the minimum evidence required to move them from Unsupported to Partial
- Block go/no-go decision until these are resolved

**During-execution validation** (acceptable to validate in-flight):
- Lower-risk assumptions where mid-course correction is feasible
- Assumptions where early results will naturally generate data

---

## Output Format

### Assumption Map

| Assumption | Category | Classification | Impact | Reverb | Verif | Risk Score |
|------------|----------|----------------|--------|--------|-------|------------|

### Top 3 Unsupported Assumptions
1. [assumption] — Risk Score: [X] — Validation action: [method, timeline]
2. ...
3. ...

### Pre-Commitment Gates
- [ ] [assumption] validated via [method] by [date]
- [ ] ...

### Assumptions Accepted Without Validation (with rationale)
- [assumption] — rationale: [why acceptable]
