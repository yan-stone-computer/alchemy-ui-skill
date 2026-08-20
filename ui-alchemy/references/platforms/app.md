# App 最佳范式（Native & Cross-platform App Paradigms）

适用范围：iOS（SwiftUI / UIKit）、Android（Jetpack Compose / View）、React Native、Flutter；含平板、折叠屏、分屏与系统字体缩放。

## 先定方案

| 目标 | 方案 |
|---|---|
| iOS 优先、追求平台原生感 | SwiftUI（新）/ UIKit（存量），遵循 Apple HIG |
| Android 优先、Material 3 | Jetpack Compose，动态配色 + 系统组件 |
| 团队熟悉 React、双端一致 | React Native，平台组件 + `Platform.select` |
| 团队熟悉 Dart / 需要高一致自绘 | Flutter，Material 3 + Cupertino 按平台切换 |

不要为"一套代码"牺牲平台习惯：iOS 用 Tab Bar + Navigation Stack，Android 用 NavigationBar + 返回键（含预测性返回）；组件、触觉、文案随平台。

## 布局、安全区与自适应

- 安全区：SwiftUI `safeAreaInset` / UIKit Safe Area、RN `SafeAreaView`、Flutter `SafeArea`/`MediaQuery.padding`、Compose `WindowInsets`。内容永远不落在状态栏、刘海、挖孔、Home Indicator 之下。
- 支持系统字体缩放（Dynamic Type / fontScale）：用自适应布局与可增长组件，禁止固定高度截断文字。
- 平板与折叠屏：响应式断点（compact / medium / expanded），两栏布局或自适应面板；分屏与旋转不丢状态。
- 密度：Material 8dp 网格；触控目标 44x44pt（iOS）/ 48x48dp（Material）。

## 导航与信息架构

- iOS Tab Bar、Android NavigationBar 均 <= 5 项；次级导航用栈，返回行为符合平台（Android 系统返回键、iOS 边缘右滑）。
- **导航是硬要求**：多页面 App 必须有可见的一级导航（iOS Tab Bar / Android NavigationBar），2-5 项，图标+文字，选中态明确；缺失即未完成。
- 深链接与状态恢复：每个可分享页面有稳定 route/URL scheme；进程恢复不丢关键状态。
- 大标题/工具条跟随平台习惯；不要照搬 Web 的汉堡菜单到 iOS。
- iOS 级打磨：一级页大标题（约 34pt）、圆角分组列表、半透明材质导航栏、44pt 触控目标、`tabular-nums`、iOS 动效曲线（200-350ms）。

## 主题、动效与可达性

- 深色模式跟随系统；语义 token（`onSurface` / `onPrimary` / `surfaceContainer`）而非写死色值。
- 动效遵循平台规范：Material motion / HIG；只动 `transform`/`opacity`（原生为 alpha/位置）；尊重系统减弱动效（`UIAccessibility.isReduceMotionEnabled` / 系统设置），动效时长 < 300ms。
- 可达性：VoiceOver / TalkBack 语义标签（SwiftUI accessibility、Compose contentDescription、RN accessibilityLabel、Flutter Semantics）；触觉反馈（`UIImpactFeedbackGenerator` / `HapticFeedback`）作为确认而非装饰。
- 高对比度、大字体、无色彩依赖的信息呈现（图标+文字）。

## 列表、表单与状态

- 列表虚拟化：`UICollectionView` / `RecyclerView` / RN `FlatList` / Flutter `ListView.builder`；骨架屏或 placeholder 优于转圈。
- 表单：系统键盘类型（`keyboardType` / `inputType`）、自动填充、日期选择用系统组件、错误内联在字段下。
- 状态完整：空 / 加载 / 错误 / 离线；下拉刷新与重试；错误文案说明问题与恢复路径。
- 图片加载用成熟库（SDWebImage / Coil / FastImage / cached_network_image）并处理占位与失败。

## 性能与交付

- 启动路径：主线程无长任务、首帧快、冷启动缓存；列表滚动 60fps（或 120Hz 设备平滑）。
- 内存：页面销毁时释放图片缓存、监听器、动画控制器。
- 跨端注意：RN/Flutter 不要直接调用仅 Web 可用 API；保持 `accessibilityLabel`/`testID` 双端一致；版本与系统差异用能力检测而非版本号硬编码。

## 交付前检查

1. iOS 与 Android 各跑一遍真机/模拟器：安全区、返回、键盘、深色、字体缩放、动效开关。
2. 平板/折叠屏一档；分屏与旋转无状态丢失。
3. VoiceOver / TalkBack 走查核心流程；对比度达标。
4. 弱网、离线、启动性能各验证一次。
