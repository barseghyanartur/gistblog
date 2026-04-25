---
name: coding-standards
description: Style, typing, and naming conventions for gistblog
---

# Coding Standards

## Style Rules

- Use Ruff for linting and formatting (configured in pyproject.toml)
- Follow PEP 8 with Ruff defaults
- Maximum line length: 88 (Ruff default)

## Typing Rules

- Use type hints where beneficial
- Use `mypy` for type checking (configured in pyproject.toml)
- When present, type hints must be valid

## Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

## Logging Conventions

- Use `logging` module, not print statements
- Use appropriate log levels: DEBUG, INFO, WARNING, ERROR

## Error-Handling Philosophy

- Raise specific exceptions, not generic ones
- Catch specific exceptions when handling
- Never silently swallow exceptions

## Enforcement

- Ruff enforces style and many best practices
- MyPy enforces type correctness
- Pre-commit hooks should enforce before commit
