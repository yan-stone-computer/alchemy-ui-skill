# 高级配色系统（Premium Palette System）

<!-- ui-alchemy: ignore-all (this file intentionally documents pure white/black production tokens as scan targets) -->

读于 Phase 1 定色阶段，配合 [premium-aesthetics.md](premium-aesthetics.md) 一起用。目标：**配色不是"选几个好看的颜色"，而是从产品世界提取一个主色，再用工具展开成一整套有温度、有层级、能过对比度的语义 token。**

## 1. 取色来源（先于选色）

主色必须来自产品世界，三条路任选：

- **材质**：木、石、茶汤、金属、布料里真实存在的颜色。
- **场景**：产品被使用时的环境光、背景色。
- **品牌资产**：已有 logo 里的主色。

反例：从"好看"的直觉里随便挑一个亮色；用灰色底 + 一个流行色就完事。

## 2. 12 组验证过的高级调色板（可直接选用）

每组 = 表面(surface) / 主色(primary) / 强调(accent) / 文字(text)。同一产品只取一组，按 60/30/10 使用。

| 名称 | 表面 | 主色 | 强调 | 文字 | 适合 |
|---|---|---|---|---|---|
| 暗夜香槟 | `#171310` | `#C9A86A` | `#8F6B3D` | `#F2EBDE` | 奢华/餐饮/美妆 |
| 雾蓝晨光 | `#F3F6F8` | `#1F3A5F` | `#5B8DB8` | `#1A232B` | SaaS/医疗/工具 |
| 编辑纸墨 | `#F7F3EA` | `#1C1A17` | `#C6402E` | `#1C1A17` | 杂志/文化/叙事 |
| 森野铜光 | `#14231A` | `#2B4A33` | `#C98244` | `#F3ECDD` | 咖啡/香氛/户外 |
| 陶土南意 | `#F7F0E4` | `#C0632E` | `#6B7A45` | `#3A2A20` | 家居/生活方式 |
| 极地冰川 | `#F4F8FA` | `#16283E` | `#3FB6A8` | `#16283E` | 金融/运动/工具 |
| 京都墨彩 | `#F3EEE2` | `#211D18` | `#B23A2A` | `#211D18` | 东方/文化/茶器 |
| 法式公寓 | `#F6F1E7` | `#4A3B32` | `#9CAF9A` | `#4A3B32` | 美妆/家居/社区 |
| 霓虹黑金 | `#0D0F12` | `#35E0C3` | `#FF7A45` | `#C8CFD6` | 潮流/3D/游戏/音乐 |
| 侘寂陶土 | `#F1EBE2` | `#A96B4B` | `#8B8178` | `#3C3A37` | 香氛/器物/疗愈 |
| 松石海岸 | `#EAF4F1` | `#0F6B5C` | `#D9A441` | `#12322B` | 旅行/餐饮/健康 |
| 石墨橙跃 | `#F5F4F2` | `#232A2E` | `#E4572E` | `#232A2E` | 工业/工具/运动 |

## 2b. 大厂体系调色板（来自成熟体系库，第 2 组）

从 [mature-systems-library.md](mature-systems-library.md) 的反解 token 提炼，适合 brief 点名要某大厂气质时直接启用。同样遵守一主一辅一强调，只取一组。

| 名称 | 表面 | 主色 | 强调 | 文字 | 适合 |
|---|---|---|---|---|---|
| 苹果展示 | `#F5F5F7` | `#1D1D1F` | `#0071E3` | `#1D1D1F` | 品牌官网/产品页/3C |
| Stripe 金融紫 | `#FFFFFF` | `#061B31` | `#533AFD` | `#061B31` | 金融/SaaS/开发者平台 |
| Linear 深靛 | `#08090A` | `#F7F8F8` | `#5E6AD2` | `#F7F8F8` | 深色原生工具 |
| Vercel 黑白 | `#FFFFFF` | `#171717` | `#0072F5` | `#171717` | 开发者工具/极简 |
| 微信原生绿 | `#EDEDED` | `#1A1A1A` | `#07C160` | `#1A1A1A` | 小程序/服务 |
| 小红书红 | `#F5F5F5` | `rgba(0,0,0,0.80)` | `#FF2442` | `rgba(0,0,0,0.80)` | 内容社区/种草 |

注意：上表是"主 token"精炼，完整表面阶梯（如 Linear 的 4 层背景、XHS 的透明填充体系）必须回到 mature-systems-library.md 取全。

## 3. 色阶生成（palette.py 已实现）

把主色展开成 50-950 共 10 级色阶 + 语义 token，规则：

- 以主色的色相为锚点，沿 HSL 提亮/压暗：浅端（50-200）接近白但保留色相，深端（800-950）接近黑但保留色相。
- 饱和度随明度向两端递减，避免浅色发灰、深色发闷。
- 自动推导 `on-primary` / `on-accent`（对比度 >= 4.5:1 选深或浅）。
- 同时产出 light / dark 两套语义 token，dark 由 light 镜像映射（surface 取深端、primary 提亮一档）。

命令：

```bash
python ui-alchemy/scripts/palette.py --hex 2B4A33 --accent C98244 --name "Forest Copper" --out design-tokens.json
python ui-alchemy/scripts/palette.py --selftest
```

## 4. 语义 token 命名（全项目统一）

```text
primary / on-primary / primary-container / on-primary-container
accent / on-accent / accent-container
surface / surface-raised / surface-overlay / border / border-strong
text-primary / text-secondary / text-muted
success / warning / danger   （状态色，占 5% 以内）
```

写代码时只许引用 token，禁止散落 hex。

## 5. 对比度自检（palette.py 输出报告）

- 正文 `text-secondary` vs surface >= 4.5:1。
- 大字/按钮 `on-primary` vs primary >= 3:1。
- `text-muted` vs surface >= 3:1（仅用于辅助信息）。
- 不合格自动给替代色并标注。

## 6. 明暗双套

- light：surface 浅、primary 中深、text 深。
- dark：surface 深、primary 提亮、text 浅。
- 强调色在两套里都保持可识别；不靠反色，靠色阶重映射。
