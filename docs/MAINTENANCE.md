# AZIMUTH Maintenance Orchestration

Single operational document describing how AZIMUTH is maintained and evolved. Read this before authoring a migration, refactor, or any structural change. Pairs with [`docs/adr/0001-bespoke-orchestration-layer.md`](adr/0001-bespoke-orchestration-layer.md) (structural decisions), [`docs/adr/0002-engine-layer-governance.md`](adr/0002-engine-layer-governance.md) (layer taxonomy), and [`docs/adr/0003-distribution-boundary.md`](adr/0003-distribution-boundary.md) (distribution topology).

This file is operational. ADRs are decisional. CLAUDE.md is maintainer-local context. The three are co-authoritative; if any conflict, fix the conflict explicitly rather than letting them drift.

---

## Distribution boundary (what ships vs. what stays)

`npx skills add MrBinnacle/azimuth` copies the **directory that contains the discovered `SKILL.md`** — nothing more, nothing less. The `skills` CLI has no `.gitignore` / `.skillignore` / manifest-based exclusion; it copies that directory tree minus only `.git`, `__pycache__`, and `__pypackages__`. The repo is therefore split into two zones:

- **Shipped skill — `azimuth/`.** The only directory an external user receives: `SKILL.md`, `BEHAVIOR_SPEC.md`, `gotchas.md`, `references/`, `diagnostics/`, `domain-policies/`, plus a shipped `LICENSE` and a 3-line `README.md` carrying the version marker. Keep this directory pristine — anything added here ships verbatim to every installer.
- **Repo-internal — everything at the repo root.** `.claude/` (dev harness: hooks, maintenance skills, agents, settings), `docs/`, `evals/`, `examples/`, `.github/`, `.out-of-scope/`, the root `README.md` / `CHANGELOG.md` / `LICENSE`, and landing-page assets. These live at the root to function and are never copied into the installed skill, because the skill now lives one level down in `azimuth/`.

Two guarantees keep a default install resolving to exactly one skill (`azimuth`):

1. **No root `SKILL.md`.** With no root skill to short-circuit on, discovery walks subdirectories and resolves to `azimuth/SKILL.md`.
2. **The four maintenance skills carry `metadata: { internal: true }`.** This removes them from the default selectable set on both the clone and blob install paths; they are installable only under `INSTALL_INTERNAL_SKILLS=1`. The gitignored `.claude/skills/azimuth/` install-test self-copy is uncommitted, so it is absent from the GitHub tree and from any fresh clone — non-discoverable regardless of the internal flag.

See [`docs/adr/0003-distribution-boundary.md`](adr/0003-distribution-boundary.md) for the full decision, the source-level verification of the `skills` CLI behaviour, and the rejected alternatives.

---

## Layer taxonomy quick reference

Per ADR-0002, every artifact belongs to exactly one layer:

| Layer | Authority | Examples |
|---|---|---|
| **SPEC** | Enforced contract; deterministic; no rationale | `docs/VALIDATION.md`, `azimuth/BEHAVIOR_SPEC.md` |
| **RUNTIME** | Engine behaviour at analysis time | `azimuth/SKILL.md`, `azimuth/references/`, `azimuth/domain-policies/`, `azimuth/diagnostics/` (override portions) |
| **DIAGNOSTICS** | Failure detection + maintenance tooling | `.claude/skills/maintenance/`, `.claude/agents/`, `azimuth/diagnostics/` (taxonomy portions) |
| **RATIONALE** | Why the others exist; not load-bearing | `CLAUDE.md`, `docs/adr/`, `.out-of-scope/`, README, CHANGELOG, this file |

A change crossing layer boundaries (e.g., a SPEC rule that demands a new RUNTIME file) MUST update both layers in the same commit set, with the SPEC commit landing first (or atomically) so RUNTIME never references a rule that doesn't exist.

### The SKILL.md ↔ BEHAVIOR_SPEC.md mirror invariant (load-bearing)

`BEHAVIOR_SPEC.md` is the SPEC layer (single decision authority). `SKILL.md` is the RUNTIME mirror — the always-loaded entry point the model reads on every invocation.

**Every load-bearing engine rule MUST exist in both files**, with `SKILL.md` carrying the full text inline (not just rule names or pointers to the spec). This is non-negotiable. The reason is empirically established: load-bearing rules that only exist in a separately-loaded file (such as `BEHAVIOR_SPEC.md` or a `references/*.md` file) fail to survive partial-load conditions in long sessions (≥150K–177K tokens of history), where the model may load `SKILL.md` but not the spec. See `CHANGELOG.md` v1.4.0 entry: *"Previously, 0 of 5 load-bearing behavioral rules survived partial load; now 5 of 5 are reliable."*

The five rules that MUST stay inline in `SKILL.md`:

1. **M4 PRE-CHECK** — self-advocacy audit
2. **M2 circuit-breaker** — sycophancy
3. **M10 confidence ceiling** — UNSUPPORTED load-bearing → MEDIUM
4. **M1 commitment inference** — RESIDUAL-RISK-REGISTER routing
5. **Output lead rule** — first 3 lines = verdict / decision / confidence

Additional runtime essentials that MUST stay inline in `SKILL.md`:
- Intake routing consequents (Layer 1 A–E mappings; Layer 2 stakes-to-mode mapping; Layer 3 domain-to-policy paths)
- Mode selection triggers + phrasing-vs-stakes tiebreaker
- 9-verdict trigger conditions
- Reference-loading matrix (per-mode load directives + conditional load triggers)

When updating any of the above:
1. Edit `BEHAVIOR_SPEC.md` (canonical) first.
2. Mirror the change in `SKILL.md` in the same commit set.
3. The mirror invariant is stated in both files' preambles. If they diverge, the spec is authoritative — but the spec is useless to the runtime if the runtime doesn't carry the rule. **Spec without mirror = silent regression.**

---

## Verification layers

Three verification scopes catch different drift classes. Each runs at its named time only.

### 1. Commit-time — `.claude/hooks/validate-azimuth.sh`

Enforces the four `docs/VALIDATION.md` repo-integrity rules as a PreToolUse hook on `git commit`:

| Rule | What it catches |
|---|---|
| Rule 1 — description = 489 chars | Drift in `azimuth/SKILL.md` frontmatter that breaks the `npx skills add` install warning |
| Rule 2 — gotchas.md = 8 sections | Structural drift in the `azimuth/gotchas.md` catalog |
| Rule 3 — no `precommitment` typo | Vocabulary discipline (the canonical term is `pre-commitment`) |
| Rule 4 — SKILL.md paths exist | `azimuth/SKILL.md` conditional-load architecture integrity (paths resolved relative to `azimuth/`) |

Bypass: `git commit --no-verify` when intentional. Every bypass MUST leave a CHANGELOG[Unreleased] note explaining why.

If the hook ever diverges from `docs/VALIDATION.md`, **the spec is authoritative — fix the hook**.

### 2. Audit-time — `.claude/skills/maintenance/`

Four maintenance skills run on operator request (no automation). Each is mapped to one failure mode:

| Skill | Failure mode | Invoke |
|---|---|---|
| `research-scout` | Source-citation staleness (8 primary families drift) | "run the research scout" / "promote staged findings" |
| `verdict-auditor` | Output drift / confidence inflation on cautious verdicts | "audit this output" (paste output first) |
| `gap-scanner` | Coverage-claim vs reality drift between SKILL.md and the files it claims to load | "run the gap scanner" |
| `reference-authoring` | EXTEND-vs-CREATE drift when adding a new reference or domain-policy file | When authoring a new reference / domain-policy |

These are not invoked on a schedule. They are invoked when a structural change is contemplated (reference-authoring), when a new release is being prepared (gap-scanner), when a real output looks suspicious (verdict-auditor), or when the citation literature has shifted (research-scout).

Two additional gate skills (`depth-gate`, `calibration-check`) are designed but **deliberately not built** — they wait on the first observed recurrence of the failure they would prevent. See ADR-0001.

### 3. Release-time — manual checklist (codified in `CLAUDE.md` Release Process)

For each `vMAJOR.MINOR.PATCH` release:

1. Run all four `docs/VALIDATION.md` checks via the hook (any `git commit` exercises them).
2. `git add` only the changed files. Never `git add -A` near `.omc/` or staging artifacts.
3. `git tag -a vX.Y.Z -m "..."` and push both master and the tag.
4. `gh release create` using the CHANGELOG entry as release notes.
5. Verify install from a clean shell:
   ```
   npx skills add https://github.com/MrBinnacle/azimuth --skill azimuth -a claude-code -y
   ```
6. Optional but recommended: invoke `gap-scanner` once and confirm no new gaps appeared since the prior release.

If step 5 fails, **block the release** — install correctness is the load-bearing contract with end users.

---

## Subagent dispatch invariants

Two `.claude/agents/` subagents are available. Both are read-only, role-bound, and dispatched by the main agent — they MUST NOT modify the skill or the output they audit.

| Subagent | Role | Dispatch when |
|---|---|---|
| `azimuth-evidence-checker` | Audits a proposed numeric heuristic, threshold, cap, or empirical claim destined for SKILL.md or a reference file against existing evidence base | Before introducing any new threshold, cap, or numeric claim — returns "citation found", "[uncalibrated] tag warranted", or "contradicting evidence" |
| `azimuth-output-auditor` | Stress-tests a pasted AZIMUTH analysis output against the skill's own structural rules | After a real AZIMUTH verdict is produced and adversarial review is wanted — checks for sycophancy, confidence inflation on cautious verdicts, output-discipline failures, hook-rule violations |

Invariants for both:
- READ-ONLY. Neither modifies the skill, the output, or any committed artifact.
- Role-bound. Do not repurpose for general code review; the gain is the focused checklist.
- Decision returns to the main agent. The subagent reports; the main agent decides.

For broader-context subagent work (research, breadth-first audits, parallel investigation), use the global `general-purpose` or `Explore` agents per `~/.claude/CLAUDE.md` §4 Subagent Protocol.

---

## Migration / rollback discipline

Pure-markdown repo, so rollback is conceptually `git revert`. Discipline ensures any single commit is independently revertable.

### Commit scoping

| Type | Scope | Examples |
|---|---|---|
| `feat` | `skill` / `meta` | new spec rule; new maintenance affordance |
| `fix` | `skill` / `meta` | drift correction; broken path |
| `refactor` | `skill` / `meta` | structure change; rename |
| `docs` | `meta` / `adr` | README, CHANGELOG, ADRs, this file |
| `chore` | `meta` / `skill` | gitignore, cleanup, dep removals |

Always: `type(scope): description`.

Never:
- Bundle a SPEC change with the runtime updates it implies — separate commits with the SPEC commit landing first.
- Use `--amend` after a commit lands in this branch. Create a new commit; reference the prior one in the message. Per `~/.claude/CLAUDE.md` global rules, amends are only acceptable when the user explicitly requests them.
- Squash spec + runtime commits at merge. Preserve the SPEC→RUNTIME causal chain in the log.

### Path renames (git mv)

When renaming a directory or file:

1. `git mv old new` — captures the rename in history so `git log --follow` works.
2. In the SAME commit, update every internal reference to `old` (use Grep across the tree).
3. Pre-commit verification: `validate-azimuth.sh` runs Rule 4 against `SKILL.md`; check the hook didn't catch a missed path.
4. Post-commit verification: `git log --diff-filter=R --stat` confirms only renames + the path-reference deltas.

If you discover after committing that a reference was missed, do NOT amend. Land a follow-up commit titled `fix: <thing> path-reference updates (follow-up to <hash>)` with the missed reference. See commit `e2dc72a` for the canonical pattern.

### Cross-layer commits

If a single change crosses layer boundaries (e.g., adding a new domain to BEHAVIOR_SPEC.md §1.3 RULE-1.x requires creating `domain-policies/new-azimuth.md`):

1. Commit SPEC first.
2. Commit RUNTIME implementing the spec rule.
3. Commit RATIONALE updates last (CLAUDE.md / README / ADR).

This order ensures any `git checkout` between the commits has a consistent state for the layer at that point.

---

## Drift vectors (identified and bounded)

Each row below is a drift class AZIMUTH is exposed to, with the mechanism that detects/bounds it. If a new drift class appears that isn't on this list, add it before authoring a fix.

| Drift class | Mechanism that bounds it |
|---|---|
| SKILL.md description char-count drift | `docs/VALIDATION.md` Rule 1 + commit-time hook |
| gotchas.md section-count drift | `docs/VALIDATION.md` Rule 2 + commit-time hook |
| Vocabulary drift (`precommitment` typo) | `docs/VALIDATION.md` Rule 3 + commit-time hook |
| SKILL.md → file path drift | `docs/VALIDATION.md` Rule 4 + commit-time hook |
| SPEC vs RUNTIME divergence | ADR-0002 layer taxonomy + "spec is authoritative" rule in each layer's preamble |
| Load-bearing rule fails to survive partial load (long sessions) | The SKILL.md ↔ BEHAVIOR_SPEC.md mirror invariant above — load-bearing rules MUST be inline in SKILL.md, not pointer-only. Empirically established by v1.4.0's eval (0/5 → 5/5 survival). Drift from this invariant = silent regression; no mechanical guard catches it. Audit before any release that touches SKILL.md structure. |
| Source-citation staleness | `research-scout` at audit time, manual cadence |
| Coverage-claim vs reality drift | `gap-scanner` at audit time, before each release |
| Output-discipline drift on cautious verdicts | `verdict-auditor` at audit time + `azimuth-output-auditor` subagent at dispatch time |
| EXTEND-vs-CREATE drift when adding reference / domain-policy | `reference-authoring` skill at author time |
| Uncalibrated numeric claims | `azimuth-evidence-checker` subagent at dispatch time |
| Description / file-tree drift between repo state and README/CLAUDE.md | No mechanical guard — audited manually before each release (this doc captures the audit checklist) |
| ADR state drift (ADR text vs. live tree) | No mechanical guard — addressed by Execution-status footers in ADRs; review before each release |
| Speculative-namespace creep (empty `runtime/`, `eval/`, `plugin/` etc.) | Discipline: only create a namespace when an occupant exists. See ADR-0002 Execution-status row for Item 2 |
| Cross-layer authority leakage (e.g., domain-policy redefining a spec verdict) | BEHAVIOR_SPEC.md §8 Domain-Policy Gating Contract (RULE-8.4..RULE-8.8) |

The unguarded drift classes (rows with "audited manually") are the highest-priority candidates for future mechanical guards if recurrence is observed. Do not author such guards speculatively — wait for an observed instance, per the `depth-over-breadth` rule.

---

## Next-session continuation

If a new session opens with no context beyond the repo:

1. **Read this file first.** It is the operational anchor.
2. Read [`SKILL.md`](../azimuth/SKILL.md) and [`BEHAVIOR_SPEC.md`](../azimuth/BEHAVIOR_SPEC.md) — the public-facing skill surface + canonical engine spec.
3. Read [`CLAUDE.md`](../CLAUDE.md) — maintainer-local context (validation rationale, environment notes, Obsidian / graphify integration).
4. Read [`docs/adr/0001-bespoke-orchestration-layer.md`](adr/0001-bespoke-orchestration-layer.md) and [`docs/adr/0002-engine-layer-governance.md`](adr/0002-engine-layer-governance.md) — structural decisions that govern any new proposal.
5. Run `git log --oneline -20` to surface what's changed recently. Each commit's message is scoped to one decision; the message body explains the why.
6. Run `.claude/hooks/validate-azimuth.sh` (empty stdin) to confirm the four repo-integrity rules pass before any work.

If a proposal would extend or modify the engine:

- New rule? → BEHAVIOR_SPEC.md (the rule), then RUNTIME files that implement it.
- New domain-policy? → BEHAVIOR_SPEC.md §1.3 (route rule), then `domain-policies/X-azimuth.md` (configuration), per `reference-authoring` discipline.
- New reference? → `reference-authoring` skill first (EXTEND-vs-CREATE), then the file.
- New diagnostic? → Confirm it's strictly observational (no rule consequents); decision authority lives in BEHAVIOR_SPEC.md.
- New threshold or empirical claim? → `azimuth-evidence-checker` first; tag `[uncalibrated]` if no citation.
- New maintenance / governance skill? → ADR-0001 trigger check (was the failure mode observed?); if no, do not author.

---

## When this doc is wrong

This is operational documentation. If repo state contradicts what's written here:

1. Verify against the repo, not this doc.
2. Update this doc to match repo state in the same commit set as whatever changed the repo.
3. Note the structural-decision implications in CHANGELOG[Unreleased].

If the repo state itself violates a layer-taxonomy invariant (e.g., a domain-policy defines a new verdict, a diagnostic file caps confidence), **fix the repo** — this doc is descriptive of intent, not corrective. Use the audit-time skill stack and the relevant ADR to scope the fix.
