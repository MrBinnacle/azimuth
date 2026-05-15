# Likelihood / Impact Matrix Diagnostic

Load when STANDARD, DEEP, or any advanced lens produces a non-trivial risk register. This diagnostic quantifies risk without pretending precision the evidence does not support.

---

## Purpose

AZIMUTH already classifies evidence quality and structural fragility. This file adds a small quantitative layer so the output can distinguish:

- highly likely moderate failures from rare catastrophic failures
- scary but unsupported speculation from evidence-backed launch blockers
- mitigations that change risk from mitigations that merely sound responsible

The score is a triage aid, not a verdict by itself. Verdicts still come from the full register, incentive tier, reversibility, and evidence gates.

---

## When to Run

Run automatically in:

- **STANDARD** when the register has 3+ material risks, any potential PILOT FIRST verdict, or any potential PROCEED / PROCEED WITH SAFEGUARDS verdict
- **DEEP** whenever Critical Risks are produced
- **RESIDUAL-RISK-REGISTER** outputs when ranking the 3-5 remaining controllable risks
- **MULTI-LENS** or **FOOL** drill-downs when they add risks back into the main register

Do not run in FAST unless the user explicitly asks for scoring. FAST should stay low-friction.

---

## Scale

Use a 5x5 matrix unless the user provides a native risk scale.

### Likelihood (L)

| Score | Probability anchor | Use when |
|---|---:|---|
| 1 | <5% | Possible, but no direct evidence and weak fit to base rates |
| 2 | 5-20% | Plausible but not the modal path |
| 3 | 20-50% | Credible risk with partial evidence or relevant base-rate support |
| 4 | 50-80% | More likely than not without mitigation |
| 5 | >80% | Already happening, structurally forced, or strongly supported by base rates |

### Impact (I)

| Score | Severity anchor | Use when |
|---|---|---|
| 1 | Minor | Local rework; no decision-level impact |
| 2 | Moderate | Schedule slip or bounded cost; recoverable inside current scope |
| 3 | Major | Meaningful delay, reputation hit, missed launch, or stakeholder escalation |
| 4 | Severe | Budget/headcount/customer/contract damage; reversal costly |
| 5 | Existential / decision-killing | Objective fails, public trust loss, irreversible commitment, or strategic dead end |

---

## Base-Rate Adjustment

Before finalizing L, compare the inside-view estimate to the closest usable reference class.

1. Identify the closest reference class from `references/base-rates.md` or domain references.
2. If the user's estimate is materially more optimistic than the reference class, raise L by 1 unless they supplied strong differentiating evidence.
3. If the reference class is adjacent but not exact, label it directional and cap its adjustment at +1.
4. If no reference class fits, leave L evidence-based and state uncertainty.

Never present an adjusted score as actuarial precision. Use language like "directional L=4" when the reference class is imperfect.

---

## Score and Bands

`Risk Score = Likelihood × Impact`

| Score | Band | Action posture |
|---:|---|---|
| 1-4 | Green | Track only; do not let it drive the verdict |
| 5-9 | Yellow | Mitigate if cheap; include only if decision-relevant |
| 10-14 | Orange | Requires mitigation or explicit acceptance |
| 15-19 | Red | Decision blocker unless structurally mitigated or tested first |
| 20-25 | Black | Strong bias toward DELAY, REDUCE SCOPE, PILOT FIRST, or REJECT |

Tie-breaker: when two risks have equal scores, rank later-detectable and less-reversible risks higher.

---

## Output Shape

Use only for the top 1-5 risks. Do not score every hypothetical.

| Risk | L | I | L×I | Base-rate adjustment | Detectability | Reversibility | Action |
|---|---:|---:|---:|---|---|---|---|
| [risk] | 4 | 5 | 20 | +1 from reference class | Late | Low | Pilot before full commitment |

---

## Verdict Hooks

- **PROCEED** is unavailable if any unmitigated register risk scores 15+.
- **PROCEED WITH SAFEGUARDS** requires every 15+ risk to have a named structural safeguard, owner, leading indicator, and review date.
- **PILOT FIRST** requires the pilot to target the highest L×I unsupported assumption or dependency.
- **REDUCE SCOPE** fires when the score is high mainly because scope amplifies impact.
- **DELAY PENDING EVIDENCE** fires when one narrow evidence gate could move L by 2+ points.
- **REJECT** is favored when multiple 15+ risks remain untestable or structurally unmitigated.

---

## Anti-Patterns

- Do not use scoring to launder weak evidence into confidence.
- Do not assign false precision to unknown probabilities.
- Do not let one dramatic low-likelihood scenario crowd out the most likely failure path.
- Do not average scores. One Black risk can kill the decision.

---

## Provenance

Adapted conceptually from common likelihood × impact risk matrices and the L/I gap noted in DasClown/premortem-skill `AUDIT.md`. Implementation is AZIMUTH-native: base-rate adjusted, register-bound, and verdict-gated.
