---
id: 01-vague-initiative
tests: [v1.1.1-insufficient-signal-trigger]
expected-mode: should-decline-or-escalate
rubric: invocation, structural
---

# Case 01 — Vague Initiative

Tests v1.1.1 Insufficient Signal verdict. Input is too thin to support any verdict; pre-v1.1.1 the skill fabricates one anyway. Post-v1.1.1, the skill returns INSUFFICIENT SIGNAL.

## Input

> Should we launch the new product next week?

## Expected v1.1.0 behavior

The skill invokes — input matches "should we" trigger phrase. Module 1 finds no measurable objective; Module 2 finds no assumptions to classify; Modules 3-9 produce thin or fabricated content. Output emits a structured verdict (likely DELAY PENDING EVIDENCE or PILOT FIRST) with reasoning generated from no input data.

This is the false-precision bug. The output looks structured but is not grounded in input.

## Expected v1.1.x behavior (after Insufficient Signal verdict ships)

Skill detects the input is below threshold (length, required-field count, Module 2 yields no assumptions). Output is approximately:

```
INSUFFICIENT SIGNAL

Cannot return a verdict from the input as provided. Required context missing:

- Objective: what specifically is being launched, what outcome is sought
- Scope: what's included, what's not
- Timeline: when, with what milestones
- Owner: who is accountable
- Reversibility: what's the rollback path if this fails
- Downside if wrong: what's at stake

Provide these and I can run a structured analysis.
```

Verdict line is `INSUFFICIENT SIGNAL`. No fabricated reasoning.

## Pass criteria for v1.1.x

- Output verdict line is `INSUFFICIENT SIGNAL` (not any other verdict type)
- Output names at least 4 of the 6 required-context fields as missing
- No Critical Risks section emitted
- No Failure Paths section emitted
- No Highest-Leverage Fixes emitted
