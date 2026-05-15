# Critical Reasoning Modes

Load when the user asks for `AZIMUTH FOOL: ...`, when framing is uncertain, or when the standard pre-mortem finds a real unresolved clash rather than a simple risk register.

---

## Purpose

These modes add challenge depth without turning AZIMUTH into a general debate bot. They are drill-down lenses that feed findings back into the main AZIMUTH register and verdict.

Use one mode at a time unless DEEP explicitly needs synthesis across modes.

---

## Modes

| Command | Mode | Use when | Output |
|---|---|---|---|
| `AZIMUTH FOOL: socratic` | Socratic Assumption Surfacing | The plan's premises are vague or inherited | Assumption inventory + probing questions + validation experiments |
| `AZIMUTH FOOL: dialectic` | Dialectic / Steelman / Synthesis | There is a credible opposing view | Thesis, antithesis, conflict dimensions, synthesis |
| `AZIMUTH FOOL: red-team` | Attack This | An adversary, competitor, regulator, or internal failure actor matters | Attack vectors + defenses + perverse incentives |
| `AZIMUTH FOOL: evidence` | Evidence Testing | Claims may outrun evidence | Claim table + evidence grade + falsifier + competing explanation |
| `AZIMUTH FOOL: critic` | Brutal Critic | Output is too polite, padded, or non-decisive | Hardest truthful objections + what must change |

---

## Auto-Load Triggers

Auto-load only in STANDARD+ and only when useful:

- **Socratic**: objective or success metric is fuzzy; key assumption is inherited from another plan
- **Dialectic**: two credible paths remain after Module 10, or the user asks for the other side
- **Red-team**: competitor, abuse, regulatory, launch, or adversarial exploitation risk is central
- **Evidence**: top claims have partial / unsupported evidence but user confidence is high
- **Critic**: draft output risks softening, motivational filler, or over-balanced prose

---

## Dialectic Synthesis

Process:

1. Steelman the user's thesis.
2. Construct the strongest opposing argument.
3. Name points of genuine conflict.
4. Propose a synthesis using one of these patterns:
   - Conditional: X when A, Y when B
   - Scope partition: X for domain A, Y for domain B
   - Temporal: start with X, migrate to Y at trigger Z
   - Risk mitigation: proceed with X only with safeguards from Y
   - Pivot: antithesis is stronger; reconsider original path

Output:

```markdown
## Synthesis
- What survives from the thesis: ...
- What survives from the antithesis: ...
- What must be given up: ...
- Register impact: [risk / assumption / verdict change]
```

---

## Evidence Testing

For each load-bearing claim:

| Claim | Evidence grade | Falsifier | Competing explanation | Register impact |
|---|---|---|---|---|

Evidence grades:

- Strong: directly relevant, recent, observable, independently checked
- Partial: relevant but incomplete, adjacent, or not independently verified
- Unsupported: asserted without evidence
- Contradicted: evidence points against the claim

---

## Red-Team

Ask:

- Who benefits if this fails?
- Who can exploit the plan's weakest dependency?
- What would a competitor, regulator, attacker, or internal opponent do first?
- What defense changes system conditions rather than adding vigilance?

---

## Brutal Critic

Use sparingly. The critic is not rude; it is compression without politeness-padding.

Rules:

- Name the hardest true objection.
- Remove hedging unless uncertainty is real.
- Convert vague concerns into concrete blockers.
- If the plan should not proceed, say so.

---

## Integration Rule

Every FOOL finding must map back to one of:

- a new or changed register entry
- a changed evidence classification
- a changed L/I score
- a changed verdict
- a decision-record note

If it does none of those, omit it.

---

## Provenance

Adapted conceptually from critical-reasoning skill patterns: Socratic questioning, dialectic synthesis, red teaming, and evidence audits. Rewritten as AZIMUTH drill-down modes.
