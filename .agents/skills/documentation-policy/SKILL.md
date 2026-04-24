---
name: documentation-policy
description: Authoritative documentation files for gistblog
---

## In-Scope Documentation

The following files are authoritative and must stay aligned with code:

- `README.rst` — Project readme
- `AGENTS.md` — Agent governance
- `docs/*.rst` — Sphinx documentation source

## Exclusions

The following are generated and derived (not authoritative):

- `builddocs/` — Built Sphinx HTML output
- `output/` — Generated static site
- `dist/` — Package distributions

## Documentation Alignment

Documentation alignment is enforced via the `update-documentation` skill.

The `documentation-policy` skill defines the contract:
- Which files are authoritative
- Which files are excluded
- When alignment must be verified