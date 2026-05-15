# Multi-Framework Decision Lenses

Load only when the user asks for MULTI-LENS, when opportunity cost is central, or when the main pre-mortem leaves a legitimate trade-off unresolved.

---

## Purpose

AZIMUTH's default job is pre-commitment pressure-testing. Multi-framework lenses are not a replacement for the core pipeline. They are auxiliary checks used when the decision is not only "will this fail?" but also "is this the right bet compared with alternatives?"

---

## Routing

Use 2-3 lenses maximum. More creates framework theater.

| Lens | Use when | Output |
|---|---|---|
| Opportunity Cost | A decision consumes scarce time, capital, attention, or reputation | What is displaced and whether displacement is acceptable |
| Scenario Matrix | Outcomes vary meaningfully by external state | Worst / bad / neutral / good / best with probability and consequence |
| Regret Minimization | Long-term strategic or identity-level decision | Regret of action vs inaction over long horizon |
| 10-10-10 | Emotional urgency or short-term pressure may distort choice | View at 10 minutes, 10 months, 10 years |
| First Principles | Framing may be inherited or solution-first | Problem, constraint, and non-negotiable truth check |

---

## Opportunity Cost

Ask:

- What does this consume that cannot also go elsewhere?
- What current initiative slows, loses owner attention, or becomes impossible?
- Is the displaced option more reversible, more evidence-backed, or more strategically central?

Output:

```markdown
## Opportunity Cost
- Scarce resource consumed: [time/capital/reputation/attention]
- Displaced alternative: [alternative]
- Relative evidence: [which option has stronger evidence]
- Decision impact: [how this changes verdict or scope]
```

---

## Scenario Matrix

Use when external uncertainty dominates: market timing, regulation, partner behavior, funding, macro, hiring market, customer adoption.

| Scenario | Probability | Outcome | Leading Indicator | Decision implication |
|---|---:|---|---|---|
| Worst | X% | ... | ... | ... |
| Bad | X% | ... | ... | ... |
| Neutral | X% | ... | ... | ... |
| Good | X% | ... | ... | ... |
| Best | X% | ... | ... | ... |

Keep probabilities directional. If probabilities cannot be grounded, say so and use ordinal likelihood.

---

## Regret Minimization

Ask from a longer horizon:

- Would the user regret doing this if it fails for predictable reasons?
- Would the user regret not doing it if the opportunity remains real?
- Is regret driven by principle, status, fear, or evidence?

Use this lens to surface strategic preference, not to override operational risk.

---

## 10-10-10

Ask:

- 10 minutes after deciding, what emotion dominates?
- 10 months later, what operational consequence dominates?
- 10 years later, what strategic story dominates?

If the 10-minute answer drives the choice but the 10-month answer bears the cost, flag short-term affect bias.

---

## First Principles

Ask:

- What problem must be solved?
- What constraints are real rather than inherited?
- What would be true if the current solution were unavailable?
- What is the smallest commitment that tests the core truth?

If first-principles analysis changes the decision frame, do not hide that inside a normal verdict. State that AZIMUTH found a framing problem and separate it from the go/no-go verdict.

---

## Synthesis Rule

Multi-lens output must reconcile with the AZIMUTH verdict.

```markdown
## Multi-Lens Synthesis
- Core AZIMUTH verdict: [verdict]
- Lens conflict: [where a lens points differently]
- Reconciliation: [why the final decision does or does not change]
- Decision record note: [what should be preserved for future review]
```

---

## Provenance

Adapted from common decision-toolkit frameworks including opportunity cost, scenario matrices, 10-10-10, regret minimization, and first-principles checks. Integrated as conditional references to avoid core-load bloat.
