# 八美学锚点（Aesthetic Anchors）

<!-- ui-alchemy: ignore-all (documents exact anchor tokens including pure black/white as scan targets) -->

读于 brief 没有指定风格、需要"一个明确审美地形"时。来自 Ilm-Alan frontend-design 的八锚点方法论：**每个锚点锁定具体 CSS tokens，选一个就全程遵守它**。"Swiss 带点 Brutalist 边"是范畴错误，锚点之间天然互斥。

用法：Context → Anchor → Differentiator（一个签名动作）→ System（tokens 全对上）→ Implementation。内容（字符串）单独自律：不编造假数据、不放无信息填充标签、不用 Unicode 符号代替图标、不写 AI 腔文案。

## 1. Swiss 瑞士国际主义

- 表面：纯白 `#FFFFFF` 或中性 `#F7F7F8`。
- 字体：Akzidenz-Grotesk / Helvetica Neue / Söhne，display 与正文同族。
- 强调：Swiss Red `#E4002B` / International Orange `#FF4F00` / Yves Klein Blue `#002FA7`，只用一个。
- 结构：可见网格线或 1px 发丝线；左对齐 + 不对称平衡；数字（日期/页码）作构图元素。
- **打破即失败**：暖纸色、衬线 display、噪点纹理、居中排版出现。

## 2. Industrial 工业

- 表面：纯黑 `#000000` 或暖黑 `#0B0C0A`。
- 字体：IBM Plex Mono / JetBrains Mono / Berkeley Mono，display 与正文都用 mono。
- 信号色：一个语义色（绿 `#00E676` / 红 `#FF3B30` / 琥珀 `#FFB800` / 酸橙 `#C6FF4A`）。
- 结构：扁平；1px 边框代替阴影；数字 tabular-nums。
- **打破即失败**：衬线、比例字体、暖纸、噪点、装饰阴影、圆角出现。

## 3. Brutalist 粗野主义

- 表面：原色或反原色（`#FF0000` / `#0000FF` / `#FFFF00` / `#000000` / `#FFFFFF`），取 2 至 3 个平等竞争。
- 字体：仅系统字体（Times New Roman / Helvetica / Courier / Arial），故意混用。
- 阴影：硬偏移无模糊 `box-shadow: 8px 8px 0 #000`。
- 控件：原生浏览器样式，不加 CSS。
- **打破即失败**：webfont、调过的 hex、软阴影、圆角、居中布局出现。

## 4. Aurora Maximalism 极光极繁

- 表面：深色饱和渐变（紫 `#5D34D0` → 洋红 `#FF006E` → 青 `#00F0FF`，或蓝紫粉）。
- 字体：Inter Variable / PP Neue Machina / Sharp Grotesk，超大 display（15 至 25vw）。
- 纹理：mesh gradient 是主表面特征；霓虹 `text-shadow` 只作强调。
- 动效：弹簧物理编排、滚动视差。
- **打破即失败**：平底、暖纸、克制、发丝线主导出现。

## 5. Chaotic Maximalism 混乱极繁

- 表面：冲突撞色（粉 `#FF71CE` + 酸黄 `#DFFF00` + 青 `#00FFFF` + 任意第三个）。
- 字体：3 种以上不同寄存器字体故意碰撞。
- 纹理：每个表面都有图案（波浪/圆点/锯齿/棋盘，SVG 或 repeating-linear-gradient）。
- **打破即失败**：统一调色板、单一字体、留白作结构、60/30/10 主导出现。

## 6. Retro-Futuristic 复古未来

- 表面：纯黑 `#0A0014` 或深海军黑。
- 字体：时代专属（VT323 / Orbitron / Space Mono / Monoton / Press Start 2P / IBM Plex Mono）。
- 强调：霓虹对（洋红 + 青 = synthwave；磷光绿 + 琥珀 = terminal）。
- 纹理：CRT 扫描线或色差 `text-shadow`，发光要彻底。
- **打破即失败**：柔和渐变、现代字体、克制的浅色出现。

## 7. Editorial 编辑出版

- 表面：纸白 `#F7F3EA` 族或象牙。
- 字体：强衬线 display（宋体 / Didot / Playfair 类）+ 正文细无衬线。
- 强调：单一高饱和（朱红 / 钴蓝），只出现一次。
- 结构：不对称网格、超大标题、极细分割线；编号只在承载顺序信息时出现。
- **打破即失败**：渐变背景、圆角卡片泛滥、三种以上强调色出现。

## 8. Dark Luxury 暗色奢华

- 表面：深黑棕 `#14100C` 族（带色相的近黑，非纯黑）。
- 字体：衬线 display（思源宋 / Cormorant 类）+ 正文无衬线。
- 强调：金 / 香槟 `#C9A86A`，低饱和使用。
- 结构：大留白 + 单列居中 + 1px 金线分隔；阴影低而柔。
- **打破即失败**：金色渐变文字、描金边框堆满、红金撞色出现。

## 纪律

- **一次只选一个锚点**，全程 token 对齐；跑偏到锚点外 = 未完成。
- 锚点是审美地形，[premium-aesthetics.md](premium-aesthetics.md) 是品牌化配方；两者都要求 60/30/10 与一主一辅一强调。
- 选完锚点后用 [palette-system.md](palette-system.md) 的 palette.py 展开色阶，写代码只用 token。
