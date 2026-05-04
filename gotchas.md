# Gotchas

Load this file for high-stakes, expensive, or irreversible decisions — especially when the plan sounds unusually clean or the user is confident.

These are failure patterns that consistently evade standard risk checklists. They are not dramatic; they are structural and predictable in hindsight.

---

## 1. The Second System Effect

When replacing or rebuilding something that works, teams routinely overload the new version with accumulated feature wishes. The rewrite that was supposed to be "cleaner" ships late, overbuilt, and harder to maintain than the original.

**Signal**: Plan includes phrases like "and while we're at it…" or "we'll finally fix…"

**Check**: Is scope tightly bounded to what the original did, plus a defined delta? Or is the migration a wish list in disguise?

---

## 2. The Availability Illusion

Key person X is "available" for this project. In practice, availability means X has space on their calendar this week — not that X can absorb full execution load across a 3-month initiative while their existing obligations remain.

**Signal**: Owner has 2+ other active responsibilities. No formal allocation defined.

**Check**: What happens if X is pulled off for 3 weeks? Does the plan have a fallback, or does it stall?

---

## 3. Approval Chains as Infinite Loop

Plans that require sign-off from multiple layers underestimate cycle time almost universally. One missing stakeholder, one unexpected objection, one round of revisions, and a 2-week approval window becomes 6 weeks.

**Signal**: Plan says "pending approval" or "subject to legal/compliance/exec review" without lead times built into the schedule.

**Check**: What is the realistic approval chain? Has anyone pressure-tested cycle time with those stakeholders recently?

---

## 4. The Quiet Dependency

The most dangerous dependency is not the one flagged in the plan — it's the one nobody thought to mention because it's "always there." Shared infrastructure, a legacy data feed, a third-party API used by a different team, a spreadsheet maintained by one person.

**Signal**: Plan references infrastructure or data sources that aren't owned by the team executing the work.

**Check**: For each data source, API, or system the plan touches: who owns it? What's the SLA? When did it last break?

---

## 5. Commitment Escalation

Once enough sunk cost accumulates — time spent, money spent, reputation staked — the willingness to stop or change course collapses. Teams continue executing a failing plan because stopping feels worse than continuing, even when the evidence clearly favors stopping.

**Signal**: User describes the initiative as already underway, already communicated externally, or carrying prior investment.

**Check**: Is the decision being made based on future value, or is past investment distorting judgment? Would this plan be approved fresh today with the current evidence?

---

## 6. The Consensus Trap

Plans that require no one to make a hard call — where every stakeholder must agree — functionally have no decision-maker. Consensus-required governance drifts, stalls on edge cases, and produces watered-down outcomes that satisfy no one's original intent.

**Signal**: Governance language like "cross-functional alignment," "everyone must agree," "no unilateral decisions."

**Check**: Who can break a tie? Who has final authority? If everyone has veto power, the plan has no owner.

---

## 7. The Last-Mile Gap

A plan can be technically complete and still fail at handoff: training not done, documentation missing, the receiving team not ready, rollout communication unclear. The last 10% of execution — the part that faces real users or live systems — is systematically underinvested.

**Signal**: Plan has detailed build phase, sparse rollout phase, and no user readiness section.

**Check**: What happens the day after go-live? Who handles first-wave issues? Is that path defined?

---

## 8. Metric Drift

The success metric is defined at plan inception. By the time the initiative concludes, the goalposts have shifted — the business context changed, stakeholder priorities shifted, the original metric no longer reflects what anyone actually cares about. The work gets done; the outcome isn't valued.

**Signal**: Plan is longer than 90 days with no metric checkpoint cadence.

**Check**: Are success metrics locked and dated? Is there a mid-point validation where the metric is reconfirmed against current business reality?

---

## 9. The Confidence-Competence Gap

Whoever presented the plan was confident. Confidence is domain-dependent — a strong operator can be a poor judge of technical timelines, or a strong engineer can be a poor judge of market demand. Confidence from outside the domain of execution is not reliable signal.

**Signal**: The person evaluating feasibility is not the person executing it.

**Check**: Has the person accountable for execution validated the timeline and scope estimate independently — not just endorsed someone else's?

---

## 10. Survivorship Framing

Analogies to successful prior initiatives ("we did X and it worked, so Y will too") ignore the structural differences. The successful case may have had better timing, more resources, a smaller scope, a stronger team, or plain luck. Citing success cases without examining the failure distribution is not evidence.

**Signal**: Justification includes "we did this before" or "company X pulled this off."

**Check**: What were the failure cases that look similar? What distinguishes this case from those?

---

## 11. The Integration Tax

Individual components each work. The assumption is they'll work together. Integration — connecting real systems with real data under real load, across real teams with different conventions — consistently takes 2–5× longer than estimated and generates most of the late-stage defects.

**Signal**: Plan has component timelines but no integration buffer. No integration test environment defined.

**Check**: When does integration testing begin? What is the contingency if integration reveals fundamental incompatibilities between components?

---

## 12. Reversibility Underestimation

Decisions that feel reversible often aren't. Once a vendor is contracted, data migrated, a team restructured, or a product shipped externally — the reversal cost is not symmetric. Plans that rely on "we can always roll back" frequently discover rollback is prohibitively expensive, technically complex, or contractually blocked.

**Signal**: Risk mitigation language includes "we can revert" or "rollback is available."

**Check**: What is the literal rollback procedure? How long does it take? What data or state would be lost? Has anyone actually tested it?
