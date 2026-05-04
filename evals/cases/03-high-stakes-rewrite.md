---
id: 03-high-stakes-rewrite
tests: [mode-escalation, deep-mode-loading]
expected-mode: DEEP
rubric: structural, invocation
---

# Case 03 — High-Stakes Rewrite

Tests DEEP mode escalation. Input has multiple DEEP signals: irreversible (vendor contract signed, public commitment), headcount changes, multi-quarter, capital outlay above tactical threshold. Skill must escalate, not silently downgrade.

## Input

> We've signed the contract with Salesforce to migrate our customer data platform from our internal Postgres-based system to Salesforce Data Cloud. 9-month migration. We've already announced this to the board and to two key customers. Three engineers reassigned full-time, plus one new senior hire in flight specifically for this. Total committed spend: $1.4M. Current internal system has 8 years of accumulated logic, partial documentation. Owner: VP Engineering. Reversal would mean breaking the Salesforce contract, walking back the board commitment, and laying off the senior hire. We're committed.

## Expected behavior (v1.1.0 and forward)

Skill escalates to DEEP mode. Loads `gotchas.md`, `references/base-rates.md`, `references/software-failure-patterns.md`, and all four diagnostic files.

Output reflects deeper analysis: more thorough Critical Risks (likely covering Second System Effect, Reversibility Underestimation, Knowledge Concentration on the 8-year-old internal system), explicit base-rate citations from `base-rates.md` (McKinsey/Oxford on rewrite outcomes), and structural mitigations.

Verdict likely: PROCEED WITH SAFEGUARDS or REDUCE SCOPE — given that REJECT is contractually impossible per the input, and the input itself flags reversal cost as committed. The skill should NOT recommend REJECT here, but should not soften language either.

## Pass criteria

- Output cites at least one specific base-rate from `references/base-rates.md` (e.g., the McKinsey/Oxford finding) — not just "rewrites often fail"
- Output references at least one of the 8 gotchas by name (Second System Effect or Reversibility Underestimation are most relevant; Commitment Escalation is also a fit given the input frames "we're committed")
- Output draws on diagnostic depth — references assumption-audit, dependency-map, or fragility-scan analysis explicitly OR reflects their depth in section content
- Critical Risks section has 4-5 entries (DEEP mode produces deeper analysis than STANDARD's 1-3)
- Structural rubric: pass on at least 10 of 12 checks
