---
title: Knowledge Directory
description: 长期知识沉淀与方法论
created: 2026-04-23
tags: [knowledge, system]
---

# Knowledge

> 长期知识沉淀与方法论仓库

---

## 目录结构

```
04_Knowledge/
├── 00_Cards/          # 原子化知识卡片
├── 01_Topics/         # 主题学习笔记
├── Frameworks/        # 方法论文档
└── README.md          # 本文件
```

> **注意**：网上剪藏文章已迁移至 `05_References/`，详见 [[../05_References|05_References/README]]

---

## 各目录说明

### 00_Cards/
原子化知识卡片集合，每张卡片聚焦一个单一知识点。

`00_Cards/.templates/` 下提供 22 种卡片模板，直接复制使用。

**卡片类型**：insight、person、book、mentalmodel、term、quote、resource、tool、opensource、prompt、course、checklist、book-note、tip、subscription、atomic-habit、techstack、story、paradox、counterintuitive、question、moc

---

### 01_Topics/
主题学习笔记，用于深度学习某个主题。

**典型场景**：
- 跟随 Andrej Karpathy 的 LLM 课程学习
- 系统学习 AI Safety
- 研究某个技术领域

**推荐结构**：
```
Topics/{主题名}/
├── 00_Overview.md       # 学习目标、进度、资源链接
├── 01_Notes/            # 视频/阅读笔记
├── 02_Exercises/        # 练习、代码、项目
├── 03_Concepts/         # 提取的概念卡片（链接到 00_Cards）
└── 99_Resources.md      # 外部资源汇总
```

---

### Frameworks/
**方法论手册** — 存放系统性、需要整体阅读的方法论文档。

**重要**：`Frameworks/` 与 `00_Cards/` 的区别

| Frameworks | 00_Cards |
|-----------|----------|
| 方法论手册（整体阅读） | 原子化知识单元（可引用） |
| 操作性框架（如何做） | 概念性知识（是什么） |
| 示例：问题-框架-落地 | 示例：mentalmodel_第一性原理 |
| 示例：课程设计五要素 | 示例：term_刻意练习 |

**区分原则**：
- 问自己：这是"一本手册"还是"一个工具"？
- **手册** → `Frameworks/`
- **工具** → `mentalmodel_` 卡片

**示例框架**：
- [[问题-框架-落地]] — 内容结构化方法
- [[课程设计五要素]] — 课程设计框架
- [[Learning_OS核心模块]] — 学习系统模块

---

## 使用指南

### 添加新知识

1. **原子化知识点** → 在 `00_Cards/` 创建对应类型的卡片
2. **网上剪藏文章** → 暂存 `05_References/01_Inbox/`，阅读后提炼为卡片
3. **主题学习** → 在 `01_Topics/` 创建主题目录
4. **新方法论** → 在 `Frameworks/` 添加文档

> **网上剪藏流程**：`05_References/01_Inbox/` → 阅读/分类 → 提炼卡片 → 归档/删除

### 卡片与 Frameworks 的选择

当你不确定内容该放哪里时：

```
内容需要整体阅读才能理解？
├── 是 → Frameworks/
└── 否 → 00_Cards/

内容是"如何做"的操作步骤？
├── 是 → Frameworks/
└── 否 → 00_Cards/

内容可以被单独引用和链接？
├── 是 → 00_Cards/
└── 否 → Frameworks/
```

---

## 相关文档

- [[../00_System/Vault_Map|Vault Map]] — 整体仓库结构
- [[../00_System/Writing_Rules|Writing Rules]] — 写作规范
