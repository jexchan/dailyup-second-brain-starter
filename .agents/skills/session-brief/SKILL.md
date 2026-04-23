---
name: session-brief
description: Generate a concise working-session brief from this Obsidian vault by reading AGENTS.md, stable context, recent daily notes, current tasks, and active project next actions. Use this skill when starting a new session, resuming work after a break, or needing a quick refresher on current priorities and what to focus on next.
disable-model-invocation: true
---

# Session Brief

Create a focused brief for the current work session using this Obsidian vault.

## When to use

Use this skill when the user wants a quick understanding of:
- current priorities
- active projects
- recent reflections
- open loops
- what to focus on right now

**This is a read-only skill.**
Do not write back to the vault.

## First step

Always read `AGENTS.md` first.

Use it to understand:
- the vault structure
- routing rules
- write/read expectations
- key files and folders

If `AGENTS.md` specifies more precise instructions, follow it.

## Files to read

### Required
- `AGENTS.md`

### Core context
Read the most relevant files in:
- `01_Context/`

Prefer:
- `About_Me.md`
- `Mission_and_Vision.md`
- `Brand_Voice.md`
- `Audience_Profiles.md`
- `Current_Priorities.md`

### Recent continuity
Read the most recent 7 files in:
- `02_Daily/`

If fewer than 7 exist, read what is available.

### Current tasks
Read if present:
- `06_Tasks/This_Week.md`
- `06_Tasks/Inbox.md`

### Active projects
Scan `03_Projects/` for likely active projects.
For each relevant active project, prefer:
1. `Overview.md`
2. `Next_Actions.md`
3. `Decisions.md`

Do not scan archived or irrelevant material unless needed.

## What to produce

Return a structured brief with these sections:

### 1. Current Focus
Summarize the most likely current focus areas.

### 2. Active Projects
List the most active projects with one-line status notes.

### 3. Recent Signals
Summarize themes, repeated concerns, or reflections from recent daily notes.

### 4. Open Loops
List unfinished items, tensions, pending decisions, or things likely needing attention.

### 5. Suggested Session Focus
Recommend the best focus for this session based on priorities, recency, and momentum.

## Style

Be concise, structured, and useful.
Prefer synthesis over raw listing.
Do not hallucinate missing context.
If evidence is weak, say so.

---

## 通用规则

- **Always read AGENTS.md first** — 首先读取仓库导航规则和结构
- **Prefer focused retrieval over scanning everything blindly** — 按目录优先级搜索，不要盲目扫描整个 vault
- **Use the vault structure as navigation** — 利用 Daily > Projects > Knowledge 优先级构建时间线
- **Do not hallucinate missing context** — 如果主题在 vault 中没有记录，明确说明，不要编造历史
- **If evidence is weak, say so** — 如果证据稀少或时间线不完整，如实指出
- **Default to read-only unless explicit confirmation is given** — 默认只读分析，不修改任何文件
- **Return structured output with headings** — 使用结构化输出，带清晰的标题层级
