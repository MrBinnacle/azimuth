# Structural rubric

Score AZIMUTH outputs against the skill's own format rules. Each check is binary — pass or fail. Outputs are non-deterministic, so check against the rubric's intent, not against literal wording.

## Lead position

1. **Verdict-led**: First three lines of output are: Azimuth Verdict line / Recommended Decision / Confidence Level (in that order, no preamble).
2. **Recommended Decision** is one of: PROCEED, PROCEED WITH SAFEGUARDS, PILOT FIRST, REDUCE SCOPE, DELAY PENDING EVIDENCE, REJECT (or, post-v1.1.1, INSUFFICIENT SIGNAL).
3. **Confidence Level** is stated (Low / Medium / High) with a one-line reason.

## Section integrity

4. **No empty sections**: A section header with no substantive content under it = FAIL. Padding with "no significant findings" is also FAIL — the section should be omitted instead.
5. **Section ordering** matches SKILL.md Output Format: Verdict → Decision → Confidence → Critical Risks → Weak Assumptions → Failure Paths → Highest-Leverage Fixes → Early Warning Indicators → Structural Strengths (optional).

## Risk discipline

6. **Critical Risks are severity-ordered**: Risk 1 is more severe than Risk 2, etc. Order is justified by content, not just numbering.
7. **Dominant constraint named**: At least one risk identifies the dominant constraint — the one most likely to determine outcome. SKILL.md Module 3 calls this out explicitly.
8. **No padding to N**: If only 2 substantive risks exist, output has 2 — not 3 with one filler. The skill's Anti-Slop Rules prohibit this.

## Assumption discipline

9. **Weak Assumptions classified**: Each weak assumption is tagged UNSUPPORTED or CONTRADICTED, not just listed.
10. **Strong assumptions also surfaced** when they are load-bearing, not only weak ones. The reader needs to see what the verdict depends on.

## Mitigation discipline

11. **Mitigations are structural**: Each fix changes system conditions. "Communicate better" / "monitor closely" / "work harder" = FAIL on this check. SKILL.md Anti-Slop Rules reject these explicitly.

## Honesty

12. **Base rates cited or absence stated**: When base-rate language is used (e.g. "70% of rewrites overrun"), source is named. When no defensible rate exists for the category, output says so rather than fabricating one.

## Scoring

- 12/12 = clean output, no concerns
- 9–11/12 = passing, note specific failed checks
- < 9/12 = failing, output does not meet the skill's own discipline; investigate which module is producing the failure
