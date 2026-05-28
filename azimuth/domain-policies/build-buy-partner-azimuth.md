# Build vs. Buy vs. Partner Azimuth Template

This file configures runtime presentation for build/buy/partner decisions. Decision authority lives in `BEHAVIOR_SPEC.md`. This file does not define rules.

Use this template when:
- The decision is which path to take to acquire a capability, not whether to acquire it
- Genuine multi-option evaluation is needed — all three paths are being considered
- Audience includes strategy, product, engineering leadership, or the executive making the path decision

**Scope:** This template handles path selection only. After a path is recommended, load the appropriate domain template for execution analysis: `domain-policies/codebase-azimuth.md` (Build) or `domain-policies/partnership-azimuth.md` (Buy or Partner). The Carry Forward section at the end of this output transfers context to the domain template — use it.

**Anchoring flag:** If the user arrives already committed to one path ("we're thinking of building X"), this template forces comparative analysis regardless. Single-path analysis belongs in the domain template; if the path choice is not genuinely open, route there directly.

---

## Template

---

**BUILD VS. BUY VS. PARTNER AZIMUTH — [Capability or Domain Name]**
*Capability gap: [What is missing] | Decision authority: [Who decides] | Timeline pressure: [When capability is needed]*

---

**VERDICT**
`RECOMMENDED PATH: [BUILD / BUY / PARTNER / NONE] — [standard verdict]`
[One sentence rationale. The path recommendation and the execution verdict are both required.]

---

**CAPABILITY OBJECTIVE**

[What specific capability gap does this decision address? State in outcome terms — not "we need a data platform" but "we need to reduce data ingestion latency for [use case] to under [threshold] by [date]."]

Also state:
- Why this capability is needed now rather than later
- What the cost of not acquiring this capability is, in concrete terms

If the capability gap is undefined or the urgency is stated without evidence: flag as primary risk before proceeding.

---

**ANCHORING ASSESSMENT**

Before analysis, determine whether genuine multi-option evaluation is possible.

| Signal | Present? | Notes |
|--------|----------|-------|
| A specific path was proposed before this analysis was requested | ☐ Yes / ☐ No | If Yes: name the path and the proposer |
| The proposer of the path is the same person who benefits most from that path | ☐ Yes / ☐ No / ☐ Unknown | |
| Concerns about the proposed path were raised and dismissed or minimized | ☐ Yes / ☐ No / ☐ Unknown | |
| Budget, timeline, or org decisions have already been made that assume one path | ☐ Yes / ☐ No | |

**If any signal is Yes:** comparative analysis across all three paths is required regardless of the user's stated preference. Anchoring on one path is the highest-probability failure mode for this decision type — Module 4 will surface whose incentive drives it. (domain-specific gate: comparative analysis is mandatory under build-buy-partner domain when anchoring signals observed)

**If all signals are No:** genuine multi-option evaluation is in play. Proceed.

---

**INCENTIVE ALIGNMENT SCAN**

Module 4 runs once for the path-selection decision. Advocate identity is the highest-signal input — it determines whether path selection is driven by organizational merit or proposer incentive.

| Actor | Advocated Path | Their Incentive | Incentive Tied to Path Merit? | Notes |
|-------|---------------|----------------|-------------------------------|-------|
| Path proposer (who initiated this decision) | | [Career / budget / team growth / deal activity / relationship building] | ☐ Yes / ☐ No / ☐ Unknown | |
| Engineering / CTO | Build | [Team growth / technical ambition / headcount expansion / interesting work] | ☐ Yes / ☐ No / ☐ Unknown | |
| Corp dev / M&A | Buy | [Deal activity / transaction experience / company growth narrative / promotion] | ☐ Yes / ☐ No / ☐ Unknown | |
| BD / Partnerships | Partner | [Alliance building / relationship portfolio / partnership function justification] | ☐ Yes / ☐ No / ☐ Unknown | |
| Finance | [Path with lowest capital outlay or preferred capex/opex treatment] | [Budget constraints / capital allocation targets] | ☐ Yes / ☐ No / ☐ Unknown | |
| Board / investors | [Path aligned with portfolio narrative or comparable company benchmarks] | [Narrative consistency / valuation optics] | ☐ Yes / ☐ No / ☐ Unknown | |

**Structured questions (run before analysis):**

1. **[IDENTITY]** Who first proposed this path decision — and are they the advocate for one specific path?
2. **[ACCOUNTABILITY]** If the chosen path fails to deliver the capability, what happens to the person who recommended it?
3. **[BENEFIT]** Who gains most if Build wins? If Buy wins? If Partner wins? What specifically do they gain?
4. **[DISSENT]** Have concerns about any path been raised and dismissed? By whom, and on what grounds?
5. **[EXTERNAL]** Is there a vendor, investor, or board pressure creating momentum toward one path regardless of outcome?
6. **[SUNK COST]** Has budget been allocated, a term sheet negotiated, or a team commitment made that makes changing paths costly?
7. **[MEASUREMENT]** Are the success metrics for the chosen path defined by the same person who advocated for it?

**Response tiering (same as core Module 4):**
- GREEN — all 7 answered: full analysis, no confidence impact
- YELLOW — 5–6 answered AND Question 1 [IDENTITY] answered: analysis proceeds, confidence reduced one tier
- RED — Question 1 skipped OR fewer than 5 answered: confidence locked at LOW; PROCEED and PROCEED WITH SAFEGUARDS unavailable for path recommendation (restates RULE-6.3/6.4 for the path-recommendation context within build-buy-partner domain)

**Anchoring enforcement:** If Module 4 returns YELLOW or RED on [IDENTITY] or [DISSENT], comparative analysis across all three paths is mandatory — regardless of whether the user has indicated a preferred path. A YELLOW or RED tier on these questions means the path selection may be driven by proposer incentive, not capability merit.

---

**PATH VIABILITY GATES**

Run each gate. A path that fails its gate is removed from comparative analysis.

### Build Gate

| Criterion | Assessment | Notes |
|-----------|------------|-------|
| The team has the skills to build this capability to production quality | ☐ Yes / ☐ No / ☐ Partial | |
| This capability is a source of competitive differentiation that justifies building vs. buying a commodity solution | ☐ Yes / ☐ No | |
| Timeline to build is consistent with competitive need | ☐ Yes / ☐ No | |
| Opportunity cost is acceptable — what does NOT get built if this is prioritized? | ☐ Acceptable / ☐ High / ☐ Unknown | |

**Build gate fails if:** capability is not differentiating AND a commodity solution exists at acceptable cost. Building a commodity is a deliberate choice that requires explicit justification. (activates RULE-4.7 REJECT for the named path-option within build-buy-partner domain)

### Buy Gate

| Criterion | Assessment | Notes |
|-----------|------------|-------|
| Acquirable targets exist at a price within decision authority | ☐ Yes / ☐ No / ☐ Unknown | |
| A credible integration plan can be defined before commitment | ☐ Yes / ☐ No | |
| The deal thesis beyond "we needed the capability" is defined | ☐ Yes / ☐ No | |
| Key talent retention through integration has been considered | ☐ Yes / ☐ No | |

**Buy gate fails if:** no acquirable targets exist at a defensible price, or no credible integration plan can be defined. Price availability without integration credibility is not a valid Buy path. (activates RULE-4.7 REJECT for the named path-option within build-buy-partner domain)

### Partner Gate

| Criterion | Assessment | Notes |
|-----------|------------|-------|
| Viable partners with structurally aligned incentives exist | ☐ Yes / ☐ No / ☐ Unknown | |
| Switching cost if the partnership ends is acceptable | ☐ Low / ☐ Manageable / ☐ High | |
| IP, data, and brand ownership is clear and contractually protectable | ☐ Yes / ☐ No / ☐ Unknown | |
| Dependency asymmetry is acceptable — could the partner exit more easily than we could? | ☐ Symmetric / ☐ Asymmetric / ☐ Unknown | |

**Partner gate fails if:** no viable partners with aligned incentives exist, or switching cost is High with no defined exit mechanism. A partner relationship with high exit cost and misaligned incentives is acquisition risk without acquisition control. (activates RULE-4.7 REJECT for the named path-option within build-buy-partner domain)

**Paths remaining after gates:** [Build / Buy / Partner / None]

If all three gates fail: return INSUFFICIENT SIGNAL — no viable path exists within current constraints.

---

**COMPARATIVE ANALYSIS**

Complete only for paths that passed their gate.

| Dimension | Build | Buy | Partner |
|-----------|-------|-----|---------|
| Time to capability | | | |
| Total capital cost (Year 1 + Year 3) | | | |
| Reversibility if it fails | | | |
| Competitive differentiation created | | | |
| Primary execution risk | | | |
| Dependency created | | | |
| Incentive alignment of primary advocate | | | |

**Dominant constraint:** Which dimension most limits the available options given current context? [Time / Capital / Capability / Risk tolerance]

---

**PATH RECOMMENDATION**

Based on gates and comparative analysis:

`RECOMMENDED PATH: [BUILD / BUY / PARTNER / NONE]`

☐ PROCEED — path is viable; gates cleared; proceed to domain template
☐ PROCEED WITH SAFEGUARDS — path is viable with specific conditions (listed below)
☐ PILOT FIRST — validate [specific assumption about the chosen path] before committing
☐ DELAY PENDING EVIDENCE — [specific gate or comparative data needed before path can be selected]
☐ REJECT — no viable path; constraints make all three paths unacceptable at this time
☐ INSUFFICIENT SIGNAL — all gates failed or input too sparse to ground a path recommendation

**Rationale:** [Two to three sentences. Name the dominant constraint, the primary reason this path wins over the alternatives, and the highest-risk assumption that could reverse the recommendation.]

**Required before committing to path:**
1. [action] — Owner: [name] — By: [date]
2. [action]

---

**CONFIDENCE LEVEL**: [Low / Medium / High]
**Basis**: [Module 4 tier, gate completion, comparative data quality, anchoring assessment]

---

## Carry Forward

*(Include this block in the next session prompt when loading `domain-policies/codebase-azimuth.md` or `domain-policies/partnership-azimuth.md`. SKILL.md Bypass Handling will ingest it and skip Module 4 re-interview if GREEN.)*

```
AZIMUTH CARRY FORWARD — Build/Buy/Partner path selection complete

Path selected: [BUILD / BUY / PARTNER]
Module 4 tier: [GREEN / YELLOW / RED]
Proposer identity: [name/role — or DECLINED if Question 1 was skipped]
Path verdict: [RECOMMENDED PATH — standard verdict]
Top unresolved assumption: [the assumption most likely to reverse the recommendation if wrong]
Capability objective: [one sentence — the capability gap this decision addresses]

Next template: [domain-policies/codebase-azimuth.md / domain-policies/partnership-azimuth.md]
```
