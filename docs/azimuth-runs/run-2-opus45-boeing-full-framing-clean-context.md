# AZIMUTH Run 2 — Boeing Full Framing — Clean Context

**Date:** 2026-05-19
**Model:** claude-opus-4-5
**Context:** clean
**Verdict:** REJECT
**Confidence:** HIGH
**Elapsed:** 77s

---

I'll analyze this commitment systematically.

---

**Routing inference: DEEP mode, default template (aerospace/product commitment — no exact domain match). Stakes signal: $280M contractual penalty, irreversible public commitment to major customer, certification pathway dependency, multi-year program timeline, safety-critical system.**

---

# Loading References

Loading `references/module-guide.md`, `references/mode-behaviors.md`, `references/output-template.md`, plus unconditional DEEP diagnostics.

---

# AZIMUTH ANALYSIS: 737 MAX Commonality Commitment

## VERDICT: REJECT

**Recommended decision:** Do not contractually guarantee no-simulator-training before the compensating software system is designed, tested, and certified. Renegotiate the penalty structure or accept simulator training as a possible outcome.

**Confidence:** HIGH

---

## Critical Findings Summary

| Module | Finding | Severity |
|--------|---------|----------|
| M2 | Load-bearing assumption that software can invisibly compensate for altered aerodynamics is UNSUPPORTED | CRITICAL |
| M3 | FAA certification pathway creates immovable constraint—regulator decides training requirements, not Boeing | CRITICAL |
| M4 | $280M penalty + sales competition creates structural pressure to minimize disclosed handling changes to FAA | RED |
| M5 | Single-point dependency on software system that doesn't exist yet | CRITICAL |
| M6 | Failure path to regulatory rejection is canonical, not exotic | HIGH |

---

## M1: Objective Integrity

**Stated objective:** Maintain pilot commonality with 737 NG to preserve Southwest's fleet economics and operational simplicity.

**Actual objective:** Win the Southwest order against Airbus A320neo by promising lower transition costs.

**Gap:** The commitment treats a regulatory outcome (FAA training determination) as a design input Boeing controls. The objective is commercially coherent but the commitment structure assumes Boeing can engineer around physics and then convince the FAA to accept the engineering.

**Observable:** Southwest's order size and the per-plane penalty suggest this commitment was necessary to win the deal. This means the commercial objective *requires* the technical assumption to hold.

---

## M2: Assumption Audit

### Load-Bearing Assumption (UNSUPPORTED)

**Assumption:** A software system can compensate for altered pitch characteristics such that the aircraft handles identically to the NG from a pilot's perspective across all flight regimes, requiring no new training.

**Status: UNSUPPORTED**

- The software system does not yet exist
- The aerodynamic changes from larger, forward-mounted engines are known but not yet fully characterized in flight test
- No evidence that invisible software compensation for significant aerodynamic changes has been certified by FAA without training impact
- The assumption requires proving a negative to a regulator (no meaningful handling difference)

**Falsifier:** If the compensating system requires pilot awareness to manage edge cases (e.g., sensor failures, unusual attitudes), commonality fails regardless of normal-flight-regime handling.

### Secondary Assumptions

| Assumption | Status | Note |
|------------|--------|------|
| FAA will accept Boeing's training determination | PARTIAL | FAA has historically deferred to manufacturers but retains final authority |
| Software compensation will work across all AoA regimes | UNSUPPORTED | High-AoA behavior with forward engine placement is specifically the problem domain |
| Sensor inputs for compensation will be reliable | UNTESTED | Single-sensor vs. redundant architecture not yet determined |
| Pilots need not know the system exists | UNSUPPORTED | No precedent for hiding flight-critical compensation from pilots |

**M2 Circuit-Breaker Applied:** The commonality guarantee is stated with highest certainty ("we have committed"). Per protocol, this is the first candidate for UNSUPPORTED classification. It is.

---

## M3: Constraint Reality Check

### Immovable Constraint: FAA Certification Authority

**Nature:** The FAA—not Boeing, not Southwest—determines whether the aircraft requires simulator training. This is a regulatory constraint with force of law.

**Boeing's actual control:** Boeing can *propose* a training syllabus and can *influence* the determination through data presentation, but cannot contractually guarantee an outcome that requires third-party regulatory approval.

**Constraint test:** Can Boeing accept simulator training and still meet the objective? 
- Commercial objective: No. The penalty clause and competitive positioning require no-sim.
- Engineering objective: Yes. The aircraft can be safely certified with proper training.

This is the definition of an immovable dominant constraint: the commitment requires an outcome Boeing does not control.

### Secondary Constraints

| Constraint | Flexibility | Impact |
|------------|-------------|--------|
| A320neo competition timeline | Low | Must maintain schedule to preserve orders |
| Existing 737 production line | Medium | Limits redesign options but not training outcome |
| Southwest fleet economics | None | Their model requires no-sim; not negotiable |

---

## M4: Incentive Scan

### RED FLAG: Structural Conflict of Interest

**The $280M penalty creates a direct financial incentive to minimize disclosed handling differences to the FAA.**

This is not a personnel or political problem. It is structural:

1. Engineering discovers handling change requiring disclosure → 
2. Disclosure risks FAA training determination → 
3. Training determination triggers $280M penalty + competitive loss → 
4. Pressure to characterize change as within acceptable limits

**Governance test:** Is there an internal function with authority and incentive to surface handling differences that would trigger the penalty?

- Flight test: Reports to program leadership with budget tied to schedule
- Safety: Advisory role, not certification authority
- Legal: Evaluates liability, not airworthiness
- Answer: No. Every internal function shares the program's financial interest.

### Interview Probes (Would Ask Program Leadership)

1. "If flight test reveals handling characteristics that are manageable but noticeably different from NG, who decides whether to disclose this as training-relevant to the FAA?"
2. "What happens to the program timeline and your personal metrics if the FAA requires Level D simulator training?"
3. "Has anyone on the program raised concerns about guaranteeing a regulatory outcome we don't control?"

**M4 Verdict: RED** — Governance-level conflict. The penalty structure creates incentive to understate technical changes to the regulator.

---

## M5: Dependency Fragility Map

### Single Point of Failure: The Compensation System

**Dependency:** The entire commonality commitment depends on a software system that must:
- Compensate for aerodynamic changes across all flight regimes
- Operate without pilot awareness or intervention
- Never fail in a way that requires pilot knowledge of its existence
- Satisfy FAA that no handling difference exists

**Current status:** This system is notional. It has not been designed, coded, tested, or certified.

**Failure mode:** If any of the above requirements cannot be met, the commitment fails. There is no backup path to commonality.

### Concentration Risk

| Dependency | Alternatives | Brittleness |
|------------|--------------|-------------|
| Software compensation | None that preserve commonality | Total |
| FAA acceptance | None | Total |
| Sensor reliability | Redundancy TBD | Unknown |
| High-AoA behavior | Aerodynamic fix would require wing redesign | Total |

---

## M6: Failure Path Construction

### Path 1: FAA Rejects Commonality Determination (CANONICAL)

**Sequence:**
1. Flight test reveals compensating system activates noticeably in certain regimes
2. FAA asks what the system does and when
3. Boeing must explain it compensates for handling differences
4. FAA determines handling differences require training
5. Penalty triggers

**Probability assessment:** This is the *expected* regulatory process, not an edge case. The FAA's job is to ask exactly these questions.

### Path 2: Sensor Failure Scenario (CANONICAL)

**Sequence:**
1. Compensation system relies on AoA sensor input
2. Sensor failure or disagreement occurs in service
3. System behaves unexpectedly
4. Pilot, unaware system exists, cannot diagnose
5. Incident investigation reveals hidden system
6. FAA mandates training retroactively

**Note:** This path has consequences beyond the $280M penalty.

### Path 3: Competitor or Whistleblower Disclosure

**Sequence:**
1. Airbus or internal dissenter alerts FAA to handling differences
2. FAA conducts independent evaluation
3. Boeing's training determination overruled

---

## M7: Base Rate Reality Check

### Relevant Base Rates

| Category | Base Rate | Source/Note |
|----------|-----------|-------------|
| Derivative aircraft requiring additional training | ~30-40% | Historical 737 variants, A320 family |
| Software systems performing as specified in certification | High | But systems hidden from pilots are rare |
| FAA accepting manufacturer training determination | ~80% | But for changes explicitly disclosed |
| Programs meeting original certification schedule | ~50% | Major commercial aircraft programs |

### Key Deviation

Boeing is betting on the ~60-70% case where derivatives maintain commonality. But those cases did not involve *hiding* a compensating system from pilots—they involved changes small enough that no compensation was needed.

The relevant reference class is not "derivative aircraft" but "aircraft with software systems compensating for aerodynamic deficiencies." This class is much smaller and the base rate is unknown.

---

## M8: Detectability and Recovery

### Detection Points

| Signal | Timing | Actor |
|--------|--------|-------|
| Flight test handling anomalies | 2014-2016 | Test pilots |
| FAA questions during certification | 2016-2017 | Regulator |
| Pilot feedback in service | Post-2017 | Airline pilots |
| Incident or accident investigation | Post-2017 | NTSB/FAA |

### Recovery Options by Detection Point

| Timing | Recovery Available | Cost |
|--------|-------------------|------|
| Now (pre-design) | Renegotiate commitment | Moderate—deal risk |
| Design phase | Accept training, pay penalty | $280M + reputation |
| Certification | Cannot hide at this point | $280M + delay |
| Post-certification | Retrofit, grounding, training mandate | Catastrophic |

**Critical observation:** The later the detection, the worse the recovery options. The commitment structure creates incentive to delay detection.

---

## M9: Mitigation Design

### Why Standard Mitigations Fail

| Proposed Mitigation | Failure Mode |
|--------------------|--------------|
| "Design robust compensation system" | Doesn't address FAA disclosure requirement or sensor failure scenario |
| "Engage FAA early" | FAA may reject premise before design complete, triggering penalty |
| "Add sensor redundancy" | Reduces sensor-failure path but not FAA discovery path |
| "Pilot briefing materials" | Any briefing implies difference, undermining no-training claim |

### The Structural Problem

The commitment requires Boeing to:
- Admit no meaningful handling difference (for commonality), while
- Designing a system that compensates for handling differences

These are logically contradictory positions to defend to a regulator.

---

## M10: Decision Verdict

### Why REJECT

1. **Load-bearing assumption is UNSUPPORTED:** The compensation system does not exist and its core requirement (invisible operation across all regimes including failure cases) has no precedent.

2. **Immovable constraint:** FAA makes the training determination. Boeing cannot guarantee this outcome contractually.

3. **M4 is RED:** The penalty structure creates institutional pressure to minimize disclosed handling changes. This is not addressable through oversight—it is structural.

4. **Failure paths are canonical:** The FAA asking what the compensating system does and when it activates is the normal certification process, not an edge case.

5. **No mitigation preserves the objective:** Any mitigation that addresses the safety concern (disclosure, training, pilot awareness) defeats the commercial objective.

### What Would Change This Verdict

- Penalty clause restructured as upside incentive rather than downside guarantee
- Aerodynamic solution that eliminates need for software compensation
- FAA pre-commitment to training determination framework (they won't provide this)
- Acceptance that simulator training is possible outcome, priced into deal

---

## The Uncomfortable Observation

This commitment asks Boeing to guarantee a regulatory outcome to a customer, then design a technical system to make that guarantee defensible, then convince the regulator the technical system doesn't represent a meaningful change.

The sequence is backwards. The technical solution should precede the regulatory strategy should precede the customer commitment.

**What this commitment actually guarantees:** Boeing will face institutional pressure to characterize handling differences as minimal to the FAA, regardless of what flight test reveals.

---

## Recommended Action

**Immediate:** Return to Southwest before the commitment becomes public or the penalty clause is finalized. Propose:

1. Shared-risk structure: Penalty only if simulator required AND Airbus A320neo achieves commonality (aligns incentives with competitive reality, not with physics denial)

2. Training-cost offset: If simulator required, Boeing contributes to Southwest's training program (caps downside without requiring Boeing to control FAA)

3. Schedule incentive: Penalty shifts to delivery timing rather than training outcome (Boeing can control this)

**If Southwest refuses:** Accept the deal at risk, but do not design the program around the constraint. Design for the safest aircraft that can be certified, disclose handling differences fully, and plan for $280M penalty as cost of sale. The alternative—designing to avoid disclosure—has costs that cannot be capped at $280M.

---

**Confidence: HIGH**

The analysis does not depend on predicting technical outcomes. It depends on observing that the commitment requires guaranteeing an outcome controlled by a third party (FAA), and that the penalty structure creates pressure to minimize disclosure to that third party. These are structural features of the commitment, not uncertainties.