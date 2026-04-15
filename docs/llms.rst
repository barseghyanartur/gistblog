Project source-tree
===================

Below is the layout of the project (to 10 levels), followed by
the contents of each key file.

.. code-block:: text
   :caption: Project directory layout

   gist-blog/
   ├── docs
   │   ├── conf.py
   │   ├── documentation.rst
   │   ├── index.rst
   │   ├── llms.rst
   │   ├── make.bat
   │   ├── Makefile
   │   ├── pelicanconf.rst
   │   └── requirements.txt
   ├── src
   │   └── gistblog
   │       ├── __init__.py
   │       ├── build_search_index.py
   │       └── fetch_data.py
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
   │       │   ├── search.html
   │       │   ├── tag.html
   │       │   ├── taglist.html
   │       │   ├── tags.html
   │       │   ├── translations.html
   │       │   └── twitter.html
   │       └── __init__.py
   ├── AGENTS.md
   ├── LICENSE
   ├── Makefile
   ├── pelicanconf.py
   ├── pyproject.toml
   ├── README.rst
   ├── requirements.txt
   └── uv.lock

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

docs/conf.py
------------

.. literalinclude:: conf.py
   :language: python
   :caption: docs/conf.py

docs/documentation.rst
----------------------

.. literalinclude:: documentation.rst
   :language: rst
   :caption: docs/documentation.rst

docs/index.rst
--------------

.. literalinclude:: index.rst
   :language: rst
   :caption: docs/index.rst

docs/llms.rst
-------------

.. literalinclude:: llms.rst
   :language: rst
   :caption: docs/llms.rst

docs/pelicanconf.rst
--------------------

.. literalinclude:: pelicanconf.rst
   :language: rst
   :caption: docs/pelicanconf.rst

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

src/gistblog/__init__.py
------------------------

.. literalinclude:: ../src/gistblog/__init__.py
   :language: python
   :caption: src/gistblog/__init__.py

src/gistblog/build_search_index.py
----------------------------------

.. literalinclude:: ../src/gistblog/build_search_index.py
   :language: python
   :caption: src/gistblog/build_search_index.py

src/gistblog/fetch_data.py
--------------------------

.. literalinclude:: ../src/gistblog/fetch_data.py
   :language: python
   :caption: src/gistblog/fetch_data.py

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
