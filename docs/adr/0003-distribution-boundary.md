# Distribution boundary: relocate the shipped skill into `azimuth/`

`npx skills add MrBinnacle/azimuth` shipped the **entire repository** to every external user — the `.claude/` dev harness (hooks, maintenance skills, agents, settings), `docs/`, `evals/`, `examples/`, `.github/`, `.out-of-scope/`, landing-page assets, and repo dotfiles — alongside the actual skill. None of that is needed at runtime; most of it is maintainer-internal process that should not be exposed.

This ADR records why the only clean fix is a directory relocation, and what was verified to rule out cheaper options.

## Diagnosis — the `skills` CLI copies the SKILL.md directory wholesale

Verified against the `skills` npm package **v1.5.9** source (`dist/cli.mjs`):

- **Discovery short-circuits at a root `SKILL.md`** (`discoverSkills`): when the repo root contains `SKILL.md`, the skill's directory *is* the repo root.
- **The clone install path** (`installSkillForAgent` → `copyDirectory`) copies that directory recursively, excluding only a hardcoded set: files `{metadata.json}`, dirs `{.git, __pycache__, __pypackages__}` (`isExcluded`). It does **not** honor `.gitignore`, there is no `.skillignore`, and `parseSkillMd` reads only `name` / `description` / `metadata` — there is **no frontmatter `files:` allowlist**.
- **The owner/repo blob path** (`tryBlobInstall`) sources its file list from `fetchSkillDownload` → `https://skills.sh/api/download/{owner}/{repo}/{slug}` — a **server-side** manifest skills.sh generates from the indexed repo tree, not a repo-committed allowlist. (Empirically, the real install pulled `.claude/`, `.github/`, and `.gitignore`, confirming the server manifest = the full tree.)
- **The `files[]` array** belongs to the `.well-known/{agent-skills,skills}/index.json` discovery format (`WellKnownProvider`), which fires only for **URL** installs (`skills add https://host/…`), never for the owner/repo form.

Conclusion: no repo-committed manifest or ignore file can restrict what an owner/repo install copies. The only lever is **what lives in the skill's directory**. Since the dev harness (`.claude/`, `.github/`) must stay at the repo root to function, the skill must move *out* of the root.

## Decision

Relocate the runtime skill into a subdirectory, **`azimuth/`**:

- Move into `azimuth/`: `SKILL.md`, `BEHAVIOR_SPEC.md`, `gotchas.md`, `references/`, `diagnostics/`, `domain-policies/` (moved as a block so SKILL.md's relative loads still resolve). Add a shipped `LICENSE` (copy; root `LICENSE` retained) and a 3-line `README.md` carrying the version marker.
- Remove the root `SKILL.md`. Discovery now walks subdirectories and resolves to `azimuth/SKILL.md`. The documented install command `npx skills add MrBinnacle/azimuth` is unchanged.
- Mark the four maintenance skills (`gap-scanner`, `reference-authoring`, `research-scout`, `verdict-auditor`) `metadata: { internal: true }` so they are removed from the default selectable set on **both** the clone and blob paths (re-admitted only under `INSTALL_INTERNAL_SKILLS=1`). Verified in source: clone `parseSkillMd` returns `null`; blob `tryBlobInstall` skips with `continue`.
- The gitignored `.claude/skills/azimuth/` install-test self-copy is uncommitted → absent from the GitHub tree and any fresh clone → non-discoverable regardless of the internal flag.

Net effect: a default install resolves to **exactly one skill (`azimuth`)** and copies **only** the pristine `azimuth/` directory.

### Lockstep wiring updates (this change set)

- `.claude/hooks/validate-azimuth.sh` — Checks 1, 2, 4 retargeted to `azimuth/SKILL.md` / `azimuth/gotchas.md`, with Rule-4 paths resolved relative to `azimuth/`.
- `docs/VALIDATION.md` — the authoritative spec updated to match (spec wins on divergence).
- `docs/MAINTENANCE.md` — distribution-boundary section added; layer-taxonomy and continuation paths re-pointed under `azimuth/`.

## Execution status (post-ADR)

| Item | Status | Notes |
|---|---|---|
| Relocate runtime into `azimuth/` | ✅ Shipped | `git mv` block move; relative loads verified resolving under `azimuth/`. |
| Maintenance skills `internal: true` | ✅ Shipped | All four; secures the default path. Footgun remains under `INSTALL_INTERNAL_SKILLS=1` (documented, accepted). |
| Hook + `VALIDATION.md` retarget | ✅ Shipped | Hook runs green against the new layout. |
| Root `README.md` | ⏸ Deferred | Restructured separately; its install-command and "What's inside" file-tree references are invalidated by this move and handled there. |
| `CLAUDE.md` topology refs | ⏸ Deferred | "Repo structure" block and validation-rationale paths now point one level up from the skill; update alongside the README restructure. |

## Alternatives rejected

- **`.skillignore` / `.gitignore` exclusion** — not honored by the CLI on the owner/repo path (verified).
- **Frontmatter `files:` allowlist** — no such mechanism exists in `parseSkillMd` (verified).
- **Delete the dev harness from the repo** — would clean the download but destroy the maintenance tooling; the maintainer explicitly wants repo dev artifacts kept.
- **Accept the bloat, document it** — ships internal process and a non-functional hook copy to every user; rejected as the default contract with end users.

## When to revisit

- The `skills` CLI gains a real ignore/manifest mechanism → a root-level skill with an exclude list could be reconsidered (likely not worth reverting once `azimuth/` is stable).
- A second shippable skill is added → promote `azimuth/` into a `skills/azimuth/` container and rely on the CLI's multi-skill subdirectory discovery.
- `INSTALL_INTERNAL_SKILLS=1` exposure becomes a real concern → consider moving maintenance skills out of the discoverable tree entirely rather than relying on the internal flag.
