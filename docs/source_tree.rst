Project source-tree
===================

Below is the layout of the project (to 10 levels), followed by
the contents of each key file.

.. code-block:: text
   :caption: Project directory layout

   gist-blog/
   ├── content
   │   ├── pages
   │   │   └── search.rst
   │   ├── 160a1cd9c12448447882f12b16e14d35.rst
   │   ├── 27c2f93e772330a4798fa7269a5ddb9b.rst
   │   ├── 2e36de0a8b64198ed98e748a0a7b7f15.rst
   │   ├── 65bd6a58ce5f2fda89594c2f4fac812a.rst
   │   ├── 7fc4de46270ba1ced2f46dc654c21add.rst
   │   ├── 916b8911e29ba9e5ee9b14916834d031.rst
   │   ├── b957e6e87d2f544054f402957d03bf7a.rst
   │   ├── cd525950b1cc849dc79306251db183fe.rst
   │   └── f041a013db9a730d2f2889663d1956f6.rst
   ├── docs
   │   └── source_tree.rst
   ├── output
   │   ├── author
   │   │   └── artur-barseghyan.html
   │   ├── category
   │   │   ├── misc.html
   │   │   └── tech.html
   │   ├── feeds
   │   │   ├── all-en.atom.xml
   │   │   ├── all.atom.xml
   │   │   ├── artur-barseghyan.atom.xml
   │   │   ├── artur-barseghyan.rss.xml
   │   │   ├── misc.atom.xml
   │   │   └── tech.atom.xml
   │   ├── pages
   │   │   └── search
   │   │       └── index.html
   │   ├── posts
   │   │   ├── 2022
   │   │   │   └── 06
   │   │   │       └── how-to-debug-python-applications
   │   │   │           └── index.html
   │   │   ├── 2025
   │   │   │   └── 03
   │   │   │       └── why-is-vivaldi-browser-a-great-companion
   │   │   │           └── index.html
   │   │   └── 2026
   │   │       ├── 02
   │   │       │   └── safezip-zero-dependency-wrapper-for-secure-zip-extraction
   │   │       │       └── index.html
   │   │       └── 04
   │   │           ├── cudatext-installation-and-config-for-sublimetext-users
   │   │           │   └── index.html
   │   │           ├── hide-pycover-files-from-ide
   │   │           │   └── index.html
   │   │           ├── log4brains-images-support
   │   │           │   └── index.html
   │   │           ├── make-scrollbars-always-visible-in-vivaldi-browser-using-stylus
   │   │           │   └── index.html
   │   │           ├── open-webui-setup-on-macos
   │   │           │   └── index.html
   │   │           └── useful-plugins-for-vscode
   │   │               └── index.html
   │   ├── tag
   │   │   ├── adrs.html
   │   │   ├── browsers.html
   │   │   ├── cudatext.html
   │   │   ├── debugging.html
   │   │   ├── ide.html
   │   │   ├── log4brains.html
   │   │   ├── macos.html
   │   │   ├── open-webui.html
   │   │   ├── progressive-web-apps.html
   │   │   ├── pycharm.html
   │   │   ├── python.html
   │   │   ├── security.html
   │   │   ├── text-editor.html
   │   │   ├── vivaldi.html
   │   │   ├── vs-code-plugins.html
   │   │   ├── vs-code.html
   │   │   └── zip.html
   │   ├── theme
   │   │   ├── css
   │   │   │   ├── fonts.css
   │   │   │   ├── main.css
   │   │   │   ├── pygment.css
   │   │   │   ├── reset.css
   │   │   │   ├── typogrify.css
   │   │   │   └── wide.css
   │   │   ├── fonts
   │   │   │   ├── font.css
   │   │   │   ├── Yanone_Kaffeesatz_400.eot
   │   │   │   ├── Yanone_Kaffeesatz_400.svg
   │   │   │   ├── Yanone_Kaffeesatz_400.ttf
   │   │   │   ├── Yanone_Kaffeesatz_400.woff
   │   │   │   └── Yanone_Kaffeesatz_400.woff2
   │   │   └── custom.css
   │   ├── archives.html
   │   ├── authors.html
   │   ├── categories.html
   │   ├── index.html
   │   └── tags.html
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
   │       │       └── Yanone_Kaffeesatz_400.woff2
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
   ├── Makefile
   ├── pelicanconf.py
   ├── README.rst
   └── requirements.txt

AGENTS.md
---------

.. literalinclude:: ../AGENTS.md
   :language: markdown
   :caption: AGENTS.md

README.rst
----------

.. literalinclude:: ../README.rst
   :language: rst
   :caption: README.rst

content/160a1cd9c12448447882f12b16e14d35.rst
--------------------------------------------

.. literalinclude:: ../content/160a1cd9c12448447882f12b16e14d35.rst
   :language: rst
   :caption: content/160a1cd9c12448447882f12b16e14d35.rst

content/27c2f93e772330a4798fa7269a5ddb9b.rst
--------------------------------------------

.. literalinclude:: ../content/27c2f93e772330a4798fa7269a5ddb9b.rst
   :language: rst
   :caption: content/27c2f93e772330a4798fa7269a5ddb9b.rst

content/2e36de0a8b64198ed98e748a0a7b7f15.rst
--------------------------------------------

.. literalinclude:: ../content/2e36de0a8b64198ed98e748a0a7b7f15.rst
   :language: rst
   :caption: content/2e36de0a8b64198ed98e748a0a7b7f15.rst

content/65bd6a58ce5f2fda89594c2f4fac812a.rst
--------------------------------------------

.. literalinclude:: ../content/65bd6a58ce5f2fda89594c2f4fac812a.rst
   :language: rst
   :caption: content/65bd6a58ce5f2fda89594c2f4fac812a.rst

content/7fc4de46270ba1ced2f46dc654c21add.rst
--------------------------------------------

.. literalinclude:: ../content/7fc4de46270ba1ced2f46dc654c21add.rst
   :language: rst
   :caption: content/7fc4de46270ba1ced2f46dc654c21add.rst

content/916b8911e29ba9e5ee9b14916834d031.rst
--------------------------------------------

.. literalinclude:: ../content/916b8911e29ba9e5ee9b14916834d031.rst
   :language: rst
   :caption: content/916b8911e29ba9e5ee9b14916834d031.rst

content/b957e6e87d2f544054f402957d03bf7a.rst
--------------------------------------------

.. literalinclude:: ../content/b957e6e87d2f544054f402957d03bf7a.rst
   :language: rst
   :caption: content/b957e6e87d2f544054f402957d03bf7a.rst

content/cd525950b1cc849dc79306251db183fe.rst
--------------------------------------------

.. literalinclude:: ../content/cd525950b1cc849dc79306251db183fe.rst
   :language: rst
   :caption: content/cd525950b1cc849dc79306251db183fe.rst

content/f041a013db9a730d2f2889663d1956f6.rst
--------------------------------------------

.. literalinclude:: ../content/f041a013db9a730d2f2889663d1956f6.rst
   :language: rst
   :caption: content/f041a013db9a730d2f2889663d1956f6.rst

content/pages/search.rst
------------------------

.. literalinclude:: ../content/pages/search.rst
   :language: rst
   :caption: content/pages/search.rst

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
