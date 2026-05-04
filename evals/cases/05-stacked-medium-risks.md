---
id: 05-stacked-medium-risks
tests: [v1.1.x-coupling-pass]
expected-mode: STANDARD
rubric: structural
---

# Case 05 — Stacked Medium Risks

Tests v1.1.x coupling pass. Input has 4-5 medium-severity risks across modules; pre-coupling-pass output enumerates them as independent paths. Post-coupling-pass output identifies pair-interaction failure modes — combinations that produce nonlinear failure.

## Input

> We're shipping a new mobile app feature in 6 weeks: in-app purchases for a previously-free social fitness app. 80% of revenue forecast comes from this feature. iOS and Android parallel development, 3 engineers each. Marketing campaign launches 3 days after feature ship — all-channel push, $400K spend, partnership with two fitness influencers. New payment processor integration (Stripe Connect); current system uses simpler Stripe Charges. Customer support team of 4 is already at 70% utilization. We have not done feature flags before — this would be our first staged rollout.

## Expected v1.1.0 behavior

Skill invokes in STANDARD mode. Critical Risks section enumerates 4-5 independent risks:
- Payment processor migration (novel integration, no fallback experience)
- Support team overload (already at 70% utilization, IAP launches always spike support)
- Marketing-feature timing (3-day buffer is thin if defects surface)
- Parallel platform release (iOS and Android shipping simultaneously)
- First-time staged rollout (org has never done this, learning curve under deadline)

Each risk gets a Failure Path. Risks are treated as independent — no analysis of which combinations produce nonlinear failure.

## Expected v1.1.x behavior (after coupling pass ships)

Above PLUS new Interaction Effects section. Identifies pair-interactions:

- **Payment integration + support overload** — if payment defects surface in week 1 of launch, support is already at saturation, complaints compound (multiplicative not additive)
- **Feature ship + marketing timing** — defects in feature visible to highest-pressure user wave, recovery window absent
- **Parallel platform release + first-time staged rollout** — staged rollout is hard enough on one platform; doing it for the first time across both compounds risk

Section is short (3-5 pair-interactions max), each with a specific multiplicative failure mechanism — not just "these are both risky."

## Pass criteria for v1.1.x

- Output contains an "Interaction Effects" or equivalently named section
- Section identifies at least 2 pair-interactions, not just enumerated risks
- Each interaction names the specific multiplicative mechanism (not just "these are both risky")
- Pre-coupling-pass output (v1.1.0 baseline) does NOT have this section — confirms the change shipped, not that it was already present
