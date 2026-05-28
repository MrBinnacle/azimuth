# Software Failure Patterns

Load when running an AZIMUTH analysis on a technical initiative: refactor, rewrite, migration, infrastructure change, API redesign, platform build, or codebase restructuring.

---

## Pattern 1: Scope Defined by Architecture, Not Outcome

**What happens**: Engineers define scope by what needs to change technically rather than what outcome the business needs. The technical scope grows to "do it right" while the business need that motivated the work gets lost or shifts.

**Failure signature**:
- Scope is described in technical units (files, modules, services) rather than business outcomes
- No success metric tied to user or business impact
- Completion is defined as "the refactor is done," not "X improved by Y"

**Azimuth question**: What specific, measurable business or operational outcome does this work produce? How will you know it's done in a way that mattered?

---

## Pattern 2: Unacknowledged Coupling

**What happens**: Code that appears modular is actually tightly coupled through shared state, implicit contracts, or undocumented side effects. Refactoring or replacing one component triggers failures in components that were not expected to be affected.

**Failure signature**:
- Test coverage is low or concentrated in unit tests without integration coverage
- Codebase has long-lived mutable state or global singletons
- Documentation describes intended architecture, not actual runtime behavior
- "It's just X" scoping language

**Azimuth question**: What are the least-documented cross-system dependencies in this codebase? Who knows the actual runtime coupling — not the intended design, the actual behavior?

---

## Pattern 3: No Rollback Mechanism

**What happens**: Migration or deployment proceeds without a validated rollback path. When something fails in production, reverting requires either extended downtime, data reconciliation, or manual intervention — none of which was planned for.

**Failure signature**:
- Deployment plan describes rollout but not rollback
- Database migrations are one-directional
- Rollback has not been tested in staging
- "We'll figure it out if something goes wrong"

**Azimuth question**: Walk through the exact rollback procedure. How long does it take? What data is at risk? Has it been tested?

---

## Pattern 4: The Long-Running Migration

**What happens**: Migrations are estimated as discrete events. In practice, they become long-running parallel states: old system and new system coexist for months, both requiring maintenance. Teams carry double the cognitive load. The cutover that was "one quarter away" persists for 12–18 months.

**Failure signature**:
- Plan has migration start date but no hard cutover date with business consequences
- Old and new systems will run in parallel "for a little while"
- No owner assigned for deprecating the old system

**Azimuth question**: What is the hard cutover date, enforced by what mechanism? What happens to the old system if the deadline slips?

---

## Pattern 5: Dependency on Undocumented Behavior

**What happens**: System relies on behavior of a third-party API, legacy service, or platform that was never formally specified — it just works that way. When that behavior changes (undocumented update, provider change, version bump), the system breaks.

**Failure signature**:
- Integration tests exist but test documented behavior only
- Third-party API has no SLA or versioning commitment
- System relies on response format, timing, or side effects that aren't in the official spec

**Azimuth question**: What is the most fragile assumption about external systems this plan depends on? What happens if that assumption is violated?

---

## Pattern 6: Team Knowledge Concentration

**What happens**: One engineer understands the system being changed. Everyone else is working from documentation, code comments, or folklore. When that engineer is unavailable — vacation, illness, departure — progress stops or mistakes multiply.

**Failure signature**:
- "Ask [name]" is the primary documentation for critical subsystems
- Code comments authored by one person with no others recently active in that area
- Turnover on the team has eroded original system knowledge

**Azimuth question**: Who are the irreplaceable individuals on this project? What happens to the timeline if any one of them is unavailable for 3 weeks?

---

## Pattern 7: Test Coverage Illusion

**What happens**: Code coverage metrics are high. Test suite passes. The tests verify that the code does what it was written to do — not that it does what the business actually requires. Edge cases, failure modes, and integration behavior are untested.

**Failure signature**:
- Coverage percentage reported without characterization of what is covered
- Tests are tightly coupled to implementation (test the how, not the what)
- No chaos or failure injection testing for critical paths
- QA is a phase at the end, not integrated throughout

**Azimuth question**: What is the most important behavior this system must have in production that is currently not tested? What is the most likely uncaught failure mode?

---

## Pattern 8: Performance Cliff

**What happens**: System works in development, staging, and initial production. Under real load, at scale, or with real data volumes, performance degrades non-linearly. The bottleneck was always present but invisible at low volume.

**Failure signature**:
- Performance testing done with synthetic or low-volume data
- No profiling done at projected production scale
- Architecture has known O(n²) or unbounded query patterns

**Azimuth question**: At 10× current expected load, where does this system break? Has that been tested? Where are the unbounded queries or operations?

---

## Pattern 9: Insufficient Observability

**What happens**: System is deployed. Something goes wrong. No one knows what. Logs are insufficient, metrics don't cover the failure domain, tracing is absent. Mean time to diagnosis extends into hours or days.

**Failure signature**:
- Monitoring plan is described as "we'll set up alerts"
- No structured logging across critical paths
- Distributed system with no distributed tracing
- Runbooks exist but don't map to observable failure signals

**Azimuth question**: If this system fails silently in production at 2am, what is the first indicator? How long until someone knows? How long until root cause is identified?

---

## Pattern 10: Version Lock and Dependency Rot

**What happens**: Project depends on specific versions of external libraries, frameworks, or services that are not being maintained or that have known vulnerabilities. Upgrading is deferred repeatedly until the cost becomes prohibitive.

**Failure signature**:
- Dependency tree has packages not updated in 12+ months
- Pinned dependencies with no upgrade path documented
- Security vulnerabilities in dependencies acknowledged but unaddressed

**Azimuth question**: What are the top 3 most outdated or vulnerable dependencies? What is the plan and timeline for addressing them?

---

## Pattern 11: Post-Cutover Spend Management Failure

**What happens**: Migration completes on schedule and within project budget, but the new environment costs materially more to operate than the old one. Over-provisioning, lift-and-shift architectural choices, and unoptimized resource allocation create a permanent operational cost increase that was not in the migration's success criteria. 84% of organizations report struggling to manage cloud spend post-migration (Flexera State of the Cloud 2025, N=750+).

**Failure signature**:
- Migration was designed for speed; right-sizing and cost optimization were deferred to "post-cutover"
- No owner assigned for cost optimization after go-live, or the owner has no mandate or deadline
- Vendor cost estimates were used for planning rather than analysis against actual workload patterns
- Cost ceiling or budget for the steady-state environment is undefined

**Azimuth question**: What is the validated ongoing monthly operational cost of the target environment against actual usage patterns — not vendor estimates? Who owns cost optimization after cutover, and what is their mandate and timeline?

---

## Pattern 12: Data Integrity Degradation

**What happens**: Data migration introduces silent corruption through schema translation, encoding mismatches, field truncation, or inconsistently applied transformation rules. The system appears operational while data quality has degraded below business requirements. Defects may not surface for weeks or months until a downstream process fails or a user discovers discrepant records.

**Failure signature**:
- Validation plan checks schema conformance but not correctness against business logic
- Validation is sampled rather than complete, with no risk stratification by data criticality
- Edge cases — null handling, character encoding, field truncation, precision loss — are not explicitly tested
- Success metric is "records migrated," not "records validated end-to-end"

**Azimuth question**: What is the data validation plan for migrated records, and does it detect silent corruption versus obvious schema failures? What percentage of records have been validated end-to-end against business logic — not just schema conformance checks?

---

## Pattern 13: Cutover Window Overrun

**What happens**: Cutover runs longer than the planned maintenance window. At execution time, the team faces a forced choice between extended downtime, partial cutover with data integrity risk, or emergency rollback — none of which was pre-decided, and decision authority was not pre-assigned. The absence of a decision tree at T+50% and T+100% converts a technical problem into a governance crisis under pressure.

**Failure signature**:
- Cutover plan has a time estimate but no decision tree for overrun scenarios
- Rollback trigger is described as "if needed" rather than specific, pre-agreed conditions
- Decision authority at key overrun thresholds is not assigned in writing before cutover
- Key decision-makers are not confirmed to be present and reachable during the cutover window

**Azimuth question**: What is the decision tree when the cutover window is exceeded by 50%? By 100%? At what point is rollback mandatory, who has explicit authority to make that call, and are they present and empowered at the scheduled cutover time?
