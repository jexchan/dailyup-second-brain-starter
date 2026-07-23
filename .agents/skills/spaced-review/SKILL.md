---
name: spaced-review
description: Manage active-recall spaced review for Obsidian knowledge cards. Use when the user asks what to review today, wants to enroll a card, or gives an explicit again/hard/good/easy rating for an identified review card.
---

# Spaced Review

Use **主动提取**: the user recalls before opening the card, receives correction,
then gives a rating that schedules the next review.

## Workflow

### 1. List due cards

Run:

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py due --limit 20
```

Present the ordered cards using `references/output-format.md`. Let the user
select one card or explicitly end the session. When no cards are due, suggest
enrolling 3–5 core cards rather than bulk-enrolling the vault.

**Completion:** The user sees the due list and selects one card or ends the
session.

### 2. Run one active-recall review

For the selected card:

1. Read the card and ask one retrieval prompt without revealing its answer.
2. Wait for the user's response.
3. Give concise correction after the attempt.
4. Ask for `again`, `hard`, `good`, or `easy`.
5. Record the explicit rating for that exact card.

Use these mappings when the user gives Chinese feedback: 忘了 → `again`; 想起一
部分/有点难 → `hard`; 能讲清楚 → `good`; 很熟且能迁移应用 → `easy`. If the
target card is not explicit in the current review turn, ask which card to
update.

Run:

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py review "04_Knowledge/00_Cards/card_name.md" --rating good
```

Add `--note` only for user-provided feedback worth retaining. The script updates
frontmatter and appends the note to the card's SRS review log.

**Completion:** One identified enrolled card has an explicit rating, and the
stored next due date and interval are reported.

### 3. Enroll a card

Confirm the exact card path and choose `core`, `normal`, or `low` priority.
The default priority is `normal`; use `core` only for concepts the user needs to
retain long term.

Run:

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py enroll "04_Knowledge/00_Cards/card_name.md" --priority core
```

Enrollment sets the card to `learning`, with a one-day interval and a next due
date tomorrow. Review requires prior enrollment.

**Completion:** The exact card path, priority, and next due date are confirmed
from script output.

## Boundaries

- The script only enrolls or reviews Markdown cards directly under
  `04_Knowledge/00_Cards/`.
- Review one card at a time; do not apply a rating to an ambiguous target.
- The script is the authority for scheduling calculations. Read
  `references/review-fields.md` when explaining stored review state.
