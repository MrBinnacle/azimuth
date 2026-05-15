# Decision Record Template

Use when the user asks for an exportable decision record, when MULTI-LENS is used, or when a DEEP run produces a consequential verdict.

---

## Template

```markdown
# Decision Record: [Decision]

Date: [YYYY-MM-DD]
Decision owner: [owner]
AZIMUTH mode: [FAST / STANDARD / RAPID / DEEP]
Advanced lenses loaded: [none / L-I / Bias Scan / Risk Triage / Multi-Lens / FOOL]

## Decision
[PROCEED / PROCEED WITH SAFEGUARDS / PILOT FIRST / REDUCE SCOPE / DELAY PENDING EVIDENCE / REJECT / RESIDUAL-RISK-REGISTER]

## Rationale
[1-3 sentences]

## Critical Assumptions
| Assumption | Evidence Class | Falsifier | Review Date |
|---|---|---|---|

## Critical Risks
| Risk | Category | L/I Score | Owner | Leading Indicator | Escalation Trigger |
|---|---|---:|---|---|---|

## Commitments
| Action | Owner | Due / Review Date | Evidence of Completion |
|---|---|---|---|

## Alternatives Considered
| Alternative | Why rejected / deferred | Opportunity cost |
|---|---|---|

## Revisit Conditions
- [condition]
- [condition]

## Outcome Review
Scheduled review date: [YYYY-MM-DD]
Outcome notes: [blank until review]
```

---

## Use Rules

- Do not include raw diagnostic clutter.
- Preserve only decision-changing evidence.
- Every commitment must be owned and dated.

---

## Provenance

Original AZIMUTH template inspired by lightweight ADR / decision-record practices and decision-toolkit export patterns.
