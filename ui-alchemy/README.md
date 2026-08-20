# UI Alchemy / 界面炼金术

> 把品味、工艺、UX 智能与 3D 动效，炼成不撞款的精品前端。
> Transmute generic frontends into distinctive, production-grade interfaces with taste, craft, UX intelligence, and 3D motion.

![MIT](https://img.shields.io/badge/license-MIT-blue)
![Agents](https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20Gemini%20%7C%20Copilot%20%7C%20more-lightgrey)
![Zero-Dep](https://img.shields.io/badge/dependencies-zero-green)

**UI Alchemy** 是一个跨智能体（agent-agnostic）的全栈前端设计 Skill：一个 SKILL.md，在 Codex、Claude Code、Cursor、Windsurf、Gemini CLI、GitHub Copilot、OpenCode、Trae、Grok 等所有主流智能体中表现一致。

它不是又一份"设计建议"，而是一套**可执行的工艺系统**：先读懂需求，再定方向，然后按质量底线构建，最后用确定性扫描器过预检。目标是消灭"AI 味"：默认紫渐变、Inter 字体、三张等宽卡片、破折号刷屏、假截图。

---

## 它融合了什么（Fused From）

UI Alchemy 是对当下最火的设计类 Skill 的系统性蒸馏与融合：

| 来源 | 贡献 | 许可 |
|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UX 优先级规则库、可访问性、交互、色彩/字体/堆栈决策 | MIT |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 反 AI 味纪律、三旋钮（VARIANCE/MOTION/DENSITY）、设计系统地图、预检清单 | MIT |
| [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) | 工艺优先的界面设计：层级、字体比例、token 架构、系统记忆 | MIT |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 质量底线（craft floor）、命令词汇、审核/打磨工作流 | Apache-2.0 |
| [anthropics/skills - frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | "扎根于主题"的差异化设计哲学、文案纪律 | MIT |
| [anthropics/skills - theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | 10 套快速主题配方（4 色 + 字体 + 场景） | MIT |
| [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | 3D / WebGL / 动效（Three.js、R3F、GSAP、Motion）最佳实践 | MIT |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 151 套生产设计体系反解（Apple / Stripe / Linear / Vercel / WeChat / 小红书 / Material 等）的 token、字体、布局签名 | AGPL-3.0（仅吸收方法与 token 事实，无代码复制） |
| [OneRedOak/claude-code-workflows - design-review](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) | Live Environment First 评审法：8 阶段流程 + Blocker/High/Medium/Nit 分级 | MIT |
| [jiji262/claude-design-skill](https://github.com/jiji262/claude-design-skill) | 10 大设计语言锚点、Design Direction Advisor 模式（方向提案 → 预览 → 用户选定） | MIT |
| [vercel-labs/agent-skills - web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Web 设计指南合规：间距/字体/色彩一致性检查 | MIT |
| [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | 高保真 HTML 设计路由、AI Slop 速查表、禁用字体清单、截图必交付铁律 | MIT |
| [addyosmani/agent-skills - frontend-ui-engineering](https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering) | 前端 UI 工程质量检查与实现纪律 | Apache-2.0 |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 动画决策框架（频率 → 目的 → 缓动）、自定义缓动曲线、Before/After 评审格式 | MIT |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 产品视频八阶段流水线、品牌→动效参数推导表、判例式审美准则（R/Q/S/C/P） | MIT |
| [meshy-dev/meshy-3d-agent](https://github.com/meshy-dev/meshy-3d-agent) | Meshy AI 3D 生成：文本/图片转 3D、纹理、绑定动画的 API 工作流 | MIT |
| [DeemosTech/rodin3d-skills](https://github.com/DeemosTech/rodin3d-skills) | Hyper3D Rodin 生产级图片/文本转 3D（glb/usdz/fbx/obj/stl） | Apache-2.0 |
| [kevinbadi/blender-skills](https://github.com/kevinbadi/blender-skills) | Blender 3D 产品精修：四灯布光、材质、EEVEE 实时渲染、turntable 运镜 | MIT |
| [AThevon/genjutsu](https://github.com/AThevon/genjutsu) | 创意编码交互论：interaction thesis 先行、复杂度匹配、预览门 | MIT |
| [CristianOlivera1/openvid](https://github.com/CristianOlivera1/openvid) | 浏览器内 3D mockup 与产品演示的成熟实现参考 | MIT |
| [Ilm-Alan/frontend-design](https://github.com/Ilm-Alan/frontend-design) | 八美学锚点（Swiss / Industrial / Brutalist / Aurora / Chaotic / Retro-Futuristic / Editorial / Dark Luxury），每个锚点锁定精确 CSS tokens 与 "breaks if" 纪律 | MIT |
| [carmahhawwari/ui-design-brain](https://github.com/carmahhawwari/ui-design-brain) | 60+ 组件布局模式：导航/卡片/表单/弹层/空态的最佳实践与常见布局 | MIT |
| [Wholiver/swiftui-design-skill](https://github.com/Wholiver/swiftui-design-skill) | 六条反 AI Sloppiness 铁律、五维设计审查（布局/排版/色彩/动效/无障碍评分制） | MIT |
| [dickwu/apple-design-skill](https://github.com/dickwu/apple-design-skill) | Apple HIG 跨平台审查基准（Flutter/RN/Electron/Tauri） | MIT |
| Apple Human Interface Guidelines | iOS 美学与导航基准：Tab Bar / Navigation Bar 硬要求、大标题、分组列表、材质模糊、44pt、动效曲线 | Apple 许可（引用规范） |
| WeUI / Ant Design / Material 3 / Fluent / Arco / Semi | 大厂设计体系：组件工程一致性 + 语义 token + 状态设计 | 各体系 MIT/Apache-2.0 |

以及 skills.sh 生态中验证过的模式：Anthropic 官方 `frontend-design`（数十万安装量）、Three.js/R3F 系列、Motion + GSAP 滚动画卷等。

---

## 特性（What You Get）

- **一套工作流，两种交付质量**：读需求 -> 定旋钮 -> 选设计系统 -> 定方向 -> 构建 -> 一次性批量验证 -> 存档决策。
- **反 AI 味硬规则**：零破折号、无默认紫渐变、无 Inter 默认、无三等宽卡片、无假截图、无 `h-screen`，全部写成可检查的规则。<!-- ui-alchemy: ignore -->
- **确定性预检扫描器**：`preflight_check.py` 零依赖，自动抓出最常见的 AI tell（破折号、纯黑纯白、`transition: all`、scroll 监听、`<div onClick>`、缺 alt、白底白字 CTA 等）。<!-- ui-alchemy: ignore -->
- **3D 与动效开箱即用**：Three.js / React Three Fiber / GSAP ScrollTrigger / Motion 的选型矩阵、规范骨架与性能红线。
- **平台最佳范式**：小程序（750rpx / setData / 分包 / 安全区）、H5（viewport / Core Web Vitals / 触控优先）、App（iOS HIG / Material 3 / RN / Flutter）各有一套独立方案，扫描器按 `--platform` 追加专属检查。
- **苹果级质感（iOS-Grade UI）**：导航架构是硬要求，多页面交付物必须有可见 Tab Bar / Navigation Bar；大标题、圆角分组列表、半透明材质、44pt 触控、iOS 动效曲线，一套可直接执行的 HIG 清单。
- **大厂体系融合**：WeUI / Ant Design / Material 3 / Fluent / Arco 的选择矩阵与 token 对齐方法，借大厂工程一致性 + iOS 细节精致度。
- **高级风格与配色（Premium Recipes + Palette System）**：10 套验证过的高级风格配方（暗夜香槟/雾蓝晨光/编辑纸墨/森野铜光/陶土南意/极地冰川/京都墨彩/法式公寓/霓虹黑金/侘寂陶土）+ 12 组验证调色板；`palette.py` 一键把品牌色展开为 50-950 色阶与明暗语义 token，自动过 WCAG 对比度；`palette_card.py` 输出可视化色卡。
- **大厂成熟体系库（Mature Systems Library）**：Apple / Stripe / Linear / Vercel / WeChat / 小红书 / Material 的反解 token、字体层级、布局签名与"最适合/最不适合"；Anthropic theme-factory 10 套快速主题；反 AI Slop 三簇校准、12 项 slop 速查与禁用字体清单。取结构方法，不抄视觉。
- **设计工程与评审法**：Emil Kowalski 动画决策框架（高频不动画、目的驱动、自定义缓动曲线）、OneRedOak Live Environment First 八阶段评审法与四档分级（Blocker/High/Medium/Nit）。
- **产品 3D 展示专场（Product 3D Showcase）**：三档交付（网页实时 WebGL / AI 生成 glb + Blender 精修 / 产品视频），Meshy 与 Hyper3D Rodin 生成工作流、Blender 四灯精修、video-shotcraft 八阶段产品视频流水线、品牌→动效参数推导表与判例式审美准则（R1-R3 / Q1-Q7），生图→3D→视频串接链路覆盖四端落地（Three.js / threejs-miniprogram / SceneView / XComponent）。
- **真实 PBR 贴图策略**：从 ambientCG / Poly Haven / three.js 内置下载 CC0 贴图（color/normal/roughness/metalness 全套），不再用程序假材质；标签文字用 CanvasTexture 叠层；贴图来源记录进资产清单。
- **滚动驱动 3D 叙事（scroll-driven product film）**：sticky 舞台 + 滚动进度驱动材质/配色/相机/粒子连续插值，每滑一段换一种样式，像视频一样流畅（Apple / Stripe 官网同款手法），四端各有原生方案。
- **Apple 级布局系统（Layout System Spec）**：8pt 网格、Apple 字号阶梯精确表、四种 Section 节奏模板、留白公式、廉价 vs 高级反模式表，布局用数字说话不是凭感觉。
- **滚动 3D 电影规格（Scroll Film Spec）**：结构规格（340vh + sticky）、参数表（zoom/pan/饱和度/字幕时机）、禁 scroll 监听的参考实现、四幕文案模板、高级 vs 廉价动效反模式表，照抄即可出 Apple 级滚动叙事。
- **高级工作流**：先澄清意图（意图门）→ 制作 → 图片人智能体（开源 SVG 图库下载 + 生图模型完善）→ 终审审美与布局 → 交付；不跳过门禁与终审。
- **图片人智能体**：内置 `image-producer` 子智能体（Codex TOML / Claude MD 双格式），负责从 Simple Icons / Tabler / Phosphor / Heroicons / Remix 下载可访问 SVG，并用生图模型（推荐 [text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)，Agnes AI 免费 API）生成照片/插画，最后产出带许可与 alt 的资产清单。
- **跨智能体兼容**：不依赖任何特定环境变量；路径解析提供运行时优先 + 项目级/用户级回退；脚本只用 Python 标准库。
- **记忆与一致**：`.ui-alchemy/system.md` 存档设计决策，跨会话复用。

## 真实效果

用本 Skill 产出、已在真实项目中验证的界面：

| 端 | 案例 | 截图 |
|---|---|---|
| 网页 | 栖山 QISHAN 度假酒店官网：深棕黑底 + 米白衬线、居中留白、静谧高级 | ![栖山首屏](../screenshots/web-qishan-hero.png) ![栖山下半页](../screenshots/web-qishan.png) |
| 小程序 | 苔径咖啡：绿色 + 米白、门店实景、快捷入口 + 人气榜单 | ![苔径小程序](../screenshots/miniapp-taijing.png) |
| 安卓 | 运动健康：卡片式数据面板、趋势图、底部导航 | ![安卓运动健康](../screenshots/android-health.png) |
| 鸿蒙 | 暖居智能家居：ArkUI 卡片化控制中心、房间温度、场景切换 | ![鸿蒙暖居](../screenshots/harmony-home.png) |
| iOS | 回声播客：暖米色调、城市插画、推荐节目与继续收听、四宫格导航 | ![iOS 回声](../screenshots/ios-echo.png) |
| Windows | 磐石产线监控台：深色模式、数据卡、产量趋势、实时告警、设备状态 | ![Windows 磐石](../screenshots/windows-panshi.png) |
| macOS | 手记笔记应用：深色暖调、侧栏列表 + 文章阅读区 | ![macOS 手记](../screenshots/macos-memento.png) |

---

## 安装（Install）

把整个 `ui-alchemy/` 目录复制到你的智能体对应的 skills 目录即可（无需联网、无需 npx）：

| 智能体 | 位置 |
|---|---|
| Codex / 通用 | `~/.agents/skills/ui-alchemy/` 或项目根 `.agents/skills/ui-alchemy/` |
| Claude Code | `~/.claude/skills/ui-alchemy/` 或 `.claude/skills/ui-alchemy/` |
| Cursor | `.cursor/skills/ui-alchemy/`（需在设置中开启 Agent Skills） |
| Gemini CLI | `~/.gemini/skills/ui-alchemy/`（预览版需启用 Skills） |
| GitHub Copilot | `.github/skills/ui-alchemy/` |
| Trae / 其他 | 对应工具的 skills 目录，命名一致即可 |

> 也可以直接把它放进项目仓库的 `.agents/skills/` 让团队共享；重启智能体后生效。

## 使用（Usage）

直接说人话：

```text
用 ui-alchemy 给这个 SaaS 做一个不像模板的落地页
use ui-alchemy to redesign this dashboard, preserve the brand
use ui-alchemy audit on the checkout flow
use ui-alchemy animate this landing page
```

也可以用内置命令词汇精确指定工作类型：`shape`（先规划）、`init`（沉淀产品上下文）、`critique`（UX 评审）、`audit`（a11y/性能/响应式）、`polish`（交付前打磨）、`bolder` / `quieter`（增强/收敛）、`distill`（极简）、`harden`（生产加固）、`animate`（动效）、`colorize` / `typeset` / `layout`、`delight` / `overdrive`、`clarify`（文案）、`adapt`（多端适配）、`optimize`（性能）。

## 四端 3D 演示（Demo）

`demos/multiplatform/` 提供四个平台的原生 demo，各自演示"产品 3D 展示"的最佳范式：

| 平台 | 3D 方案 | 效果 |
|---|---|---|
| H5（野径咖啡） | Three.js + Poly Haven 真实 HDRI 环境 + LatheGeometry 精细罐型（卷边/收腰/罐口）+ ambientCG PBR + 生图模型生成 FIELDTRACE 标签贴图 | 滚动驱动 4 段电影：铜罐入场 → 墨黑金换肤 → 特写标签 → 定格；材质/配色/相机连续插值，字幕随段切换 |
| 小程序（橘夏鲜果茶） | 原生 swiper + rotateY 3D 卡片 | 滑动换装：青柠/鲜橙/莓果三套配色卡片，当前页回正放大，两侧倾斜 |
| Android（阅刻） | Compose HorizontalPager + GraphicsLayer rotateY | 3D 书籍滑卡：滑动时卡片旋转 + 缩放 + 透明度，三种书籍配色 |
| 鸿蒙（廿四节气） | ArkUI Swiper + rotate/scale 动画 | 四季 3D 节气卡：春/夏/秋/冬四张卡，滑动换季，当前页回正 |

## 高级工作流（Advanced Workflow）

```text
Phase 0  澄清意图     缺失产品/受众/平台/目标/风格/素材/约束就提问（一轮最多 3 问），存 .ui-alchemy/BRIEF.md
Phase 1  设计读与方向  平台优先路由 → Design Read → 三旋钮 → 方向计划（颜色/字体/布局/签名）
Phase 2  构建        工艺底线 + UX 优先级 + 平台范式 + 动效/3D
Phase 3  图片生产     图片人智能体：开源 SVG 下载（fetch_svg.py）+ 生图模型（text-model-multimodal-skill）→ 资产清单
Phase 4  终审         审美（签名/换皮/眯眼/token 测试）+ 布局（网格/断点/平台范式）+ 技术审计（preflight）→ 一批修复
Phase 5  交付         截图/预览 + 资产清单 + 已知限制 + 存档 system.md
```

图片人智能体安装（可选，不装则主智能体内联执行）：

```bash
# Codex：复制到项目或全局 agents 目录后重启
cp ui-alchemy/agents/image-producer.toml .codex/agents/image-producer.toml

# Claude Code
cp ui-alchemy/agents/image-producer.claude.md .claude/agents/image-producer.md
```

生图模型推荐集成（免费）：[text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)（Agnes AI，零依赖，自动重试 + 模型降级）。首次使用配置 API Key 即可：

```bash
npx skills add https://github.com/yan-stone-computer/text-model-multimodal-skill
python {TMM_SKILL_ROOT}/scripts/agnes_api.py set-key sk-你的Key   # Key 免费：https://platform.agnes-ai.com/settings/apiKeys
```

然后由图片人智能体调用 `image`（文生图）、`image-edit`（图生图完善）、`vision`（生成后质检）。

---

## 目录结构

```text
ui-alchemy/
|-- SKILL.md                     # 入口：工作流、命令词汇、跨智能体路径解析
|-- README.md                    # 本文件
|-- agents/                      # 子智能体与 UI 元数据
|   |-- openai.yaml              # UI 元数据（显示名、图标、默认提示词）
|   |-- image-producer.toml      # 图片人智能体（Codex）
|   `-- image-producer.claude.md # 图片人智能体（Claude Code）
|-- references/                  # 按需加载的分支规范
|   |-- design-language.md       # 读需求、三旋钮、设计系统地图、反 AI 味清单
|   |-- ios-hig.md              # 苹果级美学与导航基准（Tab Bar/大标题/分组列表/材质/44pt）
|   |-- enterprise-systems.md   # 大厂设计体系融合（WeUI/AntD/Material 3/Fluent/Arco）
|   |-- premium-aesthetics.md   # 高级风格配方库（10 套方向：情绪/字体/配色/签名/反例）
|   |-- palette-system.md       # 高级配色系统（60/30/10、12 组调色板、色阶与对比度）
|   |-- intent-brief.md          # 意图澄清门：提问纪律与简报模板
|   |-- interface-craft.md       # 层级、字体比例、token 架构、组件检查点
|   |-- craft-floor.md           # 质量底线与绝对禁令
|   |-- ux-intelligence.md       # UX 优先级规则、可访问性、预交付清单
|   |-- image-assets.md          # 开源 SVG + 生图模型 + 可访问性验收
|   |-- final-review.md          # 终审：审美与布局审查
|   |-- motion-3d.md             # Motion/GSAP/Three.js/R3F 与性能红线
|   |-- redesign-audit.md        # 先审计再改、保留规则、现代化杠杆
|   |-- preflight.md             # 最终预检清单
|   `-- platforms/               # 平台最佳范式（小程序 / H5 / App）
|       |-- mini-program.md
|       |-- h5.md
|       `-- app.md
|-- scripts/
|   |-- preflight_check.py       # 零依赖 AI-tell 扫描器
|   |-- palette.py               # 品牌色 -> 50-950 色阶 + 明暗 token + 对比度报告
|   |-- palette_card.py          # token -> 可视化色卡 PNG
|   |-- fetch_svg.py             # 开源 SVG 图库下载（Simple Icons/Tabler/Phosphor/Heroicons/Remix）
|   `-- tests/                   # unittest 测试
`-- assets/
    |-- icon.svg
    `-- templates/design-tokens.json   # 设计 token 起点模板
```

## 质量保证（QA）

```bash
# 扫描生成的页面/组件
python ui-alchemy/scripts/preflight_check.py src/                    # 或具体文件
python ui-alchemy/scripts/preflight_check.py src/ --platform h5      # H5 专属检查（viewport/缩放锁）
python ui-alchemy/scripts/preflight_check.py src/ --platform miniapp # 小程序专属检查（image mode/view tap）
python ui-alchemy/scripts/preflight_check.py src/ --json             # CI 友好输出

# 开源 SVG 图标下载（自动记录许可与 alt）
python ui-alchemy/scripts/fetch_svg.py --source simple-icons --name github --out assets/icons --alt "GitHub logo" --manifest assets/manifest.json
python ui-alchemy/scripts/fetch_svg.py --source tabler --name heart --out assets/icons --manifest assets/manifest.json

# 高级配色：品牌主色一键展开（自动对比度自检）
python ui-alchemy/scripts/palette.py --hex 2B4A33 --accent C98244 --name "Forest Copper" --out design-tokens.json
python ui-alchemy/scripts/palette.py --selftest
python ui-alchemy/scripts/palette_card.py --json design-tokens.json --out palette-card.png

# 自测
python ui-alchemy/scripts/preflight_check.py --selftest
python ui-alchemy/scripts/fetch_svg.py --selftest
python -m unittest discover -s ui-alchemy/scripts/tests
```

硬违规（破折号、纯黑纯白、`h-screen`、scroll 监听、`<div onClick>`、缺 alt、白底白字、`transition: all`）会以非零退出码返回，适合接入 CI 或 pre-commit。<!-- ui-alchemy: ignore -->

---

## 许可证与署名（License & Credits）

本项目 MIT 许可。整合内容分别来自上表所列开源项目（MIT / Apache-2.0），均保留原始版权与署名；完整条款见各来源仓库 LICENSE。本 Skill 是独立整理与再创作，不附带任何原项目的商标或背书。

Made with a lot of taste. No em-dashes were harmed.
