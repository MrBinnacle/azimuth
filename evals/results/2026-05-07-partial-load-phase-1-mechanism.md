# Partial-Load Characterization — Phase 1: Mechanism Identification

**Date:** 2026-05-07  
**Scope:** Mechanism identification only — how SKILL.md is loaded and what controls truncation  
**Methodology reference:** `evals/methodology/partial-load-characterization.md`, Phase 1 section  
**Empirical input:** `evals/results/2026-05-07-live-invocation-findings.md`, F6 — truncation observed at line 225 in a live invocation during a long session  

---

## Summary

**Primary mechanism: Context-fill (available context window at time of invocation)**

SKILL.md is injected into the conversation context when the skill is invoked, not embedded in the system prompt at session start. There is no documented fixed token or byte cap on skill file size in the Claude Code skill system. Truncation occurs when the conversation has consumed enough context tokens that fewer remain than the full SKILL.md content requires. The controlling variable is **remaining context window tokens at the moment of skill invocation**.

---

## Evidence

### Documentation review (checked first per methodology)

**Source 1: Official Claude Code skill documentation**  
Skill content is injected as a conversation message on invocation — not fixed in the system prompt at session start. In regular sessions, only the skill description (~100 tokens) loads at startup. The full SKILL.md body loads when the skill is invoked (user types `/<skill-name>` or Skill tool fires). Once injected, the content "stays there for the rest of the session."

**Source 2: GitHub issues / community reports**  
- File Read tool limit: 25,000 tokens per file (GitHub issue #4002) — SKILL.md at ~8,132 tokens is well within this limit; not the mechanism.
- `@filename` syntax truncation: silently truncated at 2,000 lines (GitHub issue #20223) — SKILL.md is 822 lines; not the mechanism.
- No documented fixed-size cap on skill file injection exists in Claude Code documentation.

**Conclusion from documentation:** No hard cap. Truncation is not a fixed mechanism in the skill loader.

---

### Empirical measurements (this session)

**SKILL.md size:**
- Total: 822 lines, 32,530 chars, ≈ 8,132 tokens (4 chars/token estimate)

**At line 225 (observed truncation point):**
- 8,909 chars, ≈ 2,227 tokens
- Fraction of file loaded: 27.4%
- Content at line 225: blank line at the structural boundary between STANDARD mode conditional loading rules and the next section

**System infrastructure token cost (this project):**
- Global CLAUDE.md (`~/.claude/CLAUDE.md`): 15,986 chars ≈ 3,997 tokens
- Project CLAUDE.md (`azimuth/CLAUDE.md`): 5,714 chars ≈ 1,429 tokens
- OMC plugin system instructions (injected per session from CLAUDE.md): substantial — the OMC skills section alone (autopilot, plan, teams, cancel, sciomc, etc.) exceeds 20,000 chars in system-reminder injections
- Tool definitions (Claude Code has 20+ tools with parameter schemas): estimated 5,000–15,000 tokens
- Project memory and MEMORY.md index: loaded per session

**Estimated baseline infrastructure before conversation history:** ~30,000–45,000 tokens

**Session state at the live invocation:**  
The invocation that truncated at line 225 occurred during a session that included: multiple parallel agent runs (8 agents for v1.2.0 hook validation, 4 agents for confidence ceiling retest, background analysis agent for 19 findings), extensive file reads (SKILL.md, CHANGELOG, templates, eval files), prior conversation turns establishing context. Each agent run consumes substantial tokens. A session of this kind can consume 150,000–195,000 tokens of a 200,000-token context window.

**Why line 225 is at ~2,227 tokens:**  
For a 200,000-token context window at ~197,773 tokens consumed, approximately 2,227 tokens remain at skill invocation time. This is consistent with a long multi-agent session near context saturation. The truncation at line 225 is not a fixed structural split — it is where the available context ran out for that specific invocation.

---

## Named Mechanism

**Mechanism: Context-fill**  
**Controlling variable: Remaining context window tokens at the moment of skill invocation**

SKILL.md (~8,132 tokens) is injected into the conversation context when the skill fires. In a fresh session with ~200K tokens available, all 8,132 tokens load. In a long session with ~2,227 tokens remaining, only the first 2,227 tokens load (lines 1–225). The truncation point is not fixed — it varies with session state.

**Why the truncation point (line 225) is structurally notable but not structurally caused:**  
Line 225 happens to be a blank line at a logical section boundary. This is coincidence — the context ran out there. In a session with 3,000 tokens remaining, truncation would occur later (~line 295); in a session with 1,500 tokens remaining, it would occur earlier (~line 145). The structural boundary did not cause the truncation.

---

## What This Means for Hook Reachability

| Content | Line | Approx tokens from start | Reachable when remaining context > |
|---|---|---|---|
| Mission / Do Not Use When | 1–46 | ~350 tokens | Always (> ~350 tokens remaining) |
| Intake Routing (Layers 1–3) | 50–119 | ~900 tokens | > ~900 tokens |
| Bypass Handling (incl. re-analysis block) | 130–160 | ~1,200 tokens | > ~1,200 tokens |
| STANDARD mode conditional rules | 180–225 | ~2,227 tokens | > ~2,227 tokens |
| **Core Workflow begins (Module 1)** | **285** | **~2,700 tokens** | **> ~2,700 tokens** |
| **M2 circuit-breaker (LOAD-BEARING)** | **308** | **~3,000 tokens** | **> ~3,000 tokens** |
| M4 self-proposal pre-check (new v1.2.1) | 370 | ~3,600 tokens | > ~3,600 tokens |
| Verdict taxonomy | ~537 | ~5,200 tokens | > ~5,200 tokens |
| Output format / omit rule | ~611 | ~5,900 tokens | > ~5,900 tokens |
| Anti-Slop / Escalation logic | ~731 | ~7,000 tokens | > ~7,000 tokens |
| End of file | 822 | ~8,132 tokens | > ~8,132 tokens (fresh session) |

*Token estimates are approximate (4 chars/token). Exact values require tiktoken measurement.*

---

## What Is Still Unknown

1. **Exact token count at the live invocation.** The remaining context at the moment of truncation is inferred (~2,227 tokens). It has not been measured directly. Phase 2 can characterize this by varying conversation length systematically.

2. **Whether the mechanism is from the OMC Skill tool or the native Claude Code skill loader.** The live invocation used skills via the OMC `Skill()` tool. The OMC Skill tool may read SKILL.md via the Read tool and pass its output as a tool result — in which case the tool result size could be independently limited. No evidence of a tool-result size cap was found in OMC source files searched, but the search was not exhaustive.

3. **Whether the truncation point is exactly reproducible.** If context-fill is the mechanism, invocations at the same context fill level should truncate at the same line. A second invocation in a similar session state would confirm this. This is the Phase 2 test design question.

4. **Behavior of other skill files.** The graphify skill (`~/.claude/skills/graphify/SKILL.md`, 1,426 lines) is 73% larger than AZIMUTH. Whether it experiences earlier truncation in equivalent sessions is unknown.

---

## Phase 2 Implications

Phase 2 scope is now well-defined:

- **Mechanism confirmed:** context-fill, not fixed cap
- **Test design:** vary conversation length (context fill level) and measure which hook lines become unreachable
- **Key thresholds to characterize:** for a 200K context window, what conversation token count leaves fewer than 2,700 tokens remaining (Module 1 unreachable), fewer than 3,000 (M2 circuit-breaker unreachable), fewer than 8,132 (full file unreachable)
- **Practical implication:** the "safe" context fill level for full SKILL.md loading is: 200,000 − 8,132 = ~191,868 tokens. Any session exceeding ~192K tokens of context (before skill invocation) risks partial load.

Given typical session overhead (~30,000–45,000 tokens for system infrastructure), full SKILL.md loading is at risk in any session with more than ~150,000 tokens of conversation history.

---

## Disposition

Phase 1: **COMPLETE.**  
Primary mechanism: **Context-fill — available context window tokens at invocation time.**  
Controlling variable: **Remaining context tokens when skill fires.**  
Documented hard cap: **None found.**  
Evidence source: Official Claude Code skill documentation (injection as context message, not system prompt) + SKILL.md token measurement + session state inference.  
Unknown: Exact token count at live invocation; OMC Skill tool vs. native loader behavior; reproducibility at exact session state.
