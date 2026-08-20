# 图片资产工作流（Image Assets）：开源 SVG + 生图模型 + 可访问性

图片是前端"像不像真设计"的最大分水岭。本流程由**图片人智能体（image-producer）**执行；没有子智能体环境时，由主智能体按同一套规则直接完成。

## 1. 先定资产清单

从方向阶段产出资产清单，按类型分类：

| 类型 | 首选来源 | 何时用 |
|---|---|---|
| 品牌/产品图标（图标系统） | 开源 SVG 库下载 | 导航、按钮、空态、列表装饰 |
| Logo / 品牌字标 | 用户提供，或简单几何 SVG 原创 | 不得从图库随意冒充品牌 |
| Hero/产品/氛围照片 | 生图模型生成 | 首屏、产品图、生活方式图 |
| 插画/空态插画 | 生图模型或 unDraw 类开源插画 | 空态、引导、错误页 |
| 纹理/背景 | 生图模型或 CSS 原生实现 | 材质、渐变、噪点 |
| 社交证明 Logo | Simple Icons（真实品牌）或生成 monogram | "Trusted by" 区域 |

## 2. 开源 SVG 图库（可访问、可商用优先）

下载前查许可证，优先 MIT / CC0 / 官方许可；写入资产清单并保留来源。推荐源：

| 图库 | 许可 | 说明 |
|---|---|---|
| [Simple Icons](https://simpleicons.org) | CC0 | 品牌 Logo（`https://cdn.simpleicons.org/{slug}`，可加 `/{hex}` 着色） |
| [Tabler Icons](https://tabler.io/icons) | MIT | 线性图标，风格统一，`outline`/`filled` |
| [Phosphor Icons](https://phosphoricons.com) | MIT | 6 种字重，`regular`/`bold`/`fill` 等 |
| [Heroicons](https://heroicons.com) | MIT | 24/20px，`outline`/`solid` |
| [Remix Icon](https://remixicon.com) | Apache-2.0 | 2000+ 图标，线性/填充 |
| [unDraw](https://undraw.co) | 自定义免费许可 | 扁平插画，可自定义主色 |

使用 `scripts/fetch_svg.py` 下载并校验（内容必须是合法 `<svg>`），统一存到 `assets/` 或项目的图标目录，并在 `assets/manifest.json` 记录来源、许可证、用途。

**图标纪律**：一个项目只用一个图标家族；统一 strokeWidth（1.5 或 2.0）；不用 emoji/Unicode 当图标；不手画复杂 SVG 路径。

## 3. 生图模型完善（推荐 text-model-multimodal-skill）

照片、插画、纹理等位图素材，用生图模型按章节尺寸生成。**推荐集成 [yan-stone-computer/text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)（Agnes AI 免费 API，零依赖 Python，自动重试 + 模型降级）**；环境里没有该 skill 时，退而使用可用的 imagegen 工具，或明确告知用户需要真实素材。

### 安装与配置（一次性）

```bash
# 安装 skill（或从仓库复制到 skills 目录）
npx skills add https://github.com/yan-stone-computer/text-model-multimodal-skill

# 配置 API Key（首次必须；key 免费获取：https://platform.agnes-ai.com/settings/apiKeys）
python {TMM_SKILL_ROOT}/scripts/agnes_api.py set-key sk-用户提供的Key
```

`{TMM_SKILL_ROOT}` 为该 skill 的安装目录（如 `~/.codex/skills/text-model-multimodal-skill` 或插件缓存路径）。**未配置 Key 时停下提醒用户，不要硬跑。**

### 常用命令

```bash
# 文生图：主模型 agnes-image-2.1-flash，失败自动降到 2.0-flash
python {TMM_SKILL_ROOT}/scripts/agnes_api.py image \
  --prompt "[主体] + [场景] + [风格] + [光线] + [构图] + [质量]" \
  --ratio 16:9 --size 2K --download

# 图生图/编辑：完善已下载的图（改构图、补细节、换风格）
python {TMM_SKILL_ROOT}/scripts/agnes_api.py image-edit \
  --prompt "把这张产品图换成暖色背景，保持主体不变" \
  --image "本地路径或公开URL" --download

# 识图质检：让模型检查生成图的构图/文字/违和点
python {TMM_SKILL_ROOT}/scripts/agnes_api.py vision \
  --prompt "检查这张图：构图是否平衡、有无乱码文字、主体是否清晰" \
  --image "本地路径"
```

尺寸参考：Hero `16:9` 或 `3:2`（2K）；产品图 `1:1`（2K）；竖版 `9:16`（移动端首屏）；插画 `4:3`。

### 生图纪律

- 为每个章节生成**专属**图，而不是一张图全站复用；宁缺毋滥。
- 生成后必须 `vision` 质检：拒绝乱码文字、AI 畸形、离题构图、非法内容；不合格重生成一次，仍不合格换方案。
- 提示词结构：主体 + 场景 + 风格 + 光线 + 构图 + 质量要求；一次一个主体。
- 产物转 WebP/AVIF + 压缩；`width`/`height` 或 `aspect-ratio` 预留空间防 CLS。

## 4. 回退方案（不许空手交差）

- 没有生图能力：Hero 等关键位用 `https://picsum.photos/seed/{描述性种子}/{w}/{h}` 占位，并在交付说明里列出"需要真实图片的位置"。
- 图标库下载失败：用同一家族的备选库；仍失败才允许内联手写简单几何 SVG（正方形/圆/字母 monogram），复杂图标禁止手画。
- 品牌 Logo：用户不提供且不能虚构时，用明显占位并标注。

## 5. 可访问性验收（每条都查）

- `<img>`：有 `alt`（内容图描述内容；装饰图 `alt=""`）+ `width`/`height` + `loading="lazy"`（首屏图 preload）。<!-- ui-alchemy: ignore -->
- 内联 SVG：`role="img"` + `<title>`（或 aria-label）；装饰性 SVG `aria-hidden="true"`。
- 图片上不叠加信息性文字（无衬底文字不可读）；有衬底/遮罩的需过对比度。
- 颜色不只承担信息（图例、状态加图标/文字）。
- 版权与许可记录在 `assets/manifest.json`，可追溯。
