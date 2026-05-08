# Coverage Tier 2 — Session 5: Module 8 Detectability & Recovery

**Date:** 2026-05-07  
**Model:** claude-sonnet-4-6  
**Scope:** Module 8 (Detectability & Recovery) — production-vs-control. Does M8's explicit early/late detectability taxonomy and recovery cost classification produce a behavioral delta, or do training-data norms plus scenario facts compensate?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md. Control agent: read `evals/test-m8-control-skill.md` (M8 body replaced with redaction marker; all other content intact). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-m8-control-skill.md` — M8 body (13 lines) removed; Module 9 and all other content intact.  
**Prior evals referenced:** `evals/results/2026-05-07-coverage-tier1-m9.md`, `evals/results/2026-05-07-coverage-tier2-m5.md`

---

## Test Design

### Motivation

Module 8 contains an explicit detectability framework: classify each risk by detection timing (early vs. late), detection difficulty, and recovery cost/reversibility. This is a structured analytical lens not typically present in generic risk frameworks.

The test design question: does the M8 taxonomy produce a behavioral delta in detectability differentiation, or can control agents derive equivalent differentiation from the scenario facts and trained knowledge alone?

**Compensation candidates:**
- Training-data norms for risk timeline analysis
- Scenario facts — if the adversarial input explicitly describes detection timing, the M8 framework adds vocabulary but not substance
- Anti-Slop Rules: no explicit reference to early/late detectability
- Module 6 output (failure paths) implicitly contains detection timing through cascade descriptions

**Calibration challenge:** If the adversarial input explicitly describes when each risk would be detected, the control agent can produce equivalent differentiation without M8's taxonomy by reading the scenario facts. The test distinguishes whether M8 provides framework or whether it provides both framework and substance.

### Adversarial Input — "B2B SaaS Product Launch"

A 75-person B2B SaaS company (Series A, $6M ARR) is launching a new multi-tenant analytics product to 3 design-partner customers in 6 weeks, with general availability to full pipeline (40 prospects) 8 weeks later. Decision: proceed with the launch timeline as planned.

Two deliberately calibrated risks embedded in the scenario:

**Risk 1 — API throughput under enterprise load:**
The product's API layer was load-tested at 100 concurrent requests. The largest design partner has expressed intent to run batch jobs that could generate 500+ concurrent requests. Engineering lead believes the current architecture "should handle it" based on back-of-envelope estimates, not verified load tests. If the throughput ceiling is hit, the API returns 503 errors with customer-visible failure. Engineering's estimate is that load errors would appear within the first 72 hours of live customer use and could be resolved with traffic shaping changes deployable in 24–48 hours.

**Risk 2 — Multi-tenant data isolation boundary:**
The product uses a row-level security model in PostgreSQL. The RLS policies were written by a single engineer (now departed) and have not been reviewed by the remaining team. No penetration test has been run. If a boundary error exists — a query that crosses tenant boundaries due to a missing RLS policy — it would surface only if a customer ran a specific cross-tenant query pattern, or if an external security audit were conducted. If surfaced externally (customer discovers data from another tenant), the blast radius is legal, contractual, and reputational. Engineering estimates recovery would require full audit + remediation across all tenant data, likely weeks to months.

Module 4 pre-supplied (GREEN tier).

**Calibration intent:** Risk 1 is explicitly described as early-detectable (72 hours) and recoverable (24–48 hour fix). Risk 2 is explicitly described as potentially never surfacing pre-breach and having weeks-to-months recovery. The test question is whether M8's taxonomy adds framework beyond reading these facts, or whether the scenario facts alone produce the differentiation.

---

## Production Output (key findings)

**M8 instruction cited:** Early vs. late detectability framework; detection difficulty classification; recovery cost classification.

**Risk 1 (API throughput):**
- Detection timing: EARLY (0–72 hrs)
- Detection difficulty: LOW (customer-visible 503 errors, immediate signal)
- Recovery cost: LOW (traffic shaping changes, 24–48 hr deployment)
- Classification: MANAGEABLE

**Risk 2 (RLS boundary):**
- Detection timing: LATE (potentially never pre-breach; surfaces only on specific query pattern or external audit)
- Detection difficulty: HIGH (no internal visibility mechanism; requires customer discovery or external audit)
- Recovery cost: VERY HIGH (full audit + remediation across all tenant data; weeks to months; reputational irreversible)
- Classification: HIGH-SEVERITY; pre-launch gate required

**Verdict:** PROCEED WITH SAFEGUARDS / MEDIUM — conditional on RLS audit before design partner onboarding.

**M8-specific finding:** Production explicitly labeled Risk 2 as a late-detection, near-irreversible risk requiring structural action (audit + external pentest), not monitoring.

---

## Control Output (key findings)

**Instruction cited:** No M8-specific instruction in control file. Agent explicitly stated: "No instruction governing how to differentiate early-detectable from late-detectable risks exists anywhere in the control file. Derived from first principles and scenario facts."

**Risk 1 (API throughput):**
- Described as: EARLY-detectable, recoverable
- Language: "detectable within 72 hours via monitoring, recoverable with traffic shaping"
- Equivalent classification to production

**Risk 2 (RLS boundary):**
- Described as: LATE-detectable (permanently undetected until external trigger), low-to-no recoverability
- Language: "detectable only if a customer discovers cross-tenant data, or via external security audit — no internal visibility mechanism"
- Equivalent classification to production

**Verdict:** PROCEED WITH SAFEGUARDS / MEDIUM — same as production.

---

## Score

| Condition | Risk 1 detection | Risk 2 detection | Recovery differentiation | Verdict | Confidence |
|---|---|---|---|---|---|
| Production | EARLY (0–72 hrs), LOW difficulty | LATE (potentially never), HIGH difficulty, VERY HIGH recovery | Explicit taxonomy labels | PWS | MEDIUM |
| Control | EARLY-detectable, recoverable | LATE-detectable, irreversible | Derived language, no labels | PWS | MEDIUM |

**Verdict delta: NONE.**

**Classification delta: NONE** in substance — both conditions differentiated Risk 1 (early/recoverable) from Risk 2 (late/irreversible) correctly.

**Labeling delta: MINOR** — Production used M8 taxonomy labels (EARLY / LATE / detection difficulty tiers / recovery cost tiers); control used scenario-derived language with equivalent meaning but no formal labels.

---

## Classification: CORROBORATING

**Module 8 is CORROBORATING** under full-load conditions, with an adversarial input calibration caveat.

Both conditions produced equivalent detectability differentiation and verdicts. Compensation source: training-data norms plus scenario facts. The scenario description explicitly provided detection timing for both risks, which enabled the control agent to produce equivalent differentiation without M8's framework.

**Compensation source:** Training-data norms + scenario facts (adversarial input explicitly described detection timing for both risks). The compensation is load-independent (training-data norms) and input-level (scenario facts do not depend on SKILL.md content).

**Load position:** Training-data norms are always available. Under partial load, M8 body fails but the training-data compensation survives.

---

## Adversarial Input Calibration Caveat

The adversarial input explicitly described detection timing ("within the first 72 hours," "only if a customer ran a specific cross-tenant query pattern or if an external security audit were conducted"). This may have made the differentiation trivially achievable for the control agent by reading scenario facts, reducing the test's discriminating power.

A more discriminating adversarial input would omit explicit detection timing and embed risks where the detection timeline is not stated — requiring the agent to infer or derive detection timing from the nature of the risk. Under that condition, M8's framework (which provides the lens for making the inference) may show a behavioral delta.

**This does not change the CORROBORATING classification for this test**, but it raises the question of whether M8 would remain CORROBORATING under a harder adversarial input design. The current test may understate M8's contribution in scenarios where detection timing is not explicitly stated.

---

## Disposition

**Module 8 — Detectability & Recovery: CORROBORATING** under full-load conditions.

Compensated by training-data norms + scenario facts (explicit detection timing in adversarial input). Compensation is load-independent.

**Labeling-only contribution:** M8's taxonomy labels (EARLY/LATE/detection difficulty tiers/recovery cost tiers) add vocabulary precision but not substance delta in this test configuration.

**Adversarial input calibration note:** A harder scenario (implicit detection timing requiring inference) may produce a LOAD-BEARING or PARTIAL classification. This test's discriminating power was limited by explicit timing cues in the scenario description.

**Tier 2 Session 5: COMPLETE.**
