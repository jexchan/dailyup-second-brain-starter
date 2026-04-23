# 5 分钟快速上手

本文档一步步教你从零把这个 Vault 跑起来。

---

## 前置条件

你需要先装好：

1. **[Obsidian](https://obsidian.md)** — 免费下载
2. **Git** — `xcode-select --install`（macOS）或从 [git-scm.com](https://git-scm.com/) 下载
3. **（推荐）Claude Code / Codex CLI / Cursor** — 用来跑 AI Skills

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

## 第 3 步：填写你的个人上下文

这是**最重要的一步**。花 10–15 分钟认真填写，AI 协作质量会好 10 倍。

编辑 `01_Context/` 下这 5 个文件，把里面的 `<!-- ... -->` 占位替换成你自己的内容：

| 文件 | 填什么 |
|---|---|
| `About_Me.md` | 你是谁、你在做什么 |
| `Mission_and_Vision.md` | 你的长期使命与愿景 |
| `Brand_Voice.md` | 你希望 AI 帮你写作时用什么风格 |
| `Audience_Profiles.md` | 你的内容写给谁看（如果不输出内容可以简写） |
| `Current_Priorities.md` | 你最近 3 个月最重要的事 |

> 💡 **小技巧**：如果一时写不全，先写粗糙版本。这是活文件，以后可以随时更新。

---

## 第 4 步：试跑第一个 AI 技能

打开 Claude Code / Codex / Cursor，在 `my-brain/` 目录下运行：

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

AI 会基于你填好的 `Current_Priorities.md` + `06_Tasks/Inbox.md` + `03_Projects/*/04_Next.md`，生成一份今日聚焦计划。

---

## 第 5 步：创建你的第一张卡片

直接跟 AI 说：

```
帮我建一张 insight 卡片：「早上写作比晚上更高效」
```

`card-creator` 技能会自动：
1. 识别你要的卡片类型（insight）
2. 从 `04_Knowledge/00_Cards/.templates/Insight_Card.md` 取模板
3. 填充内容，保存到 `04_Knowledge/00_Cards/insight_早上写作比晚上更高效.md`

---

## 第 6 步：删除示例内容

最简单的方式——跑内置的初始化脚本：

```bash
bash scripts/init.sh
```

它会交互式地：
- 逐个确认是否删除 `_EXAMPLE_*` 示例文件
- 删除 `_Example_Project/`
- 为今天创建第一篇 Daily Note
- 提醒你去填写 `01_Context/` 五件套

如果你想跳过所有确认一键清理：

```bash
bash scripts/init.sh --yes
```

或者手动删除：

```bash
rm 02_Daily/_EXAMPLE_*.md
rm -rf 03_Projects/_Example_Project
rm 04_Knowledge/00_Cards/_EXAMPLE_*.md
rm 05_References/01_Inbox/_EXAMPLE_*.md
```

也可以把示例留着作为参考，不影响使用。

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
- 确保你的 Claude Code / Codex 版本支持 Skills
- 查看具体 Skill 的 `SKILL.md` 了解调用约定

### 如何让 Vault 多端同步？

推荐两种方式：
1. **Git + 自己的 GitHub 仓库**（免费，版本历史完整）
2. **[Obsidian Sync](https://obsidian.md/sync)**（付费，无缝）

### 可以把这个做成私有仓库吗？

完全可以。License 允许私用、修改、商用。

---

## 下一步

- 读一下 `00_System/` 下的所有规则文件，了解写作和命名规范
- 浏览 `04_Knowledge/00_Cards/.templates/`，看看 22 种卡片模板分别长啥样
- 看 `07_Bases/`，用 Obsidian Bases 插件查看数据库视图
- 浏览 `.claude/skills/` 下的 Skill 定义，按需新增你自己的

---

有问题欢迎提 Issue 或 PR。祝你用得开心。
