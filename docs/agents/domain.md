# Domain Docs

How the engineering skills should consume this repo's domain documentation.

## Layout

Single-context repo. If `CONTEXT.md` and `docs/adr/` exist at the repo root, read them before exploring. If they don't exist yet, proceed silently — they are created lazily as terms and decisions are resolved.

## Repo context summary

AZIMUTH is a pure-markdown AI agent skill for decision quality analysis. There is no build system, no runtime, no tests. All "development" is editing `.md` files. Key domain vocabulary lives in `SKILL.md` (the skill entry point) and `gotchas.md`.

Before working on module logic, routing, or analysis claims, check `SKILL.md` and `gotchas.md` directly — they are the authoritative source of domain truth for this repo.

## ADRs

No `docs/adr/` directory exists yet. Architectural decisions are currently tracked via the CHANGELOG and commit history. If a meaningful architectural decision is made, create `docs/adr/0001-<decision>.md`.

## Flag ADR conflicts

If your output contradicts a past architectural decision visible in CHANGELOG.md, surface it explicitly rather than silently overriding.
