---
name: connect
description: Find meaningful connections between two topics across the vault. Use this skill when the user asks to connect, link, or relate two concepts, find relationships between topics, discover how ideas intersect, or explore connections in their knowledge base. This skill searches Knowledge, Projects, and Daily Notes to identify direct links, bridge concepts, and synthesis opportunities.
---

# Connect: Find Topic Connections

在 Vault 中发现两个主题之间有意义的连接，识别直接关系、间接桥梁、共同模式和可能的综合机会。

---

## 工作流程

### Step 1: 读取核心导航

首先读取 `AGENTS.md` 理解仓库结构和导航规则。

了解目录优先级：`04_Knowledge/` > `03_Projects/` > `02_Daily/`

### Step 2: 搜索主题 A

使用 Grep 工具按优先级顺序搜索：

1. **04_Knowledge/** — 知识沉淀和定义
2. **03_Projects/** — 项目文件和决策
3. **02_Daily/** — 每日记录和讨论

搜索策略：
- 直接主题名称
- 常见变体和同义词
- 相关关键词

### Step 3: 搜索主题 B

重复 Step 2 的搜索过程，收集主题 B 的所有提及。

### Step 4: 寻找共同出现

搜索两个主题同时出现的文件：
- 使用 Grep 搜索包含两个主题关键词的文件
- 检查是否有项目同时涉及两个主题
- 查看 Daily Notes 中是否有同时讨论两个主题的记录

### Step 5: 识别桥梁笔记

找出可能连接两个主题的中间概念：
- 同时链接到两个主题的笔记
- 包含两个主题相关关键词的文件
- 跨项目的共享概念或方法论

### Step 6: 分析连接类型

识别：
- **直接连接**：两个主题在同一文件中明确关联
- **间接桥梁**：通过第三个概念连接
- **重复模式**：两个主题在不同文件中反复出现的相似结构
- **潜在综合**：可能合并或产生新视角的机会

---

## 输出格式

按照以下模板输出：

```markdown
# Topic Connection: {{Topic A}} ↔ {{Topic B}}

## Connection Summary
> 一句话概括这两个主题在你的 vault 中是如何关联的

{{基于分析的整体判断}}

---

## Direct Connections
> 两个主题在同一文件中明确出现

### Knowledge Files
- `{{文件路径}}` — {{连接方式说明}}

### Project Files
- `{{项目路径}}` — {{哪个项目同时涉及两个主题}}

### Daily Notes
- {{日期}} — {{那一天如何同时讨论这两个主题}}

---

## Indirect Bridge Notes
> 通过中间概念连接两个主题的笔记

### Bridge via {{桥梁概念1}}
- `{{文件路径}}` — {{如何连接 A 和 B}}

### Bridge via {{桥梁概念2}}
- `{{文件路径}}` — {{如何连接 A 和 B}}

---

## Shared Patterns
> 两个主题中重复出现的结构、问题或方法

- {{共同模式1}} — {{在 A 和 B 中如何体现}}
- {{共同模式2}} — {{在 A 和 B 中如何体现}}

---

## Co-occurrence Analysis
> 两个主题经常一起出现的上下文

- {{上下文1}}：{{说明}}
- {{上下文2}}：{{说明}}

---

## Possible Synthesis / New Angles
> 基于连接分析，可能的新视角或综合机会

1. **{{综合机会1}}**
   - 来源：{{哪个文件或项目启发}}
   - 可能性：{{为什么这值得探索}}

2. **{{综合机会2}}**
   - 来源：{{哪个文件或项目启发}}
   - 可能性：{{为什么这值得探索}}

---

## Connection Strength
> 评估两个主题之间的关联强度

**强度**: {{强 / 中 / 弱}}

**依据**:
- 直接连接数: {{数量}}
- 桥梁节点数: {{数量}}
- 共同模式数: {{数量}}

---

## Questions to Explore
> 基于这个连接分析，值得进一步探索的问题

- {{问题1}}
- {{问题2}}
```

---

## 搜索优先级

- **优先搜索**：`04_Knowledge/`（知识沉淀和定义）
- **其次**：`03_Projects/`（项目文件和决策）
- **补充**：`02_Daily/`（每日记录和讨论）

---

## 注意事项

- **只读模式**：不要修改任何文件
- 如果连接很少，明确指出数据有限
- 区分"同时出现"和"有意义关联"
- 优先展示有洞察力的连接，而不是罗列所有提及
- 如果两个主题看似无关，分析为什么它们可能值得连接

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和结构
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级搜索，不要盲目扫描整个 vault
- **Use the vault structure as navigation** — 利用 Knowledge > Projects > Daily 优先级定位信息
- **Do not hallucinate missing context** — 如果主题在 vault 中提及很少，明确说明，不要编造连接
- **If evidence is weak, say so** — 如果连接证据不足，如实指出关联强度较弱
- **Default to read-only unless explicit confirmation is given** — 默认只读分析，不修改任何文件
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级
