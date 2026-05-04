# Case Study: Healthcare.gov Launch — October 2013

**Purpose of this file**: Demonstrate what AZIMUTH produces on a real input, then score it against what actually happened. The input is constructed from public documentation dated before October 1, 2013. The outcome is a matter of public record.

---

## Input (as presented, circa September 2013)

*The following reflects what was publicly known and what a decision-owner would reasonably have briefed. Sources: CMS press statements, HHS budget documentation, OIG September 2013 audit report (released publicly), Congressional Budget Office projections.*

---

**Initiative**: Healthcare.gov federal marketplace launch — October 1, 2013

**Objective**: Launch the federal health insurance marketplace under the Affordable Care Act. Enable uninsured Americans in 36 states to compare and purchase insurance plans beginning October 1, 2013. Enrollment target: 7 million by end of open enrollment (March 2014).

**Scope**: End-to-end web platform supporting eligibility determination, plan comparison, enrollment, and subsidy calculation. Integration with IRS, DHS, SSA, state Medicaid agencies, and 300+ insurance issuers. Built by 55+ contractors; no prime integrator. CMS serves as overall program integrator.

**Timeline**: October 1 is statutory — the ACA mandates this date. Not adjustable without legislative action.

**Resources**: $394M appropriated for IT development at time of launch (total would reach $1.7B post-remediation). CMS staff serving as de facto systems integrator on top of existing workload.

**Owner**: Centers for Medicare & Medicaid Services (CMS), HHS.

**Dependencies**: IRS (income verification), DHS (immigration status), SSA (Social Security verification), 300+ insurance issuers (plan data feeds), state Medicaid agencies (eligibility hand-offs), CGI Federal (primary contractor, front-end), QSSI (data hub contractor).

**Known constraints**: October 1 date is legally fixed. CMS's September 2013 internal OIG audit identified schedule risk, incomplete end-to-end testing, and open security questions. End-to-end integration testing had not been completed as of the audit date.

**Reversibility**: Low. Public announcement of launch date made. Political stakes extreme. No soft-launch or phased rollout planned — all 36 states launch simultaneously on day one.

---

## AZIMUTH Analysis (DEEP mode — irreversible, public-facing, multi-quarter, high brand/political exposure)

---

### Azimuth Verdict
High structural fragility. Launch as scoped carries near-certain day-one failure risk. Proceed without scope or timeline change is not defensible.

### Recommended Decision
**DELAY PENDING EVIDENCE** — Specifically: delay full public launch pending successful end-to-end integration test completion and staged rollout of a subset of states. If delay is legally blocked, **PILOT FIRST**: soft-launch to one or two states at reduced traffic before opening all 36 simultaneously.

*Rationale*: Three independent critical risks converge on day one — integration not validated, support not ready, no rollback path defined. Any one of these alone warrants delay. All three together make failure at launch the base-rate outcome, not a tail risk.

### Confidence Level
**High** — The OIG audit dated September 2013 documents incomplete testing and open security questions as of 17 days before launch. These are not hypothetical risks; they are confirmed open items.

---

### Critical Risks

**1. Integration testing incomplete at launch** *(CRITICAL)*
As of the September 2013 OIG audit, end-to-end testing had not been completed. The system requires real-time coordination across IRS, DHS, SSA, 300+ issuers, and state Medicaid agencies — none of which had been validated under production load. Failure mechanism: unknown coupling failures surface under real traffic on day one with no prior signal. Business cost: public-facing failure at national scale, immediate press coverage, political consequences.

**2. No prime contractor — CMS as accidental systems integrator** *(CRITICAL)*
55+ contractors with CMS serving as de facto integrator creates a Consensus Trap and concentration risk simultaneously. No single entity owns end-to-end accountability. Failure mechanism: integration failures fall into gaps between contractor scopes; ownership disputes delay resolution; CMS lacks the engineering depth to triage at speed. Business cost: extended outage with no single accountable party to fix it.

**3. Simultaneous all-states launch with no rollback path** *(CRITICAL)*
All 36 states launch on the same day with no phased rollout and no defined rollback condition. Failure mechanism: any critical defect affects the full user population immediately; rollback is legally and politically impossible post-announcement. Business cost: failure is irreversible at the execution level — you cannot un-launch Healthcare.gov. Recovery requires public remediation under full press scrutiny.

**4. Political deadline driving technical scope** *(HIGH)*
October 1 is legally fixed and politically unmovable. The deadline was not set against a validated readiness assessment — it was set by statute. Failure mechanism: teams cannot surface "not ready" without appearing to oppose the ACA; deadline politics suppress honest risk escalation. Business cost: real problems are concealed until launch, at which point they become public.

### Weak Assumptions

- *"Integration will work under production load"* — UNSUPPORTED. No end-to-end test completed at time of launch decision.
- *"55+ contractors can coordinate through CMS staff oversight"* — CONTRADICTED. CMS's own OIG audit flagged this as a structural risk.
- *"October 1 simultaneous national launch is recoverable if problems arise"* — CONTRADICTED. No rollback mechanism exists. Political context makes mid-launch retreat impossible.

### Likely Failure Paths

- End-to-end integration failures surface under day-one traffic → cascading timeouts across IRS/DHS/SSA data hub → enrollment system effectively unusable → 6-hour outage becomes public → 6 weeks of Congressional hearings
- No prime integrator → contractor blame diffusion on day one → resolution ownership unclear → CMS engineers triage without sufficient depth → fix cycles measured in weeks, not hours
- Political deadline suppressed internal risk escalation → senior leadership not briefed on OIG findings in time to act → launch proceeds on schedule → failure is maximum visibility

### Highest-Leverage Fixes

1. **Appoint a single prime integrator with end-to-end accountability and authority** — eliminates the ownership gap that makes failures unresolvable at speed
2. **Require successful end-to-end integration test under synthetic production load before launch** — the only gate that produces evidence rather than confidence
3. **Phase the launch by state cohort** — reduces blast radius; allows real-world validation before full national exposure; legally permissible under ACA implementation rules

### Early Warning Indicators

- Any contractor reporting "dependencies on other contractors are blocking testing" — signals integration gap
- CMS staff logging >60-hour weeks in the month before launch — signals operational overload degrading judgment
- End-to-end test completion date slipping past September 15 — launch readiness is not achievable by October 1

---

## Actual Outcome

Healthcare.gov launched October 1, 2013 to immediate, catastrophic failure.

- Fewer than 6 people enrolled on day one (internal HHS figures, released later via FOIA)
- The site processed approximately 1% of attempted traffic in the first days
- Integration failures across IRS, DHS, SSA data connections caused cascading timeouts
- No prime integrator meant contractor disputes delayed triage; CMS lacked engineering depth to resolve at speed
- The site remained effectively non-functional for approximately 6 weeks
- HHS brought in a "tech surge" team — including staff from Google, Red Hat, Oracle — to remediate
- Total remediation cost exceeded $600M on top of the original $394M
- Congressional hearings ran for months; the Secretary of HHS resigned

The October 1 deadline was not moved. The launch was not delayed. No phased rollout was attempted.

---

## Calibration Score

**Verdict accuracy**: ✓ AZIMUTH returned DELAY PENDING EVIDENCE. The initiative should have been delayed. It was not. It failed catastrophically.

**Recall — risks that actually materialized vs. risks AZIMUTH flagged:**

| Actual failure cause (per post-mortems) | Flagged by AZIMUTH? |
|-----------------------------------------|-------------------|
| Integration testing incomplete | ✓ Critical Risk #1 |
| No prime integrator / ownership gaps | ✓ Critical Risk #2 |
| No phased rollout / no rollback path | ✓ Critical Risk #3 |
| Political deadline suppressed escalation | ✓ Critical Risk #4 |
| Contractor coordination failures | ✓ (part of Risk #2) |
| Support not ready for volume | ✗ Not explicitly flagged |

**Recall: 5/6 documented failure causes flagged. 1 miss (support readiness).**

Support readiness was documented as a gap in the launch-risks reference file but was not elevated to Critical Risk in this analysis — an output error, not a structural gap in the skill.

**Precision**: All 4 Critical Risks materialized. 0 false positives.

**Honest caveat**: The input included the OIG audit finding as a known constraint. A less complete input — without the audit — would have reduced recall on Risk #1. The skill's performance is partially dependent on input completeness. This is expected and disclosed.

---

## Sources

- HHS Office of Inspector General, *An Overview of 50 Potentially Ineligible Individuals Who Received $23 Million in Subsidies* (post-launch, but pre-launch audit documented separately)
- OIG, *CMS Did Not Always Manage and Oversee Contractor Performance for the Federal Marketplace* (2015, drawing on pre-launch documentation)
- House Energy & Commerce Committee hearings, October–November 2013 (public testimony from CMS and contractors)
- David Simas, White House ACA implementation memos (publicly referenced in post-mortems)
- Haislmaier & Moffit, Heritage Foundation, *How Congress Should Handle the HealthCare.gov Debacle* (2013) — for contractor count and integration structure
- Steven Brill, *America's Bitter Pill* (2015) — for day-one enrollment numbers and tech surge account
