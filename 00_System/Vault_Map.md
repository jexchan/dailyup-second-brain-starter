---
description: Visual map and overview of the vault structure
tags: [system, map, overview]
---
# Vault Map

## 00_System
系统级规则、导航、写作规范、命名规范、AI 工作原则

### 附件管理
- 所有附件存放到对应目录下的 `Attachments/` 文件夹
- 见 `Writing_Rules.md` 中的"附件管理规则"章节

## 01_Context
长期稳定背景与当前动态重点：

- `About_Me.md` — 我是谁、长期方向、AI 协作偏好，以及可选的受众与表达风格
- `Current_Priorities.md` — 当前目标、重点、活跃项目、关键问题和暂时不做

默认只维护这两个文件。受众、品牌或使命内容增长到明显需要独立维护时，再按需拆分。

## 02_Daily
每日记录、会话摘要、临时想法、最近进展

新建 Daily Note 时建议使用 `.templates/Daily_Note.md` 模板。模板只保留三个栏目：
- `今日重点` — 当天选择的 1～3 个关注点
- `今日记录` — 进展、问题、决定、输入和想法的统一记录区
- `一句话总结` — 可选的日终收束

## 03_Projects
具体项目资料，按项目组织

### 项目文件结构
每个项目默认只有一个核心文件：
- `Project.md` — 项目定义、完成标准、状态、下一步、Backlog、里程碑、进展与决策

### 项目产出目录（按需创建）
- `Outputs/` — 文章、方案、课程材料、设计稿等真实产出；出现第一份产出时再创建
- 内容明显增多后，可在 `Outputs/` 下按需拆分 `Docs/`、`Assets/`、`Meetings/` 等目录

### 项目模板
项目模板为 `.templates/Project.md`。新建项目时只复制这一文件，不预建空目录。

## 04_Knowledge
长期知识沉淀与方法论
- `00_Cards/` — 原子化知识卡片
  - `.templates/` — 卡片模板（22 种类型）
    - `insight`, `counterintuitive`, `paradox`, `question`, `story`, `quote`, `term`, `mentalmodel`, `book`, `book-note`, `person`, `resource`, `tool`, `opensource`, `course`, `subscription`, `prompt`, `checklist`, `tip`, `moc`, `techstack`, `atomic-habit`
- `01_Topics/` — 某个领域的系统学习过程
  - 示例：`_EXAMPLE_Learning_Science/`
  - 单个概念、观点、模型进入 `00_Cards/`
  - 可重复调用的方法论手册进入 `Frameworks/`
- `Frameworks/` — 可重复调用、需要整体阅读、能指导行动的方法论手册
  - 示例：`_EXAMPLE_问题-框架-落地.md`
  - 单个概念、观点、模型进入 `00_Cards/`
  - 某个领域的系统学习过程进入 `01_Topics/`

## 05_References
外部剪藏的收集、消化与精选原文保留

### 目录结构
- `01_Inbox/` — 尚未判断或消化的剪藏
- `02_Library/` — 已消化且原文本身值得长期保留的精选文章

### 工作流程
剪藏 → Inbox → 阅读与判断 → 产生卡片、项目决定或行动 → 原文进入 Library 或删除。主题通过标签和链接表达，不建立分类目录。

## 06_Tasks
全局任务入口与非项目任务管理：
- `Inbox.md` — 尚未分类的新任务，定期处理并尽量清空
- `Tasks.md` — 不属于具体项目的下一步、等待事项和以后可能

项目任务保留在对应项目的 `Project.md`；Daily Note 只记录当天的选择和执行结果。

## 07_Bases
Obsidian Base 数据库视图

### 内容型 Base（集中式）
跨目录聚合的知识实体数据库，需要全库视角访问：
- `Resources.base` — 资源合集
- `Persons.base` — 人物卡片
- `Books.base` — 藏书管理
- `Opensource.base` — 开源项目
- `Subscriptions.base` — 订阅追踪

**特点：** 通过文件名前缀过滤，Base 与内容分离

### 新建 Base 的判断规则
问自己：这个 Base 是"全库视角"还是"领域视角"？
- 全库 → 放在 `07_Bases/`
- 领域 → 嵌入对应子目录
