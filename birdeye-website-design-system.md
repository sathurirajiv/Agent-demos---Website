# Birdeye Website Design System

Extracted from the Figma file **"Digital Design System"** (`G557LxMANKcEDihSqYZ4lz`), page **UI Library** (`node-id=1-16`), via the Figma REST API (`Color Primitives`, `Colors`, `Radius Corner`, `Spacing`, `Typography:Desktop`, `Buttons`, `Cards` frames).

Use this as the source of truth when building new UI here or in Cursor — it's the same data behind the "New design" theme in `index.html` (`body.theme-new` CSS rules).

> This is a partial extraction (the frames listed above), not the full file. The Figma token used didn't have `file_variables:read` scope, so if the system also defines Figma Variables (common for things like the Tabs component), those weren't captured — re-pull with a variables-scoped token if you need that layer.

## Fonts

**Geist is the only font on the site** — headings, buttons, nav, body copy, labels, and inputs all use it. This is a site-wide rule (`index.html`'s `body` font-family), not scoped to any one theme or agent — Poppins and Inter have been fully retired.

Google Fonts import used in `index.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

## Color primitives

Raw scales (100–1000, or 0–1000 for black). These are the base palette — nothing else exists (no blue/navy in this system).

| Scale | 100/0 | 200/50 | 300/100 | 400/200 | 500/300 | 600/400 | 700/500 | 800/600 | 900/700 | 1000/800 | 900 | 1000 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **green** | #ebffee | #cff7d3 | #aff4c6 | #85e0a3 | #14ae5c | #009951 | #008043 | #02542d | #024023 | #062d1b | | |
| **red** | #fee9e7 | #fdd3d0 | #fcb3ad | #f4776a | #ec221f | #c00f0c | #900b09 | #690807 | #4d0b0a | #300603 | | |
| **orange** | #fcd7bc | #fbc9a6 | #f8ae79 | #f6934d | #f47820 | #c3601a | #924813 | #62300d | #49240a | #311806 | | |
| **beige** | #f1f0ee | #e6e2e0 | #cdc4c0 | #b4a7a1 | #9b8981 | #826c62 | #68564e | #4d403a | #2e2a28 | #27201d | | #0d0b0a (1000) |
| **black** | #b5b5b5 (0) | #a6a6a6 (50) | #909090 | #727272 | #646464 | #3f3f3f | #212121 | #1a1a1a | #141414 | #0d0d0d | #070707 (900) | #000000 (1000) |
| **white** | #ffffff (all steps 50–1000) | | | | | | | | | | | |

Naming convention: `beige/700` = `#4d403a`, `black/500` = `#212121`, etc. (step / hex).

## Semantic colors

**Background**
- `background/white` → `#ffffff`
- `background/beige` (50) → `#f1f0ee` — page background
- `background/beige-opacity` (60%) → `#eeece7` — card fill, hover surfaces

**Text**
- `text/dark-primary` (500) → `#212121`
- `text/dark-secondary` (300) → `#646464`
- `text/dark-tertiary` (100) → `#909090`
- `text/dark-disabled` (0) → `#b5b5b5`
- `text/white-primary` (1000) → `#ffffff` (and white-secondary/tertiary/disabled also resolve to white — used on dark surfaces)

**Border**
- `border/primary` → `#909090`
- `border/secondary` → `#a6a6a6`
- `border/tertiary` → `#b5b5b5`
- *(in practice, use lighter beige steps — `#e6e2e0` / `#cdc4c0` — for subtle dividers; reserve `#909090`+ for emphasis borders like the feature-card stroke below)*

**Icon** — same scale as Text (dark-primary/secondary/tertiary/disabled, white-*).

**Buttons background**
| Variant | Default | Hovered | Pressed | Disabled |
|---|---|---|---|---|
| dark | `#4d403a` (beige/700) | `#27201d` (beige/900) | `#0d0b0a` (beige/1000) | `#826c62` (beige/500) |
| white | `#ffffff` | `#27201d` | `#0d0b0a` | `#f1f0ee` (beige/50) |
| beige | `#f1f0ee` | `#27201d` | `#0d0b0a` | `#f1f0ee` |

**Status** (from primitives, no dedicated semantic remap found)
- Success → `green/500` `#14ae5c`
- Error → `red/500` `#ec221f`
- Warning → `orange/500` `#f47820`

## Radius scale

| Name | px |
|---|---|
| none | 0 |
| small | 4 |
| medium | 8 |
| x-medium | 12 |
| large | 16 |
| x-large | 20 |
| xl-large | 24 |
| 2x-large | 32 (desktop) / 24 (tablet) / 20 (mobile) |
| 3x-large | 48 / 32 / 24 |
| 4x-large | 60 / 56 / 52 |
| round | 999 (pill) |

> Rule of thumb from the file's own annotation: the corner radius scales with container size; for nested containers, `inner radius = outer radius − padding / 2`, rounded to the nearest step above.

## Spacing scale (desktop / tablet / mobile)

| Name | Desktop | Tablet | Mobile |
|---|---|---|---|
| none | 0 | 0 | 0 |
| 3x-small | 2 | 2 | 2 |
| 2x-small | 4 | 4 | 4 |
| x-small | 8 | 4 | 4 |
| small | 12 | 8 | 8 |
| medium | 16 | 12 | 12 |
| large | 20 | 16 | 12 |
| x-large | 24 | 20 | 16 |
| 2x-large | 28 | 24 | 24 |
| 3x-large | 32 | 32 | 20 |
| 4x-large | 40 | 32 | — |

## Typography scale (desktop, Geist unless noted)

| Style | Size / Line-height | Letter-spacing | Weight |
|---|---|---|---|
| Display | 112 / 120 | −5.6px | 300 |
| Title (H1) | 56 / 60 | −1.12px | 400 |
| Title | 52 / 56 | −1.04px | 400 |
| Title (H2) | 40 / 44 | −0.8px | 400 |
| Title | 38 / 48 | −0.38px | 400 |
| Title | 34 / 40 | −0.34px | 400 |
| Title (H3) | 32 / 32 | −0.96px | 400 |
| Title | 28 / 32 | −0.84px | 400 |
| Title | 24 / 28 | −0.24px | 400 |
| p1 | 18 / 24 | −0.18px | 400 |
| p2 | 16 / 24 | 0 | 400 |
| p3 | 14 / 20 | 0 | 400 |
| p3 (small) | 12 / 20 | 0 | 400 |
| caption / c1 | 21 / 24 | −0.21px | 400 |
| button L | 18 / 20 | 0 | 400 |
| button M | 14 / 20 | −0.14px | 400 |
| button S | 14 / 20 | −0.14px | 400 |
| UPPERCASE (eyebrow) | 16 / 24 | wide (use ~0.08em in CSS) | 400 |

Body copy (paragraphs, form labels, inputs) uses **Geist** at 400 weight, generally 12–14px (previously Inter — see Fonts section above).

## Buttons

- **Shape**: always fully rounded — `border-radius: 999px`.
- **Padding** (left/right/top/bottom, px):
  - large: 30 / 26 / 12 / 12
  - medium: 28 / 24 / 12 / 12
  - small: 24 / 20 / 12 / 12
- **Color variants**: `dark`, `beige`, `white`, `outlined-white`, `outlined-dark` (see Buttons-background table above for fill/hover/pressed).
- **States**: default, focused (adds a `999px`-radius focus ring), hovered, pressed.

## Cards

- Feature/icon card: fill `#eeece7` (beige-opacity), stroke `#646464` @ 1px, radius **24px**.
- Testimonial card: radius 32 (desktop) / 24 (tablet) / 20 (mobile).
- Author block: circular photo (radius 300, i.e. fully round at its size), name `#212121`, role `#727272`.

## Where this is applied

Most of the above (backgrounds, buttons, coworker tabs, footer, full re-skin) is wired up in `index.html` under the `body.theme-new` CSS block (search for "NEW THEME"), toggled via the switcher at the top of the page, and is still scoped to the **Review Response Agent** flow. Two exceptions are now global (see below): **fonts** (Geist everywhere) and the **"selected" state color** (`#4d403a` brown everywhere) apply across every agent regardless of theme.

## Selected-state color (site-wide rule)

Every selectable option — chips, cards, swatches, checkboxes, radio buttons, tabs, dropdown rows — uses the same **beige/700 `#4d403a`** border/fill/text as its "selected" or "active" indicator, with **beige/50 `#f1f0ee`** or the slightly warmer `#f9f8f6` as the selected background tint. This replaced a legacy blue (`#2563eb`) that used to vary by section. When adding a new selectable option anywhere on the site, match this palette rather than introducing a new accent color:

- Border / active indicator: `#4d403a`
- Selected background tint: `#f1f0ee` (or `#f9f8f6` for card-style selections with a soft shadow)
- Selected box-shadow ring (card selections): `0 0 0 3px rgba(77,64,58,0.12)`
- Hover preview (pre-selection): border `#cdc4c0`, text `#4d403a`

Applies to (non-exhaustive): Review Response Agent's response-length options and review-card picker; Review Marketing Agent's layout cards, color swatches, text-alignment buttons, background-image thumbnails, featured-review picker, and channel/content-filter checkboxes; both Ticketing agents' recommendation-type and survey-type cards; the Basic Details form's checklist and dropdown selections; the social calendar/engagement cards and post-length options; and the agent-picker dropdown itself (department nav + agent list selected rows).

## Sticky header agent picker (hover-to-expand)

Once the agent selector scrolls out of view, a minimized copy — coworker avatar + current agent name — animates into the sticky header next to the "Watch Demo" button. Hovering the docked mini pill expands the shared agent dropdown beneath it; scrolling back up reverses the dock.

Implementation notes (`index.html`):
- The mini pill lives in `.header-right`, next to `.btn-schedule` — **not** centered in the header, since the dev-only `#design-toggle` switcher is fixed at the header's exact horizontal center.
- `#agent-dropdown` is a single shared DOM node reparented between the hero pill's anchor and the header pill's anchor (`moveDropdownTo`/`openAgentDropdown`/`closeAgentDropdown` in the JS), so all existing select/search/department logic keeps working unmodified regardless of which pill triggered it.
- Dock/undock on scroll uses an `IntersectionObserver` on `#agent-selector-wrap` (no scroll-position math).
- The header pill opens on hover *and* click; a click never toggles it closed while hover has it open (closing is left to mouse-leave / click-outside), so the two interactions don't fight each other.

---

## Website demo guidelines (`body.theme-new`)

These rules apply to the agent demo page (`index.html`) when **New design** is active. They extend the Figma tokens above for this marketing surface.

### Agent picker

- **Coworker tabs** use a single **pill bar** (`#eeece7`, Jay / Myna / Robin). Each tab shows `{Department} · {N} agents` in `#909090` — no agent name on the tab (that lives in the agent pill below).
- **Selected tab:** white inner pill; subline still shows dept + count only.
- **Clicking a tab** switches to that department’s last-selected agent (does not open a dropdown).
- **Agent pill** below the tab bar opens the **separate shared dropdown** — flat single-column list for the active department (department nav hidden in new theme; tabs handle dept switching).
- **Sticky header:** docked mini agent pill + hover opens the same agent dropdown.

### Typography & labels

- Form labels use **sentence case** (e.g. “Business name”, not “BUSINESS NAME”).
- Label color: `text/dark-secondary` `#646464`, 13px Inter 500.
- Helper / consent / “More options” descriptions: `text/dark-tertiary` `#909090`, 12px.

### Color usage

- **No blue** on this surface — icons, links, focus rings, and chips use black / beige tokens only.
- **Icons** (edit, external link, info): `#212121` default; info tooltips `#909090` with `#cdc4c0` border.
- **Tooltips** (field info, edit, view profile): background `#212121`, text `#ffffff`.
- **Service chips**: fill `#212121`, text `#ffffff`.
- **Dropdowns / inputs**: border `#e6e2e0`; focus border `#4d403a` with `rgba(77,64,58,0.12)` ring.

### Buttons

- **Primary** (Continue, Generate, Watch Demo header CTA): `buttons/dark` — fill `#4d403a`, hover `#27201d`, pill radius.
- **Secondary** (Save on edit cards, Copy Response, Regenerate): beige fill `#f1f0ee`, border `#e6e2e0`, hover `#eeece7`, pill radius, Geist 14px. On white surfaces, secondary actions use the beige variant (not outlined).
- **Edit** (icon-only): no fill; icon stroke `#212121`; black tooltip on hover.

**CTA placement on this demo**
| Action | Variant | Notes |
|---|---|---|
| Continue | Primary dark | `#4d403a` |
| Generate Response / Create Ticket | Primary dark | First-run generation |
| Regenerate | Secondary beige | Left-aligned refresh icon + label, flex-aligned |
| Copy Response | Secondary beige | Footer of AI-generated response card |
| Watch Demo (header) | Primary dark | Same `#4d403a` as Continue |

### Checkboxes

- Unchecked: border `#d1d5db` (classic) / `#e6e2e0` (new theme inputs).
- **Checked (new theme):** fill and border `#4d403a` (same as primary CTA dark), white checkmark.
- Applies to `.ao-checkbox` and `.dd-check-box`.

### Header & branding

- **Birdeye logo** in new theme: fully black — `filter: brightness(0)` on `.logo-icon`, wordmark `#212121`.
- **Coworker avatars:** local wooden bird logos in `assets/coworker-jay.png`, `coworker-myna.png`, `coworker-robin.png` (44×44 circle, white border).

### Coworker tabs

- Every tab: `{Department} · {N}` in `#909090` (e.g. `Marketing · 7`). Agent name is **not** on the tab.
- **Unavailable departments** (no enabled agents, e.g. Myna/Operations): tab does not switch or open the dropdown; hover shows `Want to experience {Name}-specific agents? Contact Sales.`
- **Disabled agents** in the dropdown: no “Coming soon” label; hover shows `Want to experience this agent? Contact Sales.`

### Footer (new design only)

- Classic footer, “Learn why Birdeye”, and competition/G2/Capterra block are hidden (`classic-only`).
- **New footer** (`#new-footer`): beige page background `#f1f0ee`, VIEW 2026 navy banner (`#1a2332`), BirdAI / Jay / Myna / Robin link columns, Industries/Tools/Resources/Company row, social + app badges, legal links row.
- Toggle **New design** to preview.

### Accordions

- **Closed:** show section title + subtitle only (e.g. “Basic details” + “Business details and agent preferences”). Body content must not bleed through — collapsed bodies use `max-height: 0`, `padding: 0`, `border-top: none`, and `overflow: hidden` (the new theme must not apply open-state padding while collapsed).
- **Open:** full panel with form content, top separator, and horizontal padding.

### Consent copy (User details)

- “By continuing, you agree to…” — `#909090` body text; linked Privacy Policy / Terms — `#646464` with underline.
