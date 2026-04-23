---
name: card-creator
description: >-
  Create knowledge cards from user input. Automatically detects card type if not
  specified, then fills in the appropriate template and saves to
  04_Knowledge/00_Cards/. Use this whenever the user wants to create a
  knowledge card, note, or atomic piece of content for their knowledge
  base—even if they don't explicitly mention "cards" or "templates". Keywords:
  create card, new card, add note, save to cards, knowledge card, card from...
---

# Card Creator

> 根据用户输入创建原子化知识卡片，保存到 `04_Knowledge/00_Cards/` 目录

## 工作流程

### 0. 检查内容范围（原子化原则）

> **原子化原则**：一张卡片只讲一件事、一个观点、一个概念

在创建卡片前，先检查用户提供的内容是否符合原子化原则。

**需要拆分的信号**：
- 内容包含多个独立的观点或概念
- 有明显不同的主题（用"###"、"---"、分段标题分隔）
- 包含"另外"、"此外"、"再者"等连接多个话题的词
- 内容长度超过 300 字
- 一个主题下有多个并列的子观点

**拆分流程**：
1. 识别内容中的独立主题/观点
2. 为每个主题确定最合适的卡片类型
3. 询问用户确认拆分方案
4. 按确认后的方案创建多张卡片
5. 在卡片的 `related` 字段中建立关联

**示例**：
```
用户输入包含多个观点的内容
→ 识别为 3 个独立观点
→ 询问：这包含 3 个观点，建议拆分为 3 张观点卡片，是否同意？
→ 用户确认后创建 3 张卡片，并通过 related 字段关联
```

### 1. 确定卡片类型

**如果用户明确指定了类型**：直接使用指定的类型

**如果用户没有指定**：根据内容特征自动判断

| 类型 | 触发关键词/特征 |
|------|-----------------|
| `book` | 书籍档案、整本书信息、豆瓣链接 |
| `book-note` | 提到"书"、书名、作者、章节、页码 |
| `quote` | 引用号、引号、"xx说"、名言、金句 |
| `insight` | 观点、想法、我认为、我的理解、领悟 |
| `counterintuitive` | 反常识、意外、没想到、相反、颠覆认知 |
| `paradox` | 悖论、矛盾、看似...其实... |
| `story` | 故事、案例、例子、经历 |
| `question` | 问题、疑问、困惑、思考、为什么 |
| `person` | 人物、作者、创始人、科学家 |
| `term` | 术语、概念、定义、什么意思 |
| `tool` | 工具、软件、App、开发工具、AI工具 |
| `opensource` | 开源项目、GitHub、Repo、库、框架 |
| `course` | 课程、学习视频、训练营、在线课、教程、讲师 |
| `mentalmodel` | 思维模型、心智模型、查理芒格、决策框架、第一性原理 |
| `resource` | 博客、YouTube、Newsletter、Podcast、网站、资源推荐 |
| `subscription` | 订阅、会员、SaaS、付费工具、ChatGPT、Cursor |
| `moc` | MOC、Map of Content、内容地图、索引笔记、主题导航、知识地图 |
| `prompt` | 提示词、Prompt、AI 指令、提示词模板 |

### 2. 收集/补全内容

根据卡片类型，提取用户提供的核心信息，并补全模板中必要的字段：

**必填字段**：
- `created`: 当前日期 (YYYY-MM-DD)
- `source`: 信息来源（必须提供）
- `type`: 卡片类型
- `card_type`: 具体类型

**类型特有字段**：
- `book`: book, author, douban_url, cover
- `book-note`: book, author
- `quote`: 引用内容、作者/出处
- `person`: 姓名、领域
- `tool`: 工具名称、类型、网址、定价、平台
- `opensource`: 项目名称、作者/组织、网址、语言、许可证、Stars
- `course`: 课程名称、讲师/机构、平台、难度级别、时长、价格
- `mentalmodel`: 模型名称、提出者、学科领域、来源
- `resource`: 资源名称、类型（博客/YouTube/Newsletter/Podcast/网站）、语言、更新频率
- `subscription`: 服务名称、套餐、价格、周期、续费日期
- `moc`: MOC 名称、类型（主题/项目/人物/概念/时间）、主题描述

**辅助补全**：
- 根据用户输入，补充模板中 `{{}}` 占位符的内容
- 保持用户的原话和表达风格
- 不确定的信息留空或用 `{{待补充}}` 标记

### 3. 生成文件名

格式：`{类型}_{卡片标题}.md`

- 类型使用小写，用连字符连接：`book-note`, `counterintuitive` 等
- 标题从用户输入中提取，或根据内容生成
- 去除特殊字符，保持简洁

**特殊规则：Skills 项目命名**

当创建名为 "Skills" 的项目时，使用格式：`opensource_Skills_{项目名}`

示例：
```
opensource_Skills_MinimalistEntrepreneur.md  # The Minimalist Entrepreneur
opensource_Skills_Principles.md              # 《原则》
opensource_Skills_Rails.md                   # Rails on Guides
```

**原因**：避免同名冲突（Skills 是常见的项目名），清晰标识具体项目

### 4. 查找相关卡片并建立双向链接

> 在创建新卡片前，检查已有卡片，建立知识网络

**查找相关卡片的依据**：
- 相同或相似的标签
- 相同的来源（如同一本书、同一个人）
- 内容中的关键词匹配
- 相同的主题或概念

**双向链接的建立方式**：

1. **读取已有卡片**：扫描 `04_Knowledge/00_Cards/` 目录下所有 `.md` 文件
2. **匹配相关卡片**：根据关键词、标签、内容匹配已有卡片
3. **新卡片的 related 字段**：只添加**一条**关联强度最高的卡片链接
4. **更新已有卡片的 related 字段**：在新卡片创建后，更新相关卡片的 `related` 字段，添加指向新卡片的链接

**frontmatter 中的 related 字段格式**：
```yaml
related: "[[insight_最相关的卡片]]"
```

**正文中"关联卡片"部分格式**：
```markdown
## 关联卡片
- [[insight_相关卡片]] — 简短说明
- [[quote_另一张卡片]] — 简短说明
```

**规则说明**：
- **frontmatter related**：只放一条链接，选关联强度最高的
- **正文关联卡片**：放所有相关卡片，每条附带简短说明
- 这样做的好处：frontmatter 简洁，正文完整

**示例**：
```
新卡片：insight_数量优于质量
已有卡片：insight_写作是思考过程、insight_刻意练习的适用边界

→ frontmatter related: [[insight_写作是思考过程]]  (只放最相关的一条)
→ 正文关联卡片：
  - [[insight_写作是思考过程]] — 数量带来质量突破
  - [[insight_刻意练习的适用边界]] — 质量与数量的关系
```

**注意事项**：
- 只创建真正有意义的关联，避免过度链接
- 正文关联数量建议控制在 3-5 个以内
- 如果相关卡片超过 10 个，考虑是否过于宽泛

### 5. 创建文件

- 读取对应的模板文件：`04_Knowledge/00_Cards/.templates/{类型}_Card.md`
- 替换模板中的占位符
- 将文件写入 `04_Knowledge/00_Cards/` 目录
- 告知用户文件已创建的路径

## 模板文件位置

> 所有卡片模板统一存放在 `04_Knowledge/00_Cards/.templates/` 目录

```
04_Knowledge/00_Cards/.templates/
├── Book_Card.md
├── Book_Note_Card.md
├── Insight_Card.md
├── Quote_Card.md
├── Counterintuitive_Card.md
├── Paradox_Card.md
├── Story_Card.md
├── Question_Card.md
├── Person_Card.md
├── Term_Card.md
├── Tool_Card.md
├── Opensource_Card.md
├── Course_Card.md
├── Mental_Model_Card.md
├── Resource_Card.md
├── Subscription_Card.md
├── MOC_Card.md
├── Checklist_Card.md
├── Tip_Card.md
├── Tech_Stack_Card.md
└── Prompt_Card.md
```

## 使用示例

**用户明确指定类型**：
```
创建一个观点卡片：数量优于质量
```

**用户不指定类型**：
```
从《原则》这本书中学到一个观点：痛苦+反思=进步
```
→ 自动识别为 `book-note` 类型

**金句识别**：
```
马斯克说过一句话让我印象深刻："数量自有质量的品味"
```
→ 自动识别为 `quote` 类型

**资源卡片识别**：
```
推荐一个很棒的博客：Paul Graham's Essays
```
→ 自动识别为 `resource` 类型

**课程卡片识别**：
```
推荐一门很棒的课程：Andrej Karpathy 的 Neural Networks: Zero to Hero
```
→ 自动识别为 `course` 类型

**思维模型卡片识别**：
```
查理芒格提到一个思维模型叫"逆向思维"
```
→ 自动识别为 `mentalmodel` 类型

**MOC 卡片识别**：
```
创建一个学习科学的 MOC
帮我做一个关于编程的知识地图
整理一下关于查理芒格的所有内容，做成 MOC
```
→ 自动识别为 `moc` 类型

## YAML 引号规则

> 为确保 frontmatter 属性能被正确解析，包含特殊字符的值必须加双引号

### 需要加双引号的情况

| 字段 | 触发条件 | 示例 |
|------|----------|------|
| `book` | 中文书名 | `book: "认知天性"` |
| `author` | 包含 `[]` `（）` `、` | `author: "[美] Charles Petzold"` |
| `source` | 包含 `:` `,` `()` `中文` | `source: "Sweller, J. (1988)"` |
| `cover` | 包含 `[[ ]]` | `cover: "[[book.png]]"` |
| `douban_url` | URL（可选加引号） | `douban_url: "https://..."` |

### 不需要引号的情况

```yaml
tags: [card, book]              # 列表
created: 2026-04-11             # 纯数字/日期
related: []                     # 列表
```

### 示例对比

```yaml
# ❌ 错误 - 可能解析失败
book: 认知天性
author: [美] Peter C. Brown
source: Sweller, J. (1988). Title.

# ✅ 正确 - 加双引号
book: "认知天性"
author: "[美] Peter C. Brown"
source: "Sweller, J. (1988). Title."
```

## 注意事项

1. **原子化原则**：一张卡片只讲一件事，多观点内容必须拆分
2. **来源信息**：`source` 字段是必需的，如果用户没有提供，需要询问
3. **文件冲突**：如果同名文件已存在，询问用户是否覆盖
4. **内容保留**：尽量保留用户的原话，不要过度改写
5. **占位符处理**：用户没有提供的信息，用 `{{待补充}}` 标记
6. **related 字段规则**（重要）：
   - **frontmatter related**：只放**一条**链接，选关联强度最高的
   - **正文 关联卡片**：放所有相关卡片，每条附带简短说明
   - 这样做的好处：frontmatter 简洁，正文完整
7. **卡片关联**：
   - 拆分后的卡片通过 `related` 字段建立关联
   - **双向链接**：创建新卡片时，也要更新相关已有卡片的 `related` 字段
   - 链接格式使用 wikilink：`[[卡片文件名]]`
8. **关联数量**：建议控制在 3-5 个以内，避免过度链接
9. **MOC 特殊规则**：
   - MOC 是"内容地图"，不是知识单元，用于组织和导航其他卡片
   - MOC 命名格式：`moc_{主题名}.md`（如 `moc_学习科学.md`）
   - MOC 的 `source` 字段可以留空或填写"自己整理"
   - MOC 主要内容是 wikilink 列表，不需要大量正文
