---
name: weekly-review
description: Weekly review to check progress across projects, courses, and products. Use this skill when the user asks for weekly review, weekly recap, week summary, check weekly progress, review the week, or wants to see what happened this week. This skill reads the week's Daily Notes and project Next_Actions to generate a structured weekly summary with completed items, ongoing work, and next week's priorities.
---

# 周回顾 (Weekly Review)

每周一次的回顾，检查项目、课程、产品等事项的推进情况，为下周计划提供依据。

---

## 工作流程

### Step 1: 确定回顾范围

首先询问或确定要回顾的周范围：
- 默认：本周一到今天
- 用户可指定具体日期范围

### Step 2: 读取核心上下文

读取 `AGENTS.md` 理解仓库结构和写作规则。

### Step 3: 读取本周 Daily Notes

从 `02_Daily/` 目录读取本周所有日期对应的 `.md` 文件。

### Step 4: 读取项目 Next_Actions

扫描 `03_Projects/` 下所有项目的 `04_Next.md`，识别：
- 本周完成的任务
- 本周推进的事项
- 仍在进行中的工作
- 遇到的阻塞问题

### Step 5: 读取任务清单

读取 `06_Tasks/Inbox.md`，识别：
- 本周完成的任务
- 本周新增的任务
- 待处理的任务

### Step 6: 分析并生成周回顾

基于收集的信息，分析：
- **本周完成**：真正划掉/完成的事情
- **本周推进**：有进展但未完全完成的事项
- **新增事项**：本周新增的项目、任务、想法
- **遇到的问题**：阻塞、困惑、需要后续处理的
- **各项目进展**：按项目分类的进展摘要

### Step 7: 生成下周建议

基于本周进展和未完成事项，给出：
- 下周重点建议
- 需要继续推进的事项
- 需要处理的阻塞问题

---

## 输出格式

按照以下模板输出：

```markdown
# 周回顾 - {{周范围}}

## 本周概览

> 一句话总结本周：{{一句话总结}}

---

## 本周完成
> 真正划掉/完成的事情

### 项目进展
- {{项目1}}：{{完成内容}}
- {{项目2}}：{{完成内容}}

### 任务清理
- {{完成的任务1}}
- {{完成的任务2}}

---

## 本周推进
> 有进展但未完全完成的事项

### 持续进行的项目
- {{项目1}}：{{推进情况}}
- {{项目2}}：{{推进情况}}

### 课程/内容创作
- {{课程1}}：{{进展}}
- {{内容1}}：{{进展}}

---

## 新增事项
> 本周新增的项目、任务、想法

- {{新增1}}
- {{新增2}}

---

## 遇到的问题
> 阻塞、困惑、需要后续处理的

- {{问题1}}
- {{问题2}}

---

## 下周建议

### 优先重点
1. {{重点1}}
2. {{重点2}}
3. {{重点3}}

### 需要解决的阻塞
- {{阻塞1}}
- {{阻塞2}}

---

## 按项目分类

### {{项目名称1}}
- **完成**：{{完成内容}}
- **推进**：{{推进内容}}
- **下一步**：{{下一步}}

### {{项目名称2}}
- **完成**：{{完成内容}}
- **推进**：{{推进内容}}
- **下一步**：{{下一步}}
```

---

## 写回规则

- **默认只读**：仅展示回顾内容，不自动写入
- **确认后写入**：用户明确确认后，写入到 `02_Daily/` 目录，文件名格式为 `Week_YYYY-Www.md`（如 `Week_2026-W16.md`）

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和写作规范
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级精准检索
- **Do not hallucinate missing context** — 如果某天记录不存在，跳过并说明
- **If evidence is weak, say so** — 如果本周内容很少，如实反映
- **Default to read-only unless explicit confirmation is given** — 默认只读展示，用户确认后才写入
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级

---

## 输出要求

- 使用中文
- 结构清晰，分块明确
- 突出"完成"而非"忙碌"
- 按项目分类，便于追踪
- 下周建议要具体可执行

---

## 常见问题处理

**Q: 如果某天 Daily Note 不存在怎么办？**
A: 跳过该天，在输出中说明缺失的日期

**Q: 如果本周内容很少怎么办？**
A: 诚实输出，不强求"充实"。少量进展也是进展

**Q: 如何判断哪些应该是下周重点？**
A: 优先级判断：(1) 本周未完成的重要事项 (2) 有明确截止日期的任务 (3) 项目 Next_Actions 中标注优先的事项
