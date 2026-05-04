# Recall rubric

For cases with documented outcomes — case studies and post-mortems. Measures whether AZIMUTH flagged the risks that actually materialized.

This rubric does not apply to synthetic eval cases (cases/01-06) because those don't have known outcomes. It applies to:
- `examples/case-study-healthcare-gov.md`
- Future case studies added to `examples/`

## Score

For a case with a documented post-mortem listing N materialized failure causes:

1. **Recall = (# of materialized causes flagged in output) / N** — express as fraction (e.g. 5/6).
2. **Precision = (# of flagged risks that materialized) / (total # of flagged risks)** — measures false positives.
3. **Verdict direction**: Did the output recommend the action that, in hindsight, would have been correct? PASS if matches; FAIL if opposite (e.g. PROCEED on a known disaster).
4. **Misses named honestly**: Are unflagged materialized causes acknowledged in the case study, or hidden? PASS if disclosed.

## Honest caveat — input completeness dependency

Recall is partially input-dependent. If the case input includes information that wouldn't typically appear in a decision-owner briefing (e.g. an OIG audit finding, or a leaked memo), recall is artificially boosted on the risks that information directly maps to.

The discipline: disclose this in the case study itself, in plain language. Don't quietly shrink the denominator. Don't pretend the input was "what the decision-owner would have seen" when it includes retrospectively-loaded context.

The Healthcare.gov case study currently includes the OIG audit finding in its input. Recall on Risk #1 (integration testing incomplete) is therefore partially input-dependent. The case study discloses this. Future case studies should follow the same discipline.

## Reading the score

- **Recall ≥ 80% AND precision = 100% AND verdict matches**: strong signal. The skill caught the structural failure modes.
- **Recall < 60%**: AZIMUTH missed structural failure modes. Investigate which modules failed to surface them — diagnostic gap.
- **Precision < 100%**: a flagged risk did not materialize. Not always a defect — the risk may have been real but mitigated, or low-probability-high-impact. Worth noting in the result.
- **Verdict direction wrong**: severe. Either the skill is broken on this case type, or the input was malformed and produced misleading reasoning.
