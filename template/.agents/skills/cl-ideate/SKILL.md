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

Read `references/idea-frames.md`, `references/critique-rubric.md`, and `references/artifact-policy.md` before writing the artifact.
