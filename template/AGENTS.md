# AGENTS.md

## Compound Lite working agreements

- Use Compound Lite artifacts as source of truth for non-trivial product and engineering work.
- Keep automation at Level 1: local file edits, local tests, and local artifacts are allowed; commit, push, PR creation, deploy, and external system mutation are not automatic.
- For existing projects, run `cl-onboard` before adopting the workflow broadly.
- For product or Agent direction, use `STRATEGY.md` as the durable anchor.
- For ideas that need criticism, use `cl-ideate` and save substantial outputs in `docs/ideation/`.
- For unclear user-facing behavior, use `cl-brainstorm` as the requirements stage before planning.
- For user-facing UI/UX changes, use `cl-design` after confirmed requirements and before `cl-plan`.
- Planning stages must use `cl-review` before moving to the next planning stage.
- For non-trivial implementation, use `cl-plan` before `cl-work`.
- After substantial implementation, use `cl-verify` as an independent verification pass.
- Record durable solved-problem learnings with `cl-compound` in `docs/solutions/`.
- When Agent behavior changes, consider `docs/evals/` and define success/failure examples.

## Compound Lite planning flow

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

`cl-review` is a read-only planning gate by default. It reviews consistency
across strategy, user-confirmed decisions, and planning artifacts, then stops
for user confirmation. It does not replace `cl-verify`, and execution stages do
not need an extra Review gate beyond `cl-work -> cl-verify`.

## HTML decision editors

- Planning-oriented skills may support `~html` mode for human-facing decision and editing interfaces.
- `~html` mode creates temporary HTML editors under `docs/.compound-lite/drafts/`.
- These HTML editors are not source of truth.
- The user exports Markdown from the HTML editor. The exported Markdown file is the formal artifact.
- When a Markdown artifact exists, read the Markdown artifact instead of generated HTML or JSON drafts.
- Do not use generated HTML as context unless the task is specifically about editing the HTML renderer or debugging the HTML editor.
- Do not create `cl-finalize`, `~import`, or `~html-only` flows. Exported Markdown is final.

## Safety boundaries

Do not automatically:

- Commit, push, open PRs, or deploy.
- Add new production dependencies without explicit approval.
- Modify production data or external systems.
- Expand Agent tool permissions without explicit approval.
- Store PII, secrets, or user-private content in artifacts.

## Completion summary

For substantial work, finish with:

```text
Changed:
Verified:
Risks:
Artifacts:
Next:
```
