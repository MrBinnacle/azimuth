---
name: AZIMUTH
description: Decision-quality pressure-testing skill for Claude Code and Claude.ai
colors:
  bearing-gold: "#C9A84C"
  bearing-gold-dim: "#9C8040"
  instrument-black: "#0C0C0E"
  surface-raised: "#141417"
  surface-elevated: "#1C1C21"
  border-dim: "#252529"
  border: "#343438"
  field-white: "#E2E2EA"
  dim-reading: "#7A7A8A"
  muted-reading: "#4A4A5A"
  verdict-proceed: "#5CAE72"
  verdict-proceed-soft: "#7EC4A0"
  verdict-pilot: "#C9A84C"
  verdict-reject: "#C45C5C"
  verdict-delay: "#8888B0"
typography:
  display:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: "clamp(48px, 9vw, 80px)"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: "clamp(28px, 4vw, 38px)"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "-0.015em"
  body:
    fontFamily: "'IBM Plex Sans', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  body-light:
    fontFamily: "'IBM Plex Sans', system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 300
    lineHeight: 1.75
  label:
    fontFamily: "'IBM Plex Mono', 'Courier New', monospace"
    fontSize: "11px"
    fontWeight: 400
    letterSpacing: "0.14em"
  code:
    fontFamily: "'IBM Plex Mono', 'Courier New', monospace"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.75
rounded:
  sm: "4px"
  md: "6px"
  lg: "8px"
spacing:
  sm: "12px"
  md: "20px"
  lg: "30px"
  xl: "48px"
  section: "80px"
components:
  install-block:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.field-white}"
    rounded: "{rounded.md}"
    padding: "0"
  copy-button:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.field-white}"
    rounded: "0"
    padding: "0 18px"
  capability-card:
    backgroundColor: "{colors.instrument-black}"
    textColor: "{colors.dim-reading}"
    rounded: "0"
    padding: "{spacing.lg}"
  capability-card-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.dim-reading}"
    rounded: "0"
    padding: "{spacing.lg}"
  invoke-line:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.dim-reading}"
    rounded: "{rounded.md}"
    padding: "14px 20px"
  invoke-line-hover:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.dim-reading}"
    rounded: "{rounded.md}"
    padding: "14px 20px"
  verdict-badge:
    backgroundColor: "transparent"
    textColor: "{colors.verdict-pilot}"
    rounded: "{rounded.sm}"
    padding: "3px 10px"
---

# Design System: AZIMUTH

## 1. Overview

**Creative North Star: "The Instrument"**

An azimuth is the navigational bearing you lock in before you step off. This design system is that instrument: precise, legible, zero flourish that is not functional. Every element is either a reading (verdict, assessment, failure path) or an action (install, invoke). Nothing exists to reassure or decorate.

The aesthetic is dark because instruments are read in demanding conditions — in the field, late at night, under pressure. The gold is not a brand accent; it is the marking that shows you the bearing. It appears on the elements that carry direction: labels, verdicts, accent lines, the wordmark. Its rarity is the point.

Typography carries the cognitive register. Instrument Serif is the editorial intelligence layer — used for headlines and the wordmark because it signals serious thinking without academic distance. IBM Plex (both Sans and Mono) is the operational layer — the surface where readings are made and commands are entered. The pairing produces a system that reads as precision work, not software.

**Key Characteristics:**
- Dark, instrument-grade surface — not consumer dark mode, not developer terminal
- Gold as bearing marker, not brand paint
- Serif editorial display paired with mono operational body
- Flat depth through tonal surface layering, no shadows
- Grid texture as environmental signal, not decoration
- Verdicts color-coded by category: green (proceed), amber (conditional), red (reject), slate (defer)

## 2. Colors: The Bearing Palette

One dominant accent used with discipline. Everything else is tonal neutral.

### Primary
- **Bearing Gold** (`#C9A84C`): The direction marker. Used on labels, eyebrows, accent lines, the wordmark, active command prompts, and verdict highlights. Never used as a fill on large surfaces. Rarity is the signal.
- **Bearing Gold Dim** (`#9C8040`): The receded bearing — used for secondary accent elements, terminal number labels, and the dimmed state of gold-adjacent UI. Reads as gold under shadow. Lifted from #7A6430 to clear WCAG AA (4.5:1) on both `#0C0C0E` and `#08080A` surfaces; the token sees body-text use on `.t-num`.

### Neutral (surfaces, text, borders)
- **Instrument Black** (`#0C0C0E`): The base chassis — page background and the default state of all capability cards. A near-black with a barely-visible cool undertone; never pure `#000`.
- **Surface Raised** (`#141417`): First level of tonal lift — used for the terminal interior, install block, and nav background.
- **Surface Elevated** (`#1C1C21`): Second level — used for the copy button and secondary card hover states.
- **Border Dim** (`#252529`): The hairline boundary between sections and the default card border.
- **Border** (`#343438`): The slightly-brighter border used on interactive elements (install block, invoke lines) to signal affordance.
- **Field White** (`#E2E2EA`): Primary text. A cool off-white — never pure `#fff`. Readable on all dark surfaces.
- **Dim Reading** (`#7A7A8A`): Secondary text — body copy in hero and problem sections, card descriptions, nav links at rest. Most of the human-written copy lives here.
- **Muted Reading** (`#4A4A5A`): Tertiary text — placeholder, suppressed state, install note.

### Semantic (verdicts only)
- **Proceed** (`#5CAE72`): PROCEED verdict — positive confirmation
- **Proceed Soft** (`#7EC4A0`): PROCEED WITH SAFEGUARDS — muted green
- **Pilot** (`#C9A84C`): PILOT FIRST — same as Bearing Gold; conditional action
- **Reject** (`#C45C5C`): REJECT — the hard stop
- **Delay** (`#8888B0`): DELAY / INSUFFICIENT SIGNAL — cool slate, neither positive nor negative

**The One Voice Rule.** Bearing Gold appears on at most one semantic role per screen. If it's doing label work, do not also use it as a large-surface fill. Its authority comes from restraint.

**The No-Pure-Black Rule.** `#000000` and `#ffffff` are prohibited. The background is `#0C0C0E`; the text is `#E2E2EA`. Every neutral carries a faint cool tint toward the bearing gold's complement — the instrument shows its material even in neutral states.

## 3. Typography

**Display Font:** Instrument Serif (Google Fonts) — with Georgia, serif fallback  
**Body Font:** IBM Plex Sans (Google Fonts) — with system-ui, sans-serif fallback  
**Label / Code Font:** IBM Plex Mono (Google Fonts) — with Courier New, monospace fallback

**Character:** Instrument Serif carries editorial authority without academic distance — used only for structural signal (wordmark, section headings, the hero statement). IBM Plex is the operational register: clinical, spacious, good at reading under pressure. The mono variant handles all command-surface typography (labels, eyebrows, code, copy buttons). Never use Instrument Serif for body copy; never use sans for labels or commands.

### Hierarchy
- **Display** (400, `clamp(48px, 9vw, 80px)`, line-height 1.12, -0.02em tracking): Hero headlines only. One per page.
- **Headline** (400, `clamp(28px, 4vw, 38px)`, line-height 1.12, -0.015em tracking): Section headings in Instrument Serif. Used for h2 throughout.
- **Body Light** (IBM Plex Sans 300, 18px, line-height 1.75): Long-form explanatory copy — problem section, hero subtitle. Maximum width 620px.
- **Body** (IBM Plex Sans 400, 16px, line-height 1.6): Standard running text. Maximum 65–75ch per line.
- **Label** (IBM Plex Mono 400, 11px, letter-spacing 0.14em, UPPERCASE): Eyebrows, section labels, capability card numbers, table headers. Gold only.
- **Code / Command** (IBM Plex Mono 400–500, 13–14px, line-height 1.75): Terminal content, install commands, invoke lines, footer links.

**The Serif-for-Signal Rule.** Instrument Serif is used exclusively for elements that announce structure: the wordmark, page headings, and the hero statement. The moment a serif element appears at small sizes or in running copy, the editorial register collapses into decoration. Restrict it.

**The Mono-for-Operational Rule.** All command-surface elements — labels, eyebrows, code blocks, table headers, copy buttons, nav links, install instructions — use IBM Plex Mono. The monospace treatment signals that this is a tool, not a narrative.

## 4. Elevation

Flat by default. Depth is conveyed through tonal surface layering (Instrument Black → Surface Raised → Surface Elevated), border color graduation (Border Dim → Border), and content density — not shadows.

No `box-shadow` values are used anywhere in the system. The grid texture overlay (a very faint bearing-gold grid at 2.5% opacity, 56px pitch) provides environmental signal — a sense of being inside an instrument — without adding visual weight to individual elements.

**The Flat-by-Default Rule.** Surfaces are flat at rest. Interactive affordance is signaled through border brightness (hover lifts border color from `#252529` to `#343438`) and background shift (hover moves one step up the tonal surface scale). Never add a shadow to create perceived importance; earn importance through content.

## 5. Components

### Install Block (Signature Primary CTA)
The install command — the primary action on the page. Functionally styled, not hero-treated.
- **Container:** `background: #141417`, `border: 1px solid #343438`, `border-radius: 7px`, `overflow: hidden`, no padding on the outer container
- **Command text:** IBM Plex Mono 14px, `#E2E2EA`, `padding: 13px 22px`. The `$` prompt is Bearing Gold; user-select none.
- **Copy button:** `background: #1C1C21`, `border-left: 1px solid #252529`, `color: #E2E2EA`, IBM Plex Mono 11px uppercase, `padding: 0 18px`, `min-height: 44px`. Hover: `background: #343438`. Copied state: text color `#5CAE72`.
- No glow, no primary-color fill, no "Get Started" energy. The command is the CTA.

### Capability Card
The six-cell grid in the "What you get" section. Uses a 1px gap / shared-border technique — the grid background is `--border`, cells are `--bg`. Gap is the border.
- **Cell:** `background: #0C0C0E`, `padding: 30px`. Hover: `background: #141417`, transition 0.15s.
- **Number label:** IBM Plex Mono 10px, Bearing Gold, letter-spacing 0.14em, uppercase, `margin-bottom: 12px`
- **Heading:** Instrument Serif 15px, `#E2E2EA`, `margin-bottom: 10px`
- **Body:** IBM Plex Sans 14px, `#7A7A8A`, line-height 1.65
- Cards have no border-radius. The outer container has `border-radius: 8px; overflow: hidden` to clip corners.

### Invoke Line
The `/azimuth [decision]` example rows in the Quick Start section.
- `background: #141417`, `border: 1px solid #252529`, `border-radius: 6px`, `padding: 14px 20px`
- IBM Plex Mono 14px, `#7A7A8A`. The slash command prefix is Bearing Gold.
- Hover: `border-color: #9C8040` (Bearing Gold Dim), `background: #1C1C21`, transition 0.15s

### Verdict Badge (Table)
Color-coded by verdict category. Font-only treatment — no background fill.
- IBM Plex Mono 12px, font-weight 500, `white-space: nowrap`
- Colors: Proceed `#5CAE72`, Proceed-Soft `#7EC4A0`, Pilot `#C9A84C`, Reject `#C45C5C`, Delay/Null `#8888B0`, Register `#5C7EC4`
- The table itself uses `border-radius: 8px; overflow: hidden` on the wrapper. Row hover: `background: #141417`.

### Terminal Block
The example output display. Should read as a real terminal output, not a designed mockup.
- `background: #08080A` (slightly deeper than instrument-black), `border: 1px solid #252529`, `border-radius: 8px`
- Title bar: `background: #141417`, `border-bottom: 1px solid #252529`, three decorative dots in `#2A2A30` (no red/yellow/green)
- Body: IBM Plex Mono 13px, line-height 1.75, base text `#8888A0`
- Section headings inside terminal: Bearing Gold, font-weight 500
- Verdict text: `#C9A84C` for the decision verdict; `#DDDDE8` for supporting text; `#7EC4A0` for falsifiers and confidence

### Navigation
- `border-bottom: 1px solid #252529`, height 60px
- Logo: Instrument Serif 14px, letter-spacing 0.22em, Bearing Gold, uppercase
- Links: IBM Plex Mono 12px, `#7A7A8A`, letter-spacing 0.04em. Hover: `#E2E2EA`. No active state indicator beyond color.
- Focus-visible: `outline: 2px solid #C9A84C; outline-offset: 3px; border-radius: 2px`

### Signal List
The "How to know it's working" list. Styled as structured instrument readings.
- `border: 1px solid #252529; border-radius: 8px; overflow: hidden; list-style: none`
- Each item: `padding: 22px 28px`, `border-bottom: 1px solid #252529`
- `::before` marker: an em-dash (`—`) in Bearing Gold, IBM Plex Mono 13px, flex-shrink 0
- Hover: `background: #141417`. Item text: IBM Plex Sans 15px, `#7A7A8A`

## 6. Do's and Don'ts

### Do:
- **Do** use Bearing Gold exclusively on small, high-signal elements — labels, eyebrows, command prompts, markers. Its rarity creates its authority.
- **Do** use tonal surface layering (Instrument Black → Surface Raised → Surface Elevated) for all depth and interactive hover states.
- **Do** use Instrument Serif for section headings and the wordmark only. Serif at 15px or smaller is decoration, not signal.
- **Do** let verdicts carry their semantic color without additional treatment — the color *is* the verdict status.
- **Do** keep body text at `#7A7A8A` (Dim Reading). High-contrast white is reserved for headings and critical reading content.
- **Do** use `min-height: 44px` on all interactive targets. Instrument precision applies to touch targets too.
- **Do** include `prefers-reduced-motion` overrides on every transition. The system is used under pressure; motion must not be mandatory.
- **Do** lead with the verdict. The finding is the first sentence. Evidence follows.

### Don't:
- **Don't** use a `border-left` or `border-right` greater than 1px as a colored accent stripe on cards, callouts, or list items. This is the consulting-deliverable pattern — it reads as McKinsey-lite callout formatting and violates the instrument register.
- **Don't** use white/purple gradients, `background-clip: text` gradient text, or glowing card borders. These are the SaaS-cream AI tool signature — the system already rejected them through its dark palette, but they must never re-enter via copy or component updates.
- **Don't** use all-green-terminal styling. The terminal block uses `#08080A` base with muted blue-grey text. Developer-terminal green (`#00ff00` family) contradicts the precision instrument register.
- **Don't** use framework-in-a-box visual patterns: identical card grids with icon + heading + text repeated without variation, hero-metric templates (big number + small label + gradient accent), or modal-first interaction design.
- **Don't** write copy that reassures. "Unlock your potential," "supercharge your workflow," "AI-powered" — these phrases belong to anti-reference #1. The copy states what the tool does. It does not predict how the user will feel about it.
- **Don't** soften a verdict in copy. If the system says REJECT, the supporting copy explains the structural reason. It does not add "of course, you know your situation best."
- **Don't** use `#000000` or `#ffffff`. The system's darkest value is `#08080A` (terminal) and its lightest is `#E2E2EA` (field white).
- **Don't** add borders, backgrounds, or typographic emphasis to callout text without first asking whether a simpler treatment (larger type, Instrument Serif, a different weight) could carry the same signal.
