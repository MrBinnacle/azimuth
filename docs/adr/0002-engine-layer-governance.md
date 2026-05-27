# Engine-layer governance: declare layers, defer restructure

`VALIDATION.md` + `.claude/hooks/validate-azimuth.sh` (shipped in ADR-0001 follow-up) solved single-source-of-truth for **repo integrity**. They do not solve it for the **AZIMUTH analysis engine itself**, where behavioural spec is distributed across `SKILL.md`, `references/module-guide.md`, `references/mode-behaviors.md`, and `diagnostics/`, with no single declared contract.

This ADR records the diagnosis, declares the layer taxonomy, and defers the engine-spec work to a future session.

## Diagnosis (three structural issues)

### Issue A — `.claude/skills/` is a flat namespace mixing roles

Currently contains:
- `research-scout`, `verdict-auditor`, `gap-scanner`, `reference-authoring` (maintenance, run by humans on the repo)
- `azimuth` (install-test self-copy, now gitignored — but the directory shape doesn't prevent re-introduction)
- `ui-ux-pro-max` (plugin, public-facing tooling)

No declared separation between **runtime engine**, **maintenance**, **eval**, and **plugin** namespaces. A fork cannot tell at a glance which skill is part of AZIMUTH-the-product and which is part of AZIMUTH-the-maintenance-loop.

### Issue B — `diagnostics/` mixes safe taxonomy with sensitive override logic

The diagnostic modules (anti-sycophancy, self-advocacy, dissent-suppression) contain both:
- **Failure taxonomy** — what to call the failure mode (safe to expose; principles already in SKILL.md)
- **Behavioural overrides** — the conditions under which a verdict gets reversed or capped (sensitive; exposure creates benchmark-overfitting / prompt-exploitation surface)

Currently both live in one file per diagnostic. Cannot expose taxonomy while hiding override logic — they are not separable artifacts today.

### Issue C — `templates/` is misnamed for what it does

`templates/*-azimuth.md` encodes:
- Domain-specific decision heuristics
- Structured output schemas
- Base-rate citation cadence
- Routing-result behaviour

"Template" implies formatting. The actual contract is closer to **domain policy module**. Users (and future maintainers) read "templates" as "formatting scaffolds" and miss that they shape engine behaviour.

## The underlying root cause

AZIMUTH has **distributed governance across SKILL.md + references/ + diagnostics/ + templates/ + hooks/ + .claude/skills/** with no single declared contract that says "given mode X and domain Y, the engine MUST do A/B/C." Each artifact is partially-authoritative for its slice; none is canonically authoritative for the engine as a whole.

This is the bug class that produced the earlier hook-vs-CLAUDE.md inconsistency (resolved by VALIDATION.md). The same pattern recurs at the engine level.

## Decision

### Declared now (this ADR)

A four-layer taxonomy is adopted as AZIMUTH's contract vocabulary. Every artifact in the repo belongs to exactly one layer:

| Layer | Definition | Examples |
|---|---|---|
| **SPEC** | Authoritative, enforced contract. Deterministic. No rationale. | `VALIDATION.md`, future `BEHAVIOR_SPEC.md` |
| **RUNTIME** | Executable behaviour the engine performs. Loaded at analysis time. | `SKILL.md`, `references/`, `templates/`, `diagnostics/` (behaviour-override portions) |
| **DIAGNOSTICS** | Failure-detection taxonomy + maintenance-loop tooling. Read at maintenance time, not analysis time. | `.claude/skills/{verdict-auditor,gap-scanner,research-scout,reference-authoring}`, `diagnostics/` (taxonomy portions), `.claude/agents/azimuth-*` |
| **RATIONALE** | Why anything in SPEC/RUNTIME/DIAGNOSTICS exists. Not load-bearing for correctness. | `CLAUDE.md` (local), `docs/adr/`, `.out-of-scope/`, MEMORY entries, README, CHANGELOG |

CLAUDE.md is updated in the same commit to declare this taxonomy at the project level.

### Deferred to a future session (not done in this ADR)

1. **`BEHAVIOR_SPEC.md`** — engine-level analog of `VALIDATION.md`. Single canonical spec for what the engine MUST do per mode × domain. Source of truth that SKILL.md, references/, and templates/ each mirror.
2. **`.claude/skills/` namespace split** — separate `runtime/`, `maintenance/`, `eval/`, `meta/` (or equivalent). Resolves Issue A.
3. **Diagnostic separation** — split each diagnostic file into `taxonomy.md` (safe) + `override-logic.md` (sensitive). Decide exposure per file. Resolves Issue B.
4. **Rename `templates/` → `domain-policies/`** (or similar) and update SKILL.md Layer 3 routing. Resolves Issue C.

Each of these is a discrete architectural move requiring focused scope. Attempting them in the current session would compound risk and is rejected by the depth-over-breadth rule (`.out-of-scope/breadth-before-reliability.md`).

## What this layer does NOT decide

- Whether `BEHAVIOR_SPEC.md` should be one file or several (open: depends on whether mode and domain compose orthogonally or interact)
- Whether the namespace split should be physical (directory move) or logical (frontmatter category field)
- Whether diagnostic override-logic should be public, private, or gated by a separate skill

These are open questions for the next session.

## Why this ADR exists (not a commit message)

The diagnosis is the load-bearing artifact. The next session will re-litigate "should we restructure templates/?" unless this ADR is on the table. Capturing the diagnosis + the taxonomy + the deferred work creates the anchor.

## When to revisit

- Next eval cycle surfaces a behaviour drift traceable to spec-distribution → schedule the engine-spec work
- A proposal to add a new diagnostic, template, or reference triggers depth-gate → reuse this taxonomy in the gate's question set
- A fork or external contributor asks "what's the contract?" → this ADR is the answer until `BEHAVIOR_SPEC.md` exists
