# Distribution Strategy — AZIMUTH

This document is not for the repo. It's the playbook for getting to 100+ stars.

---

## Competitive Position

**Existing premortem skills (73 stars):** Single SKILL.md, code/PR review focus, tigers/elephants framework. Built for devs reviewing implementations.

**AZIMUTH:** 14-file decision analysis system with domain-specific templates, historical base rates, structural diagnostics. Built for operators, PMs, and founders making go/no-go calls. The audiences barely overlap. Don't acknowledge competitors — just be categorically better.

**The name is a differentiator, not just a label.** An azimuth is a navigational bearing verified before movement. It lands immediately with anyone who's done land nav, resonates with the PM/operator audience who understands direction-setting, and teaches something to everyone who looks it up. That's a name with work in it.

---

## GitHub Setup Checklist

### Repo structure
- [ ] `MrBinnacle/azimuth` (standalone repo, not buried in a collection)
- [ ] Description: "Decision-quality azimuth agent skill for Claude, Codex, Gemini CLI, and Cursor — go/no-go analysis for launches, hires, rewrites, and strategic bets"
- [ ] Website: link to agentskills.so or similar marketplace listing when live

### Topics (add all of these)
```
claude-skills
agent-skills
azimuth
decision-making
risk-analysis
claude-code
codex-skills
gemini-skills
cursor-skills
product-management
```

### Files to include
- [x] README.md (complete)
- [x] azimuth/ (full skill folder)
- [ ] LICENSE (MIT)
- [ ] CHANGELOG.md (start one even if v1.0.0 only)

---

## Aggregator Submissions (do these first — compounding effect)

Each of these has thousands of followers and submitting costs 5 minutes. PR or issue as appropriate.

### Tier 1 — Submit immediately

| Repo | How | Priority |
|------|-----|----------|
| `VoltAgent/awesome-agent-skills` | PR to add to decision-making section | HIGHEST |
| `heilcheng/awesome-agent-skills` | PR or issue | HIGH |
| `addyosmani/agent-skills` | Check if they accept external contributions | HIGH |
| `agentskills.io` / `agentskills.so` | Submit via their listing form | HIGH |
| Anthropic skills marketplace | Submit when available | HIGH |

### Tier 2 — Submit within first week

| Resource | Format |
|----------|--------|
| `explainx.ai/skills` | Submit via their form (they already list azimuth competitors) |
| `tessl.io` registry | Submit listing |
| Claude.ai community Discord | Drop link in skills/tools channel |
| Anthropic Discord | Community showcase |

---

## Reddit Strategy (your highest-conviction channel)

You've already turned Reddit into business relationships. Same playbook applies here.

### Subreddits, sequenced by audience fit

**r/ClaudeAI** — Primary. Largest Claude community. Post announcement here first.

*Post angle:* "Built AZIMUTH — a decision analysis skill for Claude. Not code review. Go/no-go on launches, hires, rewrites, strategic bets. 14 files, base rates from real project failure data, domain-specific templates. Named after the navigational bearing you verify before you step off."

Include: folder structure screenshot, example output snippet, install command. Don't bury the lede — lead with the output example, then explain what produced it.

**r/ProductManagement** — Strong secondary. This audience needs this exact thing and doesn't know agent skills exist yet.

*Post angle:* "I built an AI skill that runs Gary Klein-style pre-commitment analysis on product decisions. Here's what it surfaced on a real launch scenario." Show the example output. Don't lead with "agent skill" — that's jargon to them. Lead with the output.

**r/startups** — Good fit for the founder/strategic audience.

*Post angle:* "Ran AZIMUTH on my last 3 product decisions before committing. Here's what it found that I missed." Narrative format. The methodology is the hook, the skill is the distribution vehicle.

**r/SideProject** — Authentic build narrative. "Built a decision-analysis tool for Claude and Codex. Named it AZIMUTH — the navigational bearing you lock in before you step off."

**r/MachineLearning / r/artificial** — Lower fit, but credibility signal. Post after traction elsewhere.

### Post timing
Post r/ClaudeAI and r/ProductManagement within 24 hours of launch. These will seed the star count. Aggregator submissions compound from there.

### Comment strategy
After your main posts land, watch for questions in any subreddit about:
- "what could go wrong with X plan"
- "how do I evaluate whether to do X"
- "risk analysis for Y decision"

Drop in a non-spammy reply: "I built a azimuth skill for this exact scenario, happy to share." You know this move.

---

## Content Strategy (GitHub stars come from outside GitHub)

### LinkedIn (if active)
One post. Lead with the framework output — not the code. "Most decisions fail because of problems that were already present before execution. I built a tool that finds them." Then explain the skill.

### Dev.to / Hashnode
Write one article: "Why I built a decision-analysis azimuth for AI agents (and why code-focused azimuths miss half the picture)." Technical enough to be credible, accessible enough for PM readers. This article then gets shared in PM newsletters.

### PM newsletters / communities
Lenny's Newsletter community, Reforge alumni Slack, Mind the Product — any community where people talk about product process. One post showing the example output and the methodology behind it. The skill is the delivery mechanism for the methodology.

---

## Star Growth Model

| Phase | Action | Expected outcome |
|-------|--------|-----------------|
| Day 1 | Aggregator PRs submitted | Listed within 48–72hrs |
| Day 1–2 | r/ClaudeAI + r/ProductManagement posts | 20–40 stars from Reddit |
| Week 1 | Aggregators go live | 15–30 stars from listing traffic |
| Week 2 | Dev.to article + LinkedIn | 10–20 stars |
| Week 3+ | Organic search + skill marketplace | Compounding |

Realistic 90-day target: **100–150 stars.** Possible upside if a PM newsletter picks it up: 300+.

---

## The Unfair Advantage

The existing azimuth skills were built by devs for devs. The language, framing, and output format are all code-brained. This skill was built by someone who thinks in terms of institutional failure, incentive misalignment, and historical base rates — and that shows in the output. That's the moat. The PM and founder audience will recognize it immediately.

---

## What Not To Do

- Don't post to every subreddit at once. Sequence matters; early upvotes on one post help the algorithm.
- Don't mention the 73-star repo anywhere, ever. Your differentiation is additive, not comparative.
- Don't pad the README with badges and "coming soon" sections. Ship clean.
- Don't add a CONTRIBUTING.md for v1. Opens surface area you can't support yet.
