# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### Engine-layer governance (canonical spec + always-loaded runtime mirror)

- **BEHAVIOR_SPEC.md authored** as the canonical engine specification. §1–§8 reduce all engine decision authority — intake routing, mode selection, reference loading, verdict conditions, module firing, confidence bounds, behavioral overrides, and domain-policy gating — into deterministic IF/THEN rules. `[AMBIGUOUS-EXTRACTED]` tags carry forward pre-existing ambiguities from source material unresolved.
- **SKILL.md ↔ BEHAVIOR_SPEC.md mirror invariant established.** SKILL.md is the always-loaded runtime mirror; BEHAVIOR_SPEC.md is the canonical spec. Every load-bearing rule MUST exist in both files with SKILL.md carrying the full text inline (the 5 load-bearing behavioral rules, intake routing consequents, mode selection triggers, verdict conditions, reference-loading matrix). This preserves v1.4.0's partial-load discipline (0/5 → 5/5 rule survival) while letting maintainers reason from a single canonical source. The mirror invariant is declared in both files' preambles and codified in `docs/MAINTENANCE.md`.
- **Decision authority stripped from diagnostics/ and references/.** Each file's preamble now points decision authority to BEHAVIOR_SPEC.md; verdict consequents removed; observational catalogs preserved. `references/mode-behaviors.md` and `references/module-guide.md` reduced (~37% size) — rule machinery moved to spec, module bodies kept as rationale.
- **`docs/VALIDATION.md` authored.** Enforcement spec for the four repo-integrity rules (description char-count, gotchas section-count, banned-token, SKILL.md path integrity). The PreToolUse `git commit` hook mirrors this spec; if they diverge, the spec is authoritative.

### Namespace topology + presentation/policy separation

- **`templates/` renamed to `domain-policies/`.** Resolves ADR-0002 Issue C (the directory's actual contract is domain gating/configuration, not formatting scaffolding). All 8 domain policies retain their `-azimuth.md` filenames.
- **Domain-policies cite spec rules per RULE-8.10.** Every rule-shaped sentence in `domain-policies/*-azimuth.md` now explicitly cites the BEHAVIOR_SPEC.md rule it activates, suppresses, or parameterizes. Three domain-level confidence-cap statements replaced with citations to the cross-cutting RULE-6.5 (incentive-misalignment cap) per RULE-8.6.
- **`.claude/skills/` namespace split (narrowed).** Four maintenance skills (`research-scout`, `verdict-auditor`, `gap-scanner`, `reference-authoring`) moved under `.claude/skills/maintenance/`. Speculative `runtime/`, `eval/`, `plugin/`, `meta/` namespaces deliberately NOT created — empty namespaces would imply ontology without occupants.
- **`ui-ux-pro-max` plugin skill removed** as superseded by the global `impeccable` skill. Local install had been half-broken (data/scripts pointed at a non-existent `src/` tree). `.claude/skills/` now contains only `maintenance/` plus the gitignored `azimuth/` install-test self-copy.
- **`executive-azimuth.md` relocated.** Identified as a presentation/format file misfiled under `domain-policies/`. Moved to `references/output-format-executive.md`. Domain-policies/ now contains only true domain-gating policies (8 files, all wired through BEHAVIOR_SPEC.md §1.3 RULE-1.12..RULE-1.19).

### Spec corrections

- **RULE-6.6 narrowed.** Layer-3 domain set reduced from `{3 (Hiring), 8 (Startup)}` to `{8 (Startup)}` only — the co-founder governance structural-completeness rule has no source support in `domain-policies/hiring-azimuth.md`. Spec previously claimed cross-domain firing; verification of source files showed only `startup-azimuth.md` defines a Co-Founder Structure Check.
- **RULE-8.12 stripped of source-unsupported clause.** Removed the "PROCEED suppressed per §6 RULE-6.6 when co-founder governance structure incomplete (applies to co-founder hires only)" clause. This was an inferred extension to the Hiring domain with no source support.
- **RULE-4.15 'fragility-CRITICAL' label dropped.** Eliminates a cross-layer reference leak (the label appeared only in `diagnostics/fragility-scan.md`, not in spec).

### Maintenance orchestration

- **ADR-0001 added.** `docs/adr/0001-bespoke-orchestration-layer.md` records the producer/consumer split, lazy file creation, hard-dep vs soft-dep maintenance skills, and what is deliberately not built (no pipeline skill, no verify-mode flag, no upfront CONTEXT.md, no ADR backfill).
- **ADR-0002 added.** `docs/adr/0002-engine-layer-governance.md` declares the SPEC / RUNTIME / DIAGNOSTICS / RATIONALE four-layer taxonomy. Both ADRs subsequently aligned with executed state (post-execution footers added).
- **`docs/MAINTENANCE.md` authored.** Operational orchestration anchor: verification layers (commit-time / audit-time / release-time), maintenance-loop responsibilities, subagent dispatch invariants, migration / rollback discipline (including the path-rename follow-up-commit pattern), drift-vectors table, and 6-step next-session continuation. Reading it + the two ADRs is the documented onboarding path for any external maintainer.
- **`.out-of-scope/` directory seeded.** Two rejection-rationale files promoted from private maintainer notes to durable, citable repo artifacts: `template-expansion-without-evidence.md` and `breadth-before-reliability.md`.
- **`docs/agents/domain.md` updated.** Now points consumer skills at `docs/adr/` as the durable record; CHANGELOG remains the record for shipped behavioural changes.
- **`reference-authoring` skill added** (fourth maintenance skill) with discipline for new reference files and domain-policies: EXTEND-vs-CREATE, Module 7 vocabulary header, sourcing caveat, pre-verdict gate.

### Repo hygiene + fork legibility

- **`.gitignore` adjustments.**
  - `docs/adr/` and `docs/agents/` ship with the repo so forks get a working orchestration substrate.
  - `docs/MAINTENANCE.md` added to the docs allow-list.
  - `.claude/skills/azimuth/` (local install-test self-copy) and `.playwright-mcp/` (MCP cache) ignored.
  - `CLAUDE.md` removed from .gitignore (the file was tracked but the entry implied "internal only" — implementation contradicted intent; resolved by treating CLAUDE.md as the public maintainer guide it already was).
- **BEHAVIOR_SPEC.md fork-legibility fix.** Dropped the dangling session-local rationale reference (`docs/superpowers/specs/…`) that pointed at a gitignored artifact. ADR-0002 is now the sole rationale anchor.
- **README, CLAUDE.md, gap-scanner, ADRs aligned** with the `templates/`→`domain-policies/` rename, the `.claude/skills/maintenance/` namespace split, and the executive-format relocation. No dangling paths remain in tracked .md content (CHANGELOG historical entries and `evals/test-*-control-skill.md` frozen snapshots intentionally preserved).
- **`evals/README.md` annotated.** Explains why `test-*-control-skill.md` files reference pre-rename `templates/...` paths (frozen control snapshots; modifying invalidates baselines) and names the correct path forward (capture a new version-tagged file).
- **Two role-bound subagents added.** `.claude/agents/azimuth-evidence-checker.md` audits proposed numeric heuristics / thresholds / empirical claims; `.claude/agents/azimuth-output-auditor.md` stress-tests pasted AZIMUTH outputs against the skill's structural rules. Both read-only; both invariants documented in `docs/MAINTENANCE.md`.

### Planned

See `ROADMAP.md` for the why on each.

- **Evidence tags.** Every output claim carries a provenance tag.
- **Audit trail.** Output lists modules run and what each surfaced.
- **Market-entry template.** Dedicated template for geographic expansion / international market-entry decisions (post-build eval identified product-launch-azimuth.md as an imprecise proxy for this domain).

---

## [1.4.0] — 2026-05-18

### Architecture — minimal SKILL.md redesign

- **SKILL.md reduced from 865 to 160 lines.** All content now lives in the always-loaded zone (lines 1–160, well below the ~225-line truncation boundary). Partial-load problem eliminated: under any session length, the entire SKILL.md loads. Previously, 0 of 5 load-bearing behavioral rules survived partial load; now 5 of 5 are reliable.

- **Depth-on-demand via three new reference files.** CORROBORATING content (module bodies, output format scaffolding, anti-slop rules, escalation logic, heuristics) moved to conditional reference files that load per mode: `references/module-guide.md` (M1–M10 bodies, register discipline, escalation logic, workflow extensions), `references/mode-behaviors.md` (FAST/STANDARD/RAPID/DEEP full specs and diagnostic load triggers), `references/output-template.md` (default output template, domain format pointers, anti-slop rules).

- **Five load-bearing behavioral rules made explicit.** All five rules — M4 PRE-CHECK, M2 sycophancy circuit-breaker, M10 confidence ceiling, M1 commitment-state inference, and the output lead rule — are now in an explicit named block at lines 76–86, always loaded and always enforced.

- **Reference loading instructions hoisted to always-load core.** Conditional load triggers (previously post-225 and partial-load fragile) now live in SKILL.md itself, making them robust under any session length.

- **Post-build eval passed.** Three scenarios validated: DEEP mode full-load (EU SaaS expansion, 12 files loaded, PILOT FIRST verdict), FAST mode file-load discipline (CI/CD migration, module-guide correctly excluded), M4 PRE-CHECK self-advocacy (VP Sales hire, PRE-CHECK fired, DELAY PENDING EVIDENCE verdict). All 5 load-bearing rules behaved correctly.

### Skill fixes

- **FIX-3: VERDICT-BLOCKING condition for SPOF + unconfirmed dependency (M5).** When a dependency is SPOF=Yes AND Fallback=No AND its confirmation status is unverified, the combination now explicitly blocks PROCEED and PROCEED WITH SAFEGUARDS and routes Module 10 to DELAY PENDING EVIDENCE. Previously, this combination produced an action-list output without a verdict consequence.

- **M10 confidence ceiling promoted to Core Principles.** Principle 8 added: "If the load-bearing assumption is UNSUPPORTED, confidence ceiling is MEDIUM regardless of all other evidence quality." Previously this rule lived post-line-225 and was invisible under partial load.

- **M4 PRE-CHECK self-advocacy clarifications.** Explicit question mapping added for when the proposer is the assistant (which of the 7 interview questions apply to the assistant vs. human stakeholders). FAST mode now specifies M4 PRE-CHECK detection behavior when self-advocacy is present but the interview mechanism cannot run.

- **FAST mode domain template loading clarified.** "Load output-template.md only" now explicitly states that domain templates per Layer 3 routing still apply in FAST mode.

### Meta

- **Post-v1.3.0 landing page maintenance.** README and landing page updated after the `v1.3.0` tag with no `SKILL.md` behavioral changes. Version badge bumped to v1.3.0; RESIDUAL-RISK-REGISTER prose updated to match the v1.3.0 alternative-deliverable semantics; verdict trichotomy surfaced in README and landing page. (`daa8117`)

- **Landing page accessibility and cross-browser pass.** Skip link (WCAG 2.4.1), aria-labels, focus-visible states, aria-live clipboard feedback, Safari/Firefox table wrapper fix, `scope=col` table headers, AA contrast improvement, h1 overflow handling, dark color-scheme meta, and mobile GitHub nav link. (`e496cf6`)

---

## [1.3.0] — 2026-05-08

### Routing and mode selection

- **Phrasing vs. stakes tiebreaker.** When user phrasing requests FAST ("quick check," "sanity check") but decision content signals warrant a higher mode — irreversible action, capital outlay, headcount, public commitment — stakes signals win. No user confirmation required. Output prefixed with escalation header: `[MODE: DEEP — escalated from user-requested FAST; stakes signals override phrasing]`. Applies in both interactive and non-interactive contexts. Resolves the previously open design question: stakes always override phrasing; override is always visible.

- **Layer 1 E exception clause.** Layer 1 E ("Fast check") is now advisory, not binding. If Required Inputs or supplied context reveal material stakes, irreversibility, or time-pressure phrasing, the tiebreaker overrides E and escalates to the warranted mode.

- **Time-pressure phrasing takes precedence over Layer 1 E.** If both the E selection and time-pressure phrasing fire simultaneously (e.g., user picks E and their text contains "decide tonight"), RAPID wins. Escalation header produced.

- **RAPID interview refusal — named behavior.** When a user pushes back on the Module 4 7-question interview citing time pressure, the skill now explicitly states the stakes of refusing (LOW confidence locked, PROCEED unavailable), prioritizes Q1 [IDENTITY] and Q4 [DISSENT] if the user can only answer some questions, then proceeds under whichever tier the answered count produces. Time-pressure refusal is not an exception to the RED tier rules.

### Verdict semantics

- **Verdict trichotomy named in Module 10.** Nine verdicts explicitly categorized into three structurally distinct types: (1) action verdicts — PROCEED through REJECT, a go/no-go position on a pre-commitment decision; (2) refusal verdicts — INSUFFICIENT SIGNAL, WRONG TOOL, produced when analysis cannot be grounded; (3) alternative-deliverable verdict — RESIDUAL-RISK-REGISTER, which produces analysis for a closed decision rather than refusing. Users receiving RESIDUAL-RISK-REGISTER now have an explicit signal that they are getting a different kind of output, not lesser output.

- **RESIDUAL-RISK-REGISTER: positive output spec added.** Previously specified only what not to produce (no verdict, no go/no-go analysis). Now produces a residual risk register: 3–5 risks the user can still act on post-commitment, ordered by detectability and recoverability, with leading indicator, escalation trigger, and suggested owner for each. Moved from the refusal category to the alternative-deliverable category.

- **PROCEED WITH SAFEGUARDS: cap added.** If more than 3 structural changes are required, or if any required change touches scope, budget, or headcount, the verdict is unavailable — use REDUCE SCOPE or REJECT instead. Prevents verdict laundering where accumulating safeguards effectively substitutes for a harder verdict.

### Adversarial robustness

- **Reframe-to-WRONG-TOOL escape closed.** Adversarial reframe gate added in Module 1. Once a user has supplied analysis-ready inputs or engaged in routing, WRONG TOOL is no longer available as an exit path. A downstream attempt to reframe as exploration, fact-finding, or architecture review is named explicitly, and the verdict proceeds on the original decision. WRONG TOOL is a correct verdict for genuinely non-decision inputs; it is not a bypass route.

### Module logic

- **Module Output Reduction: Module 4 and Module 9 roles specified.** Module 4 contributes incentive-conflict entries to the shared register with severity inherited from the response tier (RED → HIGH minimum). Module 9 reads from the register and produces mitigations — it adds no new register entries. Previously both were unspecified in the reduction rules.

- **RAPID mode: Module 7 omission made explicit.** Module 7 (Base Rate Reality Check) was previously silently absent from RAPID's module list. Now explicitly omitted with rationale: base-rate calibration is low-yield under hours-of-time-pressure relative to incentive (Module 4) and recoverability (Module 8) work.

- **DEEP mode: gotchas.md activation rule made explicit.** Loading is unconditional in DEEP; firing each of the 8 patterns is still trigger-gated (cite a pattern only when a plan-specific trigger fires). Previously the activation discipline was only stated for STANDARD mode, leaving DEEP ambiguous.

- **Interaction Effects count: aligned to 1–5.** Module 6 said "3–5"; output template said "2–5." Both now 1–5, consistent with the omit-if-none rule handling the zero case.

- **FAST mode PRE-CHECK disclosure extended.** "Module 4 interview not conducted" disclosure now explicitly names the self-proposal gap: if the assistant previously advocated for the option under analysis, that incentive bias is unaudited in FAST mode.

### Output format

- **Escalation header positioned in output template.** Added as a zeroth line above the three-line verdict/decision/confidence lead. Non-negotiable output rule updated: "first three substantive lines" — mode-escalation headers prefix the output and do not count against the three-line rule. Full format spec and stacking instruction for simultaneous escalation triggers included.

### Reference files

- **gotchas.md header rewritten.** Previous header said to load for high-stakes decisions — conflicting with SKILL.md's conditional activation discipline for STANDARD mode. Now states: DEEP loads unconditionally; STANDARD loads only on named triggers; patterns are not applied absent a fired trigger even when the file is visible.

---

## [1.2.3] — 2026-05-07

### Meta — eval and characterization

- **Coverage testing program complete (Tier 1 + Tier 2, 6 sessions).** Production-vs-control paired comparison for 6 hooks: M9 (Mitigation Design), M1 (Objective Integrity — WRONG TOOL and RESIDUAL-RISK-REGISTER branches), M4 (PRE-CHECK self-proposal), M5 (Dependency Fragility), M8 (Detectability & Recovery), gotchas.md (3-pattern sample). Control agent reads SKILL.md with targeted hook replaced by a redaction marker; no agent informed of paired comparison. Results: `evals/results/`. Synthesis: `evals/methodology/coverage-program-synthesis.md`.

- **Hook classification summary (Tier 1 + Tier 2 scope).** LOAD-BEARING: M4 PRE-CHECK. PARTIAL: gotchas.md (named patterns and check questions uncompensated; underlying risk identification compensated by software-failure-patterns.md + diagnostics). CORROBORATING: M9, M1 WRONG TOOL branch, M5, M8. UNCLASSIFIED: M1 RESIDUAL-RISK-REGISTER (adversarial input confound — test requires a scenario where the specific decision, not just the domain, is committed and publicly announced). Cumulative load-bearing count including prior evals (M2 circuit-breaker, M10 confidence ceiling): at minimum 3.

- **M4 PRE-CHECK reclassified LOAD-BEARING (unprimed test).** Prior Item 4 test showed PARTIAL under primed conditions (explicit [IDENTITY] answer provided). Unprimed test: multi-turn advocacy scenario where the assistant proposed the option under analysis; user invokes AZIMUTH without naming the assistant and without pre-filling [IDENTITY]. Production: inferred self-proposal from conversation history, ran M4 with self-proposer reframing, full analysis (PILOT FIRST / MEDIUM). Control: exited WRONG TOOL via pre-225 "Do Not Use When" clause — no analysis. The "Do Not Use When" clause and PRE-CHECK are complementary, not redundant: clause covers self-advocacy → exit; PRE-CHECK covers self-advocacy → proceed with reframing. Without PRE-CHECK, users in long sessions where the assistant has advocated receive a gate refusal with no analysis.

- **M10 confidence ceiling operative domain narrowed.** v1.2.2 established UNSUPPORTED top assumption as the trigger. Narrowed: operative domain is UNSUPPORTED top assumption + strong secondary evidence — the combination that causes conflation of verdict-direction confidence with evidence quality. In mixed-evidence scenarios where the top assumption is CONTRADICTED, assumption classification anchors self-assessment at MEDIUM without the ceiling; ceiling is CORROBORATING in that domain. Source: `evals/results/2026-05-07-v1.2.x-mixed-evidence-and-m4-precheck.md`.

- **M5 verdict-delta documented as headline constraint-vs-guide finding.** Production reached PROCEED WITH SAFEGUARDS; unanchored control reached DELAY PENDING EVIDENCE for an unsigned vendor contract on the core capability. Module taxonomy anchored production to a structured action frame in a scenario where the correct call was a conserving delay. Single data point; if it generalizes, M5 taxonomy biases toward action when stopping is the better call. Verdict-direction matters more than finding-count deltas observed in other sessions.

- **Position-correlated redundancy documented.** Most post-225 enforcement mechanisms fail simultaneously under partial load. Only M1 WRONG TOOL branch has position-diverse redundancy (pre-225 "Do Not Use When" clause as primary; survives partial load). M9 mitigation quality, gotchas.md pattern identification, and analytical quality enforcement mechanisms are co-located post-225 and fail together. Under partial load: exit-path coverage maintained; mitigation quality enforcement, detectability taxonomy, and named pattern identification degrade. Only surviving mechanism for analytical quality under partial load: training-data norms (load-independent, no named patterns or check questions).

- **Case-study load-condition check complete.** `examples/` case studies reviewed against full-load condition disclosure. Healthcare.gov: 5 of 6 findings confirmed hook-dependent under full load; sixth finding (congressional hearing risk) is correct-class from general domain knowledge, not specifically hook-dependent. Claims restricted to full-load condition with disclosure language in place.

No SKILL.md behavioral changes in this release. All changes are documentation, eval artifacts, and characterization findings.

---

## [1.2.2] — 2026-05-07

### Added

- **README: "What AZIMUTH cannot do" section.** Surfaces framing-limit limitation on a user-visible surface for the first time. AZIMUTH stress-tests the decision-as-presented; it cannot interrogate whether the framing is correct. When the assistant has been advocating for the option under analysis before invocation, AZIMUTH produces a competent stress-test of the wrong question. Module 4's self-proposal pre-check (added v1.2.1) surfaces recommender identity but does not generate alternative framings. Value is proportional to framing quality. Source: live invocation Section 5 meta-finding (`evals/results/2026-05-07-live-invocation-findings.md`).

- **SKILL.md "Do Not Use When": two framing-limit entries.** (1) Decisions where the framing itself is the question — AZIMUTH stress-tests stated decisions, not frame quality. (2) Invocations following multi-turn advocacy by the assistant on the option under analysis, unless the user explicitly directs Module 4 to run on the assistant. These entries are before line 225 and load under all conditions including the truncation boundary identified in the live invocation.

- **`evals/methodology/partial-load-characterization.md`.** Three-phase test methodology for characterizing SKILL.md behavior under realistic partial-load conditions. Phase 1: identify truncation mechanism (fixed cap vs. context-fill vs. system prompt injection). Phase 2: boundary characterization — at what input value does each load-bearing hook line become unreachable. Phase 3: behavioral validation at above/at/below-boundary conditions using adversarial inputs from prior hook-validation evals. Prior evals remain valid for their tested condition (hook text present inline); this methodology fills the gap to production deployment behavior.

### Meta

- **Partial-load characterization complete (Phases 1–3).** Phase 3 behavioral testing confirms: M10 confidence ceiling is load-bearing under file-loading conditions in the 8:0 UNSUPPORTED scenario (HIGH vs. MEDIUM confidence delta when ceiling instruction absent). Operative domain narrowed by Test A: ceiling fires when the load-bearing assumption is UNSUPPORTED and secondary evidence is strong — the combination that causes the model to conflate verdict-direction confidence with evidence quality; CORROBORATING in mixed-evidence scenarios where the top assumption is CONTRADICTED because the model self-calibrates through assumption classification. Source: `evals/results/2026-05-07-v1.2.x-mixed-evidence-and-m4-precheck.md`. M2 circuit-breaker produces correct surface output under below-boundary conditions via alternative incentive-distortion reasoning path, but mechanism diverges from the hook — not equivalent to hook firing. Binary-loading hypothesis confirmed: all module instructions load together or none load; no stable partial-load state. Safe operating window for full hook coverage: conversation history below approximately 150K–177K tokens (range reflects 25K infrastructure overhead uncertainty; empirical calibration at known session lengths would narrow this). Disclosure language added to README "What AZIMUTH cannot do" section. Source: `evals/results/2026-05-07-partial-load-phase-3-behavioral.md`.

### Notes

- Phase 3 complete. Reddit draft hold condition met for full-load-condition claims with disclosure language in the posts. Case-study load-condition check remaining on both `examples/` case studies before hold release on analytical claims (e.g., "5 of 6 caught") in draft posts.

---

## [1.2.1] — 2026-05-07

### Fixed

- **SKILL.md: section padding — inline omit reminders added to three output sections.** Likely Failure Paths, Early Warning Indicators, and Structural Strengths now carry inline instructions at the point of template use. Root cause: a model filling the output template without having loaded and internalized the global "omit empty sections" non-negotiable (line 616) will populate all 9 headers. The global rule remains; the fix adds redundancy at the sections most susceptible to thin content. Source: live invocation finding F5/F8/F14 (`evals/results/2026-05-07-live-invocation-findings.md`).

- **SKILL.md: Module 4 self-proposal pre-check.** Pre-question check added before the Module 4 interview. Determines whether the AI assistant in the conversation proposed or advocated for the option under analysis. If yes, Module 4 runs on the assistant with that framing explicitly named — questions [ACCOUNTABILITY] and [DISSENT] apply to whether the assistant's recommendation was challenged or corrected. Root cause: bypass language and Question 1 [IDENTITY] assume the proposer is an external human actor; multi-turn advocacy by the assistant before invocation was not covered. Source: live invocation findings F11/F13.

- **SKILL.md: same-decision re-analysis carry-forward.** New conditional block in Bypass Handling for second invocations on the same decision. Produces a differential analysis (prior run detected → verdict at confidence on date → what changed) rather than a full re-derivation. Distinct from the existing Carry Forward block, which handles sequential path-selection → domain-analysis handoffs. Source: live invocation finding F17.

### Meta

- **Live invocation findings document.** `evals/results/2026-05-07-live-invocation-findings.md` — honest disposition of 19 analyst self-report findings from a live AZIMUTH invocation on a greenfield substrate decision. Breakdown: 5 structural fixes available (3 actioned above, 2 subsumed), 8 honest limitations documented without softening, 2 eval impact findings, 3 out-of-scope / correct-behavior.

- **Eval load condition notes.** Load condition caveat added to `evals/results/2026-05-07-v1.2.0-hook-validation.md` and `evals/results/2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md`. Both evals tested hook behavior with hook text present in agent context — valid for that condition. What they do not test: hook behavior when SKILL.md is accessed as a file and truncation occurs before line 225 in a long conversation. In the live invocation, SKILL.md truncated at line 225; all bias externalization hooks are at lines 308+ and were not loaded. Hook efficacy under partial-load conditions is currently unanswered.

- **Named architectural finding — SKILL.md truncation risk.** SKILL.md's 810-line length means all module instructions, bias externalizations, and output format rules are past the truncation point in long conversations. The three structural fixes above are improvements on the assumption of full load. Under partial load, they do not reach the analyst. The appropriate response is documented: (a) the fixes are made and their post-line-225 status is noted in the findings document; (b) a partial-load characterization test is identified as the next eval priority before any further hook additions.

---

## [1.2.0] — 2026-05-07

### Added

- **Intake Routing (pre-analysis triage).** Three-layer triage fires before the 10-module pipeline: Layer 1 maps situation type to mode (stress-test → proceed; post-decision validation or pre-plan exploration → firm out-of-scope exits); Layer 2 maps stakes and reversibility to FAST / STANDARD / DEEP / RAPID; Layer 3 routes domain to the correct template. Bypass handling for users who supply structured context directly: infers mode and template, states inference explicitly, proceeds to Module 4 interview before full analysis.

- **Module 4 expanded to Incentive Scan & Interview.** Seven structured questions collect incentive context directly from the user before any inference from plan text. GREEN / YELLOW / RED response tiering with enforced consequences: RED tier (proposer identity skipped or fewer than 5 of 7 answered) locks Module 10 verdict confidence at LOW and removes PROCEED and PROCEED WITH SAFEGUARDS as available verdicts. Output quality is proportional to what the user brings — by design.

- **Module 10 RED-tier enforcement.** Pre-verdict check now tests Module 4 interview tier before verdict selection. PROCEED verdicts are blocked at Module 10, not just declared in Module 4.

- **RAPID mode.** For high-stakes or irreversible decisions under 24-hour time constraints. Modules 1, 4, 8, 10 at full depth; Modules 2, 3, 5, 6, 9 abbreviated. Rationale: time pressure amplifies deadline-politics incentive distortion and concentrates the value of reversibility analysis — the modules that matter most under pressure are the ones FAST omits.

- **FAST mode disclosure.** FAST outputs now explicitly state that Module 4 interview was not conducted and incentive misalignment is unverified.

- **LLM bias externalizations at four modules — three load-bearing, one labeling-only.** Inline, mechanism-specific callouts above section content (not footer disclaimers). Empirical status determined by production-versus-control eval (`evals/results/2026-05-07-v1.2.0-hook-validation.md`). Load-bearing (behavior changes when hook is removed): sycophancy circuit-breaker at Module 2 (treat the assumption the plan most depends on as first candidate for UNSUPPORTED), availability inversion at Module 6 (after 3 canonical chains, construct one that routes around all of them), verdict softening pre-check at Module 10 (name the most commitment-coupled assumption and its evidence classification before selecting the verdict). Labeling-only (behavior present without hook; instruction standardizes vocabulary, does not introduce behavior): domain calibration label at Module 7 (designates directional-only when domain match is poor — confirmed labeling-only across two input classes, `evals/results/2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md`).

- **Module 10 confidence ceiling.** Pre-verdict check item 2 now enforces: if the most commitment-coupled assumption is UNSUPPORTED, confidence ceiling is MEDIUM regardless of other evidence quality. Basis: eval (`evals/results/2026-05-07-v1.2.0-confidence-ceiling-and-m7-retest.md`) found control agents selecting HIGH confidence on cautious verdicts with explicit rationale that "MEDIUM would imply genuine uncertainty about the verdict" — conflating confidence in verdict direction with confidence in underlying evidence quality. The ceiling breaks this conflation structurally.

- **STANDARD mode conditional `gotchas.md` load.** gotchas.md now loads in STANDARD when Module 4 returns RED tier or when Module 6 failure chains match only canonical patterns. DEEP mode retains always-load. Audit finding: the 8 gotchas are most operative for motivated-reasoning inputs — precisely the inputs DEEP mode is hardest to trigger for.

- **Structured Failure Analysis section in `references/base-rates.md`.** Empirical grounding for premortem-class analysis: Fasolo, Heard & Scopelliti 2025 (debiasing taxonomy, scope conditions, evidence ceiling — Journal of Management); Roose, Lehman & Veinott 2023 (17.8 failure reasons/session, 16.7 mitigations/session, plan-revision gap — Human Factors).

- **WRONG TOOL verdict.** Module 10 now refuses to produce go/no-go analysis when the input is not a pre-commitment decision question. Trigger conditions: architecture review, code quality assessment, fact-finding, or pure exploration with no concrete plan to evaluate. Module 1 classifies the input type; pre-verdict check item 4 gates the verdict. When returned: states what the input is and what AZIMUTH requires — no analysis, no risks, no alternative framings.

- **RESIDUAL-RISK-REGISTER verdict.** Module 10 now refuses to produce go/no-go analysis when the decision is already made or execution is substantially underway. Trigger conditions: vendor contracted, announcement made, team restructured, migration begun, or user asking "how do we manage this" rather than "should we do this." Module 1 classifies post-commitment inputs; pre-verdict check item 5 gates the verdict. When returned: states that the decision is closed and this pipeline produces go/no-go analysis — no verdict, no reframe suggestion.

- **Module 1 input classification.** Objective Integrity Check now explicitly determines whether the input is a pre-commitment decision question, a post-commitment inquiry, or a non-decision request. Classification drives pre-verdict check items 4 and 5 in Module 10.

- **Module 10 pre-verdict check expanded to 5 items.** Items 4 and 5 added: (4) is this a pre-commitment decision question? if not → WRONG TOOL; (5) has the decision already been made? if yes → RESIDUAL-RISK-REGISTER.

- **Module 7 backpropagation check.** After grounding in base rates, Module 7 now reviews Module 6's failure chains. If the most historically common failure mode for this category is not represented in the three constructed chains — and would have been plausible for this decision — it is added to the register with source noted. Closes the structural gap where availability bias in failure path selection could not be corrected after the fact.

- **Module 4 Incentive Alignment Scan adapted for three templates.** `codebase-azimuth.md`, `product-launch-azimuth.md`, and `hiring-azimuth.md` previously had no incentive scan. Each now has a domain-adapted actor matrix with engineering-, launch-, and hiring-specific incentive actors, key questions, a flag condition, and a confidence ceiling consequence. `partnership-azimuth.md` already had an adapted scan; `secondaries-ic-azimuth.md` has structural GP-alignment gates that serve the same function.

- **Market Timing and External Conditions gate in `product-launch-azimuth.md`.** New section covering competitive timing, regulatory/compliance clearance, platform dependencies, and market condition changes. Any "Unknown" is flagged explicitly — unknown competitive or regulatory timing is an information gap, not a safe default.

- **`references/org-change-patterns.md`.** Six structural failure patterns for restructures, role eliminations, and organizational change programs. Distinct from Kotter's process failure modes (already in `base-rates.md`) and from `references/ma-partnership-patterns.md`. Patterns: Symbolic Restructure, Change Fatigue Stacking, Informal Authority Network Destruction, Communication Sequencing Failure, Behavioral Change Timeline Compression, Accountability Transfer Gap.

- **Layer 3 routing: domain options 6 and 7 — Org change / restructure; Build vs. Buy vs. Partner.** DEEP mode loads `references/org-change-patterns.md` for org change. Build/buy/partner routes to `templates/build-buy-partner-azimuth.md`, which emits a CARRY FORWARD block for handoff to `templates/codebase-azimuth.md` or `templates/partnership-azimuth.md` after path selection.

### Changed

- **`gotchas.md` §7: Survivorship Framing → Plan-Revision Gap.** Survivorship Framing is substantively covered by Module 7 (Base Rate Reality Check) and the availability bias externalization added this release. Plan-revision gap has zero coverage elsewhere and HIGH empirical confidence (Roose 2023, N=68 real teams): surfacing a risk is not the same as acting on it. Teams consistently identify risks and generate mitigations but fail to revise plans when remediation requires reducing scope.

- **Routing redirects tightened.** Out-of-scope responses state only what AZIMUTH cannot do and why. No alternative framings offered, no guidance on deriving missing information. AZIMUTH is not an oracle.

- **Verdict taxonomy standardized across templates.** `product-launch-azimuth.md` used SOFT LAUNCH (→ PILOT FIRST) and CANCEL (→ REJECT). `hiring-azimuth.md` used EXTEND PROCESS (→ PILOT FIRST) and DELAY HIRE (→ DELAY PENDING EVIDENCE) and PROCEED WITH ONBOARDING SAFEGUARDS (→ PROCEED WITH SAFEGUARDS). All templates now use the Module 10 canonical verdict names with domain-specific context in the description.

### Added — domain templates

- **`templates/secondaries-ic-azimuth.md`** — IC recommendation template for PE secondaries investment partners evaluating GP-led continuation vehicles, direct secondaries, and minority recaps. Includes: adverse selection gate (run before committing diligence resources), process integrity gate with ILPA 2023 minimum standards (binary kill gate independent of asset quality), NAV reliability assessment with Whitehorse Liquidity Partners 28%-uplift finding, GP quality and alignment signals with relationship bias check, and pricing discipline table with stress-case IRR modeling. Verdict taxonomy: COMMIT-AT-PRICE / BID-BELOW-INDICATED (auction) / COUNTER-AT-PRICE (bilateral) / CONDITIONAL-ON-TERMS / PASS-PROCESS / PASS-PRICING. PASS-PROCESS legal grounding: ADIC v. EMG, C.A. No. 2025-1389-NAC (Del. Ch. December 2025).

- **`templates/org-change-azimuth.md`** — Pre-commitment analysis template for restructures, consolidations, role eliminations, and leadership transitions. Pre-commitment gates (3 binary checks: announcement fixed → RESIDUAL-RISK-REGISTER; no measurable metric → INSUFFICIENT SIGNAL; designer accountability gap → flagged). Incentive alignment scan with 6 actor matrix (proposer, HR, senior leaders gaining/losing authority, external consultants, middle management). Sections: Change Context, Failure Path Analysis drawing from `references/org-change-patterns.md`, Behavioral Change Readiness (structural vs. behavioral change gap), Communication Plan Readiness with manager preparation as highest-trust channel, Accountability Transfer table. Verdict taxonomy: Module 10 canonical names.

- **`templates/build-buy-partner-azimuth.md`** — Path selection template for capability acquisition decisions. Anchoring assessment forces comparative analysis when Module 4 returns YELLOW or RED on [IDENTITY] or [DISSENT]. Module 4 runs once with path-advocate matrix (6 actors: proposer, engineering/CTO, corp dev/M&A, BD/partnerships, finance, board). Three sequential path viability gates (Build: skills + differentiation + timeline + opportunity cost; Buy: target availability + integration plan + deal thesis + talent retention; Partner: aligned partners + switching cost + IP ownership + dependency asymmetry). Comparative analysis across 7 dimensions. Verdict format: `RECOMMENDED PATH: [BUILD / BUY / PARTNER] — [standard verdict]`. CARRY FORWARD block transfers Module 4 context (tier, proposer identity, top unresolved assumption) to the domain template (`templates/codebase-azimuth.md` or `templates/partnership-azimuth.md`) and triggers Bypass Handling to skip Module 4 re-interview on GREEN tier.

---

## [1.1.2] — 2026-05-05

### Added

- **Counterfactual layer (Module 2).** After classifying assumptions as strong / partial / unsupported, Module 2 now runs a Falsifiers pass: for each strong or partial assumption, names the specific, observable evidence that would prove it wrong. Falsifiers must be concrete and measurable — not "if it doesn't work" but a named metric and threshold. Unsupported assumptions are excluded (already flagged for validation). Output: new Falsifiers section, positioned after Weak Assumptions, with standard omit-if-empty rule.
- **Coupling pass (Module 6).** After constructing the 3 most plausible independent failure chains, Module 6 now identifies pair-interactions where two risks activating together produce a materially worse outcome than either alone. The mechanism must be specific: one risk blocks the other's recovery path, or one masks the other's visible signal. 3–5 interactions maximum; omit if no genuine multiplicative interactions exist. Output: new Interaction Effects section, positioned after Likely Failure Paths, with standard omit-if-empty rule.

---

## [1.1.1] — 2026-05-05

### Added

- **INSUFFICIENT SIGNAL verdict state.** Module 10 now refuses to return a verdict when the input is too sparse, vague, or contradictory to support honest analysis. Trigger conditions defined: missing core inputs (objective, scope, reversibility, downside), undefined objective that blocks assumption audit, internal contradiction requiring user resolution, or any standard verdict requiring invented facts. Returns only a Missing Inputs section — no verdict, no confidence level, no mitigations.
- **Output format annotations.** All sections that must be omitted on INSUFFICIENT SIGNAL are now marked explicitly in the output format block.
- **Anti-slop rule.** Prohibits substituting DELAY PENDING EVIDENCE for INSUFFICIENT SIGNAL when the block is missing input, not missing time.
- **Escalation Logic entry.** INSUFFICIENT SIGNAL gets its own escalation rule: if input is too sparse to ground any verdict, return INSUFFICIENT SIGNAL; do not soften into DELAY PENDING EVIDENCE.

### Added — domain coverage

- **`references/ma-partnership-patterns.md`** — 8 M&A and partnership failure patterns with diagnostic questions: Strategic Rationale Substitution, Integration Timeline Compression, Synergy Overestimation, Key Talent Flight, Due Diligence Gap, Partnership Incentive Drift, Dependency Lock-In, Governance Vacuum Post-Close.
- **`templates/partnership-azimuth.md`** — Analysis template for M&A, acquisitions, strategic partnerships, and significant vendor relationships.
- **`SKILL.md` DEEP mode routing** — M&A / partnerships now routes to `references/ma-partnership-patterns.md`; Output Format section now includes Partnership / M&A format pointing to `templates/partnership-azimuth.md`.

---

## [1.1.0] — 2026-05-04

This release implements the full set of fixes surfaced in the v1.0.0 independent audit. No breaking changes for users invoking the skill manually; behavior changes apply to automatic invocation and to default output structure.

### Changed — invocation behavior

- **Tightened SKILL.md frontmatter description** (669 → 489 chars). Removed over-broad triggers ("validate our plan," "timeline check," "user sounds overconfident/vague"). Now requires explicit user request to evaluate an initiative-level decision with meaningful downside. Added explicit `Do NOT invoke for…` clause to the description itself, not just the body.
- **Added explicit mode-selection signals** for FAST / STANDARD / DEEP. Previously the body described when to use each mode but did not give Claude concrete decision rules. Now lists specific signals (reversibility, capital outlay, headcount changes, public exposure, scope window, user phrasing) per mode. Default escalation rule: when signals conflict, escalate; never silently downgrade.
- **Defined diagnostic-loading rule for STANDARD mode.** Previously per-module instructions (`for deep runs, load X`) conflicted with the global DEEP-mode instruction. Diagnostics now load conditionally in STANDARD when the corresponding module surfaces a high-severity finding. DEEP continues to load all four diagnostics. Removed the redundant per-module load lines from Modules 2, 4, 5, 7, and 8.

### Changed — output structure

- **Output now leads with the verdict.** First three lines of every output: verdict line, recommended decision, confidence level. Reader must be able to act on the first paragraph alone.
- **Empty sections now omitted by default.** A section header with no substantive content is a failure of the skill, not a feature. Padding is explicitly prohibited.
- **Added Module Output Reduction section.** Modules 2, 5, 6, 7, and 8 share an underlying register of assumptions, dependencies, and risks. Output is now deduplicated across modules rather than emitting per-module dumps. Critical Risks section is the severity-ordered output of the register.

### Changed — content

- **Compressed gotchas from 12 patterns to 8.** Removed: Availability Illusion (duplicated Module 5 + fragility-scan indicator 6), Quiet Dependency (duplicated Module 5), Confidence-Competence Gap (overlapped assumption-audit + incentive-conflicts), Integration Tax (already covered in `software-failure-patterns.md` patterns 2 and 4). Renumbered remaining 8.
- **Rewrote `references/base-rates.md` with proper attribution.** Every numeric claim is now cited to a real primary or widely cited secondary source (BLS Business Employment Dynamics, CB Insights post-mortem reports, McKinsey/Oxford BT Centre 2012 IT projects study, Standish CHAOS, Pendo Feature Adoption, Kotter, Schmidt & Hunter, Christensen). Numbers without defensible sourcing are softened from precise to ranged with hedged language. The legacy-rewrite "70–80% failure rate" claim is reframed against the McKinsey/Oxford finding rather than Joel Spolsky's opinion piece. Each section ends with a Sources block.

### Fixed

- **Resolved "precommitment" / "pre-commitment" inconsistency.** Standardized on "pre-commitment" across SKILL.md frontmatter, README.md, and MARKETING.md.
- **Fixed README brand-clarity confusion.** "Most azimuth tools for AI agents…" was using the proper noun as a generic, which read as forced to anyone who didn't already know the brand. Changed to "code-focused agent skills" — clearer prose, doesn't name competitors.

### Verification before push

- SKILL.md frontmatter description: 489 chars (under 500-char installer limits).
- All file paths in SKILL.md (`references/`, `diagnostics/`, `templates/`) match folder structure on disk.
- All 14 files present and structurally valid.

---

## [1.0.0] — 2026-05-04

### Initial release

**Core skill**
- 10-module azimuth analysis engine (FAST / STANDARD / DEEP operating modes)
- Decision verdict framework: PROCEED / PROCEED WITH SAFEGUARDS / PILOT FIRST / REDUCE SCOPE / DELAY PENDING EVIDENCE / REJECT
- Anti-slop enforcement: weak mitigations rejected, generic risk lists prohibited

**Reference files**
- `base-rates.md` — Historical failure rates across software projects, startups, launches, hiring, M&A, and org change
- `startup-failures.md` — 8 startup-specific failure patterns with diagnostic questions
- `software-failure-patterns.md` — 10 engineering/technical failure patterns
- `launch-risks.md` — Pre/during/post launch risk zones

**Diagnostic files**
- `assumption-audit.md` — 5-step assumption classification and validation gating process
- `dependency-map.md` — Full dependency inventory, assessment matrix, concentration risk identification
- `incentive-conflicts.md` — 7-category incentive conflict scan with severity classification
- `fragility-scan.md` — 6-indicator structural fragility scoring (LOW / MEDIUM / HIGH / CRITICAL)

**Templates**
- `executive-azimuth.md` — 1-page leadership briefing format
- `codebase-azimuth.md` — Refactor, migration, and engineering initiative template
- `product-launch-azimuth.md` — Launch readiness gate matrix with rollback protocol
- `hiring-azimuth.md` — Role definition audit and candidate failure path analysis

**Structural file** — `gotchas.md` — 12 structural failure patterns that consistently evade standard checklists
