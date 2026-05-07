# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

Planned. See `ROADMAP.md` for the why on each.

- **Evidence tags.** Every output claim carries a provenance tag.
- **Audit trail.** Output lists modules run and what each surfaced.

---

## [1.2.0] — 2026-05-07

### Added

- **Intake Routing (pre-analysis triage).** Three-layer triage fires before the 10-module pipeline: Layer 1 maps situation type to mode (stress-test → proceed; post-decision validation or pre-plan exploration → firm out-of-scope exits); Layer 2 maps stakes and reversibility to FAST / STANDARD / DEEP / RAPID; Layer 3 routes domain to the correct template. Bypass handling for users who supply structured context directly: infers mode and template, states inference explicitly, proceeds to Module 4 interview before full analysis.

- **Module 4 expanded to Incentive Scan & Interview.** Seven structured questions collect incentive context directly from the user before any inference from plan text. GREEN / YELLOW / RED response tiering with enforced consequences: RED tier (proposer identity skipped or fewer than 5 of 7 answered) locks Module 10 verdict confidence at LOW and removes PROCEED and PROCEED WITH SAFEGUARDS as available verdicts. Output quality is proportional to what the user brings — by design.

- **Module 10 RED-tier enforcement.** Pre-verdict check now tests Module 4 interview tier before verdict selection. PROCEED verdicts are blocked at Module 10, not just declared in Module 4.

- **RAPID mode.** For high-stakes or irreversible decisions under 24-hour time constraints. Modules 1, 4, 8, 10 at full depth; Modules 2, 3, 5, 6, 9 abbreviated. Rationale: time pressure amplifies deadline-politics incentive distortion and concentrates the value of reversibility analysis — the modules that matter most under pressure are the ones FAST omits.

- **FAST mode disclosure.** FAST outputs now explicitly state that Module 4 interview was not conducted and incentive misalignment is unverified.

- **LLM bias externalizations at four modules.** Inline, mechanism-specific callouts above section content (not footer disclaimers): sycophancy circuit-breaker at Module 2 (treat the assumption the plan most depends on as first candidate for UNSUPPORTED), availability inversion at Module 6 (after 3 canonical chains, construct one that routes around all of them), domain calibration boundary at Module 7 (degrade to directional-only when domain match is poor), verdict softening pre-check at Module 10 (name the most commitment-coupled assumption and its evidence classification before selecting the verdict).

- **STANDARD mode conditional `gotchas.md` load.** gotchas.md now loads in STANDARD when Module 4 returns RED tier or when Module 6 failure chains match only canonical patterns. DEEP mode retains always-load. Audit finding: the 8 gotchas are most operative for motivated-reasoning inputs — precisely the inputs DEEP mode is hardest to trigger for.

- **Structured Failure Analysis section in `references/base-rates.md`.** Empirical grounding for premortem-class analysis: Fasolo, Heard & Scopelliti 2025 (debiasing taxonomy, scope conditions, evidence ceiling — Journal of Management); Roose, Lehman & Veinott 2023 (17.8 failure reasons/session, 16.7 mitigations/session, plan-revision gap — Human Factors).

### Changed

- **`gotchas.md` §7: Survivorship Framing → Plan-Revision Gap.** Survivorship Framing is substantively covered by Module 7 (Base Rate Reality Check) and the availability bias externalization added this release. Plan-revision gap has zero coverage elsewhere and HIGH empirical confidence (Roose 2023, N=68 real teams): surfacing a risk is not the same as acting on it. Teams consistently identify risks and generate mitigations but fail to revise plans when remediation requires reducing scope.

- **Routing redirects tightened.** Out-of-scope responses state only what AZIMUTH cannot do and why. No alternative framings offered, no guidance on deriving missing information. AZIMUTH is not an oracle.

### Added — domain coverage (unversioned, shipped between releases)

- **`templates/secondaries-ic-azimuth.md`** — IC recommendation template for PE secondaries investment partners evaluating GP-led continuation vehicles, direct secondaries, and minority recaps. Includes: adverse selection gate (run before committing diligence resources), process integrity gate with ILPA 2023 minimum standards (binary kill gate independent of asset quality), NAV reliability assessment with Whitehorse Liquidity Partners 28%-uplift finding, GP quality and alignment signals with relationship bias check, and pricing discipline table with stress-case IRR modeling. Verdict taxonomy: COMMIT-AT-PRICE / BID-BELOW-INDICATED (auction) / COUNTER-AT-PRICE (bilateral) / CONDITIONAL-ON-TERMS / PASS-PROCESS / PASS-PRICING. PASS-PROCESS legal grounding: ADIC v. EMG, C.A. No. 2025-1389-NAC (Del. Ch. December 2025).

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
