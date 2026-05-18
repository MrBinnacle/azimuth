# Mode Behaviors

Load this file for STANDARD, RAPID, and DEEP modes. FAST mode does not load this file.

---

## FAST

Run:
- Objective Check
- Assumption Audit (top 3 assumptions only)
- Top 3 Failure Paths
- Verdict

Do not load diagnostics or references.

Module 4 interview not conducted. Incentive misalignment is unverified in this output, including self-proposal incentive: if the assistant previously advocated for the option under analysis, that bias is unaudited in FAST mode. If incentive conflicts or self-proposal are material concerns, rerun in STANDARD or RAPID mode.

**M4 PRE-CHECK in FAST mode:** If self-advocacy is detected (the assistant previously proposed the option), the interview cannot run — but the detection must still be noted. Add to the output header: `[SELF-ADVOCACY DETECTED — M4 unaudited in FAST; rerun in STANDARD or RAPID for full incentive audit]`. Do not silently omit the detection.

---

## STANDARD

Default. Run all 10 core modules.

**Diagnostic loading in STANDARD is conditional, not automatic.** Load a diagnostic file only when the corresponding module surfaces a high-severity finding the user would benefit from drilling into:

- Module 2 surfaces 3+ unsupported assumptions or any contradicted assumption → load `diagnostics/assumption-audit.md`
- Module 4 surfaces a governance-level incentive conflict → load `diagnostics/incentive-conflicts.md`
- Module 5 surfaces a critical SPOF or concentration risk → load `diagnostics/dependency-map.md`
- Module 8 surfaces high irreversibility + late detectability → load `diagnostics/fragility-scan.md`

Load `references/base-rates.md` only when the user's plan involves a category covered by the file (software project, startup, launch, hire, M&A, migration, org change) AND the user's stated estimates appear to deviate from typical historical ranges.

Consult `gotchas.md` when either of these conditions fires. If the file is visible in context, treat its 8 patterns as active only when a trigger fires — not by default:
- Module 4 interview returns RED tier, OR any incentive conflict is governance-level
- Module 6 failure chains all match canonical patterns (scope creep, resource shortage, stakeholder misalignment) with no plan-specific trigger — availability inversion required

If neither condition fires, do not cite the 8 patterns or generate output influenced by them even if the file is visible. If a condition fires but the file is not visible, note: "Gotcha trigger fired ([condition]). Operating from structural patterns by recall; DEEP-mode rerun recommended for full pattern access."

---

## RAPID

Use for high-stakes or irreversible decisions made under time pressure (hours, not days).

Run at full depth:
- Module 1 — Objective Integrity Check
- Module 4 — Incentive Scan & Interview (full 7-question interview; do not abbreviate)
- Module 8 — Detectability & Recovery
- Module 10 — Decision Verdict

Run abbreviated:
- Module 2 — top 3 assumptions and falsifiers only
- Module 3 — dominant constraint only; no enumeration
- Module 5 — critical SPOFs only; no full inventory
- Module 6 — top 1 failure chain; coupling pass skipped
- Module 9 — one highest-leverage fix only

Module 7 (Base Rate Reality Check) is omitted in RAPID. Base-rate calibration is low-yield under hours-of-time-pressure relative to incentive (Module 4) and recoverability (Module 8) work.

Do not load diagnostics or domain references.

Rationale: Time pressure amplifies deadline-politics incentive distortion and concentrates the value of reversibility analysis. Modules 4 and 8 must run at full depth precisely because they are harder to recover from when skipped under pressure.

**If the user pushes back on the Module 4 interview citing time pressure:** State explicitly — "The interview is the highest-leverage part of RAPID. Skipping it locks confidence at LOW and removes PROCEED as a verdict option. If you have time for any questions, prioritize Q1 [IDENTITY] and Q4 [DISSENT]." Then proceed under whichever tier the answered count produces. Do not skip the interview silently. Do not treat time-pressure refusal differently from any other refusal — both apply the RED tier rules if fewer than 5 questions are answered or Q1 is skipped.

---

## DEEP

Use for high-stakes / expensive / irreversible decisions per signals above.

Run all 10 modules + load:
- `gotchas.md` — all 8 patterns are evaluation lenses in DEEP; apply each pattern to this specific plan and cite it only when a plan-specific trigger fires. Loading is unconditional; firing each pattern is still trigger-gated.
- `references/base-rates.md`
- All four `diagnostics/` files

Also load the relevant domain reference:
- Tech / engineering → `references/software-failure-patterns.md`
- Product / launch → `references/launch-risks.md`
- Startup / venture → `references/startup-failures.md`
- M&A / partnerships → `references/ma-partnership-patterns.md`
- Org change / restructure → `references/org-change-patterns.md`
- Hiring → `references/hiring-failure-patterns.md`
- PE Secondaries IC → `templates/secondaries-ic-azimuth.md` serves as the domain
  depth layer directly. The template contains the failure pattern screen (Section 1),
  process integrity gate (Section 2), NAV reliability assessment (Section 3), and
  incentive alignment scan (Section 5a) that other domains carry in separate reference
  files. No separate reference file is needed; load the template in DEEP mode for PE
  Secondaries IC decisions.
