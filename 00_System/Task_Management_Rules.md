---
description: Rules for managing tasks across Inbox, Tasks, Projects, and Daily Notes
tags: [system, task, gtd]
created: 2026-04-11
updated: 2026-07-21
---

# Task Management Rules

## 核心原则

> 一个任务只维护一个正式状态：先捕获，再归位，最后在 Daily Note 中记录当天的选择和结果。

## 四个位置的职责

### Inbox (`06_Tasks/Inbox.md`)

**职责：尚未分类的新任务入口。**

- 快速记录新任务
- 定期处理并尽量清空
- 不保存长期任务、等待事项、Someday 或资料链接

### Tasks (`06_Tasks/Tasks.md`)

**职责：不属于具体项目的长期任务。**

- “下一步”保存当前可执行的独立任务
- “等待”保存依赖他人或外部条件的事项
- “以后可能”保存尚未承诺的事项
- 不重复保存项目任务

### Project (`03_Projects/项目名/Project.md`)

**职责：有明确项目归属的任务。**

- “下一步”只保留当前最重要的 1～3 项
- 其余项目任务放入同页 Backlog
- 项目任务的完成状态只在项目主页更新

### Daily Note (`02_Daily/YYYY-MM-DD.md`)

**职责：当天的选择和执行记录。**

- “今日重点”列出从 Tasks 或项目中选出的 1～3 个承诺
- “今日记录”自由记录当天的进展、问题、决定、输入和想法
- “一句话总结”可选，用于收束当天最重要的结果或感受
- 不承担长期任务管理，不设置跨日“下一步”清单
- 正式任务的完成状态回到 `Tasks.md` 或项目 `Project.md` 更新

## 任务流向

```text
新任务
  ↓
Inbox
  ├─→ 属于项目 → Project.md
  ├─→ 独立任务 → Tasks.md
  ├─→ 2 分钟完成 / 删除
  └─→ 灵感或知识 → Daily / Knowledge

Tasks.md 或 Project.md
  ↓ 选择今天最重要的 1～3 项
Daily Note / 今日重点
  ↓ 执行
Daily Note / 今日记录 + 回到任务来源更新状态
```

## 判断规则

| 问题 | 放哪里 |
|---|---|
| 刚想到、尚未分类？ | `Inbox.md` |
| 属于明确项目？ | 项目 `Project.md` |
| 不属于项目但需要持续跟踪？ | `Tasks.md` |
| 今天决定投入什么？ | Daily Note“今日重点” |
| 今天实际完成、推进或发现了什么？ | Daily Note“今日记录” |
| 今天没做完怎么办？ | 保留或退回正式任务来源，不滚动复制 Daily |

## 避免的模式

- Inbox 变成长期任务仓库
- 同一个任务同时出现在 Tasks 和项目中
- Daily Note 成为第二份任务数据库
- 每天复制未完成任务，形成重复和残留
- 为了状态分类创建过多任务文件

## AI 写回规则

- 新捕获、尚未判断归属 → `06_Tasks/Inbox.md`
- 非项目任务 → `06_Tasks/Tasks.md`
- 项目任务 → 对应项目的 `Project.md`
- 用户确认的今日承诺 → 当日 Daily Note“今日重点”
- 当日结果、问题、决定和洞察 → 当日 Daily Note“今日记录”
