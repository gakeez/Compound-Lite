# HTML Decision Mode

Use this reference when the user passes `~html`.

In `~html` mode, do not write a durable verification Markdown artifact automatically.

Instead:

1. Build a compact decision model as JSON.
2. Write it to `docs/.compound-lite/drafts/verify/YYYY-MM-DD-topic-verify-model.json`.
3. Run:

```bash
python3 tools/render_compound_html.py decision --type verify --model docs/.compound-lite/drafts/verify/YYYY-MM-DD-topic-verify-model.json --out docs/.compound-lite/drafts/verify/YYYY-MM-DD-topic-verify-editor.html
```

4. Tell the user to open the HTML editor.
5. The user exports Markdown directly from the editor and chooses whether to save the verification report.

The HTML editor must include intent, changed files, verification commands, test results, findings, Agent behavior eval, blocking issues, non-blocking issues, recommended next action, Export Markdown, and Copy Markdown.

Use editable `table` sections for findings, commands, and test results. Findings should include severity, evidence, suggested fix, and blocking status.

The exported Markdown is the report. There is no `cl-finalize`, `~import`, or `~html-only` flow.

Generated HTML and JSON drafts are temporary human-facing files, not Agent source of truth.
