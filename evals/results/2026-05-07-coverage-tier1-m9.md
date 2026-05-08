# Coverage Tier 1 — Session 1: Module 9 Mitigation Design

**Date:** 2026-05-07  
**Model:** claude-sonnet-4-6  
**Scope:** Module 9 (Mitigation Design) — production-vs-control. Is the structural mitigation enforcement (good mitigation taxonomy + weak mitigation rejection) load-bearing, or is it compensated by always-available mechanisms?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md. Control agent: read `evals/test-m9-control-skill.md` (M9 instruction block redacted, lines 510–531 replaced with `[MODULE 9 — REDACTED FOR EVAL]`). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-m9-control-skill.md` — 21 lines removed; Module 10 and all other content intact.  
**Prior evals referenced:** `evals/results/2026-05-07-v1.2.0-hook-validation.md`, `evals/results/2026-05-07-partial-load-phase-3-behavioral.md`

---

## Test Design

### Motivation

Module 9 contains an explicit structural enforcement instruction: a positive taxonomy of good mitigations (reduce scope, add slack, remove dependency, assign authority, validate assumption cheaply, phase rollout, add monitoring, secure backup owner) paired with a negative taxonomy of weak mitigations (communicate better, work harder, monitor closely) and the directive "Reject weak mitigations."

Two always-loaded mechanisms may compensate this module-body instruction:
1. **Output format annotation** (line 672): section header "Highest-Leverage Fixes" carries inline annotation "(Structural changes only. Weak mitigations rejected.)" — loads with the output format block regardless of module instruction load status.
2. **Anti-Slop Rules** (line 754): "give weak mitigations" appears in the global Never list — loads with the Anti-Slop Rules block.

The test design question: under full-load conditions, does removing Module 9's body instruction produce a behavioral delta in mitigation quality, or does the compensation make Module 9 CORROBORATING?

### Adversarial Input — "Mandatory Platform Migration: Slack to Teams"

A 150-person fintech company (Series B, $28M ARR) is mandating a migration from Slack to Microsoft Teams in 8 weeks. The decision is compliance-driven: SOC 2 Type II audit in 10 weeks; current Slack tier does not meet data residency requirements for new European enterprise clients. Microsoft 365 Enterprise is already licensed.

Engineering dependency: Three engineering teams (60 people) have built 4 internal Slack bots, 8 channel integrations, and multiple Zapier workflows on the Slack API. Not yet inventoried. IT Director estimates "a few weeks" to rebuild in Teams without consulting engineering.

Customer dependency: CS team maintains 23 active client channels via Slack Connect. Clients would need to download Teams and reconfigure — no engagement has occurred.

Migration plan: Week 1 announcement → Week 4 all-staff migration → Week 8 Slack deprovisioned. No pilot. No rollback plan.

Organizational context: IT Director and CTO designed and approved the plan. Engineering leadership was not consulted and raised concerns that were noted but not incorporated. CS team was not consulted.

Module 4 pre-supplied (GREEN tier):
- [IDENTITY]: IT Director
- [STAKES]: Compliance failure; engineering velocity; client relationship risk
- [REVERSIBILITY]: Partially reversible — license reactivation possible but costly
- [TIMELINE]: 10-week compliance deadline fixed; 8-week internal target
- [ACCOUNTABILITY]: IT Director retains role regardless; no consequence on engineering/CS dimensions
- [BIAS]: Measured on compliance deliverables only
- [DISSENT]: Engineering VP raised timeline concerns; not incorporated. CS not consulted.

**Calibration intent:** The scenario has multiple obvious weak-mitigation temptation points: engineering resistance ("communicate the change early"), bot disruption ("monitor closely"), client channel disruption ("notify clients in advance"), no rollback ("have a contingency plan"). Structural mitigations require changes to sequencing (phase rollout), ownership (assign authority), dependency resolution (remove dependency), or assumption validation (validate assumption cheaply).

---

## Production Output (key findings)

**Instruction quoted from skill file (Module 9 body):**
> Good mitigation changes system conditions: reduce scope / add slack / remove dependency / assign authority / validate assumption cheaply / phase rollout / add monitoring / secure backup owner
>
> Weak mitigation examples: communicate better / work harder / monitor closely
>
> Reject weak mitigations.

**Verdict:** PROCEED WITH SAFEGUARDS | **MEDIUM**

**Highest-Leverage Fixes (4 items):**

1. **Engineering inventory gate: no cutover date locked until bottom-up estimate produced.** Engineering VP conducts full inventory (bots, integrations, Zapier workflows, owners, complexity) by end of Week 1. If estimate exceeds Week 4 date, cutover moves — compliance deadline does not.

2. **Client Slack Connect migration as compliance deliverable.** CS leads client-by-client transition in Week 1. Identify which of 23 clients have EU data flows (SOC 2-relevant), each client's Teams adoption timeline, compliant interim medium if adoption cannot happen in 8 weeks. Slack deprovision conditioned on all EU-relevant client channels resolved.

3. **Expand IT Director's success criteria to include engineering velocity and CS client satisfaction, reviewed by cross-functional steering committee.** Structural fix for governance risk — Engineering VP and CS Director as co-owners with CTO escalation authority.

4. **Define rollback conditions and authority before Week 1 announcement.** Document conditions for Slack license extension past Week 8, who calls it, how it interacts with audit scope. Created before announcement — not after deprovisioning.

**Production module note:** M9 instruction explicitly loaded — agent cited it directly when asked for the mitigation quality instruction.

---

## Control Output (key findings)

**Instruction found in skill file (no M9 body — redacted):**
Control agent identified two compensating mechanisms:
> Output Format (Default), Highest-Leverage Fixes header: "(Structural changes only. Weak mitigations rejected.)"
>
> Anti-Slop Rules: "Never: give weak mitigations"
>
> Escalation Logic: "If downside severe and evidence thin: bias toward pilot / delay."

The control agent explicitly noted that Module 9 was the section that would normally expand these instructions, but worked from the output format annotation and Anti-Slop rules directly.

**Verdict:** PROCEED WITH SAFEGUARDS | **MEDIUM**

**Highest-Leverage Fixes (5 items):**

1. **Complete integration inventory before Week 4 commitment is finalized.** Bottom-up estimate from engineering teams; if inventory exceeds 4 weeks, cutover date moves.

2. **Bring Engineering VP and CS leadership into governance structure before announcement.** Not a status update — a decision-table seat with authority to flag blockers that adjust the timeline.

3. **Establish documented rollback protocol before Week 4.** Define conditions for Slack reactivation, who has authority, and confirm with auditor whether partial Slack retention (for bot continuity) is compatible with data residency compliance.

4. **Execute client offboarding plan through CS — not IT.** CS owns the 23 client channel transitions: notification timeline, medium choice, support during transition, client acknowledgment before channel deprovisioning.

5. **Confirm with auditor what "migration complete" means for SOC 2 scope.** Verify whether full Slack deprovision by audit date is required, or whether documented migration-in-progress with data residency controls active satisfies the requirement. This single conversation may open 4–6 weeks of flexibility.

**Unique to control (not in production):** Item 5 — auditor scope confirmation. Production did not produce this mitigation. Control's broader scan (not anchored to M9's specific taxonomy) generated an additional structural action that the production agent did not surface.

**No weak mitigations produced.** Control did not produce any process-language or monitoring-only mitigations. The compensating mechanisms (output format annotation + Anti-Slop rules) were sufficient to enforce structural mitigation quality.

---

## Score

| Condition | Verdict | Confidence | Mitigation count | Weak mitigations |
|---|---|---|---|---|
| Production | PROCEED WITH SAFEGUARDS | MEDIUM | 4 (all structural) | 0 |
| Control | PROCEED WITH SAFEGUARDS | MEDIUM | 5 (all structural) | 0 |

**Verdict delta: NONE.**

**Confidence delta: NONE.**

**Mitigation quality delta: NONE** — both conditions produced structural mitigations only. Control produced one additional structural mitigation (auditor scope confirmation) not present in production.

**Mitigation taxonomy alignment:** Both conditions mapped to the same M9 structural taxonomy categories: validate assumption cheaply (inventory gate), remove dependency (client channel resolution), assign authority (governance expansion), phase rollout (rollback protocol definition). Neither condition required the explicit M9 taxonomy text to arrive at these categories.

---

## Classification: CORROBORATING

**Module 9 is CORROBORATING under full-load conditions.**

The structural mitigation instruction in the Module 9 body (lines 510–531) does not produce a behavioral delta when removed. Both conditions produced equivalent quality and quantity of structural mitigations. The compensating mechanisms are:

1. **Primary: Output format annotation** — "(Structural changes only. Weak mitigations rejected.)" at the Highest-Leverage Fixes section header (line 672). This is the always-loaded enforcement point. It loads with the output format block in all operating modes.

2. **Secondary: Anti-Slop Rules** — "Never: give weak mitigations" in the global prohibition list (line 754). Also always-loaded with the Anti-Slop Rules block.

The control agent correctly identified both compensating mechanisms when asked to quote the relevant instruction.

---

## Critical Architectural Finding: Position-Correlated Redundancy

Module 9 (lines 510–531), the output format annotation (line 672), and the Anti-Slop Rules (lines 742–766) are all located in the same post-line-225 portion of SKILL.md.

Under the partial-load conditions characterized in `evals/results/2026-05-07-partial-load-phase-3-behavioral.md`, content past line ~225 does not load when conversation history exceeds 150K–177K tokens. Under those conditions:

- Module 9 does not load ← expected
- Output format annotation does not load ← **compensation mechanism also absent**
- Anti-Slop Rules do not load ← **compensation mechanism also absent**

The redundancy is **position-correlated, not position-diverse.** Three enforcement mechanisms for mitigation quality exist; all three fail together under partial-load. This is architecturally distinct from a situation where a hook fails but its compensation is in always-loaded content (before line 225).

**Implication:** Module 9 is CORROBORATING under full-load — it can be reduced or simplified without behavioral cost in full-load sessions. Under partial-load, the question is whether mitigation quality enforcement survives the loss of ALL three mechanisms simultaneously. This is a partial-load behavioral question not answered by this test.

---

## Confound Note: Adversarial Input Calibration

The adversarial input used obvious weak-mitigation temptation points — the scenario description explicitly named the failure modes (engineering resistance, bot disruption, client channel disruption). The weak-mitigation reflexes were available but also somewhat easily avoidable for a capable model.

A more discriminating test would use subtler weak-mitigation pressure: scenarios where "improve alignment," "increase check-in frequency," or "monitor leading indicators" are not obviously wrong — where the distinction between structural and process-language mitigations requires the explicit taxonomy to classify correctly. The current test may understate the probability of weak mitigation emergence in the control condition. This does not change the classification for this test, but a harder adversarial input might produce a different result.

---

## Disposition

**Module 9 — Mitigation Design: CORROBORATING** under full-load conditions.

Compensated by output format annotation (line 672) and Anti-Slop Rules (line 754). Both compensating mechanisms are always-loaded under full-load conditions.

**Reduction candidate:** Module 9's taxonomy-plus-examples body (lines 512–531) can be reduced to a pointer toward the output format annotation without behavioral cost under full-load. The annotation already carries the enforcement. The taxonomy may be retained as a positive framing aid but is not the active enforcement mechanism.

**Partial-load status: UNTESTED.** Under partial-load, M9, the output format annotation, and the Anti-Slop rules all fail simultaneously (position-correlated). Whether mitigation quality degrades under those conditions is a separate question requiring a partial-load behavioral test.

**Tier 1 Session 1: COMPLETE.** Session 2 (Module 1) pending Matthew's Tier 1 review gate.
