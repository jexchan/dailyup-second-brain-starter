# 5 分钟快速上手

本文档一步步教你从零把这个 Vault 跑起来。

---

## 前置条件

你需要先装好：

1. **[Obsidian](https://obsidian.md)** — 免费下载
2. **Git** — `xcode-select --install`（macOS）或从 [git-scm.com](https://git-scm.com/) 下载
3. **（推荐）AI 编码工具** — 跑 Skills 用；作者常用组合：[Codex](https://developers.openai.com/codex/cli/) + GPT-5.5 / [ZCode](https://zcode.z.ai) + [GLM-5.2](https://z.ai/blog/glm-5.2)

---

## 第 1 步：创建你的仓库

### 方式 A：使用 GitHub 模板（推荐）

1. 打开本仓库的 GitHub 页面
2. 点右上角 **"Use this template"** → **"Create a new repository"**
3. 命名（如 `my-brain`），选择 public 或 private
4. 克隆到本地：

```bash
git clone https://github.com/<your-user>/<your-vault>.git my-brain
cd my-brain
```

### 方式 B：直接克隆

```bash
git clone https://github.com/<this-repo>/dailyup-second-brain-starter.git my-brain
cd my-brain
rm -rf .git
git init
git add -A
git commit -m "initial commit from starter"
```

---

## 第 2 步：用 Obsidian 打开

1. 打开 Obsidian
2. 如果是第一次 → **"Open folder as vault"**
3. 选择 `my-brain/` 文件夹
4. Obsidian 会读取 `.obsidian/` 里的配置并打开 Vault

第一次打开可能提示"Trust author and enable plugins?"，可以**先选 No**（后面再决定是否启用第三方插件）。

---

## 第 3 步：运行 `/onboard`

打开你的 AI 编码工具（如 Codex / ZCode），进入 `my-brain/` 目录，然后明确运行：

```text
/onboard
```

它会用一个很短的流程带你完成初始化：

1. 欢迎你并介绍这个第二大脑模板
2. 带你快速浏览核心文件和代表性示例
3. 列出所有模板示例
4. 询问是否清理示例
5. 告诉你接下来可以做什么

只有在你明确确认后，它才会删除 `_EXAMPLE_*` 和 `_Example_Project/`。你也可以先保留示例，之后再次运行 `/onboard`。

> **注意**：`/onboard` 不会创建 Daily Note，也不会替你填写个人资料。
>
> 如果示例已经清理完毕，再次运行 `/onboard` 只会提示初始化已完成。

---

## 第 4 步：填写你的个人上下文

这是**最重要的一步**。花约 10 分钟填写，AI 才能结合你的真实情况协作。

编辑 `01_Context/` 下这 2 个文件：

| 文件 | 填什么 |
|---|---|
| `About_Me.md` | 你是谁、长期方向、AI 协作偏好，以及可选的受众和表达风格 |
| `Current_Priorities.md` | 当前目标、重点、活跃项目、关键问题和暂时不做 |

> **小技巧**：如果一时写不全，先写粗糙版本。这是活文件，以后可以随时更新。

---

## 第 5 步：创建你的第一张卡片

填写上下文后，可以马上试试 `/card-creator`：

```text
/card-creator
```

然后告诉 AI：

```text
帮我建一张 insight 卡片：「早上写作比晚上更高效」
```

它会自动：

1. 识别卡片类型（insight）
2. 读取 `04_Knowledge/00_Cards/.templates/Insight_Card.md`
3. 填充内容并保存到 `04_Knowledge/00_Cards/`

---

## 第 6 步：试跑日常技能

完成初始化后，可以继续尝试下面两个技能：

### 试试 `/session-brief`

让 AI 读懂你的 Vault：

```
/session-brief
```

AI 会读取 `AGENTS.md` / `CLAUDE.md` → `01_Context/` → 最近的 Daily Notes → 当前任务，然后给你一份「当前状态摘要」。

这也是每次开新会话时推荐的第一步。

### 试试 `/today`

```
/today
```

AI 会基于你填好的 `Current_Priorities.md` + `06_Tasks/Tasks.md` + `06_Tasks/Inbox.md` + `03_Projects/*/Project.md`，生成一份今日聚焦计划。

---

## 第 7 步：建立写作习惯

**最小可用的日常工作流**：

```
早上  /today            → 今日聚焦计划
白天  创建 Daily Note + 随时记录进展
      随手创建 insight/quote/book 卡片
晚上  /closeday         → 回顾今天
周末  /weekly-review    → 周度回顾
```

---

## 常见问题

### Obsidian 找不到我刚创建的卡片？

- 检查文件是否在 `04_Knowledge/00_Cards/` 根目录（不要在 `.templates/` 里）
- 尝试 `Cmd+P` → "Reload app without saving"

### Skill 不生效？

- 确保 `.claude/skills/` 和 `.agents/skills/` 在 Vault 根目录
- 确保你的 AI 编码工具（Codex / ZCode 等）版本支持 Skills
- 查看具体 Skill 的 `SKILL.md` 了解调用约定

### 如何让 Vault 多端同步？

推荐两种方式：
1. **Git + 自己的 GitHub 仓库**（免费，版本历史完整）
2. **[Obsidian Sync](https://obsidian.md/sync)**（付费，无缝）

### 可以把这个做成私有仓库吗？

完全可以。License 允许私用、修改、商用。

---

有问题欢迎提 Issue 或 PR。祝你用得开心。
