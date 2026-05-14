---
name: cl-render
description: Render an existing Compound Lite Markdown artifact as a read-only local HTML view. Use after an artifact is finalized when the user wants a browser-friendly reading view. Does not create or edit source artifacts.
---

# cl-render

Render finalized Markdown artifacts into read-only HTML views.

## Flow

1. Read the requested Markdown artifact.
2. Confirm it is an existing source-of-truth Markdown artifact, not a generated HTML draft.
3. Choose an output path under `docs/.compound-lite/views/`, mirroring the artifact folder when helpful.
4. Run:

```bash
python3 tools/render_compound_html.py view --source <artifact.md> --out <view.html>
```

5. Tell the user the generated HTML path.

## Boundaries

- Do not edit the source Markdown artifact.
- Do not treat generated HTML views as source of truth.
- Do not use `cl-render` for pre-decision editing; use the originating skill's `~html` mode instead.
- Do not add external dependencies or CDN assets.

## Output

Default output path:

```text
docs/.compound-lite/views/<artifact-folder>/<artifact-name>.html
```

Generated HTML is a local reading aid only. Future agents should read the Markdown artifact, not the HTML view.
