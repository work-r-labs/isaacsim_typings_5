from __future__ import annotations
import datetime as datetime
import logging as logging
from omni.kit.test.nvdf import get_app_info
from omni.kit.test.nvdf import query_nvdf
from omni.kit.test.utils import clamp
from omni.kit.test.utils import get_setting
from omni.kit.test.utils import is_running_on_ci
import random as random
from statistics import mean
import typing
__all__ = ['Sampling', 'SamplingFactor', 'clamp', 'datetime', 'get_app_info', 'get_setting', 'get_tests_sampling_to_skip', 'is_running_on_ci', 'logger', 'logging', 'mean', 'query_nvdf', 'random']
class Sampling:
    """
    Basic Tests Sampling support
    """
    AGG_LAST_PASSED: typing.ClassVar[str] = 'last_passed'
    AGG_TEST_IDS: typing.ClassVar[str] = 'test_ids'
    DAYS: typing.ClassVar[int] = 4
    LAST_PASSED_COUNT: typing.ClassVar[int] = 3
    TEST_IDS_COUNT: typing.ClassVar[int] = 1000
    def __init__(self, app_info: dict):
        ...
    def _calculate_weights(self) -> list:
        """
        Simple weight adjusting to make sure all tests run an equal amount of times
        """
    def _es_query(self, extension_name: str, days: int, hours: int) -> dict:
        ...
    def _query_nvdf(self, extension_name: str, unittests: list) -> bool:
        ...
    def _random_choices_no_replace(self, population, weights, k) -> list:
        """
        Similar to numpy.random.Generator.choice() with replace=False
        """
    def get_tests_to_skip(self, sampling_factor: float) -> list:
        ...
    def run_query(self, extension_name: str, unittests: list, running_on_ci: bool):
        ...
class SamplingFactor:
    LOWER_BOUND: typing.ClassVar[float] = 0.0
    MID_POINT: typing.ClassVar[float] = 0.5
    UPPER_BOUND: typing.ClassVar[float] = 1.0
def get_tests_sampling_to_skip(extension_name: str, sampling_factor: float, unittests: list) -> list:
    """
    Return a list of tests that can be skipped for a given extension based on a sampling factor
        When using tests sampling we have to run:
          1) all new tests (not found on nvdf)
          2) all failed tests (ie: only consecutive failures, flaky tests are not considered)
          3) sampling tests (sampling factor * number of tests)
        By applying (1 - sampling factor) we get a list of tests to skip, which are garanteed not to contain any test
        from point 1 or 2.
        
    """
logger: logging.Logger  # value = <Logger omni.kit.test.sampling (DEBUG)>
