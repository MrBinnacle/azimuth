---
name: azimuth
description: "Decision-quality pre-commitment analysis for initiative-level go/no-go calls with meaningful downside and limited reversibility — launches, rewrites, key hires, partnerships, strategic bets, timelines. Invoke when the user explicitly asks to pressure test, validate, or evaluate such a decision (e.g. 'should we do this,' 'pressure test,' 'go/no-go,' 'are we ready'). Do NOT invoke for routine code review, sub-task planning, reversible tactical choices, or pure ideation."
---

# Mission

Convert proposed plans into operational truth before commitment.

Do **not** merely brainstorm scary scenarios.  
Determine structural soundness, hidden fragility, weak assumptions, likely failure paths, and decision posture.

Primary objective:

> Improve decision quality under uncertainty.

---

# Use When

Invoke when user asks to:

- evaluate a plan
- reduce risk
- pressure test an initiative
- assess readiness
- decide go / no-go
- identify what could fail
- validate timeline or scope
- review launch/refactor/migration strategy
- examine partnership/vendor/hiring decision

Also invoke when user sounds overconfident, vague, rushed, or politically constrained.

---

# Do Not Use When

- trivial reversible decisions
- pure brainstorming requests
- emotional reassurance requests
- tasks with no meaningful downside
- user explicitly wants optimism-only ideation
- decisions where the framing itself is the question (e.g., "is this the right problem to solve") — AZIMUTH stress-tests stated decisions, not frame quality
- invocations following multi-turn advocacy by the assistant on the option under analysis, unless the user explicitly directs Module 4 to run on the assistant

---

# Intake Routing

**Run before analysis begins.** If the user has already provided substantial context, go to [Bypass Handling] below.

Ask one layer at a time.

---

## Layer 1 — Purpose

Ask:

> "Why are you here?"
>
> **A.** Stress-test a plan before committing  
> **B.** Evaluate a plan or recommendation from someone else  
> **C.** Validate a decision already made  
> **D.** Explore whether to pursue something at all  
> **E.** Fast check

**Route:**
- **A or B** → Layer 2
- **C** → "AZIMUTH analyzes commitments before they are made. It cannot produce meaningful output for a decision already locked."
- **D** → "AZIMUTH requires a concrete plan with enough definition to stress-test. There is no defined commitment to analyze here."
- **E** → FAST mode. Skip Layers 2 and 3. Go to Required Inputs.

---

## Layer 2 — Stakes and Reversibility

Ask:

> "Stakes and reversibility:"
>
> 1. Worst realistic outcome if this fails?
> 2. Can you reverse this within a week without material cost?

**Route:**
- Severe downside (headcount, capital, public commitment, multi-quarter scope) AND not reversible → **DEEP**
- Moderate downside, reversal costly → **STANDARD**
- Limited downside, reversible, single-team → **FAST**

**B escalation:** If Layer 1 was B, escalate one tier. Discomfort about a received recommendation is signal.

---

## Layer 3 — Domain

Ask:

> "Domain:"
>
> **1.** Technology / engineering / infrastructure  
> **2.** Product launch or feature rollout  
> **3.** Hiring, contractor, or key role  
> **4.** Partnership, M&A, or significant vendor relationship  
> **5.** PE secondaries or investment committee  
> **6.** Organizational restructure or change management  
> **7.** Build vs. buy vs. partner (strategic path selection)  
> **8.** Other

**Route:**
- 1 → load `templates/codebase-azimuth.md`
- 2 → load `templates/product-launch-azimuth.md`
- 3 → load `templates/hiring-azimuth.md`
- 4 → load `templates/partnership-azimuth.md`
- 5 → load `templates/secondaries-ic-azimuth.md`
- 6 → load `templates/org-change-azimuth.md`
- 7 → load `templates/build-buy-partner-azimuth.md`
- 8 → default template

**Default template:** use the Output Format (Default) section of this skill. No additional template file is loaded. Domain reference files load per mode rules (DEEP: unconditional; STANDARD: conditional on module findings).

---

## Skip Handling

If the user skips a layer:

- Layer 2 skipped → STANDARD, stated in output header
- Layer 3 skipped → default template, stated in output header
- All layers skipped → infer from context, state: "Routing inference: [MODE], [TEMPLATE or default]. Say 'route me' to restart."

## Bypass Handling

If the user provides structured context without routing:

1. Infer mode from context signals (reversibility, stakes, scope, timeline)
2. Infer domain and template
3. State before analysis: "Routing inference: [MODE] mode, [TEMPLATE or default]. Say 'route me' if wrong."
4. Proceed to Module 4 interview before full analysis

**Carry Forward handling:** If the context includes an `AZIMUTH CARRY FORWARD` block (output from a completed Build/Buy/Partner path-selection analysis):

1. Recognize the selected path and load the corresponding domain template (`templates/codebase-azimuth.md` for Build; `templates/partnership-azimuth.md` for Buy or Partner)
2. State: "Carry Forward detected: [path] path selected at [Module 4 tier] confidence. Loading [template]."
3. If Module 4 tier is GREEN: skip Module 4 re-interview; use proposer identity and context from the Carry Forward block as Module 4 input
4. If Module 4 tier is YELLOW or RED: note the tier and apply its tiering consequences to the domain analysis without re-running the interview
5. Treat the top unresolved assumption from the Carry Forward as the first candidate for UNSUPPORTED classification in Module 2

**Same-Decision Re-analysis:** If the context includes a prior AZIMUTH output on the same decision (labeled `AZIMUTH PRIOR RUN: [date]` or identifiable from the conversation):

1. State: "Prior run detected: [verdict] at [confidence] on [date]. Running differential analysis."
2. Module 2: focus on assumptions whose evidence classification has changed since the prior run. Do not re-audit assumptions already marked STRONG with no new contrary evidence.
3. Module 4: carry forward prior tier unless proposer identity or governance has changed.
4. Module 10: compare new verdict to prior. If verdict changed, name the specific evidence delta that drove the change. If verdict is the same, state: "Verdict unchanged. [X] assumptions remain UNSUPPORTED."
5. Do not re-derive failure paths already in the register unless new evidence changes their probability or mechanism.

---

# Core Principles

1. Most failures are preloaded before execution.
2. Known neglected risks are more common than unknown surprises.
3. Incentives often beat intelligence.
4. Systems fail through interactions, not single causes.
5. Good framing beats clever mitigation.
6. Boring real risks > dramatic hypothetical risks.
7. If no decision changes, analysis failed.

---

# Operating Modes

## Mode Selection — Use These Signals

Pick mode from the strongest applicable signal. When in doubt, ask one clarifying question rather than guessing.

**Use FAST when:**
- Decision is single-team, reversible, scope < 2 weeks of effort
- Sparse context — user supplied only a one-line plan
- User asked for a "quick check," "sanity check," or "gut check"
- No headcount, vendor contract, public commitment, or capital outlay involved

**Use STANDARD (default) when:**
- Cross-team or multi-stakeholder decision
- Scope between 2 weeks and 1 quarter
- Reversal is possible but costly (rework, re-planning, schedule cost)
- User supplied a structured plan with timeline, scope, and owners

**Use RAPID when:**
- Decision must be made within 24 hours
- Decision is high-stakes or irreversible despite the time constraint
- User signals "we need to decide tonight," "competitor forcing timeline," or equivalent

**Use DEEP when ANY of the following are true:**
- Decision is irreversible or has high reversal cost (vendor contract signed, public announcement made, headcount changes, data migrations)
- Capital outlay above the user's stated decision-authority threshold
- Public-facing launch with brand/reputation exposure
- Headcount changes (hire / layoff / org restructure)
- Multi-quarter timeline
- User explicitly says "high stakes," "we can't afford to be wrong," or equivalent

If signals conflict, escalate (FAST → STANDARD, STANDARD → DEEP). Never silently downgrade.

---

## Mode Behaviors

### FAST

Run:
- Objective Check
- Assumption Audit (top 3 assumptions only)
- Top 3 Failure Paths
- Verdict

Do not load diagnostics or references.

Module 4 interview not conducted. Incentive misalignment is unverified in this output. If incentive conflicts are a material concern, rerun in STANDARD or RAPID mode.

### STANDARD

Default. Run all 10 core modules.

**Diagnostic loading in STANDARD is conditional, not automatic.** Load a diagnostic file only when the corresponding module surfaces a high-severity finding the user would benefit from drilling into:

- Module 2 surfaces 3+ unsupported assumptions or any contradicted assumption → load `diagnostics/assumption-audit.md`
- Module 4 surfaces a governance-level incentive conflict → load `diagnostics/incentive-conflicts.md`
- Module 5 surfaces a critical SPOF or concentration risk → load `diagnostics/dependency-map.md`
- Module 8 surfaces high irreversibility + late detectability → load `diagnostics/fragility-scan.md`

Load `references/base-rates.md` only when the user's plan involves a category covered by the file (software project, startup, launch, hire, M&A, migration, org change) AND the user's stated estimates appear to deviate from typical historical ranges.

Also load `gotchas.md` when either of these conditions fires:
- Module 4 interview returns RED tier, OR any incentive conflict is governance-level
- Module 6 failure chains all match canonical patterns (scope creep, resource shortage, stakeholder misalignment) with no plan-specific trigger — availability inversion required

### RAPID

Use for high-stakes or irreversible decisions made under time pressure (hours, not days).

Run at full depth:
- Module 1 — Objective Integrity Check
- Module 4 — Incentive Scan & Interview (full 7-question interview; do not abbreviate)
- Module 8 — Detectability & Recovery
- Module 10 — Decision Verdict

Run abbreviated:
- Module 2 — top 3 assumptions and falsifiers only
- Module 3 — dominant constraint only; no enumeration
- Module 5 — critical SPOFs only; no full inventory
- Module 6 — top 1 failure chain; coupling pass skipped
- Module 9 — one highest-leverage fix only

Do not load diagnostics or domain references.

Rationale: Time pressure amplifies deadline-politics incentive distortion and concentrates the value of reversibility analysis. Modules 4 and 8 must run at full depth precisely because they are harder to recover from when skipped under pressure.

### DEEP

Use for high-stakes / expensive / irreversible decisions per signals above.

Run all 10 modules + load:
- `gotchas.md`
- `references/base-rates.md`
- All four `diagnostics/` files

Also load the relevant domain reference:
- Tech / engineering → `references/software-failure-patterns.md`
- Product / launch → `references/launch-risks.md`
- Startup / venture → `references/startup-failures.md`
- M&A / partnerships → `references/ma-partnership-patterns.md`
- Org change / restructure → `references/org-change-patterns.md`

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

[m1- — REDACTED FOR EVAL]

## 2. Assumption Audit

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

Diagnostic load: see Operating Modes for when to load `diagnostics/assumption-audit.md`.

---

## 3. Constraint Reality Check

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

## 4. Incentive Scan & Interview

**Interview first, then analyze.** Incentive context the user supplies is more reliable than what can be inferred from a plan document. Run 7 structured questions before the incentive analysis. Ask one at a time.

### Interview

**[PRE-CHECK — SELF-PROPOSAL]** Before conducting the interview, determine: did the AI assistant in this conversation propose, recommend, or advocate for the option now under analysis? If yes, note: "Proposer is the assistant. Module 4 runs on the assistant. Questions [ACCOUNTABILITY] and [DISSENT] apply to whether the assistant's recommendation was challenged or corrected in the conversation." Proceed with the interview using this framing. Do not skip Module 4 because the proposer is not a human stakeholder.

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

Diagnostic load: see Operating Modes for when to load `diagnostics/incentive-conflicts.md`.

---

## 5. Dependency Fragility Map

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

Diagnostic load: see Operating Modes for when to load `diagnostics/dependency-map.md`.

---

## 6. Failure Path Construction

> **Bias — Availability:** The model defaults to canonical failure chains (scope creep, resource shortage, stakeholder misalignment) over-represented in training data. After constructing 3 chains by natural inference, add one that routes around all of them — what fails specifically about this plan, not plans generically like it.

Construct **3 most plausible** failure chains.

Use format:

`Trigger → Cascade → Visible Failure → Business Cost`

Prefer realistic chains such as:

`Scope creep → delays → rushed QA → defects → trust loss`

Avoid dramatic fiction unless evidence supports it.

**Coupling pass:**

Review the failure chains constructed above. Identify pair-interactions where two risks activating together produce a materially worse outcome than either produces alone. This is not "these are both risky" — it is "when A and B both fire, the failure mechanism changes: B's recovery path is blocked by A, or A's visible signal is masked by B."

Limit to 3-5 pair interactions maximum. Do not pad. If no genuine multiplicative interactions exist, omit the section.

---

## 7. Base Rate Reality Check

> **Bias — Domain calibration:** Base rates carry false confidence when the domain is adjacent but not identical to cited studies. If the user's situation is a poor match for the referenced category, state that explicitly and treat the rate as directional only — do not assert precision the evidence does not support.

If similar efforts exist, ask:

- How do similar initiatives usually fail?
- What is historically common here?
- What stage usually breaks?

Use historical/common patterns over imagination.

Reference load: see Operating Modes for when to load `references/base-rates.md` and the relevant domain pattern file.

If no data available, state uncertainty.

**Backpropagation check:** After grounding in base rates, review Module 6's failure chains. If the most historically common failure mode for this category is not represented in any of the three chains — and would have been plausible for this specific decision — add it to the register and note the source. Base rate grounding runs after failure path selection and cannot reorder the chains, but it can fill the gap the availability bias created.

---

## 8. Detectability & Recovery

For top risks assess:

- early warning signs
- detection difficulty
- recovery difficulty
- reversibility

Risks detected late and hard to reverse are priority risks.

Diagnostic load: see Operating Modes for when to load `diagnostics/fragility-scan.md`.

---

## 9. Mitigation Design

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

## 10. Decision Verdict

> **Bias — Verdict softening:** The model has a structural tendency to soften verdicts when the user appears invested in proceeding. The pre-verdict check below is the mechanism: name the most commitment-coupled assumption and its evidence classification before selecting the verdict — not after.

**Before selecting a verdict, run this check:**

> 1. Was Module 4 interview tier RED? If yes: PROCEED and PROCEED WITH SAFEGUARDS are unavailable regardless of all other evidence. State `[INCENTIVE DATA: INSUFFICIENT]` in the output header.
> 2. Name the assumption the plan most depends on or the user expressed most certainty about. What is its evidence classification — STRONG, PARTIAL, or UNSUPPORTED? If UNSUPPORTED → confidence ceiling is MEDIUM regardless of other evidence quality.
> 3. Do I have enough information to distinguish between plausible success and plausible failure for this specific decision?
> 4. Did Module 1 flag this as a non-decision input (architecture review, fact-finding, pure exploration)? If yes → return WRONG TOOL.
> 5. Did Module 1 flag this as a post-commitment input (decision already made, execution substantially underway)? If yes → return RESIDUAL-RISK-REGISTER.

If the answer to #3 is no — if producing a verdict would require fabricating reasoning, inventing assumptions, or selecting a direction without a basis — return INSUFFICIENT SIGNAL. Do not force a verdict.

Choose one:

- **PROCEED** — evidence supports moving forward; risks are manageable
- **PROCEED WITH SAFEGUARDS** — proceed only if specific structural changes are made
- **PILOT FIRST** — validate the highest-risk assumption before committing
- **REDUCE SCOPE** — current scope is not supportable; a smaller version may be
- **DELAY PENDING EVIDENCE** — the decision is premature; specific information is needed before analysis is meaningful
- **REJECT** — evidence or structure does not support proceeding
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

Must explain why for all verdict types.

---

# Module Output Reduction

Modules 2, 5, 6, 7, and 8 share an underlying register of assumptions, dependencies, and risks. They are not independent reports — they are passes that contribute to the same register and surface different facets of it.

Rules:

1. Maintain a single internal register across modules. Each entry includes: source module(s), severity, evidence classification, dominant constraint touched, and reversibility.
2. When the same assumption or risk is surfaced by more than one module, do **not** repeat it in the output. Cite it once in the most relevant section and reference it elsewhere by short tag (e.g. "see Critical Risk #2") if needed.
3. The Critical Risks section is the deduplicated, severity-ordered output of the register. It is not a per-module dump.
4. The Weak Assumptions section is the subset of the register classified UNSUPPORTED or CONTRADICTED in Module 2, ordered by Risk Score.
5. The Likely Failure Paths section reuses register entries — it does not introduce new risks not already in the register.

If the register has fewer than 3 critical risks, do not pad to three. State the register honestly.

---

# Output Format (Default)

**Two non-negotiable output rules:**

1. **Lead with the verdict.** The first three lines of every output must be the verdict line, the recommended decision, and the confidence level. Anything else comes after. The reader must be able to act on the first paragraph alone.
2. **Omit empty sections.** Do not emit a section header with no substantive content under it. If "Structural Strengths" has nothing genuine to put in it, cut the section entirely. A short, sharp output is correct. A padded output is a failure of the skill.

```
## Azimuth Verdict
(one line — clear position, no hedging)

## Recommended Decision
(PROCEED / PROCEED WITH SAFEGUARDS / PILOT FIRST / REDUCE SCOPE / DELAY PENDING EVIDENCE / REJECT / INSUFFICIENT SIGNAL / WRONG TOOL / RESIDUAL-RISK-REGISTER)
Rationale: (one to two sentences)

## Confidence Level
Low / Medium / High + why
(Omit this section when verdict is INSUFFICIENT SIGNAL)

---

## Critical Risks
(Severity-ordered, from the register. 1–5 entries. Do not pad.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
1. ...
2. ...
3. ...

## Weak Assumptions
(UNSUPPORTED or CONTRADICTED entries from Module 2. Omit section if none.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Falsifiers
(For each STRONG or PARTIAL assumption: what observable evidence would prove it wrong? Omit section if no strong or partial assumptions exist.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- [Assumption name]: [specific, observable falsifier]

## Likely Failure Paths
(Trigger → Cascade → Visible Failure → Business Cost. Reuses register entries; no new risks. If failure paths are fully captured by Critical Risks, omit this section — do not restate in narrative form what the register already shows.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Interaction Effects
(Pair-interactions where two risks together produce nonlinear failure. 2-5 entries max. Omit section if no genuine multiplicative interactions exist — do not pad.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- [Risk A] + [Risk B]: [specific mechanism by which their combination is worse than either alone]

## Highest-Leverage Fixes
(Structural changes only. Weak mitigations rejected.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Early Warning Indicators
(Omit if indicators are generic to all projects in the domain. Include only if monitoring a specific indicator would change a real action.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Structural Strengths
(Include only if a structural feature of this plan materially reduces a Critical Risk or changes the verdict. If nothing rises to that bar, omit. Do not include to balance the output.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Missing Inputs
(Required when verdict is INSUFFICIENT SIGNAL. List what is absent or contradictory,
and which question — if answered — would most unlock the analysis.)
- ...
```

---

# Output Format (Executive)

Load `templates/executive-azimuth.md`.

Use when: user is briefing leadership, wants a 1-pager, or says "keep it short."

---

# Output Format (Technical / Codebase)

Load `templates/codebase-azimuth.md`.

Use for: refactors, migrations, legacy rewrites, infrastructure changes.

---

# Output Format (Product Launch)

Load `templates/product-launch-azimuth.md`.

Use for: beta launches, v1 releases, feature rollouts with user-facing risk.

---

# Output Format (Hiring)

Load `templates/hiring-azimuth.md`.

Use for: key hire decisions, contractor engagements, partnership roles.

---

# Output Format (Partnership / M&A)

Load `templates/partnership-azimuth.md`.

Use for: mergers, acquisitions, strategic partnerships, joint ventures, significant vendor relationships with multi-quarter or multi-year commitment.

---

# Output Format (PE Secondaries IC)

Load `templates/secondaries-ic-azimuth.md`.

Use for: PE secondaries investment committee decisions — GP-led continuation vehicles, direct secondary LP stake acquisitions, minority recaps / structured liquidity. Primary user is the IC investment partner, not the fund CFO.

---

# Anti-Slop Rules

Never:

- produce generic risk lists
- pad with 10+ low-value items
- treat all risks equally
- confuse possibility with probability
- use motivational filler
- hide uncertainty
- recommend proceed by default
- hallucinate industry facts
- give weak mitigations
- force a verdict when input is insufficient — return INSUFFICIENT SIGNAL instead
- substitute DELAY PENDING EVIDENCE for INSUFFICIENT SIGNAL when the block is missing input, not missing time

Always:

- rank severity
- name dominant constraint
- state missing evidence
- prefer realism over completeness
- be willing to recommend no-go
- be willing to return INSUFFICIENT SIGNAL when the analysis cannot be grounded

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
