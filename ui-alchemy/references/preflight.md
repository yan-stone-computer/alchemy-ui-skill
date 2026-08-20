# Final Pre-Flight: run every box before declaring done

This is the last filter, executed inside Phase 4 of the advanced workflow (see [final-review.md](final-review.md)). If any box cannot be honestly ticked, the output is not done. The mechanical subset is automated by `scripts/preflight_check.py`; run it and then reason through the rest.

## Automated (run the scanner)

```bash
python <skill-dir>/scripts/preflight_check.py <target-path> [--platform h5|miniapp|app] [--json]
```

The scanner checks: em-dash and en-dash-as-separator bans, pure `#000000`/`#ffffff`, `h-screen` usage, `transition: all`, `window.addEventListener("scroll")`, `<div onClick>` (and `<div onMouseEnter>` click-alikes), `bg-white` + `text-white` same element, `font-family: Inter` defaults, missing `alt` on `<img>`, eyebrow micro-label density, and `<img>` without width/height attributes. Findings are advisory: a flagged file with an explicit comment override is acceptable; the agent decides. <!-- ui-alchemy: ignore -->

Platform-aware checks (pass `--platform`):

- `--platform h5`: missing viewport meta (hard), `user-scalable=no` / `maximum-scale=1` zoom lock (hard).
- `--platform miniapp`: `<image>` without explicit `mode` (soft), `<view bindtap>` without button semantics or feedback (soft).
- `--platform app`: no automated checks; use the manual checklist in [platforms/app.md](platforms/app.md).

## Manual checks

- [ ] Design Read declared as a one-liner (page kind, audience, vibe, design system/aesthetic).
- [ ] Dials explicit and reasoned from the brief, not silently baseline.
- [ ] Design system chosen from the map, or aesthetic labeled honestly (no official package passed off as one).
- [ ] Redesign mode detected and audit performed (if applicable).
- [ ] ZERO em-dashes anywhere visible; zero en-dash separators.
- [ ] Page theme locked: one theme (light, dark, or auto) for the whole page; no mid-page inversion unless deliberate.
- [ ] Color consistency lock: one accent used identically across all sections.
- [ ] Shape consistency lock: one corner-radius system, consistently applied.
- [ ] Button contrast: every CTA readable against its background (WCAG AA 4.5:1 / 3:1 large); no wrapped CTA labels at desktop; one label per intent.
- [ ] Form contrast: inputs, placeholders, focus rings, labels, errors all pass WCAG AA.
- [ ] Serif discipline: serif only with brand justification; not Fraunces/Instrument_Serif by default; different serif from the previous project.
- [ ] Premium-consumer palette is not the banned beige+brass+oxblood+espresso family; different family from the previous premium project.
- [ ] Italic display words with descenders (`y g j p q`) have `leading-[1.1]` minimum + reserve.
- [ ] Hero fits the initial viewport: headline <= 2 lines, subtext <= 20 words and <= 4 lines, CTAs visible without scroll, top padding <= `pt-24`, max 4 text elements, no taglines/trust strips in hero.
- [ ] Eyebrow count <= ceil(sectionCount / 3), mechanically counted (`uppercase tracking`).
- [ ] No split-header default; no zigzag beyond 2 consecutive image+text splits; no marquee beyond once.
- [ ] Logo wall: below the hero, logos only, real SVG marks, no text wordmarks.
- [ ] Bento has rhythm, exact cell count (N items -> N cells), and 2-3 cells with real visual variation.
- [ ] Long lists (> 5 items) use a fitting component, not a hairline-per-row list.
- [ ] Real images used (gen tool first, then seed-based placeholders, then explicit placeholder slots); no div-based fake screenshots, no hand-rolled decorative SVGs, no pure-text "minimalism".
- [ ] No pills overlaid on images, no photo-credit captions as decoration, no version footers, no scroll cues, no locale/weather strips, no decoration text strips, no section-number eyebrows, no decorative dots.
- [ ] Copy self-audit done: no grammatically broken, hallucinated, or fake-precise content; one register per page.
- [ ] Motion motivated (hierarchy / storytelling / feedback / state transition); no GSAP-for-show; motion claimed = motion shown; reduced motion respected.
- [ ] Navigation on one line at desktop, height <= 80px.
- [ ] Section-layout families varied: at least 4 different families across 8 sections.
- [ ] Performance plausibly meets Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1); images sized; lazy loading; no scroll listeners.
- [ ] States complete: hover/active/focus/disabled, loading/empty/error; hit areas >= 40px (44px WCAG).
- [ ] Viewport stability: `min-h-[100dvh]`, never `h-screen`; explicit mobile collapse per section. <!-- ui-alchemy: ignore -->
- [ ] Dark mode defined and tested in both modes (any consumer-facing page).
- [ ] Accessibility: alt text, keyboard nav, visible focus, ARIA where needed; no color-only meaning; touch targets.
- [ ] Icons from an allowed library or authored SVG in one consistent stroke; no emoji-as-icon, no unicode glyphs.
- [ ] Browser surfaces themed: selection, caret, scrollbars, focus rings, underline offset, tabular numerals.
- [ ] One design system per project; tokens used, not raw hex scattered; elevation declared once (border or shadow).
