# Domain Docs

How the engineering skills should consume this repo's domain documentation.

## Layout

Single-context repo. If `CONTEXT.md` and `docs/adr/` exist at the repo root, read them before exploring. If they don't exist yet, proceed silently — they are created lazily as terms and decisions are resolved.

## Repo context summary

AZIMUTH is a pure-markdown AI agent skill for decision quality analysis. There is no build system, no runtime, no tests. All "development" is editing `.md` files. Key domain vocabulary lives in `SKILL.md` (the skill entry point) and `gotchas.md`.

Before working on module logic, routing, or analysis claims, check `SKILL.md` and `gotchas.md` directly — they are the authoritative source of domain truth for this repo.

## ADRs

`docs/adr/` is the durable record of architectural decisions going forward. Read it before proposing structural changes. ADR-0001 records the bespoke maintenance orchestration layer; future ADRs are created lazily by `/grill-with-docs` when a real decision is resolved.

CHANGELOG.md remains the record for shipped behavioural changes (versioned releases); ADRs cover meta-design decisions about how the repo itself is structured and maintained.

## Flag ADR conflicts

If your output contradicts an existing ADR in `docs/adr/`, surface it explicitly rather than silently overriding. Quote the ADR and explain why it should be reopened. Also check CHANGELOG.md for prior behavioural decisions that may bear on the change.
