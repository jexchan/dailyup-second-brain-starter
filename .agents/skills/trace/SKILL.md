---
name: trace
description: Track how a topic has evolved across the vault over time. Use this skill when the user asks to trace, track, or follow the evolution of a concept, see how an idea developed over time, find the history of a topic, or explore when and how a subject emerged in their knowledge base. This skill searches Daily Notes, Projects, and Knowledge files to build a timeline and knowledge network.
---

# Trace: Track Topic Evolution

追踪一个主题在 Obsidian Vault 中随时间的演变过程，构建其发展时间线和知识网络。

---

## 工作流程

### Step 1: 读取核心上下文

首先读取 `AGENTS.md` 理解仓库结构和导航规则。

读取 `01_Context/` 下的相关文件（如果有主题相关的）。

### Step 2: 搜索主题提及

使用 Grep 工具搜索整个 vault，按优先级顺序：

1. **02_Daily/** — 每日记录，捕捉时间线索
2. **03_Projects/** — 项目文件，捕捉决策和进展
3. **04_Knowledge/** — 知识沉淀，捕捉定义和框架
4. **01_Context/** — 全局上下文，捕捉定位和方向

搜索策略：
- 直接主题名称
- 常见变体和同义词
- 相关关键词

### Step 3: 提取时间线索

从搜索结果中提取：
- 最早出现的日期和文件
- 关键决策记录（Decisions.md）
- Daily Note 中的讨论
- 项目状态变化

### Step 4: 分析主题演变

识别：
- 主题名称/定义的变化
- 框架或方法论的发展
- 相关项目的启动/转向
- 重复出现的语言模式
- 持续未解决的问题

### Step 5: 构建知识网络

找出：
- 直接链接的笔记（Obsidian wikilinks）
- 经常一起出现的其他主题
- 所属的项目
- 相关的知识领域

---

## 输出格式

按照以下模板输出：

```markdown
# Topic Trace: {{Topic}}

## Topic Summary
> 一句话定义这个主题当前在你的 vault 中意味着什么

{{基于最新文件的定义}}

---

## Earliest Appearance
**日期**: {{YYYY-MM-DD}}
**文件**: {{文件路径}}
**上下文**: {{当时是如何引入这个主题的}}

---

## Evolution Timeline

### {{阶段1}} ({{时间范围}})
- **关键事件**: {{发生了什么}}
- **定义变化**: {{主题含义如何变化}}
- **相关决策**: {{Decisions.md 中的记录}}

### {{阶段2}} ({{时间范围}})
- **关键事件**: {{发生了什么}}
- **定义变化**: {{主题含义如何变化}}
- **相关决策**: {{Decisions.md 中的记录}}

---

## Key Connected Notes

### Projects
- `{{项目路径}}` — {{关系说明}}

### Knowledge
- `{{知识文件路径}}` — {{关系说明}}

### Daily Notes
- {{日期}} — {{那一天的讨论/决策}}

---

## Repeated Language & Patterns
> 在多个文件中反复出现的表达、问题或关注点

- {{重复的表述1}}
- {{重复的表述2}}

---

## Unresolved Threads
> 尚未解决或仍在演变的问题

- {{未解决问题1}}
- {{未解决问题2}}

---

## Current Meaning
> 这个主题现在对你的工作意味着什么

{{基于最新文件的总结}}
```

---

## 搜索优先级

- **优先搜索**：`02_Daily/`（每日记录，捕捉时间线索）
- **其次**：`03_Projects/`（项目文件，捕捉决策和进展）
- **补充**：`04_Knowledge/`（知识沉淀，捕捉定义和框架）
- **背景**：`01_Context/`（全局上下文）

---

## 注意事项

- **只读模式**：不要修改任何文件
- 时间线基于文件日期和 frontmatter
- 如果主题提及很少，明确指出数据有限
- 区分"主题定义变化"和"表述方式变化"

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和结构
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级搜索，不要盲目扫描整个 vault
- **Use the vault structure as navigation** — 利用 Daily > Projects > Knowledge 优先级构建时间线
- **Do not hallucinate missing context** — 如果主题在 vault 中没有记录，明确说明，不要编造历史
- **If evidence is weak, say so** — 如果证据稀少或时间线不完整，如实指出
- **Default to read-only unless explicit confirmation is given** — 默认只读分析，不修改任何文件
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级
