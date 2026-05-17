# research-scout gotchas

Append-only. Label observed entries with the date. Label anticipated entries with [ANTICIPATED].
Never delete. A long list signals real stress-testing.

---

## 1. Paraphrase inverts the finding (observed — 2026-05-07)

Roose et al. 2023: staged description said "Teams revised plans after the premortem."
The paper's central finding is the *plan-revision gap* — teams *did not sufficiently revise*.
The staged claim was the exact opposite of the paper's conclusion.

**Rule:** Restate the finding in the paper's own terms before paraphrasing. If the paper
frames a result as a failure or gap, the staged entry must use that framing.

---

## 2. Attribution bleed — fact sourced to the wrong paper (observed — 2026-05-07)

Roose 2023 staged entry included satisfaction trajectory data that actually came from
Kaplan & Gruenfeld 2022 — a different paper entirely.

**Rule:** Before staging a numerical or behavioral claim, verify it appears in the specific
paper you are citing, not in a related paper cited *by* that paper.

---

## 3. Staging before filter step completes (observed — 2026-05-07)

Fasolo 2025: staged entry included unsupported facilitation/attribution claims that were
added before Step 2 (filter) was fully applied. PROMOTE mode caught them and they were
removed on promotion.

**Rule:** Complete the filter step fully before writing the staged entry. If you are unsure
whether a claim is supported by the source, mark it `[UNVERIFIED — DO NOT PROMOTE]` in
the staged entry rather than staging it as-is.

---

## 4. [ANTICIPATED] URL links to search page, not primary source

WebSearch returns a Google Scholar or PubMed search page as the top result. The staged
entry copies that URL rather than drilling to the paper's DOI or publisher page.

**Rule:** The URL field must resolve directly to the paper, report, or dataset — not to a
search results page, aggregator, or library proxy. If no direct URL exists, stage as
`URL: [PAYWALLED — DOI only: ...]` rather than substituting a search URL.

---

## 5. [ANTICIPATED] Secondary commentary staged as primary source

A consulting blog post or press release cites a Standish or CB Insights figure with
specific numbers. The scout stages the blog post as the finding rather than checking
whether the primary report is directly accessible.

**Rule:** If a result cites a primary source you already have in `base-rates.md`, it is
secondary commentary — discard it unless it contains new methodological critique.
Only stage primary reports, peer-reviewed papers, or official data releases.

---

## 6. [ANTICIPATED] Vendor-sponsored bias not flagged in Confidence field

A report is funded by the same company whose products it benchmarks (common in cloud,
SaaS adoption, and feature utilization studies). The scout stages it at High confidence
without disclosing the sponsor.

**Rule:** Any vendor-commissioned study defaults to Medium confidence at best. The
Confidence line must note "vendor-sponsored" and flag any self-selection in the
respondent pool. The 15% materiality threshold applies more strictly to vendor reports
than to independent or government data.

---

## 7. [ANTICIPATED] Out-of-rotation source search

The skill assigns source families by day of week. Running on a Thursday and searching
Friday's family because the day is "close" or because a headline looks interesting.

**Rule:** Only search the assigned day's source family. If a compelling off-rotation
headline appears, note it in the scout report under "Out-of-rotation signal — hold for
[day]" but do not search or stage it in the current run. Off-rotation sweeps are
explicitly named special runs, not default behavior.

---

## 8. [ANTICIPATED] PROMOTE mode edits base-rates.md before explicit per-finding confirmation

During a PROMOTE session with multiple staged entries, the scout writes the first
promotion to `base-rates.md` and then continues editing for subsequent entries without
waiting for explicit user confirmation on each one.

**Rule:** Each staged finding requires a separate explicit user decision before any edit.
Present one finding at a time. Never batch-write to `base-rates.md` even if the user
says "promote everything" — confirm each individually to catch cases where the user
changes their mind mid-session on wording.
