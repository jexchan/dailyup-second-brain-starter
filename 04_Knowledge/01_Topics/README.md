---
title: Topics Directory
description: 主题学习笔记目录
created: 2026-05-26
tags: [knowledge, topics, system]
---
# Topics

`01_Topics/` 用于存放**某个领域的系统学习过程**。

它适合承载一段持续学习：目标、路线、阅读笔记、练习记录、资源清单，以及从学习过程中提炼出来的概念卡片链接。

---

## 边界规则

- 单个概念、观点、模型 → 放入 `04_Knowledge/00_Cards/`
- 某个领域的系统学习过程 → 放入 `04_Knowledge/01_Topics/`
- 可重复调用、需要整体阅读、能指导行动的方法论手册 → 放入 `04_Knowledge/Frameworks/`

简单判断：

```text
这是一个知识点吗？
├── 是 → 00_Cards/
└── 否 → 继续判断

这是一个可复用的方法论手册吗？
├── 是 → Frameworks/
└── 否 → 继续判断

这是围绕某个领域持续学习、积累材料和练习的过程吗？
├── 是 → 01_Topics/
└── 否 → 先放入合适的 Inbox 或询问 AI
```

---

## 推荐结构

新建主题时，建议使用以下结构：

```text
01_Topics/{Topic_Name}/
├── 00_Overview.md       # 学习目标、范围、进度、资源入口
├── 01_Notes/            # 阅读、视频、课程笔记
├── 02_Exercises/        # 练习、代码、实践记录
├── 03_Concepts/         # 概念索引，链接到 00_Cards
└── 99_Resources.md      # 外部资源汇总
```

小主题可以先从一个 `00_Overview.md` 开始，不必一开始就建完整目录。

---

## 示例主题

当前模板保留一个示例主题：

- `_EXAMPLE_Learning_Science/` — 学习科学主题示例
  - `_EXAMPLE_Core_Principles.md` — 核心原则示例笔记

示例用于展示主题学习笔记的写法。初始化个人 Vault 时，`scripts/init.sh` 会清理 `_EXAMPLE_*` 主题目录。

