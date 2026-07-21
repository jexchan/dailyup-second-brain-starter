---
name: today
description: Generate today's prioritized plan based on daily notes, tasks, and current priorities. Use this skill whenever the user asks for today's plan, what to do today, daily priorities, planning the day, or wants a summary of today's focus areas. This skill integrates with the vault's task system and project next actions.
---

# Today: Daily Plan Generator

生成基于当前上下文的今日优先计划。这个技能整合 Daily Note、独立任务和项目下一步，输出一个清晰的今日行动计划。

---

## 任务流向理解

```
新任务 → Inbox（快速捕获）
           ↓ 处理
       Tasks.md（独立任务）或 Project.md（项目任务）
           ↓ 挑选
       Daily Note / 今日重点（今日承诺）
           ↓ 执行
       Daily Note / 今日记录 + 回到来源更新状态
```

---

## 工作流程

### Step 1: 读取核心上下文

首先读取这些文件来理解当前状态：

1. **AGENTS.md** — 理解仓库结构和导航规则
2. **01_Context/Current_Priorities.md** — 获取当前优先级方向
3. **01_Context/About_Me.md** — 了解工作方式偏好（如果存在）
4. **00_System/Task_Management_Rules.md** — 理解任务管理规则（如果存在）

### Step 2: 读取任务管理文件

1. **06_Tasks/Tasks.md** — 获取非项目任务的“下一步”和“等待”
2. **06_Tasks/Inbox.md** — 检查尚未分类的新任务

> 注意：Inbox 是快速捕获入口，每日应清空。里面的任务需要处理后移走。

### Step 3: 读取今日 Daily Note

检查 `02_Daily/YYYY-MM-DD.md`（今天的日期）

如果不存在，说明今日尚未创建 Daily Note。

提取：
- `今日重点`（如果有）
- `今日记录`（如果有）
- `一句话总结`（如果有）

### Step 4: 扫描项目下一步

使用 Glob 工具查找 `03_Projects/*/Project.md`，读取各项目主页中的“当前状态”“下一步”和“Backlog”，提取待推进事项。

优先关注：
- `下一步`中的 1～3 个当前动作
- `当前状态`中的截止日期与阻塞
- 与 `Current_Priorities` 中项目相关的任务

### Step 5: 生成优先计划

综合以上信息，将任务分为三个优先级：

- **Must Do**：来自 Tasks 或项目“下一步”、有明确截止、阻塞他人工作、或用户明确要求的任务
- **Should Do**：重要但不紧急、推进核心项目的事务
- **Could Do**：低优先级、可以延后的任务

---

## 输出格式

按照以下模板输出今日计划：

```markdown
# Today's Plan: {{YYYY-MM-DD}}

> {{一句话：今天最重要的3件事}}

---

## Top 3 Priorities (Must Do)

1. **[{{项目名}}]** {{任务描述}}
   - 来源：{{文件名}}
   - 原因：{{为什么这是今天的重点}}

2. **[{{项目名}}]** {{任务描述}}
   - 来源：{{文件名}}
   - 原因：{{为什么这是今天的重点}}

3. **[{{项目名}}]** {{任务描述}}
   - 来源：{{文件名}}
   - 原因：{{为什么这是今天的重点}}

---

## Suggested Sequence

### 上午 (深度工作)
1. {{最重要的任务}}
2. {{次重要任务}}

### 下午 (执行与协作)
1. {{中等优先级任务}}
2. {{会议/沟通相关}}

### 晚上 (收尾)
- 处理 Inbox（清空或分配任务）
- 检查今日完成情况，记录到“今日记录”
- 为明天做准备

---

## Should Do (If Time Allows)

- [ ] [{{项目}}] {{任务}} — {{来源}}
- [ ] [{{项目}}] {{任务}} — {{来源}}

---

## Could Do (Backlog)

- [ ] [{{项目}}] {{任务}} — {{来源}}
- [ ] [{{项目}}] {{任务}} — {{来源}}

---

## Risks / Distractions to Avoid

- {{风险1：什么可能让你偏离今天的目标}}
- {{风险2：需要注意的分心事项}}

---

## Priority Check

{{如果今日任务与既定优先级不一致，给出警告}}
{{如果一致，说明：今日任务与 Current_Priorities 和核心项目的聚焦一致}}

---

## Inbox Status

{{Inbox 中需要处理的任务数量，建议处理动作}}
- 待处理：{{数量}} 项
- 建议动作：{{清空 / 分配到项目 / 排期}}

---

## Notes

{{任何需要特别说明的上下文}}
```

---

## 优先级排序原则

- **明确截止或阻塞项** > **项目与独立任务的下一步** > **Inbox 待处理项** > **随机想法**
- **紧急且重要** > **重要不紧急** > **紧急不重要**
- 如果用户今天有自己的计划安排，尊重并整合，而不是完全覆盖
- 考虑用户的精力曲线：深度工作放在上午

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和上下文
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级精准检索，不要盲目扫描
- **Use the vault structure as navigation** — 利用目录结构（Context/Projects/Knowledge/Daily）来定位信息
- **Do not hallucinate missing context** — 如果文件或信息不存在，明确说明，不要编造
- **If evidence is weak, say so** — 如果数据有限或证据不足，如实指出
- **Default to read-only unless explicit confirmation is given** — 默认只读，仅获得明确确认后才写入
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级

---

## 注意事项

- **只读模式**：不要修改任何文件，仅生成计划
- 明确指出哪些任务应该避免（分心、低价值）
- 如果今日 Daily Note 不存在，可以建议用户创建
- **Inbox 不是长期仓库**：提醒用户 Inbox 中的任务应该被处理（完成、移到 Tasks/项目、或删除）
