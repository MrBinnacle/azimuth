# Base Rates Reference

Load when Module 7 surfaces estimates that deviate from typical historical ranges — applicable when the plan involves software projects, startups, launches, hires, M&A, migrations, or organizational change.

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

**What the peer-reviewed record supports:** In public-company acquisitions, acquirers on average earn near-zero or slightly negative abnormal returns around deal announcement (mean acquirer CAR approximately −0.7%). The combined entity (acquirer + target) creates modest positive value on average (+1.8%). Targets capture the value creation via the acquisition premium (+16–30%). This is the most replicated finding in 50+ years of M&A event study research.

**The "70–90% fail" figure is a consulting industry estimate, not peer-reviewed evidence.** It traces primarily to KPMG's 1999 "Unlocking Shareholder Value" survey (which measured acquirer share price vs. sector peer index at 6 months post-close — not total value creation) and has propagated by self-citation through practitioner commentary. The peer-reviewed literature does not produce a 70–90% failure rate. King et al. (2004, SMJ) meta-analysis of 93 studies found that identified moderators explain only ~5% of variance in M&A outcomes — meaning "failure rate" is highly sensitive to which definition is used (8 definitions in the literature produce rates from 20% to 83%).

**Actionable deal-level predictors (robust in peer-reviewed evidence):**
- *Payment method*: Cash-financed acquisitions consistently outperform stock-financed acquisitions. Stock deals signal acquirer overvaluation (Myers & Majluf adverse selection). Loughran & Vijh (1997, JF) 5-year returns: cash acquirers +61.7%, stock acquirers +14.9% vs. matched controls.
- *Target type*: Private target acquisitions yield positive acquirer announcement returns on average (+2.1%); public target acquisitions yield near-zero to negative (−1.0%). Acquirers pay a control premium they cannot extract from private sellers.
- *Value distribution*: M&A is not zero-sum but is asymmetrically distributed — combined entities create value on average; the question for the acquirer's board is whether acquirer shareholders benefit after paying the premium.

**Cost vs. revenue synergy reliability:** The direction is well-supported: cost synergies are realized more reliably than revenue synergies, which are produced under deal-team optimism and competitive pressure. Revenue synergy estimates are consistently revised down post-close. Specific realization rates (e.g., "43% of synergies captured") come from consulting firm proprietary surveys (McKinsey Quarterly, BCG), not peer-reviewed studies — treat the direction as defensible, the percentages as advisory only.

**Integration overrun**: Post-merger integration timelines are commonly underestimated. This directional claim is consistent with planning fallacy research broadly. Specific overrun rates in consulting publications (KPMG, Bain, McKinsey integration practice) should be treated as advisory given selection bias toward troubled engagements.

**Partnership dissolution**: Formal business partnerships dissolve at high rates within their first several years, most commonly due to misaligned incentives, unequal effort distribution, or shifting strategic priorities. Specific rates are not well-sourced in the peer-reviewed literature; treat as a structural warning.

**Sources**
- Andrade, G., Mitchell, M., & Stafford, E. (2001). New evidence and perspectives on mergers. *Journal of Economic Perspectives*, 15(2), 103–120. (n=3,688 US mergers, 1973–1998)
- King, D.R., Dalton, D.R., Daily, C.M., & Covin, J.G. (2004). Meta-analyses of post-acquisition performance. *Strategic Management Journal*, 25(2), 187–200. (93-study meta-analysis)
- Loughran, T., & Vijh, A.M. (1997). Do long-term shareholders benefit from corporate acquisitions? *Journal of Finance*, 52(5), 1765–1790.
- Fuller, K., Netter, J., & Stegemoller, M. (2002). What do returns to acquiring firms tell us? *Journal of Finance*, 57(4), 1763–1793.
- Tuch, C., & O'Sullivan, N. (2007). The impact of acquisitions on firm performance: A review. *International Journal of Management Reviews*, 9(2), 141–170. (systematic review tracing consulting failure claims to non-peer-reviewed origins)

---

## IT and Infrastructure Migrations

**Cloud migration overruns**: A meaningful share of cloud migration projects exceed budget or timeline. Specific percentages vary across vendor and consulting studies (Gartner, Flexera *State of the Cloud Report*); treat the directional claim as solid but the specific numbers as advisory.

**Post-cutover operational cost overruns**: Cloud migrations often surface ongoing spend management problems separate from migration project delivery. Flexera's *State of the Cloud* 2025 (750+ respondents, vendor-sponsored survey with self-selecting audience toward organizations with spend issues) reports 84% of organizations struggle to manage cloud spend, with annual cloud budgets routinely exceeded by double-digit percentages. The directional claim is solid; specific numbers are advisory.

**Data migration defects**: Data migration projects routinely surface defects during or after migration, most commonly from undocumented data dependencies or schema mismatches. The 20–40% defect-discovery range is commonly cited in vendor literature; treat as directional.

**Zero-downtime migration on first attempt**: Successful zero-downtime cutovers on first attempt are uncommon in surveyed enterprise environments. Multiple staged attempts are the norm rather than the exception.

**Sources**
- Flexera, *State of the Cloud Report* 2025. https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf
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

## Structured Failure Analysis

**Classification**: Premortem-class techniques (prospective hindsight, structured failure analysis) fall in the **debiasing** category of bias-mitigation interventions — not choice architecture. The distinction matters for scope: debiasing requires active decision-maker involvement; choice architecture modifies the environment without it.

**When debiasing is indicated** (Fasolo, Heard & Scopelliti, 2025 — integrative review of 100 experimental studies, Journal of Management):
- Early stage of decision-making (pre-commitment, information search, option identification)
- High uncertainty / novel / complex / unstructured decisions
- Organizations with diverse goals, low pre-existing trust, or high-agency cultures
- Decisions where planning fallacy is the primary risk — planning fallacy has no choice-architecture remedy in this review; debiasing is the only empirically supported approach

**Evidence ceiling**: This is an integrative review, not a meta-analysis. No aggregate effect sizes are reported. Fasolo 2025 supports the taxonomy and scope conditions; effect-size claims must be sourced from primary studies.

**Output rates** (Roose, Lehman & Veinott, 2023 — 10 real game development teams, N=68, Human Factors, Sage):
- Teams identified an average of 17.8 unique failure reasons per session
- Teams generated an average of 16.7 corresponding mitigations per session
- **Plan-revision gap**: despite identifying risks and mitigations, surprisingly few teams revised their plans to address the most commonly flagged structural risk (scope complexity). Surfacing failure reasons does not automatically produce plan changes — especially when remediation requires reducing scope rather than improving execution.

Domain caveat: student game-development context; n=10 teams. Directional signal is solid; enterprise generalizability requires independent replication.

**Sources**
- Fasolo, Heard & Scopelliti. *Mitigating Cognitive Bias to Improve Organizational Decisions: An Integrative Review, Framework, and Research Agenda.* Journal of Management, 2025. DOI: 10.1177/01492063241287188. Open access: https://eprints.lse.ac.uk/125404/
- Roose, Lehman & Veinott. *Premortems in Game Development Teams: Impact and Potential.* Human Factors, Sage, 2023. DOI: 10.1177/21695067231193680.

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
