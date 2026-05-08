# Risk lenses

Load the relevant lens based on the change surface.

## UI lens

Use when changing pages, components, forms, navigation, or interaction states.

Check loading, empty, error, disabled, accessibility, keyboard, mobile/responsive behavior, and visual regression risk.

## API / integration lens

Use when changing endpoints, webhooks, SDKs, serializers, external APIs, or shared contracts.

Check compatibility, error handling, retries, idempotency, timeouts, logging, and versioning.

## Data lens

Use when changing migrations, persistence, cache, import/export, or schema.

Check existing data, null/empty states, rollback, integrity, concurrency, idempotency, and expensive queries.

## Security / privacy lens

Use when touching auth, permissions, tokens, user input, public endpoints, payments, PII, or secrets.

Check authorization, validation, privilege escalation, unsafe logging, and data leakage.

## Reliability lens

Use when touching background jobs, queues, retries, async flows, external services, cron, or deployment-sensitive code.

Check timeouts, duplicate execution, partial failure, recovery, observability, and safe retries.

## Performance lens

Use when changing loops, data transforms, database queries, cache behavior, rendering, or heavy LLM calls.

Check big-O, query counts, batching, cache invalidation, latency, and cost.
