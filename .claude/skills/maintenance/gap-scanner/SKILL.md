---
name: gap-scanner
description: Audits AZIMUTH's coverage completeness. Cross-references what SKILL.md claims to handle against what reference, diagnostic, and domain-policy files actually cover. Identifies thin coverage, missing domains, and structural inconsistencies. Run before major version planning.
---

# Gap Scanner

Find where AZIMUTH's stated coverage exceeds its actual reference support, and where reference material covers domains not yet claimed.

This skill reads files and produces a structured gap report. It does not propose fixes — it maps the delta between claims and reality.

---

## Protocol

Run all 6 steps sequentially. Read each file group before drawing conclusions.

---

### Step 1 — Extract Coverage Claims from SKILL.md

Read `SKILL.md`. Extract and list:

1. Every decision type in "Use When"
2. Every domain named in the DEEP mode load rules (tech/engineering → `software-failure-patterns.md`, product/launch → `launch-risks.md`, startup/venture → `startup-failures.md`)
3. Every diagnostic load condition (which module trigger → which diagnostic file)
4. Every domain-policy route (which Layer-3 domain → which file in `domain-policies/`)
5. Every domain explicitly named in the base rate load rule

---

### Step 2 — Audit Reference Files Against Claims

For each domain claimed in Step 1, read the corresponding reference file. Assess coverage depth:

- **STRONG**: File provides specific patterns, mechanisms, and diagnostic questions for this domain
- **PARTIAL**: File mentions the domain but coverage is thin, hedged, or missing mechanisms
- **THIN**: Domain is in base-rates.md but has no corresponding pattern file
- **MISSING**: Domain is claimed in SKILL.md but no reference material exists for it

Known gaps to confirm (from prior analysis):
- **M&A / Partnerships**: base-rates.md has a full M&A section. Is M&A listed in SKILL.md "Use When"? Is there a pattern file for M&A failure modes? Is there a domain-policy?
- **IT / Infrastructure Migration**: base-rates.md has a migration section. Is there a pattern file? A domain-policy?
- **Organizational Change**: base-rates.md has an org change section. Is org restructure in SKILL.md "Use When"? Pattern file? Domain-policy?

For each gap found, record:
- What is claimed (exact quote from SKILL.md)
- What exists (file and coverage depth)
- The delta

---

### Step 3 — Audit Diagnostic Files Against Load Conditions

Read `SKILL.md` STANDARD mode diagnostic load conditions. For each condition:

1. Does the referenced diagnostic file exist?
2. Does the file actually handle the specific condition described? (Not adjacent to it — the condition itself)
3. Is the file's process depth appropriate for what the condition implies?

Diagnostic load conditions:
- Module 2: 3+ unsupported or any contradicted assumption → `diagnostics/assumption-audit.md`
- Module 4: governance-level incentive conflict → `diagnostics/incentive-conflicts.md`
- Module 5: critical SPOF or concentration risk → `diagnostics/dependency-map.md`
- Module 8: high irreversibility + late detectability → `diagnostics/fragility-scan.md`

For each: does the file's output format and process cover the triggering condition?

---

### Step 4 — Audit Domain-Policy Files Against Decision Types

Read each domain-policy file. For each:

1. Does it serve the decision type it's routed for?
2. Does it add domain-specific value beyond the default output format? (If it's just a renamed default format, it's redundant)
3. Which decision types in SKILL.md "Use When" have no domain-policy?

Domain-policies to check:
- `domain-policies/codebase-azimuth.md` — for refactors, migrations, rewrites
- `domain-policies/product-launch-azimuth.md` — for launches, rollouts, go-lives
- `domain-policies/hiring-azimuth.md` — for key hires, contractor engagements

Presentation-format files (not domain-policies; audit separately for cross-policy compatibility):
- `references/output-format-executive.md` — 1-page leadership briefing format paired with any domain-policy

Decision types in SKILL.md with no domain-policy: identify and list.

---

### Step 5 — Gotcha / Reference Overlap Check

Read `gotchas.md`. SKILL.md states: gotchas cover "organizational, behavioral, or temporal" failure modes; reference pattern files cover "technical or domain-specific" modes.

For each of the 8 gotchas:
- Does its core mechanism appear in any of the pattern reference files (`software-failure-patterns.md`, `startup-failures.md`, `launch-risks.md`)?
- If yes: is the overlap additive (different framing of the same pattern adds value) or redundant (exact same content in two places)?

Report: overlaps found, whether they should be consolidated, differentiated, or accepted.

---

### Step 6 — Unclaimed Domain Scan

Read all reference files. Identify failure modes, domains, or decision types that:
- Appear in reference material but are not named in SKILL.md "Use When" or DEEP mode rules
- Represent decisions AZIMUTH could plausibly handle but currently doesn't claim

These are expansion candidates. Label them as such — not bugs, not immediate action items.

---

## Output Format

```
GAP SCANNER REPORT — [date]

## Coverage Claims vs. Reference Support

| Domain | Claimed in SKILL.md | Reference file | Domain-policy | Coverage depth |
|--------|--------------------|--------------|---------|----|
| Software / Engineering | [yes/no] | software-failure-patterns.md | codebase-azimuth.md | STRONG |
| Product / Launch | [yes/no] | launch-risks.md | product-launch-azimuth.md | [depth] |
| Startup / Venture | [yes/no] | startup-failures.md | none | [depth] |
| M&A / Partnerships | [yes/no] | none | none | [depth] |
| IT / Infrastructure Migration | [yes/no] | none | none | [depth] |
| Organizational Change | [yes/no] | none | none | [depth] |
| Hiring | [yes/no] | none (base rates only) | hiring-azimuth.md | [depth] |

## Diagnostic File Gaps

[For each STANDARD mode load condition: COVERED / PARTIAL / GAP — with detail]

## Domain-Policy Coverage Gaps

[Decision types with no domain-policy, listed with estimated usage frequency]

## Gotcha / Reference Overlap

[Pattern, overlap location, recommendation: ACCEPT / DIFFERENTIATE / CONSOLIDATE]

## Unclaimed Domains (Expansion Candidates)

[Domain, where it appears in reference material, what adding it would require]

## Priority Gaps

[Top 3 by impact on AZIMUTH's stated mission — with recommended action and scope estimate]
```

---

## Constraints

- Read all files before drawing conclusions — do not rely on prior knowledge of file contents
- Report gaps only; do not propose content
- Expansion candidates are observations, not action items; label them clearly
- If a file cannot be read, report it as unreadable rather than assuming absence
