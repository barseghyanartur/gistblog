"""
tests/test_search.py

Test suite for the gist-blog search feature.

Run with:
    pytest tests/test_search.py -v
"""
import json
import os
import re
import tempfile
import textwrap
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Helpers – import the module under test from the project root
# ---------------------------------------------------------------------------

import sys
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))

from gistblog.build_search_index import (
    build_search_index,
    clean_rst_body,
    is_border,
    parse_rst_file,
    _pelican_slugify,
)


# ---------------------------------------------------------------------------
# is_border
# ---------------------------------------------------------------------------

class TestIsBorder:
    def test_equals_border(self):
        assert is_border("====") is True

    def test_dash_border(self):
        assert is_border("----") is True

    def test_tilde_border(self):
        assert is_border("~~~~") is True

    def test_too_short(self):
        assert is_border("=") is False

    def test_single_char(self):
        assert is_border("-") is False

    def test_plain_text(self):
        assert is_border("Hello world") is False

    def test_border_with_trailing_space(self):
        assert is_border("====  ") is True

    def test_mixed_chars_not_border(self):
        assert is_border("=-=") is False


# ---------------------------------------------------------------------------
# parse_rst_file – Style A (overline + title + underline)
# ---------------------------------------------------------------------------

RST_STYLE_A = textwrap.dedent("""\
    ================
    My Great Post
    ================
    :date: 2026-04-01 10:00
    :category: Tech
    :tags: python, testing
    :summary: A short summary.

    Body paragraph one.

    Body paragraph two.
""")

RST_STYLE_B = textwrap.dedent("""\
    My Other Post
    =============
    :date: 2025-09-01 09:00
    :category: Art
    :tags: sketch

    Body content here.
""")

RST_NO_METADATA = textwrap.dedent("""\
    Just a Title
    ============

    No metadata here, just prose.
""")


@pytest.fixture
def tmp_rst(tmp_path):
    """Write an RST string to a temp file and return its path."""
    def _write(content, name="test.rst"):
        p = tmp_path / name
        p.write_text(content, encoding="utf-8")
        return str(p)
    return _write


class TestParseRstFileStyleA:
    def test_title(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        title, meta, body = parse_rst_file(path)
        assert title == "My Great Post"

    def test_metadata_date(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        _, meta, _ = parse_rst_file(path)
        assert meta["date"] == "2026-04-01 10:00"

    def test_metadata_category(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        _, meta, _ = parse_rst_file(path)
        assert meta["category"] == "Tech"

    def test_metadata_tags(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        _, meta, _ = parse_rst_file(path)
        assert meta["tags"] == "python, testing"

    def test_metadata_summary(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        _, meta, _ = parse_rst_file(path)
        assert meta["summary"] == "A short summary."

    def test_body_not_empty(self, tmp_rst):
        path = tmp_rst(RST_STYLE_A)
        _, _, body = parse_rst_file(path)
        joined = " ".join(body)
        assert "Body paragraph one" in joined


class TestParseRstFileStyleB:
    def test_title(self, tmp_rst):
        path = tmp_rst(RST_STYLE_B)
        title, meta, body = parse_rst_file(path)
        assert title == "My Other Post"

    def test_metadata(self, tmp_rst):
        path = tmp_rst(RST_STYLE_B)
        _, meta, _ = parse_rst_file(path)
        assert meta["category"] == "Art"
        assert meta["tags"] == "sketch"

    def test_body(self, tmp_rst):
        path = tmp_rst(RST_STYLE_B)
        _, _, body = parse_rst_file(path)
        assert any("Body content here" in l for l in body)


class TestParseRstFileNoMetadata:
    def test_title(self, tmp_rst):
        path = tmp_rst(RST_NO_METADATA)
        title, meta, body = parse_rst_file(path)
        assert title == "Just a Title"

    def test_empty_metadata(self, tmp_rst):
        path = tmp_rst(RST_NO_METADATA)
        _, meta, _ = parse_rst_file(path)
        assert meta == {}

    def test_body_has_prose(self, tmp_rst):
        path = tmp_rst(RST_NO_METADATA)
        _, _, body = parse_rst_file(path)
        assert any("No metadata here" in l for l in body)


class TestParseRstFileEdgeCases:
    def test_leading_blank_lines_stripped(self, tmp_rst):
        content = "\n\n\n" + RST_STYLE_B
        path = tmp_rst(content)
        title, _, _ = parse_rst_file(path)
        assert title == "My Other Post"

    def test_empty_file(self, tmp_rst):
        path = tmp_rst("")
        title, meta, body = parse_rst_file(path)
        assert title == "Untitled"
        assert meta == {}

    def test_only_title_no_underline(self, tmp_rst):
        path = tmp_rst("Lonely Title\n")
        title, _, _ = parse_rst_file(path)
        assert title == "Lonely Title"


# ---------------------------------------------------------------------------
# clean_rst_body
# ---------------------------------------------------------------------------

class TestCleanRstBody:
    def test_strips_bold(self):
        result = clean_rst_body(["**bold text**"])
        assert result == "bold text"

    def test_strips_italic(self):
        result = clean_rst_body(["*italic text*"])
        assert result == "italic text"

    def test_strips_inline_code(self):
        result = clean_rst_body(["``code``"])
        assert result == "code"

    def test_strips_role(self):
        result = clean_rst_body([":py:func:`my_func`"])
        assert result == "my_func"

    def test_strips_hyperlink(self):
        result = clean_rst_body(["`Link text`_"])
        assert result == "Link text"

    def test_strips_bullet_marker(self):
        result = clean_rst_body(["- item one"])
        assert result == "item one"

    def test_strips_rst_directive(self):
        result = clean_rst_body([".. code-block:: python"])
        assert result == ""

    def test_skips_borders(self):
        result = clean_rst_body(["====", "Some text", "===="])
        assert result == "Some text"

    def test_skips_blank_lines(self):
        result = clean_rst_body(["", "  ", "hello"])
        assert result == "hello"

    def test_joins_multiple_lines(self):
        result = clean_rst_body(["line one", "line two"])
        assert result == "line one line two"

    def test_truncation_not_done_here(self):
        # clean_rst_body does NOT truncate; truncation is in build_search_index
        long_line = ["word"] * 300
        result = clean_rst_body(long_line)
        assert len(result) > 1000


# ---------------------------------------------------------------------------
# _pelican_slugify
# ---------------------------------------------------------------------------

class TestPelicanSlugify:
    @pytest.mark.parametrize("title,expected", [
        ("My Post", "my-post"),
        ("Hello World 2026", "hello-world-2026"),
        ("A small selection of photographs I took before 2012",
         "a-small-selection-of-photographs-i-took-before-2012"),
        ('Hide ``*.py,cover`` files from IDE', "hide-pycover-files-from-ide"),
        ("Safezip - zero-dependency wrapper for secure ZIP extraction",
         "safezip-zero-dependency-wrapper-for-secure-zip-extraction"),
    ])
    def test_known_titles(self, title, expected):
        assert _pelican_slugify(title) == expected

    def test_returns_string(self):
        assert isinstance(_pelican_slugify("anything"), str)

    def test_no_uppercase(self):
        assert _pelican_slugify("UPPER CASE") == _pelican_slugify("UPPER CASE").lower()


# ---------------------------------------------------------------------------
# build_search_index (integration)
# ---------------------------------------------------------------------------

SAMPLE_POST_A = textwrap.dedent("""\
    ==================
    Python Tips 2026
    ==================
    :date: 2026-03-15 08:00
    :category: Tech
    :tags: python, tips
    :summary: Handy Python tips for 2026.

    Here is the body of the Python tips post.
    It has multiple lines of useful content.
""")

SAMPLE_POST_B = textwrap.dedent("""\
    Art in Spring
    =============
    :date: 2026-04-01 12:00
    :category: Art
    :tags: art, spring

    Some artsy content here.
""")

SAMPLE_POST_WITH_SLUG = textwrap.dedent("""\
    Title That Would Slug Badly!!!
    ==============================
    :date: 2026-01-01 00:00
    :category: Tech
    :tags: test
    :slug: custom-slug-override

    Body text.
""")

SAMPLE_PAGE = textwrap.dedent("""\
    Search
    ======
    :date: 2026-01-01 00:00

    This is the search page.
""")


@pytest.fixture
def content_dir(tmp_path):
    """Create a temporary content/ + static/ directory pair."""
    cdir = tmp_path / "content"
    cdir.mkdir()
    sdir = tmp_path / "static"
    sdir.mkdir()
    return tmp_path


def run_build(tmp_path, posts: dict):
    """Write RST files and call build_search_index(), returning parsed JSON."""
    cdir = tmp_path / "content"
    for name, body in posts.items():
        (cdir / name).write_text(body, encoding="utf-8")

    old_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        build_search_index()
    finally:
        os.chdir(old_cwd)

    index_path = tmp_path / "static" / "search_index.json"
    return json.loads(index_path.read_text(encoding="utf-8"))


class TestBuildSearchIndex:
    def test_generates_index_file(self, content_dir):
        run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert (content_dir / "static" / "search_index.json").exists()

    def test_correct_number_of_posts(self, content_dir):
        data = run_build(content_dir, {
            "post_a.rst": SAMPLE_POST_A,
            "post_b.rst": SAMPLE_POST_B,
        })
        assert len(data) == 2

    def test_ignores_non_rst(self, content_dir):
        (content_dir / "content" / "readme.md").write_text("# hi")
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert len(data) == 1

    def test_ignores_dotfiles(self, content_dir):
        (content_dir / "content" / ".hidden.rst").write_text("Hidden\n=====\n")
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert len(data) == 1

    def test_title_present(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["title"] == "Python Tips 2026"

    def test_category_present(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["category"] == "Tech"

    def test_tags_are_list(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["tags"] == ["python", "tips"]

    def test_summary_present(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["summary"] == "Handy Python tips for 2026."

    def test_summary_empty_when_absent(self, content_dir):
        data = run_build(content_dir, {"post_b.rst": SAMPLE_POST_B})
        assert data[0]["summary"] == ""

    def test_date_format(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["date"] == "2026-03-15"

    def test_url_uses_pelican_slugify(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert data[0]["url"] == "posts/2026/03/python-tips-2026/"

    def test_url_uses_explicit_slug_metadata(self, content_dir):
        data = run_build(content_dir, {"post_c.rst": SAMPLE_POST_WITH_SLUG})
        assert data[0]["url"] == "posts/2026/01/custom-slug-override/"

    def test_content_is_string(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert isinstance(data[0]["content"], str)

    def test_content_truncated_at_1000(self, content_dir):
        long_body = "word " * 500
        long_post = SAMPLE_POST_A + long_body
        data = run_build(content_dir, {"post_long.rst": long_post})
        assert len(data[0]["content"]) <= 1003  # 1000 + "..."

    def test_content_includes_body_text(self, content_dir):
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        assert "Python tips post" in data[0]["content"]

    def test_pages_subdir_not_indexed(self, content_dir):
        """Files in content/pages/ must NOT appear in the index (flat scan only)."""
        pages_dir = content_dir / "content" / "pages"
        pages_dir.mkdir()
        (pages_dir / "search.rst").write_text(SAMPLE_PAGE, encoding="utf-8")
        data = run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        titles = [p["title"] for p in data]
        assert "Search" not in titles

    def test_creates_static_dir_if_missing(self, tmp_path):
        cdir = tmp_path / "content"
        cdir.mkdir()
        (cdir / "post.rst").write_text(SAMPLE_POST_A, encoding="utf-8")
        # No static/ dir yet
        old_cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            build_search_index()
        finally:
            os.chdir(old_cwd)
        assert (tmp_path / "static" / "search_index.json").exists()

    def test_empty_content_dir_produces_empty_index(self, content_dir):
        data = run_build(content_dir, {})
        assert data == []

    def test_json_is_valid(self, content_dir):
        run_build(content_dir, {"post_a.rst": SAMPLE_POST_A})
        raw = (content_dir / "static" / "search_index.json").read_text()
        parsed = json.loads(raw)
        assert isinstance(parsed, list)

    def test_unicode_content(self, content_dir):
        unicode_post = textwrap.dedent("""\
            Ünïcödë Pöst
            =============
            :date: 2026-06-01 00:00
            :category: Tech
            :tags: unicode

            Héllo wörld — café naïve.
        """)
        data = run_build(content_dir, {"unicode.rst": unicode_post})
        assert "Héllo" in data[0]["content"] or data[0]["title"] == "Ünïcödë Pöst"

    def test_missing_date_defaults_gracefully(self, content_dir):
        no_date = textwrap.dedent("""\
            No Date Post
            ============
            :category: Tech

            Body here.
        """)
        # Should not raise; date defaults to today
        data = run_build(content_dir, {"no_date.rst": no_date})
        assert data[0]["title"] == "No Date Post"
        assert re.match(r'\d{4}-\d{2}-\d{2}', data[0]["date"])


# ---------------------------------------------------------------------------
# search.html template – structural checks
# ---------------------------------------------------------------------------

class TestSearchTemplate:
    @pytest.fixture
    def template_path(self):
        # Look for the template relative to this test file
        candidates = [
            ROOT / "themes" / "custom" / "templates" / "search.html",
        ]
        for c in candidates:
            if c.exists():
                return c
        pytest.skip("search.html not found – run tests from the project root")

    def test_extends_base(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert 'extends "base.html"' in content, "Must extend base.html"

    def test_has_search_input(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert 'id="search-input"' in content, "Must have #search-input element"

    def test_has_search_results(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert 'id="search-results"' in content, "Must have #search-results element"

    def test_loads_lunr(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert "lunr" in content.lower(), "Must load Lunr.js"

    def test_fetches_search_index(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert "search_index.json" in content, "Must fetch search_index.json"

    def test_uses_siteurl_variable(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert "SITEURL" in content, "Must use {{ SITEURL }} for portability"

    def test_no_hardcoded_origin(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert "localhost" not in content, "Must not hardcode localhost"
        assert "github.io" not in content, "Must not hardcode github.io"

    def test_has_block_content(self, template_path):
        content = template_path.read_text(encoding="utf-8")
        assert "{% block content %}" in content


# ---------------------------------------------------------------------------
# pelicanconf.py – structural checks
# ---------------------------------------------------------------------------

class TestPelicanConf:
    @pytest.fixture
    def conf_path(self):
        p = ROOT / "pelicanconf.py"
        if not p.exists():
            pytest.skip("pelicanconf.py not found")
        return p

    def test_search_in_menuitems(self, conf_path):
        content = conf_path.read_text(encoding="utf-8")
        # Search must be present AND not commented out
        lines = content.splitlines()
        search_lines = [l for l in lines if "Search" in l and "MENUITEMS" not in l]
        active = [l for l in search_lines if not l.strip().startswith("#")]
        assert active, "Search must appear as an active (uncommented) MENUITEMS entry"

    def test_search_url_matches_direct_template(self, conf_path):
        content = conf_path.read_text(encoding="utf-8")
        # DIRECT_TEMPLATES has "search" → Pelican generates /search/
        # MENUITEMS must point to /search/, not /pages/search/
        assert '"/search/"' in content or "'/search/'" in content or "/search/" in content
        assert "pages/search" not in content or content.index("pages/search") < content.index("MENUITEMS")

    def test_direct_templates_has_search(self, conf_path):
        content = conf_path.read_text(encoding="utf-8")
        assert '"search"' in content or "'search'" in content

    def test_siteurl_from_env(self, conf_path):
        content = conf_path.read_text(encoding="utf-8")
        assert 'os.environ.get("SITEURL"' in content or "os.environ.get('SITEURL'" in content