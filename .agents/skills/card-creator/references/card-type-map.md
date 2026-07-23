# Card Type Map

Use this file as the sole mapping from card type to template. `source` means the
template includes a frontmatter source field; `template-defined` means follow
the existing template's fields.

| Type | Use for | Template | Source policy |
|---|---|---|---|
| `atomic-habit` | repeatable identity-based habit | `Atomic_Habit_Card.md` | template-defined |
| `book` | a whole book as an object | `Book_Card.md` | template-defined |
| `book-note` | a passage, chapter, or annotation tied to one book | `Book_Note_Card.md` | source |
| `checklist` | repeatable verification steps | `Checklist_Card.md` | source |
| `counterintuitive` | a claim that reverses a common expectation | `Counterintuitive_Card.md` | source |
| `course` | a course or learning programme | `Course_Card.md` | source |
| `insight` | a reusable claim or interpretation | `Insight_Card.md` | source |
| `mentalmodel` | a reusable reasoning or decision model | `Mental_Model_Card.md` | source |
| `moc` | navigation across an existing topic | `MOC_Card.md` | template-defined |
| `opensource` | an open-source project | `Opensource_Card.md` | source |
| `paradox` | a productive apparent contradiction | `Paradox_Card.md` | source |
| `person` | a person worth tracking | `Person_Card.md` | source |
| `prompt` | a reusable prompt | `Prompt_Card.md` | source |
| `question` | an open question worth revisiting | `Question_Card.md` | source |
| `quote` | a verbatim quotation with attribution | `Quote_Card.md` | source |
| `resource` | a reusable external resource | `Resource_Card.md` | source |
| `story` | a case or narrative with a reusable lesson | `Story_Card.md` | source |
| `subscription` | a service subscription to track | `Subscription_Card.md` | template-defined |
| `techstack` | an application's technical stack | `Tech_Stack_Card.md` | source |
| `term` | a defined term or concept | `Term_Card.md` | source |
| `tip` | an actionable technique | `Tip_Card.md` | source |
| `tool` | a software tool or service | `Tool_Card.md` | source |

Use these cues only after identifying the core object:

- whole book → `book`; book passage or annotation → `book-note`; reusable idea
  from any source → `insight`.
- recurring steps → `checklist`; repeated behavior design → `atomic-habit`;
  one software action → `tip`.
- application or service → `tool`; open-source repository → `opensource`;
  a stack of technologies → `techstack`.
- navigation across existing notes → `moc`; a question worth retaining →
  `question`; a quoted statement → `quote`.
