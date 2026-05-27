# PE Secondaries IC Azimuth Template

This file configures runtime presentation for PE secondaries IC decisions. Decision authority lives in `BEHAVIOR_SPEC.md`. This file does not define rules.

Use this template when:
- A secondaries fund IC is evaluating whether to commit capital to a transaction
- Transaction type: GP-led continuation vehicle, direct secondary (LP stake), or minority recap / structured liquidity
- Decision point: pre-commitment — before submitting a bid, signing a term sheet, or approving a price

This template is for the IC investment partner role, not the fund CFO. The CFO
supports this decision with financial data but does not own the verdict.

---

## Template

---

**SECONDARIES IC AZIMUTH — [Asset / Fund Name]**
*Transaction type: [GP-Led CV / Direct Secondary / Minority Recap] | Stage: [Screening / Preliminary IC / Final IC] | Deal lead: [Name]*

---

**VERDICT**
[One sentence. Commit, bid below, counter, condition, or pass — and the single dominant reason.]

**RECOMMENDED DECISION**

☐ COMMIT-AT-PRICE — proceed at stated terms; returns are achievable and process is clean
☐ BID-BELOW-INDICATED — submit bid at [X]% of NAV; GP has no obligation to engage *(GP-led auction context)*
☐ COUNTER-AT-PRICE — propose [X]% of NAV as a bilateral negotiation *(direct secondary / minority recap)*
☐ CONDITIONAL-ON-TERMS — commit at stated price contingent on: [governance / information rights / key person / other structural term]
☐ PASS-PROCESS — decline regardless of asset quality or pricing; process integrity is insufficient *(see Process Gate below — this verdict does not reopen on price reduction)*
☐ PASS-PRICING — pass; required returns not achievable at current ask

---

## Section 1 — Selection Signal Screen

*Run this before committing diligence resources. Screen for both adverse and positive selection — the signal can run in either direction.*

**Why is this asset in a continuation vehicle / available as a secondary?**

| Question | Finding |
|----------|---------|
| What is the GP's stated reason for the transaction? | |
| What is the most plausible unstated reason? | |
| Does the stated reason survive if LP roll rate is below 60%? | |
| Is this a motivated sale, a liquidity solution, or a genuine opportunity extension? | |
| Has the asset underperformed the GP's prior marks? (Check: were marks revised down in the 6 months before transaction announcement?) | |
| Has this GP used CVs previously, and how did those transactions perform for secondaries buyers? | |

**Adverse selection signals** (any one warrants escalation):
- Marks revised downward in the 6–12 months before CV announcement
- LP roll rate below 30% without a clear structural explanation
- GP's stated reason does not survive if the asset were performing at plan
- Prior GP-led CVs delivered below-hurdle returns for buyers
- Transaction announced shortly after a failed sale process

**Positive selection signals** (these do not eliminate diligence — they contextualize):
- Performing asset with documented value-creation path requiring additional hold
- High LP roll rate (>60%) at full information, not manufactured through information asymmetry
- GP co-investing new cash (not rolled carry) at ≥10% of CV
- Competitive process with independent fairness opinion from a non-conflicted advisor
- GP track record on comparable assets showing realized DPI, not mark-to-model

**Selection signal assessment**: ☐ Positive selection dominant  |  ☐ Mixed — requires scrutiny  |  ☐ Adverse selection dominant — escalate before proceeding to pricing

*If adverse selection dominant: document and escalate. Do not proceed to pricing until resolved.* (activates RULE-4.6 DELAY PENDING EVIDENCE; pricing analysis is blocked until evidence resolution)

---

## Section 2 — Process Integrity Gate *(GP-led CV only)*

*This is a kill gate independent of asset quality. A PASS-PROCESS verdict does not reopen if the GP reduces price.*

ILPA 2023 Continuation Funds Guidance minimum standards. Note: the SEC's Private
Fund Adviser Rules (including the Adviser-Led Secondary Rule, Rule 211(h)(2)-2) were
vacated by the Fifth Circuit in June 2024. Process compliance is now contractual
(LPA terms, LPAC consent) and reputational — not regulatory. ILPA standards are the
operative market benchmark, not a regulatory floor.

- LPAC received materials and had ≥10 business days before signing the acquisition agreement
- LPs received ≥20 business days / 30 calendar days for the election period
- Information provided to secondaries buyer is equivalent to information provided to existing LPs
- Fairness opinion obtained from an independent provider (not GP's primary banker)
- Non-electing LPs must be left no worse off than had the transaction not taken place
- Status quo option preserved: LPs can remain in original fund on existing terms

| Standard | Met / Not Met / Unknown |
|----------|------------------------|
| LPAC notice period ≥10 business days before signing | |
| LP election period ≥20 business days / 30 calendar days | |
| Information parity between buyer and existing LPs | |
| Independent fairness opinion (independent of GP's primary banking relationship) | |
| LPAC conflict disclosures complete | |
| GP conflict of interest disclosed in writing to LPAC and electing LPs | |
| Non-electing LP status quo preserved on existing terms | |

**Process integrity status**: ☐ Clean  |  ☐ Deficient — specify:

*Note: A buyer who commits into a deficient process participates in a transaction
exposed to entire fairness scrutiny under Delaware law. (ADIC v. EMG, C.A. No.
2025-1389-NAC, Del. Ch., filed December 2025 — emergency injunction granted;
underlying matter pending as of May 2026.) Process deficiency is not cured by
price reduction. If "Deficient": verdict is PASS-PROCESS, stop.* (PASS-PROCESS is a domain-specific label for RULE-4.6 DELAY PENDING EVIDENCE with process-integrity evidence requirement; non-standard verdict label flagged [AMBIGUOUS-EXTRACTED] in BEHAVIOR_SPEC.md RULE-8.17)

---

## Section 3 — NAV Reliability Assessment

*GP marks in continuation vehicle contexts are systematically optimistic. This is a
structural constraint, not a diligence gap. Price every transaction against an
independent view of value, not the GP mark. In 2024 H1, 56% of SACVs priced at or
above NAV — pricing converges to the GP mark; diligence interrogates the mark's
reliability, not the spread to it. The goal is not to apply a fixed discount to NAV
but to validate NAV quality: QoE tie-out, banker references, and transaction comps
reconciled to within ≤0.5x EBITDA tolerance.*

| Question | Finding |
|----------|---------|
| Date of last GP mark / days since last mark | |
| When was the last independent valuation? (IPEV / ASC 820 standard) | |
| Has the GP revised marks upward in the 6–12 months prior to CV announcement? | |
| What is the delta between GP mark and independent appraiser's view, if available? | |
| What adjustment to NAV does the deal team apply before pricing? | |
| What is the basis for the exit multiple assumption? Stress case? | |
| What hold period assumption underlies the IRR model? Stress case? | |

**NAV reliability**: ☐ Independently verified  |  ☐ GP-asserted, no independent check  |  ☐ GP-asserted with known upward revision history

*Industry analysis (Dawson Partners, formerly Whitehorse Liquidity Partners, reported
in Institutional Investor) found assets entering CVs marked approximately 28% higher
than GP valuations six months prior across 1,000+ transactions. Treat as a directional
signal, not a calibrated multiplier — the methodology is proprietary and undisclosed.
Validate NAV quality through QoE, banker references, and transaction comp benchmarking
rather than applying a fixed discount percentage.*

---

## Section 4 — Asset Quality Assessment

| Question | Finding |
|----------|---------|
| What is the investment thesis for the underlying asset? | |
| Is the thesis still intact relative to the original fund investment rationale? | |
| What has changed materially since the GP's original investment? | |
| What does management quality assessment reveal that the information package supports? | |
| What does the GP's track record look like on comparable assets, separated from selection effects? | |
| What are the two most likely exit paths and their timeline? | |
| What does the stress case look like on hold period (+2 years) and exit multiple (−1.0x)? | |

---

## Section 5 — GP Quality and Alignment

| Signal | Finding | Reliable / Table Stakes / Unreliable |
|--------|---------|--------------------------------------|
| Carry roll | | Table stakes at par NAV — does not discriminate |
| GP equity commitment (new cash, not rolled economics) | | Reliable if ≥10% of CV at new money (observed range 5–25%; median 10–15% in 2024) |
| LP reference calls — what did LPs say? | | Structurally compromised: LPs withhold negatives to preserve GP access |
| GP's stated exit conviction vs. prior exit record on comparable assets | | |
| Management team continuity and succession | | |

**Relationship bias check**: Does this firm have a primary fund relationship with
the GP that could distort IC approval? If yes, name it and name who at IC is
conflicted. An IC that approves a CV primarily to preserve a GP relationship, not
because the asset is compelling, is a documented secondaries failure mode.

☐ No primary relationship conflict  |  ☐ Relationship exists — named IC member(s): [name] — conflict disclosed to IC?

---

## Section 5a — Incentive Alignment Scan

Before pricing analysis, assess whether the decision to proceed is driven by asset quality or by structural incentives.

| Actor | Their Incentive | Aligned with Asset Quality? | Notes |
|-------|----------------|----------------------------|-------|
| IC deal lead | [Fee income / deal count / relationships / fund deployment pressure] | ☐ Yes / ☐ No / ☐ Unknown | |
| GP (CV seller) | [Liquidity for prior fund LPs / continuation of management fees / NAV support] | ☐ Yes / ☐ No / ☐ Unknown | |
| Placement agent / advisor | [Transaction fee contingent on close] | ☐ Yes / ☐ No / ☐ Unknown | |
| Existing LP references | [Preserve GP relationship / avoid being seen as difficult] | Structurally compromised — see Section 5 | |

**Key questions:**
- Does this firm have a primary fund relationship with the GP that creates pressure to commit independent of asset quality? (Named above — if yes, this is a GOVERNANCE RISK.)
- Is the IC member evaluating this transaction the same person who sourced it or who manages the GP relationship?
- Is deployment pressure (uninvested capital, fund timeline) influencing the threshold for commitment?

**Flag if:** primary relationship conflict exists and is not explicitly disclosed to IC; deal lead sourced the transaction and owns the approval recommendation; fund deployment pressure is named as a rationale for proceeding.

If flagged: treat relationship bias as the primary incentive risk and require an independent IC voice with no GP relationship to co-sign the verdict. (parameterizes M4 governance-conflict handling for PE-secondaries domain; activates RULE-4.6 DELAY PENDING EVIDENCE when independent IC voice not obtainable)

---

## Section 6 — Pricing Discipline

**Required return hurdles** (apply your fund's actual thresholds):

| Transaction type | Minimum MOIC | Minimum IRR |
|-----------------|-------------|------------|
| Single-asset CV | ≥2.0x | ≥20% |
| Multi-asset CV | ≥1.8–2.0x | ≥17.5–20% |
| Direct secondary (LP stake) | [fund threshold] | [fund threshold] |
| Minority recap | [fund threshold] | [fund threshold] |

**Pricing derivation** — rigorous buyers derive the discount from required return
working backward, not from negotiating off the GP mark:

| Input | Base case | Stress case |
|-------|-----------|-------------|
| Entry price (% of NAV) | | |
| Independent NAV estimate (if different from GP mark) | | |
| Exit multiple assumption | | |
| Hold period assumption | | |
| Modeled MOIC | | |
| Modeled IRR | | |
| IRR at stress (hold +2 years, exit −1.0x) | | |

**Does the deal achieve required return hurdles in the stress case?**
☐ Yes  |  ☐ No — PASS-PRICING unless price changes (PASS-PRICING is a domain-specific label for RULE-4.6 DELAY PENDING EVIDENCE with pricing-evidence requirement; flagged [AMBIGUOUS-EXTRACTED])

**Staple financing terms** *(if applicable)*: Are terms arm's-length or GP-favorable?
[Note: staple financing terms are an SEC examination focus since 2020.]

---

## Section 7 — Failure Path Register

Construct the three most plausible failure chains for this specific transaction.
Use: Trigger → Cascade → Visible Failure → Fund Cost

**1.**

**2.**

**3.**

*Do not list generic secondaries risks. Each chain must be specific to this asset,
this GP, and this transaction structure.*

---

## Section 8 — Must-Resolve Before IC Approval

| Item | Owner | Required by |
|------|-------|------------|
| | | |
| | | |

---

## Verdict (restate)

**RECOMMENDED DECISION**: [one of six categories above]

**Primary basis**: [one sentence — the single finding that most drives the verdict]

**If PASS-PROCESS**: Document the specific deficiency. This verdict does not reopen.

**If BID-BELOW-INDICATED or COUNTER-AT-PRICE**: State the price in % of NAV and
the return model that supports it.

**If CONDITIONAL-ON-TERMS**: State the specific terms required and the walk-away
condition if they are not obtained.

**Confidence**: [Low / Medium / High] — [one reason: NAV reliability, diligence depth, GP conviction quality, process integrity]

---

*Verdict taxonomy validated against PE secondaries IC practice by AZIMUTH research
scouts, May 2026. ILPA Continuation Funds Guidance (2023). PASS-PROCESS exposure
basis: ADIC v. EMG, C.A. No. 2025-1389-NAC (Del. Ch., filed December 2025 —
emergency injunction granted; matter pending as of May 2026). NAV divergence
reference: Dawson Partners (formerly Whitehorse Liquidity Partners), reported in
Institutional Investor; 1,000+ transactions, methodology proprietary — treat as
directional. Performance context: median continuation fund MOIC 1.4x (Morgan Stanley,
2018–2023 vintages); top-quartile buyers target ≥2.0x/≥20% IRR.*
