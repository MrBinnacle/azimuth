# Case Study: Open-Source Repo Launch Timing During Active Job Search

**Purpose of this file**: Demonstrate AZIMUTH STANDARD on a real timing and sequencing decision with competing dependencies. The scenario involves a solo developer deciding when to make a significant open-source project public while simultaneously running a job search that references it.

**Mode**: STANDARD

---

## Input

A developer has been building a local-first knowledge management system as an independent project. The system is substantial: 600+ tests across three languages, 40+ gate-locked build phases, a calibrated ML pipeline, encryption at rest, and a security model with four enforced invariants. The README includes architecture diagrams, screenshots, a literature survey, and running instructions.

The repo is currently private. The developer's resume and CV both reference the project with a GitHub URL that currently resolves to nothing. A second, smaller project — an open-source agent skill shipped in one day — is already public on the same GitHub profile.

The developer wants to build a landing page before making the repo public. There is no defined scope or timeline for the landing page. The developer is also preparing to submit the smaller project to tool aggregators, with a ~30-day eligibility window starting now.

The developer is in an active job search targeting senior PM and AI operations roles at growth-stage AI companies (80-500 employees). Applications are going out now.

**Key context**:
- The repo root contains ~14 debug artifacts, handoff notes, and temporary files visible at the top level
- The CI badge in the README links to GitHub Actions on the private repo
- The project has been renamed; some downstream career materials still reference the old name
- The GitHub profile currently shows only one public repo

---

## AZIMUTH Output

### Azimuth Verdict

Make the repo public, but not yet. The README and code are strong; the surrounding context isn't ready.

### Recommended Decision

**PROCEED WITH SAFEGUARDS** — Make the repo public within the 30-day aggregator eligibility window, but only after three specific gates are cleared. Do not wait for the landing page if the landing page isn't scoped and timeboxed.

Rationale: The repo is the strongest proof-point artifact in the developer's job search system. Every day it stays private during an active search is a day a hiring manager clicks the GitHub URL and sees one repo instead of two. But a premature launch with visible debris creates a first impression that's hard to overwrite.

### Confidence Level

**Medium-High.** The core asset (code, README, architecture) is verified strong. The uncertainty is around execution sequencing — specifically whether the landing page dependency creates unbounded delay.

---

### Critical Risks

**1. Landing page as unbounded blocker (Severity: High)**

"Once I launch my landing page" is an unscoped dependency. Landing pages expand from "one page" to "design system, copy, hosting, analytics, mobile responsive." If the repo's public launch is gated on the landing page, and the landing page isn't timeboxed, the repo stays private through the entire job search window. The opportunity cost compounds — applications going out right now point to a GitHub profile with one repo.

**2. Root-level debris visible on first visit (Severity: Medium)**

The repo root contains ~14 temporary files: debug scripts, handoff notes, rescue diffs, extracted output files, and a screenshot. These signal "active workbench," not "production artifact." A senior engineer reviewing this repo would read the README, then scroll down and see debug artifacts. The README earns credibility; the file list spends it.

**3. CI badge points to a private repo's Actions tab (Severity: Low-Medium)**

The README has a CI badge linking to GitHub Actions. If Actions history isn't public or the workflow isn't running on the public repo, the badge either shows "no status" or links to a 404. A broken CI badge in the first line of the README undercuts the test count claim immediately.

---

### Weak Assumptions

- **"The landing page needs to exist before the repo goes public."** Unsupported. The README already functions as a landing page. It has architecture diagrams, screenshots, a clear "what this is / who it's for" section, running instructions, and a roadmap. What would the landing page add that the README doesn't already do? If the answer is "a custom domain with better presentation" — that's nice, not blocking. If the answer is "narrative framing for a non-technical audience" — that's a different audience than the people visiting GitHub.

- **"Hiring managers will find the repo organically."** Unsupported. GitHub repos don't get discovered without distribution. The repo being public is necessary but not sufficient. The resume links to it, but that only works when someone is already reading the resume. The value of making it public is defensive (the link works when clicked), not offensive (people find it on their own).

---

### Falsifiers

- **"The README is strong enough to serve as a landing page"**: If 3+ people who represent the target audience (senior eng, hiring PM) read the README and say "I still don't understand what this does or why I should care" — then a landing page is justified as a gate. If they say "this is clear" — the landing page is a nice-to-have.
- **"Root-level cleanup is quick"**: If the cleanup takes more than 2 hours, something structural is wrong with the gitignore or the build process. Time-box it.

---

### Likely Failure Paths

**Path 1 (highest probability):** Landing page scope creeps → takes 2+ weeks → job search continues with single-repo GitHub → applications reference a broken link → the project's proof-point value is zero during peak application volume.

**Path 2:** Repo goes public with debug artifacts → someone reviews it → first impression is "messy build" → README quality doesn't fully compensate → net effect is weaker than waiting would have been.

**Path 3:** Repo goes public, clean, with working CI → no one looks at it → zero impact positive or negative. (Most likely outcome on any given day. The value is cumulative across all applications, not per-visit.)

---

### Interaction Effects

- **Landing page delay + active job search timing**: These interact multiplicatively. Each week the landing page takes is a week of applications going out with a single-repo GitHub profile. The job search doesn't pause while the landing page gets built.

---

### Highest-Leverage Fixes

1. **Decouple repo-public from landing page.** Make them independent workstreams. The repo goes public when it's clean. The landing page ships when it ships. The landing page URL can be added to the README later with a one-line commit.

2. **Root-level cleanup sprint.** Delete or `.gitignore` the ~14 debug/handoff files. This is a 30-minute task that changes the first impression from "active workbench" to "shipped product." Do it before going public.

3. **Verify CI badge renders.** Confirm GitHub Actions workflow runs on the public repo and the badge URL resolves. If Actions aren't enabled for public, either enable them or remove the badge.

4. **Timebox the landing page.** If it matters, scope it to a single page, one weekend, deployed on a static host. If that scope feels too small, the landing page is scope-creeping.

---

### Early Warning Indicators

- If the landing page doesn't have a defined scope and a deployment date within 7 days, it's an unbounded dependency. Treat it as decoupled.
- If root-level cleanup surfaces build issues (files that can't be removed without breaking something), that's a signal the repo isn't actually production-ready — investigate before going public.

---

### Structural Strengths

- The README is above the bar for most open-source projects at any funding level. Architecture diagrams, screenshots, honest capability description, a literature survey citation, clear "who this is for" section.
- 600+ tests across three languages with gate-locked phases. Verifiable — anyone can clone and run the validation suite.
- The code tells the story. The security module, the epistemic schema, the architectural decision records — a reviewer who digs past the README finds more credibility, not less.

---

## Analysis Notes

**What the skill surfaced that a standard review would not have:**

1. The interaction effect between landing page timing and job search cadence. A standard risk list would note "landing page might take a while" and "job search is time-sensitive" as separate risks. The AZIMUTH register linked them as a multiplicative pair — each week of delay during active application volume is compound cost, not additive.

2. The falsifier on "does the landing page need to exist at all." The assumption audit forced an explicit test: what would the landing page add that the README doesn't already provide? For the actual target audience (engineers and hiring PMs visiting GitHub), the answer may be nothing. This reframed the decision from "when to build the landing page" to "whether the landing page is a gate at all."

3. Gotcha #8 (Reversibility Underestimation) applied directly. Making a repo public feels reversible. But first impressions from a messy root directory aren't reversible with the person who already saw it. The asymmetry between "easy to flip the visibility switch" and "hard to undo a bad first impression" is exactly the kind of underestimated irreversibility the gotchas file is designed to catch.

**What the skill correctly did NOT do:**

- Did not pad to fill all sections. The output has no "Base Rate Reality Check" section because there's no meaningful historical base rate for "solo developer open-source launch timing." Omitting it is correct per the output format rules.
- Did not force a binary PROCEED/REJECT. PROCEED WITH SAFEGUARDS is the honest verdict — the asset is strong, the context needs cleanup, and the gates are concrete and achievable.
- Did not produce generic mitigations. "Communicate your timeline" and "monitor closely" would both be slop here. The fixes are structural: decouple, clean, verify, timebox.

**Load condition note:**

The confidence label in this output reads "Medium-High." The canonical AZIMUTH confidence scale is HIGH / MEDIUM / LOW. "Medium-High" is not in the taxonomy. Under full-load conditions, the M10 output format rules (SKILL.md line 611+) enforce the canonical scale. The non-canonical label is consistent with generation under below-boundary conditions (long multi-agent session) where the output format rules did not reach the analysis.

Impact: minor. The effective confidence is approximately MEDIUM, which is what the M10 ceiling would independently enforce — the top assumption ("landing page must precede launch") is UNSUPPORTED, so the ceiling caps at MEDIUM regardless of other evidence quality. The agent arrived at ~MEDIUM through self-assessment rather than the ceiling rule. Direction of deviation is not harmful and the analytical substance is unaffected. This output is documented as-generated; the confidence label deviation is a format artifact of the generation session, not a structural error in the analysis.
