# DailyUp Second Brain Starter

> An opinionated **Obsidian second-brain template**, built from day one for long-term human–AI collaboration.
>
> 一个为**人机长期协作**而生的 Obsidian 第二大脑模板 — 开箱即用，内置规则、模板和 AI 技能。

---

## 这是什么

一套可以直接用的 Obsidian Vault 框架，包含：

- **8 个主目录的信息架构** — 系统规则 / 上下文 / 日记 / 项目 / 知识 / 参考 / 任务 / Bases
- **22 种原子化卡片模板** — insight / book / mentalmodel / person / tool / quote …
- **14 个开箱即用的 AI 技能（Skills）** — `/today`、`/weekly-review`、`/closeday`、`/reading-coach`、`/card-creator` 等
- **完整的 AI 协作规则** — CLAUDE.md + AGENTS.md 让任意支持该协议的 AI 编码工具立刻理解你的知识库
- **Obsidian Bases 数据库视图** — Books、Persons、Resources、Opensource、Subscriptions
- **清晰的写作规范、命名规范和任务管理规则**

核心设计理念：**让知识能长期积累、让 AI 能长期协作**。

---

## 配套视频课程

如果你希望跟着作者**系统化地、从零搭建**这套 AI × Obsidian 第二大脑，作者推出了一份完全基于本开源模板构建的视频课程：

[**《从零构建 AI × Obsidian 第二大脑》**（付费课程）](https://dailyup.xyz/courses/cmqhhefjl0000ps1ynw5gxpto)

模板本身**永远开源免费**，本文档就是你的上手指南（见下方「5 分钟快速上手」）。课程面向想深入理解设计思路、完整工作流与 AI 协作实战的读者，按需选择即可。

---

## 为什么做这个

市面上的 PKM 模板大多有三个问题：

1. **结构混乱** — 随手一分类，越用越乱
2. **没考虑 AI** — 模板为人类读写设计，AI 无从下手
3. **没法长期维护** — 缺少规则，一年后回看全是"遗迹"

本模板的回答：

| 痛点 | 本模板的做法 |
|---|---|
| 信息该放哪里？| `00_System/Vault_Map.md` 给出明确路由规则 |
| AI 怎么理解我？| `CLAUDE.md` + `01_Context/` 的稳定背景与当前重点 |
| 怎么避免重复？| `.templates/` 提供统一模板，所有卡片/项目走同一个骨架 |
| 知识怎么沉淀？| 22 种原子化卡片 + 双向链接构成知识网络 |
| 每天怎么推进？| 内置 `/today`、`/closeday`、`/weekly-review` 三个常用 AI 技能 |

---

## 5 分钟快速上手

详见 [`QUICK_START.md`](./QUICK_START.md)。简要流程：

```bash
# 1. 用这个 repo 作为模板，在 GitHub 上创建你自己的 Vault
#    (点击 "Use this template" 按钮)

# 2. 克隆到本地
git clone https://github.com/<your-user>/<your-vault>.git my-brain
cd my-brain

# 3. 用 Obsidian 打开这个文件夹
#    Obsidian → Open folder as vault → 选择 my-brain/

# 4. 填写你的个人上下文（2 个文件）
#    编辑 01_Context/ 下的 About_Me / Current_Priorities

# 5. 安装 AI 编码工具（推荐 Codex / ZCode），跑第一个 Skill
#    /session-brief   → 让 AI 读懂你的 Vault
#    /today           → 生成今日计划
#    /card-creator    → 创建你的第一张知识卡片
```

---

## 目录结构

```
.
├── 00_System/         # 结构、任务、写作与命名规则
├── 01_Context/        # 全局上下文（你是谁、想做什么、写给谁看）
├── 02_Daily/          # 每日记录（含 Daily Note 模板）
├── 03_Projects/       # 轻量项目管理（单页模板 + 按需产出目录）
├── 04_Knowledge/      # 长期知识沉淀
│   ├── 00_Cards/      # 22 种原子化卡片 + 6 张示例
│   └── 01_Topics/     # 长期主题地图（含 1 个示例主题）
├── 05_References/     # 剪藏消化（Inbox → 卡片/项目/行动 → 精选 Library）
├── 06_Tasks/          # Inbox 捕获 + 非项目任务管理
├── 07_Bases/          # Obsidian 数据库视图
├── Attachments/       # 根目录内容的附件（按需使用）
├── .obsidian/         # Obsidian 配置（已精简）
├── .agents/skills/    # 通用 Agent 技能
├── CLAUDE.md          # AI 协作总导航（Claude 专用）
└── AGENTS.md          # AI 协作总导航（通用，软链到 CLAUDE.md）
```

---

## 内置 AI 技能

> 技能说明见 [`Skills_Manual.md`](./Skills_Manual.md)。当前通用 Agent 技能位于 `.agents/skills/` 下。

| 技能 | 用途 | 触发方式 |
|---|---|---|
| `session-brief` | 读懂当前 Vault 状态 | 开新会话时 |
| `today` | 根据任务和优先级生成今日计划 | "今日计划怎么安排" |
| `closeday` | 日终复盘 | "帮我结束今天" |
| `weekly-review` | 周度回顾与下周规划 | "做个周报" |
| `reading-coach` | 用 ACTOR 框架主动阅读与学习 | "帮我真正学懂这篇内容" |
| `card-creator` | 根据输入自动创建对应类型的卡片 | "帮我建一张卡" |
| `brain-storming` | 围绕一个主题多维度发散 | "头脑风暴 X" |
| `random-thinking` | 跨主题随机抽卡做关联思考 | "给点灵感" |
| `connect` | 连接两个主题，找出桥梁概念 | "连接 X 和 Y" |
| `trace` | 追踪一个主题在 Vault 中的演化 | "追踪 X 的演化" |
| `critical-check` | 对观点/证据/推理做建设性质疑与校验 | "质疑一下这个观点" |
| `check-health` | 检查孤立卡片、失效链接、矛盾观点 | "检查知识库健康" |
| `spaced-review` | 管理知识卡片间隔复习 | "今天该复习什么" |
| `system-sync` | 同步系统说明、README、统计和技能手册 | "同步系统信息" |

---

## Topics 长期主题地图

`04_Knowledge/01_Topics/` 用于维护**长期关注领域的知识地图与阶段性理解**。

- 单个概念、观点、模型 → 放入 `04_Knowledge/00_Cards/`
- 长期领域的综合理解与知识连接 → 放入 `04_Knowledge/01_Topics/`
- 有目标和完成标准的学习 → 放入 `03_Projects/`
- AI 可执行的方法 → 转化为 `.agents/skills/`

主题默认从一个文件开始，不预建复杂子目录。模板保留 `_EXAMPLE_Learning_Science.md` 展示主题地图的写法；初始化个人 Vault 时可通过 `/init` 清理。

---

## 你需要什么

**必备**：
- [Obsidian](https://obsidian.md)（免费）
- Git（用于版本控制和同步）

**强烈推荐** — 才能发挥 Skills 的价值（作者常用的组合）：

| 地区 | 编码工具 | 驱动模型 |
|---|---|---|
| 国外 | [Codex](https://developers.openai.com/codex/cli/) | GPT-5.5 |
| 国内 | [ZCode](https://zcode.z.ai) | [GLM-5.2](https://z.ai/blog/glm-5.2) |

> 本模板基于 `AGENTS.md` / `CLAUDE.md` 通用协议，理论上任何支持该协议的 AI 编码工具（Claude Code、Cursor 等）都能接入；以上只是作者实测顺手的推荐。

**Obsidian 插件**（Core 插件够用，可选增强）：
- Templater — 动态模板变量
- Dataview — 数据库式查询
- Tasks — 任务管理

---

## 它适合谁

- 想认真搭建**长期使用**的第二大脑，而不是玩票
- 已经在用 / 准备用 **AI 编码工具**（Codex / ZCode 等）
- 愿意花 10 分钟填写稳定背景和当前重点，换来更准确的 AI 协作
- 喜欢**文件优先、本地可控**的知识管理方式

它**不**适合谁：

- 只想要一个能用一周的"漂亮模板"
- 完全不打算用 AI 协作（那本模板的一半价值都用不上）
- 只用手机做笔记 —— Obsidian 桌面端体验更好

---

## 如何定制

- **结构**：可以改目录名和编号，但请同步更新 `00_System/Vault_Map.md` 和 `CLAUDE.md`
- **卡片类型**：直接在 `04_Knowledge/00_Cards/.templates/` 添加新类型
- **AI 技能**：在 `.agents/skills/` 下新建目录，写一个 `SKILL.md` 即可
- **规则**：`00_System/` 下的规则都是你的，改即可。改完告诉 AI"请读一下新规则"

---

## 贡献

欢迎提 PR！特别欢迎：

- 新的卡片模板（记得附示例）
- 新的 AI Skills（尤其是跨工具都能用的）
- 翻译（目前以中文为主）
- 使用场景分享

详见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

---

## License

本项目采用**双许可**：

- **代码部分**（Skills、脚本、配置） — [MIT License](./LICENSE)
- **内容部分**（文档、模板、示例卡片和主题地图） — [CC BY 4.0](./LICENSE)

简单说：**自由使用、修改、商用，保留出处就行**。

---

## 相关资源

- **概念来源**：[How to Take Smart Notes](https://book.douban.com/subject/35503571/) — Sönke Ahrens
- **Obsidian 官网**：https://obsidian.md
- **Zettelkasten 方法**：https://zettelkasten.de

---

_Built for people who take knowledge seriously._
