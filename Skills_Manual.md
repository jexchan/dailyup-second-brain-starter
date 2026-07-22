---
description: 本地 AI 技能说明手册
tags: [system, skills, manual]
updated: 2026-07-22
---
# Skills Manual

这份手册说明当前 Vault 自带的本地技能，帮助你知道在什么场景下可以直接对 AI 说什么，以及每个技能会读取哪些内容、产生什么结果、是否会写回知识库。

当前统计口径：按 `.agents/skills/*/SKILL.md` 统计。  
当前本地技能数量：15 个。

---

## 如何使用技能

你不需要记住技能文件路径，只要用自然语言提出需求即可。AI 会根据触发词和任务类型选择合适的技能。

常见说法：

- `/init`（新安装模板时明确运行）
- “帮我生成今天的计划”
- “做一个周回顾”
- “把这段内容创建成知识卡片”
- “检查知识库健康”
- “连接一下 Learning OS 和 Obsidian”
- “追踪一下这个主题是怎么演变的”
- “给我来个随机思考”
- “同步系统信息”

如果你希望结果写入 Vault，请明确说：

- “请写入”
- “请记录到第二大脑”
- “请更新到知识库”
- “请同步系统信息”

默认情况下，很多分析型技能只读不写，避免把未经整理的内容直接写入正式知识库。

---

## 技能总览

| 技能 | 适合场景 | 默认行为 | 主要读取位置 | 可能写入位置 |
|---|---|---|---|---|
| `init` | 首次使用模板，快速导览并清理示例 | 先只读，明确确认后清理 | 新手入口、个人上下文、代表性示例 | 删除模板示例并更新相关 README |
| `session-brief` | 开始一次工作会话，快速恢复上下文 | 只读 | `01_Context/`, `02_Daily/`, `06_Tasks/`, `03_Projects/` | 不写入 |
| `today` | 生成今日计划和优先级 | 只读 | `01_Context/`, `06_Tasks/`, `02_Daily/`, `03_Projects/*/Project.md` | 不写入 |
| `closeday` | 做每日收尾和复盘 | 先只读，确认后写入 | `02_Daily/`, `03_Projects/`, `06_Tasks/` | 今日 Daily Note |
| `weekly-review` | 做周回顾、总结本周进展 | 先只读，确认后写入 | 本周 Daily Notes, 项目主页, `06_Tasks/` | `02_Daily/Week_YYYY-Www.md` |
| `reading-coach` | 主动阅读、理解、质疑、内化并行动 | 按阅读阶段互动，明确要求后写入 | 用户提供的书籍、文章、论文、课程材料或笔记 | ACTOR 学习笔记 / 知识卡片 |
| `card-creator` | 创建原子化知识卡片 | 写入 | 用户输入、卡片模板、已有卡片 | `04_Knowledge/00_Cards/` |
| `spaced-review` | 管理知识卡片间隔复习 | 按请求读写 | 已启用 SRS 的知识卡片 | 卡片 frontmatter |
| `brain-storming` | 围绕主题发散思考 | 先只读/输出，确认后沉淀 | `01_Context/`, 相关知识文件 | `04_Knowledge/` |
| `random-thinking` | 随机抽取知识内容，获得灵感 | 只读 | `04_Knowledge/00_Cards/`, `04_Knowledge/01_Topics/` | 不写入 |
| `connect` | 寻找两个主题之间的连接 | 只读 | `04_Knowledge/`, `03_Projects/`, `02_Daily/` | 不写入 |
| `trace` | 追踪一个主题在 Vault 中的演变 | 只读 | `02_Daily/`, `03_Projects/`, `04_Knowledge/`, `01_Context/` | 不写入 |
| `critical-check` | 对观点、证据、推理做建设性质疑与校验 | 默认只读，确认后写入 | `04_Knowledge/`, `03_Projects/`, `05_References/`, `02_Daily/` | 卡片反思区 / 项目文件 |
| `check-health` | 检查知识库健康状态 | 只读报告 | Markdown 文件、知识卡片、wikilink | 不写入 |
| `system-sync` | 更新系统地图、README、技能手册等 | 写入系统说明 | 系统文件、README、技能、统计数据 | `00_System/`, `README.md`, `Skills_Manual.md` 等 |

---

## 按任务选择技能

### 1. 开始工作

如果你刚打开 Vault，不知道当前该做什么：

- 用 `session-brief` 获取当前工作态势。
- 用 `today` 生成今天的行动计划。

示例：

```text
帮我生成一个 session brief，看看现在最该推进什么。
```

```text
根据当前知识库，帮我安排今天的优先事项。
```

### 2. 收尾与复盘

如果你想总结一天或一周：

- 用 `closeday` 做每日回顾。
- 用 `weekly-review` 做周回顾。

示例：

```text
帮我 close day，总结今天做了什么，明天接着做什么。
```

```text
做一个本周周回顾，看看项目推进情况。
```

### 3. 知识沉淀

如果你有一段想法、摘录、概念或资源：

- 用 `reading-coach` 在阅读前明确使命，在阅读中压缩和质疑，在阅读后检索、内化并行动。
- 用 `card-creator` 创建原子化知识卡片。
- 如果一段内容包含多个独立观点，技能会先建议拆分。
- 创建后可以用 `spaced-review` 把重要卡片加入复习队列。

示例：

```text
帮我用 ACTOR 框架真正学懂这篇文章。
```

```text
把这段内容创建成观点卡片：……
```

```text
把这张卡片加入复习，优先级设为 core。
```

### 4. 思考与探索

如果你想打开思路：

- 用 `brain-storming` 做多维度发散。
- 用 `random-thinking` 从已有知识里随机抽取灵感。
- 用 `connect` 寻找两个主题之间的连接。
- 用 `trace` 追踪一个主题的发展脉络。

如果你想对已有观点、草稿或判断做建设性质疑：

- 用 `critical-check` 拆出主张，检查证据与推理，暴露隐含假设，给出迭代方向。

示例：

```text
围绕“AI 与学习迁移”做一次头脑风暴。
```

```text
连接一下“Learning OS”和“间隔重复”。
```

```text
追踪一下“第二大脑”这个主题在我的 Vault 里是怎么演变的。
```

```text
质疑一下这张卡片：[[insight_学习不是输入而是重组]]
```

### 5. 系统维护

如果你新增了卡片、技能、模板、目录或迁移了一批内容：

- 用 `check-health` 检查链接、孤立卡片和潜在矛盾。
- 用 `system-sync` 更新系统级导航、统计和说明。

示例：

```text
检查知识库健康，重点看失效链接和孤立卡片。
```

```text
同步系统信息，更新 Vault_Map、README 和技能说明。
```

---

## 技能详情

### `init`

用途：欢迎新用户、简要介绍模板、导览关键文件，并在明确确认后清理模板示例。

使用方式：

```text
/init
```

主要读取：

- `QUICK_START.md`
- `01_Context/About_Me.md`
- `01_Context/Current_Priorities.md`
- Daily、项目、知识卡片、主题和剪藏中的代表性示例

安全边界：只清理约定目录中的 `_EXAMPLE_*`、`03_Projects/_Example_Project/` 及相关 README 中的示例引用；询问清理时不会在同一轮执行删除。初始化不创建 Daily Note。

---

### `session-brief`

用途：生成一次工作会话的简报，让你快速恢复上下文。

适合在这些时候使用：

- 刚开始一天的工作。
- 长时间离开后回来，需要快速知道当前状态。
- 不确定当前重点、活跃项目和未闭环事项。

主要读取：

- `AGENTS.md`
- `01_Context/`
- 最近 7 篇 `02_Daily/`
- `06_Tasks/Tasks.md`
- `06_Tasks/Inbox.md`
- 活跃项目的 `Project.md`

输出包括：

- 当前焦点
- 活跃项目
- 最近信号
- 未闭环事项
- 本次会话建议重点

写回规则：默认只读，不写入。

---

### `today`

用途：基于当前任务、项目和优先级生成今日计划。

适合在这些时候使用：

- 想知道今天最重要的 3 件事。
- 需要把独立任务、项目下一步和当前优先级整合成一天的行动顺序。
- 想检查今天的任务是否偏离长期重点。

主要读取：

- `01_Context/Current_Priorities.md`
- `01_Context/About_Me.md`
- `06_Tasks/Tasks.md`
- `06_Tasks/Inbox.md`
- 今日 Daily Note：`02_Daily/YYYY-MM-DD.md`
- `03_Projects/*/Project.md`

输出包括：

- Top 3 Priorities
- 上午、下午、晚上的建议顺序
- Should Do / Could Do
- 风险和分心提醒
- Inbox 状态

写回规则：默认只读，不写入。

---

### `closeday`

用途：进行每日收尾，整理今天完成了什么、推进了什么、留下了哪些明日延续。

适合在这些时候使用：

- 一天结束前做复盘。
- 想从 Daily Note 中提炼完成事项和洞察。
- 想把未完成事项转成明日优先级。

主要读取：

- 今日 Daily Note：`02_Daily/YYYY-MM-DD.md`
- `03_Projects/*/Project.md`
- `06_Tasks/Tasks.md`

输出包括：

- 今日完成
- 今日推进
- 新想法与洞察
- 未完成事项
- 延续至明日
- 一句话总结

写回规则：默认只展示。用户确认“写入”后，追加到今日 Daily Note。

---

### `weekly-review`

用途：生成一周回顾，检查项目、课程、产品和任务推进情况。

适合在这些时候使用：

- 每周结束时做复盘。
- 想知道本周真正完成了什么。
- 需要为下周计划提供依据。

主要读取：

- 本周 `02_Daily/YYYY-MM-DD.md`
- `03_Projects/*/Project.md`
- `06_Tasks/Tasks.md`
- `06_Tasks/Inbox.md`

输出包括：

- 本周概览
- 本周完成
- 本周推进
- 新增事项
- 遇到的问题
- 下周建议
- 按项目分类的进展

写回规则：默认只展示。用户确认后写入 `02_Daily/Week_YYYY-Www.md`。

---

### `reading-coach`

用途：把 AI 作为主动阅读教练，帮助用户理解、质疑、记住并应用书籍、文章、论文、课程材料或概念，而不是用摘要替代阅读。

适合在这些时候使用：

- 阅读前明确目的、问题和阅读策略。
- 阅读中梳理论证结构、困惑、反对意见和重点。
- 阅读后进行复述测试、建立连接并制定行动实验。
- 将阅读结果整理为 ACTOR 学习笔记或 Obsidian 知识卡片。

核心流程：

1. **Aim**：明确这次阅读要服务的决定、问题或能力。
2. **Compress**：找出主干、分支和必要证据。
3. **Test**：检查作者、读者和具体情境中的假设与边界。
4. **Own**：用自己的话复述，通过检索问题确认真正掌握。
5. **Run**：转化为决定、规则、清单或 24～72 小时内可执行的实验。

主要读取：

- 用户提供的原文、文件、摘录、笔记或课程材料
- 用户指定的相关 Vault 内容

写回规则：默认互动和输出，不自动写入；用户明确要求保存或创建卡片时，再遵循 Vault 模板和写回规则。

---

### `card-creator`

用途：把用户输入整理成原子化知识卡片。

适合在这些时候使用：

- 创建观点卡片、问题卡片、术语卡片、书籍笔记、资源卡片等。
- 把聊天中的一个想法沉淀到 `04_Knowledge/00_Cards/`。
- 将多个观点拆分成多张有链接关系的卡片。

支持的常见卡片类型：

- `insight`
- `counterintuitive`
- `paradox`
- `question`
- `story`
- `quote`
- `term`
- `mentalmodel`
- `book`
- `book-note`
- `person`
- `resource`
- `tool`
- `opensource`
- `course`
- `subscription`
- `prompt`
- `checklist`
- `tip`
- `moc`
- `techstack`
- `atomic-habit`

主要读取：

- `04_Knowledge/00_Cards/.templates/`
- `04_Knowledge/00_Cards/` 中已有卡片

输出和写入：

- 自动识别或确认卡片类型。
- 生成文件名：`{类型}_{卡片标题}.md`。
- 写入 `04_Knowledge/00_Cards/`。
- 尽量建立有意义的 `related` 链接，避免过度链接。

注意：一张卡片只讲一件事。如果输入包含多个独立主题，优先拆分。

---

### `spaced-review`

用途：为知识卡片提供间隔重复复习机制。

适合在这些时候使用：

- 查看今天到期要复习的卡片。
- 把重要卡片加入复习队列。
- 根据复习反馈更新下一次复习时间。

触发说法：

- “今天该复习什么？”
- “把这张卡片加入复习。”
- “这张卡片我掌握得 good / hard / easy / again。”

主要读取和写入：

- 读取 `04_Knowledge/00_Cards/` 中 `srs_enabled: true` 的卡片。
- 更新卡片 frontmatter 中的 SRS 字段。

核心反馈：

- `again`：基本忘了，需要很快再看。
- `hard`：想起来一部分，但不稳。
- `good`：基本掌握。
- `easy`：很熟，可以拉长间隔。

注意：不要把所有卡片批量加入复习。优先选择核心概念、方法论、课程知识和重要洞察。

---

### `brain-storming`

用途：围绕一个主题进行多维度发散思考，再由用户选择值得保留和沉淀的部分。

适合在这些时候使用：

- 想打开一个主题。
- 想产生更多视角、问题、类比和反向思考。
- 想为写作、课程、产品设计寻找灵感。

常见触发词：

- “头脑风暴”
- “帮我想想”
- “发散一下”
- “探索一下”
- “多角度思考”
- “来点灵感”

发散维度：

- 联想发散
- 类比思维
- 反向思考
- 延伸推演
- 跨领域连接
- 质疑与批判
- 创意组合

写回规则：

- 第一阶段只输出发散结果。
- 用户选择后，再整合成结构化内容。
- 确认保存位置后，写入 `04_Knowledge/` 中合适的主题文件。

---

### `random-thinking`

用途：从知识库中随机抽取 3-5 个主题，激活被遗忘的内容，并寻找意外连接。

适合在这些时候使用：

- 想要一点灵感。
- 想随机重访旧卡片。
- 想看看知识库中有哪些意外关联。

主要读取：

- `04_Knowledge/00_Cards/`
- `04_Knowledge/01_Topics/`

输出包括：

- 随机抽取的主题
- 每个主题的核心内容
- 深度思考问题
- 可能的意外连接

写回规则：默认只读，不写入。

---

### `connect`

用途：寻找两个主题之间的直接连接、间接桥梁、共同模式和综合机会。

适合在这些时候使用：

- 想知道两个概念是否有关联。
- 想把两个项目、方法论或知识领域串起来。
- 想生成新的写作或课程角度。

主要读取顺序：

1. `04_Knowledge/`
2. `03_Projects/`
3. `02_Daily/`

输出包括：

- Connection Summary
- Direct Connections
- Indirect Bridge Notes
- Shared Patterns
- Possible Synthesis / New Angles
- Connection Strength
- Questions to Explore

写回规则：默认只读，不写入。

注意：这个技能会区分“两个词同时出现”和“真的有意义关联”。

---

### `trace`

用途：追踪一个主题在 Vault 中随时间的发展和意义变化。

适合在这些时候使用：

- 想知道一个概念最早什么时候出现。
- 想看一个想法如何从 Daily Note 进入项目或知识库。
- 想整理某个长期主题的发展时间线。

主要读取顺序：

1. `02_Daily/`
2. `03_Projects/`
3. `04_Knowledge/`
4. `01_Context/`

输出包括：

- Topic Summary
- Earliest Appearance
- Evolution Timeline
- Key Connected Notes
- Repeated Language & Patterns
- Unresolved Threads
- Current Meaning

写回规则：默认只读，不写入。

---

### `critical-check`

用途：对指定内容做“建设性怀疑”——拆出主张、检查证据、寻找反例、暴露隐含假设，并给出迭代方向。目标不是把内容打倒，而是帮你把一个观点理解得更深、更稳、更可迭代。

适合在这些时候使用：

- 想知道某个观点、卡片或草稿是否站得住。
- 写完文章或课程设计后，想做一轮 red team。
- 怀疑某个项目判断被单一经验过度外推。
- 想让价值判断、方法论主张、个人经验总结暴露适用边界。

常见触发词：

- “质疑一下”
- “帮我校验”
- “挑战这个观点”
- “找漏洞”
- “这个观点站得住吗”
- “帮我反驳自己”
- “red team” / “critical review” / “evidence check”

主要读取：

- `AGENTS.md`
- 用户直接贴出的内容，或 `04_Knowledge/00_Cards/`、`03_Projects/`、`05_References/`、`02_Daily/` 中的指定文件
- 需要事实核查或外部证据时联网检索，并标注来源

输出包括：

- 我对原观点的理解（先复述，避免误读）
- 主张地图（中心主张、子主张、证据、隐含假设、目标对象）
- 最值得追问的地方（附“为什么重要”和“如何改进”）
- 证据与推理校验表
- 可能的反例或边界
- 更稳妥的改写
- 下一步迭代建议

每个重要质疑会标注确信度：比较可靠 / 需要澄清 / 风险较高。

写回规则：默认只读。用户确认后，可追加到原卡片的反思区，或新建 `question` / `insight` 卡片，或写入对应项目的 `Project.md`。

---

### `check-health`

用途：审查知识库健康状况，发现潜在问题。

适合在这些时候使用：

- 定期维护知识库。
- 批量创建或迁移卡片后检查质量。
- 怀疑有失效链接、孤立卡片或观点冲突。

检查维度：

- 矛盾观点检测：按主题分组列出可能冲突的观点。
- 失效双向链接检查：发现指向不存在文件的 wikilink。
- 孤立卡片识别：统计没有入链或入链很少的卡片。

输出包括：

- 知识库健康检查报告
- 潜在矛盾主题
- 失效链接列表及修复建议
- 完全孤立和弱连接卡片
- 优先处理建议

写回规则：默认只读，不自动修复。需要修复时应另行确认。

---

### `system-sync`

用途：让系统级说明文件反映 Vault 的真实状态。

适合在这些时候使用：

- 新增、删除或修改技能后。
- 新增卡片类型、模板或目录后。
- 批量迁移内容后。
- 想更新 `Vault_Map.md`、`README.md`、`CLAUDE.md` 或 `Skills_Manual.md`。

主要读取：

- `AGENTS.md`
- `CLAUDE.md`
- `00_System/Vault_Map.md`
- `00_System/Task_Management_Rules.md`
- `00_System/Writing_Rules.md`
- `00_System/Naming_Conventions.md`
- 根目录 `README.md`
- `Skills_Manual.md`
- 相关目录的 `README.md`

统计要求：

- 不手动猜数量。
- 涉及卡片数、模板数、技能数、README 数、附件数时，必须从文件系统计算。
- 需要说明统计口径。

可能写入：

- `00_System/Vault_Map.md`
- `00_System/Writing_Rules.md`
- `00_System/Naming_Conventions.md`
- `CLAUDE.md`
- `README.md`
- 目录级 `README.md`
- `Skills_Manual.md`

注意：这个技能只维护系统信息，不替代内容创作。

---

## 推荐组合流程

### 每日工作流

1. `session-brief`：恢复上下文。
2. `today`：生成今日计划。
3. 工作中用 `card-creator` 沉淀重要想法。
4. `closeday`：收尾并规划明天。

### 每周维护流

1. `weekly-review`：生成周回顾。
2. `check-health`：检查失效链接和孤立卡片。
3. `system-sync`：同步系统说明和统计。

### 主题研究流

1. `trace`：追踪主题历史。
2. `connect`：寻找与另一个主题的连接。
3. `brain-storming`：发散新角度。
4. `card-creator`：把最终洞察沉淀为卡片。

### 知识复习流

1. `spaced-review`：查看今日到期卡片。
2. 主动回忆卡片核心意思。
3. 用 `again` / `hard` / `good` / `easy` 更新反馈。
4. 对复习中产生的新洞察，用 `card-creator` 创建新卡片。

---

## 维护规则

当 `.agents/skills/` 中新增、删除或修改技能时，应同步更新本手册。

更新时建议检查：

- 技能数量是否变化。
- 技能名称和触发词是否变化。
- 读取路径和写回路径是否变化。
- 是否出现新的组合工作流。
- 是否需要同步 `00_System/Vault_Map.md` 或根目录 `README.md`。

推荐命令：

```bash
find .agents/skills -maxdepth 2 -name SKILL.md -print | sort
find .agents/skills -maxdepth 2 -name SKILL.md | wc -l
```
