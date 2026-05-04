# Codebase Azimuth Template

Use this template when:
- Plan involves a refactor, rewrite, migration, or infrastructure change
- Technical risk is the dominant concern
- Audience includes engineering leads, architects, or technical PMs

---

## Template

---

**CODEBASE AZIMUTH — [Initiative Name]**
*Scope: [What is being changed] | Timeline: [Duration] | Owner: [Name/Team]*

---

**VERDICT**
[One sentence. Is this technically sound, conditionally safe, or not ready to proceed?]

---

**TECHNICAL OBJECTIVE**
[What specific technical outcome does this produce? State in measurable terms — not "clean up the codebase" but "reduce p99 latency by X" or "eliminate class Y of incident."]

If no measurable technical objective is defined: flag this as the primary risk before proceeding.

---

**BREAKPOINT ZONES**

Sections of the plan where failure is most likely to originate:

**Zone 1: [Name]**
[Describe what this zone is and why it's a breakpoint. What's the technical risk? What are the symptoms of failure here?]

**Zone 2: [Name]**
[Same format.]

**Zone 3: [Name]**
[Same format.]

---

**HIDDEN COUPLINGS**

[List undocumented or non-obvious dependencies that could cause unexpected failures when the changed code is deployed.]

- [Component A] — hidden dependency on [Component B] via [mechanism]. Risk: [what breaks if this is violated]
- [Shared state / global variable / implicit contract]: [where it lives, what assumes it, what could change it]
- [Third-party behavior assumed but unspecified]: [what is assumed, where it's used, what happens if it changes]

If no couplings have been identified: this is likely an audit gap, not a clean codebase.

---

**REGRESSION RISKS**

Areas most likely to regress during or after the change:

1. **[Feature / Behavior]** — Mechanism: [why this is at risk] — Test coverage: [adequate / partial / none]
2. **[Feature / Behavior]** — Mechanism: [why] — Test coverage: [status]
3. **[Feature / Behavior]** — Mechanism: [why] — Test coverage: [status]

---

**SAFE ROLLOUT PATH**

Recommended sequence for reducing blast radius:

1. [Step] — Validation gate: [what must be true to proceed to next step]
2. [Step] — Validation gate: [criteria]
3. [Step] — Validation gate: [criteria]
4. [Full rollout] — Validation gate: [criteria]

**Feature flag / dark launch applicable?** [Yes / No / Partial] — [Rationale]

**Traffic ramp recommended?** [Yes / No] — If yes: [percentage increments and dwell time]

---

**ROLLBACK TRIGGER**

Define the exact conditions under which rollback is initiated:

- Trigger condition: [specific metric, error rate, or behavior threshold]
- Rollback procedure: [step-by-step — be specific]
- Rollback lead time: [how long does rollback take to execute?]
- Data integrity risk on rollback: [none / low / high — explain]
- Rollback tested in staging: [Yes / No / Partial]

If rollback has not been tested: require staging validation before production deployment.

---

**OBSERVABILITY READINESS**

Before deployment, the following must be in place:

- [ ] Structured logs covering [specific paths / operations]
- [ ] Metrics with defined alert thresholds for [key indicators]
- [ ] Distributed tracing active across [service boundaries]
- [ ] Runbook mapped to observable failure signals
- [ ] On-call owner identified with defined response SLA

---

**RECOMMENDED DECISION**

☐ PROCEED — Technical risk is acceptable; safeguards in place
☐ PROCEED WITH SAFEGUARDS — Specific mitigations required (list below)
☐ PILOT FIRST — Deploy to [subset] before broader rollout
☐ DELAY PENDING EVIDENCE — [What needs to be validated first]
☐ REJECT — [Why this approach should not proceed]

**Required safeguards before proceeding:**
1. [action] — Owner: [name] — By: [date]
2. [action]

---

**CONFIDENCE LEVEL**: [Low / Medium / High]
**Basis**: [Test coverage quality, coupling audit completeness, rollback validation status]
