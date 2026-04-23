---
title: Projects Directory
description: 项目管理 — 每个项目一个目录
created: 2026-04-23
tags: [project, system]
---

# Projects

> 项目管理 — 每个项目一个目录，包含计划、任务、决策和产出

---

## 目录结构

```
03_Projects/
├── .templates/        # 项目模板（新建项目时复制这个）
├── _Example_Project/  # 一个完整的示例项目
├── <Your_Project>/    # 你的项目
└── README.md
```

---

## 项目文件结构

每个项目包含以下核心文件：

| 文件 | 说明 |
|------|------|
| `00_Overview.md` | 项目概览 — 定义、背景、目标、约束 |
| `01_Planning.md` | 项目计划 — 路线图、里程碑 |
| `02_Goals.md` | 目标设定 — 短/中/长期目标 |
| `03_Backlog.md` | 任务池 — 已分解但未排期的任务 |
| `04_Next.md` | 下一步 — 即将开始的任务 |
| `05_Doing.md` | 进行中 — 当前正在执行的任务 |
| `06_Testing.md` | 测试中 — 待验证的任务 |
| `07_Done.md` | 已完成 — 已完成的任务 |
| `Decisions.md` | 决策记录（可选） |
| `README.md` | 项目说明（可选） |

---

## 项目产出目录（按需创建）

| 目录 | 说明 |
|------|------|
| `Attachments/` | 附件资源（图片、PDF、设计稿等） |
| `Docs/` | 交付物文档（白皮书、设计文档、需求文档等） |
| `Meetings/` | 会议记录（命名：`YYYY-MM-DD-主题.md`） |
| `References/` | 项目相关参考资料 |
| `Sessions/` | 会话/课程记录（课程类项目专用） |

---

## 使用指南

### 新建项目

1. 复制 `.templates/` 中的模板文件
2. 根据需要创建产出目录
3. 填写 `00_Overview.md` 定义项目

### 项目命名

- 使用英文或拼音
- 使用 PascalCase 或 snake_case
- 保持简洁但描述性

### 产出目录使用

- **按需创建**：不是每个项目都需要所有目录
- **长期保留**：Docs/ 中的交付物永久保留
- **按需归档**：项目结束后可将部分内容移至 Archive

---

## 相关文档

- [[../00_System/Vault_Map|Vault Map]] — 整体仓库结构
- [[../04_Knowledge|Knowledge]] — 知识沉淀
- [[../05_References|References]] — 剪藏文章
