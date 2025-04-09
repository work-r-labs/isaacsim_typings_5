from __future__ import annotations
import carb as carb
import collections
from collections import defaultdict
import datetime as datetime
import logging as logging
from omni.kit.test.nvdf import get_app_info
from omni.kit.test.nvdf import query_nvdf
from omni.kit.test.utils import get_test_output_path
import os as os
import typing
__all__ = ['FLAKY_TESTS_QUERY_DAYS', 'FlakyTestAnalyzer', 'carb', 'datetime', 'defaultdict', 'get_app_info', 'get_test_output_path', 'logger', 'logging', 'os', 'query_nvdf']
class FlakyTestAnalyzer:
    """
    Basic Flaky Tests Analyzer
    """
    AGG_LAST_EXT_CONFIG: typing.ClassVar[str] = 'config'
    AGG_TEST_IDS: typing.ClassVar[str] = 'ids'
    BUCKET_FAILED: typing.ClassVar[str] = 'failed'
    BUCKET_PASSED: typing.ClassVar[str] = 'passed'
    ext_failed: typing.ClassVar[collections.defaultdict]  # value = defaultdict(<class 'list'>, {})
    tests_failed: typing.ClassVar[set] = set()
    def __init__(self, ext_test_id: str = '*', query_days = 30, exclude_consecutive_failure: bool = True):
        ...
    def _es_query(self, days: int, hours: int) -> dict:
        ...
    def _query_nvdf(self) -> bool:
        ...
    def _write_playlist(self, filepath: str) -> bool:
        ...
    def generate_playlist(self) -> str:
        ...
    def get_flaky_tests(self, ext_id: str) -> list:
        ...
    def should_skip_test(self) -> bool:
        ...
FLAKY_TESTS_QUERY_DAYS: int = 30
logger: logging.Logger  # value = <Logger omni.kit.test.flaky (DEBUG)>
