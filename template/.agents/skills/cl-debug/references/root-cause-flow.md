# Root cause flow

## Reproduce

Confirm the symptom exists in the current environment or explain why it cannot be reproduced.

## Trace

Follow the execution path backward from symptom to trigger. Ask where invalid state first appears.

## Hypothesize

For each hypothesis, state:

- What is wrong.
- Where it happens.
- How it leads to the symptom.
- What prediction should also be true if the hypothesis is right.

## Gate

Do not fix until the causal chain has no important gaps, unless the user explicitly accepts a best-effort fix.

## Fix

Make the smallest change that addresses the root cause. Add a regression test when practical.
