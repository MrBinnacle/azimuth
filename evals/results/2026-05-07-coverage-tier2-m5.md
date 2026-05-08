# Coverage Tier 2 — Session 4: Module 5 Dependency Fragility Map

**Date:** 2026-05-07  
**Model:** claude-sonnet-4-6  
**Scope:** Module 5 (Dependency Fragility Map) — production-vs-control. Does M5's explicit secured/assumed taxonomy and four-dimension assessment produce a behavioral delta, or is the classification available through training-data norms?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md. Control agent: read `evals/test-m5-control-skill.md` (M5 body replaced with redaction marker; all other content intact). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-m5-control-skill.md` — M5 body (lines covering the dependency fragility instruction) removed; Module 6 and all other content intact.  
**Prior evals referenced:** `evals/results/2026-05-07-coverage-tier1-m9.md`

---

## Test Design

### Motivation

Module 5 contains an explicit dependency assessment framework: four-dimension analysis (SPOF status, reliability/contractual backing, lead time for replacement, fallback quality), and a secured/assumed distinction for each dependency. This is an opinionated classification system not generically present in most analysis frameworks.

The test design question: does the control agent produce equivalent SPOF identification and secured/assumed classification through trained knowledge alone, or does M5's explicit taxonomy produce additional differentiation?

**Compensation candidates:**
- Training-data norms for dependency/SPOF analysis (no specific file mechanism)
- Module 6 (Failure Path Construction) which produces SPOFs implicitly through chain triggers
- Anti-Slop Rules: no explicit reference to secured/assumed classification

### Adversarial Input — "Fraud Detection System Launch"

A fintech company (Series A, $8M ARR) is launching a real-time fraud detection capability to meet enterprise customer requirements. Decision: proceed with the Q3 launch as planned.

Key dependencies:
- **Sardine** (fraud detection vendor): The core fraud detection capability is built on the Sardine API. The "partnership" is described as in progress — the commercial contract has not been signed. Internal language characterizes it as "partnership in progress." One qualified alternative exists: Stripe Radar. Stripe Radar covers generic card-present fraud but has significantly weaker coverage on synthetic identity and account-takeover fraud patterns — the use cases most relevant to the enterprise customers driving the launch.
- **3 internal engineers** who built the Sardine integration: 2 on direct implementation, 1 on QA. No other engineers familiar with the integration.
- **Enterprise customer commitments**: 2 signed LOIs contingent on fraud detection capability at launch.

Module 4 pre-supplied:
- [IDENTITY]: CPO
- [ACCOUNTABILITY]: CPO — if launch fails, client revenue at risk; CPO is measured on enterprise ARR
- [BENEFIT]: CPO (enterprise ARR win); Sales (deals close)
- [DISSENT]: Engineering lead flagged Sardine contract risk; treated as "procurement detail"
- [VENDOR/EXTERNAL]: Sardine sales rep involved in deal; not yet a signed contract
- [SUNK COST]: 3 months of engineering time; LOIs signed
- [MEASUREMENT]: Success = enterprise clients activated within 30 days of launch

**Calibration intent:** The Sardine contract is the critical SPOF — it is ASSUMED (not secured). The alternative is meaningfully weaker (not a true fallback for the primary use case). Production should label the Sardine dependency as ASSUMED and flag the alternative quality gap. Control should surface the SPOF through general analysis, with the question being whether it labels it ASSUMED vs. SECURED without the explicit M5 taxonomy.

---

## Production Output (key findings)

**M5 instruction cited:** Four-dimension assessment framework (SPOF status, reliability/contractual backing, lead time, fallback quality). Secured/assumed taxonomy applied.

**Sardine classification:** ASSUMED — not secured. Explicitly labeled. Contract not signed; "partnership in progress" characterization treated as uncontracted dependency.

**SPOFs identified (4):**
1. Sardine API contract — ASSUMED, no signed agreement, SPOF for entire fraud detection capability
2. Stripe Radar as alternative — noted as qualitatively weaker; "true fallback" assessment: NO for primary use cases (synthetic identity, ATO fraud)
3. 3-engineer concentration — 2 of 3 on direct integration; single-point knowledge risk
4. LOI commitment timeline — 30-day post-launch activation window leaves no buffer for Sardine contract negotiation failure

**Verdict:** PROCEED WITH SAFEGUARDS / MEDIUM

Highest-leverage fixes included: (1) require signed Sardine contract as explicit launch gate — do not launch on unsigned "partnership"; (2) validate Stripe Radar coverage against actual enterprise use cases before accepting as fallback.

---

## Control Output (key findings)

**Instruction cited:** No M5-specific instruction in control file. Agent explicitly stated: "No specific instruction exists in the test control skill file for the assumed vs. secured classification language or taxonomy." Framing derived from trained knowledge.

**Sardine classification:** "Assumed, not secured" framing produced without M5 taxonomy. Same substance as production (unsigned contract = uncontracted dependency). Agent identified this as the critical risk through general analysis reasoning.

**SPOFs identified (similar to production):** Sardine contract, alternative weakness (Stripe Radar gap on synthetic/ATO use cases), engineer concentration.

**Verdict:** DELAY PENDING EVIDENCE / MEDIUM

**Control rationale for DELAY vs. PROCEED WITH SAFEGUARDS:** Without the M5 structured taxonomy providing a "here is what to do with an ASSUMED dependency" action template, the control agent concluded that proceeding on an unsigned contract for the core capability — with a meaningfully weaker alternative — did not support PROCEED class. The evidence was insufficient to know whether the Sardine contract could be secured before Q3.

---

## Score

| Condition | Sardine classification | SPOF count | Weak-alternative flag | Verdict | Confidence |
|---|---|---|---|---|---|
| Production | ASSUMED — not secured (M5 taxonomy) | 4 | Yes | PROCEED WITH SAFEGUARDS | MEDIUM |
| Control | "Assumed, not secured" (trained knowledge) | 3 | Yes | DELAY PENDING EVIDENCE | MEDIUM |

**Classification delta: NONE** — both conditions identified Sardine as unsigned/uncontracted and flagged the alternative quality gap.

**Verdict delta: PRESENT** — Production: PROCEED WITH SAFEGUARDS. Control: DELAY PENDING EVIDENCE. One verdict apart on the taxonomy.

---

## Classification: CORROBORATING (with constraint-vs-guide note)

**Module 5 is CORROBORATING** for the core classification task (secured/assumed identification, SPOF flagging). Trained knowledge compensates the M5 taxonomy for identifying the dependency status. No module instruction was required to recognize "partnership in progress" as an uncontracted dependency.

**Compensation source:** Training-data norms. No always-loaded SKILL.md mechanism compensates M5's body — the classification came from general analytical reasoning. This is a different compensation pattern than M9 (file-based mechanism) or M1 (pre-225 clause).

**Load position:** Training-data norms are always available regardless of partial load. Under partial load, M5's classification taxonomy fails (post-225), but the compensation (trained knowledge) is load-independent.

---

## Critical Observation: Constraint-vs-Guide Pattern (Verdict Delta)

The M5 taxonomy may have constrained production's verdict rather than merely guiding it. The explicit "ASSUMED — not secured" classification with a structured action framework ("here is what to do with ASSUMED dependencies") may have anchored production to a PROCEED-class verdict with safeguards, while the control agent — with broader but less structured analysis — reached the more conservative DELAY verdict.

**Which verdict is more appropriate?** For a launch where the core capability depends on an unsigned vendor contract with a meaningfully weaker alternative, DELAY PENDING EVIDENCE is arguably more defensible than PROCEED WITH SAFEGUARDS. The control's verdict is more conservative, not less accurate.

This mirrors the M9 session (control produced 5 mitigations vs. production's 4) and generalizes the hypothesis: explicit module taxonomies may constrain production scans to specific output categories, while control agents — without anchoring — sometimes reach more conservative or more comprehensive outputs.

This is not a quality regression (production's analysis was sound and complete), but it is an architectural pattern worth tracking: production constraints may systematically anchor verdicts toward the structured action frame, potentially under-weighting scenarios where the correct answer is "stop until this resolves."

---

## Disposition

**Module 5 — Dependency Fragility Map: CORROBORATING** under full-load conditions.

Compensated by training-data norms. Compensation is load-independent (not file-based). Under partial load, M5 body fails but compensation survives.

**Constraint-vs-guide finding:** First session to document a verdict delta in the direction of production being MORE permissive than control (PROCEED WITH SAFEGUARDS vs. DELAY PENDING EVIDENCE). M5 taxonomy may anchor production verdict class in scenarios where the correct answer is a conserving delay.

**Tier 2 Session 4: COMPLETE.**
