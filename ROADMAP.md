# Roadmap

What's coming. Sequenced by what matters most.

---

## v1.1.1 — Insufficient Signal verdict

Right now the skill returns a verdict on any input. Two vague sentences in, structured PILOT FIRST out, reasoning made up from nothing. That's the false-precision problem.

Fix: add `INSUFFICIENT SIGNAL` to the Module 10 verdict set. When input is too thin to support a verdict, the skill says so and lists what's missing instead of inventing one.

Trips when:
- Input below length threshold
- Fewer than N required fields populated (objective, scope, timeline, owner)
- Module 2 finds no assumptions to classify

---

## v1.1.x — Counterfactual layer

Module 2 asks what must be true. It doesn't ask what would prove the assumption wrong. Confirming evidence gets sought; disconfirming evidence doesn't. That's lopsided.

Fix: for every strong-evidence or partial-evidence assumption, list the falsifier. What would I have to see to know this is wrong? Add a Falsifiers section to output.

---

## v1.1.x — Coupling pass

Module 6 builds three failure paths as if each risk fires alone. Real failures stack — small delay plus dependency lag plus scope creep equals nonlinear breakdown. Three independent paths miss that.

Fix: after the failure paths, identify which two listed risks together produce nonlinear failure. New Interaction Effects section.

---

## v1.2.0 — Structured self-validation pass

After generating a verdict, the skill checks its own output against a defined rule set before presenting it. Catches the most common output discipline failures without requiring the verdict-auditor skill to be run separately.

Rules checked inline:
- Output leads with verdict (not preamble)
- No section header with empty content
- No weak mitigations ("communicate better," "monitor closely") in Highest-Leverage Fixes
- Confidence level stated with a reason, not just a label
- If domain matches base-rates.md coverage, at least one rate was cited

This is the same check set as the `verdict-auditor` maintainer skill, collapsed into the skill's own output loop. Not a gate that blocks the verdict — a self-audit line appended at the end: `[Self-check: N flags]` with brief notes if flags exist.

---

## v1.2.0 — Evidence tags

Output assumptions and risks have no source. Reader can't tell what came from the user, what came from base-rates, what came from a gotcha pattern, what's inferred. That's hidden authority.

Fix: every claim in output carries a tag — `[user-stated]`, `[base-rate: source]`, `[gotcha: name]`, `[inferred]`.

---

## v1.2.0 — Audit trail

Reader can't see which modules ran. Modules that surface nothing are still signal — they checked and found no concern. Right now that's invisible.

Fix: Audit Trail section listing modules invoked and what each surfaced (null, surfaced, high-severity).

---

## Held

These came up in review. Not shipping until usage data says they matter.

- **Multi-perspective framing pre-pass.** Run stakeholder framing rotation before locking the Module 1 objective. Useful when framing is the failure. Hold until I see Module 1 actually missing these.
- **Output gating enforcement.** Make modules block the verdict instead of advise it. Architectural shift, risks brittleness. Hold until v1.1.x and v1.2.0 show whether the soft enforcement actually misfires.
- **Decision graph / constraint solver.** Different tool, not a skill. Maybe later. Probably never.

---

## Source

v1.1.0 came out of an audit of v1.0.0 — gotchas compression, base-rates attribution, frontmatter tightening, verdict-led output. Shipped.

The five items above came out of architectural review after v1.1.0 went live.

Anything past this gets prioritized against real signal — issues, feedback, observed failures — not more methodology debate.
