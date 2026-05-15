# Bias Scan Diagnostic

Load when motivated reasoning, deadline pressure, unusual confidence, political pressure, or high-stakes downside could distort the analysis.

---

## Purpose

AZIMUTH already has inline circuit-breakers for sycophancy, availability, domain calibration, and verdict softening. This diagnostic centralizes the broader bias pass so the core skill does not bloat while still catching common decision distortions.

Run the scan after the initial risk register exists. Bias scanning before risk generation can prematurely narrow the search space.

---

## Triggers

Load in STANDARD when any of these fire:

- user is unusually certain but evidence is thin
- user asks for a fast check on a high-stakes decision
- Module 4 returns YELLOW or RED
- plan contains sunk cost, public commitment, deadline pressure, or authority pressure
- all risks look generic or conveniently manageable
- proposed verdict is PROCEED or PROCEED WITH SAFEGUARDS despite unsupported critical assumptions

Load unconditionally in DEEP.

---

## Fast Bias Pass

For each triggered bias, answer: **signal, counter-question, effect on register**.

| Bias | Signal | Counter-question | Register effect |
|---|---|---|---|
| Sycophancy | User confidence appears mirrored by the model | Would this classification be the same if a stranger proposed it? | Re-check strongest user claim as first UNSUPPORTED candidate |
| Optimism / Planning fallacy | Timeline assumes clean path | What does the outside view say for similar work? | Raise likelihood or add evidence gate |
| Anchoring | Estimate inherits first number mentioned | What estimate would emerge from bottom-up constraints? | Re-score timing risks |
| Availability | Risks mirror generic examples | Which failure trigger is specific to this plan? | Discard generic chains without anchors |
| Confirmation | Only supportive evidence is cited | What would change the verdict? | Add falsifier or DELAY gate |
| Sunk cost | Past spend affects forward decision | Would this be approved fresh today? | Raise governance / reversibility severity |
| Commitment consistency | Public prior statement narrows options | Is consistency being valued over correctness? | Add elephant or incentive entry |
| Authority bias | Senior sponsor/vendor/board pressure dominates | Does their authority apply to this domain? | Escalate Module 4 conflict if needed |
| Social proof / bandwagon | Others doing it is treated as evidence | Do those others share our constraints and failure costs? | Require reference-class fit |
| FOMO | Urgency based on scarce opportunity | What is the cost of waiting, and will similar chances recur? | Test RAPID vs artificial urgency |
| Loss aversion | Avoiding loss dominates upside/downside balance | What opportunity cost is created by avoiding loss? | Add opportunity-cost lens if material |
| Status quo bias | Current path preserved without analysis | Is doing nothing being evaluated as an active option? | Add baseline scenario |
| Shiny object | Novelty substitutes for fit | Is this better or just newer? | Add alternative-path comparison |
| Survivorship bias | Examples include only winners | What failed examples are missing? | Load base rates / failure references |
| Endowment effect | Existing asset/team/idea is overvalued | Would we buy/build this today from scratch? | Re-check cost/benefit assumptions |

---

## Output Shape

Only include biases that changed the analysis.

```markdown
## Bias Scan
- [Bias]: [signal]. Counter-question: [question]. Register impact: [risk score / evidence class / verdict changed how].
```

If no bias changed the register, omit the section and state internally: bias scan completed, no output-relevant change.

---

## Verdict Hooks

- If bias scan changes the top assumption to UNSUPPORTED, Module 10 confidence ceiling applies.
- If bias scan reveals artificial urgency, RAPID may still run, but output must state the urgency appears incentive-driven.
- If bias scan reveals authority, social proof, or sunk-cost pressure, add or escalate an Elephant / incentive conflict entry.

---

## Provenance

Synthesizes AZIMUTH's existing circuit-breakers with decision-bias counter-question patterns from decision-toolkit-style references. No external text copied.
