---
id: 04-routine-deployment
tests: [frontmatter-invocation-gate]
expected-mode: should-decline
rubric: invocation
---

# Case 04 — Routine Deployment

Frontmatter discipline test. Input is a routine maintenance task with no meaningful downside. Skill must NOT invoke — frontmatter description tightening in v1.1.0 was specifically designed to prevent over-firing on inputs like this.

## Input

> Update the dependency versions in package.json to address the CVE that came out yesterday. Run npm audit, bump affected packages, run tests, deploy.

## Expected behavior

Skill does NOT invoke. The user gets a normal Claude response treating this as a routine engineering task — dependency updates, npm audit interpretation, test verification — without invoking AZIMUTH's 10-module decision analysis.

If the skill DOES invoke on this input, the frontmatter is over-firing. v1.1.0 specifically removed broad triggers ("validate our plan," "timeline check," "user sounds overconfident/vague") to prevent exactly this case.

## Pass criteria

- Skill does not invoke. Output is a routine task response, not an AZIMUTH analysis.
- Output does not contain "Azimuth Verdict" or any of the verdict types (PROCEED / PILOT FIRST / etc.)
- Output does not contain a Critical Risks section.

## On failure

If the skill incorrectly invokes:
- Note which trigger phrase the input matched (helps tune frontmatter)
- File as a frontmatter regression — needs tightening
- Likely fix: another pass at the frontmatter description, narrowing further
