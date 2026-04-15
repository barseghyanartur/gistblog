---
name: dev-workflow
description: Definition of Done and commit workflow for gistblog
---

## Definition of Done

A task is complete when:
1. Code changes work as intended
2. All linting passes
3. All tests pass
4. Documentation builds successfully
5. No regressions in static site generation

## Mandatory Workflow

Before committing:

1. **Lint**: Run `make pre-commit`
2. **Fix**: Address all linting violations
3. **Test**: Run `uv run pytest`
4. **Verify docs**: Run `make build-docs`

## Retry Logic

- If lint fails: Fix errors, re-run lint (max 3 attempts)
- If tests fail: Fix failures, re-run tests (max 3 attempts)
- If docs fail: Fix documentation issues, re-run build (max 3 attempts)

## Stop Conditions

- After 3 failed attempts in any step, stop and report the issue
- Do not commit if any step fails

## Forbidden Actions

- Do not skip linting
- Do not skip tests
- Do not skip documentation build verification
- Do not force commit despite failures