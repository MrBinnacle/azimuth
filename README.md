# AZIMUTH

> Verify your direction before you commit movement. Wrong bearing at the start compounds into wrong objective at the end.

**Decision-quality pre-commitment analysis for operators who can't afford to be wrong about direction.**

![Version](https://img.shields.io/badge/version-v1.2.0-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-blueviolet) ![Claude.ai](https://img.shields.io/badge/Claude.ai-compatible-blueviolet)

An azimuth is a navigational bearing — the angle you lock in before you step off. Get it wrong by a few degrees at the start and you're miles from your objective by the end. AZIMUTH the skill does the same thing for decisions: it finds the drift, the false assumptions, and the structural failure modes before you're committed and downrange.

Built for **Claude Code and Claude.ai.** Designed for operators, PMs, founders, and senior engineers making decisions with real downside — not just code review.

---

## Quick Start

```
npx skills add https://github.com/MrBinnacle/azimuth
```

Then invoke on any decision:

```
/azimuth We're launching the new product next week
/azimuth Should we rewrite the legacy service?
/azimuth I'm considering making this hire
/azimuth We're deciding whether to build, buy, or partner for this capability
/azimuth Pressure test our Q3 timeline
```

The skill activates automatically on decision-quality queries. No configuration required.

---

## What this is

Most agent skills answer one question: *will this code break?*

This one answers a different question: *should we do this at all, and if so, what needs to change before we commit?*

It covers the full decision surface — technical *and* strategic:

| Scenario | What you get |
| --- | --- |
| Product launch | Readiness gate checklist, market timing gates, rollback triggers, launch metrics by segment |
| Rewrite / migration | Breakpoint zones, hidden couplings, safe rollout path |
| Key hire | Role definition audit, failure path construction, onboarding readiness |
| Partnership / M&A / vendor | Incentive conflict scan, dependency fragility, integration governance |
| Build vs. buy vs. partner | Path viability gates, anchoring detection, comparative analysis, domain handoff |
| Org change / restructure | Pre-commitment gates, behavioral change readiness, accountability transfer, communication plan |
| PE secondaries IC decision | Adverse selection gate, NAV reliability assessment, process integrity kill gate, validated verdict taxonomy |
| Timeline commitment | Base rate reality check, constraint dominance, scope drift risk |
| Strategic bet | Assumption audit with falsifiers, structural fragility score, pair-interaction failure analysis |

---

## How it works

**Intake routing** fires first — three layers of triage before the analysis pipeline runs:

- **Layer 1** — Purpose: stress-test a plan, validate a post-decision, explore pre-plan? Only pre-commitment decisions proceed.
- **Layer 2** — Stakes and reversibility map to operating mode.
- **Layer 3** — Domain routes to the correct template.

**Four operating modes**, auto-selected by stakes and context:

```
FAST    → Objective Check + Top 3 Failure Paths + Verdict
STANDARD → Full 10-module analysis (default)
RAPID   → Full depth on Modules 1, 4, 8, 10 — abbreviated on 2, 3, 5, 6, 9 (24-hour deadlines)
DEEP    → All modules + loads domain reference files + gotchas
```

**The 10-module analysis:**

1. **Objective Integrity Check** — Is this the right problem or symptom treatment? Classifies input as pre-commitment, post-commitment, or non-decision.
2. **Assumption Audit** — Classified: strong / partial / unsupported / contradicted
   → **Falsifiers pass**: names the specific observable evidence that would prove each strong or partial assumption wrong
3. **Constraint Reality Check** — Which constraint most likely dominates outcome?
4. **Incentive Scan & Interview** — Seven structured questions collect incentive context directly from the user before any inference. GREEN / YELLOW / RED tiering with enforced consequences.
5. **Dependency Fragility Map** — What's a single point of failure? What's secured vs. assumed?
6. **Failure Path Construction** — Trigger → Cascade → Visible Failure → Business Cost
   → **Coupling pass**: identifies pair-interactions where two risks together produce nonlinear failure
7. **Base Rate Reality Check** — How do similar initiatives actually fail historically? Backpropagation check ensures historically common failure modes appear in Module 6 chains.
8. **Detectability & Recovery** — Which risks are found late and hard to reverse?
9. **Mitigation Design** — Structural changes only. Weak mitigations rejected.
10. **Decision Verdict** — Full verdict taxonomy (see below). Pre-verdict check enforces Module 4 tier before any verdict is selected.

---

## Verdict taxonomy

| Verdict | When it fires |
| --- | --- |
| `PROCEED` | Evidence supports moving forward; risks are manageable |
| `PROCEED WITH SAFEGUARDS` | Proceed only if specific structural changes are made |
| `PILOT FIRST` | Validate the highest-risk assumption before committing full scope |
| `REDUCE SCOPE` | Current scope is not supportable; a smaller version may be |
| `DELAY PENDING EVIDENCE` | Decision is premature; specific information is needed |
| `REJECT` | Evidence or structure does not support proceeding |
| `INSUFFICIENT SIGNAL` | Input is too sparse, vague, or contradictory to ground analysis — proceeding would substitute fabrication for analysis |
| `WRONG TOOL` | Input is not a pre-commitment decision question (architecture review, code quality, fact-finding, or pure exploration) |
| `RESIDUAL-RISK-REGISTER` | Decision is already made or execution substantially underway — go/no-go analysis is no longer applicable |

> **INSUFFICIENT SIGNAL** is not **DELAY PENDING EVIDENCE**. DELAY means the decision is premature but inputs are coherent. INSUFFICIENT SIGNAL means no analysis module can be grounded in what was provided.
>
> **WRONG TOOL** and **RESIDUAL-RISK-REGISTER** are firm exits — the skill states what the input is and what AZIMUTH requires. No analysis, no reframe suggestion.

---

## Example output

<details>
<summary>Legacy billing rewrite — PILOT FIRST verdict</summary>

**Input:** *"We're planning to rewrite our legacy billing service in Q3. 8 weeks, 2 engineers."*

**Output (abbreviated):**

```
## Azimuth Verdict
High-risk. Scope and timeline are inconsistent with known base rates for legacy rewrites.
Do not proceed without scope reduction and a validated rollback strategy.

## Recommended Decision
PILOT FIRST — Rewrite one isolated billing module with full rollback. Validate
assumptions about coupling before committing full scope.

## Confidence Level
High — base rate for legacy rewrites exceeding estimate is well-documented.
No evidence present that shifts this.

## Critical Risks
1. Integration tax — Parallel-running old and new systems historically extends to 3–5×
   estimated cutover time. No hard deprecation date defined.
2. Knowledge concentration — Single-person domain knowledge on billing logic creates
   SPOF. No fallback owner named.
3. Scope creep under deadline — "While we're at it" rewrites reliably overload scope.
   No change control mechanism defined.

## Falsifiers
- Knowledge concentration: A second engineer can document and reproduce billing edge
  case behavior independently within 2 weeks — or the SPOF is real.
- Timeline estimate: Comparable module rewrite completed within 2 weeks in a spike —
  or the 8-week total is unsupportable.

## Interaction Effects
- Integration tax + deadline pressure: When cutover extends beyond week 6, the
  remaining 2 weeks compress QA and rollback validation simultaneously — neither
  gets adequate time, and the failure modes compound rather than queue.

## Likely Failure Paths
- Billing edge cases surface in testing → scope expands → 8 weeks becomes 20 →
  old system maintenance + new system debt → both teams overloaded → defects in prod
```

</details>

---

## Core anti-patterns this skill rejects

- Generic risk lists padded to 10+ items
- Weak mitigations ("communicate better," "monitor closely")
- Treating all risks as equally probable
- Defaulting to PROCEED when evidence is thin
- Substituting DELAY PENDING EVIDENCE for INSUFFICIENT SIGNAL when the problem is missing input, not missing time
- Returning a verdict when analysis would require inventing facts the user did not supply
- Producing go/no-go analysis for inputs that are not pre-commitment decision questions
- Softening verdicts when Module 4 interview is incomplete (RED tier blocks PROCEED and PROCEED WITH SAFEGUARDS)

---

## What's inside

<details>
<summary>Full file tree</summary>

```
azimuth/
├── SKILL.md                              # Core skill — intake routing + 10-module analysis engine
├── gotchas.md                            # 8 structural failure patterns that evade standard checklists
├── references/
│   ├── base-rates.md                     # Historical failure rates: software, startups, launches, hiring, M&A, org change
│   ├── startup-failures.md               # 8 startup-specific failure patterns with diagnostic questions
│   ├── software-failure-patterns.md      # 10 engineering failure patterns with azimuth questions
│   ├── launch-risks.md                   # Pre/during/post launch risk zones with signal and mitigation
│   ├── ma-partnership-patterns.md        # 8 M&A and partnership failure patterns with diagnostic questions
│   └── org-change-patterns.md            # 6 org change and restructure failure patterns
├── diagnostics/
│   ├── assumption-audit.md               # 5-step: extract → classify → risk-score → validate → gate
│   ├── dependency-map.md                 # Full inventory, assessment matrix, concentration risk
│   ├── incentive-conflicts.md            # 7 conflict categories, severity classification
│   └── fragility-scan.md                # 6 structural fragility indicators → LOW/MEDIUM/HIGH/CRITICAL
├── templates/
│   ├── executive-azimuth.md              # 1-page format for leadership briefings
│   ├── codebase-azimuth.md               # Refactor/migration/rewrite template
│   ├── product-launch-azimuth.md         # Launch readiness gate matrix + rollback protocol
│   ├── hiring-azimuth.md                 # Role definition audit + candidate failure path analysis
│   ├── partnership-azimuth.md            # M&A, acquisitions, strategic partnerships, vendor relationships
│   ├── secondaries-ic-azimuth.md         # PE secondaries IC recommendation template
│   ├── org-change-azimuth.md             # Restructure, consolidation, role elimination, leadership transition
│   └── build-buy-partner-azimuth.md      # Path selection: build vs. buy vs. partner with domain handoff
└── examples/
    ├── case-study-healthcare-gov.md      # Healthcare.gov DEEP mode run — 5/6 recall, 0 false positives
    └── case-study-open-source-launch-timing.md  # STANDARD mode — solo dev timing a repo launch during job search
```

</details>

---

## Install

**Claude Code / Claude.ai skills:**

```
npx skills add https://github.com/MrBinnacle/azimuth
```

Or manually:

```
git clone https://github.com/MrBinnacle/azimuth.git
mkdir -p ~/.claude/skills
cp -r azimuth ~/.claude/skills/
```

---

## Compatibility

| Agent | Supported |
| --- | --- |
| Claude Code | ✓ |
| Claude.ai | ✓ |

Auto-invocation, intake routing, and template activation depend on the Claude skills system. Other agents can read the markdown files as reference material, but that is not equivalent to running AZIMUTH.

---

## Contributing

Issues and PRs welcome. Priority areas: additional domain templates, base rate data improvements with primary source citations, and domain-specific gotchas grounded in documented failure cases.

---

## License

MIT

---

*Built on Gary Klein's prospective hindsight methodology and structured analytic technique traditions. The name comes from land navigation: an azimuth is the bearing you verify before you step off. Get it wrong at the start and no amount of execution excellence puts you on the right objective.*

*Designed for operators making irreversible decisions under uncertainty.*
