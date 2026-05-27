# AZIMUTH

Decision-quality pre-commitment analysis. You put in a decision. You get a real analysis back.

AZIMUTH tests your plan before you commit to it. It surfaces the assumption holding everything together, the dependency nobody secured, and the kind of failure that's common for projects like yours but invisible from the inside.

---

## Try it now

No installation. Enter your Anthropic API key, load a prompt, run it.

**[https://azimuth-testbed.netlify.app](https://azimuth-testbed.netlify.app)**

Your key goes directly to Anthropic from your browser. Nothing touches our servers. The three Boeing 737 MAX prompt variants are pre-loaded as the demonstration.

---

## The Problem

Plans look fine until they don't. The risks that sink projects are usually the ones nobody questioned — the assumption holding everything together, the dependency nobody secured, the kind of failure that's common for projects like yours but invisible from the inside.

AZIMUTH runs that check before you're committed.

---

## What you get

**A verdict with a rationale.** Not just "risky" — a specific recommendation: proceed, pilot first, reduce scope, delay, or reject, with the structural reason why.

**Assumption audit.** Every assumption classified as strong, partial, unsupported, or contradicted — plus a falsifier for each: the specific observable evidence that would prove it wrong.

**Failure path analysis.** The most likely ways this fails, traced trigger → cascade → cost. Including the cases where two risks combine into something worse than either alone.

**Incentive scan.** Who proposed this, who benefits, who absorbs the downside if it fails, whether dissent was heard. Structured into the verdict — not an afterthought.

**Dependency fragility map.** What's a single point of failure, what's secured vs. assumed, what the lead time is to replace what isn't.

**Structural mitigations only.** Generic advice is rejected. "Communicate better" and "monitor closely" don't appear in the output.

---

## Install in your workflow

If you want AZIMUTH permanently in Claude Code:

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

---

## Methodology calibration · Boeing 737 MAX

Confidence reflects evidence, not framing.

**Decision under analysis.** Boeing's 2011 choice to retrofit the existing 737 airframe (rather than design a new aircraft) to compete with the Airbus A320neo. The retrofit required the MCAS automated trim system to compensate for changed aerodynamics, and Boeing committed to delivering the result with **no new pilot training required** — backed by a $1M-per-plane penalty clause to Southwest if simulator training became necessary.

**Outcome.** Two fatal crashes (Lion Air 610, 2018; Ethiopian Airlines 302, 2019). **346 deaths.** Worldwide fleet grounding for ~20 months. $20B+ in direct losses. Deferred Prosecution Agreement with the DOJ for conspiracy to defraud the FAA. Continuing compliance failures since, including the 2024 Alaska Airlines door-plug incident.

**What this tests.** AZIMUTH applied retroactively to a decision brief built only from **pre-2011 evidence** — what was knowable before the commitment was made. The three runs below vary how that brief is framed: full context, parameters only, and adversarial commercial framing. The goal isn't to claim AZIMUTH would have prevented the outcome. It's to show how the verdict and confidence track the evidence stack across hostile prompts.

**What to look for.** Runs 1 and 2 returning the same verdict from very different prompts (the methodology isn't reading from a pre-supplied conclusion). Run 3 returning **DELAY at LOW confidence — not PROCEED** — when the adversarial prompt drops the penalty clause. That's the confidence ceiling working as designed: when the evidence thins, confidence is capped, not abandoned.

Three prompt variants. Three runs on Opus 4.5, each from a fresh conversation. The verdicts varied — because each one tracked what its input actually supported.

| Run | Prompt | Verdict | Confidence | What happened |
|---|---|---|---|---|
| 1 | Full framing — institutional context, December 2011, $280M penalty clause, software compensation system named | REJECT | HIGH | Returned REJECT, naming the penalty clause as the structural root cause |
| 2 | Thin — parameters only, no company name, no aircraft name | REJECT | HIGH | The model worked through the structural questions silently, judged it had enough to answer, and returned a verdict |
| 3 | Adversarial — confident commercial framing, penalty clause omitted | DELAY PENDING EVIDENCE | LOW† | The model asked five structural questions, gave a verdict on what it had, and used LOW confidence to flag what was missing |

† LOW confidence on Run 3 is not a hedge. It's an explicit signal that the input doesn't carry enough evidence to support higher confidence — with a clear way to upgrade: answer the five questions, and the verdict can be revisited.

AZIMUTH returns hard verdicts when the evidence supports them. When the evidence is thin or the framing is adversarial, the model either works through the structural questions silently (Run 2) or makes them visible as part of the verdict (Run 3). On re-runs, the model sometimes refuses to give a verdict until you answer them. All three behaviors express the same principle: the verdict and confidence reflect what the evidence actually supports, not how the question was framed.

[Run the Boeing prompts yourself →](https://azimuth-testbed.netlify.app)

---

## How to know it's working

- Assumptions you treated as given are being tested, not accepted
- The verdict surprises you — or confirms what you suspected but couldn't articulate
- The failure paths describe something that has actually happened to similar decisions
- The incentive scan names a conflict you hadn't explicitly surfaced
- You change the plan before committing, not after

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

## Domains

Works on any initiative-level decision with real downside: product launches, rewrites, key hires, partnerships and M&A, build vs. buy decisions, org changes, startup and early-stage decisions, and timeline commitments. Domain-specific policies load automatically based on intake routing.

---

## Verdicts

<details>
<summary>Full verdict taxonomy</summary>

| Verdict | When it fires |
| --- | --- |
| `PROCEED` | Evidence supports moving forward; risks are manageable |
| `PROCEED WITH SAFEGUARDS` | Proceed only if specific structural changes are made |
| `PILOT FIRST` | Test the highest-risk assumption before committing full scope |
| `REDUCE SCOPE` | Current scope is not supportable; a smaller version may be |
| `DELAY PENDING EVIDENCE` | Decision is premature; specific information is needed |
| `REJECT` | Evidence or structure does not support proceeding |
| `INSUFFICIENT SIGNAL` | Input is too sparse, vague, or contradictory to ground analysis |
| `WRONG TOOL` | Input is not a real go/no-go decision |
| `RESIDUAL-RISK-REGISTER` | Decision is already made — produces a forward-looking list of remaining risks (leading indicators, escalation triggers, owners) instead of a go/no-go verdict |

**Three verdict categories:** Action verdicts (PROCEED through REJECT) are go/no-go positions. Refusal verdicts (INSUFFICIENT SIGNAL, WRONG TOOL) mean analysis cannot be grounded in the input. RESIDUAL-RISK-REGISTER is an alternative-deliverable verdict — it produces useful analysis for a closed decision, not a refusal.

</details>

---

## What's inside

<details>
<summary>File tree</summary>

```
azimuth/
├── SKILL.md                              # Core skill — intake routing + 10-module analysis engine
├── gotchas.md                            # 8 structural failure patterns that evade standard checklists
├── references/
│   ├── base-rates.md                     # Historical failure rates: software, startups, launches, hiring, M&A, org change
│   ├── startup-failures.md               # 8 startup-specific failure patterns with diagnostic questions
│   ├── software-failure-patterns.md      # 10 engineering failure patterns with azimuth questions
│   ├── launch-risks.md                   # Pre/during/post launch risk zones with signal and mitigation
│   ├── ma-partnership-patterns.md        # 12 M&A and partnership failure patterns with diagnostic questions
│   ├── hiring-failure-patterns.md        # Hiring failure patterns with diagnostic questions
│   └── org-change-patterns.md            # 6 org change and restructure failure patterns
├── diagnostics/
│   ├── assumption-audit.md               # 5-step: extract → classify → risk-score → validate → gate
│   ├── dependency-map.md                 # Full inventory, assessment matrix, concentration risk
│   ├── incentive-conflicts.md            # 7 conflict categories, severity classification
│   └── fragility-scan.md                # 6 structural fragility indicators → LOW/MEDIUM/HIGH/CRITICAL
├── domain-policies/
│   ├── codebase-azimuth.md               # Refactor / migration / rewrite
│   ├── product-launch-azimuth.md         # Launch readiness gate matrix + rollback protocol
│   ├── hiring-azimuth.md                 # Role definition audit + candidate failure path analysis
│   ├── partnership-azimuth.md            # M&A, acquisitions, strategic partnerships, vendor relationships
│   ├── secondaries-ic-azimuth.md         # PE secondaries IC recommendation
│   ├── org-change-azimuth.md             # Restructure, consolidation, role elimination, leadership transition
│   ├── startup-azimuth.md                # Startup and early-stage venture decision
│   └── build-buy-partner-azimuth.md      # Path selection: build vs. buy vs. partner with domain handoff
└── examples/
    ├── case-study-healthcare-gov.md      # Healthcare.gov DEEP mode run — 5/6 recall, 0 false positives
    └── case-study-open-source-launch-timing.md  # STANDARD mode — solo dev timing a repo launch during job search
```

</details>

---

## Limitations

AZIMUTH stress-tests the decision as framed. It cannot tell you whether the framing is correct. In long sessions where prior conversation history is large (above ~150K–177K tokens), SKILL.md may load incompletely and some analysis hooks may not fire. Fresh sessions and short sessions are unaffected.

---

## Contributing

Issues and PRs welcome. Priority areas: additional domain policies, base rate data improvements with primary source citations, and domain-specific gotchas grounded in documented failure cases.

---

## Feedback or questions

[Open a feedback issue](https://github.com/MrBinnacle/azimuth/issues/new?template=feedback.yml) or email [mlpgruber@gmail.com](mailto:mlpgruber@gmail.com). For defects in the skill itself, open a regular issue.

---

## License

MIT
