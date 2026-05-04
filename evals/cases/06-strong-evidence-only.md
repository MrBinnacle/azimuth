---
id: 06-strong-evidence-only
tests: [v1.1.x-counterfactual-layer]
expected-mode: STANDARD
rubric: structural
---

# Case 06 — Strong Evidence Only

Tests v1.1.x counterfactual layer. Input cites confirming evidence for every key assumption; pre-counterfactual output classifies these as "strong evidence" and moves on. Post-counterfactual output adds Falsifiers section listing what would prove each assumption wrong.

## Input

> We're rolling out a four-day work week for the engineering team, starting Q3. Demand is validated (annual engagement survey shows 87% of engineers list this as their top requested benefit). Productivity research supports it (cited in Microsoft Japan's 2019 trial: 40% productivity gain measured during their experiment). Cost is offset (we're not increasing headcount or salary; effectively moving from 5 days at 8 hours to 4 days at 9 hours, total weekly hours go from 40 to 36 — 10% labor reduction). Existing team is bought in (we surveyed: 92% support, 8% indifferent, 0% opposed). Leadership supports it (CEO and VP Engineering both publicly committed at last all-hands).

## Expected v1.1.0 behavior

Skill invokes in STANDARD mode. Module 2 classifies key assumptions:
- Demand → strong evidence (engagement survey)
- Productivity → partial evidence (one cited study, different culture/scale)
- Cost neutrality → strong evidence (pure arithmetic on stated terms)
- Team buy-in → strong evidence (survey, recent)
- Leadership support → strong evidence (public commitment)

Output is light on Critical Risks because most assumptions appear validated. Verdict likely PROCEED or PROCEED WITH SAFEGUARDS.

The bug: confirming evidence is sought; disconfirming evidence is not. Specifically:
- Microsoft Japan study generalizes poorly (one-month trial, single firm, different culture, different work types)
- Engagement-survey responses to "would you like X" do not predict behavioral response when X arrives
- Cost arithmetic ignores ramp-up cost, communication overhead, scheduling complications

## Expected v1.1.x behavior (after counterfactual layer ships)

Above PLUS new Falsifiers section. For each strong-evidence or partial-evidence assumption, the falsifier is named:

- **Demand**: A second survey 90 days into the change showing actual usage / satisfaction divergent from initial preference. (Engagement-survey enthusiasm ≠ retention satisfaction.)
- **Productivity**: Output metrics in months 2-3 of the change showing no improvement or decline relative to pre-change baseline. (Cited study is one trial; replication is signal.)
- **Cost neutrality**: Project velocity in the first 90 days showing engineering output decline > 10%. (Then the labor savings are illusory.)
- **Team buy-in**: Voluntary opt-out rate 60 days in. Survey-stated support and behavioral retention are different things.
- **Leadership support**: Quiet rollback or de-emphasis at 6-month mark. Public commitment is cheap to make and costlier to maintain.

This forces honest assumption pressure. Strong-evidence claims aren't allowed to ride free.

## Pass criteria for v1.1.x

- Output contains a "Falsifiers" or equivalently named section
- Section provides falsifiers for at least 3 assumptions classified strong or partial
- Falsifiers are specific and observable (not "if it doesn't work" — must name what to measure)
- Pre-counterfactual output (v1.1.0 baseline) does NOT have this section
