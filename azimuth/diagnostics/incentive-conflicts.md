# Incentive Conflicts Diagnostic

This file is an observational catalog. It describes patterns of incentive misalignment to look for during a Module 4 incentive scan. It does not assign verdicts, cap confidence, or define when to load — decision authority for those lives in `BEHAVIOR_SPEC.md`.

---

## Purpose

Identify where the incentives of actors involved in — or adjacent to — the plan create pressure toward decisions that are not in the plan's best interest.

Incentive misalignment is not about bad actors. It is structural. People respond to what they are measured on and rewarded for. If those measures diverge from plan success criteria, divergent behavior is predictable.

---

## Incentive Categories to Scan

### 1. Deadline Politics

**Pattern**: Timeline was set to satisfy an external stakeholder (investor, executive, board, event) rather than to reflect actual execution capacity. Team members feel unable to surface a realistic timeline without appearing uncommitted or incompetent.

**Risk**: Real problems are concealed until too late. Progress reports are optimistic. Issues compound in silence.

**Questions**:
- Who set the timeline, and based on what evidence?
- Do the people executing the work believe the timeline is achievable? Has anyone asked them directly, privately?
- Is there a safe mechanism for escalating timeline risk?

---

### 2. Vanity Metrics as Success Proxy

**Pattern**: The stated success metric is easy to hit but doesn't reflect actual value. Team optimizes for the metric rather than the underlying goal. Examples: launch date hit, features shipped, sign-ups generated (not retained), demos completed (not converted).

**Risk**: Plan achieves its stated metrics and still fails at the underlying goal. No one is accountable for the real outcome because the measured outcome was satisfied.

**Questions**:
- What is the success metric the team will be evaluated on?
- Does that metric directly measure the outcome the plan is intended to produce?
- Could the metric be satisfied while the underlying goal fails?

---

### 3. Sunk Cost Preservation

**Pattern**: Significant prior investment (time, money, reputation, political capital) in a direction creates incentive to continue regardless of current evidence. The person who championed the direction is now the person evaluating whether to continue it.

**Risk**: Evidence that the plan should be significantly altered or stopped is filtered, minimized, or rationalized. Stopping becomes institutionally difficult regardless of merit.

**Questions**:
- Who has the most personal investment in this plan proceeding?
- Is that person the same individual responsible for go/no-go judgment?
- Is there an independent voice with genuine authority to recommend stopping?

---

### 4. Vendor Incentive Misalignment

**Pattern**: Vendor or contractor is paid by time, feature, or deliverable — not by outcome. Their interest is in scope expansion, continued engagement, or minimizing rework. Your interest is in the smallest effective solution delivered reliably.

**Risk**: Scope expands. Timelines extend. Complexity accumulates. Vendor performs to contract while plan value degrades.

**Questions**:
- How is the vendor compensated? Time-and-materials, fixed bid, or outcome-based?
- Does scope creep benefit the vendor financially?
- Who on the internal team is responsible for holding vendor scope, and do they have the authority to enforce it?

---

### 5. Career Incentive Distortion

**Pattern**: The person responsible for a component of the plan has incentives to make the work appear larger, more complex, or more critical than it is — to justify headcount, budget, or personal visibility. Alternatively, they have incentive to suppress problems to protect their performance review.

**Risk**: Inflated estimates hide reality in the upward direction; concealed problems hide it in the downward direction.

**Questions**:
- Are estimates coming from people who benefit from large estimates?
- Is there a mechanism for surfacing bad news without penalty?
- What happens to the person who first reports that something isn't working?

---

### 6. Local Optimization vs. Plan Success

**Pattern**: Teams, departments, or individuals optimize for their own metrics in ways that are technically consistent with the plan but harmful to the whole. Engineering optimizes for code quality while missing deadlines. Sales optimizes for deal count while signing customers the product can't yet serve.

**Risk**: Each component looks fine in isolation; the integrated outcome fails.

**Questions**:
- Are there local metrics (speed, quality, quantity, cost) that could be satisfied while overall plan success is undermined?
- Who is responsible for the integrated outcome — not the components?
- Is there a mechanism to detect local optimization that harms the whole?

---

### 7. Approval Authority Without Accountability

**Pattern**: Someone with veto power over the plan — budget owner, executive sponsor, regulatory body — has no accountability for outcomes if the plan fails. They can block or delay without bearing any cost for the delay itself.

**Risk**: Approval processes are slow and conservative because delay has no downside for the approver. Decisions are made based on risk aversion rather than plan quality.

**Questions**:
- Who can veto or delay this plan?
- What are their incentives? Do they benefit from approval or delay?
- Is there a way to create shared accountability between approval authority and execution?

---

## Severity Classification

After scanning, classify each identified conflict:

**GOVERNANCE RISK** (highest): Incentive misalignment that could cause systematic concealment of problems, prevent escalation, or corrupt go/no-go judgment. Requires structural mitigation — not just communication.

**EXECUTION RISK**: Incentive misalignment that creates predictable adverse behavior in one or more actors. Can be mitigated by metric redesign, clear scope boundaries, or independent oversight.

**LATENT RISK**: Incentive misalignment that is present but unlikely to activate unless under pressure. Monitor; define trigger condition.

---

## Output Format

### Incentive Conflicts Identified

| Actor | Conflict Type | Severity | Effect on Plan |
|-------|---------------|----------|----------------|
| [name/role] | [type] | [Gov/Exec/Latent] | [what behavior does this produce?] |

### Governance Risk Summary
[If any GOVERNANCE RISK conflicts exist, summarize here with recommended structural mitigation.]

### Recommended Mitigations
1. [conflict] — Mitigation: [structural change, metric redesign, oversight mechanism]
