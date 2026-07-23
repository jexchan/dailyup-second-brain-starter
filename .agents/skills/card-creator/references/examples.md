# Type Decision Examples

Use these examples only when the type remains ambiguous after applying the map.

| Input | Type | Reason |
|---|---|---|
| `从《原则》中学到：痛苦加反思带来进步。` | `insight` | The reusable object is the claim, not the book passage. |
| `记录《原则》第三章对痛苦加反思的论述。` | `book-note` | The reusable object is a passage tied to one book. |
| `创建阅读前检查清单。` | `checklist` | The reusable object is repeatable verification steps. |
| `整理学习科学主题的已有卡片导航。` | `moc` | The requested object is navigation, not an atomic claim. |
