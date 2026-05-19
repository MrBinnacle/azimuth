# Startup / Early-Stage Azimuth Template

Use this template when:
- Evaluating whether to launch, fund, or commit significant resources to an early-stage initiative or startup
- Decision point: pre-commitment — before writing the check, signing the term sheet, or making a go/no-go on launch
- Audience: founders, early investors, or board members evaluating the plan

This template applies when PMF has not been validated at scale, runway is a binding constraint, and co-founder structure is still forming or recently settled.

---

## Template

---

**STARTUP AZIMUTH — [Company / Initiative Name]**
*Stage: [Idea / Pre-seed / Seed / Series A] | Sector: [Domain] | Decision: [Fund / Launch / Commit]*

---

**VERDICT**
[One sentence. What is the commitment decision and the single dominant basis?]

**RECOMMENDED DECISION**

☐ PROCEED — PMF evidence strong, runway adequate, co-founder structure sound
☐ PROCEED WITH SAFEGUARDS — Proceed with specific structural requirements listed below
☐ PILOT FIRST — Validate [specific assumption] at limited commitment before full resource deployment
☐ REDUCE SCOPE — Current scope exceeds what runway and team can execute; define a smaller initial bet
☐ DELAY PENDING EVIDENCE — [Named evidence] not yet available; decision premature
☐ REJECT — [Specific structural reason]

---

## Section 1 — PMF Validation Gate

*Run before committing capital or resources. If PMF evidence is absent, confidence ceiling is LOW and PROCEED and PROCEED WITH SAFEGUARDS verdicts are unavailable.*

Product-market fit is validated by behavior, not by stated intent. Surveys, interest lists, and pilot LOIs without payment or repeat usage are not PMF evidence.

| Evidence Type | Status | Source / Details |
|---------------|--------|-----------------|
| Users pay or have paid (not "would pay") | ☐ Yes / ☐ No / ☐ Unknown | |
| Retention: users return without prompting | ☐ Yes / ☐ No / ☐ Unknown | |
| Pull behavior: users refer others without incentive | ☐ Yes / ☐ No / ☐ Unknown | |
| Problem validated via paying-customer interviews, not surveys | ☐ Yes / ☐ No / ☐ Unknown | |
| Revenue or executed LOI from non-friends/family | ☐ Yes / ☐ No / ☐ Unknown | |

**PMF signal**: ☐ Validated (3+ YES with behavioral evidence) | ☐ Early signal (1–2 YES) | ☐ Absent (0 YES or survey/intent-only)

*If Absent or Early signal: state PMF status explicitly in verdict. If Absent: flag for PILOT FIRST or DELAY PENDING EVIDENCE.*

---

## Section 2 — Runway Scenario Table

*Populate all three scenarios before proceeding. If the pessimistic scenario crosses the 6-month floor, flag it before the verdict.*

| Scenario | Revenue assumption | Burn assumption | Runway |
|----------|-------------------|-----------------|--------|
| Base | As modeled | As modeled | [months] |
| Optimistic | +40% vs. base | As modeled | [months] |
| Pessimistic | −40% vs. base | +20% vs. base | [months] |

**Runway floor**: ☐ Pessimistic ≥ 12 months | ☐ 6–12 months (flag) | ☐ < 6 months (block — REDUCE SCOPE or REJECT unless financing close is imminent and committed)

**What drives the pessimistic case**: [Name the 1–2 specific assumptions most likely to miss — not generic "revenue may be lower than expected"]

**Next financing trigger**: [At what cash balance or date must the team begin a financing process, and is that trigger built into the model?]

---

## Section 3 — Co-Founder Structure Check

*Skip if single founder with no co-founders. If co-founders are present, all items must be resolved before a PROCEED verdict is available. Any PENDING or NOT ADDRESSED item blocks PROCEED.*

Co-founder collapse is a structurally preventable failure mode. Verbal agreements do not hold under the stress of adversity, dilution events, or departure decisions.

| Structural Element | Status | Notes |
|-------------------|--------|-------|
| Equity split formalized in writing (not verbal) | ☐ Done / ☐ Pending / ☐ Not addressed | |
| Vesting schedule documented with cliff | ☐ Done / ☐ Pending / ☐ Not addressed | |
| Decision authority defined for tie or deadlock | ☐ Done / ☐ Pending / ☐ Not addressed | |
| Buyout or separation mechanism documented | ☐ Done / ☐ Pending / ☐ Not addressed | |
| IP assignment executed | ☐ Done / ☐ Pending / ☐ Not addressed | |

**Any PENDING or NOT ADDRESSED: PROCEED verdict is unavailable.** Require completion before commitment.

---

## Section 4 — Distribution Architecture

*If the primary acquisition channel cannot be named, or if no one on the team owns it, flag as a structural risk — not a planning gap to resolve after launch.*

| Element | Assessment |
|---------|------------|
| Primary customer acquisition channel | [Named — not "multiple channels" or "TBD"] |
| Evidence this channel works for this product and audience | |
| CAC estimate and basis | |
| LTV estimate and basis | |
| CAC/LTV ratio and what it implies for unit economics | |
| Person on team who owns distribution execution | [Named individual — not "the team"] |

**Distribution absent**: If the primary channel cannot be named or has no named owner, treat as a critical risk in the failure path register.

---

## Section 5 — Customer Concentration Check

*Complete if the business has early customers or revenue. Skip if pre-revenue with no committed customers.*

| Check | Finding |
|-------|---------|
| Largest customer as % of total revenue | |
| If that customer churns, runway impact | |
| Does the product roadmap disproportionately serve one customer's requirements? | |
| Are any customers also investors? | |

**Concentration flag** — fires if any of the following are true:
- First or largest customer > 40% of revenue
- Roadmap is materially driven by one customer's feature requests
- A customer-investor is both the primary revenue source and a board or governance participant

*If flagged: treat as a critical dependency risk in the failure path register. Revenue concentration collapses runway non-linearly if the concentrated customer churns.*

---

## Section 6 — Failure Path Register

Construct the three most plausible failure chains for this specific initiative. Each chain must be anchored in findings from Sections 1–5 — not generic startup failure modes. Common chain origins: premature scaling, founder-market mismatch, solution looking for a problem, runway miscalculation, co-founder collapse, market timing failure, first customer trap, distribution absent. Pattern details and observable signals in `references/startup-failures.md`.

Use: Trigger → Cascade → Visible Failure → Business Cost

**1.**

**2.**

**3.**

---

**CONFIDENCE**: [Low / Medium / High] — [Primary basis: PMF evidence quality, runway pessimistic floor, co-founder structure status]
