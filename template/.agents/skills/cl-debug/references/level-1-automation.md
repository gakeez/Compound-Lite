# Level 1 automation boundaries

Allowed:

- Read local files.
- Search local code.
- Write local artifacts.
- Modify local source files and tests.
- Run local verification commands.

Ask before:

- Adding new production dependencies.
- Deleting or moving many files.
- Running database migrations.
- Changing auth, permissions, payments, or security-sensitive behavior.
- Expanding Agent tool permissions.
- Changing external API contracts.
- Connecting MCP or external data sources.

Do not automatically:

- Commit.
- Push.
- Open PRs.
- Deploy.
- Modify production data.
- Mutate external systems.
