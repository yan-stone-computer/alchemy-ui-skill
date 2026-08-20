# 滚动 3D 电影规格（Scroll Film Spec）

<!-- ui-alchemy: ignore-all (documents exact animation values and banned-pattern examples) -->

读于 brief 要"产品 3D 效果 / 滚动叙事 / 像视频一样的产品展示"时，与 [product-3d-showcase.md](product-3d-showcase.md) 一起用。这是从 Apple 官网手法提炼的**可执行规格**：不写原则，写参数、模板与反模式。

## 0. 定位：这不是动画，是电影

滚动 3D 电影 = 用滚动进度驱动一帧一帧的画面变化，观感像短视频。**核心不是转动的几何体，而是叙事**：开场 → 换肤 → 特写 → 定格，四幕完成一次产品讲述。

## 1. 结构规格（直接照抄）

```text
<section class="film">         高度 = 幕数 x 100vh（4 幕 = 340vh）
  <div class="film-sticky">    sticky top:0; height:100dvh; overflow:hidden
    <div class="film-col">     居中列，width: min(74vw, 620px)
      <div class="film-frame"> 图片卡（圆角 24-32、1px 发丝线、大投影）
        <img>                  主视觉渲染图
      </div>
      <div class="film-cap xN"> 字幕（图片下方，不叠图）
    </div>
    <div class="film-step">     右侧步骤指示（4 个短横条）
    <div class="film-progress"> 底部进度条（3px 渐变）
  </div>
</section>
```

- 幕数：桌面 4 幕封顶，移动端 3 幕封顶（滚动疲劳）。
- 字幕在图片**下方**，不叠加在图上（叠加 = 廉价，且遮挡产品）。
- 主视觉用生图渲染图或真实摄影，禁止程序几何体。

## 2. 参数表（Apple 级手感）

| 参数 | 值 | 说明 |
|---|---|---|
| section 高度 | 幕数 x 100vh（340vh / 4 幕） | 每幕约 85vh 滚动 |
| sticky | top 0，100dvh | 舞台固定在视口 |
| 滚动进度 | `p = -rect.top / (height - innerHeight)` | 0 至 1 |
| 主图 zoom | `1 + p * 1.35` | 开场 100% 到结尾 235% |
| 主图 panY | `p * 8 至 12%` | 缓移，不跳切 |
| 主图 filter | `saturate(1 + sin(p*PI) * 0.18)` | 换肤段的色彩呼吸 |
| 字幕切换 | 4 段边界 [0-0.28, 0.22-0.52, 0.48-0.75, 0.72-1] | 轻微重叠，不硬切 |
| 字幕过渡 | opacity + translateY(14px)，0.45s cubic-bezier(0.23,1,0.32,1) | 淡入淡出 |
| 步骤指示 | 当前段横条 scaleX(1.4) + accent 色 | 3px 高 |
| 进度条 | 底部 3px，`linear-gradient(90deg, accent, accent-2)` | 不抢戏 |

## 3. 驱动实现（禁 scroll 监听）

```html
<script>
var film = document.querySelector(".film");
var filmImg = document.getElementById("filmImg");
var caps = Array.prototype.slice.call(document.querySelectorAll(".film-cap"));
var steps = Array.prototype.slice.call(document.querySelectorAll(".film-step i"));
var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var running = false;

function frame() {
  if (!running) return;
  requestAnimationFrame(frame);
  var rect = film.getBoundingClientRect();
  var total = film.offsetHeight - window.innerHeight;
  var p = total > 0 ? Math.max(0, Math.min(1, -rect.top / total)) : 0;
  if (reduced) p = 1;
  filmImg.style.transform = "scale(" + (1 + p * 1.35) + ") translateY(" + (p * 10) + "%)";
  filmImg.style.filter = "saturate(" + (1 + Math.sin(p * Math.PI) * 0.18) + ")";
  var bounds = [[0, 0.28], [0.22, 0.52], [0.48, 0.75], [0.72, 1]];
  for (var j = 0; j < caps.length; j++) {
    caps[j].classList.toggle("is-on", p >= bounds[j][0] && p <= bounds[j][1]);
    steps[j].classList.toggle("on", p >= bounds[j][0] && p <= bounds[j][1]);
  }
}

new IntersectionObserver(function (entries) {
  entries.forEach(function (en) {
    if (en.isIntersecting) { if (!running) { running = true; requestAnimationFrame(frame); } }
    else { running = false; }
  });
}, { threshold: 0 }).observe(film);
</script>
```

纪律：`transform` + `filter` 都是 GPU 合成属性；无 `transition: all`；离屏即停；`prefers-reduced-motion` 跳终点帧。

## 4. 四幕文案模板（每幕只说一件事）

| 幕 | 进度 | 画面变化 | 文案结构 |
|---|---|---|---|
| 1 开场 | 0 至 25% | 图从 100% 起，字幕 1 淡入 | 卖点 + 一句话证据 |
| 2 换肤 | 25 至 50% | 饱和度升高、轻微 pan，字幕 2 | 材质 / 工艺故事 |
| 3 特写 | 50 至 75% | zoom 推进，字幕 3 | 数据 / 编号细节 |
| 4 定格 | 75 至 100% | zoom 到顶，字幕 4 | 行动召唤 / 金句 |

文案每幕 <= 20 字 + 一句 15 字内的说明；禁破折号、禁假精确数字、禁"Acme"式空名。

## 5. 高级 vs 廉价动效（反模式表）

| 廉价 | 高级 |
|---|---|
| 所有元素同一种入场动画 | 一个作者时刻，其余安静 |
| 每张卡都闪一下 / 逐个发光 | 光效只给主角一次，且裁进圆角 |
| 匀速直线运动 | 非线性缓动 + 非均匀错峰 |
| 滚动监听 + 每帧 setState | rAF 读 scrollY / CSS scroll-driven |
| 转动的几何体当卖点 | 真实渲染图 + 叙事驱动 |
| 字幕叠在图上 | 字幕在图片下方独立区 |
| 0.2s 内硬切样式 | 颜色 / 缩放 / 滤镜连续插值 |
| 转完就停（无收尾） | 定格幕：信息落定后呼吸 1 秒 |

## 6. 验收

- 滚动全程无跳变：每一帧参数连续（用 lerp / 分段 ease，禁 if 硬切）。
- 四张分镜截图逐张 vision 审查：字幕不叠图、无乱码文字、构图平衡。
- 移动端 3 幕内，`100dvh`，无横向滚动。
- reduced-motion 下进度直接等于 1，画面定格在终幕。
