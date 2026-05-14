# HTML Decision Mode

Use this reference when the user passes `~html`.

`cl-strategy ~html` is for major strategy revisions that benefit from browser-based comparison and editing. For ordinary strategy maintenance, update `STRATEGY.md` directly after confirmation.

In `~html` mode, do not write `STRATEGY.md`.

Instead:

1. Build a compact decision model as JSON.
2. Write it to `docs/.compound-lite/drafts/strategy/strategy-model.json`.
3. Run:

```bash
python3 tools/render_compound_html.py decision --type strategy --model docs/.compound-lite/drafts/strategy/strategy-model.json --out docs/.compound-lite/drafts/strategy/strategy-editor.html
```

4. Tell the user to open the HTML editor.
5. The user exports Markdown directly from the editor and uses it to replace or update `STRATEGY.md`.

The HTML editor must include target problem, approach, primary users, key metrics, tracks, not working on, Agent-native assumptions, tradeoffs, open questions, Export Markdown, and Copy Markdown.

The exported Markdown is the strategy artifact. There is no `cl-finalize`, `~import`, or `~html-only` flow.

Generated HTML and JSON drafts are temporary human-facing files, not Agent source of truth.
