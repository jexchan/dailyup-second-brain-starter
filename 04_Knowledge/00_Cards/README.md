---
title: Knowledge Cards
description: Atomic knowledge cards — one card, one idea
tags: [knowledge, cards, system]
---

# 00_Cards — 原子化知识卡片

> 一张卡片，只讲一件事。卡片之间通过 `related` 字段和 `[[双向链接]]` 构建知识网络。

---

## 卡片类型（22 种）

完整模板见 `.templates/` 目录。每种类型针对一种特定的知识单元：

| 类型 | 用途 | 示例卡片 |
|------|------|----------|
| `insight` | 自己的思考与洞察 | [[_EXAMPLE_insight_记录是思考的外部硬盘]] |
| `book` | 一本书的档案 + 概要 | [[_EXAMPLE_book_卡片笔记写作法]] |
| `book-note` | 一本书里的具体笔记 | — |
| `quote` | 有启发的引用 | [[_EXAMPLE_quote_学而不思则罔]] |
| `person` | 值得关注的人物 | [[_EXAMPLE_person_Niklas_Luhmann]] |
| `mentalmodel` | 通用思维模型 | [[_EXAMPLE_mentalmodel_第一性原理]] |
| `term` | 重要概念/术语 | — |
| `resource` | 在线资源（网站、文章） | — |
| `tool` | 实用工具 | [[_EXAMPLE_tool_Obsidian]] |
| `opensource` | 开源项目 | — |
| `prompt` | AI 提示词模板 | — |
| `counterintuitive` | 反直觉的观点 | — |
| `course` | 优质课程 / 学习视频 | — |
| `checklist` | 标准化流程清单 | — |
| `tip` | 实用技巧 | — |
| `subscription` | 付费订阅服务 | — |
| `atomic-habit` | 习惯追踪 | — |
| `techstack` | 技术栈组合 | — |
| `story` | 有启发的故事 | — |
| `paradox` | 思维悖论 | — |
| `question` | 值得长期追问的问题 | — |
| `moc` | 主题内容地图（Map of Content） | — |

---

## 卡片设计理念

1. **原子化**：一张卡片只讲一件事。信息太多就拆成多张
2. **可链接**：通过 `related` 字段和 `[[wiki链接]]` 关联其他卡片
3. **有来源**：`source` 字段记录这个知识从哪里来
4. **可复用**：同一张卡片可以在多个项目、多篇文章里引用

---

## 如何新建卡片

### 手动方式
1. 从 `.templates/` 找对应类型的模板
2. 复制到 `00_Cards/` 根目录
3. 按命名规范重命名：`{type}_{主题}.md`
4. 填写 frontmatter 和正文

### 用 AI Skill 方式
使用 `card-creator` Skill（已内置）：

```
/create-card 关于「xxx」的 insight 卡
```

AI 会自动识别卡片类型、填写合适的模板、保存到正确位置。

---

## 命名规范

```
{card_type}_{主题名称}.md

示例：
- insight_记录是思考的外部硬盘.md
- book_卡片笔记写作法.md
- mentalmodel_第一性原理.md
- person_Niklas_Luhmann.md
```

示例卡片统一带 `_EXAMPLE_` 前缀，方便批量删除。

---

## 示例卡片说明

本目录预置了 6 张示例卡片（`_EXAMPLE_` 前缀），展示不同类型的卡片长什么样，它们之间怎么互相引用。

**你可以安全删除所有 `_EXAMPLE_*` 文件**，它们只是样板。
