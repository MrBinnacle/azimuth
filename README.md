# AZIMUTH

Decision-quality pre-commitment analysis. You put in a decision. You get a real analysis back.

AZIMUTH pressure-tests decisions before commitment. It surfaces the assumption holding everything together, the dependency nobody secured, and the failure mode that's common in decisions like this one but invisible from inside it.

---

## Try it now

No installation. Enter your Anthropic API key, load a prompt, run it.

**[https://azimuth-testbed.netlify.app](https://azimuth-testbed.netlify.app)**

Your key goes directly to Anthropic from your browser. Nothing touches our servers. The three Boeing 737 MAX prompt variants are pre-loaded as the demonstration.

---

## The Problem

Plans look fine until they don't. The risks that sink projects are usually the ones nobody questioned — the assumption holding everything together, the dependency nobody secured, the failure mode that's common in decisions like this one but invisible from inside it.

AZIMUTH runs the structured pressure-test before you're committed.

---

## What you get

**A verdict with a rationale.** Not just "risky" — a specific recommendation: proceed, pilot first, reduce scope, delay, or reject, with the structural reason why.

**Assumption audit.** Every assumption classified as strong, partial, unsupported, or contradicted — plus a falsifier for each: the specific observable evidence that would prove it wrong.

**Failure path analysis.** The most plausible ways this fails, traced trigger → cascade → business cost. Pair-interaction analysis where two risks together produce a worse outcome than either alone.

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
/azimuth Pressure test our Q3 timeline
```

---

## The Boeing methodology runs

Three prompt variants. Three runs on Opus 4.5, each from a fresh conversation. Verdict stable across all framing conditions.

| Run | Prompt | Context | Verdict | Confidence |
|---|---|---|---|---|
| 2 | Full framing | Clean | REJECT | HIGH |
| 3 | Thin (parameters only) | Clean | REJECT | HIGH |
| 4 | Adversarial (confident register) | Clean | DELAY PENDING EVIDENCE | LOW† |

The thin prompt contained no company name, no aircraft name, no historical reference — decision parameters only. AZIMUTH recognized the failure pattern from the decision parameters alone and returned REJECT, HIGH confidence.

Run 3 verbatim: "Base rate for this exact strategy succeeding without training requirement: 0% in the post-MAX regulatory environment."

The irreconcilable structure is visible in the decision parameters alone.

† Opus 4.5 applied the M10 confidence ceiling more aggressively to sparse-evidence inputs; the verdict is stable, the confidence calibration is arguably more precise.

**Run 1 (full framing, contaminated context):** AZIMUTH paused at M4 PRE-CHECK and issued a structured interview rather than proceeding to verdict — methodologically significant as evidence that explicit context pre-loading and implicit session contamination trigger different protocol behavior.

---

## How to know it's working

- Assumptions you treated as given are being validated, not accepted
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

Works on any initiative-level decision with real downside: product launches, service rewrites, key hires, partnerships and M&A, build vs. buy decisions, org changes, startup and early-stage decisions, PE secondaries, and timeline commitments. Domain-specific templates load automatically.

---

## Verdicts

<details>
<summary>Full verdict taxonomy</summary>

| Verdict | When it fires |
| --- | --- |
| `PROCEED` | Evidence supports moving forward; risks are manageable |
| `PROCEED WITH SAFEGUARDS` | Proceed only if specific structural changes are made |
| `PILOT FIRST` | Validate the highest-risk assumption before committing full scope |
| `REDUCE SCOPE` | Current scope is not supportable; a smaller version may be |
| `DELAY PENDING EVIDENCE` | Decision is premature; specific information is needed |
| `REJECT` | Evidence or structure does not support proceeding |
| `INSUFFICIENT SIGNAL` | Input is too sparse, vague, or contradictory to ground analysis |
| `WRONG TOOL` | Input is not a pre-commitment decision question |
| `RESIDUAL-RISK-REGISTER` | Decision already made — produces a forward-looking residual risk register (leading indicators, escalation triggers, owners), not a go/no-go verdict |

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
├── templates/
│   ├── executive-azimuth.md              # 1-page format for leadership briefings
│   ├── codebase-azimuth.md               # Refactor/migration/rewrite template
│   ├── product-launch-azimuth.md         # Launch readiness gate matrix + rollback protocol
│   ├── hiring-azimuth.md                 # Role definition audit + candidate failure path analysis
│   ├── partnership-azimuth.md            # M&A, acquisitions, strategic partnerships, vendor relationships
│   ├── secondaries-ic-azimuth.md         # PE secondaries IC recommendation template
│   ├── org-change-azimuth.md             # Restructure, consolidation, role elimination, leadership transition
│   ├── startup-azimuth.md                # Startup and early-stage venture decision template
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

Issues and PRs welcome. Priority areas: additional domain templates, base rate data improvements with primary source citations, and domain-specific gotchas grounded in documented failure cases.

---

## License

MIT
