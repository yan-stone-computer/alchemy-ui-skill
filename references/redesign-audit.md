# Redesign & Audit: audit first, preserve what matters, modernize with intent

Read this for any redesign, audit, or review request. Misclassifying the mode is the single biggest source of bad redesign output.

## 1. Detect the mode (first action)

- **Greenfield** - no existing site, or a full overhaul approved. Dial baseline from [design-language.md](design-language.md).
- **Redesign - Preserve** - modernize without breaking the brand. Audit first, extract brand tokens, evolve gradually.
- **Redesign - Overhaul** - new visual language on top of existing content. Greenfield for visuals; preserve content and IA.

If ambiguous, ask once: "Should this redesign preserve the existing brand, or are we starting visually from scratch?"

## 2. Audit before touching

Document the current state before proposing anything:

- **Brand tokens**: primary/accent colors, type stack, logo treatment, radii, spacing.
- **Information architecture**: page tree, primary nav, key conversion paths.
- **Content blocks**: what exists, what is doing work, what is filler.
- **Patterns to preserve**: signature interactions, recognizable hero, copy voice, accessibility wins, analytics events.
- **Patterns to retire**: AI-slop tells, broken layouts, dead links, generic stock imagery, perf traps.
- **Dial reading of the existing site**: infer its current VARIANCE / MOTION / DENSITY. That is the starting point, not the baseline.
- **SEO baseline**: ranking pages, meta titles, structured data, OG cards. SEO migration is the #1 redesign risk.

## 3. Preservation rules

- Do not change information architecture unless asked: keep page slugs, anchor IDs, and primary nav labels stable.
- Extract brand colors before applying anti-default rules. A brand that is already purple stays purple.
- Preserve copy voice unless a rewrite was requested. Visual modernization is not a content rewrite.
- Honor existing accessibility wins: do not regress focus states, alt text, keyboard nav, contrast.
- Respect existing analytics events: do not rename buttons, form fields, or section IDs that downstream tracking depends on.

## 4. Modernization levers (priority order)

Apply in order; stop when the brief is satisfied:

1. **Typography refresh** - the biggest visual lift per unit of risk.
2. **Spacing & rhythm** - increase section padding, fix vertical rhythm.
3. **Color recalibration** - desaturate, unify neutrals, keep the brand accent.
4. **Motion layer** - MOTION_INTENSITY-appropriate micro-interactions on existing components.
5. **Hero & key-section recomposition** - restructure top-of-funnel using the pattern vocabulary.
6. **Full block replacement** - only when the existing block is unsalvageable.

## 5. Decision tree

- IA, content, and SEO sound -> **targeted evolution** (levers 1-4). Roughly 70% of the value at 40% of the risk.
- Visual debt is structural (broken IA, no design system, broken mobile) -> **full redesign** with strict content preservation.
- The brand itself is changing -> **greenfield**.

## 6. What never changes silently

Never modify without explicit user approval: URL structure/route slugs, primary nav labels, form field names or order (breaks analytics + autofill), brand logo or wordmark, and existing legal/consent/cookie copy.

## 7. Review output quality

After changes, run the craft-floor checks ([craft-floor.md](craft-floor.md)) and the final pre-flight ([preflight.md](preflight.md)). If a screenshot or live browser is available, compare before/after at desktop and mobile widths and confirm no regression in contrast, focus, or motion preference.
