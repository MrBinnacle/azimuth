# Org Change Azimuth Template

This file configures runtime presentation for org change decisions. Decision authority lives in `BEHAVIOR_SPEC.md`. This file does not define rules.

Use this template when:
- Plan involves a restructure, reorganization, function consolidation, role elimination, or leadership transition that materially changes reporting lines, decision authorities, or team composition
- The analysis is pre-announcement — the design is being evaluated before commitment
- Audience includes the executive sponsor, CHRO/People leader, or the leader designing the change

**Pre-commitment window:** This template applies when the restructure design is being evaluated before announcement. If the announcement has already been made or the restructure is underway, the appropriate Module 10 output is RESIDUAL-RISK-REGISTER, not a go/no-go verdict.

---

## Template

---

**ORG CHANGE AZIMUTH — [Initiative Name]**
*Type: [Restructure / Consolidation / Role Elimination / Leadership Transition] | Planned Announcement: [Date] | Affected Population: [Headcount / Teams]*

---

**VERDICT**
[One sentence. Is this restructure design sound, and is the organization ready to absorb it?]

---

**RESTRUCTURE OBJECTIVE**

[What specific failure, dysfunction, or gap does this restructure address? State in measurable terms — not "improve alignment" but "reduce decision cycle time for [class of decisions] from [X] to [Y]" or "eliminate duplicate ownership of [function] across [teams]."]

If no measurable objective is defined: flag this as the primary risk. A restructure with no measurable outcome cannot succeed or fail — it can only be completed.

---

**PRE-COMMITMENT GATES**

Run before analysis. Any ✗ changes the analysis frame.

| Gate | Status | Notes |
|------|--------|-------|
| Announcement date is not yet fixed — the design can still change before commitment | ☐ ✓ OPEN / ☐ ✗ FIXED | If ✗: this is a post-commitment input. Module 10 returns RESIDUAL-RISK-REGISTER. (activates RULE-4.12 RESIDUAL-RISK-REGISTER) |
| A measurable success metric exists for 12 months post-restructure | ☐ ✓ DEFINED / ☐ ✗ ABSENT | If ✗: analysis cannot ground a verdict. Module 10 returns INSUFFICIENT SIGNAL. (activates RULE-4.8 INSUFFICIENT SIGNAL) |
| The person who designed this restructure has a defined role in the new structure | ☐ ✓ YES / ☐ ✗ NO | If ✗: designer accountability gap — flag as primary structural risk before proceeding. |

---

**INCENTIVE ALIGNMENT SCAN**

Before structural analysis, determine whether this restructure is being pursued for the right reasons.

| Actor | Their Incentive | Aligned with Stated Objective? | Notes |
|-------|----------------|-------------------------------|-------|
| Proposer (new leader / CEO / board sponsor) | [Power consolidation / budget control / expanded span of control / new leader establishing authority] | ☐ Yes / ☐ No / ☐ Unknown | |
| HR / People function | [Implementing what leadership decides / avoiding conflict with sponsor / process compliance over outcome] | ☐ Yes / ☐ No / ☐ Unknown | |
| Senior leaders who gain authority | [Expanded scope / budget / team — incentive to support regardless of outcome quality] | ☐ Yes / ☐ No / ☐ Unknown | |
| Senior leaders who lose authority | [Reduced scope / budget / team — potential resistance, disengagement, or departure] | ☐ Yes / ☐ No / ☐ Unknown | |
| External consultants (if involved) | [Designing a solution that requires their continued engagement to implement] | ☐ Yes / ☐ No / ☐ Unknown | |
| Middle management | [Have they been consulted? Their resistance is the highest-probability failure mode.] | ☐ Yes / ☐ No / ☐ Unknown | |

**Key questions:**
- Who first proposed this restructure — and what do they gain if it proceeds regardless of whether the stated objective is achieved?
- Which senior leaders lose authority under the new structure, and have their likely responses been explicitly planned for?
- Has middle management been consulted in the design, or only informed of the outcome?
- If external consultants shaped the design, does implementation require their continued presence?

**Flag if:** proposer gains power, budget, or span of control independent of outcome quality; senior leaders losing authority have not been engaged before announcement; middle management was informed rather than consulted; external consultants designed a solution requiring their continued engagement.

Proposer incentive misalignment or middle-management exclusion triggers the cross-cutting confidence cap (see `BEHAVIOR_SPEC.md` RULE-6.5).

---

**CHANGE CONTEXT**

| Dimension | Current State | Proposed State |
|-----------|--------------|----------------|
| Reporting structure (key changes) | | |
| Decision authorities (who decides what) | | |
| Team composition / headcount | | |
| In-flight initiatives affected | | |

**Affected population:**
- Total headcount impacted: [N]
- Roles or titles changing: [count or list]
- Reporting line changes: [count or list]
- Role eliminations: [count] — named or to-be-determined?

**Change history:** How many major organizational changes in the past 18 months? [N] — [brief description]. If 2 or more: explicitly assess change fatigue stacking before proceeding. Each prior change is still being absorbed.

---

**FAILURE PATH ANALYSIS**

Construct the three most plausible failure chains. Draw from `references/org-change-patterns.md`.

**Path 1**: [Trigger] → [cascade] → [visible failure] → [business cost]
Example: Announcement leaks before Day 1 communication → key performers receive rumor without context → high performers with options begin exit conversations → attrition concentrated in most mobile talent before restructure stabilizes

**Path 2**: [Trigger] → [cascade] → [visible failure] → [business cost]

**Path 3**: [Trigger] → [cascade] → [visible failure] → [business cost]

---

**BEHAVIORAL CHANGE READINESS**

A restructure is not complete when the org chart changes. It is complete when decision-making behavior, meeting patterns, and accountability norms reflect the new structure. The gap between structural and behavioral change is where most restructures fail silently.

| Indicator | Defined? | Owner | Measurement Date |
|-----------|----------|-------|-----------------|
| Primary behavioral outcome (what specifically changes, not just what structure changes) | ☐ Yes / ☐ No | | |
| 6-month behavioral review scheduled and resourced | ☐ Yes / ☐ No | | |
| Early reversion signals defined | ☐ Yes / ☐ No | | |
| Mechanism for affected teams to signal when new structure is not functioning | ☐ Yes / ☐ No | | |

If behavioral indicators are not defined: the restructure has no mechanism to detect failure until it is too late to course-correct. Structural completion will be declared; behavioral change will not follow.

---

**COMMUNICATION PLAN READINESS**

| Element | Status | Owner |
|---------|--------|-------|
| Pre-announcement circle defined (who knows, in what order, by when) | ☐ Ready / ☐ Not ready | |
| Leak risk assessed for pre-announcement circle size and time window | ☐ Assessed / ☐ Unknown | |
| Day 1 communication sequence scripted with named owners and timing | ☐ Ready / ☐ Not ready | |
| Cascade timing defined — who hears in what order | ☐ Ready / ☐ Not ready | |
| Manager preparation complete — managers scripted before they cascade | ☐ Ready / ☐ Not ready | |
| Time between decision and announcement: [N days] | | |

Manager preparation is the highest-trust communication channel and the most common failure point. An announcement without manager prep produces rumors that managers must address without context — precisely when trust is lowest.

---

**ACCOUNTABILITY TRANSFER**

For each major accountability that changes ownership under this restructure:

| Decision Domain / Initiative / Budget | Former Owner | New Owner | Handoff Status |
|--------------------------------------|-------------|-----------|----------------|
| [Decision domain] | | | ☐ Explicit / ☐ Assumed |
| [In-flight initiative] | | | ☐ Explicit / ☐ Assumed |
| [Budget line] | | | ☐ Explicit / ☐ Assumed |

**Any "Assumed" handoff is an accountability gap.** Former owners not explicitly released will continue acting as if they own it — or will stop acting, waiting for clarity that never arrives. New owners not explicitly designated will defer, not lead.

---

**EARLY WARNING INDICATORS**

Signs within the first 30–60 days that this restructure is not working:

- [indicator] — Response: [what to do if observed]
- [indicator] — Response: [what to do if observed]
- [indicator] — Response: [what to do if observed]

Do not wait for 90-day review to act on these signals. By 90 days, informal reversion patterns have hardened.

---

**RECOMMENDED DECISION**

☐ PROCEED — Restructure design is sound; communication, behavioral change, and accountability transfer plans are in place
☐ PROCEED WITH SAFEGUARDS — Specific requirements must be met before announcement (listed below)
☐ PILOT FIRST — Validate [specific design assumption] with a subset of the organization before full rollout
☐ DELAY PENDING EVIDENCE — [Specific gate requiring resolution before announcement]
☐ REJECT — [Structural reason this design should not proceed]

**Required before announcement:**
1. [action] — Owner: [name] — By: [date]
2. [action]

---

**CONFIDENCE LEVEL**: [Low / Medium / High]
**Basis**: [Pre-commitment gate status, incentive alignment assessment, behavioral change plan completeness, communication plan readiness, accountability transfer completeness]
