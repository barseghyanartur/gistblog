---
name: dev-setup
description: Environment setup and dependency installation for gistblog
---

# Dev Setup

## Environment Setup

### Virtual Environment

The project uses `uv` for dependency management.

```bash
uv venv
source .venv/bin/activate
```

### Dependency Installation

```bash
uv sync --all-extras
uv pip install -e .
```

### Alternative (Make)

```bash
make install
```

### Verify Installation

```bash
make build
```

## Common Issues

- If Gist fetching fails: Check `.env` contains valid GitHub credentials
- If Pelican fails to build: Ensure `content/` has valid RST files
- If Sphinx docs fail: Run `make build-docs` to diagnose

## Recovery

To reset environment:

```bash
rm -rf .venv
make install
```
