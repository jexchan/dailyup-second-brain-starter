---
title: Topics Directory
description: 长期主题地图目录
created: 2026-05-26
updated: 2026-07-22
tags: [knowledge, topics, system]
---
# Topics

`01_Topics/` 用于维护**长期关注领域的知识地图与阶段性理解**。

Topic 不是资料仓库，也不是有截止时间的学习项目。它负责回答：这个领域包含什么、我目前如何理解、已有知识如何连接、接下来还想探索什么。

## 内容边界

- 单个概念、观点或模型 → `04_Knowledge/00_Cards/`
- 长期领域的知识地图与综合理解 → `04_Knowledge/01_Topics/`
- 有目标、期限或完成标准的学习 → `03_Projects/`
- 外部文章与原始资料 → `05_References/`
- 人可直接执行的方法 → `mentalmodel` 或 `checklist` 卡片
- 用来指导 AI 执行的完整流程 → `.agents/skills/`

Topic 通过链接连接这些内容，不在目录中复制保存它们。

## 从一个文件开始

新主题默认只创建一个文件：

```text
01_Topics/
└── Learning_Science.md
```

建议包含：

```markdown
# 主题名称

## 主题范围

## 核心问题

## 当前理解

## 相关知识

## 相关项目

## 重要来源

## 下一步探索
```

只有单个文件已经难以维护时，才升级为同名目录，并以 `Topic.md` 作为入口。不预建 Notes、Exercises、Concepts 或 Resources 等子目录。

## 示例

- [[_EXAMPLE_Learning_Science]] — 展示长期主题地图如何连接问题、卡片、项目与来源

初始化个人 Vault 时，`scripts/init.sh` 会清理 `_EXAMPLE_*` 示例文件。
