# Using Compound Lite

## For an existing project

1. Apply the template:

```bash
python3 tools/apply.py /path/to/project --mode existing
```

2. Open the project in Codex.

3. Run:

```text
$cl-onboard
```

4. Ask it to start with a read-only scan and not modify application code.

5. Merge any files placed in `.compound-lite-incoming/`.

## For a new project

1. Apply the template:

```bash
python3 tools/apply.py /path/to/new-project --mode new
```

2. Run:

```text
$cl-strategy
```

3. Then:

```text
$cl-ideate
```

4. Select one idea and move through:

```text
$cl-brainstorm
$cl-review
$cl-design
$cl-review
$cl-plan
$cl-review
$cl-work
$cl-verify
$cl-compound
```

## When to use each skill

| Skill | Use when | Do not use when |
|---|---|---|
| cl-onboard | Adopting Compound Lite in a repo | You just need a small code edit |
| cl-strategy | Setting or revising product/Agent direction | Writing implementation details |
| cl-ideate | Deciding what to build or criticizing ideas | A task is already decided |
| cl-brainstorm | User-facing behavior is unclear | The task is a tiny fix |
| cl-design | User-facing UI/UX needs flows, states, or visual constraints | There is no user-facing experience change |
| cl-review | A planning artifact needs consistency review before the next planning stage | Implementation has already happened; use cl-verify instead |
| cl-plan | A task needs multiple steps or risk analysis | You want to directly debug a failure |
| cl-work | You have a plan and want local implementation | You want commit/push/PR automation |
| cl-verify | Work is implemented and needs independent review | You have not implemented anything yet |
| cl-debug | A bug or failure needs root-cause analysis | The task is pure ideation |
| cl-compound | A durable learning should be saved | The change was trivial |
| cl-product-pulse | Future read-only product reporting | V1 production-data integration |
| cl-render | You want a read-only HTML view of a finalized Markdown artifact | You need to edit or decide before finalizing Markdown |

## HTML decision editor mode

Use `~html` when you want to make a human judgment before committing to a Markdown artifact.

Examples:

```text
$cl-ideate ~html "Improve Agent onboarding"
$cl-brainstorm ~html docs/ideation/2026-05-09-agent-onboarding.md
$cl-plan ~html docs/brainstorms/2026-05-09-agent-onboarding-requirements.md
$cl-verify ~html docs/plans/2026-05-09-agent-onboarding-plan.md
```

The skill generates a temporary HTML editor under `docs/.compound-lite/drafts/`.
Open it in a browser, edit or select options, then click Export Markdown.

The exported Markdown is the final artifact. Move or save it to the expected
`docs/` directory before using it with the next Compound Lite stage.

No `cl-finalize` step exists. No `~html-only` mode exists. No `~import` mode exists.

`cl-design ~html` is not part of V1.1. Use the normal Markdown design artifact
flow for now.

## Read-only HTML views

Use `cl-render` after a Markdown artifact is finalized:

```text
$cl-render docs/plans/2026-05-09-agent-onboarding-plan.md
```

It writes a read-only HTML view under `docs/.compound-lite/views/`. The source
Markdown remains the artifact of record.

## Minimal prompt examples

```text
Use $cl-onboard to adopt this workflow in the current repo. Read-only scan first.
```

```text
Use $cl-ideate to critique possible improvements to the onboarding Agent. Write the artifact under docs/ideation/.
```

```text
Use $cl-review to check the latest ideation artifact for scope drift and missing confirmations before requirements.
```

```text
Use $cl-design after the confirmed requirements. Keep the UX artifact under docs/designs/ and stop for review.
```

```text
Use $cl-plan with docs/brainstorms/2026-05-03-agent-onboarding-requirements.md. Include Agent-native and eval considerations.
```

```text
Use $cl-work to implement the latest plan locally. Do not commit, push, or open a PR.
```

```text
Use $cl-verify as an independent verifier. Start from STRATEGY.md, the requirements doc, the plan, and the current diff. Do not rely on the builder's explanation.
```

```text
Use $cl-compound to record the durable lesson from this fix under docs/solutions/.
```
