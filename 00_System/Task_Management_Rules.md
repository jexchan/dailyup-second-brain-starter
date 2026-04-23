---
description: Rules for managing tasks across Inbox, Daily Notes, and Projects
tags: [system, task, gtd]
created: 2026-04-11
---

# Task Management Rules

## 核心原则

> 一个任务只放一个地方，职责清晰，流动顺畅。

## 两个位置的职责

### Inbox (`06_Tasks/Inbox.md`)
**职责：纯粹的任务入口，快速捕获**

- ✅ 快速记录任何新想法、新任务
- ✅ 临时存放待处理事项
- ❌ 不要放长期任务
- ❌ 不要放已有项目归属的任务

**处理频率**：每日一次，清空 Inbox

**处理选项**（2分钟规则）：
1. **Do** → 2分钟能做完，立即做
2. **Delegate** → 委托给他人
3. **Defer** → 移到项目 04_Next 或排期到 Daily Note
4. **Delete** → 不值得做，删除
5. **Someday** → 移到 Someday/Maybe

---

### Daily Note (`02_Daily/YYYY-MM-DD.md`)
**职责：今天的选择 —— 聚焦当天**

- `今日重点`：今天要做的 1-3 件事（从 Inbox/Project 选取）
- `下一步`：今天未完、明天继续的（睡前移走）
- ✅ 当天聚焦，避免分心
- ❌ 不要管理长期任务
- ❌ 不要放未分配的项目任务

**日终处理**：
- 完成的 → 记录到 `今日进展`
- 未完的 → 移回项目或排期到明天
- 不要让任务在 Daily Note 中堆积

---

### Project Next (`03_Projects/项目名/04_Next.md`)
**职责：项目级待办，有归属的任务**

- 所有有明确项目归属的任务
- 长期存在，有上下文
- 从 Inbox 处理后移入
- Daily Note 从这里选取今天要做的

---

## 任务流向图

```
新任务/想法
    ↓
Inbox (快速捕获)
    ↓ 每日处理
    ├─→ 2分钟 → 立即完成
    ├─→ 不值得 → 删除
    ├─→ 有项目 → Project/04_Next.md
    └─→ 今天做 → Daily Note/今日重点
              ↓ 完成
          Daily Note/今日进展
```

```
Project/04_Next.md
    ↓ 每日挑选
Daily Note/今日重点
    ↓ 完成
Daily Note/今日进展
```

---

## 判断规则

| 问题 | 放哪里 |
|------|--------|
| 刚想到的新任务？ | Inbox |
| 这个任务属于哪个项目？ | Project/04_Next.md |
| 今天一定要做的是什么？ | Daily Note/今日重点 |
| 这个任务没做完怎么办？ | 移回项目或明天 Daily Note |
| 长期跟踪的项目任务？ | Project/04_Next.md，不是 Inbox |

---

## 避免的模式

- ❌ Inbox 变成长期任务仓库
- ❌ Daily Note 堆积大量未完成任务
- ❌ 同一个任务在多处重复
- ❌ 不知道任务该放哪里就随便放

---

## AI 写回规则

当 AI 需要记录任务时：
- 新捕获的任务 → `06_Tasks/Inbox.md`
- 项目相关任务 → `03_Projects/项目名/04_Next.md`
- 今天确认要做的 → 当日 Daily Note `今日重点`
- 完成的任务 → 当日 Daily Note `今日进展`
