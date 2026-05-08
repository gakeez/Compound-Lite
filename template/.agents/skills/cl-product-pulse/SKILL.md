---
name: cl-product-pulse
description: Future read-only product pulse workflow. In V1, use only to explain setup requirements and draft a manual pulse report template. Do not connect to analytics, tracing, payment, or database systems.
---

# cl-product-pulse

This is a V1 placeholder for future product pulse reporting.

## V1 behavior

Allowed:

- Explain what data sources would be needed.
- Draft a manual pulse report template.
- Save a manually provided report under `docs/pulse-reports/`.

Not allowed:

- Connect to analytics, tracing, payment, or database systems.
- Read production user data.
- Mutate external systems.
- Store PII.

## Future V2 behavior

Generate a compact, read-only report covering:

1. Usage.
2. Performance.
3. Errors.
4. Followups.

Reports should be saved to `docs/pulse-reports/`.
