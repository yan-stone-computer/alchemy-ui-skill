# 小程序最佳范式（Mini Program Paradigms）

适用范围：微信 / 支付宝 / 抖音 / 百度 / 快手小程序，以及 Taro、uni-app、kbone 等跨端方案编译到小程序的产物。

## 先定方案

- **原生小程序**：单端深度定制、性能最直接可控时选原生（微信 WXML/WXSS/JS）。
- **Taro（React 语法）**：团队熟悉 React、需要多端一致组件模型时选 Taro。
- **uni-app（Vue 语法）**：团队熟悉 Vue、需要快速覆盖 H5 + 多端小程序时选 uni-app。
- 跨端方案用条件编译处理差异（`#ifdef MP-WEIXIN` / `#ifdef H5`），不要为了"一套代码"牺牲单端体验。

## 设计基准与单位

- 设计稿按 **750rpx 宽度**出图；`rpx` 会自动按屏宽缩放（750rpx = 屏宽）。H5 端跨端框架会换算 rpx，注意字体与大图在不同屏宽的观感。
- 关键尺寸用 rpx，安全区用 `env(safe-area-inset-*)`，禁用"写死 px 固定宽度"的做法。
- 组件库优先：WeUI、Vant Weapp、TDesign Mini、NutUI、Ant Design Mini。**优先官方组件**（`button`、`input`、`checkbox`、`slider`），不要用 `<view>` 模拟系统控件，除非有充分理由并补全行为与可达性。

## 页面与导航

- 每个页面四件套：`.json` / `.wxml` / `.wxss` / `.js`；页面级 `json` 配置 `navigationBarTitleText`、`navigationStyle`、`backgroundColor`、`enablePullDownRefresh`。
- 自定义导航栏必须处理胶囊按钮：用 `wx.getMenuButtonBoundingClientRect()` 计算标题与右侧空间，不要遮挡胶囊。
- **导航是硬要求**：多页面商城/工具类小程序必须配置原生 `tabBar`（2-5 项，图标 81x81px，选中/未选中两态），或明确采用自定义导航方案。tabBar 是用户对"我在哪"的第一感知，缺失即未完成。
- 一级页用原生 `tabBar` + `navigationBarTitleText`；二级页保持返回可达；页面栈与返回行为一致，不做"返回后丢失状态"。
- iOS 级打磨：首页大标题（30-36px 字重 700）、卡片圆角 24-32rpx、分组列表组间距大于组内间距、底部固定栏避开安全区、数字用 `font-variant-numeric: tabular-nums`。
- 深色模式：`app.json` 开启 `"darkmode": true` + `theme.json` 变量；用 CSS 变量表达语义色，不要散落写死色值。

## 布局、触控与安全区

- 触控目标：不小于 **88rpx（约 44pt）**，间距遵循 8rpx 倍数网格。
- iPhone 底部 Home Indicator 与刘海：底部固定操作条加 `padding-bottom: env(safe-area-inset-bottom)`。
- 点击态：可点元素必须有反馈（`hover-class`、`button` 默认态或显式 pressed 态）；不要让用户感觉"点了没反应"。
- 动效：优先 CSS `transition`/`transform`；`wx.createAnimation` 只在必须时使用；列表内不做高频动画；尊重系统减弱动效设置（可检测 `wx.getSystemInfoSync()` 的 reducedMotion 字段并降级）。

## 数据与性能（setData 是命门）

- **合并 setData**：多次状态更新合并为一次调用，避免连续高频 setData。
- **数据路径更新**：`this.setData({ 'list[0].name': v })` 而非整对象替换。
- **大数据列表虚拟化**：用 `recycle-view` / `recycle-list` 或分包内虚拟列表，不要渲染几百行 view。
- **分包加载**：主包保持轻量，非首屏页面走分包；图片 `lazy-load` + WebP + CDN + 合理压缩。
- **骨架屏**：首屏/列表加载用骨架屏而非转圈；空态与错误态单独设计，给出恢复路径。
- 长任务与内存：及时解绑监听、页面卸载时清理定时器与动画。

## 可达性与表单

- 标签：`<label for>` 关联控件，禁止 placeholder 当标签；`input` 设置正确的 `type`（`number` / `digit` / `idcard`）、`confirm-type` 与键盘行为。
- 图片：`<image>` 必须显式设置 `mode`（`aspectFill` / `widthFix` / `aspectFit`），避免默认 `scaleToFill` 拉伸；装饰性图片提供空标签语义。
- 纯图标按钮必须配文字或 aria-label 类语义；触控反馈与键盘/读屏提示齐全。
- 错误态：表单错误内联显示在字段下方；网络失败给出重试。

## 交付前检查

1. 750rpx 基准下的关键屏（375pt / 414pt 模拟）全部过一遍，无横向滚动、无遮挡胶囊。
2. `--platform miniapp` 扫描结果清零（含 `<image>` 缺 `mode`、`<view bindtap>` 缺反馈等）。
3. 深色模式、弱网、首屏冷启动各验证一次。
4. 分包体积与首包体积符合平台限制，首屏无大图阻塞。
5. 导航审查：截首页，3 秒内能说出"在哪、能去哪、怎么回去"；tabBar 选中态明确。
