# ADR-0004 — Frontier models obsolete the analytical engine → MINIMIZE (freeze)

Status: Accepted (2026-07-04)
Supersedes the direction of: the v1.6.0-era "keep improving the engine" trajectory.
Related: ADR-0002 (engine-layer governance), the eval program (`evals/`), Phase-1 re-grounding record.

## Context

AZIMUTH's founding premise (v1.0.0, 2026-05-04) is that base LLMs sycophantically validate plans, so a forcing-function scaffold is needed to make the model audit assumptions, scan incentives, construct failure paths, and cap confidence. That premise was true for the 2026-05 model era against which the skill was evaluated (sonnet-4-6 / opus-4-6/4-7).

Claude models progressed. A re-grounding pass against **Opus 4.8** was run, followed by a council and a repositioning experiment. Three independent measurements converged:

1. **Phase-1 paired eval (Opus 4.8):** all five tested load-bearing hooks classified **corroborating-or-weaker** — the frontier model produces the reasoning natively.
2. **Pivot tracer v0** (a repositioning to an "independent COI gate on AI-proposed plans"; obvious-flaw scenarios): naked frontier self-review caught 8/8; the proposed blind-adjudicator mechanism added **zero lift**.
3. **Pivot tracer v1** (pre-registered fair test — subtle flaws + adversarial-user pressure + genuine proposer investment, the strongest condition): **8/8 caught both conditions, naked miss-rate 0, lift 0/4.** Under pressure the naked proposer reproduced AZIMUTH's own irreducible thesis unprompted — e.g. *"the fix is mine so I cannot be the sole reviewer,"* naming the conflicted requester and sunk-cost pressure without the skill.

The decision rule for tracer v1 was **pre-registered before running** (`lift ≤ 1/4 → null → MINIMIZE`), specifically so the pivot's advocate could not move the goalposts. The result was a clean null.

## Decision

**MINIMIZE, in the "freeze + preserve" form.**

- Stop all feature investment in the analytical engine and in the COI-gate pivot. The engine's model-compensating value decays to ~zero at the frontier; the pivot mechanism is redundant because the frontier proposer already self-gates and self-names its conflict of interest.
- **No `azimuth/` surgery.** The shipped skill is left as-is and marked maintenance-frozen (honest status note in the root README + `docs/STATE.md`).
- **Preserve the durable assets:** the paired production/control eval methodology, the tracer design, the Boeing calibration result, and this falsification record. Publish the methodology write-up.
- Downgrade the awesome-claude-code #1803 pursuit to "will not chase"; unblock any work that was deferred behind it.
- RETIRE/archive remains available later at ~zero cost (pure-markdown repo) if even the frozen presence stops earning its keep.

## Consequences

- **Honest, not defeatist.** By AZIMUTH's own philosophy (`.out-of-scope/`: never ship a technique without evidence it beats baseline), continuing to assert an edge over Opus 4.8 would be shipping an unproven claim. Freezing is the disciplined move.
- The one idea that survives — *a conflicted proposer should not silently self-adjudicate* — is now native frontier behavior; its future home, if any, is a weak-model (below-floor) artifact, which is MINIMIZE-scoped, not the engine.
- Formal limits: tracers were single-seed on the Agent-default (Opus 4.8-class) model; the Sonnet/Haiku floor population is unmeasured. Three frontier nulls + native COI reproduction make further engine investment unjustified regardless.

## Post-execution footer
- Records the executed decision; freeze bookkeeping (CHANGELOG, STATE.md, README status note) applied in the same change-set (see CHANGELOG [Unreleased]).
