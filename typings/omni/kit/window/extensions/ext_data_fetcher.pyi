"""
This module provides a class for fetching, caching, and retrieving JSON data related to extension archives from online sources.
"""
from __future__ import annotations
import asyncio as asyncio
from functools import lru_cache
import json as json
import logging as logging
import omni as omni
from omni.kit.window.extensions.common import ExtensionCommonInfo
__all__: list = ['ExtDataFetcher']
class ExtDataFetcher:
    """
    Fetches json files near extension archives from the registry and caches them
    """
    def __init__(self):
        """
        Initializes the ExtDataFetcher with default properties.
        """
    def _build_json_data_urls(self, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo) -> typing.List[str]:
        ...
    def fetch(self, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Fetches and caches the data for the given extension item.
        
                Args:
                    ext_item (:obj:`ExtensionCommonInfo`): The extension item to fetch data for.
        """
    def get_ext_data(self, package_id) -> dict:
        """
        Retrieves the cached data for a given package ID.
        
                Args:
                    package_id (str): The unique identifier of the package.
        """
def get_ext_data_fetcher(*args, **kwargs):
    ...
logger: logging.Logger  # value = <Logger omni.kit.window.extensions.ext_data_fetcher (DEBUG)>
