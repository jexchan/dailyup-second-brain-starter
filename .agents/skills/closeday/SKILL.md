---
name: closeday
description: End-of-day review and reflection. Use this skill when the user asks to close the day, end the day, do a daily review, reflect on today, summarize today's work, or wrap up the day. This skill reads today's Daily Note and projects' Next Actions to generate a structured review with completed items, insights, and tomorrow's priorities.
---

# Close Day: Daily Review

回顾一天的工作，总结进展、捕获经验教训、识别未完成事项并规划明日延续。

---

## 工作流程

### Step 1: 读取核心上下文

首先读取 `AGENTS.md` 理解仓库结构和写作规则。

确认当前日期和 vault 路径。

### Step 2: 读取今日 Daily Note

从 `02_Daily/` 目录读取今日日期对应的 `.md` 文件：
- 文件名格式：`YYYY-MM-DD.md`
- 读取模板参考：`02_Daily/.templates/Daily_Note.md`（如果存在）

### Step 3: 读取项目 Next_Actions（如存在）

检查 `03_Projects/` 下各项目的 `04_Next.md`，识别今日可能推进的项目任务。

### Step 4: 读取本周任务（可选）

读取 `06_Tasks/This_Week.md`，对比今日进展与本周重点。

### Step 5: 分析并生成回顾

基于今日 Daily Note 的内容，分析：

- **今日完成**：勾选完成的任务、产出的内容、做出的决策
- **今日推进**：即使未完成但有推进的事项
- **新想法**：在"今日思考"中出现的洞察
- **未完成事项**：未勾选的任务、遇到的问题
- **可延续内容**：值得放入明日或项目 Next_Actions 的内容

### Step 6: 生成一日总结

生成一句话的今日总结（适合作为今日记录的结尾）。

---

## 输出格式

按照以下模板输出：

```markdown
# 🌅 每日回顾 - {{日期}}

## 今日完成
> 真正划掉/完成的事情

- {{完成的任务1}}
- {{完成的任务2}}

## 今日推进
> 有进展但未完全完成的事项

- {{推进的事项1}}
- {{推进的事项2}}

## 新想法与洞察
> 值得保留的思考

- {{想法1}}
- {{想法2}}

## 未完成事项
> 今日未完成但仍需跟进的

- {{未完成1}}
- {{未完成2}}

## 延续至明日
> 明天优先要做的

1. {{明日优先事项1}}
2. {{明日优先事项2}}
3. {{明日优先事项3}}

---

## 📝 一日总结

{{一句话总结今日}}

---

是否要将此回顾写入今日 Daily Note？
- 输入 "yes" 或 "写入" — 追加到今日 Daily Note
- 输入其他 — 仅展示，不写入
```

---

## 写回规则

- **默认只读**：仅展示回顾内容，不自动写入
- **确认后写入**：用户明确确认后，才追加到今日 Daily Note
- 追加位置：在今日 Daily Note 末尾添加 `---` 分隔线和回顾内容

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和写作规范
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级精准检索，不要盲目扫描
- **Use the vault structure as navigation** — 利用目录结构定位 Daily Note 和项目文件
- **Do not hallucinate missing context** — 如果今日记录不存在，明确说明，不要编造
- **If evidence is weak, say so** — 如果今日内容很少，如实反映，不强求充实
- **Default to read-only unless explicit confirmation is given** — 默认只读展示，用户确认后才写入
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级

---

## 输出要求

- 使用中文
- 结构清晰，分块明确
- 突出"完成"而非"忙碌"
- 洞察和思考要简洁可复用
- 明日延续要具体可执行

---

## 常见问题处理

**Q: 如果今日 Daily Note 不存在怎么办？**
A: 提示用户先创建今日 Daily Note，或基于模板自动创建

**Q: 如果今日内容很少怎么办？**
A: 诚实输出，不强求"充实"。少量进展也是进展

**Q: 如何判断哪些应该延续至明日？**
A: 优先级判断：(1) 今日未完成的重点事项 (2) 跨天依赖的任务 (3) 用户明确标注的"下一步"
