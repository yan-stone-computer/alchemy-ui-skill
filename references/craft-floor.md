# Craft Floor: the quality floor and the absolute bans

Read this immediately before editing UI, after the direction is settled. Build without announcing the checklist. A pinned brief or the committed visual world overrides anything here; your own habit does not.

## Verify (checks on the built result, not intentions)

Run these together in one batched inspection round (desktop and mobile in the same round on web; the shipped device classes on native). The checks share one render.

- **Contrast:** body and placeholder text >= 4.5:1, large text >= 3:1. On colored surfaces, tint secondary text from that hue or the foreground; never gray.
- **Depth:** shadows carry an offset and a soft blur. A zero-offset colored halo is decoration.
- **Spacing:** tight groups, generous separation, more space above a heading than below it. Read the computed values.
- **Type:** body measure 65-75ch, display max 6rem, tracking floor -0.04em, balanced headings, obvious scale and weight steps. Run the real copy at every breakpoint and fix overflow.
- **Motion:** one authored moment, not scattered effects and not one identical entrance on every section. Exponential ease-out from an already-visible default. Reach past transform and opacity (blur, backdrop-filter, clip-path, mask, shadow) when they stay smooth.
- **States:** hover, disabled, loading, error, empty. Plus real content, working controls, responsive composition, keyboard focus.
- **Browser surfaces:** the parts you did not draw still carry the design: text selection, caret, custom scrollbars, focus rings, underline offset, tabular numerals. Theme them from the palette. This is the cheapest signal that a page was built rather than assembled, and the one models skip most reliably.
- **Copy:** the product's own language. Controls name their action; errors name the problem and the recovery.
- **Coverage:** every brief requirement present and findable within seconds.

## Refuse (category defaults, not universal bans)

The brief's own words can earn any of these. Reaching for one when the axis is free means you were not deciding; recognizing that means rewriting the element, not softening it.

Page scaffolds:

- Same-size cards of icon + heading + text as the page structure. Cards are the lazy container; nested cards are always wrong.
- The hero-metric template: big number, small label, supporting stats, accent.
- An eyebrow or kicker above a heading. This one is a ban, not a default: the heading carries its own weight; delete the label and let the heading speak.
- Section numbers (01 / 02 / 03) unless the sequence itself carries information the reader needs.
- A modal for a task that needs neither interruption nor protected focus.

Surface habits:

- Gradient text. Emphasis comes from weight or size.
- Glass and blur as decoration rather than as a specific effect.
- A colored `border-left` / `border-right` above 1px on cards, list items, callouts, or alerts.
- Hard offset shadows (`box-shadow: 4px 4px 0`) outside a world that is actually neobrutalist.
- Sparklines, progress rings, and soft-shadowed rounded rectangles standing in for content.
- Monospace as a costume for "technical" rather than for code, data, or measurement.
- A system display face (Impact, Arial Black, platform sans) as the display voice of an own-world page. Source and self-host a face whose character matches the approved lettering.
- Unicode glyphs or emoji standing in for an icon system. Icons are drawn, from a real library or authored SVG, in one consistent stroke and weight.
- Geometric masks standing in for organic contours (a circle or polygon approximating a photographic subject's edge). Derive an alpha matte from the actual image, or produce a cut-out asset.
- Light or dark picked by category. Pick it from the use scene: who, where, under what ambient light.

## Floor mechanics

- Tracking stops at -0.04em; -0.02 to -0.03em usually reads better.
- Declare elevation once: border OR shadow. A 1px border under a wide soft shadow is the ghost card. Card radii stay at 12-16px; pills are for small controls.
- Real illustration or none. Sketch-style SVG scenes, `loose-sketch` / `doodle` class names, and `feTurbulence` grain read as amateur. Geometry (crisp vector shapes, diagrams, animated linework, shader-driven effects) remains first-class media; a shaded, perspectived, or figure-bearing illustration is a picture even in line-art style.
- Backgrounds are surfaces, textured only from the subject's world. `repeating-linear-gradient` stripes and two-axis grid overlays need an actual canvas, map, blueprint, or measuring tool under them.
- Claims and configuration come from supplied truth; label illustrative values honestly.

The floor holds the mechanics; it never picks the direction. With every check green, spend the page on the committed world, and when torn between refined and committed, commit.

## AI slop 三簇校准（来自 Anthropic frontend-design）

AI 生成设计现在聚集在三个默认长相，自由轴上一旦落到它们就是没做选择：

1. 暖奶油底 + 高对比衬线 display + 陶土色强调；
2. 近黑底 + 单一荧光绿/朱红强调；
3. 通栏报纸风（发丝线、零圆角、密集分栏）。

brief 点名要求时这三个都合法；否则重来。完整 slop 速查、禁用字体（Inter / Roboto / Arial / Fraunces / Space Grotesk 不能当唯一字体）与文案纪律在 [mature-systems-library.md](mature-systems-library.md) 第 9 节。
