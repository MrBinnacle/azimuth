# Workflow Closure Protocol

Load after AZIMUTH returns a verdict or residual-risk register and the user needs follow-through rather than more analysis.

---

## Purpose

High-quality decision analysis fails if it does not change the next action. This protocol turns a verdict into an execution handoff, persistent tracking artifact, and review loop.

Use it to make AZIMUTH a workflow closer, not a report generator.

---

## When to Run

Run in STANDARD+ when any of these are true:

- Verdict is PROCEED WITH SAFEGUARDS, PILOT FIRST, REDUCE SCOPE, DELAY PENDING EVIDENCE, or RESIDUAL-RISK-REGISTER
- User asks "what now?", "make this actionable", "turn into a plan", "handoff", or "track this"
- The output includes any Launch-Blocking Tiger, Elephant, Red/Black L×I risk, or accepted residual risk
- DEEP mode was used and a decision record is warranted

Do not run automatically for INSUFFICIENT SIGNAL or WRONG TOOL unless the user asks for a refactoring prompt.

---

## Next Action Protocol

Produce only decision-changing follow-through.

```markdown
## Next Action Protocol

### 1. Immediate Decision Gate
- Decision owner: [person/role]
- Gate: [what must be true before commitment]
- Deadline / review point: [date or named milestone]

### 2. Required Commitments
| Finding | Action | Owner | Leading Indicator | Review Date | Escalation Trigger |
|---|---|---|---|---|---|

### 3. Handoff Prompt
Use this prompt with the execution agent / team:

> We are acting on AZIMUTH verdict [VERDICT] for [decision]. Preserve these constraints: [constraints]. Do not proceed past [gate] until [evidence]. Track these indicators: [indicators].

### 4. Follow-Up Review
- First review: [date]
- Outcome evidence to collect: [evidence]
- Decision that will be revisited: [scope / proceed / stop / expand]
```

---

## Persistence Options

If the user wants durable state, write or export one of:

- `templates/decision-record.md` — final decision artifact
- `templates/commitment-lock.md` — owned mitigation table
- `learnings/outcome-tracking.md` — post-outcome calibration record
- `templates/export-formats.md` — CSV/Jira/Obsidian-ready register formats

AZIMUTH should not pretend it can persist files unless the runtime can actually write them. If persistence is unavailable, output a copy-ready artifact.

---

## Safety Gates Before Execution

Before handing off to execution, confirm:

1. The execution task matches the verdict. Do not execute full scope after PILOT FIRST or REDUCE SCOPE.
2. Every Launch-Blocking Tiger has an owner and decision date.
3. Every accepted Red/Black L×I risk has a leading indicator and escalation trigger.
4. The highest-risk assumption has a falsifier or evidence gate.
5. The handoff prompt names what must not be optimized away.

---

## Anti-Patterns

- Do not turn every finding into a task; only decision-changing findings get tracked.
- Do not use "team" as owner.
- Do not let a generic implementation plan overwrite the verdict constraints.
- Do not produce follow-up theater when the verdict is REJECT; the only next action may be stopping or reframing.

---

## Provenance

Inspired by workflow-orchestration and persistent-planning patterns common in high-adoption Claude skills. Rewritten for AZIMUTH's verdict and register model.
