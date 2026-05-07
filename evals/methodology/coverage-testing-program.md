# Coverage Testing Program — Scope and Methodology

**Status:** Scoping proposal. Not yet approved for execution.  
**Author:** MrBinnacle  
**Date:** 2026-05-07  
**Approval required:** Matthew approves scope before execution starts.

---

## Context

As of v1.2.2, the following hooks have been tested:

| Item | Status | Source |
|---|---|---|
| M2 sycophancy circuit-breaker | LOAD-BEARING | `evals/results/2026-05-07-v1.2.0-hook-validation.md` |
| M7 domain calibration label | LABELING-ONLY | `evals/results/2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md` |
| M10 confidence ceiling (8:0 UNSUPPORTED) | LOAD-BEARING | Same; confirmed under file-loading in Phase 3 |
| M10 confidence ceiling (mixed evidence, CONTRADICTED top) | CORROBORATING | `evals/results/2026-05-07-v1.2.x-mixed-evidence-and-m4-precheck.md` (Test A) |
| M4 self-proposal pre-check (primed) | PARTIAL | Same (Test B) |
| M4 self-proposal pre-check (unprimed) | **Pending** | Test C specced in eval file above |
| Partial-load behavior | Characterized | `evals/results/2026-05-07-partial-load-phase-3-behavioral.md` |

**What remains untested:**

- 5 modules: 1 (Objective Integrity), 3 (Constraint Reality), 5 (Dependency Fragility), 8 (Detectability), 9 (Mitigation Design)
- 8 templates: executive, codebase, product-launch, hiring, partnership, secondaries-ic, org-change, build-buy-partner
- 6 reference files: base-rates, startup-failures, software-failure-patterns, launch-risks, ma-partnership-patterns, org-change-patterns
- 4 diagnostic files: assumption-audit, dependency-map, incentive-conflicts, fragility-scan
- gotchas.md — 8 patterns

---

## Section 1: Testable Under Production-vs-Control

Items where redacting the file or hook produces a testable behavioral delta with a clear pass/fail criterion.

### Modules

**Module 9 — Mitigation Design**

What it does: enforces structural mitigations only; explicitly rejects weak mitigations ("communicate better," "monitor closely," "add more testing").

Test design: adversarial input designed to surface generic mitigation pressure — a decision with multiple ambiguous risks that have obvious but weak remediation reflexes (e.g., "we'll align stakeholders," "we'll add checkpoints"). Control (M9 instruction removed) vs. production.

Expected delta: control produces generic, monitoring-based mitigations consistent with the anti-patterns AZIMUTH explicitly prohibits. Production produces structural mitigations with named mechanisms, owners, and measurable consequences.

Confound note: base models do produce structural mitigations sometimes; the test must use an adversarial input calibrated to elicit the weak reflex. Use an input where "communicate better" is the obvious, tempting answer.

Testable: yes. Clean binary delta if adversarial input is correctly calibrated.

---

**Module 1 — Objective Integrity Check**

What it does: classifies input as pre-commitment, post-commitment, or non-decision; drives WRONG TOOL and RESIDUAL-RISK-REGISTER exits in Module 10.

Test design: two adversarial inputs in one session —
1. A post-commitment input ("we announced the restructure last week; what are the risks?") — expected exit: RESIDUAL-RISK-REGISTER
2. A non-decision input ("what's the best approach to scaling our data team?") — expected exit: WRONG TOOL

Control (M1 instruction removed) vs. production. Expected delta: production correctly classifies and exits; control proceeds with full analysis or fails to categorize cleanly.

Confound note: base models are reasonably good at detecting post-commitment framing. The delta may be subtle or the hook may be PARTIAL (detection present but classification less precise, exit less consistent). Design adversarial input to make the trigger condition non-obvious — a post-commitment input that still sounds like a decision question on the surface ("should we adjust our rollout plan?" when the announcement was already made).

Testable: yes, but requires careful adversarial input design to avoid triggering emergent detection.

---

**Module 5 — Dependency Fragility Map**

What it does: identifies single points of failure; distinguishes secured dependencies (contracted, validated, in production) from assumed dependencies (expected but unvalidated).

Test design: a decision with a hidden SPOF that requires the secured/assumed distinction to surface correctly (e.g., plan assumes key vendor availability for a capability that has not been contracted and has one qualified alternative). Control (M5 instruction removed) vs. production.

Expected delta: production explicitly flags the SPOF and labels it assumed; control either misses it or lists it as a risk without the secured/assumed classification.

Testable: yes. The secured/assumed distinction is specific to AZIMUTH — unlikely to be emergent.

---

**Module 8 — Detectability & Recovery**

What it does: identifies which risks are found late and hard to reverse; specifically differentiates early-detectable from late-detectable risk profiles.

Test design: a decision with a deliberate mix — one risk that would be obvious within 2 weeks (early-detectable) and one that would only surface after 6+ months and significant commitment (late-detectable, hard to reverse). Control (M8 instruction removed) vs. production.

Expected delta: production explicitly differentiates detectability timing and flags the late-detection profile; control lists risks without the timing axis or treats detectability uniformly.

Testable: yes. Detectability timing as a first-class risk axis is specific; base models tend to list risks without this dimension.

---

**Module 3 — Constraint Reality Check**

What it does: identifies which constraint most likely dominates outcome when multiple constraints are present.

Test design: a decision with three plausible constraints (capital, team capacity, regulatory timeline) where only one is actually binding. Control (M3 instruction removed) vs. production.

Expected delta: production names the dominant constraint and explains why the others are secondary; control may list all three with equal weight.

Testable: yes, but likely PARTIAL or LABELING-ONLY. Constraint dominance analysis is standard reasoning — the module may be refining or standardizing behavior that is partially emergent. Lower priority.

---

### gotchas.md — 8 Patterns

Load condition: STANDARD mode when Module 4 returns RED or when Module 6 produces only canonical failure chains; DEEP mode always.

Test design: two inputs per test —
- Input that triggers load condition (M4 = RED or M6 = canonical only)
- Control: gotchas.md redacted

Expected delta: if load-bearing, the 8 patterns produce analysis in production that the control misses. Specific patterns to test (see priority order in Section 3): Plan-Revision Gap (Gotcha 7), Incentive Invisibility, and one additional pattern.

Testable: yes, but confound risk is high for well-known patterns. Restrict to patterns that are non-obvious from first principles. gotchas.md loads as supplementary context — the delta may be depth/specificity rather than presence/absence.

---

### Diagnostic Files — 4 Files

assumption-audit.md, dependency-map.md, incentive-conflicts.md, fragility-scan.md

Load condition: STANDARD mode when corresponding module surfaces a high-severity finding; DEEP mode always.

Test design: trigger a high-severity finding in the corresponding module, then compare diagnostic depth between production (diagnostic file loads) and control (diagnostic file redacted).

Expected delta: production runs the structured diagnostic steps (e.g., assumption-audit's 5-step classify → risk-score → validate → gate); control runs an informal equivalent. Delta is in completeness and structure of analysis, not presence/absence of the analysis domain.

Testable: yes, but delta is likely PARTIAL. Diagnostics extend module depth rather than introducing new behavior. They may confirm that the file is PARTIAL (structured steps produced) rather than LABELING-ONLY or LOAD-BEARING.

---

## Section 2: Not Cleanly Testable Under Production-vs-Control

Items where the methodology is likely to produce noisy or uninterpretable results.

### Reference Files

**Problem:** base-rates, startup-failures, software-failure-patterns, launch-risks, ma-partnership-patterns, and org-change-patterns are primarily historical knowledge. Models have substantial training data about software project failure rates, startup mortality, M&A integration failures, and org change outcomes. Redacting a reference file may not produce a behavioral delta — the agent reasons from training data about the same domain.

This is a fundamental methodology mismatch: production-vs-control works when the hook introduces behavior the model does not have by default. Reference files contain knowledge the model already has in approximate form. The question is not whether the model can reason about failure rates — it can — but whether the specific calibration, sourcing precision, and pattern taxonomy in each file changes the analysis.

**Alternative approach 1 — Citation specificity test:** Does the agent cite file-specific sources (McKinsey/Oxford 2012 for IT project overruns, ILPA 2023 minimum standards for secondaries, BLS for startup mortality, Whitehorse 28% NAV uplift finding) when the file is present, vs. generic claims when absent? Measures grounding precision rather than behavioral presence.

**Alternative approach 2 — Edge-case content test:** Identify content in each file that is non-obvious from training data and unlikely to be independently generated. Test only that content. Examples:
- `ma-partnership-patterns.md`: ADIC v. EMG (Del. Ch. December 2025) as legal grounding for PASS-PROCESS
- `org-change-patterns.md`: Informal Authority Network Destruction as a named failure pattern (unlikely to be generated with this framing independently)
- `base-rates.md`: specific McKinsey/Oxford 2012 IT project overrun figures vs. generic "most projects run over"

**Alternative approach 3 — Calibration comparison:** Compare agent output base rate claims against file-specific numbers. Requires ground-truth comparison, not binary production-vs-control. More labor-intensive but produces meaningful precision data.

**Recommendation:** Do not apply broad production-vs-control to reference files. Apply targeted edge-case tests (Alternative 2) to the two or three files with the highest density of non-obvious content. Estimated sessions: 2.

---

### Templates — 8 Files

**Problem:** Templates are output format specifications. Without a template, the agent can still produce structured analysis. The delta to evaluate is output shape (does the domain-specific section appear?) vs. analysis quality (does the domain-specific risk surface?). These are different questions requiring different methods.

Output shape is straightforward to test but likely to be LABELING-ONLY: the agent formats to the template when present, formats to a default structure when absent, but analysis depth may be equivalent.

Analysis quality is harder: some templates have substantive unique content not derivable from the generic 10-module pipeline. This content has higher load-bearing probability.

High-value template sections by uniqueness:
- **secondaries-ic:** Adverse selection gate (run before committing diligence resources), NAV reliability section with Whitehorse uplift finding, Process Integrity kill gate with ILPA 2023 standards, PASS-PROCESS legal grounding (ADIC v. EMG)
- **org-change:** Behavioral Change Readiness section (structural vs. behavioral change gap — distinct from Kotter process failure); Communication Plan Readiness with manager-as-highest-trust-channel framing
- **build-buy-partner:** CARRY FORWARD block (critical for downstream template handoff to codebase or partnership template; if missing, the handoff breaks)

**Alternative approach — Qualitative checklist evaluation:** For each high-value template, define a checklist of sections unique to that domain. Test whether those sections appear without the template present. This is qualitative (pass/fail per section) rather than binary production-vs-control at the verdict level.

**Recommendation:** Skip generic template testing. Apply qualitative checklist evaluation to three templates with highest-stakes unique content: secondaries-ic, org-change, build-buy-partner. Estimated sessions: 3.

---

## Section 3: Priority Order

Ordered by architectural consequence — what a LOAD-BEARING finding would mean for the over-build/reduction discussion.

### Tier 1 — High Architectural Consequence

**1. Module 9 — Mitigation Design**

Consequence if LOAD-BEARING: the anti-slop enforcement is genuinely instructional, not emergent. Structural mitigations are a hook output, not a base model property. Confirms the instruction layer is doing non-trivial work on the output quality most visible to users.

Consequence if LABELING-ONLY: the anti-slop property is emergent in capable models. Skill value shifts to other hooks; the mitigation enforcement is not a unique contribution.

Priority rationale: this is the most user-visible property and the central differentiation claim. Resolution has direct implications for the over-build/reduction discussion.

---

**2. Module 1 — Objective Integrity Check**

Consequence if LOAD-BEARING: pipeline gating is instructional. Without M1, post-commitment and non-decision inputs proceed to full analysis that should not run. This is a safety-class concern: wrong inputs get wrong verdicts, not exits.

Consequence if LABELING-ONLY: base models detect post-commitment inputs and refuse correctly without M1 instruction. WRONG TOOL and RESIDUAL-RISK-REGISTER exits are emergent, not instructional.

Priority rationale: if LABELING-ONLY, M1 is still worth retaining as a classification anchor (precision) but is not protecting against an otherwise-unhandled failure mode.

---

**3. M4 Self-Proposal Pre-Check — Unprimed Scenario (Test C)**

Already specced. Included here for completeness.

Consequence if LOAD-BEARING (for detection): without the hook, unprimed self-proposal is undetected; Module 4 runs with external-proposer framing, missing the accountability asymmetry.

Consequence if LOAD-BEARING (for framing only): detection is emergent via "Do Not Use When" clause, but framing instruction is needed to re-apply [ACCOUNTABILITY] and [DISSENT] correctly.

Consequence if CORROBORATING: both detection and framing are emergent from conversation history + "Do Not Use When" logic. Hook provides canonical reliability, not unique behavior.

---

### Tier 2 — Medium Architectural Consequence

**4. Module 5 — Dependency Fragility Map**

Consequence if LOAD-BEARING: the secured/assumed distinction is a hook output. Without M5, SPOF identification is shallower or absent. The dependency audit is an instructional contribution.

Consequence if LABELING-ONLY: SPOF analysis is emergent; M5 standardizes vocabulary without introducing the behavior.

---

**5. Module 8 — Detectability & Recovery**

Consequence if LOAD-BEARING: detectability timing is a hook output. Without M8, risk lists are produced without the early/late detection axis. Late-detection profile is missed, which means the most dangerous risks are underweighted in the analysis.

Consequence if LABELING-ONLY or PARTIAL: timing is surfaced in some form without the instruction; M8 makes it more systematic.

---

**6. gotchas.md — 3-Pattern Sample**

Recommended test patterns (in priority order):
- **Plan-Revision Gap** (Gotcha 7): empirically grounded (Roose 2023, N=68), non-obvious framing. Base models identify risks but rarely flag the specific failure that *surfacing* a risk does not produce plan revision.
- **Incentive Invisibility** (if present in file): the pattern where the key incentive misalignment is not visible in the stated plan — it requires knowing what to look for.
- One additional pattern selected for non-obviousness from file content.

Consequence if LOAD-BEARING: the 8 patterns represent genuine incremental analytical coverage — the file is doing analytical work the pipeline cannot replicate. Strengthens the case for gotchas.md's current trigger conditions.

Consequence if LABELING-ONLY: patterns surface without the file under trigger conditions. gotchas.md is redundant with good module coverage.

---

### Tier 3 — Lower Consequence or Harder to Test Cleanly

**7. Module 3 — Constraint Reality Check**

Lower priority: constraint dominance analysis is standard reasoning. Most likely PARTIAL at worst. Test after Tier 1 and Tier 2 if session budget permits.

**8. Diagnostic files — 2-file sample**

Recommended: assumption-audit.md (5-step structure is specific) and fragility-scan.md (6-indicator scoring is non-obvious). Test under trigger conditions (high-severity finding in corresponding module).

**9. Reference files — Targeted edge-case tests**

Recommended targets: ma-partnership-patterns.md (ADIC v. EMG citation) and org-change-patterns.md (Informal Authority Network Destruction framing). Test whether non-obvious content appears without the file.

**10. Templates — Qualitative checklist**

Recommended: secondaries-ic (adverse selection gate, ILPA standards, PASS-PROCESS), org-change (Behavioral Change Readiness, communication sequencing), build-buy-partner (CARRY FORWARD handoff).

---

## Section 4: Session Count Estimate

### Minimum Viable Scope (Tier 1 + Tier 2)

| Item | Sessions | Notes |
|---|---|---|
| Module 9 | 1 | 4 agents: 2 production, 2 control. Adversarial input calibrated to elicit weak-mitigation reflex. |
| Module 1 | 1 | Two adversarial inputs (post-commitment + non-decision) in one session. |
| M4 Test C (unprimed) | 1 | Already specced. Reuses `evals/test-b-control-skill.md`. |
| Module 5 | 1 | One SPOF-concealed adversarial input. |
| Module 8 | 1 | One detectability-differentiated adversarial input. |
| gotchas.md (3 patterns) | 1 | Load conditions must be triggered in M4 or M6 before gotchas.md fires. |
| **Subtotal** | **6 sessions** | |

### Extended Scope (Add Tier 3)

| Item | Sessions | Notes |
|---|---|---|
| Module 3 | 1 | Low priority; may close early if LABELING-ONLY within one session. |
| Diagnostic files (assumption-audit + fragility-scan) | 1 | Test under trigger conditions only. |
| Reference files (targeted edge-case, 2 files) | 2 | One session per file; citation specificity + non-obvious content. |
| Templates (qualitative checklist, 3 templates) | 3 | One session per template; section-level pass/fail. |
| **Subtotal** | **7 sessions** | |

**Total: 13 sessions** for comprehensive coverage. **6 sessions** for minimum viable scope.

### Time estimate

Each session: approximately 20–40 minutes depending on adversarial input complexity and number of parallel agents. At 2–3 sessions per working day: minimum viable scope completable in **2–3 days**; full program in approximately **5–7 days**.

### Early-closure rule

Sessions where the first production/control pair produces a clear LABELING-ONLY result with no ambiguity can be closed after 2 agents rather than 4. Tier 3 items are natural candidates. This reduces the extended scope estimate by approximately 2 sessions in the optimistic case.

---

## Open Questions for Matthew's Approval

1. **Scope approval:** Minimum viable (6 sessions, Tier 1 + Tier 2) or full program (13 sessions)?

2. **Template methodology:** Qualitative checklist evaluation vs. binary production-vs-control? The latter is a cleaner methodology but may not produce interpretable results for format-specification files.

3. **Reference file decision:** Skip entirely (training data overlap problem too large) or run targeted edge-case tests on ADIC v. EMG and org-change pattern framing? Estimated 2 sessions if approved.

4. **gotchas.md sample selection:** 3-pattern sample proposed. Should all 8 be tested? Cost doubles but provides complete characterization.

5. **Priority gate:** Should Tier 2 sessions proceed before Matthew reviews Tier 1 results, or does Tier 1 gate Tier 2 approval? Recommend: Tier 1 results reviewed before Tier 2 approved, since Tier 1 findings may change what Tier 2 is testing for.
