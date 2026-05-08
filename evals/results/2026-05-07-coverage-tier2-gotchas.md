# Coverage Tier 2 — Session 6: gotchas.md Pattern Load

**Date:** 2026-05-07  
**Model:** claude-opus-4-6 (subagents)  
**Scope:** `gotchas.md` conditional load — production-vs-control. Does gotchas.md add named pattern identification and check-question framework beyond what software-failure-patterns.md + diagnostics provides, or is the pattern coverage compensated?  
**Method:** 2 agents run in parallel. Production agent: read full SKILL.md (loads real `gotchas.md` when triggered). Control agent: read `evals/test-gotchas-control-skill.md` (references `evals/test-gotchas-empty.md` containing only "[GOTCHAS — REDACTED FOR EVAL]" in gotchas load positions at lines 233 and 263). No agent informed it was part of a paired comparison.  
**Control file:** `evals/test-gotchas-control-skill.md` — 2 gotchas.md path references replaced with `evals/test-gotchas-empty.md`; all other content intact.  
**Trigger condition:** Module 4 RED tier via [IDENTITY] blank (both conditions).  
**Prior evals referenced:** `evals/results/2026-05-07-coverage-tier1-m9.md`, `evals/results/2026-05-07-coverage-tier2-m5.md`

---

## Test Design

### Motivation

`gotchas.md` contains 8 named organizational/behavioral/temporal failure patterns that are intentionally distinct from the technical patterns in `references/software-failure-patterns.md` and the domain patterns in diagnostic files. The loading condition in STANDARD mode: M4 returns RED tier OR M6 produces only canonical chains. DEEP mode: always load.

The test design question: do the specific named patterns and check questions in gotchas.md produce a behavioral delta beyond what software-failure-patterns.md + diagnostics + training-data norms provide? Or is the pattern identification compensated by the always-loaded reference files?

**Patterns targeted in scenario design:**
- **Gotcha 1 (Second System Effect):** "while we're in there" scope expansion from CRM-only to 3-platform migration
- **Gotcha 3 (Commitment Escalation):** $180K spent, CEO investor announcement, IT Director promoted on initiative
- **Gotcha 7 (Plan-Revision Gap):** RevOps flagged scope risk in Week 6; risk log updated; plan unchanged. Engineering estimate noted but not incorporated.

Additional patterns expected to fire: Metric Drift (#6), Reversibility Underestimation (#8).

**Trigger mechanism:** [IDENTITY] blank → M4 RED tier → gotchas.md load triggered in STANDARD mode. DEEP mode (reached by production via load conditions) triggers gotchas.md unconditionally.

### Adversarial Input — "SalesPath HubSpot CRM Migration"

SalesPath Inc. (200-person B2B SaaS, $18M ARR, Series B) is migrating from Salesforce to HubSpot. Decision: proceed with the migration as currently scoped.

- **Original scope (4 months ago):** CRM records, contacts, deal pipeline. 3-person IT team, 180 days, $200K.
- **Current scope:** CRM + email marketing (Mailchimp → HubSpot Marketing Hub) + customer success (Gainsight → HubSpot Service Hub) + 4 custom API rebuilds. Scope grew via "while we're in there" reasoning; no formal re-approval.
- **Budget:** $420K estimate; $180K already spent on HubSpot consulting.
- **Timeline:** 22 weeks to Q4. Engineering lead estimate (in Slack, not in plan): 12–18 months. IT Director: "6 months achievable."
- **External commitment:** CEO announced "HubSpot by Q4" at Q2 investor update.
- **Prior review:** RevOps flagged scope risk at Week 6 planning meeting. Risk log updated. No scope reduction. Plan unchanged.
- **Rollback:** Salesforce reactivation $340K/year; data export format compatibility unverified; no rollback test run.

Module 4 answers: [IDENTITY] blank; 6/7 other questions answered → RED tier triggered.

---

## Production Output (key findings)

**Gotchas.md load trigger:**

DEEP mode unconditional: loaded gotchas.md, references/base-rates.md, all four diagnostics files, references/software-failure-patterns.md, templates/codebase-azimuth.md.

Additionally: M4 RED tier triggered gotchas.md (already loading per DEEP mode).

Verbatim trigger cited from SKILL.md:
> "Also load `gotchas.md` when either of these conditions fires: Module 4 interview returns RED tier, OR any incentive conflict is governance-level"

**Named patterns from gotchas.md (all 5 that fired):**

1. **Second System Effect** — scope grew from CRM-only to CRM + Marketing Hub + Service Hub + 4 API rebuilds via "while we're in there" reasoning. Signal: scope is 4× original; no formal re-approval.
2. **Commitment Escalation** — $180K spent, CEO on record to investors, IT Director promoted on initiative. Check applied: "Would this plan be approved fresh today with current evidence?" — No.
3. **Metric Drift** — success defined as "go-live by Q4" not measurable Sales/CS productivity outcome. No mid-point metric reconfirmation defined.
4. **Plan-Revision Gap** — RevOps flagged scope risk at Week 6; risk log updated; plan unchanged. Engineering's 12–18 month estimate noted; not incorporated into plan. Check applied: "Name one concrete change to the plan that directly addresses the highest-severity finding." Conclusion: none made; analysis produced awareness, not decision quality.
5. **Reversibility Underestimation** — rollback assumes Salesforce reactivation works; data export format unverified; no rollback test. Check applied: "What is the literal rollback procedure? How long does it take? What data would be lost?" — None of these questions are answered by the current plan.

**Production unique contribution (Plan-Revision Gap check):** The Plan-Revision Gap pattern produced a specific diagnostic action not present in control output: "Name one concrete change to the plan that directly addresses the highest-severity finding. If no plan element changed, the analysis produced awareness, not decision quality. Awareness alone does not reduce downside." This is a structural check on the gap between risk surfacing and plan revision that forced explicit acknowledgment of the Week 6 RevOps flag + no-action outcome.

**Verdict:** REDUCE SCOPE / LOW (M4 RED locks confidence at LOW regardless of evidence quality; underlying evidence strongly supports REDUCE SCOPE)

**Highest-leverage fixes (5, all structural):**
1. Reduce scope — CRM + APIs only for Q4; Marketing Hub and Service Hub deferred as separate program
2. Independent timeline review (not IT Director, not consultant); plan re-baselined to result
3. Rollback test in staging before next consultant milestone payment
4. Decouple success metric from go-live date; define measurable Sales/CS outcome
5. Move scope authority off IT Director; CFO/CEO re-approval of expanded scope required

---

## Control Output (key findings)

**Gotchas.md load trigger:**

Control agent correctly identified M4 RED trigger and attempted to load gotchas.md per control SKILL.md instruction pointing to `evals/test-gotchas-empty.md`. File contained only "[GOTCHAS — REDACTED FOR EVAL]." No pattern content available.

Verbatim from control agent:
> "evals/test-gotchas-empty.md was redacted per the eval — only contained '[GOTCHAS — REDACTED FOR EVAL]', so no gotcha checks could be applied."

Control proceeded without gotcha pattern checking.

**Named patterns (from software-failure-patterns.md + diagnostics — NOT from gotchas.md):**

From `references/software-failure-patterns.md`:
1. Pattern 1: Scope Defined by Architecture, Not Outcome
2. Pattern 3: No Rollback Mechanism
3. Pattern 4: The Long-Running Migration
4. Pattern 5: Dependency on Undocumented Behavior
5. Pattern 6: Team Knowledge Concentration
6. Pattern 9: Insufficient Observability

From `diagnostics/incentive-conflicts.md`:
7. Deadline Politics (governance-level)
8. Sunk Cost Preservation (governance-level)
9. Vendor Incentive Misalignment (execution-level)
10. Self-Measured Success / Approval Authority Without Accountability

From `diagnostics/fragility-scan.md`:
11. SPOF (3-person team)
12. Late Detectability
13. Asymmetric Reversibility → Fragility composite: CRITICAL

**Patterns NOT surfaced by control:**
- "Second System Effect" (by name and check question)
- "Commitment Escalation" (by name — Sunk Cost Preservation from incentive-conflicts.md covers the concept but without the "would this plan be approved fresh today?" check)
- "Plan-Revision Gap" (the specific named pattern with the Roose et al. citation and "name one concrete change" check question — this did NOT appear in control output despite the underlying fact pattern being noted: "RevOps risk flag: documented, not actioned")
- "Metric Drift" (control noted the go-live vs. outcome gap but did not name it as a pattern with the 90-day checkpoint check)

**Verdict:** REDUCE SCOPE / LOW — identical to production.

**Highest-leverage fixes (5, all structural):**
1. Formal scope re-approval gate this week; default to original $200K CRM-only
2. Pull engineering's 12–18 month estimate into written plan over engineering lead's signature
3. Rollback test in staging; validate Salesforce data export format; confirm reactivation path
4. Decouple success measurement from IT Director; assign to RevOps + CFO
5. Phase cutover: CRM first, marketing and customer-success as separate later program

---

## Score

| Condition | Verdict | Confidence | Named gotcha patterns | Plan-Revision Gap check | Findings count |
|---|---|---|---|---|---|
| Production | REDUCE SCOPE | LOW | 5 (from gotchas.md) | Yes — "name one concrete change" | 5 gotcha + 8 reference/diagnostic |
| Control | REDUCE SCOPE | LOW | 0 (gotchas.md redacted) | No | 13 (from reference + diagnostic files) |

**Verdict delta: NONE.**

**Confidence delta: NONE.**

**Named gotcha pattern delta: PRESENT** — production named 5 gotcha patterns (Second System Effect, Commitment Escalation, Metric Drift, Plan-Revision Gap, Reversibility Underestimation) with their specific signal descriptions and check questions. Control named 0 gotcha patterns; same underlying risks identified through software-failure-patterns.md + diagnostics.

**Plan-Revision Gap check question: PRODUCTION ONLY** — "Name one concrete change to the plan that directly addresses the highest-severity finding. If no plan element changed, the analysis produced awareness, not decision quality." This check question is unique to gotchas.md and did not appear in control output, despite the underlying scenario fact (RevOps flag + no action) being present.

**Finding count direction:** Control produced 13 named patterns (from reference + diagnostic files); production produced 5 gotcha patterns plus overlapping reference/diagnostic patterns. This continues the pattern observed in M9 (control 5, production 4) and M5: control scans may be broader when not anchored to a specific taxonomy.

---

## Classification: PARTIAL

**gotchas.md is PARTIAL** under full-load conditions.

The same verdict (REDUCE SCOPE / LOW), same confidence (LOW via M4 RED), and same mitigation quality (5 structural fixes each, all appropriate) appeared in both conditions. The underlying risk identification (scope overrun, sunk cost, suppressed dissent, rollback risk) was compensated by software-failure-patterns.md + diagnostics.

**What gotchas.md adds that is not compensated:**

1. **Named patterns with check questions** — "Second System Effect," "Commitment Escalation," "Plan-Revision Gap," "Metric Drift," "Reversibility Underestimation" as named, citable patterns with specific diagnostic signal descriptions and check questions
2. **Plan-Revision Gap check question specifically** — "Name one concrete change to the plan that directly addresses the highest-severity finding. If no plan element changed, the analysis produced awareness, not decision quality." This operationally useful check did not appear in control output and has no equivalent in software-failure-patterns.md or diagnostics
3. **Cross-domain pattern sourcing** — gotchas.md explicitly covers organizational/behavioral/temporal patterns intentionally distinct from technical failure patterns. The named patterns (Commitment Escalation, Metric Drift) are behavioral, not technical, and are not equivalently named in software-failure-patterns.md

**What is compensated:**

The underlying risk identification for all 5 gotcha patterns was present in the control output through equivalent mechanisms:
- Second System Effect → Pattern 1 (Scope Defined by Architecture, Not Outcome) from software-failure-patterns.md
- Commitment Escalation → Sunk Cost Preservation from incentive-conflicts.md
- Plan-Revision Gap → noted as "RevOps flag documented, not actioned" (without the specific named check)
- Metric Drift → noted as "go-live vs. outcome gap" (without the 90-day checkpoint check)
- Reversibility Underestimation → Asymmetric Reversibility from fragility-scan.md

**Compensation sources:** software-failure-patterns.md + diagnostics (all post-225).

---

## Architectural Finding: All Compensation Sources Post-225

gotchas.md (post-225), software-failure-patterns.md (post-225, conditionally loaded), and all diagnostic files (post-225, conditionally loaded) share the same load-position failure mode under partial load. Under partial-load conditions:

- gotchas.md fails (post-225)
- software-failure-patterns.md fails (post-225, loading instruction in SKILL.md is also post-225)
- diagnostics fail (post-225)

Under partial load, ALL organizational/behavioral pattern analysis would degrade simultaneously. No pre-225 mechanism covers the behavioral failure pattern dimension. This is position-correlated redundancy at the reference-file level.

The only surviving mechanism under partial load for organizational pattern detection is training-data norms — which are load-independent but provide no named patterns and no specific check questions.

---

## Disposition

**gotchas.md — PARTIAL** under full-load conditions.

Underlying risk identification compensated by software-failure-patterns.md + diagnostics. Named patterns and check questions (especially Plan-Revision Gap's "name one concrete change") are load-bearing for vocabulary and diagnostic precision, but not for verdict or confidence outcomes.

**Under partial load:** gotchas.md and all compensation sources fail simultaneously. Training-data norms provide load-independent baseline but without named patterns or check questions. Organizational/behavioral pattern analysis degrades to unstructured risk identification under partial load.

**Constraint-vs-guide continued:** Control produced 13 named patterns from reference + diagnostic files vs. production's 5 gotcha patterns + overlapping references. This is the fourth session showing control scans as equal or broader in count when not anchored to a specific file taxonomy.

**Tier 2 Session 6: COMPLETE.**
