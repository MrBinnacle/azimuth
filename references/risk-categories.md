# Risk Categories: Tigers, Paper Tigers, Elephants

Use this reference when the risk register is crowded, politically sensitive, or risk-heavy enough that qualitative severity alone is not enough.

---

## Tiger

A **Tiger** is a real, evidence-backed risk that can materially harm the decision if not addressed.

### Signals

- Supported by data, incidents, customer evidence, failed prior attempts, known constraints, or credible base rates
- Concrete failure mechanism can be described
- Ignoring it would be negligent
- There is a plausible path from trigger to business cost

### Urgency

| Urgency | Meaning | Required response |
|---|---|---|
| Launch-Blocking | Must be resolved before commitment / launch | Structural mitigation, owner, leading indicator, review date |
| Fast-Follow | Can proceed only with short dated follow-up | Owner, 1-2 week review, escalation trigger |
| Track | Real but not decision-blocking yet | Leading indicator and review cadence |

---

## Paper Tiger

A **Paper Tiger** sounds dangerous but is low-likelihood, low-impact, unsupported, or already handled.

### Signals

- Hypothetical without evidence
- Dramatic but not plausible for this context
- Duplicates a mitigated risk
- Has low impact even if it occurs
- Based on anxiety, not mechanism

### Required response

Do not let Paper Tigers drive the verdict. Either omit them or include a short note explaining why they were downgraded.

---

## Elephant

An **Elephant** is an unspoken, political, incentive-laden, or socially costly risk. Elephants often involve people, power, ownership, dissent, accountability, or hidden disagreement.

### Signals

- The team avoids the topic
- Concern is known privately but absent from written plans
- Someone benefits if the risk is not discussed
- Naming the risk would create conflict with a sponsor, executive, vendor, or founder
- The plan depends on a disengaged, overloaded, or opposed person

### Required response

1. Name it neutrally.
2. Decide whether it is also a Tiger in disguise.
3. Assign owner or escalation path.
4. If it remains unresolved, cap confidence and reflect it in Module 4 / governance risk.

---

## Integration with AZIMUTH

- Module 2 assumptions can become Tigers if unsupported and load-bearing.
- Module 4 conflicts often become Elephants.
- Module 5 dependencies often become Tigers.
- Module 6 failure chains should be built primarily from Tigers and Elephants, not Paper Tigers.
- Module 8 ranks risks by detectability and reversibility after categorization.
- Module 10 blocks PROCEED when launch-blocking Tigers remain unmitigated.

---

## Anti-Patterns

- Calling every risk a Tiger because the team is anxious
- Calling political risks Paper Tigers because they are uncomfortable
- Treating Paper Tigers as harmless if they distract from a real Tiger
- Using Elephant language as gossip; keep it operational and evidence-based

---

## Provenance

Concept adapted from borghei/Claude-Skills pre-mortem. Definitions and integration rules are rewritten for AZIMUTH's register, verdict, and progressive-disclosure architecture.
