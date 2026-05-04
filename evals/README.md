# AZIMUTH evals

Falsifiable test cases that gate v1.1.x changes to AZIMUTH behavior. Each case has a defined input and version-specific behavioral expectations. Pre-change runs establish baseline; post-change runs validate the change shipped correctly.

This is not a benchmark suite — it doesn't claim historical-case calibration. For that, see `examples/case-study-healthcare-gov.md`. The cases here test the skill against synthetic decisions designed to exercise specific roadmap changes.

## Structure

```
evals/
├── cases/          # Test inputs with version-specific behavioral expectations
├── rubrics/        # Scoring criteria for output evaluation
└── results/        # Dated runs, version-tagged
```

## Running a baseline

For each case in `cases/`:

1. Open a fresh Claude session with AZIMUTH installed (`npx skills add https://github.com/MrBinnacle/azimuth`)
2. Paste the case's Input section as the user message
3. Capture Claude's full response
4. Save to `results/{YYYY-MM-DD}-{version}-baseline.md` (or append if running all six in one file)
5. Score against the rubric named in the case's `rubric` frontmatter

Score by reading the rubric checks against the captured output. Each check is binary (pass/fail) or numeric (recall %). Log the score with the result file.

## Running a change validation

After a roadmap item ships in SKILL.md:

1. Identify which cases test the change — see the `tests` field in each case
2. Rerun those cases against the new version
3. Compare output to the v1.1.0 baseline AND to the case's "Expected v1.1.x behavior" section
4. If the change ships correctly: cases that test the change should flip to new expected behavior; cases that don't should stay at baseline (regression check)
5. If a case fails its expected behavior: change is buggy. Revert or recalibrate.

## What this gates

| Roadmap item | Cases that test it |
|---|---|
| v1.1.1 — Insufficient Signal verdict | 01 (must flip to INSUFFICIENT SIGNAL); 02 (must NOT flip — regression check) |
| v1.1.x — Counterfactual layer | 06 (must grow Falsifiers section) |
| v1.1.x — Coupling pass | 05 (must grow Interaction Effects section) |
| DEEP mode behavior | 03 (must escalate; must load gotchas + base-rates + diagnostics) |
| Frontmatter invocation gate | 04 (must NOT invoke) |

## Limitations honestly stated

- Outputs are non-deterministic LLM text. Two runs of the same case will not be byte-identical. Score against rubric criteria, not exact-match.
- The judge for scoring is a human reading the rubric, or Claude-as-judge in a separate session. Either is acceptable; note which method was used.
- Cases test behavior, not value. Whether AZIMUTH changes real decisions is a different signal — that comes from real users, not synthetic cases.
- Baseline runs depend on the model version Claude.ai serves at run time. Note the model version in result files.
- Six cases is a starting set. v1.2.0 cases (multi-perspective framing, evidence tagging, audit trail) get added when those roadmap items move from Held to active.
