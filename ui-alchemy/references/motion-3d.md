# Motion & 3D: purposeful animation, WebGL scenes, and performance

<!-- ui-alchemy: ignore-all (this file intentionally documents banned patterns like transition: all as scan targets) -->

Read this for `animate`, `delight`, `overdrive`, and `optimize` work, and any task with scroll choreography, 3D scenes, or interactive WebGL. Distilled from taste-skill's canonical skeletons and the claudedesignskills 3D/motion collection.

## Motion principles

- **Motion must be motivated.** Before adding any animation, answer: what does this communicate? Valid: hierarchy (drawing attention), storytelling (revealing in sequence), feedback (acknowledging action), state transition (showing change). Invalid: "it looked cool".
- **Motion claimed = motion shown.** If `MOTION_INTENSITY > 4`, the page must actually move (entry transitions, scroll reveal, hover physics). If you cannot ship working motion in scope, drop the dial to 3 and ship clean static.
- **One authored moment, not scattered effects.** An orchestrated sequence lands harder than ten independent animations; extra animation reads as AI-generated.
- **Duration < 300ms** for UI; exponential ease-out, never ease-in; press feedback `scale(0.97)`.
- **Animate only `transform` and `opacity`** (GPU-composited). Never `transition: all`, never animate width/height/margin/padding. <!-- ui-alchemy: ignore -->
- **Reduced motion is mandatory** above `MOTION_INTENSITY > 3`: `useReducedMotion()` / `@media (prefers-reduced-motion: reduce)`. Infinite loops, parallax, scroll-hijack, and magnetic physics collapse to static/instant.
- **Hard bans:** `window.addEventListener("scroll", ...)`, custom `scrollY` math in React state, `requestAnimationFrame` loops touching React state. Use Motion `useScroll()`/`useMotionValue`, GSAP ScrollTrigger, IntersectionObserver, or CSS scroll-driven animations (`animation-timeline: view()`). <!-- ui-alchemy: ignore -->
- **Do not mix GSAP/Three.js with Motion in the same component tree**; they fight over the same frames. Pick one driver per surface.

## 动画决策框架（来自 Emil Kowalski 设计工程哲学）

写任何动画代码之前，按顺序回答三个问题：

### 1. 这个该动吗？

| 用户看到频率 | 决策 |
|---|---|
| 每天 100+ 次（快捷键、命令面板） | 永不动画 |
| 每天几十次（hover、列表导航） | 删掉或大幅削减 |
| 偶尔（弹层、抽屉、toast） | 标准动画 |
| 罕见/首次（引导、庆祝） | 可以加 delight |

**键盘触发的动作永不动画。** 高频动作的动画只会让界面显得慢。Raycast 没有开关动画，那就是每天用几百次的工具的最佳体验。

### 2. 目的是什么？

每个动画必须能回答"为什么动"。合法目的：空间一致性（toast 同一方向进出）、状态指示（按钮形态变化）、解释（营销动画展示工作原理）、反馈（按下缩放确认）、防止突兀变化（无过渡的出现/消失像坏了）。
如果答案是"好看"且用户会经常看到，不做。

### 3. 用什么缓动？

- 元素进入/退出 → ease-out（起步快，响应感强）。
- 屏内移动/变形 → ease-in-out（自然加减速）。
- hover/颜色变化 → ease。
- 常速运动（跑马灯/进度条）→ linear。
- **绝不使用 ease-in**：起步慢会让界面显得迟钝，同一个 300ms，ease-in 比 ease-out 感觉慢得多。

内置缓动太弱，用自定义曲线：

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);      /* 强出，UI 交互默认 */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* 强入出，屏内移动 */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* iOS 抽屉曲线 */
```

曲线资源：easing.dev / easings.co 找强化的自定义变体，不要从零造。

### 输出格式（评审 UI 时强制）

评审 UI 动画时用 Before/After/Why 三列表格输出，一行一个问题，不用散落列表：

| Before | After | Why |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms ease-out` | 精确到属性，避免 all |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` | 真实世界的东西不会凭空出现 |
| 弹层用 `ease-in` | `ease-out` 自定义曲线 | ease-in 起步慢，反馈感差 |
| 按钮没有 `:active` | `transform: scale(0.97)` | 按钮必须对按压有反应 |
| 弹层居中缩放 | 从触发点 `transform-origin` 缩放 | 弹层从触发器长出来，模态保持居中 |

## 高级动效基准（Apple 级 vs 廉价）

动效的高级感来自**时间层级、响应感与材质感**，不是动画数量。

### 时间层级（一张表定全场）

| 场景 | 时长 | 曲线 |
|---|---|---|
| 按钮按下 / hover | 100 至 180ms | ease-out |
| 弹层 / 抽屉 / toast | 200 至 300ms | `cubic-bezier(0.23,1,0.32,1)` |
| 页面入场 / section reveal | 400 至 600ms | 同上，stagger 40 至 80ms |
| 滚动叙事（scroll film） | 由滚动进度驱动 | 连续插值，无固定时长 |
| 品牌定格 / 收尾 | 600 至 1000ms | 对称 ease-in-out |

### Apple 级动效三特征

1. **响应感**：交互反馈 180ms 内完成（按压缩放、hover 变色），操作后世界立刻回应。
2. **材质感**：动效模拟真实物理（弹簧、惯性、阻隔），不是元素飞来飞去；入场从近到远，退场收敛到触发点。
3. **层级感**：同屏动效有主次。主角一个完整动作弧（起-承-落），配角静止或微动；全场只有一个作者时刻。

### 廉价动效红线（命中即删）

- 同一入场动画用在每个 section（千篇一律 = AI 味）。
- 逐卡闪烁 / 群发发光：光效只给主角一次，且裁进圆角边界。
- 匀速直线运动：速度必须来自加速度（非线性缓动 + 错峰）。
- 键盘触发动作加动画（高频操作动画 = 迟钝感）。
- 转完就停没有收尾：关键信息落定后留 1 秒呼吸。
- 与内容无关的炫技（无动机动画一律删）。

## Library choice

- **Motion (`motion/react`)** - default for UI, bento, state-change motion, drag, layout animations, `whileInView` reveals. Import from `motion/react`; isolate in client-leaf components with `'use client'` (Next.js) and `useReducedMotion()`.
- **GSAP + ScrollTrigger** - full-page scrolltelling, pinning, horizontal pans, scrubbed sequences. Isolate in dedicated leaf components with `gsap.context()` and cleanup (`ctx.revert()`).
- **Three.js / React Three Fiber** - canvas backgrounds, 3D product viewers, immersive scenes.
- **React Spring** - physics-based gestures (drag, momentum) alongside R3F.
- **Lottie / Rive / Spline / A-Frame / PixiJS / Babylon / PlayCanvas** - only when the brief specifically calls for that medium (vector animation, interactive design tooling, WebXR, 2D canvas games).

### Decision matrix (which stack)

| Use case | Stack |
|---|---|
| Marketing landing with scroll-driven 3D | Three.js + GSAP + React UI |
| React app with interactive 3D product viewer | R3F + Motion |
| Complex timeline-based sequences | R3F + GSAP |
| Physics-based drag/momentum | R3F + React Spring |
| High-performance particle systems | Three.js + GSAP (instancing) |
| Rapid prototyping | R3F + Drei + Motion |
| Game-like physics experiences | R3F + React Spring + physics engine |

## Canonical patterns

### Scroll-reveal stagger (Motion, lightweight)

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function RevealStagger({ items }: { items: string[] }) {
  const reduce = useReducedMotion();
  return (
    <ul className="grid gap-6">
      {items.map((item, i) => (
        <motion.li
          key={item}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.6, delay: i * 0.06, ease: [0.16, 1, 0.3, 1] }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```

Use this for feature lists, testimonial grids, logo walls. Save GSAP for actual pin/scrub work.

### GSAP sticky-stack (pin cards on scroll)

Critical points: `start: "top top"` (not `"top center"`), `pin: true`, every card except the last is pinned, the scale/opacity transform is driven by the NEXT card's trigger, `pinSpacing: false`, wrap in `gsap.context()` and `ctx.revert()` on cleanup. If `useReducedMotion()` is true, skip entirely.

### GSAP horizontal-pan (vertical scroll -> horizontal slide)

Critical points: `trigger: wrap`, `start: "top top"`, `end: () => "+=" + (track.scrollWidth - window.innerWidth)`, `pin: true`, `scrub: 1`, `invalidateOnRefresh: true`. The wrapper is pinned; the inner track slides horizontally.

## Three.js essentials

Core pieces: Scene, Camera, Renderer (WebGL or WebGPU), Geometry, Material, Mesh. Scene graph: `Scene -> Camera / Lights / Meshes / Groups`.

Performance and correctness:

- **Reuse geometry and materials**; use `InstancedMesh` for hundreds/thousands of repeated objects.
- **Dispose resources**: `geometry.dispose()`, `material.dispose()`, `texture.dispose()`, `renderer.dispose()` on unmount/tear-down. Never create geometry inside the animation loop.
- **Animation clocks**: use `THREE.Clock` with `getDelta()` for frame-independent motion; never per-frame `new` allocations.
- **Camera**: FOV 45-75, near as far as possible, far as close as possible, always update aspect ratio + projection matrix on resize.
- **Shadows**: enable on renderer, lights, and meshes; keep shadow maps small and only where needed.
- **Z-fighting**: increase near, decrease far, avoid coplanar surfaces, or use `polygonOffset`.
- **Color space**: `texture.colorSpace = THREE.SRGBColorSpace`, `renderer.outputColorSpace = THREE.SRGBColorSpace`.
- **Textures**: power-of-two dimensions, mipmaps for minification, consider atlases.
- **LOD** for distant detail; frustum culling works when bounding spheres are correct (`computeBoundingSphere()`).
- **Materials**: MeshStandardMaterial (PBR) is the recommended default; MeshPhysicalMaterial for clearcoat/transmission; MeshLambertMaterial for cheap mobile; MeshBasicMaterial for unlit/UI.

## React Three Fiber essentials

- `<Canvas>` wraps the scene; components are declarative (`<mesh><boxGeometry/><meshStandardMaterial/></mesh>`).
- `useFrame((state, delta) => ...)` for per-frame logic; NEVER call React `setState` inside `useFrame` (re-renders the tree every frame; use refs/mutable values).
- `useThree` gives scene/camera/size inside Canvas only; `useLoader` + Drei's `useGLTF` for glTF models with cache; `Suspense` around heavy assets.
- Drei helpers: `OrbitControls`, `Environment`, `Text`, `Center`, `Html`, `ScrollControls`.
- Performance: on-demand rendering (`frameloop="demand"` when static), instancing, LOD, `AdaptiveDpr`, `AdaptivePerformance`, selective re-renders, dispose resources, lazy-load everything below the fold.
- Integration: with GSAP, drive R3F refs from a GSAP timeline (never both fighting over the same object's transform); with Motion for DOM overlays and state; with Zustand for shared 3D state (selectors to avoid re-renders).

## Scroll performance rules

- `will-change: transform` only on elements that actually animate.
- Debounce custom resize logic; `ScrollTrigger.refresh()` after DOM changes; `invalidateOnRefresh` for values that change on resize.
- Register GSAP plugins (`gsap.registerPlugin(ScrollTrigger)`) once; never nest ScrollTriggers inside individual tweens of a timeline (put it on the parent timeline).
- Multiple tweens on the same element: use `fromTo` or a single timeline; two `gsap.to` calls on one element fight.
- Lazy-load Three.js/Motion bundles; grain/noise filters only on fixed `pointer-events-none` pseudo-elements; document a z-index scale and never spray arbitrary `z-50`.

## WebGPU note

WebGPU is a modern alternative to WebGL (three.js supports it). Use TSL for shaders when the brief demands WebGPU; verify browser support and provide a WebGL fallback. Treat it as an enhancement, not a requirement.
