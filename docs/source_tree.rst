Project source-tree
===================

Below is the layout of the project (to 10 levels), followed by
the contents of each key file.

.. code-block:: text
   :caption: Project directory layout

   gist-blog/
   ├── docs
   │   └── source_tree.rst
   ├── static
   │   └── search_index.json
   ├── themes
   │   └── custom
   │       ├── static
   │       │   ├── css
   │       │   │   ├── fonts.css
   │       │   │   ├── main.css
   │       │   │   ├── pygment.css
   │       │   │   ├── reset.css
   │       │   │   ├── typogrify.css
   │       │   │   └── wide.css
   │       │   └── fonts
   │       │       ├── font.css
   │       │       ├── Yanone_Kaffeesatz_400.eot
   │       │       ├── Yanone_Kaffeesatz_400.svg
   │       │       ├── Yanone_Kaffeesatz_400.ttf
   │       │       ├── Yanone_Kaffeesatz_400.woff
   │       │       ├── Yanone_Kaffeesatz_400.woff2
   │       │       └── Yanone_Kaffeesatz_LICENSE.txt
   │       ├── templates
   │       │   ├── analytics.html
   │       │   ├── archives.html
   │       │   ├── article.html
   │       │   ├── article_infos.html
   │       │   ├── author.html
   │       │   ├── authors.html
   │       │   ├── base.html
   │       │   ├── categories.html
   │       │   ├── category.html
   │       │   ├── comments.html
   │       │   ├── disqus_script.html
   │       │   ├── github.html
   │       │   ├── index.html
   │       │   ├── minimal_infos.html
   │       │   ├── page.html
   │       │   ├── period_archives.html
   │       │   ├── tag.html
   │       │   ├── taglist.html
   │       │   ├── tags.html
   │       │   ├── translations.html
   │       │   └── twitter.html
   │       └── __init__.py
   ├── AGENTS.md
   ├── fetch_gists.py
   ├── generate_search_index.py
   ├── LICENSE
   ├── Makefile
   ├── pelicanconf.py
   ├── pyproject.toml
   ├── README.rst
   └── requirements.txt

README.rst
----------

.. literalinclude:: ../README.rst
   :language: rst
   :caption: README.rst

AGENTS.md
---------

.. literalinclude:: ../AGENTS.md
   :language: markdown
   :caption: AGENTS.md

docs/source_tree.rst
--------------------

.. literalinclude:: source_tree.rst
   :language: rst
   :caption: docs/source_tree.rst

fetch_gists.py
--------------

.. literalinclude:: ../fetch_gists.py
   :language: python
   :caption: fetch_gists.py

generate_search_index.py
------------------------

.. literalinclude:: ../generate_search_index.py
   :language: python
   :caption: generate_search_index.py

pelicanconf.py
--------------

.. literalinclude:: ../pelicanconf.py
   :language: python
   :caption: pelicanconf.py

pyproject.toml
--------------

.. literalinclude:: ../pyproject.toml
   :language: toml
   :caption: pyproject.toml

static/search_index.json
------------------------

.. literalinclude:: ../static/search_index.json
   :language: json
   :caption: static/search_index.json

themes/custom/__init__.py
-------------------------

.. literalinclude:: ../themes/custom/__init__.py
   :language: python
   :caption: themes/custom/__init__.py
