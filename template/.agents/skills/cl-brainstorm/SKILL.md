---
name: cl-brainstorm
description: Turn a selected idea into a requirements document. Use when user-facing behavior, scope, flows, success criteria, or Agent behavior needs clarification before planning. Does not decide implementation details or write code.
---

# cl-brainstorm

Define WHAT to build before `cl-plan` defines HOW to build it.

## Flow

1. Read `STRATEGY.md`.
2. Read the relevant `docs/ideation/` artifact when available.
3. Ask for or identify the selected idea.
4. Clarify problem, users, user-facing behavior, scope, non-goals, success criteria, flows, and edge cases.
5. If Agent behavior is involved, load the Agent-native lens.
6. Write a dated requirements document under `docs/brainstorms/`.

If arguments include `~html`, enter HTML decision mode instead of writing the
final requirements Markdown artifact. Read `references/html-decision-mode.md`,
generate a compact decision model under `docs/.compound-lite/drafts/brainstorms/`,
run `tools/render_compound_html.py`, and stop after telling the user where to
open the editor. The exported Markdown from that editor is the formal artifact.

## Output artifact

Use `docs/brainstorms/YYYY-MM-DD-topic-requirements.md`.

Required sections:

```md
# Requirements: Topic

## Origin
## Problem
## User-facing behavior
## Scope
## Non-goals
## Key flows
## Edge cases
## Success criteria
## Agent-specific behavior
## Open questions
```

## Boundaries

- Do not choose implementation architecture unless the requirement itself is architectural.
- Do not write code.
- Do not skip scope and non-goals.
- Do not create `cl-finalize`, `~import`, or `~html-only` flows.

Read `references/product-pressure-test.md`, `references/requirements-template.md`, and `references/agent-native-lens.md` when relevant. When using `~html`, also read `references/html-decision-mode.md`.
