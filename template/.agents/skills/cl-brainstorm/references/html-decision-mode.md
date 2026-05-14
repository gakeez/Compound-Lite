# HTML Decision Mode

Use this reference when the user passes `~html`.

In `~html` mode, do not write the final `docs/brainstorms/*.md` requirements artifact.

Instead:

1. Build a compact decision model as JSON.
2. Write it to `docs/.compound-lite/drafts/brainstorms/YYYY-MM-DD-topic-requirements-model.json`.
3. Run:

```bash
python3 tools/render_compound_html.py decision --type brainstorm --model docs/.compound-lite/drafts/brainstorms/YYYY-MM-DD-topic-requirements-model.json --out docs/.compound-lite/drafts/brainstorms/YYYY-MM-DD-topic-requirements-editor.html
```

4. Tell the user to open the HTML editor.
5. The user exports Markdown directly from the editor and saves it under `docs/brainstorms/`.

The HTML editor must include problem, user-facing behavior, scope, non-goals, key flows, edge cases, success criteria, Agent-specific behavior, open questions, Export Markdown, and Copy Markdown.

The exported Markdown is the final artifact. There is no `cl-finalize`, `~import`, or `~html-only` flow.

Generated HTML and JSON drafts are temporary human-facing files, not Agent source of truth.
