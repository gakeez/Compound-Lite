# Verification resolver

Choose verification commands by evidence, not assumptions.

Priority order:

1. Commands explicitly listed in AGENTS.md.
2. Commands in README, docs, or CI configuration.
3. Commands implied by manifest and lockfiles.
4. Targeted tests colocated with changed files.
5. If no command can be determined, explain what could not be verified and suggest likely commands.

Prefer targeted verification first, then broader checks when the change is high-risk.

Do not invent a command and present it as authoritative. Label fallback guesses as guesses.
