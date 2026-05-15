# Module Customization Guide

Load when users want to fork AZIMUTH, add a domain pack, or tune it for a team.

---

## Purpose

Make AZIMUTH easy to adapt without weakening the core decision discipline.

---

## What to Customize

Safe extension points:

- `references/` — domain failure patterns, base rates, bias references
- `diagnostics/` — deeper scoring or audit procedures
- `templates/` — output shapes for an audience or tool
- `learnings/` — outcome review and calibration notes

Avoid changing these unless you have eval evidence:

- verdict taxonomy
- Module 4 incentive tiering consequences
- Module 10 confidence ceilings
- WRONG TOOL / INSUFFICIENT SIGNAL / RESIDUAL-RISK-REGISTER boundaries
- anti-slop rules

---

## Domain Pack Pattern

A domain pack should include:

```text
references/[domain]-failure-patterns.md
templates/[domain]-azimuth.md
evals/[domain]-case-study.md
```

Each failure pattern should have:

- signal
- diagnostic question
- evidence class
- mitigation that changes system conditions
- known false positives

---

## Checklist for New Modules

- [ ] Does it load conditionally?
- [ ] Does it change a verdict, score, category, commitment, or artifact?
- [ ] Does it avoid duplicating existing modules?
- [ ] Does it preserve verdict-first output?
- [ ] Does it include provenance?
- [ ] Is there at least one eval or case study showing why it matters?

---

## Anti-Patterns

- Adding frameworks because they are popular, not because they change decisions
- Expanding SKILL.md until core routing is buried
- Turning AZIMUTH into generic coaching or brainstorming
- Weakening hard verdicts to improve user comfort

---

## Provenance

Inspired by high-adoption meta-skill and skill-creator patterns. Rewritten for AZIMUTH's modular architecture.
