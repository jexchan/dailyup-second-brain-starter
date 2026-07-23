# Card Writing Rules

- Use the selected template as the authority for frontmatter fields and body
  sections.
- Keep `type: card`; set `card_type` to the mapped type.
- Use valid YAML. Quote strings when quoting avoids ambiguity, including values
  containing `: `, brackets, leading special characters, or YAML-like booleans
  and dates. Keep `related` in the template's list format.
- Use the original URL alone in `source` when one exists. Without a URL, use a
  concise source name. Put explanatory context in the body.
- Use `[[wikilinks]]` for internal links and Markdown links for external pages.
- Use a concise, stable filename: `{card_type}_{title}.md`.
- Preserve the user's wording where it carries meaning; make claims concrete,
  scoped, and reusable.
