import json
import os

import pytest


@pytest.fixture
def gist_api_response():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    with open(os.path.join(data_dir, "response.json")) as f:
        return json.load(f)


@pytest.fixture
def gist_content():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    with open(
        os.path.join(data_dir, "gist_content_0c7a06e9a87f01b0dc30d15a76a8f03e.rst")
    ) as f:
        return f.read()
