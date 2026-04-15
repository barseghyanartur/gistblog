import json
import os
import pytest
from unittest.mock import MagicMock


class MockResponse:
    def __init__(self, data, text=""):
        self._data = data
        self._text = text

    def json(self):
        return self._data

    def raise_for_status(self):
        pass

    @property
    def text(self):
        return self._text


@pytest.fixture
def gist_api_response():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    with open(os.path.join(data_dir, "response.json")) as f:
        return json.load(f)


def test_import():
    from gistblog.fetch_data import _fetch_gists

    assert callable(_fetch_gists)


def test_mock_response():
    r = MockResponse([])
    assert r.json() == []
    r2 = MockResponse([{"id": "x"}])
    assert r2.json() == [{"id": "x"}]


def test_mock_call():
    client = MagicMock()
    client.get.return_value = MockResponse([])
    client.headers = {}

    result = client.get("url")
    assert result.json() == []


def test_fetch_gists_with_empty():
    from gistblog.fetch_data import _fetch_gists

    client = MagicMock()

    def mock_get(url, params=None):
        return MockResponse([])

    client.get = mock_get
    client.headers = {}

    result = _fetch_gists(client)
    assert result == 0


def test_fetch_gists_skips_non_blog():
    from gistblog.fetch_data import _fetch_gists

    client = MagicMock()

    def mock_get(url, params=None):
        page = params.get("page", 1) if params else 1
        if page == 1:
            return MockResponse(
                [{"id": "notablog123", "description": "not a blog gist", "files": {}}]
            )
        return MockResponse([])

    client.get = mock_get
    client.headers = {}

    result = _fetch_gists(client)
    assert result == 0


def test_fetch_gists_syncs_blog_gists(gist_api_response):
    from gistblog.fetch_data import _fetch_gists

    client = MagicMock()

    def mock_get(url, params=None):
        page = params.get("page", 1) if params else 1
        if "users/barseghyanartur/gists" in str(url):
            if page == 1:
                return MockResponse(gist_api_response)
            return MockResponse([])
        return MockResponse([])

    client.get = mock_get
    client.headers = {}

    result = _fetch_gists(client)
    assert result == 2
