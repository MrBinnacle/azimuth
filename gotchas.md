# Gotchas

In DEEP mode, this file loads unconditionally. In STANDARD mode, load only when a trigger fires (Module 4 RED tier or governance-level incentive conflict; OR Module 6 chains all match canonical patterns requiring availability inversion). Do not apply patterns absent a fired trigger, even if this file is visible in context.

These are 8 failure patterns that consistently evade standard risk checklists. They are not dramatic; they are structural and predictable in hindsight. They are intentionally distinct from the failure modes covered in `references/software-failure-patterns.md`, `references/launch-risks.md`, and the diagnostic files — those references cover failure modes that are technical or domain-specific. The patterns below are organizational, behavioral, or temporal failure modes that recur across domains.

---

## 1. The Second System Effect

When replacing or rebuilding something that works, teams routinely overload the new version with accumulated feature wishes. The rewrite that was supposed to be "cleaner" ships late, overbuilt, and harder to maintain than the original.

**Signal**: Plan includes phrases like "and while we're at it…" or "we'll finally fix…"

**Check**: Is scope tightly bounded to what the original did, plus a defined delta? Or is the migration a wish list in disguise?

---

## 2. Approval Chains as Infinite Loop

Plans that require sign-off from multiple layers underestimate cycle time almost universally. One missing stakeholder, one unexpected objection, one round of revisions, and a 2-week approval window becomes 6 weeks.

**Signal**: Plan says "pending approval" or "subject to legal/compliance/exec review" without lead times built into the schedule.

**Check**: What is the realistic approval chain? Has anyone pressure-tested cycle time with those stakeholders recently?

---

## 3. Commitment Escalation

Once enough sunk cost accumulates — time spent, money spent, reputation staked — the willingness to stop or change course collapses. Teams continue executing a failing plan because stopping feels worse than continuing, even when the evidence clearly favors stopping.

**Signal**: User describes the initiative as already underway, already communicated externally, or carrying prior investment.

**Check**: Is the decision being made based on future value, or is past investment distorting judgment? Would this plan be approved fresh today with the current evidence?

---

## 4. The Consensus Trap

Plans that require no one to make a hard call — where every stakeholder must agree — functionally have no decision-maker. Consensus-required governance drifts, stalls on edge cases, and produces watered-down outcomes that satisfy no one's original intent.

**Signal**: Governance language like "cross-functional alignment," "everyone must agree," "no unilateral decisions."

**Check**: Who can break a tie? Who has final authority? If everyone has veto power, the plan has no owner.

---

## 5. The Last-Mile Gap

A plan can be technically complete and still fail at handoff: training not done, documentation missing, the receiving team not ready, rollout communication unclear. The last 10% of execution — the part that faces real users or live systems — is systematically underinvested.

**Signal**: Plan has detailed build phase, sparse rollout phase, and no user readiness section.

**Check**: What happens the day after go-live? Who handles first-wave issues? Is that path defined?

---

## 6. Metric Drift

The success metric is defined at plan inception. By the time the initiative concludes, the goalposts have shifted — the business context changed, stakeholder priorities shifted, the original metric no longer reflects what anyone actually cares about. The work gets done; the outcome isn't valued.

**Signal**: Plan is longer than 90 days with no metric checkpoint cadence.

**Check**: Are success metrics locked and dated? Is there a mid-point validation where the metric is reconfirmed against current business reality?

---

## 7. The Plan-Revision Gap

Surfacing a risk is not the same as acting on it. Teams that run structured failure analysis consistently identify failure reasons and generate mitigations — and then fail to revise the plan when remediation would require reducing scope. The output of the analysis lands; the plan does not change.

**Signal**: Analysis produced a clear finding (structural risk, scope too large, dependency SPOF) but the plan's timeline, scope, or resource allocation remained unchanged after review.

**Check**: Name one concrete change to the plan that directly addresses the highest-severity finding. If no plan element changed, the analysis produced awareness, not decision quality. Awareness alone does not reduce downside.

*Source: Roose, Lehman & Veinott (2023), Human Factors — 10 real game-development teams; failure reasons identified at average 17.8 per session; plan-revision rates remained low particularly when remediation required scope reduction.*

*Domain caveat: student game-development context (N=10 teams, N=68 participants). Treat as directional; enterprise generalizability requires independent replication.*

---

## 8. Reversibility Underestimation

Decisions that feel reversible often aren't. Once a vendor is contracted, data migrated, a team restructured, or a product shipped externally — the reversal cost is not symmetric. Plans that rely on "we can always roll back" frequently discover rollback is prohibitively expensive, technically complex, or contractually blocked.

**Signal**: Risk mitigation language includes "we can revert" or "rollback is available."

**Check**: What is the literal rollback procedure? How long does it take? What data or state would be lost? Has anyone actually tested it?
