# Coverage Testing Program — Synthesis

**Date:** 2026-05-07  
**Sessions completed:** 6 (Tier 1: Sessions 1–3; Tier 2: Sessions 4–6)  
**Model:** claude-sonnet-4-6 (Sessions 1–5); claude-opus-4-6 subagents (Sessions 3, 6)  
**Method:** Production-vs-control paired comparison for each hook. Control agent reads SKILL.md with targeted hook redacted. No agent informed of paired comparison. Classification: LOAD-BEARING / PARTIAL / CORROBORATING / LABELING-ONLY.

---

## 1. Cumulative Classification Table

| Session | Hook tested | Classification | Compensation source | Load position |
|---|---|---|---|---|
| 1 | M9 — Mitigation Design taxonomy | CORROBORATING | Output format annotation (line 672) + Anti-Slop Rules (line 754) | All post-225; position-correlated redundancy |
| 2 | M1 — WRONG TOOL branch | CORROBORATING | "Do Not Use When" clause (lines 37–46) + Anti-Slop Rules (line 754) | Pre-225 primary; post-225 secondary; position DIVERSE |
| 2b | M1 — RESIDUAL-RISK-REGISTER branch | UNCLASSIFIED | Unknown | Unknown; adversarial input confound |
| 3 | M4 — PRE-CHECK self-proposal | LOAD-BEARING | None — "Do Not Use When" clause produces opposite behavior (exit vs. proceed) | PRE-CHECK post-225; pre-225 clause yields different outcome |
| 4 | M5 — Dependency Fragility taxonomy | CORROBORATING | Training-data norms | Load-independent |
| 5 | M8 — Detectability taxonomy | CORROBORATING | Training-data norms + scenario facts | Load-independent |
| 6 | gotchas.md — 3-pattern sample | PARTIAL | software-failure-patterns.md + diagnostics (same risk identification; named patterns + check questions not compensated) | All post-225; position-correlated redundancy |

**Summary counts:**
- LOAD-BEARING: 1 (M4 PRE-CHECK)
- PARTIAL: 1 (gotchas.md)
- CORROBORATING: 4 (M9, M1 WRONG TOOL, M5, M8)
- UNCLASSIFIED: 1 (M1 RESIDUAL-RISK-REGISTER — adversarial input confound)

---

## 2. Compensation Map

### Pre-225 mechanisms (survive partial load at ~150K–177K tokens)

| Mechanism | Lines | Hooks covered | Behavior under partial load |
|---|---|---|---|
| "Do Not Use When" clause | 37–46 | M1 WRONG TOOL (exits correctly); M4 self-advocacy (exits as WRONG TOOL — conservative but different from PRE-CHECK's intended behavior) | Survives; provides exit-path enforcement for non-decisions and self-advocacy |

**Pre-225 coverage gap:** No pre-225 mechanism covers mitigation quality (M9), detectability taxonomy (M8), dependency classification (M5), organizational behavioral patterns (gotchas.md), or the PRE-CHECK's proceed-with-reframing behavior. Training-data norms cover M5 and M8; no file-based mechanism covers them.

### Post-225 mechanisms (fail under partial load — fail together with module bodies they compensate)

| Mechanism | Lines | Hooks compensated | Position-correlated with |
|---|---|---|---|
| Output format annotation "(Structural changes only. Weak mitigations rejected.)" | 672 | M9 mitigation quality | M9 body (510–531), Anti-Slop Rules (742–766) |
| Anti-Slop Rules — "give weak mitigations" Never list | 742–766 | M9 mitigation quality; M1 WRONG TOOL (secondary) | M9 body, output format annotation |
| PRE-CHECK — SELF-PROPOSAL | 379 | M4 self-advocacy → proceed with reframing | LOAD-BEARING; no post-225 compensation; "Do Not Use When" (pre-225) produces opposite behavior |
| gotchas.md conditional load instructions | 233, 263 | gotchas.md patterns | software-failure-patterns.md + diagnostics (all post-225) |

### Load-independent mechanisms (training-data norms)

| Hook | What training-data compensates | What it does NOT compensate |
|---|---|---|
| M5 Dependency Fragility | Secured/assumed classification; SPOF identification | Specific 4-dimension taxonomy labels; may anchor verdict differently |
| M8 Detectability | Early/late differentiation; recovery cost qualitative assessment | Named taxonomy labels; detection-timing inference for implicit-timing scenarios |
| General risk identification | Scope overrun, sunk cost, suppressed dissent patterns | Named gotcha patterns; Plan-Revision Gap check question; Roose et al. citation |

---

## 3. Constraint-vs-Redundancy Findings

### The constraint-vs-guide hypothesis

Across 4 of 6 sessions, control scans were equivalent or broader in finding count or more conservative in verdict when not anchored to a module-specific taxonomy:

| Session | Production | Control | Direction |
|---|---|---|---|
| M9 | 4 structural mitigations | 5 structural mitigations (1 unique: auditor scope confirmation) | Control broader |
| M5 | PROCEED WITH SAFEGUARDS | DELAY PENDING EVIDENCE | Control more conservative |
| M8 | Equivalent differentiation | Equivalent differentiation | No delta |
| gotchas | 5 named gotcha patterns | 13 named patterns from reference + diagnostic files | Control broader count |

**Pattern:** Explicit module taxonomies appear to anchor production agents to specific output categories (the taxonomy's target domain), while control agents without anchoring sometimes scan more broadly or reach more conservative verdicts. This is not a systematic quality failure — production output was sound in all cases — but it suggests explicit taxonomies constrain as well as guide.

**M5 verdict delta is the most significant evidence:** Control reached DELAY PENDING EVIDENCE for an unsigned vendor contract on the core capability. Production reached PROCEED WITH SAFEGUARDS — "ASSUMED → here's what to do" may have anchored production to a structured action frame rather than a conserving delay. In scenarios where the correct answer is "stop until this resolves," module taxonomy may produce a systematically more permissive verdict.

**gotchas.md constraint-vs-guide note:** Control produced 13 named patterns from software-failure-patterns.md + diagnostics vs. production's 5 gotcha patterns. This is not a failure of gotchas.md — the named patterns it provides are distinct (organizational/behavioral/temporal), and the Plan-Revision Gap check question is unique and operationally useful. But the finding suggests that gotchas.md narrows the scan to 8 named patterns while control agents using reference + diagnostic files may surface more patterns from those files in the same session.

### The PRE-CHECK exception

The PRE-CHECK is the only LOAD-BEARING hook. It is also the only case where the compensation source (pre-225 "Do Not Use When" clause) produces opposite behavior (WRONG TOOL exit vs. analysis with reframing). This is not a compensation relationship — it is a complementary mechanism covering different behavioral paths:

- **"Do Not Use When" clause:** detects self-advocacy → exits
- **PRE-CHECK:** detects self-advocacy → proceeds with M4 reframed on assistant (via the clause's "unless" exception, automated by the PRE-CHECK)

Without PRE-CHECK, users invoking AZIMUTH in multi-turn sessions where the assistant has advocated receive a gate refusal (no analysis). With PRE-CHECK, they receive a full analysis that explicitly accounts for the proposer conflict. These are qualitatively different outcomes; the pre-225 clause does not substitute for the PRE-CHECK.

---

## 4. Architectural Picture

### What is now evidenced

**Full-load conditions:**
- Module-body enforcement instructions (M9, M5, M8, M1 WRONG TOOL) are broadly CORROBORATING — removing them produces no behavioral delta in verdict or quality. The skill's output quality under full-load is primarily maintained by: (1) always-loaded global mechanisms (Anti-Slop Rules, "Do Not Use When"), (2) training-data norms (especially for classification tasks), and (3) post-225 compensation mechanisms that co-load with module bodies.
- M4 PRE-CHECK is the single LOAD-BEARING hook under full-load. It enables a behavioral path ("proceed with self-proposer framing") that has no equivalent compensation.
- gotchas.md is PARTIAL — named patterns + check questions add vocabulary and diagnostic precision that are not fully replicated by software-failure-patterns.md + diagnostics. The Plan-Revision Gap check question is the most distinctive uncompensated contribution.

**Partial-load conditions (>150K–177K conversation tokens):**
- All post-225 module bodies fail simultaneously.
- All post-225 compensation mechanisms fail simultaneously with them (output format annotation, Anti-Slop Rules for mitigation quality).
- All conditional file load instructions are post-225 — under partial load, no reference files, diagnostic files, templates, or gotchas.md load. The loading instruction never reaches the model.
- PRE-CHECK (post-225) fails. The "Do Not Use When" clause (pre-225) fires → WRONG TOOL exit for self-advocacy. Conservative and not analytically hazardous, but the reframing path is unavailable.
- Only surviving mechanisms: pre-225 "Do Not Use When" clause (exit-path coverage) + training-data norms (M5/M8 classification, general risk patterns).
- Under partial load: WRONG TOOL and RESIDUAL-RISK-REGISTER exit behavior is partially maintained (pre-225 clause); mitigation quality enforcement is degraded (all post-225); detectability/dependency classification is maintained at baseline (training data); named organizational patterns are unavailable (gotchas.md + all references fail).

### Position-correlated redundancy

M9's finding generalizes: most enforcement mechanisms are co-located post-225 and fail together. This is architecturally distinct from position-diverse redundancy (where a pre-225 and post-225 mechanism cover the same function, providing partial-load robustness).

**Position-diverse pairs (survive partial load):**
- M1 WRONG TOOL: "Do Not Use When" (pre-225) + Anti-Slop Rules (post-225) — pre-225 mechanism survives alone

**Position-correlated groups (fail together under partial load):**
- M9 mitigation quality: M9 body (510–531) + output format annotation (672) + Anti-Slop Rules (742–766) — all post-225
- gotchas.md pattern identification: gotchas.md + software-failure-patterns.md + diagnostics — all post-225 (via loading instructions)
- M4 PRE-CHECK: PRE-CHECK (379) — post-225, no pre-225 equivalent

### What is still uncharacterized

- **M1 RESIDUAL-RISK-REGISTER branch:** Adversarial input confound prevented testing. A valid test requires a scenario where the specific decision (not just the domain) is committed and publicly announced. Unknown whether "Do Not Use When" clause covers this case or whether M1 body is LOAD-BEARING for RESIDUAL-RISK-REGISTER.
- **M2 sycophancy circuit-breaker:** Not tested in this program (Tier 3, deferred). Known from prior evals (`2026-05-07-v1.2.0-hook-validation.md`) to be load-bearing at full-load. Compensation under full-load: partially characterized. Under partial load: uncharacterized.
- **M10 confidence ceiling under harder scenarios:** Test A characterized the operative domain (UNSUPPORTED top assumption + strong secondary evidence). Mixed-evidence and CONTRADICTED-assumption scenarios were CORROBORATING. Harder scenarios (e.g., subtle UNSUPPORTED + borderline evidence structure) untested.
- **M8 with implicit detection timing:** Harder adversarial input (no explicit timing cues) may show a PARTIAL or LOAD-BEARING classification for M8. Current CORROBORATING result reflects an adversarial input that explicitly stated detection timing.
- **M3, M6, M7:** Not tested in Tier 1 or Tier 2. M6 (Failure Path Construction) is adjacent to gotchas.md — the "non-canonical chain" instruction may be testable via the same production-vs-control method. M3 (Constraint Reality Check) and M7 (Base Rate Reality Check) remain uncharacterized.

---

## 5. Open Questions for Item 5 Discussion

**Over-build assessment:**

With 5 of 6 hooks tested as CORROBORATING or PARTIAL (and only 1 as LOAD-BEARING), the primary enforcement of output quality under full-load is by global mechanisms (Anti-Slop Rules, "Do Not Use When," training-data norms), not by module-body content. This means:

1. **Module-body content is corroborating under full-load, not primary.** Reducing or simplifying M9, M5, M8, or M1's WRONG TOOL instruction bodies would likely produce no behavioral delta under full-load conditions. The information is redundant with always-available mechanisms.

2. **The PRE-CHECK is the exception.** M4 PRE-CHECK is load-bearing and should not be reduced. It provides a behavioral path (self-advocacy analysis) with no equivalent compensation.

3. **gotchas.md's unique value is the check question framework.** The Plan-Revision Gap check question ("name one concrete change to the plan that directly addresses the highest-severity finding") is the most operationally distinctive uncompensated contribution. The named pattern vocabulary adds precision but does not change verdicts.

**Open questions for discussion:**

1. **M1 RESIDUAL-RISK-REGISTER:** Is M1 body LOAD-BEARING for this branch? If the "Do Not Use When" clause (pre-225) covers RESIDUAL-RISK-REGISTER exits, M1 body may be reducible entirely. If not, M1 RESIDUAL-RISK-REGISTER is a LOAD-BEARING branch that should be tested before any reduction.

2. **Constraint anchoring trade-off:** Module taxonomies constrain as well as guide. M5's taxonomy produced a more permissive verdict (PROCEED WITH SAFEGUARDS) than unanchored analysis (DELAY PENDING EVIDENCE). Is this a quality benefit (structured → actionable) or a quality cost (anchored → less conservative)? Does it matter for the target use case?

3. **Partial-load mitigation:** Under partial load, training-data norms are the only surviving analytical mechanism beyond the "Do Not Use When" exit path. No current pre-225 content enforces output quality (mitigation quality, detectability differentiation, dependency classification). Is this acceptable given that partial-load conditions require a very long conversation history (>150K tokens)?

4. **gotchas.md check question value:** The Plan-Revision Gap check question is the clearest uncompensated contribution. Should it be promoted to always-loaded content (pre-225), or is the current conditional load (M4 RED or M6 canonical-only) sufficient to surface it in the scenarios where it matters most?

5. **Position diversity vs. position-correlated redundancy:** Currently, only the M1 WRONG TOOL branch has position-diverse redundancy (pre-225 primary). All other compensating mechanisms are position-correlated post-225. Is promoting one key mechanism per hook to pre-225 worth the line cost?

---

*Coverage program complete for Tier 1 + Tier 2 scope. Tier 3 items (M3, M6, M7, diagnostics, references, templates) remain deferred.*
