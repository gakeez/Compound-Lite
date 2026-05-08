# Compound Lite for Codex

[中文](README.zh-CN.md) | English

Compound Lite is a lightweight, repo-scoped workflow system inspired by compound engineering. It is designed for solo developers and Agent-product projects that need durable planning, independent verification, and reusable learnings without adopting a large multi-agent automation stack.

It is intentionally **Level 1 semi-automatic**:

- It may read project files, write local code, write local tests, run local verification, and create local Markdown artifacts.
- It must not automatically commit, push, open PRs, deploy, mutate production data, or change external systems.
- It separates planning, building, verification, and learning through artifacts instead of relying on one continuous chat memory.

## What this package contains

```text
template/
  AGENTS.md
  STRATEGY.md
  .agents/skills/          # Codex repo-scoped skills
  .codex/agents/           # Optional Codex custom agents for role separation
  docs/                    # Artifact folders and README files

tools/
  apply.py                 # Safely copy the template into a target repo
  validate_structure.py    # Check that a repo has the expected Compound Lite structure

docs/
  BUILD_PLAN.md            # Full construction plan
  MIGRATION_TO_OTHER_AGENTS.md
  USAGE.md
```

## Install into an existing project

From this package root:

```bash
python3 tools/apply.py /path/to/your-project --mode existing
```

The installer is conservative. It does not overwrite existing files by default. Conflicting files are written under `.compound-lite-incoming/` so you can merge them manually.

## Install into a new project folder

```bash
python3 tools/apply.py /path/to/new-project --mode new
```

Then open that folder in Codex and run:

```text
$cl-onboard
```

## Core workflow

```text
$cl-strategy     -> STRATEGY.md
$cl-ideate       -> docs/ideation/
$cl-review       -> planning consistency gate
$cl-brainstorm   -> docs/brainstorms/
$cl-review       -> planning consistency gate
$cl-design       -> docs/designs/
$cl-review       -> planning consistency gate
$cl-plan         -> docs/plans/
$cl-review       -> planning consistency gate
$cl-work         -> local code + tests
$cl-verify       -> independent verification
$cl-compound     -> docs/solutions/
```

`$cl-review` is only for planning stages. Execution stays `$cl-work -> $cl-verify`.

`$cl-product-pulse` is included as a future-facing placeholder. It only describes the intended read-only pulse workflow and does not connect to analytics, tracing, payments, or databases in V1.

## Recommended first run in an existing project

```text
Use $cl-onboard to adopt Compound Lite in this repo. Start with a read-only scan, then draft AGENTS.md and STRATEGY.md. Do not change application code.
```

## Recommended first run in a new project

```text
Use $cl-strategy to create STRATEGY.md, then use $cl-ideate to explore initial product/Agent directions.
```
