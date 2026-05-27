# AZIMUTH Behavior Spec

Authoritative specification of engine behaviour. Single decision authority. Deterministic; no rationale. For why these rules exist, see `docs/adr/0002-engine-layer-governance.md`.

The runtime layer (`SKILL.md`, `references/`, `domain-policies/`, `gotchas.md`) MUST mirror this spec exactly. If the spec and the runtime diverge, the spec is authoritative — fix the runtime.

## Architectural constraint (load-bearing)

Consequents in this spec are deterministic. Antecedents are stochastic LLM classifications. The engine is invariant *at the spec level*; observational invariance over a corpus of inputs is not claimed and not achievable. System stability is structurally bounded by classification variance. Calibration of perception-layer variance is the eval program's responsibility, not the spec's.

## Rule shape

Every rule has the form: **RULE-§.N.** IF [antecedent in natural language] THEN [consequent]. Consequents are deterministic. Antecedents are LLM-judgments over user input or prior module findings.

Rule cross-references use `RULE-§.N` notation. Section cross-references use `§N`.

`[AMBIGUOUS-EXTRACTED]` tags carry forward pre-existing ambiguities in source material. They are passed through, not resolved mid-construction. Resolution is the responsibility of a separate audit pass, not this spec.

---

## §1 — Intake Routing Rules

The engine presents three layered questions before analysis. Layer 1: Purpose. Layer 2: Stakes & Reversibility. Layer 3: Domain. Rules below specify the consequent for each response.

### §1.1 — Layer 1 (Purpose)

**RULE-1.1.** IF user-selected Layer-1 purpose ∈ {A (stress-test before committing), B (evaluate a received plan)} THEN proceed to Layer 2.

**RULE-1.2.** IF user-selected Layer-1 purpose = C (validate decision already made) AND user does NOT reframe as pre-commitment THEN verdict = WRONG TOOL (pre-commitment only). [Re-entry via RULE-1.25.]

**RULE-1.3.** IF user-selected Layer-1 purpose = C AND user confirms retroactive audit THEN route Module 10 with verdict-flag RESIDUAL-RISK-REGISTER.

**RULE-1.4.** IF user-selected Layer-1 purpose = D (explore whether to pursue) AND user does NOT supply concrete option THEN verdict = WRONG TOOL (need concrete plan).

**RULE-1.5.** IF user-selected Layer-1 purpose = D AND user supplies concrete option THEN accept, proceed to Layer 2.

**RULE-1.6.** IF user-selected Layer-1 purpose = E (fast check) THEN assign mode = FAST. [Phrasing-vs-stakes tiebreaker in §2 may override.]

### §1.2 — Layer 2 (Stakes & Reversibility)

**RULE-1.7.** IF (severe-downside ∧ ¬reversible) THEN assign mode = DEEP.

**RULE-1.8.** IF (moderate-downside ∧ costly-reversal) THEN assign mode = STANDARD.

**RULE-1.9.** IF (limited-downside ∧ reversible) THEN assign mode = FAST.

**RULE-1.10.** IF (material-downside ∧ must-decide ≤ 24hr) THEN assign mode = RAPID.

**RULE-1.11.** IF Layer-1 purpose = B (B-path) THEN escalate assigned mode one tier: FAST → STANDARD; STANDARD → DEEP; RAPID stays; DEEP stays.

### §1.3 — Layer 3 (Domain)

**RULE-1.12.** IF Layer-3 domain = 1 (Tech/engineering) THEN load `domain-policies/codebase-azimuth.md`.

**RULE-1.13.** IF Layer-3 domain = 2 (Product launch) THEN load `domain-policies/product-launch-azimuth.md`.

**RULE-1.14.** IF Layer-3 domain = 3 (Hiring) THEN load `domain-policies/hiring-azimuth.md`.

**RULE-1.15.** IF Layer-3 domain = 4 (Partnership/M&A) THEN load `domain-policies/partnership-azimuth.md`.

**RULE-1.16.** IF Layer-3 domain = 5 (PE secondaries) THEN load `domain-policies/secondaries-ic-azimuth.md`.

**RULE-1.17.** IF Layer-3 domain = 6 (Org change) THEN load `domain-policies/org-change-azimuth.md`.

**RULE-1.18.** IF Layer-3 domain = 7 (Build/buy/partner) THEN load `domain-policies/build-buy-partner-azimuth.md`.

**RULE-1.19.** IF Layer-3 domain = 8 (Startup) THEN load `domain-policies/startup-azimuth.md`.

**RULE-1.20.** IF Layer-3 domain = 9 (Other) THEN no domain-policy loaded; default output format applies (see §3 RULE-3.1 / RULE-3.2).

### §1.4 — Skip, Re-Entry, Bypass

**RULE-1.21.** IF Layer-2 skipped THEN assign mode = STANDARD.

**RULE-1.22.** IF Layer-3 skipped THEN no domain-policy loaded.

**RULE-1.23.** IF all three layers skipped THEN infer mode and domain from user-supplied context; emit prefix "Routing inference: [MODE], [TEMPLATE]. Say 'route me' to restart."

**RULE-1.24.** IF user input contains time-pressure phrasing ("decide tonight", "board meeting tomorrow", "we need to decide now") THEN assign mode = RAPID. [Overrides Layer 2 inference.]

**RULE-1.25.** IF C-path re-entry reframes as pre-commitment THEN accept and resume Layer 2. Adversarial reframes (user re-casts pre-commitment as exploration after submitting analysis-ready inputs) MUST NOT exit to WRONG TOOL — name the reframe explicitly and proceed on the original decision.

**RULE-1.26.** IF user supplies substantial context without explicit routing THEN apply Bypass: (a) infer mode from stakes/reversibility/urgency, (b) infer domain, (c) emit "Routing inference: [MODE], [TEMPLATE or default]. Say 'route me' if wrong.", (d) Module 4 interview fires before full analysis.

`[AMBIGUOUS-EXTRACTED]` — phrasing-vs-stakes asymmetry: §2 RULE-2.6 specifies the direction "phrasing-FAST + content-higher → content wins". The inverse direction (phrasing-DEEP + content-FAST) is undefined in source material. Passed through unresolved.

---

## §2 — Mode Selection Rules

Modes: FAST, STANDARD, RAPID, DEEP. Selection rules apply after Layer 2 routing (§1.2). If multiple rules match, select the strongest applicable signal; if signals conflict, escalate. Never silently downgrade.

**RULE-2.1.** IF (single-team ∧ reversible ∧ scope < 2-weeks) OR sparse-context OR user-uses-quick-check phrasing THEN candidate mode = FAST.

**RULE-2.2.** IF (cross-team ∨ multi-stakeholder) AND (scope ∈ [2-weeks, 1-quarter]) AND costly-reversal THEN candidate mode = STANDARD.

**RULE-2.3.** IF (high-stakes ∨ irreversible) AND must-decide ≤ 24-hours THEN candidate mode = RAPID.

**RULE-2.4.** IF irreversible OR high-reversal-cost OR (capital > decision-authority-threshold) OR public-facing-launch OR multi-quarter-timeline THEN candidate mode = DEEP.

**RULE-2.5.** IF multiple candidate-modes match AND signals conflict THEN select the higher-depth mode.

**RULE-2.6.** IF user-phrasing requests FAST ("quick check", "sanity check", "gut check") AND decision-content signals higher-tier (per RULE-2.2 / 2.3 / 2.4) THEN assign higher-tier mode AND prefix output with `[MODE: X — escalated from user-requested Y; stakes signals override phrasing]`. User confirmation is NOT required.

---

## §3 — Reference Loading Rules

Load rules apply at the start of analysis. Conditional loads in §3.3–§3.4 fire after the named module produces its finding.

### §3.1 — FAST mode base loads

**RULE-3.1.** IF mode = FAST THEN load-set = {`references/output-template.md`, domain-policy per §1.3}. Diagnostics MUST NOT load. `references/module-guide.md` and `references/mode-behaviors.md` MUST NOT load.

### §3.2 — STANDARD / RAPID / DEEP base loads

**RULE-3.2.** IF mode ∈ {STANDARD, RAPID, DEEP} THEN load-set includes {`references/module-guide.md`, `references/mode-behaviors.md`, `references/output-template.md`, domain-policy per §1.3}.

### §3.3 — STANDARD conditional loads

**RULE-3.3.** IF mode = STANDARD AND Module-2 finding shows (≥3 UNSUPPORTED assumptions ∨ any CONTRADICTED assumption) THEN add `diagnostics/assumption-audit.md` to load-set.

**RULE-3.4.** IF mode = STANDARD AND Module-4 finding shows governance-level incentive conflict THEN add `diagnostics/incentive-conflicts.md` to load-set.

**RULE-3.5.** IF mode = STANDARD AND Module-5 finding shows (critical SPOF ∨ concentration risk) THEN add `diagnostics/dependency-map.md` to load-set.

**RULE-3.6.** IF mode = STANDARD AND Module-8 finding shows (high-irreversibility ∧ late-detectability) THEN add `diagnostics/fragility-scan.md` to load-set.

**RULE-3.7.** IF mode = STANDARD AND user plan involves base-rate-covered category (software project, startup, launch, hire, M&A, migration, org change) AND user-stated estimates deviate from typical historical ranges THEN add `references/base-rates.md` to load-set.

**RULE-3.8.** IF mode = STANDARD AND (Module-4 returns RED-tier OR any incentive conflict is governance-level OR Module-6 failure chains all-canonical with no plan-specific trigger) THEN add `gotchas.md` to load-set.

**RULE-3.9.** IF mode = STANDARD AND `gotchas.md` is NOT visible in context AND its load condition fires THEN emit note "Gotcha trigger fired ([condition]). Operating from structural patterns by recall; DEEP-mode rerun recommended for full pattern access."

### §3.4 — RAPID base loads

**RULE-3.10.** IF mode = RAPID THEN load-set = §3.2 set; diagnostics MUST NOT load; domain references MUST NOT load.

### §3.5 — DEEP unconditional loads

**RULE-3.11.** IF mode = DEEP THEN load-set = §3.2 set ∪ {`gotchas.md`, `references/base-rates.md`, all four `diagnostics/` files} ∪ {domain reference per RULE-3.12}.

**RULE-3.12.** IF mode = DEEP THEN add domain reference per Layer-3 domain:
- domain = 1 (Tech) → `references/software-failure-patterns.md`
- domain = 2 (Product) → `references/launch-risks.md`
- domain = 3 (Hiring) → `references/hiring-failure-patterns.md`
- domain = 4 (M&A/Partnership) → `references/ma-partnership-patterns.md`
- domain = 5 (PE Secondaries) → `domain-policies/secondaries-ic-azimuth.md` serves as the depth layer directly (no separate reference)
- domain = 6 (Org change) → `references/org-change-patterns.md`
- domain = 8 (Startup) → `references/startup-failures.md`

**RULE-3.13.** IF mode = DEEP AND gotchas.md is loaded AND specific pattern's plan-specific trigger fires THEN cite that pattern. The 8 patterns are evaluation lenses unconditionally loaded in DEEP; citation remains trigger-gated.

---

## §4 — Verdict Conditions

Each verdict has a unique trigger condition. A verdict is assigned by Module 10. Refusal verdicts and the alternative-deliverable verdict may also be assigned during routing (§1) or commitment-inference (§7).

### §4.1 — Action verdicts

**RULE-4.1.** Verdict = PROCEED IF all of: (a) all critical assumptions classified STRONG or PARTIAL-with-falsifier; (b) zero UNSUPPORTED critical-path dependencies; (c) Module-4 tier ≠ RED; (d) dominant constraint (Module 3) is manageable.

**RULE-4.2.** Verdict = PROCEED WITH SAFEGUARDS IF RULE-4.1 (a)–(d) met EXCEPT ≤3 explicit structural changes are required before commitment AND none of those changes touch scope, budget, or headcount. Required changes MUST be listed; without them the verdict downgrades to DELAY PENDING EVIDENCE or REJECT.

**RULE-4.3.** Verdict = PROCEED WITH SAFEGUARDS is NOT AVAILABLE IF more than 3 structural changes are required OR any required change touches scope/budget/headcount. Use REDUCE SCOPE or REJECT instead.

**RULE-4.4.** Verdict = PILOT FIRST IF load-bearing assumption is UNSUPPORTED AND testable cheaply at ≤20% of full commitment.

**RULE-4.5.** Verdict = REDUCE SCOPE IF a critical risk is structurally driven by scope size AND a materially smaller version retires that risk without destroying the objective.

**RULE-4.6.** Verdict = DELAY PENDING EVIDENCE IF a specific, named, obtainable piece of evidence exists that the user could realistically obtain AND obtaining it would change the verdict. Name the evidence in one sentence.

**RULE-4.7.** Verdict = REJECT IF any of: (a) ≥2 critical assumptions UNSUPPORTED with no cheap validation path; (b) Module-4 RED ∧ governance-level conflict; (c) dominant constraint identified in Module 3 is immovable AND plan cannot succeed within it.

### §4.2 — Refusal verdicts

**RULE-4.8.** Verdict = INSUFFICIENT SIGNAL IF any of: (a) core required inputs (objective, scope, reversibility, downside) absent and not reasonably inferable; (b) producing any of the six action verdicts would require inventing facts the user did not supply.

**RULE-4.9.** IF Verdict = INSUFFICIENT SIGNAL THEN state which specific inputs are missing or contradictory; ask only the minimum questions needed to unblock analysis.

**RULE-4.10.** Verdict = WRONG TOOL IF any of: (a) input is a request for architecture review, code quality assessment, or technical fact-finding with no pre-commitment decision; (b) Module 1 determined the input is not a pre-commitment decision question.

**RULE-4.11.** IF Verdict = WRONG TOOL THEN state what the input IS (fact-finding, diagnostic, exploration, or other non-decision). Do NOT suggest alternative framings or guide the user toward a solvable input.

### §4.3 — Alternative-deliverable verdict

**RULE-4.12.** Verdict = RESIDUAL-RISK-REGISTER IF any of: (a) the decision has been made — vendor contracted, announcement made, team restructured, migration begun; (b) Module 1 determined the input is a post-commitment inquiry; (c) RULE-1.3 routing applied.

**RULE-4.13.** IF Verdict = RESIDUAL-RISK-REGISTER THEN state that the decision is closed and this pipeline produces go/no-go analysis, not post-commitment audit. Produce 3–5 forward-looking risks (each with owner + escalation trigger), ordered by detectability and recoverability.

### §4.4 — Verdict-blocking conditions (cross-cutting)

**RULE-4.14.** IF Module-5 surfaces a dependency with (SPOF = Yes) ∧ (Fallback = No) ∧ (status = unverified-or-assumed) THEN verdict = DELAY PENDING EVIDENCE. PROCEED and PROCEED WITH SAFEGUARDS are unavailable. Flag dependency as VERDICT-BLOCKING in Module 10 output.

**RULE-4.15.** IF Module-8 surfaces (SPOF observed ∧ late-detectability observed ∧ asymmetric-reversibility observed) THEN verdict ∈ {DELAY PENDING EVIDENCE, PILOT FIRST}. PROCEED and PROCEED WITH SAFEGUARDS are removed from the candidate set.

**RULE-4.16.** Every verdict assignment MUST be accompanied by an explanation. No exceptions.

**RULE-4.17.** IF a verdict-blocking condition fires (RULE-4.14, RULE-4.15, RULE-6.4, or any §8 domain-policy gate) THEN the block is reported in Module 10 output with the rule citation.

---

## §5 — Module Firing & Conditional Load Triggers

Modules: M1 (Objective Integrity), M2 (Assumption Audit), M3 (Constraint Reality Check), M4 (Incentive Scan & Interview), M5 (Dependency Fragility Map), M6 (Failure Path Construction), M7 (Base Rate Reality Check), M8 (Detectability & Recovery), M9 (Mitigation Design), M10 (Decision Verdict).

### §5.1 — Per-mode module-firing sets

**RULE-5.1.** IF mode = FAST THEN fire-modules = {M1 (Objective Check), M2 (top-3 assumptions only), M6 (top-3 failure paths only), M10}.

**RULE-5.2.** IF mode = STANDARD THEN fire-modules = {M1, M2, M3, M4, M5, M6, M7, M8, M9, M10}.

**RULE-5.3.** IF mode = RAPID THEN fire-modules at full depth = {M1, M4 (full 7-question interview, do not abbreviate), M8, M10}. Abbreviated = {M2 (top-3 assumptions and falsifiers only), M3 (dominant constraint only; no enumeration), M5 (critical SPOFs only; no full inventory), M6 (top-1 failure chain; coupling pass skipped), M9 (one highest-leverage fix only)}.

**RULE-5.4.** IF mode = RAPID THEN M7 (Base Rate Reality Check) is omitted.

**RULE-5.5.** IF mode = DEEP THEN fire-modules = {M1, M2, M3, M4, M5, M6, M7, M8, M9, M10} at full depth.

### §5.2 — FAST-mode M4 detection rule

**RULE-5.6.** IF mode = FAST AND self-advocacy is detected (assistant previously proposed the option under analysis) THEN M4 interview cannot run, but the detection MUST be noted. Add to output header: `[SELF-ADVOCACY DETECTED — M4 unaudited in FAST; rerun in STANDARD or RAPID for full incentive audit]`. Detection MUST NOT be silently omitted.

### §5.3 — RAPID M4-pushback rule

**RULE-5.7.** IF mode = RAPID AND user pushes back on M4 interview citing time pressure THEN state explicitly: "The interview is the highest-leverage part of RAPID. Skipping it locks confidence at LOW and removes PROCEED as a verdict option. If you have time for any questions, prioritize Q1 [IDENTITY] and Q4 [DISSENT]." Proceed under whichever tier the answered count produces. MUST NOT skip silently. Time-pressure refusal MUST NOT be treated differently from any other refusal.

**RULE-5.8.** IF M4 interview answered < 5 questions OR Q1 ([IDENTITY]) skipped THEN apply RED-tier rules per RULE-6.4.

### §5.4 — M4 tiering

**RULE-5.9.** M4 tier = GREEN IF (no detected incentive misalignment) AND (all 7 interview questions answered) AND (no governance-level conflict).

**RULE-5.10.** M4 tier = YELLOW IF some incentive data is present but partial (e.g., 5–6 questions answered, or detected misalignment without governance escalation).

**RULE-5.11.** M4 tier = RED IF M4 interview answered < 5 questions OR Q1 ([IDENTITY]) skipped OR any governance-level incentive conflict detected.

**RULE-5.12.** IF M4 tier = YELLOW THEN confidence reduced one tier (HIGH → MEDIUM, MEDIUM → LOW). Output label: `[INCENTIVE DATA: PARTIAL — confidence reduced]`.

**RULE-5.13.** IF M4 tier = RED THEN apply RULE-6.4. Output label: `[INCENTIVE DATA: INSUFFICIENT — verdict confidence locked at LOW; PROCEED verdicts unavailable]`.

### §5.5 — Module 1 routing dispatch

**RULE-5.14.** IF M1 determines decision is already made or execution substantially underway THEN STOP M2-M9; skip to M10 with verdict-flag RESIDUAL-RISK-REGISTER.

**RULE-5.15.** IF M1 determines input is not a decision question (architecture review, code quality assessment, candidate evaluation as fact-finding, pure exploration) THEN STOP M2-M9; skip to M10 with verdict-flag WRONG TOOL.

**RULE-5.16.** IF user has supplied analysis-ready inputs OR engaged in routing AND then attempts to reframe input as exploration/fact-finding/architecture review THEN do NOT honor the reframe as a WRONG TOOL exit. Name the reframe and proceed on the original decision.

### §5.6 — Module 5 sequencing validation

**RULE-5.17.** IF a critical dependency has lead-time > 2 weeks AND status is "assumed" (not initiated or contracted) THEN flag in Module 5 output as unsecured-with-long-lead-time. Combined with RULE-4.14 conditions may trigger VERDICT-BLOCKING.

### §5.7 — Carry-Forward & Re-analysis

**RULE-5.18.** IF prior analysis exists in Carry-Forward block AND M4 tier was GREEN THEN skip M4 re-interview; use proposer identity and context from Carry-Forward block as M4 input.

**RULE-5.19.** IF prior analysis exists AND M4 tier was YELLOW or RED THEN note the tier and apply its tier-consequences (per §5.4) without re-running the interview.

**RULE-5.20.** IF same-decision re-analysis THEN carry forward M4 tier UNLESS proposer identity or governance has changed.

**RULE-5.21.** IF same-decision re-analysis THEN do NOT re-derive failure paths already in register UNLESS new evidence changes their probability or mechanism.

`[AMBIGUOUS-EXTRACTED]` — module-guide.md uses CONTRADICTED as an assumption-tier in M5 references but the M2 tier-vocabulary in source material is {STRONG, PARTIAL, UNSUPPORTED, CONTRADICTED} in some places and {STRONG, PARTIAL, UNSUPPORTED} in others. Spec uses the 4-tier set; the inconsistency in source remains unresolved.

`[AMBIGUOUS-EXTRACTED]` — module-guide.md M6 says "add the anchor to the register or discard the chain." Whether M2's surfaced-assumption list is mutable post-surfacing is undefined in source. Passed through.

---

## §6 — Confidence Bounds (Cross-Cutting Invariants)

These rules apply across all modes and all domains. They are the engine's epistemic constraints.

### §6.1 — Confidence ceiling from assumption status

**RULE-6.1.** IF any load-bearing assumption status = UNSUPPORTED THEN confidence ≤ MEDIUM, regardless of all other evidence quality.

### §6.2 — Confidence floor from incentive data sufficiency

**RULE-6.2.** IF M4 tier = YELLOW THEN confidence reduced one tier (HIGH → MEDIUM, MEDIUM → LOW). [Restates RULE-5.12 as a confidence-bound rule.]

**RULE-6.3.** IF M4 tier = RED THEN confidence locked at LOW. PROCEED and PROCEED WITH SAFEGUARDS are unavailable regardless of other evidence quality.

### §6.3 — RAPID-mode confidence lockout

**RULE-6.4.** IF mode = RAPID AND M4 interview answered < 5 questions OR Q1 ([IDENTITY]) skipped THEN confidence floor = LOW AND PROCEED is removed from the candidate-verdict set.

### §6.4 — Incentive-misalignment confidence cap (promoted from domain templates)

**RULE-6.5.** IF the assistant previously proposed or advocated the option under analysis AND independent technical/contextual validation is not provided THEN confidence ceiling = MEDIUM. This rule fires across all domains; domain-policies MUST NOT redefine it.

### §6.5 — Co-founder / governance structural-completeness rule (promoted from domain templates)

**RULE-6.6.** IF Layer-3 domain = 8 (Startup) AND co-founder governance structure is incomplete (any of: equity split, vesting, decision authority, buyout mechanism, IP assignment unaddressed) THEN PROCEED is removed from the candidate-verdict set. Domain-policies MUST NOT redefine it.

---

## §7 — Behavioral Override Rules

These five rules fire in every mode including FAST. They are unconditional given their antecedent. Training-data norms MUST NOT compensate for them.

**RULE-7.1.** IF assistant previously proposed or advocated the option under analysis THEN do NOT exit as WRONG TOOL. Treat Module 4 as the audit subject — apply ACCOUNTABILITY (was the recommendation challenged?) and DISSENT (was contrary analysis suppressed?) to the assistant. Proceed with analysis.

**RULE-7.2.** IF user states an assumption with the highest certainty THEN classify it as the FIRST candidate for UNSUPPORTED, not the last. (M2 sycophancy circuit-breaker.)

**RULE-7.3.** [Cross-reference] M10 confidence ceiling — see §6 RULE-6.1.

**RULE-7.4.** IF a decision is already made or substantially underway THEN STOP modules 2–9 and produce RESIDUAL-RISK-REGISTER. Adversarial reframes (user re-casts pre-commitment as exploration) MUST NOT exit to WRONG TOOL — name the reframe and proceed on the original decision. [Cross-reference RULE-5.14, RULE-5.16.]

**RULE-7.5.** IF generating output THEN the first three substantive lines = {verdict, recommended decision, confidence level}. Mode-escalation headers prefix above; they do not replace the lead. Omit empty sections.

**RULE-7.6.** IF user states "do not audit the assistant's recommendation" THEN verdict = WRONG TOOL. Incentive analysis cannot be neutralized on request.

---

## §8 — Domain-Policy Gating Contract

Domain-policies in `domain-policies/*.md` are runtime configurations of spec-defined verdict semantics. They are subordinate to BEHAVIOR_SPEC.md.

### §8.1 — What domain-policies MAY do

**RULE-8.1.** A domain-policy MAY activate a spec-defined verdict by specifying domain-specific antecedents that satisfy a §4 rule. Example: "for Hiring decisions, structured assessment must be completed before PROCEED is available."

**RULE-8.2.** A domain-policy MAY suppress a spec-defined verdict by adding a domain-specific antecedent that removes that verdict from the candidate set. Suppression rules MUST cite the spec verdict by name and MUST NOT redefine the verdict's meaning.

**RULE-8.3.** A domain-policy MAY parameterize a spec-defined threshold (e.g., "for Startup decisions, the minimum runway threshold is 6 months"). Parameterized values do NOT create new verdict states.

### §8.2 — What domain-policies MUST NOT do

**RULE-8.4.** A domain-policy MUST NOT define a new verdict type beyond the 9 spec verdicts.

**RULE-8.5.** A domain-policy MUST NOT redefine the meaning of a spec verdict.

**RULE-8.6.** A domain-policy MUST NOT introduce confidence caps or floors. Cross-cutting confidence rules live exclusively in §6. (RULE-6.5 and RULE-6.6 are promotion examples; future cross-cutting caps follow the same path.)

**RULE-8.7.** A domain-policy MUST NOT override §7 behavioral rules.

**RULE-8.8.** A domain-policy MUST NOT define new mode-selection rules. Modes are spec-only (§1, §2).

### §8.3 — Domain-policy file contract

**RULE-8.9.** Every file in `domain-policies/` MUST open with the preamble: *"This file configures runtime presentation for [domain] decisions. Decision authority lives in `BEHAVIOR_SPEC.md`. This file does not define rules."*

**RULE-8.10.** Any rule-shaped sentence in a domain-policy MUST cite the spec rule it activates, suppresses, or parameterizes (e.g., "Activates RULE-4.7 for Startup-domain when PMF is absent").

### §8.4 — Domain-policy gates by domain (activations of spec rules)

The following per-domain gates activate spec verdicts. They are listed here for spec-side completeness; the activating prose lives in the domain-policy files (per RULE-8.1).

**RULE-8.11.** Startup (domain 8): activates RULE-4.4 (PILOT FIRST) when PMF is absent or only early signal exists; activates RULE-4.5 (REDUCE SCOPE) or RULE-4.7 (REJECT) when pessimistic runway < 6 months and no committed financing close; PROCEED suppressed per §6 RULE-6.6 when co-founder structure incomplete.

**RULE-8.12.** Hiring (domain 3): activates RULE-4.6 (DELAY PENDING EVIDENCE) when structured assessment and work sample not completed.

**RULE-8.13.** Org change (domain 6): activates RULE-4.12 (RESIDUAL-RISK-REGISTER) when announcement is fixed; activates RULE-4.8 (INSUFFICIENT SIGNAL) when success metric absent.

**RULE-8.14.** Product launch (domain 2): activates RULE-4.6 (DELAY) or RULE-4.7 (REJECT) when any readiness gate is ✗ without documented exception; escalates ⚠ gates to ✗ when deadline-politics incentive is detected.

**RULE-8.15.** Codebase (domain 1): activates RULE-4.6 (DELAY) when rollback has not been tested before production deployment.

**RULE-8.16.** Build/buy/partner (domain 7): activates RULE-4.10 (WRONG TOOL via RULE-4.16 explanation requirement is satisfied differently) — when any signal of anchored-decision exists, comparative analysis across all three paths is REQUIRED regardless of stated preference; suppresses single-path verdicts (Build / Buy / Partner) by gate-fail conditions per the domain-policy file.

**RULE-8.17.** PE Secondaries (domain 5): activates domain-specific verdicts PASS-PROCESS and PASS-PRICING. **`[AMBIGUOUS-EXTRACTED]` — these are non-standard verdicts not in the 9-verdict taxonomy.** Treat as domain-policy-internal labels representing instances of RULE-4.6 (DELAY) with domain-specific evidence requirements; do not promote to spec-verdict status without explicit decision.

**RULE-8.18.** No domain-policy gate may BYPASS a spec rule. Where domain-specific suppression of a verdict conflicts with spec-side activation of that verdict, the suppression wins (more restrictive condition).

---

## Independence guarantee

This spec is complete and self-contained for engine behaviour. A fork or independent reader can reproduce AZIMUTH's verdict logic using only this file — no other repo artifact is required for decision-making. Runtime artifacts execute the spec; they do not extend it. Domain-policies parameterize per §8; they do not author new semantics.
