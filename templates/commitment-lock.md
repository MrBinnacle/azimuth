# Commitment Lock Template

Use in DEEP mode and in STANDARD when the verdict is PROCEED, PROCEED WITH SAFEGUARDS, PILOT FIRST, DELAY PENDING EVIDENCE, or RESIDUAL-RISK-REGISTER.

---

## Purpose

A decision-pressure test only matters if it changes the plan. Commitment Lock converts findings into owned, dated actions.

This is not a generic action-items list. Each item must map to a Critical Risk, Weak Assumption, Launch-Blocking Tiger, or residual risk.

---

## Commitment Triplet

Use this format:

| Risk / Finding | Action | Owner | Leading Indicator | Review Date | Stop / Escalate Trigger |
|---|---|---|---|---|---|
| [risk] | [specific structural action] | [one owner] | [observable signal] | [date] | [condition that changes decision] |

The minimum unit is actually five fields: **Action + Owner + Leading Indicator + Review Date + Escalation Trigger**.

---

## Rules

- Every Launch-Blocking Tiger needs a Commitment Lock entry.
- Every accepted Red/Black L×I risk needs a Commitment Lock entry.
- Every residual risk needs a leading indicator and escalation trigger.
- Owners must be singular. "Team" is not an owner.
- Review dates must be calendar dates or named decision checkpoints.
- Weak mitigations are rejected.

---

## Confirmation Block

For DEEP mode, end with:

```markdown
## Commitment Lock
The decision should not be treated as accepted until the following commitments are explicitly owned:

[table]

Confirmation required: [decision-maker] accepts these owners, indicators, and review dates before proceeding.
```

For STANDARD mode, include the table when it changes the verdict or prevents a soft PROCEED.

---

## Residual-Risk Variant

When Module 10 returns RESIDUAL-RISK-REGISTER, do not ask whether to proceed. Use:

```markdown
## Residual Risk Commitments
| Residual Risk | Owner | Leading Indicator | Escalation Trigger | First Review |
|---|---|---|---|---|
```

---

## Provenance

Adapted from commitment mechanisms in premortem practice and the commitment gap identified in DasClown/premortem-skill `AUDIT.md`. Implemented as an AZIMUTH verdict-to-action gate.
