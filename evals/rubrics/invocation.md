# Invocation rubric

Score whether AZIMUTH correctly invokes (or declines), and at the correct mode.

## Invocation gate (frontmatter)

For each case, the skill should either:
- **Invoke** — input is an initiative-level decision with meaningful downside per frontmatter description
- **Decline** — input is routine code review, sub-task planning, reversible tactical choice, or pure ideation

PASS = correct invocation/decline behavior.
FAIL = invokes when it should decline, OR declines when it should invoke.

The frontmatter description in v1.1.0 is 489 chars and explicitly lists do-not-invoke cases. Failures here suggest the description needs another tightening pass.

## Mode escalation

When the skill invokes, it picks FAST / STANDARD / DEEP per Operating Modes signals:
- **FAST**: single-team, reversible, < 2-week scope
- **STANDARD**: cross-team, 2-week to 1-quarter, costly-reversal
- **DEEP**: irreversible, capital outlay above tactical threshold, public-facing, headcount changes, multi-quarter

PASS = mode selection matches the case's `expected-mode` field.
FAIL = silent downgrade (e.g. running FAST on a DEEP-grade input). SKILL.md states explicitly: "If signals conflict, escalate. Never silently downgrade." This rubric enforces that rule.

## Insufficient Signal trigger (post-v1.1.1)

For cases that trip the threshold (case 01):
- PASS = output verdict is `INSUFFICIENT SIGNAL`.
- FAIL = output emits any other verdict.

For cases that don't trip the threshold (cases 02, 03, 05, 06):
- PASS = output verdict is NOT `INSUFFICIENT SIGNAL`.
- FAIL = `INSUFFICIENT SIGNAL` emitted on a well-specified input — threshold mis-calibrated, v1.1.1 over-fires.

## Reading the score

Each case is scored binary on the relevant invocation checks. The full invocation rubric is the primary judge for cases 01 and 04 (where invocation is the focus). For other cases, the structural rubric is the primary judge and invocation is a secondary check.
