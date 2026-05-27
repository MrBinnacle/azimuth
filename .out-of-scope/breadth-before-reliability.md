# Adding scope before the current tool's quality floor is verified

AZIMUTH does not add new capabilities, templates, references, or diagnostics while known quality gaps in the existing tool remain unaddressed. Proposals to expand surface area before reliability is verified are out of scope.

## Why this is out of scope

One tool that actually does what it says is worth more than a variety of applications that produce mediocre output. There is already enough AI slop in the world. Breadth that dilutes quality is worse than narrow scope with real depth.

The decision rule, when an addition is proposed:

- Does this make the tool **better at its core job**, or does it just make it **look bigger**?
- If quality gaps exist in the current tool (open eval findings, uncalibrated heuristics, identified placement conflicts), fix those first.
- When choosing between "does this add a new capability" and "does this make the existing capability more reliable" — choose reliability.

This rule applies symmetrically to:

- Domain templates (also gated by [template-expansion-without-evidence.md](./template-expansion-without-evidence.md))
- Reference files
- Diagnostic modules
- New SKILL.md modules
- Operating modes

The escape hatch is the same in every case: **close the open quality gap, then revisit the proposal.** Nothing about the proposal is rejected on its merits — only its sequencing.

## Prior requests

_To be added as requests come in._
