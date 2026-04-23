---
description: How AI assistants should work with this vault
tags: [system, ai, workflow]
---
# AI Workflow Principles

## 基本原则
- AI 先读上下文，再行动
- AI 尽量复用已有资料，不重复造轮子
- AI 只在明确允许时写回
- AI 写回时要结构化，不要倾倒原始聊天

## 读的优先级
1. `CLAUDE.md`
2. 相关 Context 文件
3. 相关 Project 文件
4. 相关 Knowledge 文件
5. 相关 Resource / Skill 文件

## 写的优先级
- 项目决策 → 项目 `00_Overview.md` 或 `01_Planning.md`
- 项目下一步 → 项目 `04_Next.md`
- 新规则 → `Writing_Rules.md` 或相关规则文件
- 当日进展 → 对应 Daily Note
- 长期知识 → `04_Knowledge/`

## Git Commit 格式
- 使用简洁的中文提交消息
- **不添加** `Co-Authored-By: Claude...` 协作者信息
- 示例：`git commit -m "Add new knowledge cards"`

## 不该做的事
- 不要无依据编造用户上下文
- 不要把一段聊天随便存成长期知识
- 不要在多个地方重复记录同一条规则
- 不要轻易新建平行结构