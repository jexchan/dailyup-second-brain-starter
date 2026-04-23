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
稳定的全局上下文：个人定位、使命、品牌、受众、当前优先级

首次使用时需要填写 `01_Context/` 下的占位模板：
- `About_Me.md`
- `Mission_and_Vision.md`
- `Brand_Voice.md`
- `Audience_Profiles.md`
- `Current_Priorities.md`

## 02_Daily
每日记录、会话摘要、临时想法、最近进展

新建 Daily Note 时建议使用 `.templates/Daily_Note.md` 模板。

## 03_Projects
具体项目资料，按项目组织

### 项目文件结构
每个项目包含以下核心文件：
- `00_Overview.md` — 项目基本概况
- `01_Planning.md` — 项目计划与路线图
- `02_Goals.md` — 目标设定（短/中/长期）
- `03_Backlog.md` — 任务池，已分解但未排期
- `04_Next.md` — 下一步要做的任务
- `05_Doing.md` — 正在进行的任务
- `06_Testing.md` — 校验/测试中的任务
- `07_Done.md` — 已完成的任务
- `Decisions.md` — 决策记录（可选）

### 项目产出目录（按需创建）
- `Attachments/` — 附件资源（图片、PDF、设计稿等）
- `Docs/` — 交付物文档（白皮书、设计文档、需求文档、技术方案等）
- `Meetings/` — 会议记录（命名：`YYYY-MM-DD-主题.md`）
- `References/` — 项目相关参考资料（行业分析、竞品研究、技术调研等）
- `Sessions/` — 会话/课程记录（课程类项目专用）

### 项目模板
项目模板位于 `.templates/` 目录，新建项目时复制 `.templates/` 的全部内容到你的项目目录即可。

## 04_Knowledge
长期知识沉淀与方法论
- `00_Cards/` — 原子化知识卡片
  - `.templates/` — 卡片模板（22 种类型）
    - `insight`, `counterintuitive`, `paradox`, `question`, `story`, `quote`, `term`, `mentalmodel`, `book`, `book-note`, `person`, `resource`, `tool`, `opensource`, `course`, `subscription`, `prompt`, `checklist`, `tip`, `moc`, `techstack`, `atomic-habit`
- `01_Topics/` — 主题学习笔记
- `Frameworks/` — 常用框架和方法论（示例）

## 05_References
网上剪藏文章的收集与消化

### 目录结构
- `01_Inbox/` — 新剪藏入口
- `02_AI_&_Tech/` — AI 和技术相关
- `03_Education/` — 教育、学习科学相关
- `04_Product/` — 产品、设计相关
- `05_Writing/` — 写作、内容创作相关
- `06_Research/` — 研究论文、深度报告
- `07_Archive/` — 已消化/归档

### 工作流程
网上剪藏 → Inbox → 阅读/分类 → 提炼卡片 → 归档/删除

## 06_Tasks
任务收集、本周重点、等待项

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
