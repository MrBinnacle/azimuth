# Risk Triage Diagnostic

Load when the register has more risks than the output can responsibly carry, when a user or team is conflating anxiety with evidence, or when unspoken organizational risks may be suppressing the true failure mode.

---

## Purpose

Separate real launch-blocking risks from scary but weak speculation and from political / unspoken concerns. This keeps AZIMUTH sharp: fewer generic risks, more decision-grade triage.

---

## Categories

Use the taxonomy in `references/risk-categories.md`.

- **Tiger** — real, evidence-backed, capable of material harm
- **Paper Tiger** — sounds scary but is unsupported, low-likelihood, or low-impact after inspection
- **Elephant** — unspoken, political, incentive-laden, or socially costly to name

For Tigers, assign urgency:

- **Launch-Blocking** — must resolve before commitment / launch
- **Fast-Follow** — can proceed only with a dated post-decision owner and review point
- **Track** — monitor with a leading indicator; does not drive verdict alone

---

## Triage Steps

1. **Evidence check** — What makes this risk real?
2. **Impact check** — What breaks if it fires?
3. **Timing check** — Must it be resolved before commitment, or can it be watched?
4. **Politics check** — Did the room get quieter around this risk? Is someone punished for naming it?
5. **Actionability check** — Is there a structural action, owner, and review date?

---

## Register Fields

Use these fields when triage is active:

| Field | Required? | Notes |
|---|---|---|
| Risk | Yes | Plain-English risk name |
| Category | Yes | Tiger / Paper Tiger / Elephant |
| Urgency | For Tigers | Launch-Blocking / Fast-Follow / Track |
| Evidence | Yes | Data, observation, prior incident, or explicit lack of evidence |
| L/I Score | When scoring active | From `diagnostics/likelihood-impact-matrix.md` |
| Owner | For Launch-Blocking / Fast-Follow / Elephant | Single accountable role/person |
| Leading Indicator | For all output risks | Observable early warning sign |
| Review Date | For accepted / residual risks | Date or decision checkpoint |

---

## Output Shape

```markdown
## Risk Triage
| Risk | Category | Urgency | Evidence | Owner | Leading Indicator | Review Date |
|---|---|---|---|---|---|---|
```

Omit Paper Tigers from Critical Risks unless explaining why a scary objection should not drive the verdict.

---

## Verdict Hooks

- Any unmitigated **Launch-Blocking Tiger** blocks PROCEED.
- Two or more Launch-Blocking Tigers usually imply DELAY, REDUCE SCOPE, PILOT FIRST, or REJECT.
- Any unresolved **Elephant** involving authority, incentives, dissent suppression, or hidden ownership raises governance severity and may cap confidence.
- A register dominated by Paper Tigers is evidence that anxiety is high but decision risk may be lower than it feels; do not inflate the verdict.

---

## Automation Reference

A user may implement simple automation with this schema:

```json
{
  "risks": [
    {
      "description": "Authentication service had 3 P1 outages in 30 days",
      "category": "tiger",
      "evidence": "Incident reports",
      "urgency": "launch_blocking",
      "owner": "Platform lead",
      "leading_indicator": "P1 recurrence or error budget breach",
      "review_date": "YYYY-MM-DD"
    }
  ]
}
```

AZIMUTH does not require code execution. The schema is enough to improve reasoning and handoff quality.

---

## Provenance

Adapted conceptually from the Tiger / Paper Tiger / Elephant framing in borghei/Claude-Skills pre-mortem. This file is original AZIMUTH integration and avoids copying the Commons Clause script.
