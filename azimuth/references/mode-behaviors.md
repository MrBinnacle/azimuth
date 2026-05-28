# Mode Behaviors — Rationale

This file is descriptive. Mode selection rules, per-mode module-firing rules, and conditional load rules are specified in `BEHAVIOR_SPEC.md` §2, §3, and §5. This file explains WHY each mode is structured the way it is — the rationale a human or LLM benefits from understanding, separately from the rules the engine executes.

---

## FAST — rationale

FAST is shaped as a rapid pressure-test: top-level integrity checks, a narrow assumption pass, the most salient failure paths, and a verdict. Its purpose is to surface obvious disqualifiers quickly, not to produce a defensible incentive or recoverability analysis.

The Module 4 incentive interview cannot run meaningfully in FAST. The interview derives its value from dialogue length and follow-up — abbreviating it would produce a worse artifact than omitting it, because a shallow interview reads as audited when it is not.

Self-advocacy is still detected and surfaced in the output header even though the interview itself does not run. Silently omitting a known incentive issue is a more serious failure than declining to audit it; the user needs to know that the bias exists and that this mode did not audit it, so they can choose to escalate.

Users whose decision turns on incentive integrity or recoverability should escalate to STANDARD or RAPID rather than rely on FAST.

---

## STANDARD — rationale

STANDARD is the default mode and runs the full module set. The design choice worth understanding is that **diagnostic loading is conditional, not automatic**.

Loading every diagnostic on every run would dilute their signal: diagnostics exist to deepen analysis when a module surfaces something that warrants drilling in, and reading them when nothing has fired trains the engine to apply their lenses indiscriminately. Conditional loading preserves the diagnostic-as-escalation pattern.

The same logic applies to base-rate and gotcha consultation. Base rates are most useful when a user's stated estimates are testable against typical historical ranges; pulling them into every analysis converts them from a calibration check into background noise. Gotcha patterns are similarly trigger-gated — visibility of the file in context does not mean the 8 patterns are active by default, because availability-bias would push the engine to cite patterns that do not match the plan. The trigger gating exists to prevent that drift.

---

## RAPID — rationale

RAPID exists for high-stakes, irreversible decisions made under hours of time pressure rather than days. Under that pressure, the value distribution across the 10 modules is not uniform.

Two modules become disproportionately valuable: **Module 4 (incentives)** and **Module 8 (detectability and recovery)**. Time pressure amplifies deadline-politics incentive distortion — the rush itself is often manufactured by the party most invested in the outcome. And reversibility analysis under pressure is precisely the work that is hardest to redo later if skipped, because the action it would have flagged has already been taken. These modules earn full-depth treatment in RAPID for that reason.

**The rationale for dropping Module 7 (base-rate reality check) in RAPID** is that base-rate calibration is low-yield under hours-of-time-pressure relative to incentive and recoverability work. The base-rate framing is most valuable when the user has time to revise estimates; under RAPID-style pressure, the user is not going to re-plan around a base rate — they will act. The engine concentrates effort where it can still change the decision.

**Pushback on the Module 4 interview must be handled explicitly, not silently.** If the user resists the interview citing time pressure, the rationale is that the interview is the single highest-leverage component of RAPID — skipping it would produce an artifact that looks audited but is not. Pretending the interview ran, or quietly dropping it, would mislead the user about what the verdict is built on. The engine must name the trade-off out loud so the user can make an informed choice; the exact phrasing and the consequences of partial answers are specified in `BEHAVIOR_SPEC.md`.

---

## DEEP — rationale

DEEP is used for high-stakes, expensive, or irreversible decisions where the user has explicitly traded time for thoroughness. Under those conditions, the cost of failing to consult a relevant diagnostic, gotcha, or domain reference exceeds the cost of loading material that turns out not to fire.

DEEP therefore loads everything unconditionally. Gotcha patterns are still trigger-gated at the point of citation — loading them is not the same as firing them — but the engine has the full pattern set in context rather than relying on recall. Domain-specific reference files are loaded based on the plan's domain so that the failure-pattern, base-rate, and incentive-pattern material specific to that domain is available without round-tripping.

The principle: in DEEP, the engine pays a context cost up front to eliminate the recall-vs-retrieval gap that conditional loading otherwise tolerates.
