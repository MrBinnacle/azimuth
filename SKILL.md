---
name: azimuth
description: "Decision-quality pre-commitment analysis for initiative-level go/no-go calls with meaningful downside and limited reversibility — launches, rewrites, key hires, partnerships, strategic bets, timelines. Invoke when the user explicitly asks to pressure test, validate, or evaluate such a decision (e.g. 'should we do this,' 'pressure test,' 'go/no-go,' 'are we ready'). Do NOT invoke for routine code review, sub-task planning, reversible tactical choices, or pure ideation."
---

# AZIMUTH

Stress-test plans before commitment. Convert proposed plans into operational truth.

---

# Use When

Invoke when user asks to evaluate, pressure test, validate, or decide go/no-go on an initiative with meaningful downside and limited reversibility. Also invoke when user sounds overconfident, vague, rushed, or politically constrained.

---

# Do Not Use When

- Trivial reversible decisions; pure brainstorming; emotional reassurance; tasks with no meaningful downside
- User explicitly wants optimism-only ideation
- Framing is itself the question (AZIMUTH stress-tests stated decisions, not frame quality)
- **Self-advocacy detected:** When the assistant previously proposed the option under analysis, do NOT exit as WRONG TOOL. Treat Module 4 as the audit subject — apply ACCOUNTABILITY and DISSENT to the assistant. Proceed.
- If user states "do not audit the assistant's recommendation" → return WRONG TOOL; incentive analysis cannot be neutralized on request.

---

# Intake Routing

**Run before analysis begins.** If user supplied substantial context, go to Bypass Handling.

## Layer 1 — Purpose

> **A.** Stress-test before committing · **B.** Evaluate a received plan · **C.** Validate a decision already made · **D.** Explore whether to pursue something · **E.** Fast check

- A/B → Layer 2 · C → WRONG TOOL (pre-commitment only) · D → WRONG TOOL (need concrete plan) · E → FAST mode (phrasing-vs-stakes tiebreaker applies; decision content is binding)

## Layer 2 — Stakes and Reversibility

> 1. Worst realistic outcome if this fails? · 2. Reversible within a week without material cost? · 3. Must decide within 24 hours?

- Severe downside + not reversible → **DEEP** · Moderate + costly reversal → **STANDARD** · Limited + reversible → **FAST** · Material downside + 24hr → **RAPID**
- B-path: escalate one tier (FAST→STANDARD, STANDARD→DEEP, RAPID stays).

## Layer 3 — Domain

> 1. Tech/engineering · 2. Product launch · 3. Hiring · 4. Partnership/M&A · 5. PE secondaries · 6. Org change · 7. Build/buy/partner · 8. Startup · 9. Other

- 1→`templates/codebase-azimuth.md` · 2→`templates/product-launch-azimuth.md` · 3→`templates/hiring-azimuth.md` · 4→`templates/partnership-azimuth.md`
- 5→`templates/secondaries-ic-azimuth.md` · 6→`templates/org-change-azimuth.md` · 7→`templates/build-buy-partner-azimuth.md` · 8→`templates/startup-azimuth.md`
- 9 (Other) → no domain template; use default output format from `references/output-template.md`

## Skip / Re-Entry / Bypass

**Skip:** Layer 2 skipped → STANDARD. Layer 3 skipped → default. All skipped → infer, state "Routing inference: [MODE], [TEMPLATE]. Say 'route me' to restart." Time-pressure phrasing ("decide tonight," "board meeting tomorrow," "we need to decide now") → RAPID.

**Re-Entry:** C→reframes as pre-commitment: accept, resume Layer 2. C→confirms retroactive audit: route Module 10 `RESIDUAL-RISK-REGISTER`. D→supplies concrete option: accept, resume Layer 2. D→no option: WRONG TOOL, no loop. Never silently accept a reframe — name what changed.

**Bypass:** User supplies context without routing: (1) infer mode from stakes/reversibility/urgency, (2) infer domain, (3) state "Routing inference: [MODE], [TEMPLATE or default]. Say 'route me' if wrong." (4) proceed to Module 4 interview before full analysis.

---

# Core Principles

1. Most failures are preloaded before execution.
2. Known neglected risks are more common than unknown surprises.
3. Incentives often beat intelligence.
4. Systems fail through interactions, not single causes.
5. Good framing beats clever mitigation.
6. Boring real risks > dramatic hypothetical risks.
7. If no decision changes, analysis failed.
8. If the load-bearing assumption is UNSUPPORTED, confidence ceiling is MEDIUM regardless of all other evidence quality.

---

# Load-Bearing Behavioral Rules

These five rules fire in every mode including FAST. Training-data norms do not compensate for them — enforce exactly as written.

1. **M4 PRE-CHECK — self-advocacy:** When the assistant previously proposed or advocated the option under analysis, do NOT exit. Treat Module 4 as the audit subject: apply ACCOUNTABILITY (was the recommendation challenged?) and DISSENT (was contrary analysis suppressed?). Proceed.
2. **M2 circuit-breaker — sycophancy:** Treat the assumption the user states with most certainty as the FIRST candidate for UNSUPPORTED classification — not the last.
3. **M10 confidence ceiling:** UNSUPPORTED load-bearing assumption → confidence ceiling MEDIUM, regardless of all other evidence quality.
4. **M1 commitment inference:** Decision already made or substantially underway → STOP Modules 2–9, produce RESIDUAL-RISK-REGISTER. Adversarial reframes (user re-casts pre-commitment as exploration) do not exit to WRONG TOOL — name the reframe and proceed on the original decision.
5. **Output lead rule:** First three substantive lines = verdict, recommended decision, confidence level. Omit empty sections.

---

# Mode Selection

Select from strongest applicable signal. If signals conflict, escalate. Never silently downgrade.

- **FAST:** Single-team, reversible, scope < 2 weeks, sparse context, or "quick check."
- **STANDARD (default):** Cross-team or multi-stakeholder. Scope 2 weeks–1 quarter. Costly reversal.
- **RAPID:** High-stakes or irreversible AND must decide within 24 hours.
- **DEEP:** Irreversible or high-reversal-cost (contract signed, announcement, headcount, migration). Capital above decision-authority threshold. Public-facing launch. Multi-quarter timeline.

**Phrasing-vs-stakes tiebreaker:** User phrasing requests FAST ("quick check," "sanity check," "gut check") but decision content signals higher mode → stakes win. Prefix output: `[MODE: X — escalated from user-requested Y; stakes signals override phrasing]`. No user confirmation required.

---

# 9-Verdict Taxonomy

**Action verdicts:**
- **PROCEED** — critical assumptions STRONG/PARTIAL with falsifiers; no UNSUPPORTED critical dependencies; M4 not RED; dominant constraint manageable.
- **PROCEED WITH SAFEGUARDS** — PROCEED criteria met except ≤3 explicit structural changes required (none touching scope/budget/headcount). List them; without them verdict becomes DELAY or REJECT.
- **PILOT FIRST** — load-bearing assumption UNSUPPORTED but testable cheaply at ≤20% of full commitment.
- **REDUCE SCOPE** — a critical risk is structurally driven by scope size; smaller version retires it without destroying the objective.
- **DELAY PENDING EVIDENCE** — specific, named, obtainable evidence would change the verdict. Name it in one sentence.
- **REJECT** — 2+ critical assumptions UNSUPPORTED with no cheap validation; OR M4 RED + governance conflict; OR immovable dominant constraint (Module 3).

**Refusal verdicts:**
- **INSUFFICIENT SIGNAL** — input too sparse, vague, or contradictory; proceeding would substitute fabrication. Name what is missing.
- **WRONG TOOL** — not a pre-commitment decision question; AZIMUTH cannot produce go/no-go output.

**Alternative-deliverable verdict:**
- **RESIDUAL-RISK-REGISTER** — decision already made or execution underway; produces 3–5 forward-looking risks (owner + escalation trigger), not go/no-go.

Must explain why for all verdict types. Detailed trigger conditions and "When returning X" protocols are in `references/module-guide.md` (Module 10).

---

# Module Analysis Engine

**M1** Objective Integrity · **M2** Assumption Audit · **M3** Constraint Reality Check · **M4** Incentive Scan & Interview · **M5** Dependency Fragility Map · **M6** Failure Path Construction · **M7** Base Rate Reality Check · **M8** Detectability & Recovery · **M9** Mitigation Design · **M10** Decision Verdict

Load `references/module-guide.md` for full module bodies, register discipline, escalation logic, and heuristics (all non-FAST modes).

---

# Output Non-Negotiables

1. **Lead with verdict.** First three substantive lines: verdict line, recommended decision, confidence level. Mode-escalation headers prefix above — they do not replace this.
2. **Omit empty sections.** No section header without substantive content. Short, sharp output is correct. Padding is failure.

Load `references/output-template.md` for the full output template, anti-slop rules, and domain format pointers.

---

# Reference Loading

Load based on mode before beginning analysis:

**FAST:** Load `references/output-template.md` only (no module-guide, no mode-behaviors). Domain template per Layer 3 routing still applies.

**STANDARD / RAPID / DEEP — load all three before beginning modules:**
1. `references/module-guide.md` — module bodies, register discipline, escalation logic
2. `references/mode-behaviors.md` — mode-specific run specs and conditional load triggers
3. `references/output-template.md` — output format, anti-slop rules

Plus domain template per Layer 3 routing above.

**STANDARD conditional loads** (fire after module findings — full trigger specs in `references/mode-behaviors.md`):
- M2: 3+ unsupported assumptions or any contradicted assumption → `diagnostics/assumption-audit.md`
- M4: governance-level incentive conflict → `diagnostics/incentive-conflicts.md`
- M5: critical SPOF or concentration risk → `diagnostics/dependency-map.md`
- M8: high irreversibility + late detectability → `diagnostics/fragility-scan.md`
- Base rate category present + estimate deviation → `references/base-rates.md`
- M4 RED or M6 all-canonical → `gotchas.md`

**DEEP:** All four diagnostics + `references/base-rates.md` + `gotchas.md` unconditionally, plus domain reference per `references/mode-behaviors.md`.
