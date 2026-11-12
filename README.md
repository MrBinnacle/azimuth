# AZIMUTH

A Claude Code skill that stress-tests a go/no-go decision before you commit to it. You describe
the decision. AZIMUTH audits its assumptions, traces the likely failure paths, names who gains if
the plan goes ahead unexamined, and returns one of nine verdicts with the reasons behind it.

It is frozen: in July 2026 tests, a newer Claude model did this reasoning unaided. See
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

The verdict held in all three runs, one run per framing. Only the confidence moved: it was highest
with the full brief and lower for the other two. It does not claim the skill would have prevented
the crashes.

## What a newer model changed

AZIMUTH was built in May 2026 on one premise: the models of that time tended to agree with the plan
they were shown, so they needed a structured audit to push back. In July 2026 I re-tested that
premise on an Opus 4.8-class model:

- **The skill against the plain model.** In paired runs with and without the skill, the plain
  model produced the reasoning of all five tested parts of the skill on its own.
- **A proposed successor.** I also tested a new idea, a separate reviewer that checks a plan the
  AI itself proposed. I set the pass/fail rule before the stronger run. In both runs the plain
  model caught every planted flaw by reviewing its own plan, so the extra reviewer added nothing.
  Under pressure it named its own conflict of interest without being asked.

On that evidence I stopped developing the skill and left it as it was. The decision is recorded in
[ADR-0004](docs/adr/0004-frontier-obsoletes-the-engine.md); the run records behind it are not
published. What remains useful is the method: paired runs with and without the skill, and a
pass/fail rule written before the run.

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
freeze tests were single runs on one frontier model. They did not test smaller models such as
Sonnet and Haiku, and the skill may still help them. In very long sessions `SKILL.md` may load
incompletely, so some checks may not fire.

## License

MIT
