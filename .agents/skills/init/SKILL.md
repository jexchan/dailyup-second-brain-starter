---
name: init
description: Welcome a new user to the DailyUp Second Brain Starter, give a concise guided tour, and safely remove template example files after explicit confirmation. Use only when the user explicitly invokes `/init`.
---

# Initialize the Vault

Guide a new user through a short, friendly initialization. Keep the entire experience simple and concise. Do not create a Daily Note or modify personal context files.

## 1. Check initialization state

Read `AGENTS.md`, then run this read-only command from the Vault root:

```bash
bash .agents/skills/init/scripts/cleanup_examples.sh --list
```

Treat the numeric `TOTAL` line as the initialization signal.

- If `TOTAL=0`, say only that initialization is already complete, then suggest filling in `01_Context/About_Me.md` and `01_Context/Current_Priorities.md` or running `/card-creator`. Stop there.
- If examples exist, continue with the onboarding flow.

## 2. Welcome the user

Open with this concise idea, adapting the wording naturally without expanding it into a long explanation:

> 欢迎来到 DailyUp Second Brain。这不只是一个笔记仓库，而是一个让你与 AI 共同维护上下文、项目、知识和行动的长期工作空间。

## 3. Give a minimal guided tour

Read the files that exist from the lists below. Present each selected file as a clickable path with one short sentence explaining what it demonstrates. Do not summarize its full contents.

Core entry points:

- `QUICK_START.md`
- `01_Context/About_Me.md`
- `01_Context/Current_Priorities.md`

Representative examples:

- `02_Daily/_EXAMPLE_2025-01-01.md`
- `03_Projects/_Example_Project/Project.md`
- One `_EXAMPLE_*` file from `04_Knowledge/00_Cards/`
- `04_Knowledge/01_Topics/_EXAMPLE_Learning_Science.md`
- `05_References/01_Inbox/_EXAMPLE_clip.md`

Keep the tour compact: group the core files together and the examples together.

## 4. Ask before cleanup

Show the complete target list returned by `--list`, state the total, and ask one direct question: whether to delete all listed template examples now.

Stop and wait for the user's answer. Do not interpret silence, ambiguity, or an unrelated reply as consent. Do not run any deletion command in the same turn that asks for confirmation.

The cleanup scope must remain limited to:

- `_EXAMPLE_*` entries found by the helper in its designated template directories
- `03_Projects/_Example_Project/`

Never delete other paths merely because their names contain `example`.

## 5. Handle the answer

If the user clearly confirms, run:

```bash
bash .agents/skills/init/scripts/cleanup_examples.sh --clean --yes
```

Report whether cleanup completed and whether any targets remain. If cleanup fails, preserve the error details and do not improvise broader deletion commands.

If the user declines, do not delete anything. Mention that `/init` can be run again later.

In either case, close with two next steps:

1. Fill in `01_Context/About_Me.md` and `01_Context/Current_Priorities.md`.
2. Run `/card-creator` to create a first knowledge card.

Mention `/today` only as an optional next step for planning the day and creating the Daily Note.
