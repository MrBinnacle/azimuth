# AZIMUTH

A Claude Code skill that stress-tests a go/no-go decision before you commit to it. You describe
the decision. AZIMUTH audits its assumptions, traces the likely failure paths, names who gains if
the plan goes ahead unexamined, and returns one of nine verdicts with the reasons behind it.

It is frozen: a July 2026 test found that a newer Claude model does this unaided. See
[What a newer model changed](#what-a-newer-model-changed).

## Try it without installing

[azimuth-testbed.netlify.app](https://azimuth-testbed.netlify.app) runs the skill in your browser
with your own Anthropic API key. The key goes from your browser to Anthropic and is not stored.

## Install

```
npx skills add https://github.com/MrBinnacle/azimuth
```

Then, in Claude Code:

```
/azimuth We're planning to rewrite the legacy billing service in Q3
```

## Calibration: Boeing 737 MAX

The test of a verdict is whether you can change it by changing how you ask. In 2011 Boeing
committed that the 737 MAX would need no simulator training, with a $1M-per-plane penalty across
280 aircraft if it did. I described that decision three ways: a full brief, the bare numbers with
the company and aircraft removed, and an upbeat pitch that leads with the competitive win. Each ran
in a clean conversation on Claude Opus 4.7 against AZIMUTH v1.5.0.

| Framing | Verdict | Confidence |
|---|---|---|
| Full brief | REJECT | HIGH |
| Bare facts | REJECT | MEDIUM |
| Upbeat pitch | REJECT | MEDIUM |

The verdict held. Only the confidence moved, and it moved down when the model had less evidence.
This shows the verdict does not bend to framing. It does not claim the skill would have prevented
the crashes.

## What a newer model changed

AZIMUTH was built in May 2026 on one premise: the models of that time tended to agree with the plan
they were shown, so they needed a structured audit to push back. In July 2026 I tested that
premise against a newer model, Claude Opus 4.8. I set the pass/fail rule before the test ran. The
test used subtle flaws and a user pressing for a yes. The plain model, without the skill, caught 8
of 8 flaws, the same as with the skill. It even named its own conflict of interest without
prompting.

So at the frontier the skill no longer adds anything the model does not already do. I froze it
as it was, and it still works as written. The decision and the evidence are in
[ADR-0004](docs/adr/0004-frontier-obsoletes-the-engine.md). What remains useful is the method:
paired runs with and without the skill, and a pass/fail rule written before the run.

## Verdicts

`PROCEED`, `PROCEED WITH SAFEGUARDS`, `PILOT FIRST`, `REDUCE SCOPE`, `DELAY PENDING EVIDENCE` and
`REJECT` are go/no-go positions. `INSUFFICIENT SIGNAL` and `WRONG TOOL` mean the input cannot
support an analysis. `RESIDUAL-RISK-REGISTER` lists the remaining risks of a decision already made.

## What is here

- `azimuth/` is the skill: `SKILL.md`, its canonical rules in `BEHAVIOR_SPEC.md`, diagnostics,
  domain policies and reference base rates.
- `docs/adr/` holds the design decisions, including the freeze.
- `index.html` is the project page at
  [mrbinnacle.github.io/azimuth](https://mrbinnacle.github.io/azimuth/).

## Limits

AZIMUTH tests the decision as you frame it. It cannot tell you whether the framing is right. The
freeze result comes from single runs on one frontier model. Smaller models such as Sonnet and Haiku
were not tested, and the skill may still help them.

## License

MIT
