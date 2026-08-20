# Design Language: read the room, set the dials, choose the system

Read this when choosing a visual direction or during `bolder`, `quieter`, `colorize`, `typeset`, `layout`, or `clarify` work. It merges the brief-inference discipline of taste-skill with the "ground it in the subject" doctrine of Anthropic's frontend-design.

## 0. Brief inference (read the room before anything else)

Read these signals first:

1. **Page kind**: landing (SaaS / consumer / agency / event), portfolio (dev / designer / studio), redesign (preserve vs overhaul), editorial / blog, or product surface (dashboard / settings / tool).
2. **Vibe words**: "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "playful", "serious B2B", "editorial", "glassy", "dark tech".
3. **Reference signals**: URLs, screenshots, named products, competitors.
4. **Audience**: the audience picks the aesthetic, not your taste.
5. **Brand assets that already exist**: logo, color, type, photography. For redesigns these are starting material, not optional input.
6. **Quiet constraints**: accessibility-first, public sector, regulated, trust-first commerce, kids' products. These OVERRIDE aesthetic preference.

State a one-line Design Read before any code, then set the dials. If the read genuinely diverges, ask exactly one question, never a dump.

## 1. The three dials

`DESIGN_VARIANCE` (1-10: symmetry to artsy chaos), `MOTION_INTENSITY` (1-10: static to cinematic), `VISUAL_DENSITY` (1-10: art gallery to cockpit). Baseline `8 / 6 / 4`; adjust from the table, conversationally, never by asking the user to edit a file.

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| minimalist / calm / editorial / Linear-style | 5-6 | 3-4 | 2-3 |
| premium consumer / Apple-y / luxury | 7-8 | 5-7 | 3-4 |
| playful / Dribbble / Awwwards / agency | 9-10 | 8-10 | 3-4 |
| landing / portfolio / marketing (default) | 7-9 | 6-8 | 3-5 |
| trust-first / public-sector / accessibility-critical | 3-4 | 2-3 | 4-5 |
| redesign - preserve | match existing | +1 | match existing |
| redesign - overhaul | +2 | +2 | match existing |

Dials drive everything below; never invent aliases for them. High variance means asymmetric layouts (grid with fractional units, huge empty zones) that collapse to strict single-column under 768px. High motion means the page must actually move: entry transitions, scroll reveal, hover physics. High density means tight paddings, 1px separators, `font-mono` for numbers, and generic card containers are banned.

## 2. Brief to design-system map

When the brief reads as one of these, install and use the official package. Do not recreate its CSS by hand, and do not import a system's tokens and then override 90% of them. One system per project.

| Brief reads as... | Reach for |
|---|---|
| Microsoft / enterprise SaaS / dashboards | `@fluentui/react-components` or `@fluentui/web-components` |
| Google-ish / Material-flavored | `@material/web` + Material 3 tokens |
| IBM-style B2B / analytics | `@carbon/react` + `@carbon/styles` |
| Shopify app surfaces | Polaris web components / Polaris React |
| Atlassian / Jira-style | `@atlaskit/*` + `@atlaskit/tokens` |
| GitHub-style devtool / community | `@primer/css` or `@primer/react-brand` |
| UK public sector | `govuk-frontend` |
| US public sector / trust-first | `uswds` |
| Fast local-business / agency MVP | Bootstrap 5.3 |
| Accessible React foundation | `@radix-ui/themes` |
| SaaS where you own the components | shadcn/ui (`npx shadcn@latest add ...`), never in default state |
| Tailwind-based modern SaaS | Tailwind v4 utilities + `dark:` variant |

For aesthetic directions with no official package (glassmorphism, bento, brutalism, editorial, dark tech, aurora gradients, kinetic type), build with native CSS + Tailwind + a maintained component library, and label borrowed inspiration honestly in comments.

Install anchors (verify current versions): `npm install @material/web`, `@fluentui/react-components`, `@carbon/react @carbon/styles`, `@radix-ui/themes`, `@primer/css`, `govuk-frontend`, `uswds`, `bootstrap`; `npx shadcn@latest init && npx shadcn@latest add button card badge separator input`.

## 3. Ground it in the subject

If the brief does not pin the subject, pin it yourself: one concrete subject, its audience, and the page's single job. The subject's own world (materials, instruments, artifacts, vernacular) is where distinctive choices come from. Before proposing a direction, produce all four:

- **Domain**: 5+ concepts, metaphors, vocabulary from this product's world, not features.
- **Color world**: 5+ colors that exist naturally in that world. Not "warm" or "cool"; walk into the physical version of the space.
- **Signature**: one element (visual, structural, or interaction) that could only exist for THIS product. If you cannot name one, keep exploring.
- **Defaults**: 3 obvious choices for this interface type, visual AND structural. You cannot avoid patterns you have not named.

The test: read your proposal with the product name removed. If someone cannot identify what it is for, explore deeper.

## 4. Anti-default bans (AI tells)

These are the signatures of templated AI output. Treat them as hard bans unless the brief explicitly calls for one:

- **Em-dash (`-`) is completely banned** in headlines, eyebrows, labels, body, quotes, attribution, captions, buttons, alt text. Use periods, commas, parentheses, or hyphens. En-dash as separator is banned too; date ranges use a hyphen. This is non-negotiable; the scanner in `scripts/preflight_check.py` enforces it.
- **No default purple/blue gradient glows.** Neutral bases (Zinc / Slate / Stone) with one high-contrast accent (Emerald, Electric Blue, Deep Rose, Burnt Orange). If the brand asks for purple, execute it with intent.
- **No Inter by default.** Prefer Geist, Outfit, Cabinet Grotesk, Satoshi, or a brand-appropriate face. Inter is acceptable when the user explicitly asks for a neutral / Linear-style feel or the brief is public-sector / accessibility-first.
- **Serif is not the default for "creative".** Only when the brand names a serif, or the aesthetic family is genuinely editorial / luxury / heritage AND you can articulate why this specific serif fits. Banned as defaults: Fraunces, Instrument_Serif. Emphasis within a headline uses italic or bold of the SAME font, never a random injected serif.
- **No three-equal-cards feature rows.** Use asymmetric grids, 2-column zig-zag, bento, scroll-pinned, or horizontal-scroll alternatives.
- **No premium-consumer beige+brass+oxblood+espresso default palette** (`#f5f1ea`-family backgrounds, brass/clay/ochre accents). Rotate among cold luxury, forest+amber, black+tan, cobalt+cream, terracotta+slate, or monochrome+one saturated pop.
- **No eyebrow above every section.** Maximum 1 eyebrow per 3 sections (hero counts). Count `uppercase tracking` micro-labels; if the count exceeds ceil(sectionCount / 3), fail.
- **No split-header default** ("left big headline + right small explainer"). Stack vertically; use the right column only for a real visual or interactive element.
- **No section-number eyebrows** (`01 / 02`, `001 - Capabilities`) unless the content is genuinely a sequence where order carries information.
- **No hero-metric template** (big number, small label, supporting stats, gradient accent) unless it is truly the best option.
- **No zigzag alternation beyond 2 consecutive sections** with image+text splits.
- **No marquee beyond once per page.**
- **No duplicate CTA intent** (one label per intent: "Get in touch" / "Contact us" / "Let's talk" all count as one).
- **No logo wall inside the hero**; it belongs under the hero, logos only, real SVG marks (Simple Icons / devicon / generated monogram), never plain text wordmarks.
- **No fake screenshots from divs**, no fake-precise numbers without real data or `mock` labels, no generic names ("Jane Doe"), no startup-slop brand names ("Acme", "Nexus"), no filler verbs ("Elevate", "Seamless", "Revolutionize").
- **No scroll cues** ("Scroll", arrow-down hints), no version labels in hero (`v0.6`, `BETA`) unless it is a real launch, no locale/weather strips, no decoration text strip at hero bottom ("BRAND. MOTION. SPATIAL."), no photo-credit captions as decoration, no pills overlaid on images.
- **No pure `#000000` / `#ffffff`** (off-black / off-white with depth), no oversized H1s that just scream, no gradient text for emphasis, no custom mouse cursors, no `h-screen` (use `min-h-[100dvh]`). <!-- ui-alchemy: ignore -->
- **No `transition: all`**, no animating width/height/margin/padding, no `window.addEventListener("scroll")` for scroll logic. <!-- ui-alchemy: ignore -->
- **Hero discipline**: fits the initial viewport; headline max 2 lines; subtext max 20 words; CTAs visible without scroll; top padding max `pt-24`; max 4 text elements; trust micro-strips and taglines move below the hero.
- **One accent, one palette, one theme per page.** No warm-gray site suddenly getting a blue CTA; no mid-page light/dark flip (unless a deliberate one-time "theme switch" device).

## 5. Copy discipline

- **Hero is a thesis.** Open with the most characteristic thing in the subject's world: headline, image, animation, live demo, or interactive moment.
- **Structure is information.** Numbering, eyebrows, dividers, labels encode something true about the content; they do not decorate it.
- **Words are design material.** Name things by what people control and recognize, never by how the system is built. "Save changes", not "Submit". Same name through the whole flow: "Publish" produces a "Published" toast.
- **Active voice, sentence case, no filler.** Errors do not apologize and are never vague. Empty screens invite action.
- **Self-audit copy before ship**: re-read every visible string; rewrite anything grammatically broken, hallucinated, or trying to sound thoughtful.

## 6. Redesign-specific levers

For `bolder`/`quieter`/redesign work, apply the full audit protocol in [redesign-audit.md](redesign-audit.md). Priority order of modernization levers: typography refresh, spacing & rhythm, color recalibration, motion layer, hero & key-section recomposition, then full block replacement.

## 7. 审美基准与平台主题适配（Aesthetic floor & platform fitting）

### 参考级标杆（用于校准，不是照抄）

- **Persuade**（营销/落地页）：Apple、Linear、Spotify 的品牌页。
- **Operate**（产品/工具）：Linear、Stripe、Notion 的界面。
- **Read**（文档/阅读）：Stripe、Apple 的文档站。
- **Experience**（展陈/作品）：精选 Awwwards / FWA 作品。

交付前问一句：把这个界面放到这些标杆旁边，它会被认成"又一个 AI 模板"，还是有自己的性格？

### "丑"的五个诊断（逐条对照）

1. **无焦点**：每块内容一样大、一样重，眼睛没有落点。修：每屏只让一个元素赢。
2. **间距随手**：没有落在 4/8px 网格上，随机 14/17/23px。修：定一个 base unit，全身只用它的倍数。
3. **色彩无来源**：灰色底 + 一个强调色，但说不出来自哪个世界。修：从产品本身的材质/场景里取色。
4. **字体无性格**：默认系统字体、只有一个字号档。修：一个有个性的 display face + 3 档字重/色彩层级。
5. **图片像占位**：没有艺术指导，随便一张图。修：图片与文案同一机位、同一光线、同一情绪。

### Chanel 法则

交付前删掉一个"配饰"：多余的边框、装饰色、图标、动效、渐变。删完之后如果还好看，说明之前确实多了一件。

### 平台主题适配（不要强行统一品牌）

不要为了"一套品牌"牺牲平台语境。用户没有指定统一主题时，**每个平台选最适合它的主题**：

| 平台 | 语境 | 主题倾向 |
|---|---|---|
| H5 营销页 | 叙事与转化 | 编辑式排版、强焦点、签名动效、真实图片艺术指导 |
| 小程序 | 消费与服务 | 明快或氛围化、官方组件库（WeUI/Vant）、卡片网格、底部安全区 |
| Android | 工具与效率 | Material You 动态取色、大数字 tabular-nums、系统动效、触控密度 |
| HarmonyOS | 服务与展陈 | 卡片式分层、大圆角、半透明材质、服务卡片思维 |
| 桌面后台 | 效率 | 密度、键盘可达、数据可视化优先 |

同一品牌多端时遵循"同源不同面"：共享色彩/字体/签名元素，但交互与组件跟随平台（iOS 标签栏、Android 返回键、小程序胶囊按钮）。

### "看起来贵"的配方

- 一个有个性且被节制的 display 字体（衬线或几何无衬线），正文用互补字体。
- 三档层级：`strong`（600/primary）、`regular`（500/secondary）、`muted`（400/tertiary），同一字号也能分出层级。
- 每屏一个焦点：更大的字、更实的色、或更宽的留白。
- 间距系统化：4/8 网格，组内紧、组间松，标题上方比下方多留白。
- 图片有艺术指导：统一光线与情绪；宁缺毋滥，绝不用无意义的渐变球。
- 细节：tabular numbers、光学对齐、`text-wrap: balance`、1px 内描边、按钮按下反馈。
- 极简不等于空：每个留白都有让眼睛休息的理由，每个元素都有存在的原因。

## 8. 苹果级质感与大厂范式（App 类界面必读）

App / 小程序 / 移动 H5 的审美基准是"像 iPhone 原生 UI 一样好看"，这来自两套规范：

- **[references/ios-hig.md](ios-hig.md)**：导航架构硬要求（Tab Bar / Navigation Bar 二选一或组合）、大标题、分组列表、材质模糊、44pt 触控、iOS 动效曲线、状态齐全。多页面交付物没有可见导航 = 未完成。
- **[references/enterprise-systems.md](enterprise-systems.md)**：WeUI / Ant Design / Material 3 / Fluent 等大厂体系的选择与融合，借体系的工程一致性 + iOS 的细节精致度。

核心法则：**先导航，后配色，再动效**。导航缺席时，任何漂亮配色都无法让页面像"产品"。

## 9. 高级风格与配色（所有项目必读）

高级感不是玄学，是配方：

- **选风格**：[premium-aesthetics.md](premium-aesthetics.md) 有 10 套验证过的高级风格方向（暗夜香槟、雾蓝晨光、编辑纸墨、森野铜光、陶土南意、极地冰川、京都墨彩、法式公寓、霓虹黑金、侘寂陶土），每套含情绪/字体/配色/布局签名/质感/反例。选一套，禁止混搭。
- **出配色**：[palette-system.md](palette-system.md) 讲 60/30/10、12 组验证调色板、色阶生成与对比度自检；`scripts/palette.py` 把品牌主色一键展开成 50-950 色阶 + 明暗语义 token + WCAG 对比度报告，`scripts/palette_card.py` 把 token 渲染成可视化色卡。
- **铁律**：一主一辅一强调；表面有温度（无纯黑纯白）；色温统一；写代码只用 token。
