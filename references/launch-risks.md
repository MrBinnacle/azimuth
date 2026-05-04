# Launch Risks Reference

Load when running a azimuth on a product launch, feature release, service go-live, beta rollout, or public announcement with execution dependencies.

---

## Pre-Launch Risk Zone

### Risk: Go-Live Date Set Politically

**What it looks like**: Launch date anchored to an external event (conference, investor update, board meeting, competitor response) rather than to actual readiness. Team works backward from the date rather than forward from the work.

**Why it fails**: Political deadlines compress QA, skip edge case testing, force incomplete feature sets, and create rushed communication. Problems are found by users, not the team.

**Signal**: "We have to ship by [event]." Scope is being cut to hit the date rather than the date being adjusted to fit scope.

**Mitigation**: Separate the announcement from the feature. Announce intent; ship when ready.

---

### Risk: Definition of "Launch-Ready" Is Ambiguous

**What it looks like**: No explicit criteria for what constitutes a launchable state. Engineers think it's ready when the feature works. PMs think it's ready when the demo works. Legal/compliance hasn't been consulted.

**Why it fails**: Different stakeholders have different internal definitions. Last-minute gate discoveries cause delays or force unvetted launches.

**Signal**: No written launch checklist. Launch criteria not formally agreed upon.

**Mitigation**: Define launch criteria by category: functional, performance, security, legal, support readiness, communication. Require sign-off in each category before launch.

---

### Risk: Incomplete Rollback Plan

**What it looks like**: Launch plan describes go-live procedure in detail. Rollback procedure is one sentence: "revert the deployment."

**Why it fails**: Rollback at user-facing scale often involves data state, external integrations, cached assets, and customer communications — none of which "revert the deployment" addresses.

**Signal**: No rollback procedure documented beyond the technical deployment layer. No definition of the trigger condition for rollback.

**Mitigation**: Define rollback condition explicitly ("if X metric drops below Y within Z hours, we roll back"). Document the full rollback procedure, including communication, data reconciliation, and dependency handling.

---

## Launch Execution Risk Zone

### Risk: Support Is Not Ready

**What it looks like**: Engineering and product are ready. Support team is not trained, documentation doesn't exist, escalation paths aren't defined. Users experience problems and have no functional support path.

**Why it fails**: User experience at launch is heavily determined by support quality, not product quality. An underserved launch generates disproportionately negative reputation.

**Signal**: Support documentation is "in progress." No dry-run of support flows. No triage runbook for expected issue types.

**Mitigation**: Support readiness is a launch gate, not a post-launch task. Require support documentation and escalation flows to be tested before launch.

---

### Risk: Infrastructure Not Sized for Launch Spike

**What it looks like**: Infrastructure is provisioned for steady-state expected traffic. Launch drives a spike — from press, product hunt, email campaigns, or word of mouth — that exceeds provisioned capacity.

**Why it fails**: Launch-day degradation or outage is highly visible, disproportionately damaging to trust and press coverage, and entirely avoidable.

**Signal**: Load testing done at expected average traffic, not spike traffic. No autoscaling configured or tested.

**Mitigation**: Define expected spike (announcement reach × conversion rate). Load test to 3–5× expected steady state. Confirm autoscaling is configured and has been tested.

---

### Risk: Third-Party Integration Failure at Launch

**What it looks like**: Launch depends on a third-party payment processor, email provider, identity service, or API. That service has an unrelated outage or rate-limit issue during the launch window.

**Why it fails**: Third-party failures are outside control. When they happen during a high-visibility launch, the effect is the same as if you caused the failure.

**Signal**: Launch is tightly coupled to a single third-party service with no graceful degradation path.

**Mitigation**: For each critical third-party dependency, define: what happens to the user experience if it's unavailable? Is there graceful degradation? Is there a notification path?

---

## Post-Launch Risk Zone

### Risk: No Launch Metrics Defined

**What it looks like**: Launch happens. Team watches dashboards but has no defined success thresholds. "Looking good" is the standard. Problems are identified reactively when they become too large to ignore.

**Why it fails**: Absence of defined thresholds means absence of triggers. Small problems that compound go unaddressed.

**Signal**: No go-live dashboard with explicitly defined health thresholds and alert conditions.

**Mitigation**: Define: What are the 3–5 metrics that indicate launch health? What are the thresholds for "watch," "respond," and "rollback"? Who is on call? What are their response time expectations?

---

### Risk: Silent Failure in Edge Populations

**What it looks like**: Launch analytics look healthy at aggregate level. A subset of users — specific devices, regions, browsers, or account types — experience silent failures. They don't report; they just churn.

**Why it fails**: Aggregate metrics mask edge population failures. Without segment-level monitoring, problems in 5–10% of the user base can go undetected for weeks.

**Signal**: Monitoring is aggregate-only. No segment-level breakdowns configured.

**Mitigation**: Monitor key metrics broken out by: platform, region, user cohort, account tier. Define alert thresholds at segment level, not just aggregate.

---

### Risk: Communication Plan Decoupled from Execution Plan

**What it looks like**: Marketing has scheduled announcements, social posts, and email campaigns. Engineering has its own deployment schedule. They are not coordinated. Announcements go out before the feature is live, or the feature ships without any communication.

**Why it fails**: Decoupled communication and deployment creates confusion, credibility damage, and support overload.

**Signal**: Marketing and engineering are in separate planning documents with no shared launch timeline.

**Mitigation**: Single shared launch timeline with both engineering milestones and communication milestones. Communication holds until deployment is confirmed live and healthy.
