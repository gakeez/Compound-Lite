# Compound Lite for Codex — Overall Build Plan

## 1. Purpose

Compound Lite for Codex is a lightweight, portable, semi-automatic workflow system for building software and Agent products with durable artifacts. It keeps the parts of compound engineering that create leverage:

1. Strategy before scattered features.
2. Critical ideation before planning.
3. Requirements before implementation planning.
4. UX/UI design before implementation planning when user-facing experience changes.
5. Review gates between planning stages.
6. Implementation plans before non-trivial code changes.
7. Independent verification after building.
8. Solution capture after non-trivial learning.

It deliberately avoids the heavy parts of a full automation platform:

- No automatic multi-agent swarm.
- No automatic commit, push, PR, or deploy.
- No external system mutation.
- No product analytics integration in V1.
- No technology-stack-specific hardcoding.

## 2. Confirmed design decisions

### Must keep

- `cl-strategy`, corresponding to strategy capture and maintenance.
- `cl-plan`, corresponding to implementation planning.
- `cl-compound`, corresponding to durable solution capture.
- `cl-ideate`, because ideas need criticism before commitment.
- `cl-brainstorm`, because requirements should not be silently invented during planning.
- `cl-design`, because user-facing experience should be designed before implementation planning.
- `cl-review`, because planning artifacts need a dedicated consistency gate before the next stage.
- `cl-onboard`, because existing projects must be able to adopt the workflow midstream.
- `cl-verify`, because verification should be separated from the builder role.

### Add later

- `cl-product-pulse`, once the product has real usage, performance, error, payment, or read-only database data sources.

### Automation level

Level 1 semi-automation only.

Allowed:

- Read files.
- Search code.
- Write local artifacts.
- Modify local source files.
- Add or update tests.
- Run local tests, lint, type checks, and builds.

Not allowed by default:

- Commit.
- Push.
- Open PRs.
- Deploy.
- Change external systems.
- Mutate production data.
- Connect to analytics, tracing, payment, or database systems without explicit user setup.

### Adapter strategy

Use discovery-first, thin adapters:

1. Read `AGENTS.md`.
2. Read `STRATEGY.md` when product direction matters.
3. Read README and local docs.
4. Inspect CI configuration.
5. Inspect manifest, lockfile, and config files.
6. Find similar source files and tests.
7. Only then infer fallback commands from technology stack.

Do not make stack-specific assumptions before project-specific evidence.

## 3. Artifact system

Compound Lite uses ordinary Markdown artifacts so the workflow can migrate across Codex, Claude Code, Cursor, and other coding agents.

```text
AGENTS.md                         # Persistent repo rules for coding agents
STRATEGY.md                       # Product/Agent strategy anchor

docs/ideation/                    # Criticized and ranked ideas
docs/brainstorms/                 # Requirements documents
docs/designs/                     # UX/UI design artifacts
docs/plans/                       # Implementation plans
docs/solutions/                   # Durable solved-problem learnings
docs/pulse-reports/               # Future product pulse reports
docs/evals/                       # Agent behavior eval cases and criteria
docs/.compound-lite/drafts/       # Temporary HTML decision editors
docs/.compound-lite/views/        # Read-only HTML views of Markdown artifacts
```

Markdown remains the durable source of truth. Generated HTML files under
`docs/.compound-lite/` are human-facing aids and should not be used as default
Agent context.

## 4. Skill inventory

### cl-onboard

Adopts Compound Lite in an existing or new project. It performs a read-only scan first, creates or proposes `AGENTS.md`, drafts `STRATEGY.md`, creates artifact directories, and optionally creates a current active-work plan. It must not change application code.

### cl-strategy

Creates or updates `STRATEGY.md`. It captures target problem, approach, primary users, key metrics, tracks, non-goals, and Agent-native assumptions.

### cl-ideate

Generates, criticizes, rejects, and ranks ideas. It writes to `docs/ideation/` and stops before requirements or implementation planning.

### cl-brainstorm

Turns a chosen idea into a requirements document under `docs/brainstorms/`. It defines user-facing behavior, scope, non-goals, success criteria, flows, edge cases, and Agent-specific behavior.

### cl-design

Turns confirmed requirements into a UX/UI design artifact under `docs/designs/`. It defines user journeys, screen states, interaction rules, copy rules, accessibility/responsive notes, and visual direction before implementation planning.

### cl-review

Reviews planning artifacts before the workflow advances. It checks consistency across `STRATEGY.md`, confirmed user decisions, and the latest planning artifacts. It is read-only by default, reports in chat unless explicitly asked to write a document, and does not replace `cl-verify`.

### cl-plan

Turns a requirements document or clear task into an implementation plan under `docs/plans/`. It performs project discovery, selects risk lenses, determines verification, and includes Agent-native/eval considerations when relevant.

### cl-work

Executes a plan locally. It may edit code and tests, but it must not commit, push, open PRs, deploy, or mutate external systems.

### cl-verify

Reviews the result independently. It should read the plan, requirements, strategy, and diff; run appropriate verification; and produce findings. It can be run in a separate Codex custom agent or a fresh agent session.

### cl-debug

Diagnoses bugs systematically: reproduce, trace causal chain, form hypotheses, verify root cause, write or update regression tests, then apply minimal fix.

### cl-compound

Captures durable learning under `docs/solutions/` only when the lesson will prevent future work or repeated mistakes.

### cl-product-pulse

V1 placeholder. Future read-only reporting workflow for usage, performance, errors, and followups saved to `docs/pulse-reports/`.

### cl-render

Renders a finalized Markdown artifact into a read-only HTML view under
`docs/.compound-lite/views/`. It does not edit the Markdown artifact and does
not create pre-decision editors.

## 5. Role separation

Do not default to automatic many-agent parallelism. Instead, separate roles by phase and artifact:

```text
strategy -> ideation -> review -> requirements -> review -> design -> review -> plan -> review -> builder -> verifier -> curator
```

The builder should not be the only reviewer of its own work. The verifier should start from artifacts and diff, not from the builder's self-explanation.

## 6. Suggested adoption modes

### New project

1. Apply template.
2. Run `cl-strategy`.
3. Run `cl-ideate`.
4. Run `cl-review`.
5. Run `cl-brainstorm` for the selected idea.
6. Run `cl-review`.
7. Run `cl-design` for user-facing UI/UX changes.
8. Run `cl-review`.
9. Run `cl-plan`.
10. Run `cl-review`.
11. Run `cl-work`.
12. Run `cl-verify`.
13. Run `cl-compound` if durable learning exists.

### Existing project

1. Apply template.
2. Run `cl-onboard`.
3. Merge generated `AGENTS.md` or `STRATEGY.md` drafts if conflicts exist.
4. Write one active plan for current work if needed.
5. Start using the full workflow for the next non-trivial task.

## 7. V1.1 HTML decision editor mode

- Add optional `~html` support to planning-oriented skills: `cl-strategy`, `cl-ideate`, `cl-brainstorm`, `cl-plan`, and `cl-verify`.
- Keep `cl-work` execution-only; it does not support `~html`.
- Generate temporary HTML editors under `docs/.compound-lite/drafts/`.
- Export Markdown directly from the HTML editor; exported Markdown is the formal artifact.
- Add `tools/render_compound_html.py` with stdlib-only `decision` and `view` commands.
- Add `cl-render` for finalized Markdown to read-only HTML views.
- Keep `cl-design ~html` as a future extension, not part of V1.1.

## 8. V2 roadmap

- Implement `cl-product-pulse` data-source setup and report generation.
- Add optional thin adapters when repeated mistakes appear in a real stack.
- Add optional plugin packaging after repo-scoped skills prove useful.
- Add optional explicit verifier subagent setup guides for Claude Code and Cursor.
