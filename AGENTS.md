# AGENTS.md — gistblog

## Project overview

A static site generator powered by GitHub Gists. Pulls content from GitHub Gists and generates a static blog using Pelican.

## Architecture invariants

- Python project using Pelican as the static site generator
- Requires Python ≥3.10
- Uses `uv` for dependency management
- GitHub Gists are the source of truth for blog content

## Repository layout (authoritative)

```text
gistblog/
├── .venv/              # Virtual environment (generated)
├── .ruff_cache/        # Ruff linter cache (generated)
├── builddocs/          # Built documentation (generated)
├── content/            # Blog content (RST format)
├── dist/               # Package distributions (generated)
├── docs/               # Source documentation
├── output/             # Built static site (generated)
├── src/gistblog/       # Source code
├── pyproject.toml      # Project configuration
├── requirements.txt    # Runtime dependencies
├── Makefile            # Build commands
├── pelicanconf.py      # Pelican configuration
└── .env                # Environment variables
```

- Generated directories: `.venv/`, `.ruff_cache/`, `builddocs/`, `dist/`, `output/`
- These directories MUST NOT be committed

## Hard constraints

- MUST NOT modify `.env` file
- Generated directories MUST NOT be committed
- DO NOT commit secrets or credentials

## Known intentional behaviors — do not change

- Gist fetching is driven by environment variables (stored in `.env`)
- Documentation build uses Sphinx
- Package release uses `twine` and `build`
- Test runner: `pytest` with `pytest-codeblock` for documentation testing

## Configuration authority

- Project dependencies: `pyproject.toml`
- Pelican settings: `pelicanconf.py`
- Environment variables: `.env` (must not modify)
- Make targets: `Makefile`

## Agent obligations

- Run linting before committing (`ruff` is configured)
- Run tests before committing (`uv run pytest src/gistblog/tests/`)
- Verify documentation builds successfully

## How to run Python commands

All Python commands MUST be run using `uv run` or Makefile shortcuts:

```bash
# Using Makefile (preferred)
make fetch       # Fetch Gists and generate search index
make build       # Fetch + build static site
make dev         # Development mode with live reload

# Using uv directly
uv run pytest src/gistblog/tests/
uv run pelican content -s pelicanconf.py
uv run gistblog-fetch-data
```

Never use `python` or `python3` directly - always use `uv run`.