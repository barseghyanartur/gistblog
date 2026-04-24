==================================
gistblog – Serverless headless CMS
==================================

**Zero Git friction.** Write in reStructuredText → Public Gist → auto-deployed Pelican blog with full-text search.

.. image:: https://img.shields.io/pypi/v/gistblog.svg
   :target: https://pypi.python.org/pypi/gistblog
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/gistblog.svg
   :target: https://pypi.python.org/pypi/gistblog/
   :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/gistblog/actions/workflows/test.yml/badge.svg?branch=main
   :target: https://github.com/barseghyanartur/gistblog/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/gistblog/badge/?version=latest
    :target: http://gistblog.readthedocs.io
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/docs-llms.txt-blue
    :target: https://gistblog.readthedocs.io/en/latest/llms.txt
    :alt: llms.txt - documentation for LLMs

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/gistblog/#License
   :alt: MIT

.. image:: https://coveralls.io/repos/github/barseghyanartur/gistblog/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/barseghyanartur/gistblog?branch=main
    :alt: Coverage

How to publish a post
=====================
1. Create a **public** Gist on GitHub.
2. Description must start with: `blog: Your Post Title`
3. File must be valid reST with field-list metadata (see example in the original prompt).
4. Save. The site updates automatically every 4 hours (or manually trigger the GitHub Action).

.. code-block:: rst

    ================
    The Post Title
    ================
    :date: 2026-04-02 14:00
    :category: Tech
    :tags: python, automation
    :summary: This text appears **only** in the post listings (homepage, archives, etc.).
    :image: https://picsum.photos/id/1015/800/450

    Post body starts here...


Search page lives at `/pages/search/`.

**Important:** Change `USERNAME = "barseghyanartur"` in `src/gistblog/fetch_data.py` to **your own GitHub username** before the first run.

Local development
==================
All Python commands are run using `uv run` or Makefile shortcuts.

1. Clone the repo
-----------------

::

    git clone https://github.com/YOURUSERNAME/YOUR-REPO.git
    cd YOUR-REPO

2. Install dependencies
-----------------------

::

    make install

3. Pull your latest Gists
-------------------------

::

    make fetch

4. One-time build + static preview
----------------------------------
::

    make serve

# → http://localhost:8000

5. LIVE development mode (recommended)
--------------------------------------
::

    make dev

# → Auto-rebuilds on any change + live server at http://localhost:8000
