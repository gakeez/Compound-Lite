---
name: cl-review
description: Review Compound Lite planning artifacts before moving to the next planning stage. Use after cl-ideate, cl-brainstorm, cl-design, or cl-plan. Read-only by default; does not replace cl-verify.
---

# cl-review

Review planning work before the workflow advances. The goal is to catch drift,
missing decisions, unconfirmed assumptions, and contradictions while the work is
still cheap to correct.

## Flow

1. Read `AGENTS.md`.
2. Read `STRATEGY.md` when product direction or Agent behavior matters.
3. Read the current planning artifact under `docs/ideation/`, `docs/brainstorms/`, `docs/designs/`, or `docs/plans/`.
4. Read the immediately preceding planning artifacts when they exist.
5. Compare the artifact against confirmed user decisions, strategy, scope, non-goals, UX constraints, and implementation boundaries.
6. Identify conflicts, scope drift, missing decisions, premature implementation detail, and assumptions that still require user confirmation.
7. Report the review in chat by default.
8. Stop for user confirmation before the next planning stage.

## Output

Default output is chat only. Do not write a review artifact unless the user
explicitly asks for one.

```text
Verdict:
Confirmed decisions:
Conflicts:
Scope drift risks:
Missing decisions:
Required changes:
User confirmation needed:
Recommended next stage:
```

## Boundaries

- Do not write code.
- Do not modify planning artifacts unless the user explicitly asks for edits.
- Do not create durable review documents by default.
- Do not introduce new product direction, scope, requirements, UX decisions, or implementation plans.
- Do not advance from one planning stage to the next without user confirmation.
- Do not use `cl-review` as an extra gate after `cl-work`; use `cl-verify` for implemented work.
- Do not replace `cl-verify`; implementation verification remains `cl-work` then `cl-verify`.

## Planning Stages

Use `cl-review` after these planning stages:

```text
cl-ideate
  -> cl-review
  -> cl-brainstorm   # requirements stage
  -> cl-review
  -> cl-design
  -> cl-review
  -> cl-plan
  -> cl-review
  -> cl-work
  -> cl-verify
```
