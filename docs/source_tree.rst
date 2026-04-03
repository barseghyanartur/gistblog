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
   │   └── f041a013db9a730d2f2889663d1956f6.rst
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
   │   ├── aboutwilson
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── ipython.css
   │   │   │   │   ├── local.css
   │   │   │   │   └── pygments.css
   │   │   │   ├── fonts
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   └── FontAwesome.otf
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── activestate.png
   │   │   │   │       ├── bitbucket.png
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── gitorious.png
   │   │   │   │       ├── jamendo.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── phosting.png
   │   │   │   │       ├── reader.png
   │   │   │   │       ├── rss.png
   │   │   │   │       ├── stackoverflow.png
   │   │   │   │       └── twitter.png
   │   │   │   ├── img
   │   │   │   │   ├── glyphicons-halflings-white.png
   │   │   │   │   └── glyphicons-halflings.png
   │   │   │   ├── js
   │   │   │   │   ├── bootstrap.js
   │   │   │   │   ├── bootstrap.min.js
   │   │   │   │   └── jquery-1.11.0.min.js
   │   │   │   ├── forkme_right_darkblue_121621.png
   │   │   │   └── html5.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── disqus.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── alchemy
   │   ├── apricot
   │   ├── attila
   │   ├── backdrop
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── backdrop.css
   │   │   │   │   ├── backdrop.css.map
   │   │   │   │   └── pygments.css
   │   │   │   ├── fonts
   │   │   │   │   ├── charter_bold-webfont.eot
   │   │   │   │   ├── charter_bold-webfont.ttf
   │   │   │   │   ├── charter_bold-webfont.woff
   │   │   │   │   ├── charter_bold_italic-webfont.eot
   │   │   │   │   ├── charter_bold_italic-webfont.ttf
   │   │   │   │   ├── charter_bold_italic-webfont.woff
   │   │   │   │   ├── charter_italic-webfont.eot
   │   │   │   │   ├── charter_italic-webfont.ttf
   │   │   │   │   ├── charter_italic-webfont.woff
   │   │   │   │   ├── charter_regular-webfont.eot
   │   │   │   │   ├── charter_regular-webfont.ttf
   │   │   │   │   ├── charter_regular-webfont.woff
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   ├── fontawesome-webfont.woff2
   │   │   │   │   ├── FontAwesome.otf
   │   │   │   │   └── generator_config.txt
   │   │   │   └── js
   │   │   │       ├── app.js
   │   │   │       ├── foundation.min.js
   │   │   │       ├── jquery.min.js
   │   │   │       └── modernizr.js
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── footer.html
   │   │   │   ├── index.html
   │   │   │   ├── macros.html
   │   │   │   ├── page.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── sample.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   ├── screenshot1.png
   │   │   ├── screenshot2.png
   │   │   └── screenshot3.png
   │   ├── basic
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── desert.css
   │   │   │       ├── main.css
   │   │   │       ├── mustang.css
   │   │   │       └── rdark.css
   │   │   ├── templates
   │   │   │   └── base.html
   │   │   ├── README.rst
   │   │   └── screenshot.png
   │   ├── blue-penguin
   │   ├── blue-penguin-dark
   │   ├── bluegrasshopper
   │   ├── bold
   │   ├── bootlex
   │   │   ├── static
   │   │   │   ├── bootstrap.css
   │   │   │   └── pastie.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── bootstrap
   │   │   ├── static
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── activestate.png
   │   │   │   │       ├── bitbucket.png
   │   │   │   │       ├── careers.stackoverflow.png
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── jamendo.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── phosting.png
   │   │   │   │       ├── reader.png
   │   │   │   │       ├── rss.png
   │   │   │   │       ├── stackoverflow.png
   │   │   │   │       ├── twitter.png
   │   │   │   │       └── weibo.png
   │   │   │   ├── bootstrap.min.css
   │   │   │   ├── forkme_right_darkblue_121621.png
   │   │   │   ├── html5.js
   │   │   │   ├── local.css
   │   │   │   └── pygments.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── disqus.html
   │   │   │   ├── facebook.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── metadata.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── NOTICE.txt
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── bootstrap2
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── bootstrap-responsive.min.css
   │   │   │   │   ├── bootstrap.min.css
   │   │   │   │   ├── font-awesome.css
   │   │   │   │   └── pygments.css
   │   │   │   ├── font
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.svgz
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   └── fontawesome-webfont.woff
   │   │   │   ├── img
   │   │   │   │   ├── glyphicons-halflings-white.png
   │   │   │   │   └── glyphicons-halflings.png
   │   │   │   └── js
   │   │   │       ├── autosidebar.js
   │   │   │       ├── bootstrap.min.js
   │   │   │       └── jquery-1.7.2.min.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── search_sidebar.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   ├── twitter.html
   │   │   │   └── twitter_profile.html
   │   │   ├── README.rst
   │   │   └── screenshot.png
   │   ├── bootstrap2-dark
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── bootstrap-responsive.dark.css
   │   │   │   │   ├── bootstrap.dark.css
   │   │   │   │   ├── font-awesome.css
   │   │   │   │   └── pygments.css
   │   │   │   ├── font
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.svgz
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   └── fontawesome-webfont.woff
   │   │   │   ├── img
   │   │   │   │   ├── glyphicons-halflings-white.png
   │   │   │   │   └── glyphicons-halflings.png
   │   │   │   └── js
   │   │   │       ├── autosidebar.js
   │   │   │       ├── bootstrap.min.js
   │   │   │       └── jquery-1.7.2.min.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── search_sidebar.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   ├── twitter.html
   │   │   │   └── twitter_profile.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── bricabrac
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   └── main.css
   │   │   │   └── fonts
   │   │   │       ├── alegreya
   │   │   │       │   ├── Alegreya-Bold.otf
   │   │   │       │   ├── Alegreya-Italic.otf
   │   │   │       │   ├── Alegreya-Regular.otf
   │   │   │       │   └── SIL Open Font License.txt
   │   │   │       └── alegreya-sans
   │   │   │           ├── AlegreyaSans-Bold.otf
   │   │   │           ├── AlegreyaSans-Italic.otf
   │   │   │           ├── AlegreyaSans-Medium.otf
   │   │   │           ├── AlegreyaSans-Regular.otf
   │   │   │           └── SIL Open Font License.txt
   │   │   ├── templates
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── translations
   │   │   │   └── en
   │   │   │       └── LC_MESSAGES
   │   │   │           ├── messages.mo
   │   │   │           └── messages.po
   │   │   ├── babel.cfg
   │   │   ├── messages.pot
   │   │   └── README.md
   │   ├── bricks
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── foundation.min.css
   │   │   │   │   └── lamboz.css
   │   │   │   ├── img
   │   │   │   │   ├── lego_background.jpg
   │   │   │   │   └── lego_background_mobile.jpg
   │   │   │   └── js
   │   │   │       └── modernizr.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_discus.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── credits.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── paginator.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   ├── trademark.html
   │   │   │   └── translations.html
   │   │   ├── README.md
   │   │   ├── screenshot-3.png
   │   │   ├── screenshot-mobile-2.png
   │   │   ├── screenshot-mobile.png
   │   │   └── screenshot.png
   │   ├── brownstone
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygment.css
   │   │   │   │   └── style.css
   │   │   │   └── images
   │   │   │       ├── img01.jpg
   │   │   │       ├── img02.jpg
   │   │   │       ├── img03.jpg
   │   │   │       ├── img04.jpg
   │   │   │       ├── img05.jpg
   │   │   │       └── img06.jpg
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── brutalist
   │   ├── BT3-Flat
   │   ├── built-texts
   │   │   ├── static
   │   │   │   ├── font
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   └── fontawesome-webfont.woff
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── activestate.png
   │   │   │   │       ├── bitbucket.png
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── jamendo.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── phosting.png
   │   │   │   │       ├── reader.png
   │   │   │   │       ├── rss.png
   │   │   │   │       ├── stackoverflow.png
   │   │   │   │       └── twitter.png
   │   │   │   ├── font-awesome-ie7.css
   │   │   │   ├── font-awesome.css
   │   │   │   ├── html5.js
   │   │   │   ├── local.css
   │   │   │   └── pygments.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article-sidebar.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── colophon.html
   │   │   │   ├── disqus.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── metadata.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── readme.md
   │   │   └── screenshot.png
   │   ├── bulrush
   │   ├── burrito
   │   ├── buruma
   │   ├── cebong
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   ├── typogrify.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       └── icons
   │   │   │           ├── delicious.png
   │   │   │           ├── facebook.png
   │   │   │           ├── gitorious.png
   │   │   │           ├── lastfm.png
   │   │   │           ├── linkedin.png
   │   │   │           ├── rss.png
   │   │   │           └── twitter.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.markdown
   │   │   ├── screenshot-article.png
   │   │   ├── screenshot-with-tagline.png
   │   │   └── screenshot-without-tagline.png
   │   ├── chameleon
   │   ├── chunk
   │   ├── cid
   │   ├── clean-blog
   │   ├── crowsfoot
   │   ├── custom
   │   │   ├── static
   │   │   │   └── custom.css
   │   │   ├── templates
   │   │   │   ├── base.html
   │   │   │   └── index.html
   │   │   └── __init__.py
   │   ├── dev-random
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygments.css
   │   │   │   │   └── skeleton.css
   │   │   │   ├── img
   │   │   │   │   └── corner.png
   │   │   │   └── js
   │   │   │       ├── html5shiv.js
   │   │   │       └── microTags.js
   │   │   ├── templates
   │   │   │   ├── includes
   │   │   │   │   └── sidebar.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── dev-random2
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── normalize.css
   │   │   │   │   ├── pygments.css
   │   │   │   │   ├── skeleton.css
   │   │   │   │   └── theme.css
   │   │   │   └── js
   │   │   │       ├── html5shiv.js
   │   │   │       ├── microTags.js
   │   │   │       └── microTags.min.js
   │   │   ├── templates
   │   │   │   ├── includes
   │   │   │   │   ├── article_meta.html
   │   │   │   │   └── sidebar.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── dev-random3
   │   ├── eevee
   │   ├── elegant
   │   ├── Flex
   │   ├── foundation-default-colours
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygment
   │   │   │   │   │   ├── autumn.css
   │   │   │   │   │   ├── borland.css
   │   │   │   │   │   ├── bw.css
   │   │   │   │   │   ├── colorful.css
   │   │   │   │   │   ├── default.css
   │   │   │   │   │   ├── emacs.css
   │   │   │   │   │   ├── friendly.css
   │   │   │   │   │   ├── fruity.css
   │   │   │   │   │   ├── manni.css
   │   │   │   │   │   ├── monokai.css
   │   │   │   │   │   ├── murphy.css
   │   │   │   │   │   ├── native.css
   │   │   │   │   │   ├── pastie.css
   │   │   │   │   │   ├── perldoc.css
   │   │   │   │   │   ├── tango.css
   │   │   │   │   │   ├── trac.css
   │   │   │   │   │   └── vs.css
   │   │   │   │   ├── alt-fonts.css
   │   │   │   │   ├── custom.css
   │   │   │   │   ├── foundation.css
   │   │   │   │   ├── foundation.min.css
   │   │   │   │   ├── normalize.css
   │   │   │   │   └── pygment.css
   │   │   │   ├── img
   │   │   │   └── js
   │   │   │       ├── foundation
   │   │   │       │   ├── foundation.abide.js
   │   │   │       │   ├── foundation.accordion.js
   │   │   │       │   ├── foundation.alert.js
   │   │   │       │   ├── foundation.clearing.js
   │   │   │       │   ├── foundation.dropdown.js
   │   │   │       │   ├── foundation.interchange.js
   │   │   │       │   ├── foundation.joyride.js
   │   │   │       │   ├── foundation.js
   │   │   │       │   ├── foundation.magellan.js
   │   │   │       │   ├── foundation.offcanvas.js
   │   │   │       │   ├── foundation.orbit.js
   │   │   │       │   ├── foundation.reveal.js
   │   │   │       │   ├── foundation.tab.js
   │   │   │       │   ├── foundation.tooltip.js
   │   │   │       │   └── foundation.topbar.js
   │   │   │       ├── vendor
   │   │   │       │   ├── custom.modernizr.js
   │   │   │       │   ├── fastclick.js
   │   │   │       │   ├── jquery.autocomplete.js
   │   │   │       │   ├── jquery.cookie.js
   │   │   │       │   ├── jquery.js
   │   │   │       │   ├── modernizr.js
   │   │   │       │   └── placeholder.js
   │   │   │       ├── foundation.min.js
   │   │   │       ├── jquery.js
   │   │   │       └── modernizr.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── franticworld
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── franticworld.css
   │   │   │   │   └── pygments.css
   │   │   │   └── img
   │   │   │       └── pattern.png
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   └── screenshot.png
   │   ├── free-agent
   │   ├── fresh
   │   ├── genus
   │   ├── graymill
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── custom.css
   │   │   │   │   └── milligram.css
   │   │   │   └── images
   │   │   │       └── icons
   │   │   │           ├── facebook.png
   │   │   │           ├── github.png
   │   │   │           ├── gplus.png
   │   │   │           ├── linkedin.png
   │   │   │           ├── mail.png
   │   │   │           ├── mastodon.png
   │   │   │           ├── rss.png
   │   │   │           └── twitter.png
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── footer.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── README.md
   │   │   ├── sample_pelicanconf.py
   │   │   └── screenshot.png
   │   ├── gum
   │   │   ├── static
   │   │   │   ├── fonts
   │   │   │   │   └── icons
   │   │   │   │       ├── entypo.eot
   │   │   │   │       ├── entypo.ttf
   │   │   │   │       └── entypo.woff
   │   │   │   ├── js
   │   │   │   │   ├── libs
   │   │   │   │   │   ├── ui
   │   │   │   │   │   │   └── gumby.navbar.js
   │   │   │   │   │   ├── gumby.init.js
   │   │   │   │   │   ├── gumby.js
   │   │   │   │   │   ├── gumby.min.js
   │   │   │   │   │   ├── jquery-1.9.1.min.js
   │   │   │   │   │   ├── jquery.mobile.custom.min.js
   │   │   │   │   │   └── modernizr-2.6.2.min.js
   │   │   │   │   └── plugins.js
   │   │   │   ├── gumby.css
   │   │   │   ├── pygment.css
   │   │   │   └── style.css
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── extra_footer.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   ├── screenshot.png
   │   │   └── typography.png
   │   ├── html5-dopetrope
   │   ├── hyde
   │   ├── irfan
   │   ├── iris
   │   ├── jesuislibre
   │   ├── jojo
   │   ├── Just-Read
   │   │   ├── less
   │   │   │   ├── base.less
   │   │   │   ├── codehilite.less
   │   │   │   ├── main.less
   │   │   │   ├── mixins.less
   │   │   │   ├── print.less
   │   │   │   └── var.less
   │   │   ├── psd
   │   │   │   ├── bullet.psd
   │   │   │   ├── bullet.pxm
   │   │   │   ├── line2px.psd
   │   │   │   ├── line2px.pxm
   │   │   │   ├── pages.psd
   │   │   │   └── pages.pxm
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   └── main.css
   │   │   │   └── images
   │   │   │       ├── 2px.png
   │   │   │       ├── bullet.png
   │   │   │       └── pages.png
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── metadata.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── license.md
   │   │   ├── pelican.conf.py-sample.py
   │   │   ├── readme.md
   │   │   └── screenshot.png
   │   ├── lannisport
   │   ├── lazystrap
   │   ├── lightweight
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   └── main.css
   │   │   │   ├── fonts
   │   │   │   │   └── Goudy Bookletter 1911.ttf
   │   │   │   └── images
   │   │   │       └── bg.png
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── menu.html
   │   │   │   ├── meta.html
   │   │   │   ├── page.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── LISEZ-MOI.rst
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── lovers
   │   ├── maggner-pelican
   │   ├── martin-pelican
   │   ├── martyalchin
   │   │   ├── static
   │   │   │   └── css
   │   │   │       └── style.css
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── material
   │   ├── materialistic
   │   ├── medio
   │   │   ├── screenshots
   │   │   │   ├── archives.png
   │   │   │   ├── article.png
   │   │   │   ├── author.png
   │   │   │   ├── blogroll.png
   │   │   │   ├── categories.png
   │   │   │   ├── index.png
   │   │   │   └── tags.png
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── .Rhistory
   │   │   │   │   ├── grids-responsive-min.css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── main.css.map
   │   │   │   │   └── pure-min.css
   │   │   │   ├── font-awesome-4.7.0
   │   │   │   │   ├── css
   │   │   │   │   │   ├── font-awesome.css
   │   │   │   │   │   └── font-awesome.min.css
   │   │   │   │   ├── fonts
   │   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   │   ├── fontawesome-webfont.woff2
   │   │   │   │   │   └── FontAwesome.otf
   │   │   │   │   ├── less
   │   │   │   │   │   ├── animated.less
   │   │   │   │   │   ├── bordered-pulled.less
   │   │   │   │   │   ├── core.less
   │   │   │   │   │   ├── fixed-width.less
   │   │   │   │   │   ├── font-awesome.less
   │   │   │   │   │   ├── icons.less
   │   │   │   │   │   ├── larger.less
   │   │   │   │   │   ├── list.less
   │   │   │   │   │   ├── mixins.less
   │   │   │   │   │   ├── path.less
   │   │   │   │   │   ├── rotated-flipped.less
   │   │   │   │   │   ├── screen-reader.less
   │   │   │   │   │   ├── stacked.less
   │   │   │   │   │   └── variables.less
   │   │   │   │   ├── scss
   │   │   │   │   │   ├── _animated.scss
   │   │   │   │   │   ├── _bordered-pulled.scss
   │   │   │   │   │   ├── _core.scss
   │   │   │   │   │   ├── _fixed-width.scss
   │   │   │   │   │   ├── _icons.scss
   │   │   │   │   │   ├── _larger.scss
   │   │   │   │   │   ├── _list.scss
   │   │   │   │   │   ├── _mixins.scss
   │   │   │   │   │   ├── _path.scss
   │   │   │   │   │   ├── _rotated-flipped.scss
   │   │   │   │   │   ├── _screen-reader.scss
   │   │   │   │   │   ├── _stacked.scss
   │   │   │   │   │   ├── _variables.scss
   │   │   │   │   │   └── font-awesome.scss
   │   │   │   │   └── HELP-US-OUT.txt
   │   │   │   └── images
   │   │   │       ├── authors
   │   │   │       │   └── johndoe.png
   │   │   │       └── categories
   │   │   │           └── ggplot2.png
   │   │   ├── templates
   │   │   │   ├── includes
   │   │   │   │   ├── post_metadata.html
   │   │   │   │   └── posts.html
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── blogroll.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── COPYING
   │   │   ├── example_pelicanconf.py
   │   │   └── README.md
   │   ├── mediumfox
   │   ├── medius
   │   ├── mg
   │   ├── MinimalXY
   │   ├── mnmlist
   │   │   ├── compass
   │   │   │   ├── src
   │   │   │   │   └── main.scss
   │   │   │   └── config.rb
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── main.css
   │   │   │       └── pygment.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.rst
   │   │   └── screenshot.png
   │   ├── monospace
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── main.css
   │   │   │       └── pygment.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── neat
   │   ├── nest
   │   ├── new-bootstrap2
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── bootstrap-responsive.min.css
   │   │   │   │   ├── bootstrap.min.css
   │   │   │   │   ├── font-awesome.css
   │   │   │   │   └── pygments.css
   │   │   │   ├── font
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.svgz
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   └── fontawesome-webfont.woff
   │   │   │   ├── img
   │   │   │   │   ├── glyphicons-halflings-white.png
   │   │   │   │   ├── glyphicons-halflings.png
   │   │   │   │   ├── grey.png
   │   │   │   │   └── grey_2x.png
   │   │   │   └── js
   │   │   │       ├── autosidebar.js
   │   │   │       ├── bootstrap.min.js
   │   │   │       └── jquery-1.7.2.min.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── footer.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── metryka.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── search_sidebar.html
   │   │   │   ├── shortmail.html
   │   │   │   ├── sidebar.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   ├── twitter.html
   │   │   │   └── twitter_profile.html
   │   │   ├── preview.png
   │   │   └── README.rst
   │   ├── nice-blog
   │   ├── nikhil-theme
   │   ├── niu-x2
   │   ├── nmnlist
   │   │   ├── compass
   │   │   │   ├── src
   │   │   │   │   └── main.scss
   │   │   │   └── config.rb
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── main.css
   │   │   │       └── pygment.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.rst
   │   │   └── screenshot.png
   │   ├── notebook
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   └── notebook.css
   │   │   │   └── images
   │   │   │       ├── icons
   │   │   │       │   ├── activestate.png
   │   │   │       │   ├── bitbucket.png
   │   │   │       │   ├── delicious.png
   │   │   │       │   ├── facebook.png
   │   │   │       │   ├── facebook2.png
   │   │   │       │   ├── github.png
   │   │   │       │   ├── github2.png
   │   │   │       │   ├── gplus.png
   │   │   │       │   ├── gplus2.png
   │   │   │       │   ├── jamendo.png
   │   │   │       │   ├── lastfm.png
   │   │   │       │   ├── linkedin.png
   │   │   │       │   ├── phone.png
   │   │   │       │   ├── phone2.png
   │   │   │       │   ├── phosting.png
   │   │   │       │   ├── pinterest.png
   │   │   │       │   ├── reader.png
   │   │   │       │   ├── rss.png
   │   │   │       │   ├── stackoverflow.png
   │   │   │       │   ├── twitter.png
   │   │   │       │   ├── twitter2.png
   │   │   │       │   └── weibo.png
   │   │   │       ├── avatar.png
   │   │   │       ├── download_firefox.png
   │   │   │       └── download_firefox_android.png
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── COPYING
   │   │   ├── README.md
   │   │   ├── screenshot.png
   │   │   ├── screenshot_list.png
   │   │   └── screenshot_source_code.png
   │   ├── notmyidea-cms
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       └── icons
   │   │   │           ├── delicious.png
   │   │   │           ├── gitorious.png
   │   │   │           ├── jamendo.png
   │   │   │           ├── lastfm.png
   │   │   │           ├── linkedin.png
   │   │   │           ├── rss.png
   │   │   │           ├── stackoverflow.png
   │   │   │           └── twitter.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── preview.png
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── notmyidea-cms-fr
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       └── icons
   │   │   │           ├── delicious.png
   │   │   │           ├── jamendo.png
   │   │   │           ├── lastfm.png
   │   │   │           ├── linkedin.png
   │   │   │           ├── rss.png
   │   │   │           ├── stackoverflow.png
   │   │   │           └── twitter.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── octopress
   │   ├── ops
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── custom.css
   │   │   │   │   ├── fonts.css
   │   │   │   │   ├── github-prettify-theme.css
   │   │   │   │   ├── normalize.css
   │   │   │   │   ├── pygement.css
   │   │   │   │   └── skeleton.css
   │   │   │   ├── fonts
   │   │   │   │   ├── -_Ctzj9b56b8RgXW8FArifk_vArhqVIZ0nv9q090hN8.woff2
   │   │   │   │   ├── 0AKsP294HTD-nvJgucYTaI4P5ICox8Kq3LLUNMylGO4.woff2
   │   │   │   │   ├── 0dTEPzkLWceF7z0koJaX1A.woff2
   │   │   │   │   ├── clhLqOv7MXn459PTh0gXYFK2TSYBz0eNcHnp4YqE4Ts.woff2
   │   │   │   │   ├── DK0eTGXiZjN6yA8zAEyM2Ud0sm1ffa_JvZxsF_BEwQk.woff2
   │   │   │   │   ├── Fpg3e9UodPQGSPnPRzpRPSEAvth_LlrfE80CYdSH47w.woff2
   │   │   │   │   ├── QQt14e8dY39u-eYBZmppwYlIZu-HDpmDIZMigmsroc4.woff2
   │   │   │   │   ├── rNoM5619GlhqKyeG2oawaw.woff2
   │   │   │   │   ├── STBOO2waD2LpX45SXYjQBSEAvth_LlrfE80CYdSH47w.woff2
   │   │   │   │   ├── Tdr3uiFXZJES_xwnu1bdu_esZW2xOQ-xsNqO47m55DA.woff2
   │   │   │   │   ├── WFDkXpubrEwopJnSlHV6CPk_vArhqVIZ0nv9q090hN8.woff2
   │   │   │   │   ├── xkvoNo9fC8O2RDydKj12b_k_vArhqVIZ0nv9q090hN8.woff2
   │   │   │   │   ├── yg3UMEsefgZ8IHz_ryz86IpVThvdH1ZERIrfWb3R7t4.woff2
   │   │   │   │   ├── yQiAaD56cjx1AooMTSghGfY6323mHUZFJMgTvxaG2iE.woff2
   │   │   │   │   └── ZKwULyCG95tk6mOqHQfRBCEAvth_LlrfE80CYdSH47w.woff2
   │   │   │   ├── images
   │   │   │   │   ├── aim-128.png
   │   │   │   │   ├── amazon-128.png
   │   │   │   │   ├── animexx-128.png
   │   │   │   │   ├── avatar.jpg
   │   │   │   │   ├── basecamp-128.png
   │   │   │   │   ├── behance-128.png
   │   │   │   │   ├── blogger-128.png
   │   │   │   │   ├── cloud-128.png
   │   │   │   │   ├── delicious-128.png
   │   │   │   │   ├── deviantart-128.png
   │   │   │   │   ├── digg-128.png
   │   │   │   │   ├── dribbble-128.png
   │   │   │   │   ├── dropbox-128.png
   │   │   │   │   ├── facebook-128.png
   │   │   │   │   ├── favicon.ico
   │   │   │   │   ├── flickr-128.png
   │   │   │   │   ├── github-128.png
   │   │   │   │   ├── goodread-128.png
   │   │   │   │   ├── google_plus-128.png
   │   │   │   │   ├── hangouts-128.png
   │   │   │   │   ├── houzz-128.png
   │   │   │   │   ├── instagram-128.png
   │   │   │   │   ├── itunes-128.png
   │   │   │   │   ├── linkedin-128.png
   │   │   │   │   ├── location-128.png
   │   │   │   │   ├── mail-128.png
   │   │   │   │   ├── path-128.png
   │   │   │   │   ├── paypal-128.png
   │   │   │   │   ├── picasa-128.png
   │   │   │   │   ├── pinboard-128.png
   │   │   │   │   ├── pinterest-128.png
   │   │   │   │   ├── playstation-128.png
   │   │   │   │   ├── pocket-128.png
   │   │   │   │   ├── podcast-128.png
   │   │   │   │   ├── qq-128.png
   │   │   │   │   ├── reddit-128.png
   │   │   │   │   ├── rss-128.png
   │   │   │   │   ├── skype-128.png
   │   │   │   │   ├── spotify-128.png
   │   │   │   │   ├── squarespace-128.png
   │   │   │   │   ├── stackoverflow-128.png
   │   │   │   │   ├── steam-128.png
   │   │   │   │   ├── stumbleUpon-128.png
   │   │   │   │   ├── tumblr-128.png
   │   │   │   │   ├── twitter-128.png
   │   │   │   │   ├── vimeo-128.png
   │   │   │   │   ├── vine-128.png
   │   │   │   │   ├── wechat-128.png
   │   │   │   │   ├── weibo-128.png
   │   │   │   │   ├── whatsapp-128.png
   │   │   │   │   ├── wikipedia-128.png
   │   │   │   │   ├── wordpress-128.png
   │   │   │   │   ├── youtube-128.png
   │   │   │   │   └── zhihu-128.png
   │   │   │   └── js
   │   │   │       ├── jquery.min.js
   │   │   │       ├── run_prettify.js
   │   │   │       └── site.js
   │   │   ├── templates
   │   │   │   ├── _includes
   │   │   │   │   ├── footer.html
   │   │   │   │   └── header.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   └── README.md
   │   ├── Papyrus
   │   ├── Peli-Kiera
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── main.css
   │   │   │       └── pygment.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── README.md
   │   │   ├── screenshot-1.png
   │   │   ├── screenshot-2.png
   │   │   └── screenshot-3.png
   │   ├── pelican-b-side
   │   ├── pelican-blue
   │   ├── pelican-bootstrap3
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygments
   │   │   │   │   │   ├── autumn.css
   │   │   │   │   │   ├── borland.css
   │   │   │   │   │   ├── bw.css
   │   │   │   │   │   ├── colorful.css
   │   │   │   │   │   ├── default.css
   │   │   │   │   │   ├── emacs.css
   │   │   │   │   │   ├── friendly.css
   │   │   │   │   │   ├── fruity.css
   │   │   │   │   │   ├── github.css
   │   │   │   │   │   ├── igor.css
   │   │   │   │   │   ├── manni.css
   │   │   │   │   │   ├── monokai.css
   │   │   │   │   │   ├── murphy.css
   │   │   │   │   │   ├── native.css
   │   │   │   │   │   ├── paraiso-dark.css
   │   │   │   │   │   ├── paraiso-light.css
   │   │   │   │   │   ├── pastie.css
   │   │   │   │   │   ├── perldoc.css
   │   │   │   │   │   ├── rrt.css
   │   │   │   │   │   ├── solarizeddark.css
   │   │   │   │   │   ├── solarizedlight.css
   │   │   │   │   │   ├── tango.css
   │   │   │   │   │   ├── trac.css
   │   │   │   │   │   ├── vim.css
   │   │   │   │   │   ├── vs.css
   │   │   │   │   │   ├── xcode.css
   │   │   │   │   │   └── zenburn.css
   │   │   │   │   ├── shariff
   │   │   │   │   │   └── shariff.min.css
   │   │   │   │   ├── bootstrap.cerulean.min.css
   │   │   │   │   ├── bootstrap.cosmo.min.css
   │   │   │   │   ├── bootstrap.cupid.min.css
   │   │   │   │   ├── bootstrap.custom.min.css
   │   │   │   │   ├── bootstrap.cyborg.min.css
   │   │   │   │   ├── bootstrap.darkly.min.css
   │   │   │   │   ├── bootstrap.flatly.min.css
   │   │   │   │   ├── bootstrap.journal.min.css
   │   │   │   │   ├── bootstrap.lumen.min.css
   │   │   │   │   ├── bootstrap.min.css
   │   │   │   │   ├── bootstrap.paper.min.css
   │   │   │   │   ├── bootstrap.readable-old.min.css
   │   │   │   │   ├── bootstrap.readable.min.css
   │   │   │   │   ├── bootstrap.sandstone.min.css
   │   │   │   │   ├── bootstrap.shamrock.min.css
   │   │   │   │   ├── bootstrap.simplex.min.css
   │   │   │   │   ├── bootstrap.slate.min.css
   │   │   │   │   ├── bootstrap.spacelab.min.css
   │   │   │   │   ├── bootstrap.superhero.min.css
   │   │   │   │   ├── bootstrap.united.min.css
   │   │   │   │   ├── bootstrap.yeti.min.css
   │   │   │   │   ├── font-awesome.css
   │   │   │   │   ├── font-awesome.css.map
   │   │   │   │   ├── font-awesome.min.css
   │   │   │   │   ├── html4css1.css
   │   │   │   │   ├── style.css
   │   │   │   │   └── typogrify.css
   │   │   │   ├── fonts
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   ├── fontawesome-webfont.woff2
   │   │   │   │   ├── FontAwesome.otf
   │   │   │   │   ├── glyphicons-halflings-regular.eot
   │   │   │   │   ├── glyphicons-halflings-regular.svg
   │   │   │   │   ├── glyphicons-halflings-regular.ttf
   │   │   │   │   ├── glyphicons-halflings-regular.woff
   │   │   │   │   └── glyphicons-halflings-regular.woff2
   │   │   │   ├── js
   │   │   │   │   ├── bodypadding.js
   │   │   │   │   ├── bootstrap.min.js
   │   │   │   │   ├── github.js
   │   │   │   │   ├── jquery.min.js
   │   │   │   │   ├── jXHR.js
   │   │   │   │   ├── respond.min.js
   │   │   │   │   └── shariff.min.js
   │   │   │   └── tipuesearch
   │   │   │       ├── tipuesearch.css
   │   │   │       ├── tipuesearch.js
   │   │   │       ├── tipuesearch.min.js
   │   │   │       ├── tipuesearch_content.js
   │   │   │       └── tipuesearch_set.js
   │   │   ├── templates
   │   │   │   ├── includes
   │   │   │   │   ├── sidebar
   │   │   │   │   │   ├── archive.html
   │   │   │   │   │   ├── article-li.html
   │   │   │   │   │   ├── authors.html
   │   │   │   │   │   ├── categories.html
   │   │   │   │   │   ├── github-js.html
   │   │   │   │   │   ├── github.html
   │   │   │   │   │   ├── images.html
   │   │   │   │   │   ├── links.html
   │   │   │   │   │   ├── macros.jinja
   │   │   │   │   │   ├── recent_posts.html
   │   │   │   │   │   ├── series.html
   │   │   │   │   │   ├── show_source.html
   │   │   │   │   │   ├── social.html
   │   │   │   │   │   ├── tag_cloud.html
   │   │   │   │   │   └── twitter_timeline.html
   │   │   │   │   ├── aboutme.html
   │   │   │   │   ├── addthis.html
   │   │   │   │   ├── article_info.html
   │   │   │   │   ├── banner.html
   │   │   │   │   ├── cc-license.html
   │   │   │   │   ├── comment_count.html
   │   │   │   │   ├── comments.html
   │   │   │   │   ├── disqus_script.html
   │   │   │   │   ├── footer.html
   │   │   │   │   ├── ga.html
   │   │   │   │   ├── liquid_tags_nb_footer.html
   │   │   │   │   ├── liquid_tags_nb_header.html
   │   │   │   │   ├── matomo.html
   │   │   │   │   ├── minify_tipuesearch.html
   │   │   │   │   ├── pagination.html
   │   │   │   │   ├── piwik.html
   │   │   │   │   ├── related-posts.html
   │   │   │   │   ├── series.html
   │   │   │   │   ├── shariff.html
   │   │   │   │   ├── show_source.html
   │   │   │   │   ├── sidebar.html
   │   │   │   │   ├── taglist.html
   │   │   │   │   ├── translations.html
   │   │   │   │   └── twitter_cards.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_list.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── search.html
   │   │   │   ├── tag.html
   │   │   │   └── tags.html
   │   │   ├── translations
   │   │   │   ├── ca
   │   │   │   │   └── LC_MESSAGES
   │   │   │   │       ├── messages.mo
   │   │   │   │       └── messages.po
   │   │   │   ├── de
   │   │   │   │   └── LC_MESSAGES
   │   │   │   │       ├── messages.mo
   │   │   │   │       └── messages.po
   │   │   │   └── fr
   │   │   │       └── LC_MESSAGES
   │   │   │           ├── messages.mo
   │   │   │           └── messages.po
   │   │   ├── AUTHORS.md
   │   │   ├── babel.cfg
   │   │   ├── CONTRIBUTING.md
   │   │   ├── EXAMPLES.md
   │   │   ├── Makefile
   │   │   ├── messages.pot
   │   │   ├── README.md
   │   │   ├── screenshot-article.png
   │   │   └── screenshot.png
   │   ├── pelican-cait
   │   ├── pelican-fh5co-marble
   │   ├── pelican-haerwu-theme
   │   ├── pelican-hss
   │   ├── pelican-mockingbird
   │   ├── pelican-simplegrey
   │   ├── pelican-sober
   │   ├── pelican-striped-html5up
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── images
   │   │   │   │   │   ├── bg01.png
   │   │   │   │   │   └── bg02.png
   │   │   │   │   ├── font-awesome.min.css
   │   │   │   │   ├── ie8.css
   │   │   │   │   └── main.css
   │   │   │   ├── fonts
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.svg
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   ├── fontawesome-webfont.woff2
   │   │   │   │   └── FontAwesome.otf
   │   │   │   ├── js
   │   │   │   │   ├── ie
   │   │   │   │   │   ├── html5shiv.js
   │   │   │   │   │   ├── PIE.htc
   │   │   │   │   │   └── respond.min.js
   │   │   │   │   ├── jquery.min.js
   │   │   │   │   ├── main.js
   │   │   │   │   ├── skel.min.js
   │   │   │   │   └── util.js
   │   │   │   └── sass
   │   │   │       ├── libs
   │   │   │       │   ├── _functions.scss
   │   │   │       │   ├── _mixins.scss
   │   │   │       │   ├── _skel.scss
   │   │   │       │   └── _vars.scss
   │   │   │       ├── ie8.scss
   │   │   │       └── main.scss
   │   │   ├── templates
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── gosquared.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── pelicanconf.py.py-sample.py
   │   │   ├── README.md
   │   │   ├── screenshot.png
   │   │   └── screenshot2.png
   │   ├── pelican-twitchy
   │   ├── pelicanthemes-generator
   │   ├── photowall
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   ├── typogrify.css
   │   │   │   │   └── wide.css
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── aboutme.png
   │   │   │   │       ├── bitbucket.png
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── gitorious.png
   │   │   │   │       ├── gittip.png
   │   │   │   │       ├── google-groups.png
   │   │   │   │       ├── google-plus.png
   │   │   │   │       ├── hackernews.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── reddit.png
   │   │   │   │       ├── rss.png
   │   │   │   │       ├── slideshare.png
   │   │   │   │       ├── speakerdeck.png
   │   │   │   │       ├── stackoverflow.png
   │   │   │   │       ├── twitter.png
   │   │   │   │       ├── vimeo.png
   │   │   │   │       └── youtube.png
   │   │   │   └── js
   │   │   │       └── mousetrap.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── photowall.jpg
   │   │   └── readme.md
   │   ├── pjport
   │   ├── plumage
   │   ├── pujangga
   │   ├── relapse
   │   ├── Responsive-Pelican
   │   ├── resume
   │   ├── semantic-ui
   │   ├── simple-bootstrap
   │   │   ├── static
   │   │   │   ├── static
   │   │   │   │   └── css
   │   │   │   │       └── style.css
   │   │   │   └── style.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── readme.md
   │   │   └── screenshot.png
   │   ├── simplify-theme
   │   ├── smoothie
   │   ├── sneakyidea
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       ├── icons
   │   │   │       │   ├── delicious.png
   │   │   │       │   ├── github.png
   │   │   │       │   ├── lastfm.png
   │   │   │       │   ├── linkedin.png
   │   │   │       │   ├── rss.png
   │   │   │       │   └── twitter.png
   │   │   │       └── bg.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── google_plusone.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.rst
   │   │   └── screenshot.png
   │   ├── SOB
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   └── main.css
   │   │   │   └── images
   │   │   │       └── icons
   │   │   │           ├── delicious.png
   │   │   │           ├── github.png
   │   │   │           ├── gitorious.png
   │   │   │           ├── gittip.png
   │   │   │           ├── google-plus.png
   │   │   │           ├── lastfm.png
   │   │   │           ├── linkedin.png
   │   │   │           ├── rss.png
   │   │   │           └── twitter.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── article_infos_bottom.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disclaimer.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── translations.html
   │   │   ├── License.txt
   │   │   └── README.md
   │   ├── SoMA
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── body-bg.jpg
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   ├── typogrify.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       ├── icons
   │   │   │       │   ├── delicious.png
   │   │   │       │   ├── facebook.png
   │   │   │       │   ├── github.png
   │   │   │       │   ├── gitorious.png
   │   │   │       │   ├── gittip.png
   │   │   │       │   ├── google-plus.png
   │   │   │       │   ├── lastfm.png
   │   │   │       │   ├── linkedin.png
   │   │   │       │   ├── rss.png
   │   │   │       │   └── twitter.png
   │   │   │       └── body-bg.jpg
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── facebook_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── SoMA2
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── body-bg.jpg
   │   │   │   │   ├── main.css
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── reset.css
   │   │   │   │   ├── typogrify.css
   │   │   │   │   └── wide.css
   │   │   │   └── images
   │   │   │       ├── icons
   │   │   │       │   ├── delicious.png
   │   │   │       │   ├── facebook.png
   │   │   │       │   ├── github.png
   │   │   │       │   ├── gitorious.png
   │   │   │       │   ├── gittip.png
   │   │   │       │   ├── google-plus.png
   │   │   │       │   ├── lastfm.png
   │   │   │       │   ├── linkedin.png
   │   │   │       │   ├── rss.png
   │   │   │       │   └── twitter.png
   │   │   │       ├── blue-pin.png
   │   │   │       ├── body-bg.jpg
   │   │   │       └── favicon.ico
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── facebook_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── sora
   │   ├── stirring
   │   ├── storm
   │   ├── subtle
   │   │   ├── static
   │   │   │   └── css
   │   │   │       ├── downdown.png
   │   │   │       ├── groovepaper.png
   │   │   │       ├── lightpaper.png
   │   │   │       ├── main.css
   │   │   │       ├── paper.png
   │   │   │       ├── pygment.css
   │   │   │       ├── reset.css
   │   │   │       ├── toptop.png
   │   │   │       ├── typogrify.css
   │   │   │       ├── wavecut.png
   │   │   │       ├── white.png
   │   │   │       └── wide.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── gosquared.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── taglist.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   ├── screenshot-1-top.png
   │   │   └── screenshot-2-bottom.png
   │   ├── sundown
   │   ├── supersimple
   │   ├── svbhack
   │   ├── svbtle
   │   ├── syte
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygments.css
   │   │   │   │   └── styles.css
   │   │   │   ├── imgs
   │   │   │   │   ├── b.png
   │   │   │   │   ├── favicon.ico
   │   │   │   │   ├── ico-comments.png
   │   │   │   │   ├── ico-forks.png
   │   │   │   │   ├── ico-likes.png
   │   │   │   │   ├── ico-plusoners copy.png
   │   │   │   │   ├── ico-plusoners.png
   │   │   │   │   ├── ico-resharers copy.png
   │   │   │   │   ├── ico-resharers.png
   │   │   │   │   └── ico-watchers.png
   │   │   │   ├── js
   │   │   │   │   ├── libs
   │   │   │   │   │   ├── bootstrap-modal.js
   │   │   │   │   │   ├── github.js
   │   │   │   │   │   ├── google+.js
   │   │   │   │   │   ├── handlebars.js
   │   │   │   │   │   ├── instagram.js
   │   │   │   │   │   ├── jquery-1.7.2.min.js
   │   │   │   │   │   ├── jquery.url.js
   │   │   │   │   │   ├── json.js
   │   │   │   │   │   ├── moment.min.js
   │   │   │   │   │   ├── prettify.js
   │   │   │   │   │   ├── require.js
   │   │   │   │   │   ├── spin.min.js
   │   │   │   │   │   ├── text.js
   │   │   │   │   │   └── twitter.js
   │   │   │   │   └── common.js
   │   │   │   └── templates
   │   │   │       ├── github-view.html
   │   │   │       ├── google-view.html
   │   │   │       ├── instagram-view.html
   │   │   │       └── twitter-view.html
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── github.html
   │   │   │   ├── google_plusone.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── taman
   │   ├── tuxlite_tbs
   │   │   ├── static
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── activestate.png
   │   │   │   │       ├── bitbucket.png
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── gitorious.png
   │   │   │   │       ├── glyphicons-halflings-white.png
   │   │   │   │       ├── glyphicons-halflings.png
   │   │   │   │       ├── jamendo.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── phosting.png
   │   │   │   │       ├── reader.png
   │   │   │   │       ├── rss.png
   │   │   │   │       ├── stackoverflow.png
   │   │   │   │       └── twitter.png
   │   │   │   ├── bootstrap-collapse.js
   │   │   │   ├── bootstrap.min.css
   │   │   │   ├── bootstrap.min.responsive.css
   │   │   │   ├── forkme_right_darkblue_121621.png
   │   │   │   ├── html5.js
   │   │   │   ├── local.css
   │   │   │   └── pygments.css
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── author.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── disqus.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── metadata.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── sitemap.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── tuxlite_zf
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── foundation.min.css
   │   │   │   │   ├── normalize.css
   │   │   │   │   ├── pygments.css
   │   │   │   │   └── style.css
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── gitorious.png
   │   │   │   │       ├── gittip.png
   │   │   │   │       ├── google-plus.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── rss.png
   │   │   │   │       └── twitter.png
   │   │   │   └── js
   │   │   │       ├── custom.modernizr.js
   │   │   │       ├── foundation.min.js
   │   │   │       ├── jquery.js
   │   │   │       └── zepto.js
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── article_infos_bottom.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── License.txt
   │   │   ├── README.md
   │   │   └── Screenshot.png
   │   ├── twenty-html5up
   │   ├── uikit
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── components
   │   │   │   │   │   ├── accordion.almost-flat.css
   │   │   │   │   │   ├── accordion.almost-flat.min.css
   │   │   │   │   │   ├── accordion.css
   │   │   │   │   │   ├── accordion.gradient.css
   │   │   │   │   │   ├── accordion.gradient.min.css
   │   │   │   │   │   ├── accordion.min.css
   │   │   │   │   │   ├── autocomplete.almost-flat.css
   │   │   │   │   │   ├── autocomplete.almost-flat.min.css
   │   │   │   │   │   ├── autocomplete.css
   │   │   │   │   │   ├── autocomplete.gradient.css
   │   │   │   │   │   ├── autocomplete.gradient.min.css
   │   │   │   │   │   ├── autocomplete.min.css
   │   │   │   │   │   ├── datepicker.almost-flat.css
   │   │   │   │   │   ├── datepicker.almost-flat.min.css
   │   │   │   │   │   ├── datepicker.css
   │   │   │   │   │   ├── datepicker.gradient.css
   │   │   │   │   │   ├── datepicker.gradient.min.css
   │   │   │   │   │   ├── datepicker.min.css
   │   │   │   │   │   ├── dotnav.almost-flat.css
   │   │   │   │   │   ├── dotnav.almost-flat.min.css
   │   │   │   │   │   ├── dotnav.css
   │   │   │   │   │   ├── dotnav.gradient.css
   │   │   │   │   │   ├── dotnav.gradient.min.css
   │   │   │   │   │   ├── dotnav.min.css
   │   │   │   │   │   ├── form-advanced.almost-flat.css
   │   │   │   │   │   ├── form-advanced.almost-flat.min.css
   │   │   │   │   │   ├── form-advanced.css
   │   │   │   │   │   ├── form-advanced.gradient.css
   │   │   │   │   │   ├── form-advanced.gradient.min.css
   │   │   │   │   │   ├── form-advanced.min.css
   │   │   │   │   │   ├── form-file.almost-flat.css
   │   │   │   │   │   ├── form-file.almost-flat.min.css
   │   │   │   │   │   ├── form-file.css
   │   │   │   │   │   ├── form-file.gradient.css
   │   │   │   │   │   ├── form-file.gradient.min.css
   │   │   │   │   │   ├── form-file.min.css
   │   │   │   │   │   ├── form-password.almost-flat.css
   │   │   │   │   │   ├── form-password.almost-flat.min.css
   │   │   │   │   │   ├── form-password.css
   │   │   │   │   │   ├── form-password.gradient.css
   │   │   │   │   │   ├── form-password.gradient.min.css
   │   │   │   │   │   ├── form-password.min.css
   │   │   │   │   │   ├── form-select.almost-flat.css
   │   │   │   │   │   ├── form-select.almost-flat.min.css
   │   │   │   │   │   ├── form-select.css
   │   │   │   │   │   ├── form-select.gradient.css
   │   │   │   │   │   ├── form-select.gradient.min.css
   │   │   │   │   │   ├── form-select.min.css
   │   │   │   │   │   ├── htmleditor.almost-flat.css
   │   │   │   │   │   ├── htmleditor.almost-flat.min.css
   │   │   │   │   │   ├── htmleditor.css
   │   │   │   │   │   ├── htmleditor.gradient.css
   │   │   │   │   │   ├── htmleditor.gradient.min.css
   │   │   │   │   │   ├── htmleditor.min.css
   │   │   │   │   │   ├── nestable.almost-flat.css
   │   │   │   │   │   ├── nestable.almost-flat.min.css
   │   │   │   │   │   ├── nestable.css
   │   │   │   │   │   ├── nestable.gradient.css
   │   │   │   │   │   ├── nestable.gradient.min.css
   │   │   │   │   │   ├── nestable.min.css
   │   │   │   │   │   ├── notify.almost-flat.css
   │   │   │   │   │   ├── notify.almost-flat.min.css
   │   │   │   │   │   ├── notify.css
   │   │   │   │   │   ├── notify.gradient.css
   │   │   │   │   │   ├── notify.gradient.min.css
   │   │   │   │   │   ├── notify.min.css
   │   │   │   │   │   ├── placeholder.almost-flat.css
   │   │   │   │   │   ├── placeholder.almost-flat.min.css
   │   │   │   │   │   ├── placeholder.css
   │   │   │   │   │   ├── placeholder.gradient.css
   │   │   │   │   │   ├── placeholder.gradient.min.css
   │   │   │   │   │   ├── placeholder.min.css
   │   │   │   │   │   ├── progress.almost-flat.css
   │   │   │   │   │   ├── progress.almost-flat.min.css
   │   │   │   │   │   ├── progress.css
   │   │   │   │   │   ├── progress.gradient.css
   │   │   │   │   │   ├── progress.gradient.min.css
   │   │   │   │   │   ├── progress.min.css
   │   │   │   │   │   ├── search.almost-flat.css
   │   │   │   │   │   ├── search.almost-flat.min.css
   │   │   │   │   │   ├── search.css
   │   │   │   │   │   ├── search.gradient.css
   │   │   │   │   │   ├── search.gradient.min.css
   │   │   │   │   │   ├── search.min.css
   │   │   │   │   │   ├── slidenav.almost-flat.css
   │   │   │   │   │   ├── slidenav.almost-flat.min.css
   │   │   │   │   │   ├── slidenav.css
   │   │   │   │   │   ├── slidenav.gradient.css
   │   │   │   │   │   ├── slidenav.gradient.min.css
   │   │   │   │   │   ├── slidenav.min.css
   │   │   │   │   │   ├── slider.almost-flat.css
   │   │   │   │   │   ├── slider.almost-flat.min.css
   │   │   │   │   │   ├── slider.css
   │   │   │   │   │   ├── slider.gradient.css
   │   │   │   │   │   ├── slider.gradient.min.css
   │   │   │   │   │   ├── slider.min.css
   │   │   │   │   │   ├── slideshow.almost-flat.css
   │   │   │   │   │   ├── slideshow.almost-flat.min.css
   │   │   │   │   │   ├── slideshow.css
   │   │   │   │   │   ├── slideshow.gradient.css
   │   │   │   │   │   ├── slideshow.gradient.min.css
   │   │   │   │   │   ├── slideshow.min.css
   │   │   │   │   │   ├── sortable.almost-flat.css
   │   │   │   │   │   ├── sortable.almost-flat.min.css
   │   │   │   │   │   ├── sortable.css
   │   │   │   │   │   ├── sortable.gradient.css
   │   │   │   │   │   ├── sortable.gradient.min.css
   │   │   │   │   │   ├── sortable.min.css
   │   │   │   │   │   ├── sticky.almost-flat.css
   │   │   │   │   │   ├── sticky.almost-flat.min.css
   │   │   │   │   │   ├── sticky.css
   │   │   │   │   │   ├── sticky.gradient.css
   │   │   │   │   │   ├── sticky.gradient.min.css
   │   │   │   │   │   ├── sticky.min.css
   │   │   │   │   │   ├── tooltip.almost-flat.css
   │   │   │   │   │   ├── tooltip.almost-flat.min.css
   │   │   │   │   │   ├── tooltip.css
   │   │   │   │   │   ├── tooltip.gradient.css
   │   │   │   │   │   ├── tooltip.gradient.min.css
   │   │   │   │   │   ├── tooltip.min.css
   │   │   │   │   │   ├── upload.almost-flat.css
   │   │   │   │   │   ├── upload.almost-flat.min.css
   │   │   │   │   │   ├── upload.css
   │   │   │   │   │   ├── upload.gradient.css
   │   │   │   │   │   ├── upload.gradient.min.css
   │   │   │   │   │   └── upload.min.css
   │   │   │   │   ├── custom.css
   │   │   │   │   ├── custom.min.css
   │   │   │   │   ├── index.html
   │   │   │   │   ├── pygment.css
   │   │   │   │   ├── pygment.min.css
   │   │   │   │   ├── uikit.almost-flat.css
   │   │   │   │   ├── uikit.almost-flat.min.css
   │   │   │   │   ├── uikit.css
   │   │   │   │   ├── uikit.gradient.css
   │   │   │   │   ├── uikit.gradient.min.css
   │   │   │   │   └── uikit.min.css
   │   │   │   ├── fonts
   │   │   │   │   ├── fontawesome-webfont.eot
   │   │   │   │   ├── fontawesome-webfont.ttf
   │   │   │   │   ├── fontawesome-webfont.woff
   │   │   │   │   ├── fontawesome-webfont.woff2
   │   │   │   │   └── FontAwesome.otf
   │   │   │   ├── ico
   │   │   │   │   ├── cc
   │   │   │   │   │   ├── by-nc
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   ├── by-nc-nd
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   ├── by-nc-sa
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   ├── by-nd
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   ├── by-nd-nc
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   ├── by-sa
   │   │   │   │   │   │   └── 4.0
   │   │   │   │   │   │       ├── 80x15.png
   │   │   │   │   │   │       └── 88x31.png
   │   │   │   │   │   └── licenses.sh
   │   │   │   │   └── favicon
   │   │   │   │       ├── android-chrome-144x144.png
   │   │   │   │       ├── android-chrome-192x192.png
   │   │   │   │       ├── android-chrome-36x36.png
   │   │   │   │       ├── android-chrome-48x48.png
   │   │   │   │       ├── android-chrome-72x72.png
   │   │   │   │       ├── android-chrome-96x96.png
   │   │   │   │       ├── apple-touch-icon-114x114.png
   │   │   │   │       ├── apple-touch-icon-120x120.png
   │   │   │   │       ├── apple-touch-icon-144x144.png
   │   │   │   │       ├── apple-touch-icon-152x152.png
   │   │   │   │       ├── apple-touch-icon-180x180.png
   │   │   │   │       ├── apple-touch-icon-57x57.png
   │   │   │   │       ├── apple-touch-icon-60x60.png
   │   │   │   │       ├── apple-touch-icon-72x72.png
   │   │   │   │       ├── apple-touch-icon-76x76.png
   │   │   │   │       ├── apple-touch-icon-precomposed.png
   │   │   │   │       ├── apple-touch-icon.png
   │   │   │   │       ├── browserconfig.xml
   │   │   │   │       ├── favicon-16x16.png
   │   │   │   │       ├── favicon-32x32.png
   │   │   │   │       ├── favicon-96x96.png
   │   │   │   │       ├── favicon.ico
   │   │   │   │       ├── manifest.json
   │   │   │   │       ├── mstile-144x144.png
   │   │   │   │       ├── mstile-150x150.png
   │   │   │   │       ├── mstile-310x150.png
   │   │   │   │       ├── mstile-310x310.png
   │   │   │   │       ├── mstile-70x70.png
   │   │   │   │       └── safari-pinned-tab.svg
   │   │   │   ├── img
   │   │   │   │   ├── author.svg
   │   │   │   │   ├── yoshi.png
   │   │   │   │   └── yoshi.png.bak
   │   │   │   └── js
   │   │   │       ├── components
   │   │   │       │   ├── accordion.js
   │   │   │       │   ├── accordion.min.js
   │   │   │       │   ├── autocomplete.js
   │   │   │       │   ├── autocomplete.min.js
   │   │   │       │   ├── datepicker.js
   │   │   │       │   ├── datepicker.min.js
   │   │   │       │   ├── form-password.js
   │   │   │       │   ├── form-password.min.js
   │   │   │       │   ├── form-select.js
   │   │   │       │   ├── form-select.min.js
   │   │   │       │   ├── grid.js
   │   │   │       │   ├── grid.min.js
   │   │   │       │   ├── htmleditor.js
   │   │   │       │   ├── htmleditor.min.js
   │   │   │       │   ├── lightbox.js
   │   │   │       │   ├── lightbox.min.js
   │   │   │       │   ├── nestable.js
   │   │   │       │   ├── nestable.min.js
   │   │   │       │   ├── notify.js
   │   │   │       │   ├── notify.min.js
   │   │   │       │   ├── pagination.js
   │   │   │       │   ├── pagination.min.js
   │   │   │       │   ├── parallax.js
   │   │   │       │   ├── parallax.min.js
   │   │   │       │   ├── search.js
   │   │   │       │   ├── search.min.js
   │   │   │       │   ├── slider.js
   │   │   │       │   ├── slider.min.js
   │   │   │       │   ├── slideset.js
   │   │   │       │   ├── slideset.min.js
   │   │   │       │   ├── slideshow-fx.js
   │   │   │       │   ├── slideshow-fx.min.js
   │   │   │       │   ├── slideshow.js
   │   │   │       │   ├── slideshow.min.js
   │   │   │       │   ├── sortable.js
   │   │   │       │   ├── sortable.min.js
   │   │   │       │   ├── sticky.js
   │   │   │       │   ├── sticky.min.js
   │   │   │       │   ├── timepicker.js
   │   │   │       │   ├── timepicker.min.js
   │   │   │       │   ├── tooltip.js
   │   │   │       │   ├── tooltip.min.js
   │   │   │       │   ├── upload.js
   │   │   │       │   └── upload.min.js
   │   │   │       ├── core
   │   │   │       │   ├── alert.js
   │   │   │       │   ├── alert.min.js
   │   │   │       │   ├── button.js
   │   │   │       │   ├── button.min.js
   │   │   │       │   ├── core.js
   │   │   │       │   ├── core.min.js
   │   │   │       │   ├── cover.js
   │   │   │       │   ├── cover.min.js
   │   │   │       │   ├── dropdown.js
   │   │   │       │   ├── dropdown.min.js
   │   │   │       │   ├── grid.js
   │   │   │       │   ├── grid.min.js
   │   │   │       │   ├── modal.js
   │   │   │       │   ├── modal.min.js
   │   │   │       │   ├── nav.js
   │   │   │       │   ├── nav.min.js
   │   │   │       │   ├── offcanvas.js
   │   │   │       │   ├── offcanvas.min.js
   │   │   │       │   ├── scrollspy.js
   │   │   │       │   ├── scrollspy.min.js
   │   │   │       │   ├── smooth-scroll.js
   │   │   │       │   ├── smooth-scroll.min.js
   │   │   │       │   ├── switcher.js
   │   │   │       │   ├── switcher.min.js
   │   │   │       │   ├── tab.js
   │   │   │       │   ├── tab.min.js
   │   │   │       │   ├── toggle.js
   │   │   │       │   ├── toggle.min.js
   │   │   │       │   ├── touch.js
   │   │   │       │   ├── touch.min.js
   │   │   │       │   ├── utility.js
   │   │   │       │   └── utility.min.js
   │   │   │       ├── lib
   │   │   │       │   ├── extensions
   │   │   │       │   │   ├── MathEvents.js
   │   │   │       │   │   ├── MathMenu.js
   │   │   │       │   │   ├── MathZoom.js
   │   │   │       │   │   ├── mml2jax.js
   │   │   │       │   │   └── tex2jax.js
   │   │   │       │   ├── jax
   │   │   │       │   │   ├── input
   │   │   │       │   │   │   ├── MathML
   │   │   │       │   │   │   │   └── config.js
   │   │   │       │   │   │   └── TeX
   │   │   │       │   │   │       └── config.js
   │   │   │       │   │   └── output
   │   │   │       │   │       └── HTML-CSS
   │   │   │       │   │           └── config.js
   │   │   │       │   ├── jquery-1.11.3.js
   │   │   │       │   ├── jquery-1.11.3.min.js
   │   │   │       │   └── MathJax.js
   │   │   │       ├── uikit.js
   │   │   │       └── uikit.min.js
   │   │   ├── templates
   │   │   │   ├── _sidebar.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_macros.html
   │   │   │   ├── articles.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── cc_license.html
   │   │   │   ├── html_macros.html
   │   │   │   ├── index.html
   │   │   │   ├── menu_macros.html
   │   │   │   ├── page.html
   │   │   │   ├── period_archives.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   ├── time_macros.html
   │   │   │   └── uikit.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── voce
   │   ├── voidy-bootstrap
   │   ├── w3-personal-blog
   │   ├── water-iris
   │   ├── waterspill
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygment.css
   │   │   │   │   └── style.css
   │   │   │   └── images
   │   │   │       ├── background.jpg
   │   │   │       ├── body.gif
   │   │   │       ├── bottom.gif
   │   │   │       ├── header.gif
   │   │   │       ├── hr.gif
   │   │   │       ├── menubar.gif
   │   │   │       └── spill.gif
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── README.md
   │   │   └── screenshot.png
   │   ├── waterspill-en
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── pygment.css
   │   │   │   │   └── style.css
   │   │   │   └── images
   │   │   │       ├── background.jpg
   │   │   │       ├── body.gif
   │   │   │       ├── bottom.gif
   │   │   │       ├── header.gif
   │   │   │       ├── hr.gif
   │   │   │       ├── menubar.gif
   │   │   │       └── spill.gif
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   └── twitter.html
   │   │   ├── license.md
   │   │   ├── README.md
   │   │   ├── screenshot-suppressed-categories.png
   │   │   └── screenshot.png
   │   ├── WhatsTheScoop
   │   ├── yapeme
   │   ├── zurb-F5-basic
   │   │   ├── static
   │   │   │   ├── css
   │   │   │   │   ├── foundation.css
   │   │   │   │   ├── foundation.min.css
   │   │   │   │   ├── normalize.css
   │   │   │   │   ├── pygments.css
   │   │   │   │   └── style.css
   │   │   │   ├── images
   │   │   │   │   └── icons
   │   │   │   │       ├── delicious.png
   │   │   │   │       ├── facebook.png
   │   │   │   │       ├── github.png
   │   │   │   │       ├── gitorious.png
   │   │   │   │       ├── gittip.png
   │   │   │   │       ├── google-plus.png
   │   │   │   │       ├── lastfm.png
   │   │   │   │       ├── linkedin.png
   │   │   │   │       ├── rss.png
   │   │   │   │       └── twitter.png
   │   │   │   ├── js
   │   │   │   │   ├── foundation
   │   │   │   │   │   ├── foundation.abide.js
   │   │   │   │   │   ├── foundation.accordion.js
   │   │   │   │   │   ├── foundation.alert.js
   │   │   │   │   │   ├── foundation.clearing.js
   │   │   │   │   │   ├── foundation.dropdown.js
   │   │   │   │   │   ├── foundation.interchange.js
   │   │   │   │   │   ├── foundation.joyride.js
   │   │   │   │   │   ├── foundation.js
   │   │   │   │   │   ├── foundation.magellan.js
   │   │   │   │   │   ├── foundation.offcanvas.js
   │   │   │   │   │   ├── foundation.orbit.js
   │   │   │   │   │   ├── foundation.reveal.js
   │   │   │   │   │   ├── foundation.tab.js
   │   │   │   │   │   ├── foundation.tooltip.js
   │   │   │   │   │   └── foundation.topbar.js
   │   │   │   │   ├── vendor
   │   │   │   │   │   ├── custom.modernizr.js
   │   │   │   │   │   ├── fastclick.js
   │   │   │   │   │   ├── jquery.autocomplete.js
   │   │   │   │   │   ├── jquery.cookie.js
   │   │   │   │   │   ├── jquery.js
   │   │   │   │   │   └── placeholder.js
   │   │   │   │   ├── foundation.min.js
   │   │   │   │   ├── jquery.js
   │   │   │   │   └── modernizr.js
   │   │   │   └── Screenshot.png
   │   │   ├── templates
   │   │   │   ├── analytics.html
   │   │   │   ├── archives.html
   │   │   │   ├── article.html
   │   │   │   ├── article_infos.html
   │   │   │   ├── article_infos_bottom.html
   │   │   │   ├── author.html
   │   │   │   ├── authors.html
   │   │   │   ├── base.html
   │   │   │   ├── categories.html
   │   │   │   ├── category.html
   │   │   │   ├── comments.html
   │   │   │   ├── disqus_script.html
   │   │   │   ├── github.html
   │   │   │   ├── index.html
   │   │   │   ├── page.html
   │   │   │   ├── pagination.html
   │   │   │   ├── piwik.html
   │   │   │   ├── tag.html
   │   │   │   ├── tags.html
   │   │   │   ├── translations.html
   │   │   │   └── twitter.html
   │   │   ├── License.txt
   │   │   ├── README.md
   │   │   └── Screenshot.png
   │   ├── pelican-sad.png
   │   └── README.rst
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

themes/Just-Read/license.md
---------------------------

.. literalinclude:: ../themes/Just-Read/license.md
   :language: markdown
   :caption: themes/Just-Read/license.md

themes/Just-Read/pelican.conf.py-sample.py
------------------------------------------

.. literalinclude:: ../themes/Just-Read/pelican.conf.py-sample.py
   :language: python
   :caption: themes/Just-Read/pelican.conf.py-sample.py

themes/Just-Read/readme.md
--------------------------

.. literalinclude:: ../themes/Just-Read/readme.md
   :language: markdown
   :caption: themes/Just-Read/readme.md

themes/Peli-Kiera/README.md
---------------------------

.. literalinclude:: ../themes/Peli-Kiera/README.md
   :language: markdown
   :caption: themes/Peli-Kiera/README.md

themes/README.rst
-----------------

.. literalinclude:: ../themes/README.rst
   :language: rst
   :caption: themes/README.rst

themes/SOB/README.md
--------------------

.. literalinclude:: ../themes/SOB/README.md
   :language: markdown
   :caption: themes/SOB/README.md

themes/SoMA/README.md
---------------------

.. literalinclude:: ../themes/SoMA/README.md
   :language: markdown
   :caption: themes/SoMA/README.md

themes/SoMA2/README.md
----------------------

.. literalinclude:: ../themes/SoMA2/README.md
   :language: markdown
   :caption: themes/SoMA2/README.md

themes/aboutwilson/README.md
----------------------------

.. literalinclude:: ../themes/aboutwilson/README.md
   :language: markdown
   :caption: themes/aboutwilson/README.md

themes/aboutwilson/static/html5.js
----------------------------------

.. literalinclude:: ../themes/aboutwilson/static/html5.js
   :language: javascript
   :caption: themes/aboutwilson/static/html5.js

themes/aboutwilson/static/js/bootstrap.js
-----------------------------------------

.. literalinclude:: ../themes/aboutwilson/static/js/bootstrap.js
   :language: javascript
   :caption: themes/aboutwilson/static/js/bootstrap.js

themes/aboutwilson/static/js/bootstrap.min.js
---------------------------------------------

.. literalinclude:: ../themes/aboutwilson/static/js/bootstrap.min.js
   :language: javascript
   :caption: themes/aboutwilson/static/js/bootstrap.min.js

themes/aboutwilson/static/js/jquery-1.11.0.min.js
-------------------------------------------------

.. literalinclude:: ../themes/aboutwilson/static/js/jquery-1.11.0.min.js
   :language: javascript
   :caption: themes/aboutwilson/static/js/jquery-1.11.0.min.js

themes/backdrop/README.md
-------------------------

.. literalinclude:: ../themes/backdrop/README.md
   :language: markdown
   :caption: themes/backdrop/README.md

themes/backdrop/static/js/app.js
--------------------------------

.. literalinclude:: ../themes/backdrop/static/js/app.js
   :language: javascript
   :caption: themes/backdrop/static/js/app.js

themes/backdrop/static/js/foundation.min.js
-------------------------------------------

.. literalinclude:: ../themes/backdrop/static/js/foundation.min.js
   :language: javascript
   :caption: themes/backdrop/static/js/foundation.min.js

themes/backdrop/static/js/jquery.min.js
---------------------------------------

.. literalinclude:: ../themes/backdrop/static/js/jquery.min.js
   :language: javascript
   :caption: themes/backdrop/static/js/jquery.min.js

themes/backdrop/static/js/modernizr.js
--------------------------------------

.. literalinclude:: ../themes/backdrop/static/js/modernizr.js
   :language: javascript
   :caption: themes/backdrop/static/js/modernizr.js

themes/basic/README.rst
-----------------------

.. literalinclude:: ../themes/basic/README.rst
   :language: rst
   :caption: themes/basic/README.rst

themes/bootlex/README.md
------------------------

.. literalinclude:: ../themes/bootlex/README.md
   :language: markdown
   :caption: themes/bootlex/README.md

themes/bootstrap/README.md
--------------------------

.. literalinclude:: ../themes/bootstrap/README.md
   :language: markdown
   :caption: themes/bootstrap/README.md

themes/bootstrap/static/html5.js
--------------------------------

.. literalinclude:: ../themes/bootstrap/static/html5.js
   :language: javascript
   :caption: themes/bootstrap/static/html5.js

themes/bootstrap2/README.rst
----------------------------

.. literalinclude:: ../themes/bootstrap2/README.rst
   :language: rst
   :caption: themes/bootstrap2/README.rst

themes/bootstrap2/static/js/autosidebar.js
------------------------------------------

.. literalinclude:: ../themes/bootstrap2/static/js/autosidebar.js
   :language: javascript
   :caption: themes/bootstrap2/static/js/autosidebar.js

themes/bootstrap2/static/js/bootstrap.min.js
--------------------------------------------

.. literalinclude:: ../themes/bootstrap2/static/js/bootstrap.min.js
   :language: javascript
   :caption: themes/bootstrap2/static/js/bootstrap.min.js

themes/bootstrap2/static/js/jquery-1.7.2.min.js
-----------------------------------------------

.. literalinclude:: ../themes/bootstrap2/static/js/jquery-1.7.2.min.js
   :language: javascript
   :caption: themes/bootstrap2/static/js/jquery-1.7.2.min.js

themes/bootstrap2-dark/README.md
--------------------------------

.. literalinclude:: ../themes/bootstrap2-dark/README.md
   :language: markdown
   :caption: themes/bootstrap2-dark/README.md

themes/bootstrap2-dark/static/js/autosidebar.js
-----------------------------------------------

.. literalinclude:: ../themes/bootstrap2-dark/static/js/autosidebar.js
   :language: javascript
   :caption: themes/bootstrap2-dark/static/js/autosidebar.js

themes/bootstrap2-dark/static/js/bootstrap.min.js
-------------------------------------------------

.. literalinclude:: ../themes/bootstrap2-dark/static/js/bootstrap.min.js
   :language: javascript
   :caption: themes/bootstrap2-dark/static/js/bootstrap.min.js

themes/bootstrap2-dark/static/js/jquery-1.7.2.min.js
----------------------------------------------------

.. literalinclude:: ../themes/bootstrap2-dark/static/js/jquery-1.7.2.min.js
   :language: javascript
   :caption: themes/bootstrap2-dark/static/js/jquery-1.7.2.min.js

themes/bricabrac/README.md
--------------------------

.. literalinclude:: ../themes/bricabrac/README.md
   :language: markdown
   :caption: themes/bricabrac/README.md

themes/bricks/README.md
-----------------------

.. literalinclude:: ../themes/bricks/README.md
   :language: markdown
   :caption: themes/bricks/README.md

themes/bricks/static/js/modernizr.js
------------------------------------

.. literalinclude:: ../themes/bricks/static/js/modernizr.js
   :language: javascript
   :caption: themes/bricks/static/js/modernizr.js

themes/brownstone/README.md
---------------------------

.. literalinclude:: ../themes/brownstone/README.md
   :language: markdown
   :caption: themes/brownstone/README.md

themes/built-texts/readme.md
----------------------------

.. literalinclude:: ../themes/built-texts/readme.md
   :language: markdown
   :caption: themes/built-texts/readme.md

themes/built-texts/static/html5.js
----------------------------------

.. literalinclude:: ../themes/built-texts/static/html5.js
   :language: javascript
   :caption: themes/built-texts/static/html5.js

themes/custom/__init__.py
-------------------------

.. literalinclude:: ../themes/custom/__init__.py
   :language: python
   :caption: themes/custom/__init__.py

themes/dev-random/README.md
---------------------------

.. literalinclude:: ../themes/dev-random/README.md
   :language: markdown
   :caption: themes/dev-random/README.md

themes/dev-random/static/js/html5shiv.js
----------------------------------------

.. literalinclude:: ../themes/dev-random/static/js/html5shiv.js
   :language: javascript
   :caption: themes/dev-random/static/js/html5shiv.js

themes/dev-random/static/js/microTags.js
----------------------------------------

.. literalinclude:: ../themes/dev-random/static/js/microTags.js
   :language: javascript
   :caption: themes/dev-random/static/js/microTags.js

themes/dev-random2/README.md
----------------------------

.. literalinclude:: ../themes/dev-random2/README.md
   :language: markdown
   :caption: themes/dev-random2/README.md

themes/dev-random2/static/js/html5shiv.js
-----------------------------------------

.. literalinclude:: ../themes/dev-random2/static/js/html5shiv.js
   :language: javascript
   :caption: themes/dev-random2/static/js/html5shiv.js

themes/dev-random2/static/js/microTags.js
-----------------------------------------

.. literalinclude:: ../themes/dev-random2/static/js/microTags.js
   :language: javascript
   :caption: themes/dev-random2/static/js/microTags.js

themes/dev-random2/static/js/microTags.min.js
---------------------------------------------

.. literalinclude:: ../themes/dev-random2/static/js/microTags.min.js
   :language: javascript
   :caption: themes/dev-random2/static/js/microTags.min.js

themes/foundation-default-colours/README.md
-------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/README.md
   :language: markdown
   :caption: themes/foundation-default-colours/README.md

themes/foundation-default-colours/static/js/foundation/foundation.abide.js
--------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.abide.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.abide.js

themes/foundation-default-colours/static/js/foundation/foundation.accordion.js
------------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.accordion.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.accordion.js

themes/foundation-default-colours/static/js/foundation/foundation.alert.js
--------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.alert.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.alert.js

themes/foundation-default-colours/static/js/foundation/foundation.clearing.js
-----------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.clearing.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.clearing.js

themes/foundation-default-colours/static/js/foundation/foundation.dropdown.js
-----------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.dropdown.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.dropdown.js

themes/foundation-default-colours/static/js/foundation/foundation.interchange.js
--------------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.interchange.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.interchange.js

themes/foundation-default-colours/static/js/foundation/foundation.joyride.js
----------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.joyride.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.joyride.js

themes/foundation-default-colours/static/js/foundation/foundation.js
--------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.js

themes/foundation-default-colours/static/js/foundation/foundation.magellan.js
-----------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.magellan.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.magellan.js

themes/foundation-default-colours/static/js/foundation/foundation.offcanvas.js
------------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.offcanvas.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.offcanvas.js

themes/foundation-default-colours/static/js/foundation/foundation.orbit.js
--------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.orbit.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.orbit.js

themes/foundation-default-colours/static/js/foundation/foundation.reveal.js
---------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.reveal.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.reveal.js

themes/foundation-default-colours/static/js/foundation/foundation.tab.js
------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.tab.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.tab.js

themes/foundation-default-colours/static/js/foundation/foundation.tooltip.js
----------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.tooltip.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.tooltip.js

themes/foundation-default-colours/static/js/foundation/foundation.topbar.js
---------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation/foundation.topbar.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation/foundation.topbar.js

themes/foundation-default-colours/static/js/foundation.min.js
-------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/foundation.min.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/foundation.min.js

themes/foundation-default-colours/static/js/jquery.js
-----------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/jquery.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/jquery.js

themes/foundation-default-colours/static/js/modernizr.js
--------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/modernizr.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/modernizr.js

themes/foundation-default-colours/static/js/vendor/custom.modernizr.js
----------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/custom.modernizr.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/custom.modernizr.js

themes/foundation-default-colours/static/js/vendor/fastclick.js
---------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/fastclick.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/fastclick.js

themes/foundation-default-colours/static/js/vendor/jquery.autocomplete.js
-------------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/jquery.autocomplete.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/jquery.autocomplete.js

themes/foundation-default-colours/static/js/vendor/jquery.cookie.js
-------------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/jquery.cookie.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/jquery.cookie.js

themes/foundation-default-colours/static/js/vendor/jquery.js
------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/jquery.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/jquery.js

themes/foundation-default-colours/static/js/vendor/modernizr.js
---------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/modernizr.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/modernizr.js

themes/foundation-default-colours/static/js/vendor/placeholder.js
-----------------------------------------------------------------

.. literalinclude:: ../themes/foundation-default-colours/static/js/vendor/placeholder.js
   :language: javascript
   :caption: themes/foundation-default-colours/static/js/vendor/placeholder.js

themes/graymill/README.md
-------------------------

.. literalinclude:: ../themes/graymill/README.md
   :language: markdown
   :caption: themes/graymill/README.md

themes/graymill/sample_pelicanconf.py
-------------------------------------

.. literalinclude:: ../themes/graymill/sample_pelicanconf.py
   :language: python
   :caption: themes/graymill/sample_pelicanconf.py

themes/gum/README.md
--------------------

.. literalinclude:: ../themes/gum/README.md
   :language: markdown
   :caption: themes/gum/README.md

themes/gum/static/js/libs/gumby.init.js
---------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/gumby.init.js
   :language: javascript
   :caption: themes/gum/static/js/libs/gumby.init.js

themes/gum/static/js/libs/gumby.js
----------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/gumby.js
   :language: javascript
   :caption: themes/gum/static/js/libs/gumby.js

themes/gum/static/js/libs/gumby.min.js
--------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/gumby.min.js
   :language: javascript
   :caption: themes/gum/static/js/libs/gumby.min.js

themes/gum/static/js/libs/jquery-1.9.1.min.js
---------------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/jquery-1.9.1.min.js
   :language: javascript
   :caption: themes/gum/static/js/libs/jquery-1.9.1.min.js

themes/gum/static/js/libs/jquery.mobile.custom.min.js
-----------------------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/jquery.mobile.custom.min.js
   :language: javascript
   :caption: themes/gum/static/js/libs/jquery.mobile.custom.min.js

themes/gum/static/js/libs/modernizr-2.6.2.min.js
------------------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/modernizr-2.6.2.min.js
   :language: javascript
   :caption: themes/gum/static/js/libs/modernizr-2.6.2.min.js

themes/gum/static/js/libs/ui/gumby.navbar.js
--------------------------------------------

.. literalinclude:: ../themes/gum/static/js/libs/ui/gumby.navbar.js
   :language: javascript
   :caption: themes/gum/static/js/libs/ui/gumby.navbar.js

themes/gum/static/js/plugins.js
-------------------------------

.. literalinclude:: ../themes/gum/static/js/plugins.js
   :language: javascript
   :caption: themes/gum/static/js/plugins.js

themes/lightweight/LISEZ-MOI.rst
--------------------------------

.. literalinclude:: ../themes/lightweight/LISEZ-MOI.rst
   :language: rst
   :caption: themes/lightweight/LISEZ-MOI.rst

themes/lightweight/README.md
----------------------------

.. literalinclude:: ../themes/lightweight/README.md
   :language: markdown
   :caption: themes/lightweight/README.md

themes/martyalchin/README.md
----------------------------

.. literalinclude:: ../themes/martyalchin/README.md
   :language: markdown
   :caption: themes/martyalchin/README.md

themes/medio/README.md
----------------------

.. literalinclude:: ../themes/medio/README.md
   :language: markdown
   :caption: themes/medio/README.md

themes/medio/example_pelicanconf.py
-----------------------------------

.. literalinclude:: ../themes/medio/example_pelicanconf.py
   :language: python
   :caption: themes/medio/example_pelicanconf.py

themes/mnmlist/README.rst
-------------------------

.. literalinclude:: ../themes/mnmlist/README.rst
   :language: rst
   :caption: themes/mnmlist/README.rst

themes/monospace/README.md
--------------------------

.. literalinclude:: ../themes/monospace/README.md
   :language: markdown
   :caption: themes/monospace/README.md

themes/new-bootstrap2/README.rst
--------------------------------

.. literalinclude:: ../themes/new-bootstrap2/README.rst
   :language: rst
   :caption: themes/new-bootstrap2/README.rst

themes/new-bootstrap2/static/js/autosidebar.js
----------------------------------------------

.. literalinclude:: ../themes/new-bootstrap2/static/js/autosidebar.js
   :language: javascript
   :caption: themes/new-bootstrap2/static/js/autosidebar.js

themes/new-bootstrap2/static/js/bootstrap.min.js
------------------------------------------------

.. literalinclude:: ../themes/new-bootstrap2/static/js/bootstrap.min.js
   :language: javascript
   :caption: themes/new-bootstrap2/static/js/bootstrap.min.js

themes/new-bootstrap2/static/js/jquery-1.7.2.min.js
---------------------------------------------------

.. literalinclude:: ../themes/new-bootstrap2/static/js/jquery-1.7.2.min.js
   :language: javascript
   :caption: themes/new-bootstrap2/static/js/jquery-1.7.2.min.js

themes/nmnlist/README.rst
-------------------------

.. literalinclude:: ../themes/nmnlist/README.rst
   :language: rst
   :caption: themes/nmnlist/README.rst

themes/notebook/README.md
-------------------------

.. literalinclude:: ../themes/notebook/README.md
   :language: markdown
   :caption: themes/notebook/README.md

themes/notmyidea-cms/README.md
------------------------------

.. literalinclude:: ../themes/notmyidea-cms/README.md
   :language: markdown
   :caption: themes/notmyidea-cms/README.md

themes/notmyidea-cms-fr/README.md
---------------------------------

.. literalinclude:: ../themes/notmyidea-cms-fr/README.md
   :language: markdown
   :caption: themes/notmyidea-cms-fr/README.md

themes/ops/README.md
--------------------

.. literalinclude:: ../themes/ops/README.md
   :language: markdown
   :caption: themes/ops/README.md

themes/ops/static/js/jquery.min.js
----------------------------------

.. literalinclude:: ../themes/ops/static/js/jquery.min.js
   :language: javascript
   :caption: themes/ops/static/js/jquery.min.js

themes/ops/static/js/run_prettify.js
------------------------------------

.. literalinclude:: ../themes/ops/static/js/run_prettify.js
   :language: javascript
   :caption: themes/ops/static/js/run_prettify.js

themes/ops/static/js/site.js
----------------------------

.. literalinclude:: ../themes/ops/static/js/site.js
   :language: javascript
   :caption: themes/ops/static/js/site.js

themes/pelican-bootstrap3/AUTHORS.md
------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/AUTHORS.md
   :language: markdown
   :caption: themes/pelican-bootstrap3/AUTHORS.md

themes/pelican-bootstrap3/CONTRIBUTING.md
-----------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/CONTRIBUTING.md
   :language: markdown
   :caption: themes/pelican-bootstrap3/CONTRIBUTING.md

themes/pelican-bootstrap3/EXAMPLES.md
-------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/EXAMPLES.md
   :language: markdown
   :caption: themes/pelican-bootstrap3/EXAMPLES.md

themes/pelican-bootstrap3/README.md
-----------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/README.md
   :language: markdown
   :caption: themes/pelican-bootstrap3/README.md

themes/pelican-bootstrap3/static/js/bodypadding.js
--------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/bodypadding.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/bodypadding.js

themes/pelican-bootstrap3/static/js/bootstrap.min.js
----------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/bootstrap.min.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/bootstrap.min.js

themes/pelican-bootstrap3/static/js/github.js
---------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/github.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/github.js

themes/pelican-bootstrap3/static/js/jXHR.js
-------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/jXHR.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/jXHR.js

themes/pelican-bootstrap3/static/js/jquery.min.js
-------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/jquery.min.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/jquery.min.js

themes/pelican-bootstrap3/static/js/respond.min.js
--------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/respond.min.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/respond.min.js

themes/pelican-bootstrap3/static/js/shariff.min.js
--------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/js/shariff.min.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/js/shariff.min.js

themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.js
-----------------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.js

themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.min.js
---------------------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.min.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/tipuesearch/tipuesearch.min.js

themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_content.js
-------------------------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_content.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_content.js

themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_set.js
---------------------------------------------------------------

.. literalinclude:: ../themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_set.js
   :language: javascript
   :caption: themes/pelican-bootstrap3/static/tipuesearch/tipuesearch_set.js

themes/pelican-striped-html5up/README.md
----------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/README.md
   :language: markdown
   :caption: themes/pelican-striped-html5up/README.md

themes/pelican-striped-html5up/pelicanconf.py.py-sample.py
----------------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/pelicanconf.py.py-sample.py
   :language: python
   :caption: themes/pelican-striped-html5up/pelicanconf.py.py-sample.py

themes/pelican-striped-html5up/static/js/ie/html5shiv.js
--------------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/ie/html5shiv.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/ie/html5shiv.js

themes/pelican-striped-html5up/static/js/ie/respond.min.js
----------------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/ie/respond.min.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/ie/respond.min.js

themes/pelican-striped-html5up/static/js/jquery.min.js
------------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/jquery.min.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/jquery.min.js

themes/pelican-striped-html5up/static/js/main.js
------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/main.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/main.js

themes/pelican-striped-html5up/static/js/skel.min.js
----------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/skel.min.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/skel.min.js

themes/pelican-striped-html5up/static/js/util.js
------------------------------------------------

.. literalinclude:: ../themes/pelican-striped-html5up/static/js/util.js
   :language: javascript
   :caption: themes/pelican-striped-html5up/static/js/util.js

themes/photowall/readme.md
--------------------------

.. literalinclude:: ../themes/photowall/readme.md
   :language: markdown
   :caption: themes/photowall/readme.md

themes/photowall/static/js/mousetrap.js
---------------------------------------

.. literalinclude:: ../themes/photowall/static/js/mousetrap.js
   :language: javascript
   :caption: themes/photowall/static/js/mousetrap.js

themes/simple-bootstrap/readme.md
---------------------------------

.. literalinclude:: ../themes/simple-bootstrap/readme.md
   :language: markdown
   :caption: themes/simple-bootstrap/readme.md

themes/sneakyidea/README.rst
----------------------------

.. literalinclude:: ../themes/sneakyidea/README.rst
   :language: rst
   :caption: themes/sneakyidea/README.rst

themes/subtle/README.md
-----------------------

.. literalinclude:: ../themes/subtle/README.md
   :language: markdown
   :caption: themes/subtle/README.md

themes/syte/README.md
---------------------

.. literalinclude:: ../themes/syte/README.md
   :language: markdown
   :caption: themes/syte/README.md

themes/syte/static/js/common.js
-------------------------------

.. literalinclude:: ../themes/syte/static/js/common.js
   :language: javascript
   :caption: themes/syte/static/js/common.js

themes/syte/static/js/libs/bootstrap-modal.js
---------------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/bootstrap-modal.js
   :language: javascript
   :caption: themes/syte/static/js/libs/bootstrap-modal.js

themes/syte/static/js/libs/github.js
------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/github.js
   :language: javascript
   :caption: themes/syte/static/js/libs/github.js

themes/syte/static/js/libs/google+.js
-------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/google+.js
   :language: javascript
   :caption: themes/syte/static/js/libs/google+.js

themes/syte/static/js/libs/handlebars.js
----------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/handlebars.js
   :language: javascript
   :caption: themes/syte/static/js/libs/handlebars.js

themes/syte/static/js/libs/instagram.js
---------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/instagram.js
   :language: javascript
   :caption: themes/syte/static/js/libs/instagram.js

themes/syte/static/js/libs/jquery-1.7.2.min.js
----------------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/jquery-1.7.2.min.js
   :language: javascript
   :caption: themes/syte/static/js/libs/jquery-1.7.2.min.js

themes/syte/static/js/libs/jquery.url.js
----------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/jquery.url.js
   :language: javascript
   :caption: themes/syte/static/js/libs/jquery.url.js

themes/syte/static/js/libs/json.js
----------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/json.js
   :language: javascript
   :caption: themes/syte/static/js/libs/json.js

themes/syte/static/js/libs/moment.min.js
----------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/moment.min.js
   :language: javascript
   :caption: themes/syte/static/js/libs/moment.min.js

themes/syte/static/js/libs/prettify.js
--------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/prettify.js
   :language: javascript
   :caption: themes/syte/static/js/libs/prettify.js

themes/syte/static/js/libs/require.js
-------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/require.js
   :language: javascript
   :caption: themes/syte/static/js/libs/require.js

themes/syte/static/js/libs/spin.min.js
--------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/spin.min.js
   :language: javascript
   :caption: themes/syte/static/js/libs/spin.min.js

themes/syte/static/js/libs/text.js
----------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/text.js
   :language: javascript
   :caption: themes/syte/static/js/libs/text.js

themes/syte/static/js/libs/twitter.js
-------------------------------------

.. literalinclude:: ../themes/syte/static/js/libs/twitter.js
   :language: javascript
   :caption: themes/syte/static/js/libs/twitter.js

themes/tuxlite_tbs/README.md
----------------------------

.. literalinclude:: ../themes/tuxlite_tbs/README.md
   :language: markdown
   :caption: themes/tuxlite_tbs/README.md

themes/tuxlite_tbs/static/bootstrap-collapse.js
-----------------------------------------------

.. literalinclude:: ../themes/tuxlite_tbs/static/bootstrap-collapse.js
   :language: javascript
   :caption: themes/tuxlite_tbs/static/bootstrap-collapse.js

themes/tuxlite_tbs/static/html5.js
----------------------------------

.. literalinclude:: ../themes/tuxlite_tbs/static/html5.js
   :language: javascript
   :caption: themes/tuxlite_tbs/static/html5.js

themes/tuxlite_zf/README.md
---------------------------

.. literalinclude:: ../themes/tuxlite_zf/README.md
   :language: markdown
   :caption: themes/tuxlite_zf/README.md

themes/tuxlite_zf/static/js/custom.modernizr.js
-----------------------------------------------

.. literalinclude:: ../themes/tuxlite_zf/static/js/custom.modernizr.js
   :language: javascript
   :caption: themes/tuxlite_zf/static/js/custom.modernizr.js

themes/tuxlite_zf/static/js/foundation.min.js
---------------------------------------------

.. literalinclude:: ../themes/tuxlite_zf/static/js/foundation.min.js
   :language: javascript
   :caption: themes/tuxlite_zf/static/js/foundation.min.js

themes/tuxlite_zf/static/js/jquery.js
-------------------------------------

.. literalinclude:: ../themes/tuxlite_zf/static/js/jquery.js
   :language: javascript
   :caption: themes/tuxlite_zf/static/js/jquery.js

themes/tuxlite_zf/static/js/zepto.js
------------------------------------

.. literalinclude:: ../themes/tuxlite_zf/static/js/zepto.js
   :language: javascript
   :caption: themes/tuxlite_zf/static/js/zepto.js

themes/uikit/README.md
----------------------

.. literalinclude:: ../themes/uikit/README.md
   :language: markdown
   :caption: themes/uikit/README.md

themes/uikit/static/ico/favicon/manifest.json
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/ico/favicon/manifest.json
   :language: json
   :caption: themes/uikit/static/ico/favicon/manifest.json

themes/uikit/static/js/components/accordion.js
----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/accordion.js
   :language: javascript
   :caption: themes/uikit/static/js/components/accordion.js

themes/uikit/static/js/components/accordion.min.js
--------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/accordion.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/accordion.min.js

themes/uikit/static/js/components/autocomplete.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/autocomplete.js
   :language: javascript
   :caption: themes/uikit/static/js/components/autocomplete.js

themes/uikit/static/js/components/autocomplete.min.js
-----------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/autocomplete.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/autocomplete.min.js

themes/uikit/static/js/components/datepicker.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/datepicker.js
   :language: javascript
   :caption: themes/uikit/static/js/components/datepicker.js

themes/uikit/static/js/components/datepicker.min.js
---------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/datepicker.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/datepicker.min.js

themes/uikit/static/js/components/form-password.js
--------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/form-password.js
   :language: javascript
   :caption: themes/uikit/static/js/components/form-password.js

themes/uikit/static/js/components/form-password.min.js
------------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/form-password.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/form-password.min.js

themes/uikit/static/js/components/form-select.js
------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/form-select.js
   :language: javascript
   :caption: themes/uikit/static/js/components/form-select.js

themes/uikit/static/js/components/form-select.min.js
----------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/form-select.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/form-select.min.js

themes/uikit/static/js/components/grid.js
-----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/grid.js
   :language: javascript
   :caption: themes/uikit/static/js/components/grid.js

themes/uikit/static/js/components/grid.min.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/grid.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/grid.min.js

themes/uikit/static/js/components/htmleditor.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/htmleditor.js
   :language: javascript
   :caption: themes/uikit/static/js/components/htmleditor.js

themes/uikit/static/js/components/htmleditor.min.js
---------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/htmleditor.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/htmleditor.min.js

themes/uikit/static/js/components/lightbox.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/lightbox.js
   :language: javascript
   :caption: themes/uikit/static/js/components/lightbox.js

themes/uikit/static/js/components/lightbox.min.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/lightbox.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/lightbox.min.js

themes/uikit/static/js/components/nestable.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/nestable.js
   :language: javascript
   :caption: themes/uikit/static/js/components/nestable.js

themes/uikit/static/js/components/nestable.min.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/nestable.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/nestable.min.js

themes/uikit/static/js/components/notify.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/notify.js
   :language: javascript
   :caption: themes/uikit/static/js/components/notify.js

themes/uikit/static/js/components/notify.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/notify.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/notify.min.js

themes/uikit/static/js/components/pagination.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/pagination.js
   :language: javascript
   :caption: themes/uikit/static/js/components/pagination.js

themes/uikit/static/js/components/pagination.min.js
---------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/pagination.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/pagination.min.js

themes/uikit/static/js/components/parallax.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/parallax.js
   :language: javascript
   :caption: themes/uikit/static/js/components/parallax.js

themes/uikit/static/js/components/parallax.min.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/parallax.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/parallax.min.js

themes/uikit/static/js/components/search.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/search.js
   :language: javascript
   :caption: themes/uikit/static/js/components/search.js

themes/uikit/static/js/components/search.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/search.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/search.min.js

themes/uikit/static/js/components/slider.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slider.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slider.js

themes/uikit/static/js/components/slider.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slider.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slider.min.js

themes/uikit/static/js/components/slideset.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideset.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideset.js

themes/uikit/static/js/components/slideset.min.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideset.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideset.min.js

themes/uikit/static/js/components/slideshow-fx.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideshow-fx.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideshow-fx.js

themes/uikit/static/js/components/slideshow-fx.min.js
-----------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideshow-fx.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideshow-fx.min.js

themes/uikit/static/js/components/slideshow.js
----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideshow.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideshow.js

themes/uikit/static/js/components/slideshow.min.js
--------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/slideshow.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/slideshow.min.js

themes/uikit/static/js/components/sortable.js
---------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/sortable.js
   :language: javascript
   :caption: themes/uikit/static/js/components/sortable.js

themes/uikit/static/js/components/sortable.min.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/sortable.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/sortable.min.js

themes/uikit/static/js/components/sticky.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/sticky.js
   :language: javascript
   :caption: themes/uikit/static/js/components/sticky.js

themes/uikit/static/js/components/sticky.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/sticky.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/sticky.min.js

themes/uikit/static/js/components/timepicker.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/timepicker.js
   :language: javascript
   :caption: themes/uikit/static/js/components/timepicker.js

themes/uikit/static/js/components/timepicker.min.js
---------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/timepicker.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/timepicker.min.js

themes/uikit/static/js/components/tooltip.js
--------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/tooltip.js
   :language: javascript
   :caption: themes/uikit/static/js/components/tooltip.js

themes/uikit/static/js/components/tooltip.min.js
------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/tooltip.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/tooltip.min.js

themes/uikit/static/js/components/upload.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/upload.js
   :language: javascript
   :caption: themes/uikit/static/js/components/upload.js

themes/uikit/static/js/components/upload.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/components/upload.min.js
   :language: javascript
   :caption: themes/uikit/static/js/components/upload.min.js

themes/uikit/static/js/core/alert.js
------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/alert.js
   :language: javascript
   :caption: themes/uikit/static/js/core/alert.js

themes/uikit/static/js/core/alert.min.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/alert.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/alert.min.js

themes/uikit/static/js/core/button.js
-------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/button.js
   :language: javascript
   :caption: themes/uikit/static/js/core/button.js

themes/uikit/static/js/core/button.min.js
-----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/button.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/button.min.js

themes/uikit/static/js/core/core.js
-----------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/core.js
   :language: javascript
   :caption: themes/uikit/static/js/core/core.js

themes/uikit/static/js/core/core.min.js
---------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/core.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/core.min.js

themes/uikit/static/js/core/cover.js
------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/cover.js
   :language: javascript
   :caption: themes/uikit/static/js/core/cover.js

themes/uikit/static/js/core/cover.min.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/cover.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/cover.min.js

themes/uikit/static/js/core/dropdown.js
---------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/dropdown.js
   :language: javascript
   :caption: themes/uikit/static/js/core/dropdown.js

themes/uikit/static/js/core/dropdown.min.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/dropdown.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/dropdown.min.js

themes/uikit/static/js/core/grid.js
-----------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/grid.js
   :language: javascript
   :caption: themes/uikit/static/js/core/grid.js

themes/uikit/static/js/core/grid.min.js
---------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/grid.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/grid.min.js

themes/uikit/static/js/core/modal.js
------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/modal.js
   :language: javascript
   :caption: themes/uikit/static/js/core/modal.js

themes/uikit/static/js/core/modal.min.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/modal.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/modal.min.js

themes/uikit/static/js/core/nav.js
----------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/nav.js
   :language: javascript
   :caption: themes/uikit/static/js/core/nav.js

themes/uikit/static/js/core/nav.min.js
--------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/nav.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/nav.min.js

themes/uikit/static/js/core/offcanvas.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/offcanvas.js
   :language: javascript
   :caption: themes/uikit/static/js/core/offcanvas.js

themes/uikit/static/js/core/offcanvas.min.js
--------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/offcanvas.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/offcanvas.min.js

themes/uikit/static/js/core/scrollspy.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/scrollspy.js
   :language: javascript
   :caption: themes/uikit/static/js/core/scrollspy.js

themes/uikit/static/js/core/scrollspy.min.js
--------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/scrollspy.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/scrollspy.min.js

themes/uikit/static/js/core/smooth-scroll.js
--------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/smooth-scroll.js
   :language: javascript
   :caption: themes/uikit/static/js/core/smooth-scroll.js

themes/uikit/static/js/core/smooth-scroll.min.js
------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/smooth-scroll.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/smooth-scroll.min.js

themes/uikit/static/js/core/switcher.js
---------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/switcher.js
   :language: javascript
   :caption: themes/uikit/static/js/core/switcher.js

themes/uikit/static/js/core/switcher.min.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/switcher.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/switcher.min.js

themes/uikit/static/js/core/tab.js
----------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/tab.js
   :language: javascript
   :caption: themes/uikit/static/js/core/tab.js

themes/uikit/static/js/core/tab.min.js
--------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/tab.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/tab.min.js

themes/uikit/static/js/core/toggle.js
-------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/toggle.js
   :language: javascript
   :caption: themes/uikit/static/js/core/toggle.js

themes/uikit/static/js/core/toggle.min.js
-----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/toggle.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/toggle.min.js

themes/uikit/static/js/core/touch.js
------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/touch.js
   :language: javascript
   :caption: themes/uikit/static/js/core/touch.js

themes/uikit/static/js/core/touch.min.js
----------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/touch.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/touch.min.js

themes/uikit/static/js/core/utility.js
--------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/utility.js
   :language: javascript
   :caption: themes/uikit/static/js/core/utility.js

themes/uikit/static/js/core/utility.min.js
------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/core/utility.min.js
   :language: javascript
   :caption: themes/uikit/static/js/core/utility.min.js

themes/uikit/static/js/lib/MathJax.js
-------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/MathJax.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/MathJax.js

themes/uikit/static/js/lib/extensions/MathEvents.js
---------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/extensions/MathEvents.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/extensions/MathEvents.js

themes/uikit/static/js/lib/extensions/MathMenu.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/extensions/MathMenu.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/extensions/MathMenu.js

themes/uikit/static/js/lib/extensions/MathZoom.js
-------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/extensions/MathZoom.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/extensions/MathZoom.js

themes/uikit/static/js/lib/extensions/mml2jax.js
------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/extensions/mml2jax.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/extensions/mml2jax.js

themes/uikit/static/js/lib/extensions/tex2jax.js
------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/extensions/tex2jax.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/extensions/tex2jax.js

themes/uikit/static/js/lib/jax/input/MathML/config.js
-----------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/jax/input/MathML/config.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/jax/input/MathML/config.js

themes/uikit/static/js/lib/jax/input/TeX/config.js
--------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/jax/input/TeX/config.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/jax/input/TeX/config.js

themes/uikit/static/js/lib/jax/output/HTML-CSS/config.js
--------------------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/jax/output/HTML-CSS/config.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/jax/output/HTML-CSS/config.js

themes/uikit/static/js/lib/jquery-1.11.3.js
-------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/jquery-1.11.3.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/jquery-1.11.3.js

themes/uikit/static/js/lib/jquery-1.11.3.min.js
-----------------------------------------------

.. literalinclude:: ../themes/uikit/static/js/lib/jquery-1.11.3.min.js
   :language: javascript
   :caption: themes/uikit/static/js/lib/jquery-1.11.3.min.js

themes/uikit/static/js/uikit.js
-------------------------------

.. literalinclude:: ../themes/uikit/static/js/uikit.js
   :language: javascript
   :caption: themes/uikit/static/js/uikit.js

themes/uikit/static/js/uikit.min.js
-----------------------------------

.. literalinclude:: ../themes/uikit/static/js/uikit.min.js
   :language: javascript
   :caption: themes/uikit/static/js/uikit.min.js

themes/waterspill/README.md
---------------------------

.. literalinclude:: ../themes/waterspill/README.md
   :language: markdown
   :caption: themes/waterspill/README.md

themes/waterspill-en/README.md
------------------------------

.. literalinclude:: ../themes/waterspill-en/README.md
   :language: markdown
   :caption: themes/waterspill-en/README.md

themes/waterspill-en/license.md
-------------------------------

.. literalinclude:: ../themes/waterspill-en/license.md
   :language: markdown
   :caption: themes/waterspill-en/license.md

themes/zurb-F5-basic/README.md
------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/README.md
   :language: markdown
   :caption: themes/zurb-F5-basic/README.md

themes/zurb-F5-basic/static/js/foundation/foundation.abide.js
-------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.abide.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.abide.js

themes/zurb-F5-basic/static/js/foundation/foundation.accordion.js
-----------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.accordion.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.accordion.js

themes/zurb-F5-basic/static/js/foundation/foundation.alert.js
-------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.alert.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.alert.js

themes/zurb-F5-basic/static/js/foundation/foundation.clearing.js
----------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.clearing.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.clearing.js

themes/zurb-F5-basic/static/js/foundation/foundation.dropdown.js
----------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.dropdown.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.dropdown.js

themes/zurb-F5-basic/static/js/foundation/foundation.interchange.js
-------------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.interchange.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.interchange.js

themes/zurb-F5-basic/static/js/foundation/foundation.joyride.js
---------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.joyride.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.joyride.js

themes/zurb-F5-basic/static/js/foundation/foundation.js
-------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.js

themes/zurb-F5-basic/static/js/foundation/foundation.magellan.js
----------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.magellan.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.magellan.js

themes/zurb-F5-basic/static/js/foundation/foundation.offcanvas.js
-----------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.offcanvas.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.offcanvas.js

themes/zurb-F5-basic/static/js/foundation/foundation.orbit.js
-------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.orbit.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.orbit.js

themes/zurb-F5-basic/static/js/foundation/foundation.reveal.js
--------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.reveal.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.reveal.js

themes/zurb-F5-basic/static/js/foundation/foundation.tab.js
-----------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.tab.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.tab.js

themes/zurb-F5-basic/static/js/foundation/foundation.tooltip.js
---------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.tooltip.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.tooltip.js

themes/zurb-F5-basic/static/js/foundation/foundation.topbar.js
--------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation/foundation.topbar.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation/foundation.topbar.js

themes/zurb-F5-basic/static/js/foundation.min.js
------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/foundation.min.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/foundation.min.js

themes/zurb-F5-basic/static/js/jquery.js
----------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/jquery.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/jquery.js

themes/zurb-F5-basic/static/js/modernizr.js
-------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/modernizr.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/modernizr.js

themes/zurb-F5-basic/static/js/vendor/custom.modernizr.js
---------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/custom.modernizr.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/custom.modernizr.js

themes/zurb-F5-basic/static/js/vendor/fastclick.js
--------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/fastclick.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/fastclick.js

themes/zurb-F5-basic/static/js/vendor/jquery.autocomplete.js
------------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/jquery.autocomplete.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/jquery.autocomplete.js

themes/zurb-F5-basic/static/js/vendor/jquery.cookie.js
------------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/jquery.cookie.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/jquery.cookie.js

themes/zurb-F5-basic/static/js/vendor/jquery.js
-----------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/jquery.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/jquery.js

themes/zurb-F5-basic/static/js/vendor/placeholder.js
----------------------------------------------------

.. literalinclude:: ../themes/zurb-F5-basic/static/js/vendor/placeholder.js
   :language: javascript
   :caption: themes/zurb-F5-basic/static/js/vendor/placeholder.js
