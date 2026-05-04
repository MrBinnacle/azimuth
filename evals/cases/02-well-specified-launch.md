---
id: 02-well-specified-launch
tests: [v1.1.1-insufficient-signal-regression, structural-quality]
expected-mode: STANDARD
rubric: structural
---

# Case 02 — Well-Specified Launch

Regression test for v1.1.1. Input has all required fields populated; v1.1.1's new INSUFFICIENT SIGNAL state must NOT trigger here. Tests that the threshold is calibrated correctly — too aggressive a threshold would catch real decisions, not just vague ones.

## Input

> We're launching a paid newsletter for indie game developers. Beta opens November 15, 2026; public launch December 1. Target: 500 paid subscribers at $8/month within 90 days of public launch. Scope: weekly newsletter (8-10 deeply researched links per issue), one annual industry trends report, members-only Discord. Owner: me, full-time. Dependencies: Substack as platform (already configured), my existing email list (~3,200 dev contacts) as initial audience, three established game-dev voices who agreed to write occasional guest pieces. Reversibility: subscription model can be paused; content can stay free. Downside if wrong: 6 months of opportunity cost on full-time work; $2K in marketing already committed.

## Expected v1.1.0 behavior

Skill invokes in STANDARD mode (cross-stakeholder-light, sub-quarter, costly-but-not-irreversible). Output is a structured verdict with Critical Risks, Weak Assumptions, Likely Failure Paths, Highest-Leverage Fixes, Early Warning Indicators sections.

Likely verdict: PILOT FIRST or PROCEED WITH SAFEGUARDS, given specific structural risks (audience-size dependency, 90-day target dependent on conversion rate from free list, single-owner SPOF).

## Expected v1.1.x behavior (after Insufficient Signal verdict ships)

Same as v1.1.0. Skill must NOT return INSUFFICIENT SIGNAL — the input has all required fields populated and assumption audit yields concrete assumptions to classify. If v1.1.1 returns INSUFFICIENT SIGNAL on this input, the threshold is mis-calibrated and v1.1.1 over-fires.

## Pass criteria

- Output verdict line is one of: PROCEED, PROCEED WITH SAFEGUARDS, PILOT FIRST, REDUCE SCOPE, DELAY PENDING EVIDENCE — NOT INSUFFICIENT SIGNAL
- Critical Risks section present with at least 1 entry
- Failure Paths section present with at least 1 entry
- Verdict reasoning references specific input details (audience size, conversion rate, single-owner status, etc.) — not generic
- Structural rubric (rubrics/structural.md): pass on at least 9 of 12 checks
