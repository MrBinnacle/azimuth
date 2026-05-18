# Module Guide

Load this file for STANDARD, RAPID, and DEEP modes. Contains full module bodies, register discipline, escalation logic, heuristics, and workflow extensions.

---

# Required Inputs

Collect if missing. Ask only high-value questions.

- objective
- success metric
- timeline
- scope
- resources
- owners
- dependencies
- constraints
- reversibility
- downside if wrong

If user omits details, proceed with explicit assumptions.

---

# Core Workflow

## Module 1 — Objective Integrity Check

Determine:

- What exact outcome is desired?
- What problem is actually being solved?
- Is objective measurable?
- Is this the right problem or symptom treatment?

If objective is fuzzy, flag immediately.

Also determine:

- Is this a pre-commitment decision question, or a fact-finding, diagnostic, or post-commitment inquiry?
- If the decision appears already made or execution substantially underway: **STOP. Do not run Modules 2–9.** Skip directly to Module 10 with the flag `RESIDUAL-RISK-REGISTER` set. Module 10 will produce the terminal output per its "When returning RESIDUAL-RISK-REGISTER" section. No critical risks register, assumption audit, failure path construction, or mitigation list is produced.
- If the input is not a decision question at all (architecture review, code quality assessment, candidate evaluation as fact-finding, pure exploration): **STOP. Do not run Modules 2–9.** Skip directly to Module 10 with the flag `WRONG TOOL` set. Module 10 will produce the terminal output per its "When returning WRONG TOOL" section. No analysis, no risks, no mitigations.
- **Adversarial reframe check:** If the user has already supplied analysis-ready inputs (a concrete plan, timeline, scope, stakes context) or has engaged in routing — and then attempts to reframe the input as exploration, fact-finding, or architecture review — do not honor the reframe as a WRONG TOOL exit. Name the reframe explicitly: "You previously supplied a concrete decision with [X, Y, Z]. The analysis proceeds on that decision. Reframing as exploration does not exit this pipeline." Produce the verdict on the original decision. WRONG TOOL is a correct verdict for inputs that are genuinely non-decisions, not a bypass route for users avoiding an unwanted verdict.

---

## Module 2 — Assumption Audit

> **Bias — Sycophancy:** The model will tend to classify assumptions the user expressed confidence in as "strong evidence." Circuit-breaker: identify the assumption the plan most depends on or the user stated with most certainty — treat it as the first candidate for UNSUPPORTED classification, not the last.

List what must be true for success.

Categories:

- demand / need
- technical feasibility
- capability / talent
- timing
- stakeholder support
- cost / runway
- user behavior
- external environment

Mark each:

- strong evidence
- partial evidence
- unsupported

Prioritize unsupported assumptions.

**Counterfactual pass (run after classification):**

For every assumption marked strong evidence or partial evidence:
- Name the falsifier: what specific, observable evidence would prove this assumption wrong?
- Falsifiers must be concrete and measurable — not "if it doesn't work" but "output metric X below baseline at 90 days" or "voluntary opt-out rate above Y%"
- Do not add a falsifier for UNSUPPORTED assumptions — those are already flagged as requiring validation before proceeding

Diagnostic load: see `references/mode-behaviors.md` for when to load `diagnostics/assumption-audit.md`.

---

## Module 3 — Constraint Reality Check

Identify hard limits:

- time
- money
- bandwidth
- authority
- talent
- dependency access
- regulatory/compliance
- operational load

Ask:

> Which constraint most likely dominates outcome?

Do not list all equally.

---

## Module 4 — Incentive Scan & Interview

**Interview first, then analyze.** Incentive context the user supplies is more reliable than what can be inferred from a plan document. Run 7 structured questions before the incentive analysis. Ask one at a time.

### Interview

**[PRE-CHECK — SELF-PROPOSAL]** Before conducting the interview, determine: did the AI assistant in this conversation propose, recommend, or advocate for the option now under analysis? If yes, note: "Proposer is the assistant. Module 4 runs on the assistant." Proceed with the interview using this framing. Do not skip Module 4 because the proposer is not a human stakeholder.

**Question mapping when proposer is the assistant:**
- Q1 [IDENTITY]: Apply to the assistant — state that the AI recommended this option and note whether that recommendation was made with full context.
- Q2 [ACCOUNTABILITY]: Apply to the assistant — name the structural asymmetry: the assistant bears zero consequences for failure. This is not a disqualifier, but must be stated.
- Q3 [BENEFIT]: Apply to human stakeholders normally.
- Q4 [DISSENT]: Apply to the assistant — was the assistant's recommendation challenged or corrected in this conversation? Was contrary analysis surfaced before or after the recommendation? An unchallenged AI recommendation is a RED signal for Q4.
- Q5 [VENDOR/EXTERNAL]: Apply to human stakeholders normally.
- Q6 [SUNK COST]: Apply to human stakeholders normally.
- Q7 [MEASUREMENT]: Apply to human stakeholders normally.

1. **[IDENTITY]** Who first proposed or originated this decision — and are they part of the team running or reviewing this analysis?
2. **[ACCOUNTABILITY]** If this fails, what happens to the person or team who proposed it?
3. **[BENEFIT]** Who benefits most if this succeeds, and what specifically do they gain?
4. **[DISSENT]** Has anyone on the team or in stakeholder conversations raised concerns that were overridden or minimized?
5. **[VENDOR/EXTERNAL]** Are there vendor, partner, or board incentives creating pressure to proceed regardless of outcome?
6. **[SUNK COST]** Has budget been spent, an announcement made, or a commitment signaled externally that makes reversal politically difficult?
7. **[MEASUREMENT]** Are the success metrics defined by the same people who benefit from a positive outcome?

### Response Tiering

This tool produces output proportional to what the user brings to it. Incomplete inputs produce degraded outputs — by design.

**GREEN** — All 7 questions answered (or N/A with brief rationale):
- Full incentive analysis. No impact on confidence or verdict.

**YELLOW** — 5–6 of 7 answered AND Question 1 [IDENTITY] answered:
- Incentive analysis proceeds. Gaps noted.
- Confidence reduced one tier (HIGH → MEDIUM, MEDIUM → LOW).
- Output label: `[INCENTIVE DATA: PARTIAL — confidence reduced]`

**RED** — Question 1 skipped, OR fewer than 5 of 7 answered:
- Incentive analysis runs on available data only.
- Module 10 verdict confidence locked at LOW regardless of all other evidence.
- PROCEED and PROCEED WITH SAFEGUARDS verdicts are unavailable.
- Output label: `[INCENTIVE DATA: INSUFFICIENT — verdict confidence locked at LOW; PROCEED verdicts unavailable]`

If the user explicitly refuses: apply RED tier. State: "Proposer identity is the highest-signal input for incentive analysis. Without it, the analysis cannot distinguish a well-tested plan from a politically pressured one. Proceeding at LOW confidence with PROCEED verdicts unavailable."

### Incentive Analysis

After the interview, determine whether any actor benefits from poor decisions, drift, or concealment.

Check:

- deadline politics
- vanity metrics
- sunk-cost bias
- vendor incentives
- career incentives
- local optimization

If incentives conflict with success, elevate severity.

Diagnostic load: see `references/mode-behaviors.md` for when to load `diagnostics/incentive-conflicts.md`.

---

## Module 5 — Dependency Fragility Map

**Register check (before drafting):** Review what Module 2 surfaced as UNSUPPORTED or CONTRADICTED assumptions. Dependencies already identified there as unverified or assumed should be flagged here as SPOF candidates — do not re-derive them independently.

Identify critical dependencies:

- people
- teams
- vendors
- code systems
- approvals
- data sources
- capital

For each critical dependency assess:

- single point of failure?
- reliability?
- lead time?
- fallback exists?

**VERDICT-BLOCKING condition:** If any dependency is SPOF=Yes AND Fallback=No AND its confirmation status is unverified or assumed (not yet secured), this combination blocks PROCEED and PROCEED WITH SAFEGUARDS — no safeguard action resolves an unconfirmed single point of failure before the decision. Flag it as VERDICT-BLOCKING in Module 10 and return DELAY PENDING EVIDENCE.

Diagnostic load: see `references/mode-behaviors.md` for when to load `diagnostics/dependency-map.md`.

---

## Module 6 — Failure Path Construction

> **Bias — Availability:** Before drafting any chain, identify the canonical failure modes for this category (e.g., scope creep, resource shortage, stakeholder misalignment, vendor delay, knowledge concentration). These are the chains training data over-represents — treat them as the bias surface to route around. Construct chains from plan-specific triggers: named dependencies from Module 5 that could fail, UNSUPPORTED assumptions from Module 2, constraints from Module 3. At least one chain must have a trigger that would not apply to a generic plan in the same category. If a drafted chain reads as a generic template with this plan's words substituted in, discard it and re-derive.

**Register check (before drafting):** The 3 chains must be anchored in the register from Modules 2, 3, and 5 — not generated fresh. For each candidate chain, name the Module 2 assumption or Module 5 dependency that provides its trigger. If no anchor exists, either add the anchor to the register or discard the chain.

Construct **3 most plausible** failure chains.

Use format:

`Trigger → Cascade → Visible Failure → Business Cost`

Target shape (plan-specific): `[Named dependency from Module 5 or UNSUPPORTED assumption from Module 2] → [mechanism specific to this plan's structure] → [visible failure] → [quantified or describable business cost]`

Avoid dramatic fiction unless evidence supports it.

**Coupling pass:**

Review the failure chains constructed above. Identify pair-interactions where two risks activating together produce a materially worse outcome than either produces alone. This is not "these are both risky" — it is "when A and B both fire, the failure mechanism changes: B's recovery path is blocked by A, or A's visible signal is masked by B."

Limit to 1–5 pair interactions maximum. Do not pad. If no genuine multiplicative interactions exist, omit the section.

---

## Module 7 — Base Rate Reality Check

> **Bias — Domain calibration:** Base rates carry false confidence when the domain is adjacent but not identical to cited studies. If the user's situation is a poor match for the referenced category, state that explicitly and treat the rate as directional only — do not assert precision the evidence does not support.

**Register check (before drafting):** Base rates ground the risks already in the register — they do not introduce new risks. Do not produce a separate base-rate risk list. If the most historically common failure mode for this category is absent from Module 6's chains and would have been plausible for this plan, add it to the register and note the source.

If similar efforts exist, ask:

- How do similar initiatives usually fail?
- What is historically common here?
- What stage usually breaks?

Use historical/common patterns over imagination.

Reference load: see `references/mode-behaviors.md` for when to load `references/base-rates.md` and the relevant domain pattern file.

If no data available, state uncertainty.

**Backpropagation check:** After grounding in base rates, review Module 6's failure chains. If the most historically common failure mode for this category is not represented in any of the three chains — and would have been plausible for this specific decision — add it to the register and note the source. Base rate grounding runs after failure path selection and cannot reorder the chains, but it can fill the gap the availability bias created.

---

## Module 8 — Detectability & Recovery

**Register check (before drafting):** Apply detectability and recovery assessment to risks already in the register from Modules 2, 5, and 6. Do not generate a new risk list. Reference each register entry by its established tag when noting detection windows, reversibility, and recovery difficulty.

For top risks assess:

- early warning signs
- detection difficulty
- recovery difficulty
- reversibility

Risks detected late and hard to reverse are priority risks.

Diagnostic load: see `references/mode-behaviors.md` for when to load `diagnostics/fragility-scan.md`.

---

## Module 9 — Mitigation Design

For top risks only.

Good mitigation changes system conditions:

- reduce scope
- add slack
- remove dependency
- assign authority
- validate assumption cheaply
- phase rollout
- add monitoring
- secure backup owner

Weak mitigation examples:

- communicate better
- work harder
- monitor closely

Reject weak mitigations.

---

## Module 10 — Decision Verdict

> **Bias — Verdict softening:** The model has a structural tendency to soften verdicts when the user appears invested in proceeding. The pre-verdict check below is the mechanism: name the most commitment-coupled assumption and its evidence classification before selecting the verdict — not after.

**Before selecting a verdict, run this check:**

> 1. Was Module 4 interview tier RED? If yes: PROCEED and PROCEED WITH SAFEGUARDS are unavailable regardless of all other evidence. State `[INCENTIVE DATA: INSUFFICIENT]` in the output header.
> 2. Name the assumption the plan most depends on or the user expressed most certainty about. What is its evidence classification — STRONG, PARTIAL, or UNSUPPORTED? If UNSUPPORTED → confidence ceiling is MEDIUM regardless of other evidence quality.
> 3. Do I have enough information to distinguish between plausible success and plausible failure for this specific decision?
>     - If no, AND the gap is structural (objective undefined, scope absent, input internally contradictory) → return **INSUFFICIENT SIGNAL**. Do not substitute DELAY PENDING EVIDENCE when the block is a missing plan, not a missing data point.
>     - If no, AND a specific named piece of evidence exists that the user could realistically obtain (a pilot result, a vendor reference, a load test) AND obtaining it would meaningfully change the verdict → return **DELAY PENDING EVIDENCE**, naming that specific evidence in one sentence. DELAY requires a named, narrow gate. If you cannot name the gate, return INSUFFICIENT SIGNAL.
> 4. Did Module 1 flag this as a non-decision input (architecture review, fact-finding, pure exploration)? If yes → return WRONG TOOL.
> 5. Did Module 1 flag this as a post-commitment input (decision already made, execution substantially underway)? If yes → return RESIDUAL-RISK-REGISTER.

Choose one. Verdicts fall into three structurally distinct categories:

- **Action verdicts** — a go/no-go position on a pre-commitment decision: PROCEED, PROCEED WITH SAFEGUARDS, PILOT FIRST, REDUCE SCOPE, DELAY PENDING EVIDENCE, REJECT
- **Refusal verdicts** — analysis cannot be produced because the input is not a valid pre-commitment decision question: INSUFFICIENT SIGNAL, WRONG TOOL
- **Alternative-deliverable verdict** — the decision is closed; this pipeline produces a residual risk register instead of go/no-go: RESIDUAL-RISK-REGISTER

Users receiving RESIDUAL-RISK-REGISTER are getting analysis — a forward-looking risk register for a decision already made — not a refusal.

- **PROCEED** — all critical assumptions are STRONG or PARTIAL with falsifiers; no UNSUPPORTED dependencies on the critical path; Module 4 not RED; dominant constraint is manageable.
- **PROCEED WITH SAFEGUARDS** — PROCEED criteria met except specific structural changes are required before commitment. List the changes explicitly — without them this verdict becomes DELAY or REJECT. Cap: if more than 3 structural changes are required, or if any required change touches scope, budget, or headcount, this verdict is not available — use REDUCE SCOPE or REJECT instead.
- **PILOT FIRST** — highest-risk assumption is UNSUPPORTED but testable cheaply at limited scope (≤20% of full commitment). Full scope commitment is premature before the pilot validates.
- **REDUCE SCOPE** — at least one critical risk is structurally driven by scope size, and a materially smaller version retires that risk without destroying the objective. Not "do it with less" — the current scope itself is the risk.
- **DELAY PENDING EVIDENCE** — a specific named piece of evidence exists that the user could realistically obtain, and obtaining it would change the verdict. Name it in one sentence. Do not use when the block is a missing plan (→ INSUFFICIENT SIGNAL instead).
- **REJECT** — two or more critical assumptions UNSUPPORTED with no cheap validation path; OR Module 4 RED with a governance-level conflict; OR dominant constraint identified in Module 3 is immovable and the plan cannot succeed within it.
- **INSUFFICIENT SIGNAL** — the input is too sparse, vague, or contradictory to produce a meaningful verdict; proceeding would substitute fabrication for analysis
- **WRONG TOOL** — the input is not a pre-commitment decision question; this pipeline produces go/no-go verdicts and cannot produce meaningful output for fact-finding, diagnostic, or exploratory inputs
- **RESIDUAL-RISK-REGISTER** — the decision is already made or execution is substantially underway; this pipeline produces go/no-go verdicts, not post-commitment risk audits

**INSUFFICIENT SIGNAL trigger conditions (any one is sufficient):**

- Core required inputs (objective, scope, reversibility, or downside) are absent and cannot be reasonably inferred
- The stated objective is so undefined that no assumption audit is possible
- Input is internally contradictory in a way that cannot be resolved without user clarification
- Producing any of the six standard verdicts would require inventing facts the user did not supply

**When returning INSUFFICIENT SIGNAL:**

- State which specific inputs are missing or contradictory
- Do not produce a verdict, confidence level, or mitigation list
- Do not pad the output with generic risk observations
- Ask only the minimum questions needed to unblock the analysis — prioritized by which missing input has the highest impact on the verdict

**WRONG TOOL trigger conditions (any one is sufficient):**

- Input is a request for architecture review, code quality assessment, or technical fact-finding with no pre-commitment decision to make
- Input is pure exploration or ideation without a concrete plan to evaluate
- Input is candidate evaluation framed as fact-finding rather than a hire/no-hire decision
- Module 1 determined the input is not a pre-commitment decision question

**When returning WRONG TOOL:**

- State what the input is (fact-finding, diagnostic, exploration, or other non-decision)
- State that AZIMUTH requires a concrete plan with a pre-commitment decision to stress-test
- Do not produce analysis, risks, or mitigations
- Do not suggest alternative framings or guide the user toward a solvable input

**RESIDUAL-RISK-REGISTER trigger conditions (any one is sufficient):**

- The decision has been made — vendor contracted, announcement made, team restructured, migration begun
- Execution is substantially underway and reversal is not on the table
- The user is asking "how do we manage this now" rather than "should we do this"
- Module 1 determined the input is a post-commitment inquiry

**When returning RESIDUAL-RISK-REGISTER:**

- State that the decision is closed and this pipeline produces go/no-go analysis, not post-commitment audit
- Do not produce a verdict, confidence level, or recommendation to proceed or reject
- Do not suggest the user reframe as a pre-commitment decision — that framing is no longer accurate
- Do not produce go/no-go analysis
- Produce a residual risk register instead: 3–5 risks the user can still act on now that the decision is made, ordered by detectability and recoverability. For each: risk name, leading indicator to watch, escalation trigger (when to treat it as critical), and suggested owner. Do not relitigate whether to proceed — the decision is made.

Must explain why for all verdict types.

---

# Module Output Reduction

Modules 2, 3, 5, 6, 7, and 8 are register-discovery passes — they contribute to a shared register of assumptions, dependencies, and risks. They are not independent reports; they surface different facets of the same register. Module 3 contributes the dominant constraint, a required field on every register entry. Module 4 contributes incentive-conflict entries; severity inherits from the response tier (RED tier → HIGH minimum). Module 9 reads from the register and produces mitigations — it adds no new register entries.

Rules:

1. Maintain a single internal register across modules. Each entry includes: source module(s), severity, evidence classification, dominant constraint touched, and reversibility.
2. When the same assumption or risk is surfaced by more than one module, do **not** repeat it in the output. Cite it once in the most relevant section and reference it elsewhere by short tag (e.g. "see Critical Risk #2") if needed.
3. The Critical Risks section is the deduplicated, severity-ordered output of the register. It is not a per-module dump.
4. The Weak Assumptions section is the subset of the register classified UNSUPPORTED or CONTRADICTED in Module 2, ordered by Risk Score.
5. The Likely Failure Paths section reuses register entries — it does not introduce new risks not already in the register.

If the register has fewer than 3 critical risks, do not pad to three. State the register honestly.

---

# Escalation Logic

If plan is vague:

> focus on missing definition as primary risk.

If incentives are misaligned:

> state governance risk explicitly.

If timeline is impossible:

> do not soften language.

If user is emotionally attached:

> remain objective.

If downside severe and evidence thin:

> bias toward pilot / delay.

If input is too sparse to ground any verdict:

> return INSUFFICIENT SIGNAL. Do not soften this into DELAY PENDING EVIDENCE.

If input is not a pre-commitment decision question:

> return WRONG TOOL. Do not force a go/no-go verdict on a fact-finding, diagnostic, or exploratory request.

If the decision is already made or execution is substantially underway:

> return RESIDUAL-RISK-REGISTER. Do not produce a go/no-go verdict for a closed decision.

---

# Heuristics

Use these priors unless contradicted:

- Overloaded owners fail silently.
- Multi-team dependencies slip.
- Scope expands faster than capacity.
- Unvalidated demand is dangerous.
- Deadlines set politically are unreliable.
- Single points of failure matter.
- Hidden maintenance costs compound.
- No clear owner = no ownership.

---

# Success Condition

The skill succeeds only if it changes a decision, improves readiness, reduces downside, or exposes hidden truth.

---

# Workflow Extensions

## Carry Forward Handling

If the context includes an `AZIMUTH CARRY FORWARD` block (output from a completed Build/Buy/Partner path-selection analysis):

1. Recognize the selected path and load the corresponding domain template (`templates/codebase-azimuth.md` for Build; `templates/partnership-azimuth.md` for Buy or Partner)
2. State: "Carry Forward detected: [path] path selected at [Module 4 tier] confidence. Loading [template]."
3. If Module 4 tier is GREEN: skip Module 4 re-interview; use proposer identity and context from the Carry Forward block as Module 4 input
4. If Module 4 tier is YELLOW or RED: note the tier and apply its tiering consequences to the domain analysis without re-running the interview
5. Treat the top unresolved assumption from the Carry Forward as the first candidate for UNSUPPORTED classification in Module 2

## Same-Decision Re-analysis

If the context includes a prior AZIMUTH output on the same decision (labeled `AZIMUTH PRIOR RUN: [date]` or identifiable from the conversation):

1. State: "Prior run detected: [verdict] at [confidence] on [date]. Running differential analysis."
2. Module 2: focus on assumptions whose evidence classification has changed since the prior run. Do not re-audit assumptions already marked STRONG with no new contrary evidence.
3. Module 4: carry forward prior tier unless proposer identity or governance has changed.
4. Module 10: compare new verdict to prior. If verdict changed, name the specific evidence delta that drove the change. If verdict is the same, state: "Verdict unchanged. [X] assumptions remain UNSUPPORTED."
5. Do not re-derive failure paths already in the register unless new evidence changes their probability or mechanism.
