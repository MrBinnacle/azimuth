# New domain templates without empirical support

AZIMUTH only ships a new domain template (a routed `templates/*-azimuth.md` for a new decision type) when the empirical evidence explicitly supports the technique working for that decision context. Plausible-sounding use cases without evidence are out of scope, no matter how often they are requested.

## Why this is out of scope

Every domain template hard-codes a structure into the routing layer. A template asserts that AZIMUTH's pre-commitment analysis produces a useful verdict for the decision type it routes. If the underlying technique (premortem, RCF, base-rate anchoring) was never validated for that context, the template produces output that *looks like* an AZIMUTH verdict but isn't grounded — what the maintainer calls "half-vibe coded slop." The cost is reputational: outputs degrade trust in every other verdict the tool produces.

The evidence bar, in order:

1. **Stage 2 scope conditions** (Fasolo 2025) — does the proposed use case match the debiasing context where the technique was shown to work?
2. **Stage 3 failure modes** — does the use case have elevated risk of attribution side-effect, plan-revision gap, or overcorrection?
3. **Stage 4 tool fit** — is premortem actually the right tool, or would RCF or another intervention be more appropriate?

A new template gets added only when the evidence says the technique will do what the template implies it does. Otherwise the request is closed.

The escape hatch already exists:

- **Default output template** (`references/output-template.md`) handles any decision routed as Layer 3 "Other." Users who want analysis for an unvalidated decision type get the default format, with no claim that the technique is calibrated for their domain.

This keeps the tool honest about where it has evidence and where it does not.

## Prior requests

_To be added as requests come in._
