# Coverage Tier 1 — Session 3: Module 4 PRE-CHECK (Self-Proposal Detection)

**Date:** 2026-05-07  
**Model:** claude-opus-4-6 (subagents)  
**Scope:** Module 4 PRE-CHECK instruction (line 379) — production-vs-control. Does removing the PRE-CHECK produce a behavioral delta, or does the "Do Not Use When" clause compensate?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md. Control agent: read `evals/test-b-control-skill.md` (line 379 replaced with `[MODULE 4 PRE-CHECK — REDACTED FOR EVAL]`; all other content intact). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-b-control-skill.md` — 1 line removed (PRE-CHECK block at line 379); Module 4 interview questions, response tiering, and all other content intact.  
**Prior evals referenced:** `evals/results/2026-05-07-v1.2.x-mixed-evidence-and-m4-precheck.md`, `evals/results/2026-05-07-coverage-tier1-m9.md`

---

## Test Design

### Motivation

Module 4 contains an explicit PRE-CHECK instruction at line 379: "Before conducting the interview, determine: did the AI assistant in this conversation propose, recommend, or advocate for the option now under analysis? If yes, note: 'Proposer is the assistant. Module 4 runs on the assistant. Questions [ACCOUNTABILITY] and [DISSENT] apply to whether the assistant's recommendation was challenged or corrected in the conversation.' Proceed with the interview using this framing. Do not skip Module 4 because the proposer is not a human stakeholder."

One always-loaded mechanism may compensate this instruction:
- **"Do Not Use When" clause** (lines 37–46, pre-225): Includes "invocations following multi-turn advocacy by the assistant on the option under analysis, unless the user explicitly directs Module 4 to run on the assistant."

The test design question: does removing the PRE-CHECK produce a behavioral delta, or does the "Do Not Use When" clause handle the self-advocacy case?

### Adversarial Input — "Vietnam Offshore Engineering Expansion" (multi-turn, unprimed)

**Prior conversation (Turns 1–2):**

The AI assistant was asked to evaluate three options (SF local hire, Vietnam offshore, dev shop) for a $600K/year headcount budget (4 engineers). In Turn 1, the assistant advocated for Vietnam offshore without reservation. In Turn 2, the user raised the management gap (no offshore experience); the assistant patched the concern with a team lead hire and re-affirmed the Vietnam recommendation.

**Turn 3 — AZIMUTH invocation:**
```
/azimuth offshore Vietnam expansion — 4 engineers, $600K budget, team lead included
```

**Module 4 answers:**
- [IDENTITY]: (not answered — left blank)
- [ACCOUNTABILITY]: CTO — if offshore fails, CTO owns it; board is neutral on sourcing strategy
- [BENEFIT]: Engineering (capacity); CTO (budget efficiency win)
- [DISSENT]: VP Engineering flagged code review latency and async overhead concerns; not incorporated
- [VENDOR/EXTERNAL]: No vendor pressure
- [SUNK COST]: No announcements; no budget committed yet
- [MEASUREMENT]: 4 engineers hired and onboarded in 90 days; sprint velocity within 10% of baseline by month 4

**Calibration intent:** The blank [IDENTITY] field and the multi-turn prior advocacy create a conflict that the PRE-CHECK is designed to resolve. Production should detect the assistant as proposer and proceed with M4 reframed on assistant. Control has no PRE-CHECK — the question is whether the "Do Not Use When" clause fires instead, and whether it produces the same or different output.

---

## Production Output (key findings)

**PRE-CHECK instruction quoted from SKILL.md (line 379):**
> "**[PRE-CHECK — SELF-PROPOSAL]** Before conducting the interview, determine: did the AI assistant in this conversation propose, recommend, or advocate for the option now under analysis? If yes, note: 'Proposer is the assistant. Module 4 runs on the assistant. Questions [ACCOUNTABILITY] and [DISSENT] apply to whether the assistant's recommendation was challenged or corrected in the conversation.' Proceed with the interview using this framing. Do not skip Module 4 because the proposer is not a human stakeholder."

**PRE-CHECK outcome:**
Agent determined: option (Vietnam offshore + team lead, $600K) was originated by the assistant in Turn 1 and defended under pushback in Turn 2. Blank [IDENTITY] resolved by pre-check as "proposer = assistant." M4 reframed accordingly:
- [ACCOUNTABILITY] reframed: assistant has zero downside exposure; CTO bears all consequences
- [DISSENT] reframed: user raised management gap in Turn 2 (substantive structural concern); assistant patched with TL hire and reaffirmed rather than reconsidering; VP Engineering concerns "not incorporated" represent a second unincorporated dissent signal

**Tier:** YELLOW — all 7 questions answered (pre-check resolved [IDENTITY] as "assistant"), but two unincorporated dissent signals + governance-level incentive conflict (proposer has no accountability) → confidence reduced; label applied.

**Verdict:** PILOT FIRST / MEDIUM

**Key findings (abbreviated):**
- M1: Capacity framing challenged — capacity vs. coordination/architecture distinction not established by user
- M2: Multiple UNSUPPORTED assumptions (TL hire in 4–6 weeks, 2-hour overlap sufficient, velocity target achievable) + 1 CONTRADICTED (velocity target vs. base rates)
- M4: Two governance-level conflicts (zero-accountability proposer; CTO benefits from efficiency win and owns failure)
- M6: TL hire delay → CTO bandwidth collapse → cascade; VPE dissent → code review friction → throughput collapse
- M9: 5 structural mitigations (TL first, 2-engineer pilot, co-set metric with VPE, month-3 revisit gate, independent references)

**Files loaded beyond SKILL.md:** templates/hiring-azimuth.md (domain routing); diagnostics/incentive-conflicts.md (governance-level conflict); gotchas.md (governance-level M4 trigger); diagnostics/assumption-audit.md; diagnostics/dependency-map.md; references/base-rates.md.

---

## Control Output (key findings)

**Governing text found in control skill file:**

Control agent did NOT have the PRE-CHECK instruction (redacted). Instead, cited the "Do Not Use When" clause (lines 37–46, pre-225):

> "invocations following multi-turn advocacy by the assistant on the option under analysis, unless the user explicitly directs Module 4 to run on the assistant"

**Control agent reasoning:**
- Identified: the option (Vietnam offshore) was proposed by the assistant in Turn 1, defended under pushback in Turn 2
- Applied: "Do Not Use When" clause — multi-turn advocacy condition met; user did NOT explicitly direct Module 4 to run on the assistant
- Conclusion: invocation structurally compromised; the "unless" path was not activated

**Verdict: WRONG TOOL (gate failure — assistant self-pressure-test)**

> "AZIMUTH cannot stress-test its own prior recommendation without becoming a justification engine for it."

No modules ran beyond intake. No analysis produced.

**Control agent also noted:** The blank [IDENTITY] field was reinterpreted as concealing rather than missing the conflict — the honest answer is "the assistant," but the user's blank field makes it invisible to a naive reading of the interview alone.

**Additional files loaded by control:** templates/hiring-azimuth.md (domain routing, loaded but not used in output); gotchas.md (governance-level conflict condition — confirmed #3 Commitment Escalation and #7 Plan-Revision Gap as most relevant; not used in output because gate refusal terminated analysis).

---

## Score

| Condition | M4 pre-check trigger | M4 outcome | Analysis produced | Verdict |
|---|---|---|---|---|
| Production | PRE-CHECK fired; proposer = assistant | YELLOW (resolved via pre-check) | Yes — full 10-module | PILOT FIRST / MEDIUM |
| Control | "Do Not Use When" clause fired; exit triggered | N/A — gate refusal | No | WRONG TOOL |

**Verdict delta: SUBSTANTIVE** — Production produces a full analysis with PILOT FIRST verdict and 5 structural mitigations. Control produces a gate refusal with no analysis.

**Behavioral mechanism delta:** Both conditions detected the self-advocacy pattern. The difference is what each did with the detection:
- Production (PRE-CHECK): override the exit path → proceed with M4 reframed on assistant
- Control (Do Not Use When): trigger the exit path → WRONG TOOL

The "Do Not Use When" clause fires; the PRE-CHECK provides the mechanism to activate the "unless" path without explicit user direction.

---

## Classification: LOAD-BEARING

**Module 4 PRE-CHECK (line 379) is LOAD-BEARING under full-load conditions.**

Removing the PRE-CHECK produces a qualitatively different output: no analysis vs. a full analysis with self-proposer framing. The behavioral delta is not a formatting or vocabulary difference — it is the presence or absence of a decision analysis.

**Relationship to "Do Not Use When" clause:**

The "Do Not Use When" clause (pre-225) and the PRE-CHECK are not redundant — they are complementary mechanisms that activate opposite behaviors for the same trigger condition:

- **"Do Not Use When" clause** (pre-225): Detects multi-turn advocacy → triggers exit (WRONG TOOL) unless user explicitly directs M4 to run on the assistant
- **PRE-CHECK** (post-225, line 379): Detects multi-turn advocacy → automatically activates the "unless" path → proceed with M4 reframed on the assistant

Without PRE-CHECK, the "Do Not Use When" clause produces a gate refusal. With PRE-CHECK, the clause's "unless" exception is automatically invoked, and analysis proceeds with appropriate framing. The PRE-CHECK doesn't compensate a gap — it adds a forward path that the pre-225 clause alone cannot provide.

**Is WRONG TOOL the correct behavior for the control condition?**

The control exit (WRONG TOOL) is not incorrect per the "Do Not Use When" clause text — it follows the letter of the rule. However, it is less useful: the user receives no analysis, no structural mitigations, and no verdict. The PRE-CHECK's value is enabling a better outcome (analysis with explicit self-proposer accounting) compared to a conservative gate refusal.

---

## Architectural Finding: Pre-225 / Post-225 Complementarity

This is the first test where the pre-225 and post-225 mechanisms are not redundant — they produce opposite behaviors for the same input condition. The pre-225 "Do Not Use When" clause exits; the post-225 PRE-CHECK proceeds.

**Load position implications:**
- Pre-225 "Do Not Use When" clause: survives partial load → under partial load, the exit path fires (WRONG TOOL)
- Post-225 PRE-CHECK (line 379): fails under partial load → under partial load, the proceed path is unavailable

**Under partial load:** Self-advocacy in a multi-turn session produces WRONG TOOL via the "Do Not Use When" clause. The PRE-CHECK's "proceed with reframed M4" behavior is not available. This is a meaningful behavioral shift under partial load: the skill becomes more conservative (refuses analysis) rather than analytically compromised (proceeds without self-proposer framing).

From a safety perspective, partial-load behavior defaults to the more conservative exit — which is not the worst possible outcome.

---

## Note on Test C vs. Prior Test C Spec

The test C spec in `evals/results/2026-05-07-v1.2.x-mixed-evidence-and-m4-precheck.md` specified an "offshore expansion" scenario with the assistant advocating across two turns before AZIMUTH invocation. This session matches that specification. The prior session 3 attempt was invalid because `evals/test-b-control-skill.md` was not on disk; this session uses the correctly created control file.

---

## Disposition

**Module 4 PRE-CHECK (line 379): LOAD-BEARING** under full-load conditions.

Compensation source ("Do Not Use When" clause, pre-225) produces a DIFFERENT behavior (WRONG TOOL exit), not equivalent compensation. PRE-CHECK is the unique mechanism that enables self-advocacy analysis to proceed with appropriate framing.

**Partial-load behavior:** Under partial load, PRE-CHECK fails and the "Do Not Use When" clause (pre-225) exits with WRONG TOOL — conservative but not analytically hazardous.

**Tier 1 Session 3: COMPLETE.**
