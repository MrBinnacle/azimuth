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

## Installed external skills

| Skill | Source | Purpose | Invoke |
|-------|--------|---------|--------|
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (73K stars) | UI/UX design intelligence — 50+ styles, 97 palettes, 57 font pairings, 99 UX guidelines. Use for README visual design and presentation work. | `/ui-ux-pro-max` |

Installed to `.agents/skills/ui-ux-pro-max/`, symlinked into Claude Code.

Staged research findings live in `research/staged-findings.md`. The research-scout writes there; you promote to `references/base-rates.md` via the PROMOTE mode.

## Obsidian vault

Project notes live in a local Obsidian vault under `Writ_vault/azimuth/`. Subfolders: `notes/`, `references/`, `outputs/`.

## Graphify knowledge graph

A navigable knowledge graph of the full repo is maintained in `graphify-out/` and mirrored into the Obsidian vault.

**Graph location:** `graphify-out/graph.json` — 208 nodes, 296 edges, 14 communities  
**Obsidian vault:** `C:\Users\mlpgr\Writ_vault\graphify\azimuth\` — 222 notes, open as vault in Obsidian  
**HTML graph:** `graphify-out/graph.html` — open in browser, no server needed  
**Python interpreter:** `C:\Python313\python.exe`

**Before answering questions about module relationships, loading conditions, template routing, or skill architecture — check the graph first:**

```
/graphify query "diagnostic load triggers"
/graphify query "template routing by decision type"
/graphify query "SKILL.md module loading conditions"
```

**God nodes (best traversal entry points):**
- `v1.1.0 Baseline Eval Results` (degree 19)
- `PE Secondaries IC Template` (degree 19)
- `AZIMUTH` skill (degree 17)
- `W Capital Partners` (degree 13)

**Rebuild after any significant file changes:**
```bash
/graphify . --obsidian --obsidian-dir "C:\Users\mlpgr\Writ_vault\graphify\azimuth"
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
