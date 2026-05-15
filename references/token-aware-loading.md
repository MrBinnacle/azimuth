# Token-Aware Loading and Drill Commands

Load when extending AZIMUTH or when a run risks bloat from too many diagnostics.

---

## Purpose

AZIMUTH's advantage is progressive disclosure. The core should route sharply; depth should load only when it changes the decision.

---

## Drill Commands

Users can force specific modules without turning on every advanced lens:

| Command | Loads |
|---|---|
| `AZIMUTH DRILL: commitments` | `templates/commitment-lock.md`, `references/workflow-closure.md` |
| `AZIMUTH DRILL: score` | `diagnostics/likelihood-impact-matrix.md` |
| `AZIMUTH DRILL: triage` | `diagnostics/risk-triage.md`, `references/risk-categories.md` |
| `AZIMUTH DRILL: bias` | `diagnostics/bias-scan.md`, optionally `references/bias-encyclopedia.md` |
| `AZIMUTH DRILL: export` | `templates/export-formats.md`, `templates/decision-record.md` |
| `AZIMUTH DRILL: audit` | `references/audit-trail.md` |
| `AZIMUTH DRILL: learn` | `learnings/outcome-tracking.md` |
| `AZIMUTH MULTI-LENS` | `references/multi-frameworks.md`, `templates/multi-lens-summary.md` |
| `AZIMUTH FOOL: [mode]` | `references/critical-reasoning-modes.md` |

---

## Loading Budget

Use this order:

1. Core SKILL routing and modules
2. Domain template / domain reference
3. Only diagnostics whose triggers fired
4. Only templates needed for final artifact
5. Audit/provenance only for DEEP or exportable records
6. Learning loop only after outcome evidence exists

If more than three optional files would load in STANDARD, stop and ask whether the user wants deeper analysis or a lean verdict.

---

## Integration Rule

Optional files must change at least one of:

- evidence classification
- L/I score
- risk category
- verdict
- commitment / owner / indicator
- export artifact
- learning update

If not, do not include their output.

---

## Provenance

Original AZIMUTH loading discipline for modular adoption-oriented extensions.
