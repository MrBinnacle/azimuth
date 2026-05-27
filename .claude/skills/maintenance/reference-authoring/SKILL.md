---
name: reference-authoring
description: |
  Authoring discipline for new AZIMUTH reference files and templates. Use when
  adding a new domain reference file, extending an existing one, or creating a
  new template. Covers: (1) EXTEND vs. CREATE decision heuristic, (2) the Module 7
  vocabulary header pattern that prevents domain-gap recurrence, (3) the sourcing
  caveat pattern for narrow-evidence-base files, (4) pre-verdict gate structure
  for templates. Validated by research-mpbaese4 (2026-05-18).
author: Claude Sonnet 4.6
version: 1.0.0
date: 2026-05-18
---

# Reference File Authoring Discipline

## Problem

Each new domain addition to AZIMUTH risks leaving Module 7 without vocabulary
for the new domain — or creating redundant files when extension was the right
operation. The symptoms: Module 7 produces generic output for a domain, or the
analyst must load two files to complete one domain analysis.

## EXTEND vs. CREATE Decision

**EXTEND an existing file when:**
- Adding ≤ 3 new patterns (≤ 30% increase on a 10-pattern file)
- The majority of existing patterns already apply to the new domain
- The file's own load condition already covers the new domain

**CREATE a new file when:**
- Adding 6+ patterns that are distinct from the existing file
- The new domain requires different load conditions than the host file
- Loading both the existing file and new content would require two separate loads anyway

*Example applied:* Migration patterns (3 patterns, 9 of 10 existing patterns apply to
migrations) → EXTEND `software-failure-patterns.md`. Hiring patterns (6 patterns,
zero overlap with software failure modes) → CREATE `hiring-failure-patterns.md`.

At 4–5 patterns, use judgment: if the domain is structurally distinct and all patterns
are domain-specific (not shared with the host file), CREATE. If the domain shares most
of its mechanisms with the host file, EXTEND.

## Module 7 Vocabulary Header

Every new reference file and template must answer this question in its header:

> "What vocabulary and diagnostic anchors does this file supply to Module 7?"

Without this, each new domain leaves Module 7 producing generic output — the analyst
gets no domain-specific signal even when the file is loaded.

**Format** (include near the top of the file, after the load condition):

```markdown
**Module 7 vocabulary this file supplies:** [list of specific terms, base rates,
and diagnostic anchors — e.g., "coachability as a distinct failure mode (26% of
failures); interpersonal vs. technical failure rate inversion (81% vs. 11%)"]
```

*Why it matters:* The gap scanner found that the hiring and startup domains both hit
the same failure — Module 7 expected template-supplied domain vocabulary that wasn't
there. The Module 7 header makes this provision explicit and checkable.

## Sourcing Caveat Pattern

Include a sourcing note near the top of any reference file where the evidence base is
narrower than `software-failure-patterns.md` or `ma-partnership-patterns.md`.

**Include when:**
- Primary source is a single study or report (even a large one)
- Methodology of the primary source is undisclosed
- Evidence base has not been replicated across multiple independent sources

**Format:**

```markdown
**Sourcing note:** Pattern rates below are drawn primarily from [Source] ([year],
N=[sample], [methodology caveat if applicable]). Treat percentage rates as
directional, not precise. Evidence base is narrower than [comparator file].
```

*Example:* `hiring-failure-patterns.md` draws primarily from Leadership IQ 2011
(N=5,247, methodology undisclosed) and Schmidt & Hunter 1998. Rates cited as
directional accordingly.

## Pre-Verdict Gate Structure (Templates)

Use explicit blocking gates — not just checkboxes — when a pattern is structurally
impossible to surface without a structured diagnostic section.

**Signal that a gate is needed:** The failure pattern requires specific arithmetic
(runway scenarios), a governance checklist (co-founder structure), or a concentration
threshold (>40% customer share) that cannot be expressed as prose.

**Gate structure:**
1. Run the gate before the verdict section (not after)
2. State the blocking condition explicitly: "Any PENDING item blocks PROCEED verdict"
3. Include the specific threshold or criterion inline, not as a footnote

*Example gates validated this session:*
- **PMF Validation Gate** — 3+ behavioral YES required; absent PMF locks confidence
  ceiling at LOW and blocks PROCEED/PROCEED WITH SAFEGUARDS
- **Runway Scenario Table** — three rows: base / optimistic (+40% revenue) /
  pessimistic (−40% revenue, +20% burn); < 6 months in pessimistic = hard block
- **Co-Founder Structure Check** — any PENDING item blocks PROCEED regardless of
  other findings

Distinguish gates from checklists: gates have explicit verdict consequences stated
in the gate itself. Checklists surface information; gates block verdicts.

## Validation After Authoring

Run these checks before committing any new reference file or template:

```bash
# 1. All paths referenced in SKILL.md must exist
grep -oE '(references|diagnostics|templates)/[^ \n"`]+\.md' SKILL.md | sort -u | \
  while read f; do test -f "$f" && echo "OK: $f" || echo "MISSING: $f"; done

# 2. SKILL.md frontmatter description must remain 489 chars
awk '/^description: /{flag=1} flag{print; if(/"$/) flag=0}' SKILL.md | tr -d '\n' | wc -c

# 3. gotchas.md must still have exactly 8 numbered sections
grep -E '^## [0-9]+\.' gotchas.md | wc -l
```

## Notes

- The Module 7 vocabulary header is the main architectural defense against gap
  recurrence. If a new domain is added without this header, the gap scanner will
  catch the symptom (Module 7 producing generic output) but not the cause.
- EXTEND operations require no SKILL.md changes if the domain is already in the
  DEEP mode load rules. Migration patterns required no SKILL.md change; hiring
  required one line added to the DEEP mode domain reference block.
- Reference file pattern format: `## Pattern N: [Title]` / `**What happens**:` /
  `**Failure signature**:` (bullet list) / `**Azimuth question**:`. Match density
  and register of `software-failure-patterns.md` exactly.
