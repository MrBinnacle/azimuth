# Partial-Load Characterization — Test Methodology

**Created:** 2026-05-07  
**Motivation:** Live invocation documented in `evals/results/2026-05-07-live-invocation-findings.md` (F6) found SKILL.md truncating at line 225 in a long conversation. All module instructions, bias externalization hooks, and the output format rules are at lines 285+. Prior hook-validation evals (`2026-05-07-v1.2.0-hook-validation.md`, `2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md`) tested with hook text present in agent context — valid for that condition. Hook efficacy under partial-load conditions is currently unanswered.  
**Constraint:** This methodology must be executed in three sequential phases. Phase 1 output determines Phase 2 scope. Phase 2 output determines Phase 3 design.

---

## Phase 1 — Mechanism Investigation

**Question:** How is SKILL.md loaded by the skill system in production? What variable controls the truncation point?

**Why this comes first:** The live invocation truncated at a fixed line (225). That suggests a deterministic mechanism — fixed byte cap, fixed token cap, or context-fill threshold — rather than stochastic compression. The fix and the test design differ depending on mechanism. If size-driven, reducing SKILL.md below the cap is the structural fix. If context-fill-driven, the truncation point moves with conversation length and the test must vary conversation length, not file size.

**What to determine:**

1. When a skill is invoked via `npx skills add` and loaded by Claude Code, is SKILL.md injected into the system prompt at session start, loaded by a file-read tool on invocation, or both?
2. Is there a documented token or byte cap on skill file loading in the Claude Code skill system?
3. Is the line-225 truncation reproducible? Test: load SKILL.md in a fresh conversation with minimal prior context. Does it load completely? Load the same SKILL.md after a long conversation. Does it truncate at the same line?
4. If the truncation point varies with conversation length, at what conversation token count does line 225 become the truncation boundary for SKILL.md at its current size (~30K chars)?

**Expected output:** A named mechanism and the variable that controls it. One of:
- Fixed cap: SKILL.md exceeds a [N]-token skill file size limit; lines past [N] are not loaded regardless of conversation state
- Context-fill: SKILL.md loads completely in fresh sessions; truncation begins when conversation context exceeds [X] tokens
- System prompt injection: SKILL.md is in the system prompt from session start; full-conversation truncation by the model's context window is the variable

**Inputs needed from prior research (check before testing):**
- Claude Code skill loading documentation or source — does it specify a file size cap?
- Any prior community reports of skill file truncation at specific sizes

---

## Phase 2 — Boundary Characterization

**Prerequisite:** Phase 1 must identify the truncation mechanism before this phase runs.

**Question:** At what input value does line N become unreachable? Produce a boundary curve.

**Lines of interest** (in order of importance):
- Line 285: Core Workflow begins (Module 1)
- Line 308: M2 sycophancy circuit-breaker (LOAD-BEARING per prior eval)
- Line 363: Module 4 interview start
- Line 370: M4 self-proposal pre-check (added v1.2.1)
- Line 413: Module 4 end / response tiering
- Line 537: Verdict taxonomy start
- Line 611: Output Format section (includes "omit empty sections" non-negotiable)
- Line 650: Likely Failure Paths inline omit reminder (added v1.2.1)
- Line 664: Early Warning Indicators inline omit reminder (added v1.2.1)
- Line 670: Structural Strengths inline omit reminder (added v1.2.1)
- Line 731: Anti-Slop Rules
- Line 775: Escalation logic (caution bias)

**Test design (if fixed-cap mechanism):**
- Vary SKILL.md size by inserting or removing content in non-critical sections
- Measure: at what size does each line of interest become unreachable?
- Produce: minimum SKILL.md size that keeps all load-bearing hooks reachable

**Test design (if context-fill mechanism):**
- Fix SKILL.md at current size
- Vary conversation length (0 tokens, 5K tokens, 10K tokens, 20K tokens, etc.)
- Measure: at what conversation token count does each line of interest become unreachable?
- Produce: maximum conversation length at which all load-bearing hooks are reachable

**Expected output:** A boundary table:

| Line | Content | Reachable at [input X]? | Boundary value |
|---|---|---|---|
| 285 | Module 1 start | [Y/N] | [threshold] |
| 308 | M2 circuit-breaker | [Y/N] | [threshold] |
| 370 | M4 self-proposal pre-check | [Y/N] | [threshold] |
| 537 | Verdict taxonomy | [Y/N] | [threshold] |
| 611 | Output format / omit rule | [Y/N] | [threshold] |

---

## Phase 3 — Behavioral Validation

**Prerequisite:** Phase 2 must establish the boundary before this phase runs.

**Question:** Do load-bearing hooks fire under realistic deployment conditions (at the boundary identified in Phase 2)?

**Test conditions:**
- Above-boundary: SKILL.md loaded completely (baseline, replicates prior eval conditions)
- At-boundary: SKILL.md loaded to the point where load-bearing hooks are marginally reachable
- Below-boundary: SKILL.md truncated before load-bearing hooks (replicates the live invocation condition)

**Hooks to test** (in priority order):
1. M2 sycophancy circuit-breaker (line 308) — assessed LOAD-BEARING in prior eval; most important to characterize under partial load
2. M10 confidence ceiling (in Module 10 pre-verdict check) — assessed LOAD-BEARING in prior eval
3. M4 self-proposal pre-check (line 370) — new in v1.2.1; untested under any condition

**Test design:** Replicate the adversarial inputs from the prior hook-validation evals. Run production condition (hook text present in full SKILL.md) and below-boundary condition (SKILL.md truncated before hook). Compare behavioral deltas.

**Expected output:** For each hook:
- Under full load: LOAD-BEARING / LABELING-ONLY assessment (should replicate prior eval)
- Under partial load: behavioral delta observed / no delta observed
- Combined assessment: does load-bearing status hold under realistic deployment conditions?

---

## Decision Gate

**Before committing Phase 3 results to claims about production behavior:**

Phase 3 results answer: "do the hooks fire when SKILL.md is loaded as a file under realistic partial-load conditions." Phase 1 and 2 must be complete for Phase 3 results to be interpretable. A Phase 3 result without Phase 1 mechanism identification cannot be generalized.

**Implication for external claims:**

Claims that AZIMUTH's hooks fire in production (README, CHANGELOG, Reddit submissions, awesome-claude-code) should be held until Phase 3 is complete and confirms the hooks are reachable under production conditions.

Current eval status: hooks validated under inline-text condition only. Production deployment behavior uncharacterized.

---

## Relationship to Prior Evals

Prior evals (`2026-05-07-v1.2.0-hook-validation.md`, `2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md`) are not invalidated by this methodology. They correctly test hook behavior when hook text is present in agent context. Their findings are valid for:

- Determining whether a hook is structurally necessary (LOAD-BEARING vs. LABELING-ONLY)
- Validating the specific text of a hook

They are not valid for:

- Claiming hooks fire in production when SKILL.md is loaded from file in a long conversation
- Characterizing production deployment behavior

This methodology fills the gap between "hook is load-bearing when present" and "hook reaches the analyst in production."
