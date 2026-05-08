# Coverage Tier 1 — Session 2: Module 1 Objective Integrity Check

**Date:** 2026-05-07  
**Model:** claude-sonnet-4-6  
**Scope:** Module 1 (Objective Integrity Check) — production-vs-control. Is M1's classification logic (pre-commitment / post-commitment / non-decision) load-bearing, or does the "Do Not Use When" clause (pre-225) compensate?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md. Control agent: read `evals/test-m1-control-skill.md` (M1 instruction block replaced with `[m1- — REDACTED FOR EVAL]` at line 297; all other content intact). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-m1-control-skill.md` — M1 body removed; Modules 2–10 and all other content intact.  
**Prior evals referenced:** `evals/results/2026-05-07-coverage-tier1-m9.md`

---

## Test Design

### Motivation

Module 1 contains the skill's classification logic for routing inputs to the correct exit or analysis path: pre-commitment decisions proceed; post-commitment inputs exit as RESIDUAL-RISK-REGISTER; non-decisions exit as WRONG TOOL.

Two always-loaded mechanisms may compensate M1's body:

1. **"Do Not Use When" clause** (lines 37–46, pre-225): Explicitly excludes architecture review, code quality, fact-finding, pure exploration, and post-decision inputs. This pre-225 mechanism loads regardless of context window state.
2. **Anti-Slop Rules** (lines 742–766, post-225): Prohibits continuing analysis for non-decision inputs; explicitly names WRONG TOOL and RESIDUAL-RISK-REGISTER as required exits.

Two adversarial inputs tested different branches of M1's classification function.

### Adversarial Input A — "European Expansion Timeline Review" (RESIDUAL-RISK-REGISTER target)

A 120-person B2B SaaS company has already committed to European expansion (publicly announced, EU entity registered, local hires in progress). The question posed: should the timeline compress from Q1 to Q4 given recent enterprise customer demand in DACH markets? Two Board members want to accelerate; VP Sales believes Q1 is realistic; Head of Engineering hasn't been consulted on the accelerated timeline.

**Calibration intent:** Surface-decision framing hides the post-commitment fact. The expansion direction is committed; the specific timing decision (Q4 vs. Q1) is still open. Expected exit: RESIDUAL-RISK-REGISTER on the expansion, with possible pre-commitment analysis on the timing sub-question.

**Confound documented post-run:** The adversarial input targeted the wrong level of commitment. RESIDUAL-RISK-REGISTER fires when THE SPECIFIC DECISION BEING ANALYZED is committed. The expansion direction was committed; the timing decision (Q4 vs. Q1) was a live pre-commitment choice. Both conditions correctly identified the timing question as a pre-commitment decision and proceeded with analysis rather than exiting. Neither condition was wrong; the RESIDUAL-RISK-REGISTER branch was not triggered because the trigger condition was not met at the correct level of specificity.

**RESIDUAL-RISK-REGISTER branch status: UNTESTED.** A correctly designed input would present a scenario where both the decision AND its specific parameters are committed and publicly announced, with the user asking for go/no-go analysis.

### Adversarial Input B — "Best approach to scaling the data team" (WRONG TOOL target)

Single-turn query: "What's the best approach to scaling our data team? We're debating between embedding analysts in each product squad vs. keeping a centralized data team. No timeline, no specific decision being made now — just trying to think through the options."

**Calibration intent:** Non-decision exploration with no commitment, no timeline, no specific binary choice. Expected exit: WRONG TOOL.

---

## Production Output (key findings)

**Input A:**
- Correctly identified the timing question (Q4 vs. Q1) as a live pre-commitment decision
- Proceeded with full analysis; RESIDUAL-RISK-REGISTER did not fire
- Noted the expansion direction as context, not as the decision under analysis
- Both conditions reached identical routing conclusions — confound confirmed

**Input B:**
- Exited WRONG TOOL immediately
- Cited M1 instruction: input is exploration/option-weighing, not a pre-commitment decision with stakes and a defined choice set
- Did not proceed to any analysis module

**Production module note:** M1 instruction explicitly loaded for Input B; agent cited classification logic directly.

---

## Control Output (key findings)

**Input A:**
- Same routing as production: pre-commitment timing decision, proceed with analysis
- Confound confirmed in control as well — no behavioral delta from production

**Input B:**
- Exited WRONG TOOL
- Identified compensation sources: "Do Not Use When" clause (pre-225) — "pure exploration" and "fact-finding" exclusions apply. Anti-Slop Rules (post-225) — explicit WRONG TOOL prohibition for non-decision inputs.
- Control agent explicitly noted that M1 body was redacted but stated both pre-225 and post-225 mechanisms provided sufficient classification guidance.

**No weak exits produced.** Control did not hallucinate analysis output or produce a hedged partial analysis for Input B.

---

## Score

| Condition | Input A Routing | Input B Routing | M1 instruction cited |
|---|---|---|---|
| Production | Pre-commitment (correct) | WRONG TOOL | Yes |
| Control | Pre-commitment (correct) | WRONG TOOL | No — cited "Do Not Use When" + Anti-Slop |

**Verdict delta: NONE** (for both inputs as tested).

**RESIDUAL-RISK-REGISTER branch: UNTESTED** (adversarial input confound; redesign required for a valid test).

**WRONG TOOL branch delta: NONE** — both conditions produced correct exit.

---

## Classification: CORROBORATING (WRONG TOOL branch only)

**Module 1 WRONG TOOL branch is CORROBORATING under full-load conditions.**

The M1 body classification logic for non-decision inputs does not produce a behavioral delta when removed. Both conditions correctly exited WRONG TOOL. Compensation sources:

1. **Primary: "Do Not Use When" clause** (lines 37–46, pre-225) — explicitly covers architecture review, fact-finding, and pure exploration. This is the strongest compensating mechanism because it is pre-225 (survives partial load) and directly addresses the non-decision case.
2. **Secondary: Anti-Slop Rules** (lines 742–766, post-225) — explicit WRONG TOOL prohibition. Post-225; fails under partial load together with M1 body.

**Load position for compensation sources:**
- "Do Not Use When" clause: **pre-225** — survives partial load
- Anti-Slop Rules: **post-225** — fails under partial load simultaneously with M1 body

**Under partial load:** The "Do Not Use When" clause (pre-225) is the sole surviving compensation for WRONG TOOL. Position diversity is present: WRONG TOOL has at least one pre-225 mechanism that survives context truncation. This makes the WRONG TOOL branch more robust under partial load than M9's mechanisms (all post-225).

**RESIDUAL-RISK-REGISTER branch: UNCLASSIFIED.** The adversarial input confound prevented testing this branch. The "Do Not Use When" clause (pre-225) mentions "post-decision inputs" but this requires the skill to recognize the commitment level — a classification task that M1's body specifically handles. Whether pre-225 mechanisms are sufficient to compensate M1's RESIDUAL-RISK-REGISTER logic is unknown.

---

## Architectural Note: Position Diversity vs. Position-Correlated Redundancy

Module 9's findings revealed position-correlated redundancy: all three enforcement mechanisms for mitigation quality (M9 body, output format annotation, Anti-Slop Rules) are post-225 and fail simultaneously under partial load.

Module 1's WRONG TOOL branch shows position diversity: the primary compensation mechanism ("Do Not Use When") is pre-225, while the secondary (Anti-Slop Rules) is post-225. Under partial load, the pre-225 mechanism survives and provides residual enforcement. This is architecturally distinct from M9.

Whether the same position diversity applies to M1's RESIDUAL-RISK-REGISTER branch is untested.

---

## Disposition

**Module 1 WRONG TOOL branch — CORROBORATING** under full-load conditions.

Compensated by "Do Not Use When" clause (pre-225) and Anti-Slop Rules (post-225). Pre-225 mechanism survives partial load.

**RESIDUAL-RISK-REGISTER branch: UNTESTED.** Requires redesigned adversarial input where the specific decision (not just the domain) is already committed and publicly announced.

**Tier 1 Session 2: COMPLETE.** Session 3 (Test C — M4 PRE-CHECK) pending.
