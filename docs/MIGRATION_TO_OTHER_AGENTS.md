# Migrating Compound Lite to Other Coding Agents

Compound Lite is designed around portable Markdown artifacts and Agent Skills-style folders. The core workflow can move between Codex, Claude Code, Cursor, and other coding agents if you keep the artifacts and skill instructions platform-neutral.

## What is portable

These files are plain Markdown and should work with any coding agent that can read a repository:

```text
AGENTS.md
STRATEGY.md
docs/ideation/
docs/brainstorms/
docs/plans/
docs/solutions/
docs/pulse-reports/
docs/evals/
```

The skill instructions are also mostly portable because each skill is a folder with `SKILL.md` and optional `references/` files.

## Codex layout

Codex repo-scoped skills live here:

```text
.agents/skills/<skill-name>/SKILL.md
```

Codex project-scoped custom agents live here:

```text
.codex/agents/<agent-name>.toml
```

Use this package as-is for Codex.

## Claude Code migration

Claude Code project skills usually use:

```text
.claude/skills/<skill-name>/SKILL.md
```

Claude Code project subagents usually use:

```text
.claude/agents/<agent-name>.md
```

Manual migration steps:

1. Copy `.agents/skills/*` into `.claude/skills/`.
2. Convert optional `.codex/agents/*.toml` into Claude Code agent Markdown files under `.claude/agents/`.
3. Keep `AGENTS.md`, `STRATEGY.md`, and `docs/` unchanged.
4. Update skill references only if a Claude-specific tool name is needed.
5. Keep Level 1 automation boundaries unchanged.

Recommended Claude Code role split:

```text
cl-builder   -> may edit local files and tests
cl-verifier  -> read-only review/test agent when possible
cl-curator   -> writes solution docs only after work is verified
```

## Cursor migration

Cursor can use project rules and Agent Skills. A typical migration shape is:

```text
.cursor/rules/compound-lite.mdc      # short always-on rules only
.cursor/skills/<skill-name>/SKILL.md # workflow skills
AGENTS.md                            # keep for portable project guidance
docs/                                # keep unchanged
STRATEGY.md                          # keep unchanged
```

Manual migration steps:

1. Copy the lightweight working agreements from `AGENTS.md` into `.cursor/rules/compound-lite.mdc` only if you want Cursor-specific always-on rules.
2. Copy `.agents/skills/*` into Cursor's supported skills folder for your setup.
3. Keep full workflow content in skills, not in always-on rules.
4. Use separate Cursor agent/session invocations for builder and verifier if supported by your setup.

## General migration principles

1. Keep artifacts as Markdown.
2. Keep skills focused: one skill, one job.
3. Keep platform-specific tool names out of core instructions unless necessary.
4. Put only short, durable rules in always-on instruction files.
5. Put long workflows in skills.
6. Keep builder and verifier roles separate when possible.
7. Do not migrate external automation until the target platform's permission model is clear.

## What not to migrate automatically

Do not automatically migrate:

- MCP server configs.
- GitHub/Slack/Linear integrations.
- Hooks.
- Approval policies.
- Production database credentials.
- Analytics/tracing/payment integrations.

Those should be recreated manually per platform after reviewing security and permission behavior.
