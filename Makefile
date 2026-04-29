VERSION := 0.1.1
SHELL := /bin/bash
# Makefile for project
VENV := .venv/bin/activate
UNAME_S := $(shell uname -s)

# Makefile for Gist2Pelican – Serverless Headless CMS
# Run "make help" to see all commands

.PHONY: help install fetch build clean serve dev

PYTHON := python3
PELICAN := pelican
PIP := pip3
CONFFILE := pelicanconf.py

help:
	@echo "Gist2Pelican Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  make install   → Install all Python dependencies"
	@echo "  make fetch     → Pull latest blog Gists + regenerate search index"
	@echo "  make build     → Build static site (output/)"
	@echo "  make serve     → Serve statically on http://localhost:8000"
	@echo "  make dev       → LIVE RELOAD + auto-serve (best for local editing)"
	@echo "  make clean     → Remove generated output/"
	@echo ""
	@echo "After 'make dev' open → http://localhost:8000"

fetch:
	@echo "Fetching Gists and generating search index..."
	uv run gistblog-fetch-data
	uv run gistblog-build-search-index

build:
	@echo "Building site with Pelican..."
	uv run env SITEURL='' $(PELICAN) -s $(CONFFILE)

clean-output:
	rm -rf output/
	@echo "✅ Cleaned. content/ (including static pages) was preserved."

serve:
	@echo "🚀 Serving built site at http://localhost:8000"
	@echo "Press Ctrl+C to stop"
	uv run env SITEURL='' python -m http.server 8000 --directory output

pipeline: fetch build serve

run: build serve

dev: fetch build
	@echo "🚀 Starting DEV mode with live reload"
	@echo "→ Changes to any .rst file in content/ will auto-rebuild"
	@echo "→ Server running at http://localhost:8000"
	@echo ""
	@echo "Tip: In another terminal run 'make fetch' to pull new Gists while dev server is running."
	uv run env SITEURL='' $(PELICAN) -s $(CONFFILE) --autoreload --listen

# ----------------------------------------------------------------------------
# Installation
# ----------------------------------------------------------------------------

create-venv:
	uv venv

# Install the project
install: create-venv
	source $(VENV) && uv sync --all-extras
	source $(VENV) && uv pip install -e .

# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------

# Build documentation using Sphinx and zip it
build-docs:
	source $(VENV) && sphinx-source-tree
	source $(VENV) && sphinx-build -n -b text docs builddocs
	source $(VENV) && sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

rebuild-docs:
	source $(VENV) && sphinx-apidoc . --full -o docs -H 'gistblog' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/conf.py.distrib docs/conf.py
	cp docs/index.rst.distrib docs/index.rst

build-docs-epub:
	$(MAKE) -C docs/ epub

build-docs-pdf:
	$(MAKE) -C docs/ latexpdf

auto-build-docs:
	source $(VENV) && sphinx-autobuild docs docs/_build/html

# Serve the built docs on port 5001
serve-docs:
	source $(VENV) && cd builddocs && python -m http.server 5001

compile-requirements:
	source $(VENV) && uv pip compile --all-extras -o docs/requirements.txt pyproject.toml

compile-requirements-upgrade:
	source $(VENV) && uv pip compile --all-extras -o docs/requirements.txt pyproject.toml --upgrade

# ----------------------------------------------------------------------------
# Release
# ----------------------------------------------------------------------------

package-build:
	source $(VENV) && python -m build .

check-package-build:
	source $(VENV) && twine check dist/*

release:
	source $(VENV) && twine upload dist/* --verbose

test-release:
	source $(VENV) && twine upload --repository testpypi dist/* --verbose

# ----------------------------------------------------------------------------
# Pre-commit
# ----------------------------------------------------------------------------

pre-commit-install:
	pre-commit install

pre-commit: pre-commit-install
	pre-commit run --all-files

# ----------------------------------------------------------------------------
# Security
# ----------------------------------------------------------------------------

create-secrets:
	source $(VENV) && detect-secrets scan > .secrets.baseline

detect-secrets:
	source $(VENV) && detect-secrets scan --baseline .secrets.baseline

# ----------------------------------------------------------------------------
# Housekeeping
# ----------------------------------------------------------------------------
clean-dev:
	find . -name "*.orig" -exec rm -rf {} +
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf dist/ src/safezip.egg-info/ .cache/ .mypy_cache/ .ruff_cache/

clean-test:
	find . -name "*.pyc" -exec rm -rf {} +
	rm -rf .coverage .pytest_cache/ htmlcov/

clean: clean-dev clean-test clean-output

update-version:
	@echo "Updating version in pyproject.toml and __init__.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/^version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/gistblog/__init__.py; \
	else \
		sed -i 's/^version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/gistblog/__init__.py; \
	fi
