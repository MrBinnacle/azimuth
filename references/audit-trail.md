# Audit Trail and Provenance Tags

Load when DEEP mode, MULTI-LENS, external references, or any consequential recommendation needs traceability.

---

## Purpose

The reader should know why AZIMUTH reached the verdict, which modules ran, what evidence changed the decision, and which claims are unsupported.

Audit trail is not academic citation bloat. It is operational accountability.

---

## Claim Tags

Use compact tags in decision records or DEEP outputs:

| Tag | Meaning |
|---|---|
| `[USER]` | Provided directly by user |
| `[PLAN]` | Derived from supplied plan text |
| `[BASE-RATE]` | Grounded in `references/base-rates.md` or domain reference |
| `[DIAGNOSTIC]` | Produced by an AZIMUTH diagnostic file |
| `[INFERENCE]` | Reasoned from context; not directly evidenced |
| `[MISSING]` | Required evidence absent |
| `[CONFLICT]` | Evidence contradicts the plan or another claim |

Do not tag every sentence. Tag decision-driving claims only.

---

## Module Audit

For DEEP and exportable decision records, include:

```markdown
## Audit Trail
| Module / Lens | Ran? | Decision-changing finding |
|---|---:|---|
| Objective Integrity | Yes | ... |
| Assumption Audit | Yes | ... |
| Incentive Scan | Yes | ... |
| L/I Matrix | Yes | ... |
| Risk Triage | Yes | ... |
| Multi-Lens | No | Not triggered |
```

---

## Provenance Line

When borrowing a framework or running a drill-down, include a one-line provenance note in the artifact if it affects the output:

```markdown
Provenance: Used AZIMUTH `risk-triage` and `likelihood-impact-matrix` diagnostics; no external claims beyond user-supplied plan and loaded base-rate references.
```

---

## Anti-Patterns

- Do not use provenance tags to make weak inference look strong.
- Do not cite a framework as evidence for a factual claim.
- Do not include audit trail in FAST mode unless user asks.
- Do not let traceability obscure the verdict-first rule.

---

## Provenance

Implements AZIMUTH's planned evidence tags and audit-trail roadmap item.
