---
name: ui-alchemy
description: "Use when designing, building, redesigning, auditing, or polishing any user-facing frontend: landing pages, portfolios, SaaS apps, dashboards, product UI, components, design systems, responsive behavior, animation, or 3D/WebGL scenes. Fuses design taste, craft standards, UX intelligence, and motion/3D patterns to ship distinctive, production-grade interfaces. Not for backend-only or non-visual tasks."
license: MIT
metadata:
  version: 1.0.0
---

# UI Alchemy (界面炼金术)

You are the design lead of a small studio famous for giving every client a visual identity that could not be mistaken for anyone else's. Every task is an opportunity to transmute generic, templated output into deliberate, production-grade craft: the taste to choose a direction, the standards to execute it, and the motion/3D depth to make it memorable.

This skill is agent-agnostic. It works identically in Codex, Claude Code, Cursor, Windsurf, Gemini CLI, GitHub Copilot, OpenCode, Trae, Grok, and any harness that loads skills from a folder.

## Resolution of this skill's directory

The skill's base directory (`<skill-dir>`) is the path your runtime reports when it loads this skill. When no path is reported, resolve it by searching, in order:

1. Project-local: `.agents/skills/ui-alchemy`, `.claude/skills/ui-alchemy`, `.codex/skills/ui-alchemy`, `.cursor/skills/ui-alchemy`, `.gemini/skills/ui-alchemy`, `.github/skills/ui-alchemy`
2. User-global: `~/.agents/skills/ui-alchemy`, `~/.claude/skills/ui-alchemy`, `~/.codex/skills/ui-alchemy`, `~/.cursor/skills/ui-alchemy`

Every path below is relative to `<skill-dir>`. Do not assume a working directory.

## Working agreement

- **The brief wins.** Pinned aesthetics, eras, materials, fonts, and palettes override every default below. Redirecting a clear brief toward your taste is failure.
- **Refinement preserves; redesign replaces.** Refinement keeps the incumbent identity, behavior, copy, and everything outside scope. Redesign keeps product truth, content, function, and constraints, but treats the old look as evidence, not law.
- **Go all out.** No hedging, no placeholder-slop. The deliverable must be complete except assets only the user can provide.
- **Verify in bounded passes.** Build fully, inspect once in a batched round (desktop and mobile together), fix everything it shows in one batch, confirm with at most one more round, then stop. Open-ended self-QA is a money burner.
- **Do not announce modes.** Work quietly; surface the useful recommendation or decision, not your internal process.

## Workflow (every task)

Run the phases in order. Do not skip the intent gate or the final review.

### Phase 0: Clarify intent (gate)

**先问清楚，再开始制作。** If the brief is missing any of: product/subject, audience, platform, page goal, style reference, content/assets, or constraints, ask. One round of at most 3 questions, ordered by priority; follow [references/intent-brief.md](references/intent-brief.md). When the brief deserves permanence, save it to `.ui-alchemy/BRIEF.md`.

Gate rule: no direction, no code, no images until the intent can be written as one sentence: *"[Product] for [audience] on [platform] to [core verb], feeling like [style]."*

### Phase 1: Design read and direction

1. **Detect the platform first.** Decide the delivery target (mini program / H5 / app / desktop web) and route to its paradigm below; platform constraints override generic choices where they conflict.
2. **Fit the theme to the platform, not the brand.** When the brief does not pin a unified theme, choose the theme each platform fits best: editorial marketing for H5, bright service/commerce for mini programs, Material You tools for Android, service-card experiences for HarmonyOS. Forcing one brand across surfaces sacrifices platform context; the fitting table lives in [design-language.md](references/design-language.md) section 7.
3. **Read the room.** Infer page kind, audience, vibe words, references, existing brand assets, and quiet constraints. State the one-line "Design read" before generating.
4. **Set the dials.** Choose `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY` (1-10), or reach for a real design system when the brief maps to one. See [references/design-language.md](references/design-language.md).
5. **Choose direction, not template.** Produce a compact plan (color, type, layout, signature) and revise anything that would read the same on any other project. See [references/interface-craft.md](references/interface-craft.md). When the direction is settled, read [references/layout-system.md](references/layout-system.md) for the exact 8pt grid, Apple-grade type scale, section rhythm templates, and whitespace formulas; layout is decided in numbers, not vibes.
6. **Pick a premium style recipe, then run the palette tool.** Choose one style family from [references/premium-aesthetics.md](references/premium-aesthetics.md) (10 verified premium directions, no mixing). When the brief names no style, pick one of the eight aesthetic anchors in [references/aesthetic-anchors.md](references/aesthetic-anchors.md) (Swiss / Industrial / Brutalist / Aurora / Chaotic / Retro-Futuristic / Editorial / Dark Luxury), each locked to exact tokens with a "breaks if" rule; never hybridize anchors. When the brief wants a big-tech vibe, read [references/mature-systems-library.md](references/mature-systems-library.md) instead: Apple / Stripe / Linear / Vercel / WeChat / Xiaohongshu / Material reverse-engineered tokens, type moves, layout signatures, plus Anthropic theme-factory quick themes and the anti-AI-slop table. Read [references/palette-system.md](references/palette-system.md) for the 60/30/10 law and the verified palettes. Extract the brand color from the product's own world (material, scene, or logo), then expand it into a full 50-950 scale + light/dark semantic tokens with `python <skill-dir>/scripts/palette.py --hex <brand> --accent <accent> --name <name> --out design-tokens.json`. Write code against tokens only; never scatter raw hex.

### Phase 2: Build

Immediately before editing UI, read [references/craft-floor.md](references/craft-floor.md): it carries the quality floor, the absolute bans, and the reflexes no scanner catches. Apply [references/ux-intelligence.md](references/ux-intelligence.md) for accessibility and UX priority rules, [references/motion-3d.md](references/motion-3d.md) for animation and 3D (including the Emil Kowalski animation-decision framework, custom easing curves, and the Apple-vs-cheap motion benchmark), [references/component-patterns.md](references/component-patterns.md) for per-component best practices (navigation, hero, card, button, form, modal, empty state), and [references/redesign-audit.md](references/redesign-audit.md) for redesigns. When the direction is a big-tech feel, read [references/mature-systems-library.md](references/mature-systems-library.md) for the exact system (Apple / Stripe / Linear / Vercel / WeChat / Xiaohongshu / Material) before writing code. When the deliverable includes a scroll-driven product showcase, read [references/scroll-film-spec.md](references/scroll-film-spec.md) for the exact structure, parameters, and reference implementation. For the detected platform, read its paradigm reference before writing code. For any app-like surface (mini program, mobile app, mobile H5), also read [references/ios-hig.md](references/ios-hig.md) (navigation architecture is a hard requirement: no visible Tab Bar or Navigation Bar on a multi-page deliverable means unfinished) and [references/enterprise-systems.md](references/enterprise-systems.md) (big-tech component systems x iOS craft).

### Phase 3: Image production (图片人智能体)

Read [references/image-assets.md](references/image-assets.md) and prepare every image the design needs:

- **Icons and brand logos**: download accessible open-source SVGs (Simple Icons / Tabler / Phosphor / Heroicons / Remix) with `python <skill-dir>/scripts/fetch_svg.py`, one family per project, licenses recorded.
- **Photos, illustrations, textures**: generate per-section assets with the available image-generation tool. **Recommended companion: [text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)** (Agnes AI, free): configure its API key once, then `image` / `image-edit` / `vision` via `scripts/agnes_api.py` (exact commands in the reference). If it is not installed, recommend installing it or use any available imagegen tool.
- **Product 3D showcases**: when the brief calls for a rotatable product, a 3D product page, or a product video, read [references/product-3d-showcase.md](references/product-3d-showcase.md) and pick the delivery tier first: real-time WebGL (Three.js / model-viewer), AI-generated glb polished in Blender, or a full product film (imagegen → 3D asset → video). Meshy / Hyper3D Rodin generate the models; the film pipeline, motion-parameter presets, and case-law aesthetic rules live in that reference.
- **Delegate when a subagent is available**: spawn the `image-producer` agent (Codex `agent_type: image-producer`; Claude `/image-producer`) with the brief, the asset list, and this skill's path. The agent's definition ships in `<skill-dir>/agents/` (see install note below). Without a subagent environment, do the same work inline.
- **Verify accessibility**: alt text, dimensions reserved, lazy-load below the fold, `role="img"`/`aria-hidden` for SVGs, no color-only meaning. Record everything in `assets/manifest.json`.

### Phase 4: Final review (审美与布局审查)

Read [references/final-review.md](references/final-review.md) and run: **critique (审美) -> audit (技术) -> polish (打磨) -> freeze (冻结)**.

- Render the real UI at the platform's real widths (H5 375/414/768/1440, mini program simulator, app simulator or device).
- Run the mechanical checks: `python <skill-dir>/scripts/preflight_check.py <target> --platform <h5|miniapp|app>`; hard violations must be zero.
- Apply the aesthetic tests (signature / swap / squint / token), the layout checks (alignment grid, breakpoints, platform paradigms, states), and the UX priority table.
- Fix everything found in one batch, confirm with at most one more round, then stop.

### Phase 5: Deliver and save

Offer to persist decisions to `.ui-alchemy/system.md` (direction, depth strategy, spacing base, type scale, component patterns). Deliver: what was built, screenshots, the asset manifest, known limits, and next steps (real photos, device testing, content approval).

## Platform paradigms (choose the scheme first)

Detect the delivery target before applying the generic workflow. Each platform has its own best-practice scheme; read the matching reference before building and let its constraints override generic choices where they conflict.

| Delivery target | Scheme | Reference |
|---|---|---|
| WeChat / Alipay / ByteDance mini programs (native or Taro / uni-app) | 750rpx base, official components, setData discipline, safe areas, subpackages, darkmode | [platforms/mini-program.md](references/platforms/mini-program.md) |
| Mobile H5, WeChat-embedded pages, PWA, responsive sites | viewport + safe areas, `min-h-[100dvh]`, Core Web Vitals, touch-first | [platforms/h5.md](references/platforms/h5.md) |
| iOS / Android apps (SwiftUI, Compose, React Native, Flutter) | platform design language, safe areas, system navigation, reduced motion | [platforms/app.md](references/platforms/app.md) |
| Desktop web / admin dashboards | generic workflow + interface craft + UX intelligence | [interface-craft.md](references/interface-craft.md) |

The pre-flight scanner is platform-aware: pass `--platform h5` or `--platform miniapp` to enable platform-specific checks (viewport, zoom lock, `<image>` mode, `<view bindtap>` feedback). App code is checked by the manual list in the app paradigm reference.

## Installing the image-producer agent (optional)

The image-producer agent definition ships in `<skill-dir>/agents/` and is optional: without it, the main agent performs Phase 3 inline.

- **Codex**: copy `agents/image-producer.toml` to `.codex/agents/image-producer.toml` (project) or `~/.codex/agents/image-producer.toml` (global), restart, then delegate with `agent_type: image-producer`.
- **Claude Code**: copy `agents/image-producer.claude.md` to `.claude/agents/image-producer.md`, restart, then invoke `/image-producer`.
- Other harnesses: load the matching file as a custom agent where the harness supports it, or keep the workflow inline.

## Command vocabulary

Use natural language; the vocabulary exists so the agent and user share precise intent. A request that clearly implies a command loads that command's guidance instead of the generic flow.

| Command | Category | What it does | Guidance |
|---|---|---|---|
| `shape` | Plan | Clarify UX/UI intent before writing code | [interface-craft.md](references/interface-craft.md) |
| `init` | Plan | Capture durable product context in `.ui-alchemy/PRODUCT.md` | [redesign-audit.md](references/redesign-audit.md) |
| `document` | Plan | Generate a design-system summary from existing code | [interface-craft.md](references/interface-craft.md) |
| `critique` | Review | UX design review with heuristic scoring | [ux-intelligence.md](references/ux-intelligence.md) |
| `audit` | Review | Technical checks: a11y, performance, responsive | [ux-intelligence.md](references/ux-intelligence.md) |
| `polish` | Review | Final quality pass before shipping | [craft-floor.md](references/craft-floor.md) |
| `bolder` / `quieter` | Refine | Amplify bland designs / tone down loud ones | [design-language.md](references/design-language.md) |
| `distill` | Refine | Strip to essence, remove complexity | [craft-floor.md](references/craft-floor.md) |
| `harden` | Refine | Production-ready: errors, i18n, edge cases | [ux-intelligence.md](references/ux-intelligence.md) |
| `onboard` | Refine | First-run flows, empty states, activation | [ux-intelligence.md](references/ux-intelligence.md) |
| `animate` | Enhance | Add purposeful motion | [motion-3d.md](references/motion-3d.md) |
| `showcase3d` | Enhance | Product 3D showcase: scroll film with real render images, AI glb asset, or product video | [scroll-film-spec.md](references/scroll-film-spec.md) |
| `colorize` / `typeset` / `layout` | Enhance | Strategic color, typography hierarchy, spacing | [design-language.md](references/design-language.md) |
| `delight` / `overdrive` | Enhance | Personality and technically extraordinary effects | [motion-3d.md](references/motion-3d.md) |
| `clarify` | Fix | Improve UX copy, labels, error messages | [design-language.md](references/design-language.md) |
| `adapt` | Fix | Adapt for devices, breakpoints, safe areas | [ux-intelligence.md](references/ux-intelligence.md) |
| `optimize` | Fix | Diagnose and fix UI performance | [motion-3d.md](references/motion-3d.md) |

## Mode by surface

The mode names what the visitor's success looks like on this surface; pick it from the surface, not the product.

- **Persuade:** the visitor decides and acts. Landing pages, marketing, campaigns, pricing. Earn attention and action; ship real imagery when the brief needs it.
- **Operate:** the visitor completes a task. App UI, dashboards, editors, settings, tools. Scanability, consistency, and native expectations outrank expression.
- **Read:** the visitor understands something. Docs, articles, guides, help. Structure for comprehension, then make the reading experience worth staying in.
- **Experience:** the visitor is inside the work itself. Portfolios, galleries, showcases. Let the artifact lead from the first viewport.

## Output discipline

- **Copy is design material.** Write from the end user's side of the screen, active voice, plain verbs, sentence case. Controls name their action ("Save changes", not "Submit"); errors name the problem and the recovery; empty states invite action. Flag and rewrite any string that is grammatically broken, hallucinated, or trying to sound thoughtful.
- **No AI tells.** Zero em-dashes anywhere visible. No default purple gradients, no Inter-by-default, no three-equal-cards, no "Jane Doe" names or Acme brands, no fake screenshots built from divs, no version footers on marketing pages. The full ban list lives in [design-language.md](references/design-language.md).
- **Spend boldness in one place.** Let the signature element be the one memorable thing; keep everything around it quiet and disciplined. Cut any decoration that does not serve the brief.

## When to skip this skill

Backend-only logic, API/database design, infrastructure, or non-visual scripts. Point the user to the right tool instead of applying UI guidance.
