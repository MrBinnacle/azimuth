---
name: research-scout
description: Tracks AZIMUTH's 8 primary citation source families for new publications or significant updates. Stages validated findings in research/staged-findings.md for human review before promotion to references/base-rates.md. Invoke with 'run the research scout' or 'promote staged findings'.
---

# Research Scout

Maintain AZIMUTH's empirical integrity by tracking source publications and staging updates to `references/base-rates.md`.

This skill has two modes. Trigger is determined from the user's request.

**SCOUT** — Search for new publications. Stage validated findings.
**PROMOTE** — Review `research/staged-findings.md`. Promote, hold, or discard each staged entry.

Trigger PROMOTE when user says "promote," "review staged findings," or "what's in the queue."

---

## Source Map

`references/base-rates.md` draws from 8 source families. Each has a day-of-week assignment. Do not search all groups every run.

| Day | Source Family | What constitutes a finding |
|-----|--------------|---------------------------|
| Mon | Standish CHAOS + PMI *Pulse of the Profession* | New annual edition; changed on-time/overrun rates |
| Tue | CB Insights startup failure reports | New edition (last known: 2021); updated failure-cause percentages |
| Wed | BLS Business Employment Dynamics | New annual entrepreneurship/survival cohort tables |
| Thu | McKinsey large IT projects + transformation research | New survey citing overrun or value-delivery figures |
| Fri | Nielsen Breakthrough Innovation + consumer launch research | New consumer product failure rate data |
| Sat | Pendo Feature Adoption + B2B SaaS adoption research | New feature utilization dataset |
| Sun | Schmidt & Hunter follow-on meta-analyses + KPMG/Bain M&A + Flexera *State of the Cloud* | New predictive validity meta-analysis; M&A value-destruction update; cloud migration overrun data |

---

## SCOUT Mode

### Step 1 — Search

For today's source family, run:
1. `WebSearch`: `"[source name]" [current year] report`
2. `WebSearch`: `site:[publisher domain] [topic] [current year]`

Maximum 3 searches per source family. Do not search topics outside the assigned family.

### Step 2 — Filter

**Keep only:**
- New edition or meaningful update to a previously cited source
- Data that materially changes a figure in `references/base-rates.md` (direction reversal, or >15% change in a cited rate)
- A new rigorous source that improves on a currently hedged or weakly attributed claim
- Retraction or significant methodological critique of a currently cited source

**Discard:**
- Blog posts or secondary commentary citing the same primary source already in base-rates.md
- Consultant reports without disclosed methodology
- Publications predating 2023 (within training data; not net-new signal)
- Any result without a verifiable URL to the primary source

### Step 3 — Stage

Append each surviving finding to `research/staged-findings.md`:

```
## [YYYY-MM-DD] [Source Name] — [Brief title]
**URL:** [direct link to primary source — not a search results page]
**Source family:** [which rotation day]
**Current base-rates.md claim:** "[quote the exact sentence this finding would update or replace]"
**New finding:** [what the source actually says — one sentence, no paraphrase that changes numerical meaning]
**Impact:** UPDATE existing claim / ADD new claim / CONTRADICTS cited source / IMPROVES attribution
**Confidence:** High / Medium / Low — [one reason]
**Status:** STAGED
```

Maximum 3 findings per SCOUT run.

If 0 findings survive filtering:
```
## [YYYY-MM-DD] NO NEW FINDINGS
Sources searched: [list]
```

### Step 4 — Report

```
RESEARCH SCOUT — [date]
Source family searched: [which rotation]
Searches run: [N]
Findings staged: [N]
Discarded: [N] — [brief reason if any]

Staged:
[list titles]

Run 'promote staged findings' to review queue.
```

---

## PROMOTE Mode

Read `research/staged-findings.md`. For each entry with `Status: STAGED`:

1. Read the current relevant section of `references/base-rates.md`
2. Present the staged finding and the current text side by side
3. State a recommendation: promote, hold, or discard — with one-sentence rationale
4. Wait for explicit user decision per finding
5. On **promote**: edit `references/base-rates.md` with the new or updated claim. Update entry status to `PROMOTED — [date]`
6. On **hold**: leave status as STAGED
7. On **discard**: update status to `DISCARDED — [reason]`

Do not edit `references/base-rates.md` without explicit user confirmation.

---

## Constraints

- Never write directly to `references/base-rates.md` without PROMOTE mode and explicit confirmation
- Never stage a finding without a direct URL to the primary source
- Never paraphrase in a way that changes a numerical claim
- Maximum 3 staged findings per SCOUT run; no cap on PROMOTE sessions
- Pattern files (`references/startup-failures.md`, `software-failure-patterns.md`, `launch-risks.md`) are out of scope — route any findings about those to a separate editorial session
