# Interface Craft: hierarchy, type, tokens, and the "decided" look

Read this before committing to a direction and before writing any component. This is the craft-first discipline of interface-design: Linear, Vercel, Stripe, Apple quality is not talent; it is a hundred decided details.

## Intent first

Before touching code, answer three questions and keep the answers in a compact working brief:

- **Who is this human?** Not "users". The actual person, where they are, what they did 5 minutes ago and will do 5 minutes after.
- **What must they accomplish?** The verb. Grade these submissions. Find the broken deployment. Approve the payment. The answer determines what leads, what follows, what hides.
- **What should this feel like?** In words that mean something. "Clean and modern" means nothing. Warm like a notebook? Cold like a terminal? Dense like a trading floor?

Intent must be systemic: if the intent is warm, surfaces, text, borders, accents, semantic colors, and type are all warm. For every choice you must be able to say why. "It's common" means you defaulted.

## The problem with defaults

You will generate generic output. Your training has seen thousands of dashboards; the patterns are strong, and process alone does not fix that. The bar: if another AI given a similar prompt would produce substantially the same output, you have failed. Different not for its own sake, but because the interface emerged from this user, this task, this world.

Defaults hide in the parts that "just need to work": typography is the design, navigation is the product, data is meaning, token names are worldbuilding. There are no structural decisions; everything is design.

## Visual hierarchy and composition

- **One focal point per view.** Name it out loud, then make it win through size, contrast, position, or surrounding whitespace. Demote everything else deliberately.
- **Type scale is a ratio, and weight beats size.** ~1.2 (dense/calm), ~1.25 (most product UI), ~1.333 (expressive). From a 14-16px body that yields visibly distinct steps. The Apple/Linear move: one 14px size holds three tiers through weight + opacity (`value: 600/primary`, `label: 500/secondary`, `meta: 400/muted`). Build from all three levers, never size alone.
- **Density is a decision, expressed in px.** A tool panel at 12-16px padding feels workbench-tight; the same card at 24px feels like a brochure. Pick deliberately, then hold it.
- **Breathe unevenly.** Dense control zones give way to open content; vary rhythm on purpose. Monotone layouts (same card, same gap, same density everywhere) are the sound of no one deciding.
- **Proportions speak.** A 280px sidebar says "navigation serves content"; a 360px sidebar says "these are peers". Choose widths that state a relationship.
- **Distribution and restraint.** ~60/30/10: dominant neutral surface, secondary tone, ~10% accent. One accent used with intention beats five colors used without thought. Reach for whitespace and tonal shift before borders and dividers. Optical sizing on large type: tighten letter-spacing as type grows, loosen line-height on body (~1.5).

## Craft foundations

- **Subtle layering is the backbone.** Numbered surface elevation (dark base -> +7% -> +9% -> +12%; light adds shadow instead). Sidebars share the canvas background; popovers sit one level above their parent; inputs are slightly DARKER than surroundings (inset, they receive content).
- **Borders disappear unless you need them.** Low-opacity rgba (`rgba(255,255,255,0.06-0.12)` dark, slightly higher light), a progression from standard to emphasis to focus-ring, matched to boundary importance.
- **The squint test:** blur your eyes; hierarchy should remain readable and nothing should jump out.
- **Infinite expression:** a metric display can be a hero number, inline stat, sparkline, gauge, progress bar, comparison delta, or trend badge. No two interfaces should look the same; before building ask what the ONE thing users do here is, and which product solves a similar problem brilliantly.
- **Color lives somewhere.** Every product exists in a world; the palette should feel like it came FROM somewhere, not applied TO something.

## Before writing each component (mandatory checkpoint)

State, and be able to justify:

```
Intent:     [who is this human, what must they do, how should it feel]
Hierarchy:  [the focal element, and how it wins]
Palette:    [colors from your exploration, and WHY they fit this world]
Depth:      [borders / subtle shadows / layered, and WHY]
Surfaces:   [your elevation scale, and WHY this temperature]
Typography: [typeface + size/weight/color levers, and WHY]
Spacing:    [base unit + chosen density]
```

If you cannot explain WHY for each, you are defaulting: stop and think.

## Use what exists

The most common way AI degrades a codebase is hand-rolling what already exists.

Controls: native -> primitive -> hand-roll.

1. Native HTML first (`<button>`, `<a>`, `<input>`, `<dialog>`, `<details>`). Never `<div onClick>` what the platform provides.
2. A battle-tested headless primitive for anything stateful and hard: select, combobox, dialog, popover, tooltip, tabs, date picker (Radix UI, React Aria, Ark, Headless UI, Vaul, `cmdk`). Then style it to your direction.
3. Hand-roll only as a genuine last resort, and then you owe the complete behavior contract: keyboard nav, focus trap/return, ARIA roles and state, click-outside, scroll-lock.

Styling: system -> component -> token -> utility.

1. If the project has a design system, use it (shadcn/`Button`, CVA variants, theme, component library) before writing a one-off.
2. When a styled element repeats, extract a component (on the second real reuse).
3. Bind to semantic tokens, not hardcoded literals: `bg-card border-border text-muted-foreground`, not `bg-white border-gray-200`.
4. Inline utilities are for genuine one-offs; the same long className sprayed everywhere is a missing component or token.

## Design system essentials

- **Token architecture.** Every color traces to primitives: foreground, background/surface, border, brand, semantic (destructive/warning/success). No random hex.
- **Text hierarchy: four levels.** Primary, secondary, tertiary, muted. Two levels means the hierarchy is too flat.
- **Spacing.** A base unit (4 or 8px), multiples only; scaled by context (micro, component, section, major). Random values signal no system.
- **Padding.** Symmetrical unless content genuinely demands asymmetry.
- **Depth: choose ONE and commit.** Borders-only (clean, technical) / subtle shadows (approachable) / layered shadows (premium) / surface-color shifts. Never mix.
- **Border radius is a scale.** Small for inputs/buttons, medium for cards, large for modals. Never mix sharp and soft randomly.
- **Control tokens.** Inputs, selects, checkboxes get dedicated background/border/focus tokens, not surface tokens, so you can tune them independently.
- **Dark mode.** Shadows are weak on dark: lean on borders. Desaturate semantic colors slightly. Same hierarchy, inverted values; keep one hue, shift only lightness.

## Polish and motion essentials

Static polish:

- **Concentric radius:** `outerRadius = innerRadius + padding`. Same radius on parent and child is the most common "off" feeling.
- **Tabular numbers** (`font-variant-numeric: tabular-nums`) on any dynamic number.
- **Optical alignment:** icon-side padding != text-side (nudge ~2px); play triangles nudge right.
- **States are not optional:** default, hover, active, focus, disabled; data needs loading, empty, error.
- **Hit areas:** 44x44px (WCAG), 40 minimum. Extend small controls with a pseudo-element; never overlap hit areas.
- **Shadows over borders for elevation.** Layered transparent box-shadow (`0 0 0 1px rgba(0,0,0,.06), 0 1px 2px -1px rgba(0,0,0,.06), 0 2px 4px rgba(0,0,0,.04)`); dark mode collapses to a single ring.
- **Text wrapping:** `text-wrap: balance` on headings, `text-wrap: pretty` on body.
- **Font smoothing** (`-webkit-font-smoothing: antialiased`) on root; 1px inset outlines on images with pure rgba, never tinted near-black/white.

Motion:

- **Should it animate at all?** Actions repeated 100+ times/day get none; occasional surfaces get standard; rare/first-run moments may delight.
- **Duration < 300ms** for UI: button press 100-160ms, tooltips/popovers 125-200ms, dropdowns 150-250ms, modals/drawers 200-300ms.
- **Custom ease-out, never ease-in.** `cubic-bezier(0.23, 1, 0.32, 1)` for entering; `cubic-bezier(0.77, 0, 0.175, 1)` for on-screen movement.
- **Press feedback** `transform: scale(0.97)` on `:active`, never below 0.95.
- **Never animate from `scale(0)`**; start at `scale(0.95)` + `opacity: 0`. Popovers scale from their trigger origin.
- **Only animate `transform` and `opacity`.** Never `transition: all`. <!-- ui-alchemy: ignore -->
- **Stagger entrances 30-60ms**; exits faster and subtler than enters. Respect `prefers-reduced-motion`.

## Avoid

Harsh borders, dramatic surface jumps, flat hierarchy, monotone layout, inconsistent spacing, mixed depth strategies, missing states, dramatic drop shadows, large radius on small elements, thick decorative borders, gradients/color for decoration, multiple accent colors, different hues across surfaces, default typography, structural hacks (negative margins undoing parent padding, escape-hatch calc, absolute positioning to dodge layout).

## The checks before showing

- **Swap test:** swap your typeface for the usual one, your layout for a standard template. If nothing would feel different, you defaulted.
- **Squint test:** hierarchy still readable, nothing jumping out harshly.
- **Signature test:** point to five specific elements where your signature appears. "The overall feel" does not count.
- **Token test:** read your CSS variables aloud. Do they belong to this product's world, or any project?

## Persistence

At the end of a task, offer to save to `.ui-alchemy/system.md`: direction and feel, depth strategy and spacing base, hierarchy decisions (type scale ratio, density values, focal pattern), and reusable component patterns with measurements (e.g. `Button primary - 36px h / 12px 16px pad / 6px radius / 14px 500`). Future sessions read it first and hold to it.
