# 产品 3D 展示专场（Product 3D Showcase）

<!-- ui-alchemy: ignore-all (this file intentionally documents banned patterns and production tokens as scan targets) -->

读于 brief 涉及"产品 3D 效果 / 3D 产品页 / 产品宣传视频 / 3D mockup"时，配合 [motion-3d.md](motion-3d.md) 一起用。目标：把产品从"一张图"升级为"一个可以转、可以看材质、可以进视频的 3D 专场"，并把生图、3D 模型生成、视频渲染串成一条流水线。

来源：video-shotcraft（产品视频八阶段流水线与判例式审美）、Meshy / Hyper3D Rodin 官方 3D 生成 skill、Blender product-polish 产品精修、genjutsu 创意编码交互论、openvid 3D mockup。

## 0. 先选档位（三档，按预算与平台选）

| 档位 | 交付物 | 成本 | 适用 |
|---|---|---|---|
| A 网页实时 3D | Three.js / model-viewer 内嵌可旋转产品 | 低 | H5 / 官网 / 小程序 WebView |
| B 真 3D 资产 | AI 生成 glb + Blender 精修 + 网页/APP 嵌入 | 中 | 需要材质真实感的电商/产品页 |
| C 产品视频 | AI 视频生成或 Remotion 程序化动画 | 高 | 营销片 / 广告 / 社媒 |

规则：**先定档位再开工**。档位 B 的模型可以作为 C 的素材；档位 A 不需要先做 B。预算或平台受限时，档位 A 用 CSS 3D / 轻量 WebGL 也可以成立，但"转得起来 + 有光照 + 有材质"三条底线不能少。

## 1. 档位 A：网页实时 3D（默认首选）

### 实现选型

- **Three.js（CDN 或 npm）**：默认。产品展示标准件：`OrbitControls` 拖拽旋转 + `Environment` 环境光 + `MeshPhysicalMaterial` 物理材质。
- **model-viewer**：无需写 WebGL，glb 直接拖入，AR 能力白送。适合已有模型、只想快速嵌入。
- **CSS 3D transforms**：离线零依赖的最后手段，适合几何简单（瓶/罐/盒）的展示；必须真 3D 透视，禁止"伪 3D 的 hover 倾斜卡片"冒充。
- 原生端：小程序用 threejs-miniprogram 适配层或 web-view；Android Compose 用 SceneView / OpenGL 封装；鸿蒙用 XComponent 接 3D 引擎。

### 场景清单（产品 3D 专场最少要有的东西）

1. **可旋转主体**：拖拽或自动环绕，速度可控，`prefers-reduced-motion` 下只保留静态初始角。
2. **三点布光**：主光 + 补光 + 轮廓光，材质高光必须来自真实光源，禁止环境贴图糊一层假光泽。
3. **地面/接触感**：软阴影或反射面，产品不能"悬浮在渐变里"。
4. **材质叙事**：金属有 roughness/metalness 区分，玻璃有 transmission，布料有 sheen；同一个产品只讲一种材质故事。
5. **UI 协调**：3D 画布用产品 token 的底色和文字覆盖层；加载态有占位和进度，WebGL 不可用时回退到产品图。
6. **性能**：60fps 或降级；移动端限制像素比 2x；离屏后才暂停动画循环。

## 2. 档位 B：AI 生成 3D 资产 + 精修

### 生成（二选一，API 模式）

**Meshy**（api.meshy.ai）：
- 文本转 3D / 图片转 3D / 纹理生成 / 绑定与动画，任务 1 至 5 分钟，轮询直到完成，99% 后 30 至 120 秒正常。
- 产出 glb/fbx/obj 等，按项目建目录 `meshy_output/{时间戳}_{prompt}_{id}/`，记录 metadata 与 history。
- 3D 打印需求走专门的打印参数（target_formats 含 3mf），不要用通用生成流程。

**Hyper3D Rodin**（developer.hyper3d.ai）：
- 图片转 3D（最多 5 张输入图）、文本转 3D；输出 glb/usdz/fbx/obj/stl。
- 提交 → 轮询 → 下载三步，下载链接 10 分钟过期。
- 档位选择：低档快速原型，高档生产级几何与纹理。

通用提示词纪律（两个平台一致）：
- 给材质词，不给风格词：说"哑光陶瓷、铜色边缘氧化、表面细磨砂"，不说"好看、高级、炫酷"。
- 给体积与比例锚点："瓶身 8 厘米高、口径 3 厘米、底部圆角 2 毫米"。
- 多角度参考优先：有产品实拍图时走图片转 3D，比文本描述稳一个数量级。
- 生成完先看线框/法线/UV 贴图，再谈渲染；几何破面比贴图丑更致命。

### 精修（Blender product-polish 模式）

1. 导入 glb/gltf，清掉 AI 导出自带的噪点法线/粗糙贴图（会形成点状反光）。
2. 材质改玻璃感：roughness 接近 0、clearcoat 1.0、高 IOR；或按产品真实材质调。
3. 四灯布光：主光 350W + 补光 250W + 轮廓光 250W + 反弹光 100W。
4. 预设三档：studio 平衡 / dramatic 强主光少补光 / soft 全向柔光。
5. EEVEE 实时渲染优先（不出采样噪点），最终出图再上 Cycles。
6. 导出 glb 时确认贴图内嵌或路径正确，模型文件 < 5MB（移动端预算）。

## 3. 档位 C：产品视频（八阶段流水线）

### 流水线（video-shotcraft 提炼）

1. **产品理解与约束**：用途、受众、核心卖点、必须展示的功能、时长/画幅/语言、数据口径。敏感数据一律虚构/脱敏。
2. **视觉方向与 styleframe**：最多 3 个文字方向，每个附动效性格 tokens；选一个后用纯 HTML/CSS 做 2 至 3 张 1920x1080 静态关键帧，先锁色板/字体/光感，再写第一行动画代码。
3. **功能到镜头映射**：每个卖点对应一个镜头，不为凑时长加空镜头。
4. **分镜与制作放行**：分镜表 = 时间 | 镜头 | 关键动效 四列；确认后不重开业务问题。
5. **最终素材采集**：复刻既有页面必须真实截图（整页 + 元素级抠图 + 坐标），手搓 UI 只用于页面上不存在的独立展示件，且质量过出版级。
6. **逐镜头实现**：每镜头渲染静帧肉眼验收，版本归档 `out/qa/`。
7. **声音设计**：BGM 先按节奏分析再卡点；无指定时由产品与发布场景选型。
8. **独立终检**：对照审美准则逐条自检，输出编号式报告，再交付。

### 品牌→动效参数推导表（不凭手感挑 easing）

先把品牌放到两根轴上：**能量轴**（低 = 沉稳/premium ↔ 高 = 运动/娱乐）与**调性轴**（严肃 ↔ 活泼），再从最近预设起步：

| 预设（品类） | 主时长@30fps | 入场 easing | 过冲 | squash |
|---|---|---|---|---|
| 专业信赖（fintech/B2B） | ~21f | bezier(0,0,0.2,1) | 1.0 不弹 | 0 |
| 精致高端（奢侈品/时尚） | ~48f | bezier(0.4,0,0.6,1) | ≤1.02 | 0 |
| 活力大胆（体育/游戏） | ~18f | bezier(0.16,1,0.3,1) | 1.12 | 0.25 |
| 活泼愉悦（消费/社交） | ~27f | bezier(0.34,1.56,0.64,1) | 1.08 | 0.18 |
| 平静关怀（健康/教育） | ~42f | 对称 ease-in-out | 1.0 | ≤0.04 |
| 亲和友好（小微/社区） | ~26f | bezier(0.25,0.46,0.45,0.94) | 1.04 | 0.08 |

自检两条：①三个词描述成片动效，与品牌词对得上吗；②同一套 tokens 同时管入场/转场/hold，一个品牌一种动效嗓音。

### 判例式审美准则（每条违反必须写进项目说明）

**节奏 R**：
- R1 关键信息落定后必须呼吸，品牌字标 hold 满 1 秒；停顿给品牌/关键信息，不随手给普通卡片。
- R2 速度来自加速度不是匀速：批量入场用"越来越快"的硬加速节拍（如发牌隐喻），满板后静止 0.5 秒再切下一拍。
- R3 初版默认放慢一档：主体动作弧 ≥ 3 秒，交互演示按真人操作速度。

**质感与运镜 Q**：
- Q1 复刻既有页面必须真实截图，数据按确认口径处理，敏感内容先虚构/脱敏。
- Q2 3D 透视下的 UI 纹理按显示尺寸 2 至 4 倍栅格化再向下采样；文字发糊先查纹理分辨率链路，不先动相机/景深。
- Q3 产品宣传片默认无手持抖动；相机噪声只在暗场氛围片用极小值。
- Q4 高光/扫光不群发，一个镜头最多给主角一次，且必须裁进圆角边界。
- Q5 开场只给一个主角：单主体 + 完整动作弧（聚光→推近→悬浮→归位），胜过群体群舞。
- Q6 信息密集镜头正视，文字特写侧向水平，风格化倾斜逐镜头验证，禁止全局一刀切。
- Q7 物件特写四件套：侧面倾斜角 + 可感知高度 + orbit 环绕 + 反差深色材质背景。

## 4. 生图 + 3D + 视频的串接

推荐链路（无 GPU 也能走通）：

1. **生图定锚**：用生图模型（推荐 [text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)，Agnes AI 免费 API）先出产品概念图/场景图，锁定色板、材质、光感。图片转 3D 比文本转 3D 稳。
2. **生成 3D 资产**：Meshy 或 Rodin 图片转 3D，出 glb。
3. **精修出片**：Blender product-polish 布光精修，或直接在网页 Three.js 里用环境光渲染。
4. **视频成片**：需要真视频时，优先用 AI 视频生成（Kling / Veo / Seedance / 可灵等，见 mult-modal skill 接入方式）把 3D 静帧变成运镜视频；需要精确动效时用 Remotion 程序化动画，走第 3 节流水线。
5. **四端落地**：glb 同一份资产，H5 用 Three.js，小程序用适配层或 web-view，Android 用 SceneView，鸿蒙用 XComponent。

## 5. 真实贴图策略（告别假材质，先下载再渲染）

程序化纯色材质是"3D 看起来很假"的第一大原因。真实感 = 真实 PBR 贴图，按以下顺序获取：

### 下载来源（全部 CC0 / 可商用）

| 来源 | 地址 | 说明 |
|---|---|---|
| ambientCG | https://ambientcg.com | CC0，金属/木材/织物全套 PBR，1K 约 2 至 4MB，zip 内含 Color/Normal/Roughness/Metalness/Displacement |
| Poly Haven | https://polyhaven.com/textures | CC0，电影级贴图，需按资产构造下载 URL |
| three.js 内置 | three.js 仓库 `examples/textures/` | 含 `pbr/Scratched_gold`（法线）、`carbon`、`floors` 等，raw.githubusercontent 直链 |

### 使用纪律

1. **全套贴图，不用半套**：color + normal + roughness + metalness 一起上，只上 color 会像贴纸。
2. **贴图必须真实下载**：先查 ambientCG / Poly Haven / three.js 内置，下载失败才允许 CanvasTexture 程序化生成（拉丝、划痕、标签文字可程序化，但主材质优先真实贴图）。
3. **标签/文字用 CanvasTexture 叠层**：品牌名、批次号、刻度线画在 1024 或 2048 canvas 上，叠加到罐身，比建模文字便宜且清晰。
4. **记录来源**：贴图文件与 URL 写进 `assets/manifest.json`，标注 CC0 许可。
5. **尺寸预算**：1K 贴图移动端足够；罐身 + 标签 + 地面最多 3 张贴图，单张 < 1MB（压缩后）。
6. **UV 对齐**：圆柱罐身 UV 默认环绕，标签贴图要按 2:1 画布设计，文字在中心带，上下留材质区。

## 6. 滚动驱动 3D 叙事（scroll-driven product film）

把 3D 展示从"一个能转的罐子"升级为"像视频一样每滑一段换一种样式的电影"。这是 Apple / Stripe 官网的成熟产品改造手法。

### 结构

```text
sticky 3D 舞台（视口中央固定，高度 100vh）
滚动容器高度 = 场景数 x 100vh（每个场景一段滚动）
滚动进度 -> 3D 变换参数（旋转 / 材质 / 配色 / 相机 / 粒子）
每段叠加字幕文案，随进度淡入淡出
```

### 场景节奏（4 段为例）

| 段 | 进度 | 3D 变化 | 文案 |
|---|---|---|---|
| 1 入场 | 0 至 25% | 罐子从远到近、旋转 360°、铜色拉丝金属 | 名字/卖点 |
| 2 换肤 | 25 至 50% | 材质与配色整体切换（铜到墨黑金），相机左移 | 工艺/材质故事 |
| 3 特写 | 50 至 75% | 罐身放大、标签纹理清晰、粒子加速环绕 | 数据/编号细节 |
| 4 定格 | 75 至 100% | 回到品牌色，缓停，logo 定格 | CTA |

### 实现纪律

- **禁 window scroll 监听**：用 IntersectionObserver 检测 sticky 舞台进出，在 rAF 循环里读 `scrollY` 计算进度；或 CSS scroll-driven animations（`animation-timeline: view()`）。
- **材质切换用 lerp 过渡**：颜色、roughness、metalness 全部连续插值，禁止硬切（硬切=幻灯片，不叫电影）。
- **每个场景只变 2 至 3 件事**：材质 + 相机 + 文案，不要同时变 5 件事。
- **`prefers-reduced-motion`**：进度直接跳到终点帧，不做连续动画。
- **移动端**：sticky 高度 100dvh；场景数 3 段封顶，避免滚动疲劳。

## 7. 成熟产品改造清单（从"假"到"引人入胜"）

对 3D 展示逐条打勾，全绿才算改造完成：

- [ ] **真实贴图**：color/normal/roughness/metalness 全套，来自真实下载或高保真程序化生成；无纯色塑料感。
- [ ] **环境反射**：scene.environment + environmentIntensity，金属有可读的反射层次。
- [ ] **接触与 AO**：接触阴影 + 环境光遮蔽，产品"站"在地上而不是"飘"在空中。
- [ ] **运镜叙事**：有开场、有变换、有特写、有定格，不是静止一镜。
- [ ] **引人入胜**：至少一个 wow 时刻（材质切换、粒子爆发、360 环绕、光影变化），一段滚动一个变化。
- [ ] **平台原生**：H5 真 WebGL；小程序用原生动画做 3D 感卡片（rotateY/scale/渐变切换）；Android 用 Compose GraphicsLayer rotateY + Canvas 圆柱渐变；鸿蒙用 ArkUI 动画 + Canvas 同构方案。
- [ ] **降级完整**：无 WebGL、无 JS、reduced-motion 都有退路，不出现白屏。
- [ ] **性能达标**：60fps，移动端 pixelRatio <= 2，离屏暂停。

## 8. 交互论（genjutsu cast 提炼）

- **没有验证过的 interaction thesis 不写代码**：先说清这个 3D 场景"让用户感觉到什么"，再实现。
- **复杂度匹配范围**：一个 hover 效果不配 GSAP + ScrollTrigger 流水线；原生 API 能做的先用原生。
- **60fps 或降级**：移动端优先，动画循环离屏即停。
- **展示先行**：动效和颜色不能被一句话描述批准；首次视觉门时问用户"Artifact 实时页 / 项目内预览 / 对话内描述"三种看法，选定后整场不变。

## 9. 真实资产优先铁律（程序化=占位，交付必须真实）

程序化几何体 + 假环境是"3D 看起来很假"的根因。**代码生成的圆柱 + 球 = 玩具，不是产品展示。** 交付级 3D 必须逐项替换为真实资产：

### 9.1 环境（HDRI，第一步）

- 下载 CC0 HDRI：Poly Haven（https://polyhaven.com/hdris），studio 类环境最适合产品展示。
- 直接下载 URL 模式：`https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/1k/<asset>_1k.hdr`（jpg 版本需从资产页确认路径）。
- .hdr 在浏览器加载需要 RGBELoader（ESM）；UMD 环境可先用脚本把 HDR 转成 tone-mapped equirect JPG（Radiance RGBE 解码 + Reinhard 色调映射），再用 `PMREMGenerator.fromEquirectangular` 加载。
- **异步陷阱**：`TextureLoader.load` 是异步的，回调触发前 `texture.image` 为 null，直接调 `fromEquirectangular` 会抛错中断整段初始化。环境贴图必须在 load 回调里设置。

### 9.2 模型（禁止"圆柱+盖子+球钮"式程序玩具）

- 优先真实 glb 模型：Khronos glTF Sample Models（CC0，含 WaterBottle / Avocado / ToyCar 等产品级模型）、Sketchfab CC0、厂商资产库。
- 必须程序建模时用 `LatheGeometry` 画真实轮廓（底部卷边、收腰、肩部、罐口台阶、盖檐），配 64 至 96 段分段；不要裸 `CylinderGeometry`。
- 模型/轮廓要经 vision 审查确认"有真实产品轮廓"，不是"几何体"。

### 9.3 贴图

- color/normal/roughness 全套真实贴图（ambientCG / Poly Haven / three.js 内置）。
- **color 通道会污染 tint**：灰蓝金属贴图乘铜色 tint 永远偏冷偏灰。金属色不靠贴图 color 乘色，用程序生成的品牌色拉丝纹理做 color，真实贴图只提供 normal/roughness 细节。
- metalnessMap 若为纯黑会把材质金属性归零（哑光塑料感），metalness 直接用常量并保留 map 只做细节。
- 标签/品牌纹理用生图模型生成（推荐 [text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)），再叠加到模型，比 Canvas 文字真实一个数量级；生图前用 vision 验证文字拼写。

### 9.4 平台落地

- H5：Three.js 或 model-viewer，本地文件必须走 http 服务器（file:// 下 WebGL 纹理被 CORS 拦截，整段初始化静默失败）。
- 小程序：原生 swiper + rotateY/scale 3D 卡片（当前页回正放大，两侧倾斜），不要硬塞 WebGL。
- Android：Compose `HorizontalPager` + `graphicsLayer { rotationY; cameraDistance }`，跟手 3D 是官方最佳实践。
- 鸿蒙：ArkUI `Swiper` + rotate/scale 动画同构实现。

### 9.5 验收（交付前 vision 审查 + 自检）

- vision 逐项审查：罐型轮廓 / 材质反射 / 标签可读 / 阴影落地 / 无穿模 / 整体质感，每项必须"达标"或给出明确改进项。
- 自检清单：真实 HDRI 已加载（不是程序平面墙）、模型有轮廓细节、贴图全套、生图标签、换肤连续插值、reduced-motion 降级、离线回退。

## 10. Apple 级审美基准与生图渲染图优先（别再出 WebGL 玩具）

**WebGL 程序化几何体（圆柱 + 球 + 程序环境）在消费级展示里永远是玩具，除非模型与材质达到真实渲染级。** 用户要的"3D 效果"是 Apple 官网那种：真实产品渲染图 + 滚动叙事 + 克制动效，而不是转动的几何体。

### 10.1 生图渲染图优先（默认路线）

1. 用生图模型（推荐 [text-model-multimodal-skill](https://github.com/yan-stone-computer/text-model-multimodal-skill)）生成广告级产品渲染图：铜罐/瓶子/产品 + 品牌色背景 + 电影布光 + 漂浮粒子。
2. **提示词必须写 `no other text, no letters, no numbers`**：AI 生图的标签小字必出乱码，vision 审查发现乱码就重画，直到标签干净。
3. 多角度/多配色生成 3 至 4 张，滚动切换 = 视频感 3D，天然真实、零 WebGL 风险。
4. 图内标签区如有瑕疵，用 HTML 覆盖层（精致标签卡 UI）或缩放裁切规避。

### 10.2 Apple 官网设计基准（四端通用）

- **大标题**：Hero 用超大粗体（clamp 46 至 84px / 小程序 76rpx），一行一句，负字距 -0.02em。
- **留白**：section 间距 100px+，图片上下留白充足，宁空勿挤。
- **毛玻璃导航**：吸顶 + `backdrop-filter: saturate(1.4) blur(18px)` + 半透明背景 + 细发丝分隔线。
- **编辑排版**：eyebrow（大写英文 + 0.24em 字距）+ 衬线大标题 + 灰色说明，Apple 式层级。
- **真实摄影**：主视觉用生图渲染图或真实照片，禁止纯色占位。
- **圆角与按钮**：图片卡 22 至 32px，按钮胶囊 999px。
- **克制动效**：滚动 zoom/pan + 字幕淡入淡出，无炫技动画。
- **四端同基准**：H5 同款结构；小程序大标题 + 精致图片卡 + 半透明徽章；安卓大标题 + 大数字统计卡 + 圆角卡；鸿蒙大标题 + 精致节气卡。

### 10.3 交付验收

- vision 审查首屏与每个滚动分镜：标签文字无乱码、构图平衡、无廉价元素。
- 每个端至少一次全页截图审查（H5 浏览器、小程序开发者工具、安卓模拟器、鸿蒙模拟器）。
- 任一端的截图不过 vision 审查 = 该端不算完成，直接重构该端视觉，不交付半成品。
