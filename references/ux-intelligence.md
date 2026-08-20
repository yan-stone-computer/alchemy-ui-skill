# UX Intelligence: priority rules, accessibility, and the pre-delivery bar

Read this for `critique`, `audit`, `harden`, `onboard`, and `adapt` work, and as the UX backbone of every build. Distilled from the ui-ux-pro-max rule database (which also ships its own searchable data; when that skill is installed in the same harness, prefer its `search.py` queries over the defaults below and label any fallback as such).

## Priority categories

Follow priority 1 -> 10; the earlier categories dominate:

| # | Category | Key checks (must have) | Anti-patterns (avoid) |
|---|---|---|---|
| 1 | Accessibility | Contrast 4.5:1, alt text, keyboard nav, ARIA labels | Removing focus rings, icon-only buttons without labels |
| 2 | Touch & interaction | Min size 44x44px, 8px+ spacing, loading feedback | Hover-only interactions, instant 0ms state changes |
| 3 | Performance | WebP/AVIF, lazy loading, reserved space (CLS < 0.1) | Layout thrashing, cumulative layout shift |
| 4 | Style selection | Match product type, consistency, SVG icons (no emoji) | Mixing flat and skeuomorphic randomly, emoji as icons |
| 5 | Layout & responsive | Mobile-first breakpoints, viewport meta, no horizontal scroll | Fixed px container widths, disabled zoom |
| 6 | Typography & color | Base 16px, line-height 1.5, semantic color tokens | Body text < 12px, gray-on-gray, raw hex in components |
| 7 | Animation | Context-aware timing, motion conveys meaning, spatial continuity | One duration for everything, animating width/height, no reduced-motion |
| 8 | Forms & feedback | Visible labels, error near field, helper text, progressive disclosure | Placeholder-only labels, errors only at top, overwhelming upfront |
| 9 | Navigation | Predictable back, bottom nav <= 5, deep linking | Overloaded nav, broken back behavior, no deep links |
| 10 | Charts & data | Legends, tooltips, accessible colors | Relying on color alone to convey meaning |

## High-leverage UX rules

Accessibility:

- Search one observable outcome at a time ("error summary validation", "decorative icon aria hidden", "icon button accessible label"). Do not accept a generic accessibility result for a specific interaction or WCAG criterion.
- Focus must never be obscured; visible focus rings stay on all interactive elements; never remove them.
- Dragging must never be the only way to act; provide a non-drag alternative.
- Dark mode must keep hierarchy parity: if a CTA pops in light, it pops in dark; brand color stays recognizable; no pure black or pure white.

Interaction:

- Loading feedback: skeletons matching final layout shapes beat generic spinners.
- Every interactive element needs the full state cycle: default, hover, active, focus, disabled.
- Tactile feedback on press (`scale(0.97)` / `-translate-y-[1px]`).
- No instant 0ms state changes; 100-200ms is the responsiveness sweet spot; repeated actions (100+/day) get no animation.

Forms:

- Label ABOVE input; helper text present in markup; error text BELOW input.
- No placeholder-as-label, ever.
- Error summary near the submit control plus inline errors; errors name the problem and the recovery.
- Every form element passes WCAG AA contrast against the section background (inputs, placeholders, focus rings, helper text, error text).

Layout & navigation:

- Mobile-first breakpoints (sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1536); explicit per-section collapse under 768px; never `h-screen` (use `min-h-[100dvh]`). <!-- ui-alchemy: ignore -->
- Bottom navigation max 5 items; predictable back behavior; deep-linkable states.
- Navigation renders on one line at desktop, height max 80px (default 64-72px).
- Buttons: label fits one line at desktop (max 3 words for primary CTAs), text readable against background (WCAG AA 4.5:1 body / 3:1 large), one label per intent across the whole page.

Content & data:

- Long lists (> 5 items) get a different UI component: 2-column split, card grid, tabs/accordion, scroll-snap pills, carousel, marquee. Never the default `<ul>` with a hairline under every row.
- No fake-precise numbers unless they come from real data or are explicitly labeled mock.
- Charts: legends, tooltips, and never color alone; consider patterns/labels in addition to hue.

## Query contract (when searching local guidance)

Choose the smallest search mode that fits: design-system for new project/page direction; one explicit domain for a targeted concern; stack for implementation specifics. Build queries around one dominant intent with 2-3 meaningful terms plus one useful constraint. Verify the result's category and fit before applying; retry once narrower; if still empty, state that no verified match exists and label general guidance as fallback. Never persist unverified output.

Useful domain queries: `"error summary validation"` (ux), `"decorative icon aria hidden"` (icons), `"keyboard focus modal"` (ux), `"virtualize lists"` (ux), `"suspense streaming bundle"` (nextjs), `"rerender memo list"` (react), `"glassmorphism dark"` (style), `"entertainment vibrant"` (color), `"playful modern"` (typography), `"real-time dashboard"` (chart), `"hero social-proof"` (landing), `"scroll reveal stagger"` (gsap).

## Pre-delivery checklist (app UI)

For native/mobile app UI (iOS / Android / React Native / Flutter) additionally verify: icon/visual-element discipline, touch feedback, light/dark contrast, safe-area layout (notches and gesture bars), and full keyboard/screen-reader support. Safe areas: use `env(safe-area-inset-*)` on web, SafeAreaView/system insets on native; never let interactive content sit under the gesture bar.
