---
name: cl-compound
description: Capture durable solved-problem learning in docs/solutions. Use after a verified non-trivial fix, Agent behavior lesson, project convention discovery, framework gotcha, or debugging path worth preserving. Do not document trivial edits.
---

# cl-compound

Write durable knowledge only when it will reduce future work.

## Learning gate

Write a solution doc when one or more are true:

- The root cause was non-obvious.
- The same mistake could happen again.
- A project-specific convention was discovered.
- An Agent behavior, eval, memory, tool, or permission lesson emerged.
- A framework, dependency, deployment, data, or testing gotcha was learned.
- The user corrected an assumption future agents may repeat.

Do not write a solution doc for:

- Typos.
- Obvious one-line fixes.
- Routine edits with no reusable lesson.

## Flow

1. Read the relevant plan, verification output, diff summary, and any user correction.
2. Classify the solution category.
3. Check existing `docs/solutions/` for obvious duplicates.
4. Write or update one solution doc.
5. Do not include secrets, PII, private user content, or unnecessary logs.
6. End with the path written and a one-sentence summary of how it helps future work.

## Output path

Use:

```text
docs/solutions/<category>/YYYY-MM-DD-short-title.md
```

Suggested categories:

```text
bugs
architecture
agent-behavior
workflow
testing
data
security
integrations
```

Read `references/solution-template.md` and `references/artifact-policy.md` before writing.
