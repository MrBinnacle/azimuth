# Outcome Tracking Loop

Use after a decision has time to produce signal. This is not part of the core run unless the user asks for a learning review.

---

## Purpose

Feed real outcomes back into AZIMUTH's base rates, gotchas, and diagnostic calibration. The skill improves only if predictions are compared against reality.

---

## Review Cadence

At the review date from `templates/commitment-lock.md` or `templates/decision-record.md`, capture:

| Field | Prompt |
|---|---|
| Original verdict | What did AZIMUTH recommend? |
| Actual decision | What did the user/team do? |
| Outcome | What happened? |
| Prediction hit | Which risks occurred? |
| Prediction miss | What happened that AZIMUTH missed? |
| False alarm | Which risks were over-weighted? |
| Leading indicator quality | Did indicators fire early enough? |
| Calibration change | What should change in base rates, gotchas, or diagnostics? |

---

## Learning Classes

- **Base-rate update** — observed outcome changes reference-class expectations
- **Gotcha candidate** — recurring cross-domain pattern not currently captured
- **Diagnostic weakness** — existing diagnostic missed or over-weighted a signal
- **Commitment failure** — risk was identified but no owned action happened
- **Verdict calibration** — verdict was too soft or too severe for the evidence

---

## Output

```markdown
## AZIMUTH Outcome Review
- Original verdict: ...
- Actual outcome: ...
- Calibration finding: ...
- Repository update candidate: ...
```

---

## Provenance

Implements AZIMUTH's self-improvement loop: outcome evidence should feed future base-rate, gotcha, and commitment calibration rather than remain anecdotal.
