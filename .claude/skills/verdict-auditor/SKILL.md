---
name: verdict-auditor
description: Stress-tests an AZIMUTH output against the skill's own structural rules. Paste an AZIMUTH output and invoke to get a severity-rated diagnostic. Diagnoses only — does not rewrite. Use after any real AZIMUTH session to detect quality drift.
---

# Verdict Auditor

Apply AZIMUTH's own rules against its own output. Find where the skill drifted from its discipline.

This skill does not improve the output. It identifies exactly what rule was violated and how severely. Rewrites happen in a separate session.

---

## Input

User pastes an AZIMUTH output. If none is provided, ask: "Paste the AZIMUTH output to audit."

---

## Audit Checks

Run all 8 checks. Assign each finding a severity: **CRITICAL** / **MODERATE** / **MINOR**.

---

### Check 1 — Verdict-First Rule

**Rule**: The first three elements of every output must be: (1) Azimuth Verdict line, (2) Recommended Decision, (3) Confidence Level. Nothing else precedes them.

**How to check**: Read the first 10 lines. Does anything appear before the verdict line?

**Severity if violated**: CRITICAL — the reader cannot act on the first paragraph alone.

---

### Check 2 — Empty Section Rule

**Rule**: Do not emit a section header with no substantive content. If a section has nothing genuine, it must be omitted entirely.

**How to check**: Scan all section headers. Is there any header followed by a placeholder, "N/A," "none identified," or a single generic sentence?

**Severity if violated**: MODERATE — signals padding; reduces trust in sections that do have content.

---

### Check 3 — Register Deduplication

**Rule**: Modules 2, 5, 6, 7, and 8 feed a shared register. The same risk or assumption must not appear independently in multiple output sections. It is cited once in the most relevant section; other sections reference it by tag.

**How to check**: Does the same underlying risk appear in both Critical Risks and Likely Failure Paths as if they are independent? Does the same assumption appear in both Weak Assumptions and Critical Risks as a separate entry?

**Severity if violated**: MODERATE — register duplication bloats output and obscures which entries are actually high-severity.

---

### Check 4 — Failure Path Source Check

**Rule**: Likely Failure Paths reuse register entries. They do not introduce risks that are not already in Critical Risks.

**How to check**: For each failure path, identify the root risk. Does that risk appear in Critical Risks? If a failure path introduces a risk that appears nowhere else in the output, flag it.

**Severity if violated**: MODERATE — unregistered risks in failure paths bypass the severity-ranking system.

---

### Check 5 — Weak Mitigation Scan

**Rule**: Mitigations must change system conditions. The following are rejected by the skill's own anti-slop rules.

Scan Highest-Leverage Fixes for any of:
- "communicate better" / "improve communication" / "ensure clear communication"
- "monitor closely" / "monitor carefully" / "keep an eye on"
- "work harder" / "increase effort" / "be more diligent"
- "be more careful" / "exercise caution"
- Any mitigation that describes an attitude rather than a structural change

**Severity if violated**: CRITICAL per instance — weak mitigations are a defined failure mode of the skill.

---

### Check 6 — Verdict Calibration

**Rule**: The verdict must be consistent with the evidence in the output. Four specific calibration failures are defined:

- Confidence Level is **Low** AND Recommended Decision is **PROCEED** → flag (low-confidence proceed)
- Critical Risks section contains 3+ HIGH-severity items AND verdict is PROCEED WITH SAFEGUARDS or weaker → flag (verdict undershoots severity)
- Weak Assumptions section contains a **CONTRADICTED** entry AND verdict is PROCEED → flag (contradicted assumptions require at minimum PILOT FIRST)
- Input was sparse (inferable from thin analysis depth) AND verdict is anything other than INSUFFICIENT SIGNAL or DELAY PENDING EVIDENCE → flag (false-precision verdict)

**Severity if violated**: CRITICAL — miscalibrated verdicts are the primary failure mode the skill is designed to prevent.

---

### Check 7 — Padding Check

**Rule**: Critical Risks lists 1–5 entries. Risks must be specific to this decision, not generic.

Check:
- Does Critical Risks list more than 5 items?
- Does any risk entry read as generic rather than specific? (e.g., "timeline may slip" without naming which constraint, who owns it, and what the mechanism is)
- Are any entries labeled "risks" that are actually uncertainties with no identified failure mechanism?

**Severity if violated**: MINOR — padding dilutes the severity signal of genuine risks.

---

### Check 8 — Base Rate Opportunity

**Rule**: When the decision domain matches a section in `references/base-rates.md`, a relevant base rate should be cited in Module 7 output.

Domains covered: software projects, startups/new ventures, product launches, hiring, M&A/partnerships, IT migrations, organizational change.

If the decision clearly falls in one of these domains and no base rate appears in the output, flag it.

**Severity if violated**: MINOR — a relevant calibration prior was available and not used.

---

## Output Format

```
VERDICT AUDIT — [date if available, otherwise "undated output"]
Decision audited: [one-line summary of the decision from the output]

CRITICAL: [N] | MODERATE: [N] | MINOR: [N]

---
[For each finding, in severity order:]

[SEVERITY] — Check [N]: [Check name]
Observed: [specific quote or observation from the output]
Rule: [quote the specific rule violated]

---
OVERALL: [One sentence — did this output meet AZIMUTH's discipline, partially meet it, or fail it?]
```

If no issues found:
```
VERDICT AUDIT — [date]
Decision audited: [...]
CRITICAL: 0 | MODERATE: 0 | MINOR: 0
Output meets AZIMUTH's structural discipline.
```

---

## Constraints

- Do not rewrite or improve the output — diagnose only
- Every finding must cite a specific rule from SKILL.md or this file; no invented criteria
- Do not flag style, word choice, or analytical depth — only structural and rule violations
- Do not flag a MODERATE or MINOR issue as CRITICAL
