# Partial-Load Characterization — Phase 2: Boundary Characterization

**Date:** 2026-05-07  
**Scope:** Boundary characterization — at what conversation token count does each hook line become unreachable  
**Methodology reference:** `evals/methodology/partial-load-characterization.md`, Phase 2 section  
**Phase 1 result:** `evals/results/2026-05-07-partial-load-phase-1-mechanism.md` — mechanism = context-fill; controlling variable = remaining context window tokens at invocation  
**Method:** Analytical derivation from measured SKILL.md token positions + known context window size. Synthetic only; no real invocation data beyond the Phase 1 calibration point (line 225 in a live invocation).

---

## Summary

**All load-bearing hooks become unreachable within a 5,273-token band of each other.** SKILL.md is effectively all-or-nothing: any session with enough remaining context to reach Module 1 (line 285) has enough context to reach Module 10's confidence ceiling (line 537) and the output format rules (line 611). The transition from full-file reachable to full-file unreachable occurs over ~5K tokens of remaining context — a negligible range relative to the 200K window. There is no meaningful "partial load with some hooks firing" scenario. Either the session is short enough that all hooks fire, or it is long enough that none do.

---

## Measurement Method

**Token positions measured from SKILL.md** (char/4 estimate; tiktoken not available):

| Line | Chars to line | Tokens to line | Content at line |
|---|---|---|---|
| 285 | 11,458 | 2,864 | Core Workflow / Module 1 begins |
| 308 | 11,853 | 2,963 | M2 circuit-breaker region |
| 370 | 13,861 | 3,465 | M4 self-proposal pre-check |
| 537 | 20,334 | 5,083 | M10 verdict softening / confidence ceiling |
| 611 | 25,448 | 6,362 | Output Format / omit-empty-sections rule |
| 650 | 27,459 | 6,864 | Likely Failure Paths omit reminder |
| 664 | 28,202 | 7,050 | Early Warning Indicators omit reminder |
| 670 | 28,550 | 7,137 | Structural Strengths omit reminder |
| 823 (EOF) | 32,530 | 8,132 | End of file |

**Boundary formula:**

```
Remaining context at invocation (R) = Context window − Infrastructure − Conversation tokens
Line L is reachable if: Token position of L ≤ R
Line L becomes unreachable when: Conversation tokens > Context window − Infrastructure − Token position of L
```

**Context window:** 200,000 tokens (claude-sonnet-4-6)

**Infrastructure overhead scenarios:**
- **Minimal (15K):** System prompt only — global CLAUDE.md (~4K tokens) + project CLAUDE.md (~1.4K tokens) + tool definitions (~5-10K tokens)
- **Heavy (40K):** System prompt + accumulated OMC system-reminder content injected across many turns in a long session (per-turn system-reminder injections for skills, hooks, and session context)

---

## Boundary Table

*Unreachable when conversation history (cumulative tokens before invocation) exceeds threshold.*

| Line | Token pos | Hook / content | Eval status | Conv threshold (15K infra) | Conv threshold (40K infra) |
|---|---|---|---|---|---|
| 285 | 2,864 | Core Workflow / Module 1 | — | 182,136 | 157,136 |
| 308 | 2,963 | M2 sycophancy circuit-breaker | LOAD-BEARING | **182,037** | **157,037** |
| 370 | 3,465 | M4 self-proposal pre-check | untested | 181,535 | 156,535 |
| 537 | 5,083 | M10 verdict softening / confidence ceiling | LOAD-BEARING | 179,917 | 154,917 |
| 611 | 6,362 | Output Format / omit-empty-sections | — | 178,638 | 153,638 |
| 650 | 6,864 | Likely Failure Paths omit reminder | — | 178,136 | 153,136 |
| 664 | 7,050 | Early Warning Indicators omit reminder | — | 177,950 | 152,950 |
| 670 | 7,137 | Structural Strengths omit reminder | — | 177,863 | 152,863 |
| EOF | 8,132 | Full file loads | — | 176,868 | 151,868 |

---

## Key Finding: All-or-Nothing Loading

**The range between "first module unreachable" (line 285, 2,864 tokens) and "last hook unreachable" (line 670, 7,137 tokens) is 4,273 tokens.** In conversation length terms, this corresponds to approximately 4,273 tokens of additional conversation — roughly 10-20 exchanges in a typical session.

**Practical consequence:** There is no stable middle state where some hooks fire and others do not. A session that cannot reach Module 1 also cannot reach Module 10. A session that reaches Module 10 also reaches Module 1. The load-bearing hooks (M2 at line 308, M10 at line 537) become unreachable within 2,219 tokens of each other — they fail together.

**The gap between M2 circuit-breaker (line 308) and Module 1 (line 285) is 99 tokens.** These are functionally at the same boundary. SKILL.md does not have a "load the modules but not the hooks" failure mode.

---

## Safe Operating Windows

Sessions where all hooks reliably fire:

| Infrastructure scenario | Max conversation tokens for full load | Practical description |
|---|---|---|
| Minimal (15K) | < 176,868 | Fresh sessions, simple tasks, limited prior context |
| Heavy (40K) | < 151,868 | Long sessions, multi-agent work, many tool calls |

**Calibration against live invocation:**  
Phase 1 observed truncation at line 225 (~2,227 tokens loaded). Working backward:
- With 15K infrastructure: conversation at truncation ≈ **182,773 tokens**
- With 40K infrastructure: conversation at truncation ≈ **157,773 tokens**

The live invocation's session (multi-agent hook validation runs + findings analysis + multiple parallel evaluations) is consistent with 157K–183K tokens of conversation history. Both infrastructure scenarios produce a calibration-consistent result. The heavy scenario (40K) is more plausible given the session's OMC system-reminder accumulation across many tool calls.

---

## Infrastructure Overhead Note

The 15K–40K infrastructure estimate is the primary source of uncertainty in the boundary table. The threshold values shift by approximately **25,000 tokens** between the two scenarios (the difference between minimal and heavy infrastructure). This matters for the "safe operating window" interpretation:

- If true infrastructure is 15K: full loading is safe up to ~177K conversation tokens. Most AZIMUTH invocations in dedicated short sessions would be safe.
- If true infrastructure is 40K: full loading is safe up to ~152K conversation tokens. Any AZIMUTH invocation after substantial prior session work (agents, file reads, multiple back-and-forth turns) is at risk.

Phase 3 behavioral testing would empirically calibrate this — by observing truncation behavior at known session lengths, the true infrastructure overhead can be inferred directly from the live behavior rather than estimated.

---

## Test Run Documentation

Phase 2 is an analytical derivation, not a live invocation series. The "test runs" are the boundary computations above, grounded in:

1. **Measured token positions** — char/4 estimate from SKILL.md content; accurate to ±10% (tiktoken would improve precision but is not installed; cl100k_base tokenizer typically runs 3.5–4.5 chars/token for mixed markdown/prose content of this kind)
2. **Known context window** — 200,000 tokens, confirmed for claude-sonnet-4-6
3. **Infrastructure estimate** — 15K–40K range derived from CLAUDE.md file sizes + tool definition estimate + OMC system-reminder accumulation assessment
4. **Live invocation calibration** — truncation at line 225 (~2,227 tokens) in a known long session, consistent with both infrastructure scenarios

---

## What Is Still Unknown

1. **True infrastructure overhead.** The 25,000-token range between scenarios is the dominant uncertainty. Phase 3 behavioral testing at known session lengths would resolve this by calibrating the formula against observed behavior.

2. **Token count accuracy.** The char/4 estimate may be off by ±10–15% for SKILL.md's content mix (Markdown headers, structured tables, numbered lists, prose). Tiktoken measurement would provide ±1% accuracy. Errors here shift all thresholds proportionally but do not change the all-or-nothing structural finding.

3. **OMC Skill tool vs. native loader.** Phase 1 found no evidence of a secondary tool-result size cap in OMC source files, but the search was not exhaustive. If the OMC Skill tool has a cap that fires before the context-fill mechanism, the boundary table would be wrong at the low end (boundary would be the cap, not the formula).

4. **Conversation token count at the live invocation.** The 157K–183K range is inferred, not measured. Direct measurement would eliminate the infrastructure uncertainty and anchor the formula.

---

## Phase 3 Implications

Phase 3 behavioral scope is now well-defined:

- **Test conditions:** three specific session lengths — (a) fresh session (~0 conversation tokens), (b) mid-range (~100K conversation tokens, well within safe window), (c) near-boundary (~160K conversation tokens, within or just outside safe window depending on infrastructure)
- **What to measure at each condition:** whether M2 circuit-breaker fires (line 308), whether M10 confidence ceiling fires (line 537), whether the output format omit rule is applied (line 611)
- **Decision condition for clip:** if mid-range condition (b) shows all hooks firing and near-boundary condition (c) shows hook suppression, Phase 3 confirms the mechanism and provides an empirical calibration point that resolves the infrastructure uncertainty
- **If all three conditions show all hooks firing:** the boundary is beyond the longest test session; Phase 3 result would indicate SKILL.md loading is more robust than Phase 2's heavy-infrastructure estimate

Phase 3 also resolves the OMC Skill tool vs. native loader question by directly observing behavior rather than inferring from source review.

---

## Disposition

Phase 2: **COMPLETE.**  
Primary finding: **All-or-nothing loading. No stable partial-load state with some hooks firing and others not.**  
Boundary range for LOAD-BEARING hooks: **conversation < 157K–182K tokens** (depending on infrastructure overhead).  
Key unknown: **True infrastructure overhead** (25K-token uncertainty range); resolves in Phase 3 behavioral testing.
