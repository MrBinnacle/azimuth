# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

AZIMUTH is a pure-markdown AI agent skill — no build system, no dependencies, no tests. There is nothing to compile or run. All "development" is editing `.md` files and validating their content against the constraints below.

## Repo structure

```
azimuth/
├── SKILL.md                     # Core skill entry point — frontmatter + 10-module analysis engine
├── gotchas.md                   # Must contain exactly 8 numbered sections (## 1. … ## 8.)
├── references/                  # Loaded on demand in STANDARD/DEEP mode
├── diagnostics/                 # Deep-mode diagnostic modules
├── domain-policies/             # Per-domain gating/configuration (loaded via Layer 3 intake)
├── docs/adr/                    # Architectural decisions (lazy-created; start at ADR-0001)
└── .out-of-scope/               # Rejection rationale for proposed-but-not-built features
```

All paths referenced inside `SKILL.md` must exist as real files. The install tool (`npx skills add`) copies the entire directory tree.

## Codebase Overview

AZIMUTH is a conditional file-loading system. `SKILL.md` is the always-loaded orchestrator; every other file loads on-demand based on mode, domain, and per-module findings. The skill has a 10-module analysis engine, four operating modes (FAST/STANDARD/RAPID/DEEP), domain-policies routed via Layer 3 intake, and a 9-verdict taxonomy.

**Stack:** Pure markdown — no code, no build system, no dependencies  
**Critical constraint:** SKILL.md truncates at line 225 under long sessions (>~150K–177K token history); all module instructions are past line 225

For detailed architecture, module load matrix, domain-policy routing, hook classification, and eval program findings, see [docs/CODEBASE_MAP.md](docs/CODEBASE_MAP.md).

For the maintenance orchestration design (producer/consumer split, lazy file creation, hard-dep vs soft-dep skills, and what is deliberately not built), see [docs/adr/0001-bespoke-orchestration-layer.md](docs/adr/0001-bespoke-orchestration-layer.md). Consult before proposing new maintenance skills, pipeline workflows, or verify-mode flags.

For the engine-layer governance diagnosis and the SPEC/RUNTIME/DIAGNOSTICS/RATIONALE taxonomy, see [docs/adr/0002-engine-layer-governance.md](docs/adr/0002-engine-layer-governance.md). Consult before proposing new diagnostics, domain-policies, references, or behavioural rules.

## Layer taxonomy (per ADR-0002)

Every artifact in this repo belongs to exactly one layer. Use this vocabulary when proposing additions.

- **SPEC** — authoritative, enforced contract. Deterministic, no rationale. Today: `VALIDATION.md`. Future: `BEHAVIOR_SPEC.md`.
- **RUNTIME** — executable behaviour the engine performs at analysis time. `SKILL.md`, `references/`, `domain-policies/`, `diagnostics/` (behaviour-override portions).
- **DIAGNOSTICS** — failure-detection taxonomy + maintenance-loop tooling, read at maintenance time. `.claude/skills/maintenance/`, `.claude/agents/`, `diagnostics/` (taxonomy portions).
- **RATIONALE** — why SPEC/RUNTIME/DIAGNOSTICS exist. Not load-bearing for correctness. This file, `docs/adr/`, `.out-of-scope/`, MEMORY, CHANGELOG, README.

Hooks depend on SPEC only. SPEC does not depend on RATIONALE. RUNTIME and DIAGNOSTICS may cite RATIONALE but do not require it for execution.

## Validation checks (run before every commit)

The 4 repo-integrity rules are specified authoritatively in [VALIDATION.md](VALIDATION.md) and enforced mechanically by `.claude/hooks/validate-azimuth.sh` as a PreToolUse hook on `git commit`. Spec is the source of truth; hook mirrors it. Diverge → fix the hook, not the spec.

**Rationale for each rule** (the why; spec is the what):

- **Rule 1 (description = 489 chars).** The `npx skills add` install pipeline validates this character count; drift breaks installs with a cryptic warning. 489 is the count that has shipped in v1.x and is treated as load-bearing for skill-listing context budget.
- **Rule 2 (gotchas.md = 8 sections).** The 8-section structure is referenced by Pocock's gotchas-discipline (one section per anticipated/observed anti-pattern); the count is a structural-drift smoke alarm, not a feature limit. If real evidence justifies a 9th section, change the rule deliberately — don't let it drift.
- **Rule 3 (no "precommitment").** "Pre-commitment" is AZIMUTH's canonical term per the verdict taxonomy. The hyphenless form is a recurring typo that erodes vocabulary discipline (see CONTEXT.md when authored).
- **Rule 4 (path integrity).** SKILL.md's conditional-load architecture depends on referenced paths resolving. A missing file is a silent failure at load time — STANDARD/DEEP runs simply skip the load with no error.

Hook bypass (`git commit --no-verify`) is acceptable when intentional but every bypass should leave a CHANGELOG[Unreleased] note explaining why.

## Commit conventions

```
type(scope): description
```

Types: `feat`, `fix`, `docs`, `refactor`  
Scope: `skill`, `gotchas`, `references`, `diagnostics`, `domain-policies`, `meta`

## Release process

Releases follow `vMAJOR.MINOR.PATCH`. Key steps:

1. Validate all four checks above
2. `git add` only the changed files (never `.omc/`)
3. `git tag -a vX.Y.Z -m "..."` and push both master and the tag
4. `gh release create` using the CHANGELOG entry as release notes
5. Verify install: `npx skills add https://github.com/MrBinnacle/azimuth --skill azimuth -a claude-code -y`

## Maintenance skill stack

For the full operational orchestration model — verification layers (commit/audit/release-time), maintenance-loop responsibilities, subagent dispatch invariants, migration / rollback discipline, drift vectors, and next-session continuation — see [docs/MAINTENANCE.md](docs/MAINTENANCE.md). The section below summarizes only the maintenance skill stack.

Four skills live in `.claude/skills/maintenance/` for maintainer use. They are not installed by `npx skills add` — they travel with the repo for whoever works on it.

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `research-scout` | Tracks 8 citation source families; stages updates to `references/base-rates.md` | "run the research scout" / "promote staged findings" |
| `verdict-auditor` | Stress-tests a real AZIMUTH output against the skill's own structural rules | "audit this output" (paste output first) |
| `gap-scanner` | Cross-references SKILL.md coverage claims against actual reference, diagnostic, and domain-policy files | "run the gap scanner" |
| `reference-authoring` | Discipline for new reference files and domain-policies: EXTEND-vs-CREATE, Module 7 vocabulary header, sourcing caveat, pre-verdict gate | When adding a new reference file or domain-policy |

Two additional gate skills are **designed but deliberately not built** (see ADR-0001):

- `depth-gate` — fires before adding a new domain-policy/reference/diagnostic. Awaits first observed recurrence of unjustified expansion.
- `calibration-check` — fires when claiming a new threshold/cap in SKILL.md. Awaits first observed recurrence of an uncited heuristic.

Do not author these speculatively. The trigger is an observed failure, not anticipated friction.

Staged research findings live in `research/staged-findings.md`. The research-scout writes there; you promote to `references/base-rates.md` via the PROMOTE mode.

## Installed external skills

Installed via `npx skills@latest add`, copied to `~/.claude/skills/`:

| Skill | Source | Purpose | Invoke |
|-------|--------|---------|--------|
| `grill-with-docs` | [mattpocock/skills](https://github.com/mattpocock/skills) | Stress-test skill output or code against its own documentation rules. | `/grill-with-docs` |
| `write-a-skill` | [mattpocock/skills](https://github.com/mattpocock/skills) | Scaffold a new agent skill with correct frontmatter and structure. | `/write-a-skill` |
| `zoom-out` | [mattpocock/skills](https://github.com/mattpocock/skills) | Architectural perspective — step back from details, identify bigger patterns. | explicit only (`disable-model-invocation: true`) |
| `triage` | [mattpocock/skills](https://github.com/mattpocock/skills) | Process incoming GitHub issues through the five-state triage workflow. | `/triage` |
| `to-issues` | [mattpocock/skills](https://github.com/mattpocock/skills) | Convert a task list, PRD, or free-text scope into GitHub issues. | `/to-issues` |
| `handoff` | [mattpocock/skills](https://github.com/mattpocock/skills) | Structured agent handoff — context, goal, success criteria, return condition. | `/handoff` |
| `setup-matt-pocock-skills` | [mattpocock/skills](https://github.com/mattpocock/skills) | Re-run agent skills config (issue tracker, labels, domain docs). | explicit only (`disable-model-invocation: true`) |

## Agent skills

### Issue tracker

Issues tracked in GitHub Issues (`MrBinnacle/azimuth`) via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Default mattpocock vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context repo. `SKILL.md` and `gotchas.md` are the authoritative domain source. See `docs/agents/domain.md`.

## Obsidian vault

Project notes live in a local Obsidian vault under `Writ_vault/azimuth/`. Subfolders: `notes/`, `references/`, `outputs/`.

## Environment notes (Windows)

- `jq` is not available — use `node -e` for all JSON manipulation
- `cmd /c` wrapper required for npx-based MCP servers (set in `~/.claude.json` args array as `["/c", "npx", "-y", ...]`)
- `CLAUDE_PLUGIN_ROOT` env var expansion breaks in bash — use absolute paths directly
- `~/.claude/.omc-config.json` may be emptied by hooks — always write it via the Write tool rather than shell read+patch

## What not to touch

- `.omc/` — session state, never commit
- `LICENSE` — MIT, do not modify
- `MARKETING.md` — internal strategy doc, gitignored (local only, not in public repo)
