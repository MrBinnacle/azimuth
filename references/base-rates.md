# Base Rates Reference

Use when conducting Base Rate Reality Check (Module 7) in STANDARD or DEEP mode.

Purpose: Ground risk estimates in historical distributions, not imagination. Prefer these priors unless the user provides strong contradicting evidence.

These rates are approximate. They come from the sources cited at the end of each section. Treat them as calibration anchors, not precise predictions. Where the underlying evidence is contested or where rates are widely cited but not rigorously sourced, the language is hedged rather than numerical.

---

## Software Projects

**Budget overruns**
- Roughly half of large IT projects exceed their original budget; the McKinsey/Oxford BT Centre study of >5,400 large IT projects found ~45% ran over budget on average.
- The same study found ~17% of large IT projects went so poorly they threatened the company's existence.
- Larger projects (>$10M) overrun more often and by larger margins than smaller projects.

**Schedule overruns**
- A majority of software projects deliver late. The Standish Group's CHAOS reports have consistently shown only ~30–40% of projects deliver on time, on budget, and to scope.
- Average delays are commonly reported in the 30–50% range over original estimate, though figures vary by methodology and study.

**Scope creep**
- Roughly half of software projects experience significant unplanned scope expansion (Project Management Institute, *Pulse of the Profession* annual reports).
- Most common cause of cascade delay and budget overrun.
- Highest risk in projects with no formal change control.

**Feature utilization**
- Industry surveys (Pendo *Feature Adoption Report* 2019; earlier Standish *Modernization Project*) consistently show 30–50% of shipped features are rarely or never used.
- Implication: most software projects build more than is necessary.

**Rewrite projects**
- Big-bang legacy system rewrites are widely reported to fail or be cancelled at high rates, but the precise numbers cited in industry commentary often trace back to anecdote and opinion (e.g. Joel Spolsky, *Things You Should Never Do, Part I*, 2000) rather than rigorous study.
- The defensible signal: the McKinsey/Oxford study found 56% of large IT projects deliver less value than predicted. For rewrite-class projects specifically, treat that as the lower bound — rewrites tend to compound the same risks (scope, knowledge concentration, integration tax) that drive that distribution.
- Practical prior: assume a rewrite is more likely to fall short of intended outcomes than to meet them, and require explicit evidence to the contrary.

**Sources**
- Bloch, Blumberg, Laartz. *Delivering large-scale IT projects on time, on budget, and on value.* McKinsey & University of Oxford BT Centre for Major Programme Management, 2012.
- Standish Group, *CHAOS Reports* (multiple years).
- PMI, *Pulse of the Profession* (annual).
- Pendo, *2019 Feature Adoption Report*.

---

## Startups and New Ventures

**Survival rates** (US BLS Business Employment Dynamics, multi-year cohort tracking):
- Approximately 80% of new businesses survive their first year.
- Approximately 50% survive five years.
- Approximately 35% survive ten years (i.e., ~65% fail within ten).

**Top reported causes of startup failure** (CB Insights, *The Top 12 Reasons Startups Fail*, 2021 post-mortem analysis of 110+ failed startups):
1. No market need (~35% of failures)
2. Ran out of cash / failed to raise (~38% in 2021 update; historically ~29%)
3. Wrong team (~14–23%)
4. Got outcompeted (~20%)
5. Pricing / cost issues (~18%)
6. User-unfriendly product (~17%)
7. Product without business model (~17%)
8. Regulatory / legal challenges (~8%)

Note: These categories overlap. Most failures are multi-cause, not single-cause. CB Insights' specific percentages have shifted across their 2014, 2019, and 2021 reports — directionally consistent, methodologically a sample of self-reported post-mortems, not a random sample of all failed startups.

**Series A to exit success**: The fraction of Series A companies reaching a successful exit (IPO or meaningful acquisition) is widely reported as below 10%, though it varies significantly by vintage, sector, and how "successful exit" is defined.

**Time-to-PMF**: Founders commonly underestimate time-to-product-market-fit, often by a year or more. This is widely observed in venture commentary but not from a single rigorous study; treat as directional rather than precise.

**Sources**
- US Bureau of Labor Statistics, *Business Employment Dynamics* (annual entrepreneurship and survival tables).
- CB Insights, *The Top 12 Reasons Startups Fail* (2014, 2019, 2021).
- US Small Business Administration, *Frequently Asked Questions* (survival rate references).

---

## Product Launches

**Consumer product failure rate**: 70–95% of new consumer products fail within their first 1–2 years, depending on category. Most-cited is Clayton Christensen's estimate of ~95% in CPG; Nielsen and others report 70–80% across broader categories. The high end of the range reflects categories with very low marginal cost of trying (apps, CPG); enterprise products fail less frequently but more expensively.

**Enterprise feature adoption**: A meaningful share of new enterprise software features see low adoption within their first 6 months. Pendo's 2019 dataset showed ~80% of features in B2B SaaS fall in the "rarely or never used" tail.

**B2B sales cycle vs. forecast**: B2B sales cycles routinely run longer than initial forecasts. The 2× to 6× multiplier sometimes cited is anecdotal rather than from a rigorous study; treat as a directional warning that initial timeline estimates are systematically optimistic.

**Beta-to-GA conversion**: Conversion from beta users to paid customers in B2B SaaS is widely reported in the 15–30% range, but this figure is highly dependent on beta program design, qualification, and pricing — treat the range as a sanity check, not a precise prior.

**Sources**
- Christensen, *The Innovator's Solution* (2003) and follow-on commentary.
- Nielsen *Breakthrough Innovation Report* series.
- Pendo, *2019 Feature Adoption Report*.

---

## Hiring and Talent

**New hire failure rate**: Roughly 40–50% of new hires are reported to be underperforming or to have departed within 18 months. The most-cited figure is from Mark Murphy / Leadership IQ (~46% within 18 months across 5,000+ hires), though the specific number varies by sector and methodology.

**Primary causes of new hire failure** (Leadership IQ study, Hiring for Attitude):
1. Coachability (~26% of failures)
2. Emotional intelligence / interpersonal fit (~23%)
3. Motivation (~17%)
4. Temperament (~15%)
5. Technical competence (~11%)

The implication: most new-hire failure is *not* about skill mismatch. It's about culture, fit, and motivation. Reference-check and structured-interview practices that emphasize past behavior outperform credential-focused screens.

**Time-to-productivity**: Knowledge workers typically take 3–6 months to reach full productivity for individual contributor roles, and 6–12 months for management roles, though figures vary widely by role type and onboarding quality.

**Interview validity**: Meta-analyses (Schmidt & Hunter, *Personnel Selection*, 1998 and 2016 update) consistently find structured interviews and work-sample tests substantially outperform unstructured interviews on predictive validity for job performance — by approximately 2× on validity coefficients.

**Sources**
- Murphy, *Hiring for Attitude* (Leadership IQ research, 2011).
- Schmidt, Oh, Shaffer, *The Validity and Utility of Selection Methods in Personnel Psychology* (1998 / 2016 update).

---

## Mergers, Partnerships, and Integrations

**M&A value destruction**: The most widely cited figure is that 70–90% of mergers fail to create shareholder value. This range traces to multiple studies (KPMG *World Class Transactions*, HBR analyses, Christensen et al. *The Big Idea: The New M&A Playbook* 2011) using different definitions of "failure" — value destruction, target underperformance, or post-deal divestiture. The 70–90% range is directionally well-supported; the specific number depends on the methodology.

**Integration overrun**: Post-merger integration timelines are commonly underestimated; specific overrun rates vary across consulting studies (KPMG, Bain, McKinsey post-merger integration practice publications).

**Partnership dissolution**: Formal business partnerships dissolve at high rates within their first several years, most commonly due to misaligned incentives, unequal effort distribution, or shifting strategic priorities. Specific rates are not well-sourced; treat as a structural warning.

**Sources**
- Christensen, Alton, Rising, Waldeck. *The Big Idea: The New M&A Playbook.* Harvard Business Review, March 2011.
- KPMG, *World Class Transactions* and follow-on M&A studies.

---

## IT and Infrastructure Migrations

**Cloud migration overruns**: A meaningful share of cloud migration projects exceed budget or timeline. Specific percentages vary across vendor and consulting studies (Gartner, Flexera *State of the Cloud Report*); treat the directional claim as solid but the specific numbers as advisory.

**Data migration defects**: Data migration projects routinely surface defects during or after migration, most commonly from undocumented data dependencies or schema mismatches. The 20–40% defect-discovery range is commonly cited in vendor literature; treat as directional.

**Zero-downtime migration on first attempt**: Successful zero-downtime cutovers on first attempt are uncommon in surveyed enterprise environments. Multiple staged attempts are the norm rather than the exception.

**Sources**
- Flexera, *State of the Cloud Report* (annual).
- Gartner research notes on cloud migration (multiple years).

---

## Organizational Change

**Change management failure rate**: 60–70% of large-scale organizational change initiatives fail to achieve intended outcomes. This is one of the most widely cited statistics in the change-management literature (Kotter, *Leading Change*, 1996; McKinsey *Transformational Change* studies). Definitions of "failure" vary — failed to meet objectives, reverted, or never institutionalized.

**Primary failure modes** (Kotter, *Leading Change*; McKinsey *Why do most transformations fail?*):
1. Insufficient executive sponsorship
2. Middle management resistance
3. Employee burnout from initiative overload
4. Reversion after initial compliance

**Behavioral change timelines**: Lasting behavioral change in organizations consistently takes longer than initial project plans assume — multi-quarter horizons are typical for habits and norms to stabilize.

**Sources**
- Kotter, *Leading Change* (1996).
- McKinsey, *Why do most transformations fail? A conversation with Harry Robinson* (2019).

---

## How to Use These Rates

1. Identify which category best matches the initiative.
2. Use the base rate as the prior probability of failure.
3. Ask: "What evidence do we have that shifts this probability up or down?"
4. If no strong evidence exists to shift it, treat the base rate as credible.
5. Surface the base rate to the user when their confidence appears inconsistent with it.

Do not present these rates as certainties. Present them as: "Historically, initiatives like this fail at X rate. What makes this case different?"

---

## A Note on Sourcing

These figures are drawn from the named primary studies and widely cited industry research. Specific percentages shift across studies and definitions; the ranges and directional claims are robust, the precise numbers are not. When citing these rates to a user, name the source if challenged. Do not assert precision the underlying evidence does not support.
