---
name: digest
description: Process one Inbox clipping into useful knowledge, action, or an explicit rejection.
disable-model-invocation: true
---

# Digest

Process one Inbox clipping into the smallest justified outcome. Ask the user
only for personal intent, judgment, and confirmation; handle routine reading,
analysis, comparison, formatting, linking, and routing directly.

## Principles

- Keep exactly one source in scope for the entire run.
- Digest toward the smallest justified outcome, including an explicit decision
  to create nothing.
- Preserve the user's judgment. Distinguish source claims, AI analysis, and the
  user's conclusions.
- Treat a card, project decision, action, reusable evidence, explicit rejection,
  or deliberate deferral as equally valid outcomes.
- Present proposed outcomes and receive explicit confirmation before writing,
  moving, or deleting files.
- Treat deletion as a separate destructive decision. Confirm the exact source
  path immediately before deleting it.

## Workflow

### 1. Select one clipping

If the user supplies a file, verify that it exists and read it.

If the user invokes `$digest` without a file:

1. List Markdown files directly under `05_References/01_Inbox/`.
2. If none exist, explain that Inbox is empty and ask the user to clip an
   article there first.
3. If one exists, identify it and continue.
4. If several exist, show a short numbered list and ask the user to choose one.

Treat only Markdown files directly under the Inbox as clippings; exclude
`.DS_Store`, `.gitkeep`, attachments, and nested support files.

**Completion:** Exactly one readable clipping is selected and its vault path is
known.

### 2. Read the source and relevant vault context

Read:

- the selected clipping in full;
- `05_References/README.md`;
- `01_Context/Current_Priorities.md` when populated.

Record only metadata present in the clipping or verified source, such as title,
author, source URL, publication date, clip date, and tags.

If the source is incomplete, empty, or only contains a URL, state what is
missing and ask the user for the article content or a complete clipping. Treat
unavailable material as unread.

**Completion:** The source has been read in full, available metadata recorded,
and applicable reference context loaded.

### 3. Establish the user's purpose

If the user's purpose is not already clear, ask one concise question:

> 你希望这篇内容主要帮助你解决什么问题，或者为什么想保留它？

Allow “暂时没有明确目的” as a valid answer. Keep this to one concise question.
If the purpose is already explicit, restate it briefly and continue.

**Completion:** The run has either a stated purpose or an explicit
“暂时没有明确目的” state.

### 4. Analyze internally

Without asking the user to provide additional prompts:

1. Identify the central claim and 3–5 load-bearing ideas.
2. Separate arguments, evidence, cases, quotations, and incidental detail.
3. Check whether the evidence supports the claims.
4. Identify assumptions, counterexamples, applicable conditions, and limits.
5. Search the vault using the title, central concepts, and the user's stated
   purpose; open only meaningful project, Topic, and card matches.
6. Compare the material with the relevant matches and current priorities.
7. Distinguish genuinely new value from repetition of existing knowledge.
8. Decide which, if any, durable outcomes the source supports.

Keep quotations minimal, preserve source attribution, and label source claims,
AI inferences, and user conclusions separately.

**Completion:** Every proposed takeaway is traceable to the source, every AI
inference is labeled, and overlap with relevant vault knowledge has been
assessed.

### 5. Present a digestion proposal

Use this compact structure:

```markdown
## 这篇内容讲什么
[One-sentence central claim]

## 值得带走
- [Up to 3 durable ideas, evidence items, or cases]

## 需要保留判断
- [Weak evidence, assumptions, boundaries, or disagreement]

## 与知识库的关系
- [Only meaningful links to cards, Topics, projects, or priorities]

## 建议产出
- [Smallest justified set of cards, project decisions, actions, or no output]

## 原文初步建议
- [暂留 Inbox / 移入 Library / 提炼后删除] — [Reason]
```

The proposal may explicitly recommend “无需创建卡片” or “没有长期价值.”
Avoid creating several cards from minor variations of the same idea.

Ask the user to approve or adjust the proposed knowledge and action outcomes.
State that this approval does not authorize moving or deleting the source;
source disposition is decided separately after approved outcomes are complete.

**Completion:** The user has approved, adjusted, or declined every proposed
knowledge and action outcome. No source disposition is implied by this approval.

### 6. Create only approved outcomes

After approval, read the applicable routing, naming, and writing rules under
`00_System/`, then route each outcome to its single authoritative location.
Create no artifact when the approved decision is that the source has no durable
value.

When creating cards:

1. Enforce one concept or claim per card.
2. Read the matching template under
   `04_Knowledge/00_Cards/.templates/`.
3. Preserve the source URL or clipping reference in `source`.
4. Search existing cards before creating a duplicate.
5. Add only meaningful links; do not link merely to reduce isolation.
6. If the approved content still contains multiple independent ideas, show the
   proposed split and obtain confirmation before creating multiple cards.

When updating a project or task file, show the exact proposed destination if it
was not already part of the approved plan. Do not copy one task into multiple
formal task locations.

**Completion:** Every approved artifact exists at its approved destination,
follows the applicable vault rules, preserves source attribution, and has been
checked for duplicate formal tasks or cards.

### 7. Decide the source's final location

After approved outputs are complete, revisit the original source.

Recommend `05_References/02_Library/` only when the original itself has lasting
reference value, such as:

- complete reasoning that a summary cannot replace;
- likely future citation value;
- important cases, data, charts, or primary evidence;
- expression worth studying repeatedly;
- risk that the source will disappear;
- strong relevance to a long-term direction.

“已经读过” is not a reason to keep it.

Ask the user to make a separate source-disposition decision:

1. Move it to Library.
2. Leave it in Inbox for now.
3. Remove it because its useful value has been captured or it has no value.

For removal, name the exact file and ask for explicit confirmation in a
separate turn. Never bulk-delete, infer confirmation, or remove attachments
whose ownership is unclear. Prefer a recoverable deletion mechanism when one
is available.

For a public repository, do not retain or commit an unauthorized full
copyrighted article. Prefer source metadata, a link, brief necessary excerpts,
and the user's own analysis.

**Completion:** The source has been moved, deliberately left in Inbox, or
removed after a separate exact-path confirmation. If confirmation is pending,
record the source as remaining in Inbox.

### 8. Finish briefly

Report only what actually happened:

```text
本次剪藏已处理完成：
- [created or updated outcome]
- [source disposition]
```

If the source remains in Inbox or a proposed output was declined, say so
plainly.

**Completion:** The report names every artifact actually created or updated and
the source's actual final state.
