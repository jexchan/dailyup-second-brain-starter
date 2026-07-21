---
title: Projects Directory
description: 项目管理 — 每个项目一个目录
created: 2026-04-23
tags: [project, system]
---

# Projects

> 项目管理 — 一个项目主页承载上下文，产出目录按需创建

---

## 目录结构

```
03_Projects/
├── .templates/
│   └── Project.md       # 单页项目模板
├── _Example_Project/
│   └── Project.md       # 单页示例项目
├── <Your_Project>/
│   ├── Project.md       # 项目唯一入口
│   └── Outputs/         # 有真实产出时才创建
└── README.md
```

## 项目主页

`Project.md` 集中保存：

- 项目定义与完成标准
- 当前状态与最重要的 1～3 个下一步
- Backlog、等待项和里程碑
- 进展、决策及相关内容

同一条任务或状态只维护一次，不在多个文件间流转。

---

## 项目产出目录

默认不创建空目录。出现第一份文章、方案、课程材料或设计稿时，再创建 `Outputs/`。内容明显增多后，才按实际需要拆分 `Docs/`、`Assets/`、`Meetings/` 等子目录。

---

## 使用指南

### 新建项目

1. 新建项目目录
2. 将 `.templates/Project.md` 复制为项目下的 `Project.md`
3. 填写项目定义、完成标准和第一个下一步

### 项目命名

- 使用英文或拼音
- 使用 PascalCase 或 snake_case
- 保持简洁但描述性

### 日常推进

- “下一步”始终只保留最重要的 1～3 项
- 完成任务后，在“进展与决策”留下简短记录
- 从 Backlog 补入新的下一步
- 项目结束时更新状态和完成标准，再整体归档

---

## 相关文档

- [[../00_System/Vault_Map|Vault Map]] — 整体仓库结构
- [[../04_Knowledge|Knowledge]] — 知识沉淀
- [[../05_References|References]] — 剪藏文章
