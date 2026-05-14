---
name: cl-ideate
description: Generate, criticize, reject, and rank ideas before requirements. Use when deciding what to build, improving a product or Agent, challenging an idea, or exploring roadmap options. Does not write code or implementation plans.
---

# cl-ideate

Generate and critically evaluate ideas. The goal is not more ideas; the goal is better selection.

## Flow

1. Read `STRATEGY.md` if present.
2. Read relevant existing `docs/ideation/` artifacts if the topic overlaps.
3. Establish the ideation subject.
4. Generate candidates across multiple frames.
5. Critique every candidate.
6. Reject weak ideas explicitly.
7. Rank survivors.
8. Select one or a small number for `cl-brainstorm`.
9. Write a dated artifact under `docs/ideation/` when the decision has durable value.

If arguments include `~html`, enter HTML decision mode instead of writing the
final Markdown artifact. Read `references/html-decision-mode.md`, generate a
compact decision model under `docs/.compound-lite/drafts/ideation/`, run
`tools/render_compound_html.py`, and stop after telling the user where to open
the editor. The exported Markdown from that editor is the formal artifact.

## Output artifact

Use `docs/ideation/YYYY-MM-DD-topic.md`.

Required sections:

```md
# Ideation: Topic

## Strategy context
## Candidate ideas
## Critique
## Rejected ideas
## Ranked survivors
## Selected idea for brainstorm
## Open questions
```

## Non-goals

- Do not write requirements.
- Do not write implementation plans.
- Do not change code.
- Do not create `cl-finalize`, `~import`, or `~html-only` flows.

Read `references/idea-frames.md`, `references/critique-rubric.md`, and `references/artifact-policy.md` before writing the artifact. When using `~html`, also read `references/html-decision-mode.md`.
