from .fetch_data import fetch_data, fetch_data_cli
from .build_search_index import build_search_index, build_search_index_cli

__title__ = "gistblog"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2026 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "build_search_index",
    "build_search_index_cli",
    "fetch_data",
    "fetch_data_cli",
)
