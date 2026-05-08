# Agent-native lens

Load this lens whenever a task changes Agent behavior, instructions, tools, memory, context retrieval, planning/execution, human approval, evals, or observability.

Ask:

1. Context: What information does the Agent see? Is anything missing, excessive, stale, or unsafe?
2. Tools: What tools/actions can the Agent call? Are permissions scoped? Which actions require confirmation?
3. Memory: What is stored across turns or sessions? What must not be stored?
4. Control: When should the Agent ask the user instead of acting?
5. Recovery: How are failures surfaced, retried, or rolled back?
6. Evaluation: What examples prove behavior improved? What regressions must be caught?
7. Safety: Could prompt injection, data leakage, or tool misuse occur?

For substantial Agent behavior changes, update or create docs/evals/ cases.
