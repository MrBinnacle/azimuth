# Dependency Fragility Map Diagnostic

Load when running a full Dependency Fragility Map (Module 5) in STANDARD or DEEP mode, or when the plan involves multiple teams, vendors, external services, or shared infrastructure.

---

## Purpose

Identify which dependencies are load-bearing and which are fragile. Most plans list dependencies; few assess them. This diagnostic forces assessment.

---

## Step 1: Full Dependency Inventory

Extract all dependencies from the plan. Include:

**People**
- Named individuals whose work, decisions, or knowledge is required
- Roles that are currently vacant or partially filled
- Subject matter experts consulted but not directly involved

**Teams / Organizations**
- Internal teams outside the executing team
- Shared services (platform, security, legal, compliance, IT)
- Partner organizations

**Vendors and Third Parties**
- Software vendors and SaaS providers
- Contractors and agencies
- Data providers

**Systems and Infrastructure**
- Internal services and APIs the plan calls into
- Shared databases or data pipelines
- Legacy systems the plan must coexist with or migrate from

**Approvals and Decisions**
- Regulatory or compliance approvals required
- Executive or board decisions required
- Budget approvals

**Capital and Funding**
- Committed budget
- Budget pending approval
- External funding that hasn't closed

---

## Step 2: Dependency Assessment Matrix

For each dependency, assess:

| Dependency | Type | SPOF? | Reliability | Lead Time | Fallback? | Risk Level |
|------------|------|-------|-------------|-----------|-----------|------------|

**Single Point of Failure (SPOF)**: Yes/No — If this dependency fails, does the plan fail?

**Reliability**: Historical reliability of this dependency.
- High: Consistently delivers, low failure rate
- Medium: Occasional delays or issues; recoverable
- Low: Unreliable, frequently blocks progress, high variance

**Lead Time**: How far in advance does this dependency need to be secured?
- Short: Days
- Medium: 1–4 weeks
- Long: >4 weeks

**Fallback**: Is there an alternative if this dependency fails?
- Yes: Defined and available
- Partial: Possible but more expensive or slower
- No: No fallback; plan fails if dependency fails

**Risk Level**: Composite assessment
- Critical: SPOF + Low reliability or No fallback
- High: SPOF OR low reliability without fallback
- Medium: Not SPOF, partial fallback, medium reliability
- Low: Redundant, reliable, short lead time

---

## Step 3: Critical Path Analysis

Identify which dependencies are on the critical path — meaning their delay directly delays the final outcome.

For each Critical or High risk dependency on the critical path:

1. **What is the failure mode?** — How does this dependency typically fail? (Delay, quality problem, capacity constraint, refusal, outage?)

2. **What is the early warning?** — What observable signal would indicate this dependency is about to fail or slip?

3. **What is the recovery action?** — What does the team do if this dependency fails? Is recovery realistic within the plan's constraints?

4. **Is the fallback currently available?** — Not theoretically available. Available right now, with confirmed capacity, at known cost.

---

## Step 4: Dependency Sequencing Check

Review whether the plan's timeline correctly sequences dependency resolution.

Common errors:
- Dependency assumed to be available is not actually secured yet
- Parallel work tracks that converge on a dependency that hasn't been validated
- Approval cycle time underestimated (treat formal approvals as 2–3× stated timeline until evidence exists otherwise)
- External vendor work not contracted or scoped

For each dependency with lead time > 2 weeks: confirm it has been initiated or contracted, not merely assumed.

---

## Step 5: Concentration Risk

Identify whether risk is concentrated in:

**A single person**: More than one critical path dependency routes through the same individual.

**A single team**: Multiple critical path items require action from the same external team.

**A single vendor**: Multiple system or service dependencies route through the same third-party provider.

**A single approval chain**: Multiple work streams are blocked by the same approval authority.

Concentration risk is multiplicative: one failure blocks multiple things simultaneously.

---

## Output Format

### Dependency Risk Summary

**Critical Dependencies (plan fails if these fail)**:
- [dependency] — Fallback: [Yes/Partial/No] — Early warning: [signal]

**High Risk Dependencies (plan severely impacted)**:
- [dependency] — Current status: [confirmed/assumed] — Lead time: [X]

**Concentration Risk Identified**:
- [person/team/vendor] is load-bearing for [N] separate critical path items

### Unsecured Dependencies (initiated but not confirmed)
- [dependency] — Current status: [state] — Must be confirmed by: [date]

### Recommended Dependency Actions
1. [action] — Owner: [name] — By: [date]
