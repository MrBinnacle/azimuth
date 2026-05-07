# Product Launch Azimuth Template

Use this template when:
- Plan involves a product launch, feature release, beta rollout, or public go-live
- Risk involves user-facing failures, communication timing, or support readiness
- Audience includes product managers, engineering leads, and marketing/communications owners

---

## Template

---

**PRODUCT LAUNCH AZIMUTH — [Product / Feature Name]**
*Launch Target: [Date] | Scope: [User segment / traffic] | Owner: [Name/Team]*

---

**VERDICT**
[One sentence. Is this launch ready, conditionally ready, or not ready?]

---

**LAUNCH OBJECTIVE**
[What specific outcome is this launch intended to produce? State the primary metric and the target. Not "ship the feature" — "acquire X users with Y retention at 30 days."]

---

**INCENTIVE ALIGNMENT SCAN**

Before readiness assessment, determine whether this launch date reflects technical readiness or external pressure.

| Actor | Their Incentive | Aligned with Launch Readiness? | Notes |
|-------|----------------|--------------------------------|-------|
| Launch sponsor / PM | [Delivery milestone / performance review / roadmap commitment] | ☐ Yes / ☐ No / ☐ Unknown | |
| Marketing / comms | [Pre-built campaign investment / press commitment] | ☐ Yes / ☐ No / ☐ Unknown | |
| Sales / revenue | [Pipeline dependent on launch date / quota pressure] | ☐ Yes / ☐ No / ☐ Unknown | |
| Investor / board | [Funding milestone / demo day / investor update tied to launch] | ☐ Yes / ☐ No / ☐ Unknown | |
| Engineering | [Ship pressure vs. quality signal] | ☐ Yes / ☐ No / ☐ Unknown | |

**Key questions:**
- Was the launch date set by technical readiness assessment or external commitment (board, press, campaign)?
- Has a public announcement, marketing campaign, or sales promise been made that makes delay politically costly?
- Who owns accountability if this launch fails — and is it the same person driving the date?
- Are launch success metrics defined by the team that benefits from a "shipped" outcome?

**Flag if:** launch date is externally committed before readiness is confirmed; marketing spend or sales pipeline is already dependent on the launch proceeding; accountability for failure is diffuse or absent.

If flagged: treat deadline politics as the primary failure risk, ahead of technical readiness. Escalate any ⚠ readiness gate to ✗ status for verdict purposes.

---

**MARKET TIMING AND EXTERNAL CONDITIONS**

| Condition | Assessment | Notes |
|-----------|------------|-------|
| Competitive: is a competitor launching something materially similar in this window? | ☐ Known clear / ☐ At risk / ☐ Unknown | |
| Regulatory / compliance: does this launch require review or clearance that is pending? | ☐ Clear / ☐ Pending / ☐ Unknown | |
| Platform dependency: is this launch dependent on a third-party platform change or API not under your control? | ☐ Stable / ☐ At risk / ☐ Unknown | |
| Market conditions: has the target market or user context materially changed since the launch was committed? | ☐ Stable / ☐ Changed / ☐ Unknown | |

**Any "Unknown" is an information gap, not a safe default.** For a public-facing launch, unknown competitive or regulatory timing must be flagged explicitly — not left blank.

---

**READINESS ASSESSMENT**

Rate each gate: ✓ READY | ⚠ PARTIAL | ✗ NOT READY

| Gate | Status | Notes |
|------|--------|-------|
| Feature functionally complete | | |
| Performance tested at launch spike | | |
| Security review complete | | |
| Legal / compliance reviewed | | |
| Support docs and training complete | | |
| Rollback procedure defined and tested | | |
| Launch metrics and alerts configured | | |
| Communication plan finalized and coordinated | | |
| On-call coverage confirmed for launch window | | |

**Any ✗ is a launch blocker. Any ⚠ requires a documented exception.**

---

**TOP 3 LAUNCH RISKS**

**1. [Risk Name]** — *Pre / During / Post launch*
[What is the risk. What triggers it. What the user impact is. What the business cost is.]
Mitigation: [Specific action, not "monitor closely."]

**2. [Risk Name]**
[Description.]
Mitigation: [Action.]

**3. [Risk Name]**
[Description.]
Mitigation: [Action.]

---

**ROLLBACK CONDITION AND PROCEDURE**

**Rollback trigger**: [Specific metric, error rate, or behavior threshold — e.g., "If error rate exceeds 2% within 1 hour of launch..."]

**Rollback procedure**: [Step-by-step. Who does what. In what order.]

**Estimated rollback time**: [How long from trigger to full rollback]

**Data or state impact of rollback**: [What user data or actions, if any, are affected]

**Rollback tested?**: [Yes / No — if No, this is a launch blocker]

---

**LAUNCH METRICS**

| Metric | Baseline | Watch Threshold | Respond Threshold | Rollback Threshold |
|--------|----------|-----------------|-------------------|--------------------|
| [metric] | | | | |
| [metric] | | | | |
| [metric] | | | | |

**Segments monitored** (not just aggregate):
- [ ] Platform (iOS / Android / Web)
- [ ] Geography
- [ ] User cohort / account tier
- [ ] New vs. returning users

---

**COMMUNICATION COORDINATION**

| Communication | Owner | Scheduled | Dependent on |
|---------------|-------|-----------|--------------|
| Press/blog | | | Deployment confirmed live |
| Email campaign | | | Feature confirmed functional |
| In-app messaging | | | A/B test complete |
| Internal announcement | | | External launch |
| Social posts | | | Press release |

**Single launch timeline shared between engineering and marketing?** [Yes / No]

---

**RECOMMENDED DECISION**

☐ PROCEED — All gates cleared; launch ready
☐ PROCEED WITH SAFEGUARDS — Partial gates; documented exceptions accepted
☐ SOFT LAUNCH — Limited rollout to [segment] before full launch
☐ DELAY — [Specific gate or risk requiring resolution; estimated date]
☐ CANCEL — [Rationale]

**Must-resolve before launch:**
1. [item] — Owner: [name] — By: [date]
2. [item]

---

**CONFIDENCE LEVEL**: [Low / Medium / High]
**Basis**: [Readiness gate completion rate, rollback test status, load test results]
