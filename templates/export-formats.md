# Export Formats

Use when the user wants AZIMUTH output to become an operational artifact in CSV, Jira, GitHub Issues, Obsidian, Notion, or a plain Markdown decision packet.

---

## CSV Risk Register

```csv
id,risk,category,urgency,likelihood,impact,score,evidence,owner,leading_indicator,review_date,escalation_trigger,status
R1,"[risk]","Tiger","Launch-Blocking",4,5,20,"[evidence]","[owner]","[indicator]","YYYY-MM-DD","[trigger]","open"
```

Required fields:

- `risk`
- `category`
- `evidence`
- `owner` for Launch-Blocking / Fast-Follow / Elephant
- `leading_indicator`
- `review_date` or decision checkpoint
- `escalation_trigger`

---

## Jira / GitHub Issue

```markdown
## Risk / Finding
[Clear description]

## Source
AZIMUTH verdict: [verdict]
Category: [Tiger / Paper Tiger / Elephant]
L/I score: [score]
Evidence class: [Strong / Partial / Unsupported / Contradicted]

## Required Action
[Specific structural action]

## Acceptance Criteria
- [ ] Evidence gate satisfied: [gate]
- [ ] Leading indicator instrumented: [indicator]
- [ ] Escalation trigger agreed: [trigger]
- [ ] Review date scheduled: [date]

## Owner
[one accountable person/role]
```

---

## Obsidian Decision Note

```markdown
---
type: decision-record
date: YYYY-MM-DD
azimuth_mode: [mode]
verdict: [verdict]
confidence: [low/medium/high]
status: active
review_date: YYYY-MM-DD
tags: [azimuth, decision, risk]
---

# [Decision]

## Verdict
[verdict + rationale]

## Critical Risks
- [[R1]] — [risk]

## Commitments
- [ ] [Action] — owner: [owner] — review: [date]

## Revisit Conditions
- [condition]
```

---

## Notion / Table Fields

Recommended properties:

| Property | Type | Notes |
|---|---|---|
| Name | Title | Risk or decision name |
| Verdict | Select | AZIMUTH verdict |
| Category | Select | Tiger / Paper Tiger / Elephant |
| L/I Score | Number | 1-25 |
| Evidence Class | Select | Strong / Partial / Unsupported / Contradicted |
| Owner | Person/Text | Single accountable owner |
| Review Date | Date | Next decision checkpoint |
| Leading Indicator | Text | Observable early signal |
| Escalation Trigger | Text | Condition that changes action |
| Status | Select | Open / Accepted / Mitigated / Closed |

---

## Use Discipline

Export only the top decision-changing risks and commitments. A polished artifact that includes every speculative risk is worse than a shorter register people actually use.

---

## Provenance

Original AZIMUTH template for production-ready handoffs. Designed to reduce post-analysis formatting work.
