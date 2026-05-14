# HTML Decision Mode

Use this reference when the user passes `~html`.

In `~html` mode, do not write the final `docs/ideation/*.md` artifact.

Instead:

1. Build a compact decision model as JSON.
2. Write it to `docs/.compound-lite/drafts/ideation/YYYY-MM-DD-topic-model.json`.
3. Run:

```bash
python3 tools/render_compound_html.py decision --type ideation --model docs/.compound-lite/drafts/ideation/YYYY-MM-DD-topic-model.json --out docs/.compound-lite/drafts/ideation/YYYY-MM-DD-topic-editor.html
```

4. Tell the user to open the HTML editor.
5. The user exports Markdown directly from the editor and saves it under `docs/ideation/`.

The HTML editor must include strategy context, candidate ideas as cards, critique, rejected ideas, ranked survivors, selected idea for brainstorm, open questions, Export Markdown, and Copy Markdown.

The exported Markdown is the final artifact. There is no `cl-finalize`, `~import`, or `~html-only` flow.

Generated HTML and JSON drafts are temporary human-facing files, not Agent source of truth.
