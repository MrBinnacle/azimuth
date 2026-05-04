# AZIMUTH

> Verify your direction before you commit movement. Wrong bearing at the start compounds into wrong objective at the end.

**Decision-quality pre-commitment analysis for operators who can't afford to be wrong about direction.**

An azimuth is a navigational bearing — the angle you lock in before you step off. Get it wrong by a few degrees at the start and you're miles from your objective by the end. AZIMUTH the skill does the same thing for decisions: it finds the drift, the false assumptions, and the structural failure modes before you're committed and downrange.

Built for **Claude Code, Claude.ai, Codex, Gemini CLI, Cursor, and all major AI coding agents.** Designed for operators, PMs, founders, and senior engineers making decisions with real downside — not just code review.

---

## What this is

Most azimuth tools for AI agents answer one question: *will this code break?*

This one answers a different question: *should we do this at all, and if so, what needs to change before we commit?*

It covers the full decision surface — technical *and* strategic:

| Scenario | What you get |
|----------|-------------|
| Product launch | Readiness gate checklist, rollback triggers, launch metrics by segment |
| Rewrite / migration | Breakpoint zones, hidden couplings, safe rollout path |
| Key hire | Role definition audit, failure path construction, onboarding readiness |
| Partnership / vendor | Incentive conflict scan, dependency fragility assessment |
| Timeline commitment | Base rate reality check, constraint dominance, scope drift risk |
| Strategic bet | Assumption audit with validation gating, structural fragility score |

---

## Install

**Claude Code / Claude.ai skills:**

```bash
npx skills add https://github.com/MrBinnacle/azimuth
```

Or manually:

```bash
git clone https://github.com/MrBinnacle/azimuth.git
mkdir -p ~/.claude/skills
cp -r azimuth ~/.claude/skills/
```

**Codex, Gemini CLI, Cursor, Copilot:**

```bash
git clone https://github.com/MrBinnacle/azimuth.git
# Copy azimuth/ to your agent's skills directory
```

After install, the skill activates automatically on decision-quality queries. Or invoke directly:

```
/azimuth We're launching the new product next week
/azimuth Should we rewrite the legacy service?
/azimuth I'm considering making this hire
/azimuth Pressure test our Q3 timeline
```

---

## How it works

Three operating modes auto-selected by stakes and context:

```
FAST    → Objective Check + Top 3 Failure Paths + Verdict
STANDARD → Full 10-module analysis (default)
DEEP    → All modules + loads domain reference files + gotchas
```

The 10-module core analysis:

1. **Objective Integrity Check** — Is this the right problem or symptom treatment?
2. **Assumption Audit** — What must be true for success? Classified: strong / partial / unsupported / contradicted
3. **Constraint Reality Check** — Which constraint most likely dominates outcome?
4. **Incentive Scan** — Who benefits from poor decisions, drift, or concealment?
5. **Dependency Fragility Map** — What's a single point of failure? What's actually secured vs. assumed?
6. **Failure Path Construction** — Trigger → Cascade → Visible Failure → Business Cost
7. **Base Rate Reality Check** — How do similar initiatives actually fail historically?
8. **Detectability & Recovery** — Which risks are found late and hard to reverse?
9. **Mitigation Design** — Structural changes only. Weak mitigations rejected.
10. **Decision Verdict** — PROCEED / PILOT FIRST / REDUCE SCOPE / DELAY / REJECT

---

## What's inside

```
azimuth/
├── SKILL.md                          # Core skill — 10-module analysis engine
├── gotchas.md                        # 12 structural failure patterns that evade standard checklists
├── references/
│   ├── base-rates.md                 # Historical failure rates: software, startups, launches, hiring, M&A
│   ├── startup-failures.md           # 8 startup-specific failure patterns with diagnostic questions
│   ├── software-failure-patterns.md  # 10 engineering failure patterns with azimuth questions
│   └── launch-risks.md               # Pre/during/post launch risk zones with signal and mitigation
├── diagnostics/
│   ├── assumption-audit.md           # 5-step process: extract → classify → risk-score → validate → gate
│   ├── dependency-map.md             # Full inventory, assessment matrix, concentration risk
│   ├── incentive-conflicts.md        # 7 conflict categories, severity classification
│   └── fragility-scan.md            # 6 structural fragility indicators → LOW/MEDIUM/HIGH/CRITICAL score
└── templates/
    ├── executive-azimuth.md        # 1-page format for leadership briefings
    ├── codebase-azimuth.md         # Refactor/migration/rewrite template
    ├── product-launch-azimuth.md   # Launch readiness gate matrix + rollback protocol
    └── hiring-azimuth.md           # Role definition audit + candidate failure path analysis
```

---

## Example output

**Input:** *"We're planning to rewrite our legacy billing service in Q3. 8 weeks, 2 engineers."*

**Output (abbreviated):**

```
## Azimuth Verdict
High-risk. Scope and timeline are inconsistent with known base rates for legacy rewrites.
Do not proceed without scope reduction and a validated rollback strategy.

## Critical Risks
1. Integration tax — Parallel-running old and new systems historically extends to 3–5×
   estimated cutover time. No hard deprecation date defined.
2. Knowledge concentration — Single-person domain knowledge on billing logic creates
   SPOF. No fallback owner named.
3. Scope creep under deadline — "While we're at it" rewrites reliably overload scope.
   No change control mechanism defined.

## Likely Failure Paths
- Billing edge cases surface in testing → scope expands → 8 weeks becomes 20 →
  old system maintenance + new system debt → both teams overloaded → defects in prod

## Recommended Decision
PILOT FIRST — Rewrite one isolated billing module with full rollback. Validate
assumptions about coupling before committing full scope.

## Confidence Level
High — base rate for legacy rewrites exceeding estimate: 70–80%. No evidence present
that shifts this.
```

---

## Core anti-patterns this skill rejects

- Generic risk lists padded to 10+ items
- Weak mitigations ("communicate better," "monitor closely")
- Treating all risks as equally probable
- Defaulting to PROCEED when evidence is thin
- Recommending "proceed with caution" when the right call is stop

---

## Why this is different from code-focused azimuths

Most azimuth skills for AI agents are built around code and PR review — they ask "what's wrong with this implementation?" This skill asks "what's wrong with this decision?" It covers the full stack of how initiatives fail: incentive misalignment, political timelines, unvalidated demand, dependency concentration, and the 12 structural gotchas that survive standard checklists.

---

## Compatibility

| Agent | Supported |
|-------|-----------|
| Claude Code | ✓ |
| Claude.ai | ✓ |
| Codex (OpenAI) | ✓ |
| Gemini CLI | ✓ |
| Cursor | ✓ |
| GitHub Copilot | ✓ |
| Windsurf | ✓ |
| OpenCode | ✓ |

---

## Contributing

Issues and PRs welcome. Priority areas: additional domain templates (M&A, compliance, infrastructure), base rate data improvements, and domain-specific gotchas.

---

## License

MIT

---

*Built on Gary Klein's prospective hindsight methodology and structured analytic technique traditions. The name comes from land navigation: an azimuth is the bearing you verify before you step off. Get it wrong at the start and no amount of execution excellence puts you on the right objective.*

*Designed for operators making irreversible decisions under uncertainty.*
