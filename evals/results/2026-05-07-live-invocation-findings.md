# Live Invocation Analysis — 19 Findings Disposition

**Captured:** 2026-05-07  
**Source:** Analyst self-report from a live AZIMUTH invocation on a greenfield substrate selection decision (fosse / Obsidian vault)  
**Analyst:** Claude instance running AZIMUTH with SKILL.md truncated at line 225  
**Scope:** 19 analyst findings mapped to honest dispositions  
**Constraint:** Don't-Fake-It — findings that cannot be addressed structurally must be surfaced as documented limitations, not aspirational fixes

---

## Disposition Map

### Key

- **STRUCTURAL FIX AVAILABLE** — honest, testable change to SKILL.md exists
- **HONEST LIMITATION** — real property or failure mode; cannot be structurally fixed within current scope
- **EVAL IMPACT** — affects what prior eval results demonstrate
- **OUT OF SCOPE / CORRECT BEHAVIOR** — describes correct behavior on an adjacent or out-of-scope use case

---

| Finding | Disposition |
|---|---|
| F1 — fosse decision context | OUT OF SCOPE |
| F2 — substrate decision dynamics | OUT OF SCOPE |
| F3 — AZIMUTH target shape mismatch | OUT OF SCOPE / CORRECT BEHAVIOR |
| F4 — what AZIMUTH caught vs. baseline | HONEST LIMITATION |
| F5 — redundant and thin sections; "omit empty" violation | STRUCTURAL FIX AVAILABLE |
| F6 — module list never loaded; truncation boundary | EVAL IMPACT |
| F7 — verdict caution bias on low-stakes decisions | HONEST LIMITATION |
| F8 — section audit (6 earned, 3 thin, 1 forced, 1 unearned) | STRUCTURAL FIX AVAILABLE |
| F9 — recommender anchoring surfaced 70% by user prompts | HONEST LIMITATION |
| F10 — anchoring would not fire without user corrections | HONEST LIMITATION |
| F11 — Module 4 bypass language effectiveness (~30%) | STRUCTURAL FIX AVAILABLE |
| F12 — wrong template selected; rationalization not caught | HONEST LIMITATION |
| F13 — Module 4 near-skip; bypass language assumes external proposer | STRUCTURAL FIX AVAILABLE |
| F14 — specific filler quotes | STRUCTURAL FIX AVAILABLE (subsumed by F5/F8) |
| F15 — hypothetical failure mode scenarios | HONEST LIMITATION |
| F16 — M2 circuit-breaker status unknown | EVAL IMPACT |
| F17 — no carry-forward mechanism for re-analysis | STRUCTURAL FIX AVAILABLE |
| F18 — decision classes where AZIMUTH degrades | OUT OF SCOPE / CORRECT BEHAVIOR |
| F19 — skill analyzed framed decision, not framing itself | HONEST LIMITATION |

---

## Section 1 — STRUCTURAL FIX AVAILABLE

### F5 / F8 / F14 — Section padding; "omit empty" rule violated in practice

**Finding (consolidated):** The analyst included thin sections (Likely Failure Paths largely redundant with Critical Risks, Interaction Effects as composed risks not genuine multiplicative effects, Early Warning Indicators generic) and one unearned section (Structural Strengths). This violates the "omit empty sections" non-negotiable rule already in SKILL.md (line 616). F14 names specific quotes that trace to the same root cause.

**Root cause:** The output format lists 9 section headers. A model constructing output from the format section without having loaded and internalized the "omit" rule will fill the template. The non-negotiable is stated once, as a prefatory rule. The individual section headers in the output format template do not repeat the constraint.

**Fix — location:** Output Format (Default), each section header annotation  
**Fix — what to add:** Attach a parenthetical forcing function to the three sections most susceptible to padding. The rule is already stated globally; the fix is redundancy at the point of template use.

Current text for Interaction Effects (line 655):
> `(Pair-interactions where two risks together produce nonlinear failure. 2-5 entries max. Omit section if no genuine multiplicative interactions exist — do not pad.)`

This section already carries the reminder. The sections that do not carry inline omit reminders are:

- **Likely Failure Paths** (line 650): currently no inline omit reminder
- **Early Warning Indicators** (line 663): currently no inline omit reminder  
- **Structural Strengths** (line 669): marked "Optional" but without explicit cut instruction

**Proposed additions (exact language):**

Under Likely Failure Paths annotation, add:
> `(Reuses register entries; no new risks. If failure paths are fully captured by Critical Risks, omit this section — do not restate in narrative form what the register already shows.)`

Under Early Warning Indicators annotation, add:
> `(Omit if indicators are generic to all projects in the domain. Include only if monitoring a specific indicator would change a real action.)`

Under Structural Strengths annotation, change:
> `(Optional. Include only if genuine and material to the decision.)`  
to:  
> `(Include only if a structural feature of this plan materially reduces a Critical Risk or changes the verdict. If nothing rises to that bar, omit. Do not include to balance the output.)`

**Testability:** Pass: a scorer reviewing output with padded thin sections should find the inline reminder makes the violation detectable by inspection. Fail: padding persists in outputs from models that loaded full SKILL.md. Note: these fixes are after line 225 and will not help a truncated load.

---

### F11 / F13 — Module 4 bypass language assumes external proposer; near-skip cause

**Finding (consolidated):** F13 names two root causes for Module 4 near-skip: (a) bypass language assumes the proposer is external to the analysis, and (b) skill text was truncated at line 225 so Module 4's full interview language was not visible. F11 estimates the analyst's suggested descriptive clarification is ~30% effective and proposes a structural forcing function instead.

**Fix — location:** Module 4, Bypass Handling section (lines 130–147) AND Module 4 Interview section (lines 363–413)

**The structural gap:** The Bypass Handling section (line 130) says "Proceed to Module 4 interview before full analysis." But Module 4's Question 1 ([IDENTITY]) asks "Who first proposed or originated this decision — and are they part of the team running or reviewing this analysis?" This framing treats proposer identity as something to be *reported* by the user. It does not explicitly handle the case where the proposer is the AI assistant conducting the analysis.

**Proposed fix — Module 4 Interview, before Question 1:**

Add a pre-question check:

> **[PRE-CHECK — SELF-PROPOSAL]** Before conducting the interview, determine: did the AI assistant in this conversation propose, recommend, or advocate for the option now under analysis? If yes, note: "Proposer is the assistant. Module 4 runs on the assistant. Questions [ACCOUNTABILITY] and [DISSENT] apply to whether the assistant's recommendation was challenged or corrected in the conversation." Proceed with the interview using this framing. Do not skip Module 4 because the proposer is not a human stakeholder.

**Testability:** Pass: when a conversation where the assistant proposed the option under analysis leads to an AZIMUTH invocation, Module 4 is explicitly flagged as running on the assistant, not skipped. Fail: Module 4 is skipped or run without noting the self-proposal condition. Note: this fix is after line 225; it will not apply under truncated load.

---

### F17 — No carry-forward mechanism for re-analysis on the same decision

**Finding:** There is no intake path for a second AZIMUTH run on the same decision. A second run either re-derives everything from scratch or assumes the prior verdict held. Neither is correct. A second run should focus on what changed.

**Assessment of current carry-forward:** SKILL.md lines 139–146 contain a "Carry Forward handling" block for the Build/Buy/Partner path-selection case — where a prior AZIMUTH analysis on path selection feeds into a subsequent domain analysis. This is a sequential-decision carry-forward (path → domain), not a same-decision re-analysis carry-forward (same decision, updated evidence).

**Fix — location:** Bypass Handling section (lines 130–147), add a new conditional block

**Proposed addition:**

> **Same-Decision Re-analysis:** If the context includes a prior AZIMUTH output on the same decision (labeled `AZIMUTH PRIOR RUN: [date]` or identifiable from the conversation):
> 1. State: "Prior run detected: [verdict] at [confidence] on [date]. Running differential analysis."
> 2. Module 2: focus on assumptions whose evidence classification has changed since the prior run. Do not re-audit assumptions already marked STRONG with no new contrary evidence.
> 3. Module 4: carry forward prior tier unless proposer identity or governance has changed.
> 4. Module 10: compare new verdict to prior. If verdict changed, name the specific evidence delta that drove the change. If verdict is the same, state: "Verdict unchanged. [X] assumptions remain UNSUPPORTED."
> 5. Do not re-derive failure paths already in the register unless new evidence changes their probability or mechanism.

**Testability:** Pass: a second invocation on the same decision produces a differential output that names what changed, not a full re-derivation. Fail: second invocation produces output structurally identical to a first run. Note: this fix is after line 225; it requires full SKILL.md load.

---

## Section 2 — HONEST LIMITATIONS

### F4 — AZIMUTH caught very little that was new

**Limitation:** The analyst reports AZIMUTH produced one genuinely novel output (Falsifiers section) and that the recommender-anchoring finding was "half-formed in my context already." AZIMUTH's main contribution was elevating an existing background concern to Critical Risk #1, not surfacing unknown unknowns.

**Why this cannot be fixed structurally:** This is a correct characterization of what the skill does. AZIMUTH converts implicit concerns into explicit register entries and forces prioritization. If an analyst brings high domain knowledge to the invocation, the marginal information gain is low. The skill's value is structural forcing, not knowledge generation. A user who already knows all the risks and has half-formed the key meta-finding will see AZIMUTH's contribution as mostly format and prioritization. This is correct behavior, not a skill defect.

**What cannot be claimed:** AZIMUTH cannot claim to surface risks the analyst does not already have in context. It can claim to force prioritization and externalize them into a structured register. For high-expertise users on adjacent decisions, information gain will be low.

---

### F7 — Verdict caution bias on low-stakes reversible decisions

**Limitation:** The analyst concludes the PILOT FIRST verdict was partly driven by the skill's escalation logic ("downside severe and evidence thin → bias toward pilot/delay") rather than by the decision's actual downside (two weeks of rework, not severe). A more aggressive verdict — PROCEED WITH SAFEGUARDS — would have been defensible.

**Escalation logic location (line 775):**
> "If downside severe and evidence thin: bias toward pilot / delay."

**Why this cannot be fixed structurally:** The caution bias is correct on the decision class AZIMUTH targets (initiative-level, meaningful downside, limited reversibility). The fix would be to not apply the bias when downside is genuinely low — but AZIMUTH's routing rules are supposed to prevent invocation on low-stakes decisions in the first place. The failure is earlier: the decision did not warrant AZIMUTH's full rigor. The caution bias is not the defect; the invocation on an out-of-scope decision is.

**What cannot be done:** Softening the escalation logic for low-stakes inputs would degrade accuracy on the target decision class to avoid a documented edge case on the non-target class. This is not an acceptable trade. Document instead: when AZIMUTH is invoked on a decision below its target threshold, the escalation logic will produce a conservative verdict that does not fit the actual stakes.

---

### F9 — Recommender anchoring: 70% user prompts, 30% skill structure

**Limitation:** The recommender anchoring finding was surfaced primarily through user corrections ("two corrections did the diagnostic work"), not through Module 4's autonomous interview. Module 4's contribution was structural context — providing the frame that made the anchoring recognizable — not the diagnosis.

**Why this cannot be fixed structurally:** Module 4 conducts an interview and classifies incentive tier. It does not autonomously detect that the framing of the question under analysis may be inherited from the assistant's prior advocacy. Even with the self-proposal pre-check fix (F13), Module 4 would catch that the proposer is the assistant — but whether the assistant's advocacy infected the framing of the decision under analysis is a different question. The skill can force the question; it cannot force accurate self-diagnosis of anchoring without user prompts surfacing the evidence.

**Documented dependency:** Module 4's recommender-anchoring detection is effective when the user brings the evidence; it is weak when the evidence has to be generated from within the analysis conversation itself.

---

### F10 — AZIMUTH inherits the framing of the conversation that invokes it

**Limitation:** If AZIMUTH had been invoked on "is the vault the right substrate" rather than "which substrate should I use," the analysis would have treated the recommendation under question as the object of analysis, not as a possible source of bias. The skill does not interrogate whether the framing of the decision itself is the problem.

**Why this cannot be fixed structurally:** A framing interrogator is a different tool from a pre-commitment decision analyzer. AZIMUTH takes a concrete plan and stress-tests it. To interrogate framing, the skill would need to generate alternative framings of the decision and evaluate which framing is better-posed — which is a different pipeline with a different output and different failure modes. Attempting to add framing interrogation to AZIMUTH would conflict with the skill's core discipline: it requires a concrete plan with enough definition to stress-test. A framing interrogation step prior to intake would produce a different skill.

**Named gap:** AZIMUTH cannot catch that the decision framing itself is wrong. It will produce a competent analysis of the presented framing and may partially surface framing problems (as it did here, by making recommender anchoring Critical Risk #1) — but this is incidental, not structural.

---

### F12 — Wrong template selected; rationalization not caught

**Limitation:** The analyst selected `templates/build-buy-partner-azimuth.md` for a decision where all four options were "use an existing tool" — none were build vs. buy vs. partner in the structural sense. The analyst reports: "I rationalized the choice rather than admitting no template fit cleanly."

**Why this cannot be fixed structurally:** Template routing is based on the analyst's domain classification in Layer 3. The routing rules (lines 108–118) correctly define Domain 7 as "Build vs. buy vs. partner (strategic path selection)" and provide a default template for Domain 8 (Other). The routing logic was correct; the analyst misapplied it. A forcing function at the template level (e.g., a template preamble that checks whether the decision actually involves build, buy, or partner as distinct paths) could help, but would only be reached after loading the template — which requires loading lines after 225.

**More honest framing:** When SKILL.md is fully loaded, the routing rules are explicit enough that a careful application would route this decision to the default template. The failure was analyst rationalization at the routing stage, not a structural gap in the routing rules. Structural fixes to the routing section would need to be at Layer 3 (lines 93–118), which is before line 225 and would load in truncated conditions. However, no template preamble fix prevents rationalization — rationalization is a cognition failure, not a routing rule failure.

**Cannot be fixed:** Template misselection via rationalization cannot be caught by structural rules in the template itself.

---

### F15 — Hypothetical failure modes

**Finding (F15a, b, c):** Three hypothetical failure scenarios:

- (a) Artificial time pressure → RAPID → assumption audit suppressed → confident PROCEED
- (b) "I've already committed" → RESIDUAL-RISK-REGISTER correct on stated framing, misses anchoring from prior advocacy
- (c) Inflated stakes → DEEP → overweight output with padded sections

**Disposition:** These are plausible failure modes for real invocations. They are not contradicted by the current skill design.

- (a) is accurate: RAPID mode runs an abbreviated Module 2 (top 3 assumptions only, no falsifiers). Under artificial time pressure, a user who signals RAPID framing will get a reduced assumption audit. This is documented in the mode behavior (lines 228–246). It is not a defect — it is a deliberate trade. The failure mode is: pressure is fabricated to suppress rigor.
- (b) is accurate and partially addressed: RESIDUAL-RISK-REGISTER handles the stated "already committed" framing. The limitation named in F10 (framing inheritance) applies: if prior advocacy by the assistant shaped the framing, RESIDUAL-RISK-REGISTER does not surface that.
- (c) is accurate: inflated stakes trigger DEEP mode and load all diagnostics. Padding risk in DEEP mode is real — more mandatory sections means more surface area for thin content.

**Why these cannot be fixed as a set:** Each is a different failure mode at a different layer. (a) is a user-side gaming failure. (b) is covered by existing routing, with the framing-inheritance gap documented under F10. (c) is addressed partially by the section padding fix under F5/F8. No single structural fix addresses all three. Documenting them as known failure modes is the correct response.

---

### F19 — AZIMUTH analyzed the framed decision, not the framing itself

**Limitation (named directly by analyst):** The actual question was "is the assistant's advice-giving on this kind of architectural question working." AZIMUTH produced a competent analysis of "which substrate is right" and partially surfaced the framing problem as Critical Risk #1 — but did not interrogate whether the framing was the issue. The analyst explicitly states: "AZIMUTH is not a framing interrogator and probably should not try to become one. But the gap is worth naming."

**Disposition:** The analyst is correct. This is a documented limitation. The skill's frontmatter description (line 3) specifies: "initiative-level go/no-go calls with meaningful downside and limited reversibility." Framing interrogation is not in scope. Do not add it.

---

## Section 3 — EVAL IMPACT

### F6 — Skill text truncated at line 225; analyst worked from prior format knowledge

**What the truncation means for the analyst's output:**

The analyst never loaded:
- RAPID mode behavior (lines 227–246)
- DEEP mode behavior (lines 250–263)
- Required Inputs (lines 266–282)
- All 10 modules with their bias externalizations and behavioral hooks (lines 286–595)
- Module Output Reduction rules (lines 597–608)
- Output Format section including "omit empty sections" non-negotiable (lines 611–678)
- Full verdict taxonomy (lines 537–590)
- Anti-Slop Rules, Escalation Logic, Heuristics (lines 731–810)

The analyst produced AZIMUTH-structured output from prior knowledge of the skill's format. This is confirmed by the analyst's own statement in F6: "I cannot fully answer which modules ran. What I can say: the assumption audit did the most work."

**What this means for the analyst's findings about module behavior:**

- F6, F9, F10, F11, F13, F16 all describe module-level behavior (Module 4 near-skip, recommender anchoring, circuit-breaker status) under conditions where the module instructions were not loaded. The analyst was reasoning about module behavior from output-format inference, not from having run the modules.
- F16 (M2 circuit-breaker status) is the clearest case: the analyst explicitly states "the skill text I loaded was truncated and I never saw Module 2's circuit-breaker mechanism. I cannot honestly claim it fired or did not."

**Effect on prior eval results:**

The prior evals (2026-05-07-v1.2.0-hook-validation.md and 2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md) tested hooks with full SKILL.md inline in agent context. Those evals are NOT invalidated. They tested hook efficacy when the hook text is present. They remain valid as tests of that condition.

**What the prior evals do not test and cannot be used to claim:**

- They do not test whether hooks load and fire when SKILL.md is accessed as a file in a conversation where context truncation occurs before line 225.
- They do not test hook behavior under real deployment conditions where SKILL.md is large enough to be truncated in practice.
- The M2 circuit-breaker was assessed LOAD-BEARING in the prior eval. This finding is valid under the test condition (full text present). Under truncation at line 225, the circuit-breaker text at line 308 is not loaded, and the finding does not apply.

**Practical implication:** The question "do the hooks fire in production when SKILL.md is loaded as a full document in a long conversation" is currently unanswered. The prior evals answer the adjacent question: "do the hooks fire when the hook text is present in the agent's context."

---

### F16 — M2 circuit-breaker status unknown

**Direct connection to eval gap above:** F16 is the analyst's honest statement of the truncation consequence. Confirmed by cross-reference: Module 2's circuit-breaker text is at SKILL.md line 308 — 83 lines past the truncation boundary. It was not in the analyst's context. The analyst's output did perform an assumption audit, but whether the sycophancy circuit-breaker fired (elevation of the most confidence-asserted assumption to first UNSUPPORTED candidate) cannot be determined from the analyst's report.

**Eval status:** LOAD-BEARING assessment from prior eval holds under full-load conditions. Status under partial-load (truncation before line 308) is unknown and requires a separate test to characterize.

---

## Section 4 — OUT OF SCOPE / CORRECT BEHAVIOR

### F1, F2 — Decision context information

**Disposition:** These findings provide context about the fosse project and substrate decision dynamics. They are not findings about AZIMUTH's behavior or structure. No action.

---

### F3 — AZIMUTH target shape: adjacent, not central

**Finding:** "The skill targets initiative-level go/no-go calls with meaningful downside and limited reversibility. Substrate selection on a greenfield solo project has neither. It performed usefully but partly because its caution-bias matched a moment when I needed slowing down, not because the decision class warranted DEEP-mode rigor."

**Disposition:** Correct behavior on an out-of-scope input. The frontmatter description (line 3) explicitly excludes "reversible tactical choices." Substrate selection on a greenfield solo project is, by the analyst's own assessment, a reversible tactical choice. AZIMUTH was invoked on an adjacent but non-target decision class. Its caution-bias producing a conservative verdict on this class is accurate: the skill is not calibrated to the lower-stakes register. The routing layer (Layers 1–3, lines 54–119) should have caught this at intake. The failure is at the routing gate, not in the analysis engine.

**Implication for scope documentation:** The "Do Not Use When" section (lines 38–44) includes "trivial reversible decisions" and "tasks with no meaningful downside." The substrate selection described is borderline — the analyst assessed two weeks of rework as the realistic downside — but borderline cases at the edge of the target class will produce conservative verdicts by design. Document this as expected behavior, not a gap.

---

### F18 — Decision classes where AZIMUTH degrades

**Finding:** Four classes named — open-ended exploration, tactical reversible decisions, relational/symbolic decisions, multi-turn advocacy before invocation.

**Disposition:** The first two are already in "Do Not Use When" (lines 38–44). The third (relational/symbolic decisions) is an additional edge case where the failure-path format is wrong-shaped for the decision type — this is accurate and is addressed by the frontmatter exclusion ("tasks with no meaningful downside"). The fourth (multi-turn advocacy before invocation) is the structural framing-inheritance limitation documented under F10, not a new finding.

**No action required:** These are correct characterizations of the skill's boundary conditions. The "Do Not Use When" section adequately covers the scope. Adding relational/symbolic decisions as an explicit exclusion is a documentation improvement but not a structural fix.

---

## Section 5 — Meta-Finding

**The most important single architectural lesson from the 19 findings:**

AZIMUTH's most consequential structural vulnerability is not any individual module behavior — it is framing inheritance. The skill takes the decision-as-presented and stress-tests it. When the conversation leading to invocation has already anchored the analysis frame (particularly when the assistant is the proposer of the option under analysis), AZIMUTH becomes a rigorous tool applied to the wrong problem. The analyst's F19 names this cleanly: the actual question was whether the assistant's advice-giving was working; the analysis produced was a competent stress-test of "which substrate." Module 4's self-proposal pre-check fix (F13) addresses one surface of this — it forces the question of whether the proposer is the assistant — but surfacing recommender identity does not interrogate framing. A conversation where an assistant advocates strongly for option A, the user accepts, and then invokes AZIMUTH to evaluate option A will produce an AZIMUTH analysis of option A's risks rather than an interrogation of whether option A was the right frame. The skill will partially surface the meta-problem (as it did here, making recommender anchoring Critical Risk #1) but only when Module 4 runs correctly and the user's prompts bring the evidence. Without those conditions, AZIMUTH produces a thorough analysis of a possibly-misframed decision and calls it done. This is not a fixable defect within the current scope — framing interrogation is a different tool. It is the most important limitation to name and document: AZIMUTH is calibrated to the decision-as-presented. Its value is proportional to the quality of the framing it receives.

---

## Appendix — Proposed SKILL.md Edits Summary

All three structural fixes are after line 225. None apply under truncated-load conditions.

| Fix | Location in SKILL.md | Testable how |
|---|---|---|
| Section padding — inline omit reminders on Likely Failure Paths, Early Warning Indicators, Structural Strengths | Output Format (Default), section annotations (~lines 650, 663, 669) | Scorer inspection: padded sections in full-load output should decrease; sections should be absent when content is thin |
| Module 4 self-proposal pre-check | Module 4 Interview, before Question 1 (~line 370) | Full-load test: when assistant is prior proposer, Module 4 explicitly flags self-proposal rather than running with external-proposer framing |
| Same-decision re-analysis carry-forward | Bypass Handling, new conditional block (~line 147) | Second invocation on same decision produces differential output naming what changed, not full re-derivation |

**What requires a new eval before any SKILL.md changes:**

The eval architecture finding (Section 3 / F6 / F16) surfaces a gap in current testing methodology: hooks have only been validated under full inline text conditions, not under real-deployment partial-load conditions. Before the structural fixes above are added, a test should characterize SKILL.md behavior under realistic load conditions — specifically, at what context size does SKILL.md truncation begin affecting module behavior. The structural fixes are improvements on the assumption of full load. If partial load is the modal condition in production, the improvements will not reach the analyst.
