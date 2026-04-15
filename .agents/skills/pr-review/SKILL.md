---
name: pr-review
description: Pull request review checklist for gistblog
---

## Review Checklist

1. **Lint check**: Verify `ruff` passes with no warnings
2. **Test check**: Verify `pytest` passes with no failures
3. **Docs check**: Verify `make build-docs` succeeds
4. **No secrets**: Ensure no credentials or secrets in changes
5. **No generated artifacts**: Ensure no committed `.venv`, `builddocs`, `dist`, `output`, `.ruff_cache`
6. **AGENTS.md alignment**: Ensure changes don't violate AGENTS.md constraints
7. **Type hints valid**: If changed, ensure mypy passes

## Must Check Items

- All modified files have proper type hints where applicable
- No hardcoded credentials or secrets
- No accidental commits of generated directories

## Reporting

If any checklist item fails, report:
- Which item failed
- Specific violation or error
- Suggested fix