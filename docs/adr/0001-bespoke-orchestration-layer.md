# Bespoke orchestration layer for AZIMUTH

AZIMUTH is a pure-markdown agent skill consumed by user projects, not a project that consumes engineering skills. Its maintenance stack must support a single repo whose entire surface area is markdown — no code, no tests, no build. Mainstream engineering-skill stacks (Pocock's `to-issues` / `tdd` / `diagnose` / `improve-codebase-architecture`) were designed for codebases. They apply here only partially.

This ADR records the orchestration layer AZIMUTH uses and the patterns it rejects, so future proposals can be evaluated against a written design rather than re-litigated from scratch.

## Decision

Two layers. No pipeline skill. No verify flags. No second config layer.

### Layer 1 — Documentation substrate

- **`SKILL.md`** — the spec. Always-loaded. Authoritative source of what AZIMUTH does.
- **`gotchas.md`** — must hold exactly 8 numbered sections. Always-loaded feedback loop.
- **`references/`, `diagnostics/`, `templates/`** — on-demand-loaded by mode, domain, and per-module findings.
- **`CONTEXT.md`** — does not exist yet. Created lazily, one term at a time, when a real grilling session resolves a confusion. Never authored upfront.
- **`docs/adr/`** — this directory. Created lazily; only meaningful structural decisions earn an ADR.
- **`.out-of-scope/`** — rejection rationale for proposed-but-not-built features. Public, durable, citable from future proposals.
- **`docs/agents/{issue-tracker,triage-labels,domain.md}`** — seeded by `/setup-matt-pocock-skills`. Consumer config for engineering skills.

### Layer 2 — Maintenance skill stack

Three failure-mode-mapped skills live in `.claude/skills/` and travel with the repo for maintainers. None are installed to end users.

| Skill | Failure mode | Hard-dep |
|---|---|---|
| `research-scout` | Source staleness — 8 primary citation families drift | `references/base-rates.md`, `research/staged-findings.md` |
| `verdict-auditor` | Output drift / confidence inflation on cautious verdicts | A pasted AZIMUTH output |
| `gap-scanner` | Coverage-claim vs reality drift between SKILL.md and the files it claims to load | Soft (degrades silently) |

Two additional gate skills are designed but **deliberately not built**: `depth-gate` (fires before adding a template/reference/diagnostic) and `calibration-check` (fires when claiming a new threshold). Both wait for the next observed recurrence before being authored, per Pocock's failure-mode-first principle. Authoring them speculatively would violate the depth-over-breadth rule the gates themselves enforce.

## Patterns this layer adopts

- **Hard-dep vs soft-dep skill split** (Pocock ADR-0001). Hard-dep skills carry explicit setup pointers. Soft-dep skills degrade silently without their config.
- **Producer/consumer separation.** `/grill-with-docs` produces `CONTEXT.md` and ADRs; `/diagnose`, `/tdd`, `/improve-codebase-architecture` consume them. AZIMUTH's maintenance trio consume `references/`, `gotchas.md`, and `staged-findings.md` produced by hand or by `/research-scout`.
- **Lazy file creation.** Don't scaffold; write only when there is something to write. Applied to `CONTEXT.md`, `docs/adr/`, and `.out-of-scope/` additions.
- **`.out-of-scope/` as rejection log.** Closed feature requests preserved as design rationale, citable from future proposals.
- **Mainstream-only escape hatches.** Default output template (`references/output-template.md`) handles any Layer 3 "Other" decision — replaces the impulse to add a domain template for every new use case.
- **CLAUDE.md as discipline enforcer.** Validation checks (489-char description, 8-section gotchas, paths exist) are enforced pre-commit. Same pattern as Pocock's bucket-promotion enforcement in his `skills` repo.

## Patterns this layer explicitly rejects

- **No pipeline skill.** No `/azimuth-release`, no `/azimuth-full-audit` chaining gap-scan + verdict-audit + research-scout. Composition belongs in conversation. Anti-framework — same posture Pocock takes against GSD/BMAD/Spec-Kit.
- **No verify-mode skill or `--verify` flag for `/setup-matt-pocock-skills`.** Re-run the prompt-driven setup with a verify intent. Matches `.out-of-scope/setup-skill-verify-mode.md` in Pocock's skills repo.
- **No backfill of MEMORY entries as ADRs.** Lazy-creation rule — ADRs document decisions when they crystallise, not retroactively. MEMORY entries that capture rejections promote to `.out-of-scope/`; MEMORY entries that capture known defects stay in MEMORY or promote to GitHub issues with `ready-for-human`.
- **No upfront `CONTEXT.md` glossary.** Drafting 15 unproven terms is spec-writing, not discipline. The glossary grows one resolved confusion at a time via `/grill-with-docs`.
- **No second config skill.** All per-repo agent config flows through `/setup-matt-pocock-skills` and `docs/agents/*.md`. Splitting the surface area duplicates maintenance.

## What this layer does NOT yet have

These are deliberately open, awaiting evidence:

- No `CONTEXT.md` (first term must emerge from a real grilling session)
- No `depth-gate` or `calibration-check` skills (first recurrence must happen)
- No install-time test that confirms `.out-of-scope/` ships to end users via `npx skills add`
- No calibration of the PROCEED-WITH-SAFEGUARDS threshold cap (pending eval scope)

## When to revisit this ADR

- A proposal arrives to add a pipeline skill, verify-mode skill, or second config layer — point at this ADR
- A real recurrence of template bloat or unvalidated heuristic — author `depth-gate` or `calibration-check`, then update this ADR
- The first `CONTEXT.md` term gets resolved — update `docs/agents/domain.md` to point at it
- An install-time test reveals `.out-of-scope/` does not ship to users — decide whether to move it or accept maintainer-only scope
