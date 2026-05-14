# HTML Decision Mode

Use this reference when the user passes `~html`.

In `~html` mode, do not write the final `docs/plans/*.md` plan artifact.

Instead:

1. Build a compact decision model as JSON.
2. Write it to `docs/.compound-lite/drafts/plans/YYYY-MM-DD-topic-plan-model.json`.
3. Run:

```bash
python3 tools/render_compound_html.py decision --type plan --model docs/.compound-lite/drafts/plans/YYYY-MM-DD-topic-plan-model.json --out docs/.compound-lite/drafts/plans/YYYY-MM-DD-topic-plan-editor.html
```

4. Tell the user to open the HTML editor.
5. The user exports Markdown directly from the editor and saves it under `docs/plans/`.

The HTML editor must include origin, goal, scope, non-goals, project discovery, implementation plan, files likely to change, verification, risks, Agent-native considerations, rollback/recovery, open questions, Export Markdown, and Copy Markdown.

Use editable `table` sections for verification cases and risk items. Risk rows should include severity, blocking status, and mitigation.

The exported Markdown is the final artifact. There is no `cl-finalize`, `~import`, or `~html-only` flow.

Generated HTML and JSON drafts are temporary human-facing files, not Agent source of truth.
