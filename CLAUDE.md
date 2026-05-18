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
└── templates/                   # Pasteable output templates for specific decision types
```

All paths referenced inside `SKILL.md` must exist as real files. The install tool (`npx skills add`) copies the entire directory tree.

## Codebase Overview

AZIMUTH is a conditional file-loading system. `SKILL.md` is the always-loaded orchestrator; every other file loads on-demand based on mode, domain, and per-module findings. The skill has a 10-module analysis engine, four operating modes (FAST/STANDARD/RAPID/DEEP), domain-specific templates routed via Layer 3 intake, and a 9-verdict taxonomy.

**Stack:** Pure markdown — no code, no build system, no dependencies  
**Critical constraint:** SKILL.md truncates at line 225 under long sessions (>~150K–177K token history); all module instructions are past line 225

For detailed architecture, module load matrix, template routing, hook classification, and eval program findings, see [docs/CODEBASE_MAP.md](docs/CODEBASE_MAP.md).

## Validation checks (run before every commit)

```bash
# 1. SKILL.md frontmatter description must be exactly 489 chars
awk '/^description: /{flag=1} flag{print; if(/"$/) flag=0}' SKILL.md | tr -d '\n' | wc -c

# 2. gotchas.md must have exactly 8 numbered sections
grep -E '^## [0-9]+\.' gotchas.md | wc -l

# 3. No "precommitment" (must be "pre-commitment") outside CHANGELOG
grep -rn precommitment . --include="*.md" | grep -v CHANGELOG.md

# 4. All paths referenced in SKILL.md must exist
grep -oE '(references|diagnostics|templates)/[^ \n"]+\.md' SKILL.md | sort -u | while read f; do
  test -f "$f" && echo "OK: $f" || echo "MISSING: $f"
done
```

All four checks must pass before committing. If the description char count drifts from 489, the `npx skills add` install will surface a validation warning.

## Commit conventions

```
type(scope): description
```

Types: `feat`, `fix`, `docs`, `refactor`  
Scope: `skill`, `gotchas`, `references`, `diagnostics`, `templates`, `meta`

## Release process

Releases follow `vMAJOR.MINOR.PATCH`. Key steps:

1. Validate all four checks above
2. `git add` only the changed files (never `.omc/`)
3. `git tag -a vX.Y.Z -m "..."` and push both master and the tag
4. `gh release create` using the CHANGELOG entry as release notes
5. Verify install: `npx skills add https://github.com/MrBinnacle/azimuth --skill azimuth -a claude-code -y`

## Maintenance skill stack

Three skills live in `.claude/skills/` for maintainer use. They are not installed by `npx skills add` — they travel with the repo for whoever works on it.

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `research-scout` | Tracks 8 citation source families; stages updates to `references/base-rates.md` | "run the research scout" / "promote staged findings" |
| `verdict-auditor` | Stress-tests a real AZIMUTH output against the skill's own structural rules | "audit this output" (paste output first) |
| `gap-scanner` | Cross-references SKILL.md coverage claims against actual reference, diagnostic, and template files | "run the gap scanner" |

Staged research findings live in `research/staged-findings.md`. The research-scout writes there; you promote to `references/base-rates.md` via the PROMOTE mode.

## Installed external skills

**Plugin** (enabled via `settings.json`, no install step needed):

| Skill | Source | Purpose | Invoke |
|-------|--------|---------|--------|
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design intelligence — 50+ styles, 97 palettes, 57 font pairings, 99 UX guidelines. Use for README visual design and presentation work. | `/ui-ux-pro-max` |

**Agent skills** (installed via `npx skills@latest add`, copied to `~/.claude/skills/`):

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

## Graphify knowledge graph

A navigable knowledge graph of the full repo is maintained in `graphify-out/` and mirrored into the Obsidian vault.

**Graph location:** `graphify-out/graph.json` — 460 nodes, 683 edges, 24 communities  
**Obsidian vault:** `C:\Users\mlpgr\Writ_vault\graphify\azimuth\` — open as vault in Obsidian  
**HTML graph:** `graphify-out/graph.html` — open in browser, no server needed  
**Python interpreter:** `C:\Python313\python.exe`

### Mandatory maintenance cycle

Every structural change (new file, new pattern, template, or domain) follows this sequence in order. None of these steps are optional:

1. **Pre-implementation gate** — before writing anything, query the graph to check where the new domain lands:
   ```
   /graphify query "<new domain name>"
   ```
   Look at which community it falls into and what it connects to. Use this to make the EXTEND vs. CREATE decision with evidence, not heuristics alone.

2. **Implement** the change.

3. **Extract patterns** — run `/claudeception` to capture any non-obvious patterns from the session as reusable skills.

4. **Rebuild** — keep the graph and vault current:
   ```
   /graphify . --obsidian --obsidian-dir "C:\Users\mlpgr\Writ_vault\graphify\azimuth"
   ```

Skipping step 1 means EXTEND vs. CREATE decisions lose their evidence base. Skipping step 4 means the graph drifts from reality within a session and future pre-implementation queries return stale results.

### God nodes (best traversal entry points)

- `IC Decision Anatomy: What Investment Partners Actually Evaluate` (degree 21)
- `PE Secondaries Pre-Commitment Decision Anatomy` (degree 20)
- `Coverage Testing Program — Synthesis` (degree 18)
- `AZIMUTH Fit Assessment — PE Secondaries IC Decision` (degree 17)
- `M&A and Partnership Failure Patterns` (degree 17)
- `Module Guide Reference File` (degree 16)
- `v1.1.0 Baseline Eval Results` (degree 16)
- `Base Rates Reference` (degree 15)

**Bridge node to watch:** `Anti-Sycophancy: Confidence Inflation on Cautious Verdicts (M10)` (betweenness 0.034) — bridges Anti-Sycophancy Eval Program and Anti-Sycophancy Patterns & Diagnostics communities.

### Graph queries

**Before answering questions about module relationships, loading conditions, template routing, or skill architecture — check the graph first:**

```
/graphify query "diagnostic load triggers"
/graphify query "template routing by decision type"
/graphify query "SKILL.md module loading conditions"
```

Full integration guide: `graphify-out/OBSIDIAN_INTEGRATION.md`  
Query cheat sheet: `graphify-out/GRAPHIFY_CHEATSHEET.md`

## Environment notes (Windows)

- `jq` is not available — use `node -e` for all JSON manipulation
- `cmd /c` wrapper required for npx-based MCP servers (set in `~/.claude.json` args array as `["/c", "npx", "-y", ...]`)
- `CLAUDE_PLUGIN_ROOT` env var expansion breaks in bash — use absolute paths directly
- `~/.claude/.omc-config.json` may be emptied by hooks — always write it via the Write tool rather than shell read+patch

## What not to touch

- `.omc/` — session state, never commit
- `LICENSE` — MIT, do not modify
- `MARKETING.md` — internal strategy doc, gitignored (local only, not in public repo)
