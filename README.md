# AZIMUTH

> *An azimuth is the bearing you lock in before you step off. Wrong by a few degrees at the start — miles from your objective by the end.*

**Decision-quality pre-commitment analysis for operators who can't afford to be wrong about direction.**

Built for Claude Code, Claude.ai, Codex, Gemini CLI, Cursor, and all major AI coding agents. Designed for operators, PMs, founders, and senior engineers making go/no-go calls with real downside.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## See it in action

**Input:** *"We're planning to rewrite our legacy billing service in Q3. 8 weeks, 2 engineers."*

```
Azimuth Verdict
High-risk. Scope and timeline are inconsistent with known base rates for legacy rewrites.
Do not proceed without scope reduction and a validated rollback strategy.

Recommended Decision: PILOT FIRST
Rewrite one isolated billing module with full rollback. Validate assumptions about
coupling before committing full scope.

Confidence: High — base rate for legacy rewrites exceeding estimate: 70–80%.
No evidence present that shifts this.

Critical Risks
1. Integration tax — Parallel-running old and new systems historically extends to 3–5×
   estimated cutover time. No hard deprecation date defined.
2. Knowledge concentration — Single-person domain knowledge on billing logic creates
   SPOF. No fallback owner named.
3. Scope creep under deadline — "While we're at it" rewrites reliably overload scope.
   No change control mechanism defined.

Likely Failure Paths
- Billing edge cases surface in testing → scope expands → 8 weeks becomes 20 →
  old system maintenance + new system debt → both teams overloaded → defects in prod
```

---

## Install

```bash
npx skills add https://github.com/MrBinnacle/azimuth
```

<details>
<summary>Manual install / other agents</summary>

```bash
git clone https://github.com/MrBinnacle/azimuth.git
mkdir -p ~/.claude/skills
cp -r azimuth ~/.claude/skills/
```

For Codex, Gemini CLI, Cursor, Copilot — copy the `azimuth/` directory to your agent's skills folder.

</details>

After install, invoke directly:

```
/azimuth We're launching the new product next week
/azimuth Should we rewrite the legacy service?
/azimuth I'm considering making this hire
/azimuth Pressure test our Q3 timeline
```

**Compatible with:** Claude Code · Claude.ai · Codex · Gemini CLI · Cursor · GitHub Copilot · Windsurf · OpenCode

---

## What it covers

Most agent skills answer: *will this code break?*

This one answers: *should we do this at all — and if so, what needs to change before we commit?*

| Scenario | What you get |
|----------|-------------|
| Product launch | Readiness gate checklist, rollback triggers, launch metrics by segment |
| Rewrite / migration | Breakpoint zones, hidden couplings, safe rollout path |
| Key hire | Role definition audit, failure path construction, onboarding readiness |
| Partnership / vendor | Incentive conflict scan, dependency fragility assessment |
| Timeline commitment | Base rate reality check, constraint dominance, scope drift risk |
| Strategic bet | Assumption audit with validation gating, structural fragility score |

---

## How it works

Three modes, auto-selected by stakes and context:

```
FAST      → Objective Check + Top 3 Failure Paths + Verdict
STANDARD  → Full 10-module analysis (default)
DEEP      → All modules + domain reference files + gotchas
```

The 10-module core:

1. **Objective Integrity Check** — Is this the right problem or symptom treatment?
2. **Assumption Audit** — What must be true for success? Classified: strong / partial / unsupported / contradicted
3. **Constraint Reality Check** — Which constraint most likely dominates outcome?
4. **Incentive Scan** — Who benefits from poor decisions, drift, or concealment?
5. **Dependency Fragility Map** — What's a single point of failure? What's actually secured vs. assumed?
6. **Failure Path Construction** — Trigger → Cascade → Visible Failure → Business Cost
7. **Base Rate Reality Check** — How do similar initiatives actually fail historically?
8. **Detectability & Recovery** — Which risks are found late and hard to reverse?
9. **Mitigation Design** — Structural changes only. Weak mitigations rejected.
10. **Decision Verdict** — PROCEED / PILOT FIRST / REDUCE SCOPE / DELAY / REJECT / INSUFFICIENT SIGNAL

---

## What's inside

```
azimuth/
├── SKILL.md                          # Core skill — 10-module analysis engine
├── gotchas.md                        # 8 structural failure patterns that evade standard checklists
├── references/
│   ├── base-rates.md                 # Historical failure rates: software, startups, launches, hiring, M&A
│   ├── startup-failures.md           # 8 startup-specific failure patterns with diagnostic questions
│   ├── software-failure-patterns.md  # 10 engineering failure patterns
│   ├── launch-risks.md               # Pre/during/post launch risk zones with signal and mitigation
│   └── ma-partnership-patterns.md    # 8 M&A and partnership failure patterns with diagnostic questions
├── diagnostics/
│   ├── assumption-audit.md           # 5-step process: extract → classify → risk-score → validate → gate
│   ├── dependency-map.md             # Full inventory, assessment matrix, concentration risk
│   ├── incentive-conflicts.md        # 7 conflict categories, severity classification
│   └── fragility-scan.md            # 6 structural fragility indicators → LOW/MEDIUM/HIGH/CRITICAL score
├── templates/
│   ├── executive-azimuth.md          # 1-page format for leadership briefings
│   ├── codebase-azimuth.md           # Refactor/migration/rewrite template
│   ├── product-launch-azimuth.md     # Launch readiness gate matrix + rollback protocol
│   ├── hiring-azimuth.md             # Role definition audit + candidate failure path analysis
│   └── partnership-azimuth.md        # M&A and partnership analysis template
├── examples/
│   └── case-study-healthcare-gov.md  # Healthcare.gov October 2013 — DEEP mode retrospective
└── evals/                            # Falsifiable test cases and scored baselines gating v1.1.x changes
```

---

## Why this is different

Most pre-commitment skills for AI agents are built around code review — they ask *what's wrong with this implementation?* This skill asks *what's wrong with this decision?*

It covers the full stack of how initiatives fail: incentive misalignment, political timelines, unvalidated demand, dependency concentration, and the 8 structural gotchas that survive standard checklists.

**What it explicitly rejects:**

- Generic risk lists padded to 10+ items
- Weak mitigations ("communicate better," "monitor closely")
- Treating all risks as equally probable
- Defaulting to PROCEED when evidence is thin
- Recommending "proceed with caution" when the right call is stop

---

## Contributing

Issues and PRs welcome. Priority areas: additional domain templates (compliance, infrastructure, org change), base rate data improvements, and domain-specific gotchas.

---

## License

MIT

---

*Built on Gary Klein's prospective hindsight methodology and structured analytic technique traditions. Designed for operators making irreversible decisions under uncertainty.*
