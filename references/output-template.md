# Output Template

Load this file for all modes. Contains the default output format, domain format pointers, and anti-slop rules.

---

# Output Format (Default)

**Two non-negotiable output rules:**

1. **Lead with the verdict.** The first three substantive lines of every output must be the verdict line, the recommended decision, and the confidence level. Anything else comes after. The reader must be able to act on the first paragraph alone. Exception: mode-escalation headers prefix the output above the verdict line and do not count against the three-line rule.
2. **Omit empty sections.** Do not emit a section header with no substantive content under it. If "Structural Strengths" has nothing genuine to put in it, cut the section entirely. A short, sharp output is correct. A padded output is a failure of the skill.

```
[MODE: DEEP — escalated from user-requested FAST; stakes signals override phrasing]
(Include this line only when the phrasing-vs-stakes tiebreaker fired. Substitute the actual mode pair and escalation reason. If multiple escalation rules fired simultaneously, list all: e.g., "stakes signals + time-pressure phrasing". Omit entirely when no escalation occurred.)

## Azimuth Verdict
(one line — clear position, no hedging)

## Recommended Decision
(PROCEED / PROCEED WITH SAFEGUARDS / PILOT FIRST / REDUCE SCOPE / DELAY PENDING EVIDENCE / REJECT / INSUFFICIENT SIGNAL / WRONG TOOL / RESIDUAL-RISK-REGISTER)
Rationale: (one to two sentences)

## Confidence Level
Low / Medium / High + why
(Omit this section when verdict is INSUFFICIENT SIGNAL)

---

## Critical Risks
(Severity-ordered, from the register. 1–5 entries. Do not pad.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
1. ...
2. ...
3. ...

## Weak Assumptions
(UNSUPPORTED or CONTRADICTED entries from Module 2. Omit section if none.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Falsifiers
(For each STRONG or PARTIAL assumption: what observable evidence would prove it wrong? Omit section if no strong or partial assumptions exist.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- [Assumption name]: [specific, observable falsifier]

## Likely Failure Paths
(Trigger → Cascade → Visible Failure → Business Cost. Reuses register entries; no new risks. If failure paths are fully captured by Critical Risks, omit this section — do not restate in narrative form what the register already shows.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Interaction Effects
(Pair-interactions where two risks together produce nonlinear failure. 1–5 entries max. Omit section if no genuine multiplicative interactions exist — do not pad.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- [Risk A] + [Risk B]: [specific mechanism by which their combination is worse than either alone]

## Highest-Leverage Fixes
(Structural changes only. Weak mitigations rejected.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Early Warning Indicators
(Omit if indicators are generic to all projects in the domain. Include only if monitoring a specific indicator would change a real action.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Structural Strengths
(Include only if a structural feature of this plan materially reduces a Critical Risk or changes the verdict. If nothing rises to that bar, omit. Do not include to balance the output.)
(Omit this section when verdict is INSUFFICIENT SIGNAL)
- ...

## Missing Inputs
(Required when verdict is INSUFFICIENT SIGNAL. List what is absent or contradictory,
and which question — if answered — would most unlock the analysis.)
- ...
```

---

# Output Format (Executive)

Load `references/output-format-executive.md`.

Use when: user is briefing leadership, wants a 1-pager, or says "keep it short."

---

# Output Format (Technical / Codebase)

Load `domain-policies/codebase-azimuth.md`.

Use for: refactors, migrations, legacy rewrites, infrastructure changes.

---

# Output Format (Product Launch)

Load `domain-policies/product-launch-azimuth.md`.

Use for: beta launches, v1 releases, feature rollouts with user-facing risk.

---

# Output Format (Hiring)

Load `domain-policies/hiring-azimuth.md`.

Use for: key hire decisions, contractor engagements, partnership roles.

---

# Output Format (Partnership / M&A)

Load `domain-policies/partnership-azimuth.md`.

Use for: mergers, acquisitions, strategic partnerships, joint ventures, significant vendor relationships with multi-quarter or multi-year commitment.

---

# Output Format (PE Secondaries IC)

Load `domain-policies/secondaries-ic-azimuth.md`.

Use for: PE secondaries investment committee decisions — GP-led continuation vehicles, direct secondary LP stake acquisitions, minority recaps / structured liquidity. Primary user is the IC investment partner, not the fund CFO.

---

# Anti-Slop Rules

Never:

- produce generic risk lists
- pad with 10+ low-value items
- treat all risks equally
- confuse possibility with probability
- use motivational filler
- hide uncertainty
- recommend proceed by default
- hallucinate industry facts
- give weak mitigations
- force a verdict when input is insufficient — return INSUFFICIENT SIGNAL instead
- substitute DELAY PENDING EVIDENCE for INSUFFICIENT SIGNAL when the block is missing input, not missing time

Always:

- rank severity
- name dominant constraint
- state missing evidence
- prefer realism over completeness
- be willing to recommend no-go
- be willing to return INSUFFICIENT SIGNAL when the analysis cannot be grounded
