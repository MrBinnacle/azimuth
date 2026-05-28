# AZIMUTH

**You put in a decision. You get back a verdict you can act on, and the structural reason behind it.**

Plans look fine until they don't. The risks that sink them are the ones nobody questioned — the assumption holding everything together, the dependency nobody secured, the failure that's common for work like yours but invisible from inside. AZIMUTH runs that check before you're committed: it classifies your assumptions, traces the most likely failure paths, names who benefits if the plan proceeds unexamined, and returns one of nine verdicts with the evidence behind it.

---

## Try it — no install

Enter your Anthropic API key, pick a decision, run it. Your key goes straight to Anthropic from your browser; nothing touches our servers, and nothing is stored.

**→ [azimuth-testbed.netlify.app](https://azimuth-testbed.netlify.app)**

You can run it on your own decision, or load one of the pre-built prompts — including the Boeing 737 MAX calibration set below — and watch the analysis happen turn by turn.

---

## What you get

**A verdict with a rationale.** Not "risky" — a specific call: proceed, proceed with safeguards, pilot first, reduce scope, delay, or reject, with the structural reason why. (Full taxonomy below.)

**An assumption audit.** Every assumption the plan depends on, classified strong / partial / unsupported / contradicted — each paired with a falsifier: the specific observable evidence that would prove it wrong.

**Failure-path analysis.** The most likely ways this fails, traced trigger → cascade → cost, including the cases where two risks combine into something worse than either alone.

**An incentive scan.** Who proposed this, who benefits, who absorbs the downside if it fails, whether dissent was heard — folded into the verdict, not bolted on as a footnote.

**A dependency map.** What's a single point of failure, what's secured versus assumed, and the lead time to replace what isn't.

**Structural mitigations only.** The skill rejects generic advice by instruction — "communicate better" and "monitor closely" don't appear in the output.

---

## Calibration · Boeing 737 MAX

**A verdict you can argue with isn't worth wiring into a decision. The test is whether you can talk it into a different answer by changing how you ask.**

The same decision — Boeing's 2011 commitment that the 737 MAX would need no simulator training, with a $1M-per-plane penalty across 280 aircraft ($280M) if it did — described three ways: a full institutional brief, the bare parameters with the company and aircraft stripped out, and an optimistic pitch that leads with the competitive win. Three runs on Claude Opus 4.7, each from a clean conversation, against AZIMUTH v1.5.0.

The verdict held **REJECT** all three times. Only the confidence moved.

| Run | Framing | Verdict | Confidence |
|---|---|---|---|
| Full brief | Institutional context, Dec 2011, $280M penalty clause, software compensation named | REJECT | HIGH |
| Bare facts | Parameters only — no company, no aircraft | REJECT | MEDIUM |
| Optimistic spin | Leads with the competitive win; penalty present, framing built to sell a yes | REJECT | MEDIUM |

The structure is decisive under every framing, so the verdict doesn't move. What moves is confidence: the full brief carries the most evidence and earns HIGH; strip the brief to bare parameters, or pitch it as a win, and the model still reaches REJECT but caps its confidence at MEDIUM to reflect that it's working from less. Optimistic framing doesn't soften the answer — it lowers what the model will claim to be sure of.

This is calibration, not a claim that AZIMUTH would have prevented the crashes. The decision-makers had the same information in 2011. The point is that the terrain was readable, and the read doesn't bend to how the question is asked.

[Run the three prompts yourself →](https://azimuth-testbed.netlify.app)

---

## Install in your workflow

For AZIMUTH permanently in Claude Code or Claude.ai:

```
npx skills add https://github.com/MrBinnacle/azimuth
```

Then invoke on any decision:

```
/azimuth We're planning to rewrite the legacy billing service in Q3
/azimuth Should we make this hire?
/azimuth We're launching next week — is the plan sound?
/azimuth Build vs. buy vs. partner for this capability?
/azimuth Stress-test our Q3 timeline
```

The skill activates automatically on decision-quality queries, or you can invoke it directly.

---

## Example output

<details>
<summary>Legacy billing rewrite — REJECT verdict (abbreviated)</summary>

**Input:** *"We're planning to rewrite our legacy billing service in Q3. 8 weeks, 2 engineers."*

```
## Azimuth Verdict
Do not proceed. Revenue-critical system. Timeline is incompatible with known base
rates for this class of rewrite. Team structure creates a single point of failure.
Scope reduction does not fix either of these.

## Recommended Decision
REJECT — Return with a realistic timeline (3× minimum), a second engineer with
documented billing domain knowledge, and a defined rollback architecture. A pilot
validates coupling; it does not address the structural issues here.

## Confidence Level
High — base rates for legacy billing rewrites in this class are well-documented.
2-engineer teams on revenue-critical rewrites carry asymmetric downside on either
departure.

## Critical Risks
1. Timeline incompatibility — Rewrites at this complexity class historically run
   3–5× estimate. 8 weeks implies 24–40 actual weeks. No evidence this project
   shifts the base rate.
2. Single point of failure — 2 engineers on a revenue-critical system: one
   departure or absence stops the rewrite entirely. No fallback owner named.
3. No rollback architecture — Billing cutover without a tested rollback path has
   no safe recovery if defects reach production.

## Falsifiers
- Timeline: A comparable billing module completed within 2 weeks in a spike — or
  the 8-week estimate is not grounded in this codebase.
- SPOF: A second engineer documents and reproduces all billing edge cases
  independently within 2 weeks — or the knowledge concentration is real.

## Likely Failure Paths
- One engineer exits → domain knowledge inaccessible → rewrite stalls → legacy
  system maintained indefinitely → original problem compounds.
```

</details>

---

## Domains

Works on any initiative-level decision with real downside: product launches, rewrites, key hires, partnerships and M&A, build vs. buy, org changes, startup and early-stage decisions, and timeline commitments. Domain-specific policies load automatically based on intake routing.

---

## Verdicts

<details>
<summary>Full verdict taxonomy</summary>

| Verdict | When it fires |
| --- | --- |
| `PROCEED` | Evidence supports moving forward; risks are manageable |
| `PROCEED WITH SAFEGUARDS` | Proceed only if specific structural changes are made first |
| `PILOT FIRST` | Test the highest-risk assumption before committing full scope |
| `REDUCE SCOPE` | Current scope is not supportable; a smaller version may be |
| `DELAY PENDING EVIDENCE` | Decision is premature; specific information is needed |
| `REJECT` | Evidence or structure does not support proceeding |
| `INSUFFICIENT SIGNAL` | Input is too sparse, vague, or contradictory to ground analysis |
| `WRONG TOOL` | Input is not a real go/no-go decision |
| `RESIDUAL-RISK-REGISTER` | Decision is already made — produces a forward-looking list of remaining risks (leading indicators, escalation triggers, owners) instead of a go/no-go verdict |

**Three categories.** Action verdicts (PROCEED through REJECT) are go/no-go positions. Refusal verdicts (INSUFFICIENT SIGNAL, WRONG TOOL) mean the analysis can't be grounded in the input. RESIDUAL-RISK-REGISTER is an alternative deliverable — useful analysis for a closed decision, not a refusal.

</details>

---

## What's inside

<details>
<summary>What installs</summary>

`npx skills add` delivers only the skill. The development harness, eval suite, case studies, and docs stay in the repo and are not copied to your machine.

```
azimuth/                                  # the shipped skill
├── SKILL.md                              # Intake routing + 10-module analysis engine
├── BEHAVIOR_SPEC.md                      # Canonical engine spec — deterministic rules SKILL.md mirrors
├── gotchas.md                            # 8 structural failure patterns that evade standard checklists
├── references/
│   ├── base-rates.md                     # Failure rates: software, startups, launches, hiring, M&A, org change
│   ├── startup-failures.md               # Startup-specific failure patterns with diagnostic questions
│   ├── software-failure-patterns.md      # Engineering failure patterns
│   ├── launch-risks.md                   # Pre / during / post launch risk zones
│   ├── ma-partnership-patterns.md        # M&A and partnership failure patterns
│   ├── hiring-failure-patterns.md        # Hiring failure patterns
│   ├── org-change-patterns.md            # Org change and restructure failure patterns
│   ├── module-guide.md                   # M1–M10 bodies, register discipline, escalation logic
│   ├── mode-behaviors.md                 # FAST / STANDARD / RAPID / DEEP specs + diagnostic load triggers
│   ├── output-template.md                # Default output format + anti-slop rules
│   └── output-format-executive.md        # 1-page leadership briefing format
├── diagnostics/
│   ├── assumption-audit.md               # extract → classify → risk-score → validate → gate
│   ├── dependency-map.md                 # Inventory, assessment matrix, concentration risk
│   ├── incentive-conflicts.md            # 7 conflict categories, severity classification
│   └── fragility-scan.md                 # 6 fragility indicators → LOW / MEDIUM / HIGH / CRITICAL
└── domain-policies/
    ├── codebase-azimuth.md               # Refactor / migration / rewrite
    ├── product-launch-azimuth.md         # Launch readiness gate + rollback protocol
    ├── hiring-azimuth.md                 # Role definition audit + candidate failure path analysis
    ├── partnership-azimuth.md            # M&A, acquisitions, partnerships, vendor relationships
    ├── secondaries-ic-azimuth.md         # PE secondaries IC recommendation
    ├── org-change-azimuth.md             # Restructure, consolidation, leadership transition
    ├── startup-azimuth.md                # Startup and early-stage venture decision
    └── build-buy-partner-azimuth.md      # Path selection: build vs. buy vs. partner
```

Worked case studies ([Healthcare.gov](examples/case-study-healthcare-gov.md), [open-source launch timing](examples/case-study-open-source-launch-timing.md)) and the eval suite live in the repo, not the installed skill.

</details>

---

## Limitations

AZIMUTH stress-tests the decision as framed; it can't tell you whether the framing is the right one. In very long sessions (prior conversation above roughly 150K–177K tokens), `SKILL.md` may load incompletely and some checks may not fire — fresh and short sessions are unaffected.

---

## Contributing

Issues and PRs welcome. Priority areas: additional domain policies, base-rate data improvements with primary-source citations, and domain-specific gotchas grounded in documented failure cases.

---

## Feedback or questions

[Open a feedback issue](https://github.com/MrBinnacle/azimuth/issues/new?template=feedback.yml) or email [mlp.gruber@gmail.com](mailto:mlp.gruber@gmail.com). For defects in the skill itself, open a regular issue.

---

## License

MIT
