from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import defaultdict
import enum
from enum import IntEnum
import fnmatch as fnmatch
import io as io
import multiprocessing as multiprocessing
import omni as omni
from omni.kit.test.code_change_analyzer import CodeChangeAnalyzer
from omni.kit.test.crash_process import crash_process
from omni.kit.test.flaky import FlakyTestAnalyzer
from omni.kit.test.repo_test_context import RepoTestContext
from omni.kit.test.reporter import TestReporter
from omni.kit.test.sampling import SamplingFactor
from omni.kit.test.teamcity import is_running_in_teamcity
from omni.kit.test.teamcity import teamcity_message
from omni.kit.test.teamcity import teamcity_test_retry_support
from omni.kit.test.test_coverage import read_coverage_collector_settings
from omni.kit.test.test_reporters import TestRunStatus
from omni.kit.test.test_reporters import _test_status_report
from omni.kit.test.utils import Colors
from omni.kit.test.utils import TestReturnCode
from omni.kit.test.utils import clamp
from omni.kit.test.utils import cleanup_folder
from omni.kit.test.utils import ext_id_to_fullname
from omni.kit.test.utils import get_argv
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import get_local_timestamp
from omni.kit.test.utils import get_setting
from omni.kit.test.utils import get_unprocessed_argv
from omni.kit.test.utils import is_etm_run
from omni.kit.test.utils import is_running_on_ci
from omni.kit.test.utils import resolve_path
import os as os
import pprint as pprint
import psutil as psutil
import random as random
import re as re
import subprocess as subprocess
import sys as sys
import time as time
import typing
__all__ = ['BEGIN_SEPARATOR', 'CodeChangeAnalyzer', 'Colors', 'DEFAULT_TEST_NAME', 'END_SEPARATOR', 'ExtTest', 'ExtTestResult', 'FLAKY_TESTS_QUERY_DAYS', 'FailPatterns', 'FlakyTestAnalyzer', 'IntEnum', 'KEY_FAILING_TESTS', 'PRAGMA_REGEX', 'RepoTestContext', 'RetryStrategy', 'RunExtTests', 'STARTED_UNITTEST', 'STARTUP_ONLY_TEST_MARKER', 'SamplingContext', 'SamplingFactor', 'TestApp', 'TestReporter', 'TestReturnCode', 'TestRunContext', 'TestRunStatus', 'asyncio', 'carb', 'clamp', 'cleanup_folder', 'crash_process', 'defaultdict', 'escape_for_fnmatch', 'ext_id_to_fullname', 'fnmatch', 'gather_with_concurrency', 'get_argv', 'get_global_test_output_path', 'get_local_timestamp', 'get_registry_extensions', 'get_setting', 'get_unprocessed_argv', 'io', 'is_etm_run', 'is_matching_list', 'is_running_in_teamcity', 'is_running_on_ci', 'kill_process_recursive', 'match', 'matched_patterns', 'multiprocessing', 'omni', 'os', 'pprint', 'psutil', 'random', 're', 'read_coverage_collector_settings', 'resolve_path', 'run_ext_tests', 'run_serial_and_parallel_tasks', 'subprocess', 'sys', 'teamcity_message', 'teamcity_test_retry_support', 'time', 'unescape_fnmatch']
class ExtTest:
    def __init__(self, ext_id: str, ext_info: carb.dictionary.Item, test_config: dict, test_id: str, is_parallel_run: bool, run_context: TestRunContext, test_app: TestApp, valid = True):
        ...
    def _fill_ext_test(self):
        ...
    def _pre_test_run(self, test_run: int, retry_strategy: str):
        """
        Update arguments that must change between each test run
        """
    def _use_tests_sampling(self) -> bool:
        ...
    def get_cmd(self) -> str:
        ...
    def on_fail(self, fail_message):
        ...
    def on_finish(self, test_result: bool):
        ...
    def on_start(self):
        ...
class ExtTestResult:
    def __init__(self):
        ...
class FailPatterns:
    def __init__(self, include = list(), exclude = list()):
        ...
    def __str__(self):
        ...
    def match_line(self, line: str) -> tuple[str, str, bool]:
        ...
    def merge(self, patterns: FailPatterns):
        ...
class RetryStrategy:
    ITERATIONS: typing.ClassVar[str] = 'iterations'
    NO_RETRY: typing.ClassVar[str] = 'no-retry'
    RERUN_UNTIL_FAILURE: typing.ClassVar[str] = 'rerun-until-failure'
    RETRY_ON_FAILURE: typing.ClassVar[str] = 'retry-on-failure'
    RETRY_ON_FAILURE_CI_ONLY: typing.ClassVar[str] = 'retry-on-failure-ci-only'
class RunExtTests(enum.IntEnum):
    """
    An enumeration.
    """
    BOTH: typing.ClassVar[RunExtTests]  # value = <RunExtTests.BOTH: 2>
    RELIABLE_ONLY: typing.ClassVar[RunExtTests]  # value = <RunExtTests.RELIABLE_ONLY: 0>
    UNRELIABLE_ONLY: typing.ClassVar[RunExtTests]  # value = <RunExtTests.UNRELIABLE_ONLY: 1>
class SamplingContext:
    ANY: typing.ClassVar[str] = 'any'
    CI: typing.ClassVar[str] = 'ci'
    LOCAL: typing.ClassVar[str] = 'local'
class TestApp:
    def __init__(self, stream):
        ...
class TestRunContext:
    def __init__(self):
        ...
def _build_exts_set(exts: list[str], exclude: list[str], use_registry: bool, match_version_as_string: bool) -> list[str]:
    ...
def _build_test_id(test_type: str, ext: str, app: str = '', test_name: str = '') -> str:
    ...
def _debug(stream, msg):
    ...
def _error(stream, msg):
    ...
def _extract_metadata_pragma(line, metadata):
    """
    
        Test subprocs can print specially formatted pragmas, that get picked up here as extra fields
        that get printed into the status report. Pragmas must be at the start of the line, and should
        be the only thing on that line.
    
        Format:
        ##omni.kit.test[op, key, value]
          op = operation type, either "set", "append" or "del" (str)
          key = name of the key (str)
          value = string value (str)
    
        Examples:
            # set a value
            ##omni.kit.test[set, foo, this is a message and spaces are allowed]
    
            # append a value to a list
            ##omni.kit.test[append, bah, test-13]
        
    """
def _format_cmdline(cmdline: str) -> str:
    """
    Format commandline printed from CI so that we can run it locally
    """
def _get_test_cmdline(ext_name: str, failed_tests: list = list()) -> list:
    """
    Return an example cmdline to run extension tests or a single unittest
    """
def _get_test_configs_for_ext(ext_info, name_filter = None) -> list[dict]:
    ...
def _parse_arg_shortcut(argv, arg_name):
    ...
def _prepare_app_for_testing(stream) -> tuple[str | None, str]:
    """
    Returns path to app (kit file) and short name of an app.
    """
def _prepare_ext_for_testing(ext_name, stream = ...):
    ...
def _propagate_args(argv, arg_name, has_value = False, starts_with = False):
    ...
def _run_ext_test(run_context: TestRunContext, test: ExtTest, on_status_report_fn):
    ...
def _run_ext_test_once(test: ExtTest, on_status_report_fn, is_last_try: bool, retry_failed_tests: bool):
    ...
def _run_ext_tests(exts, on_status_report_fn, exclude_exts, only_list = False) -> bool:
    ...
def _run_test_process(test: ExtTest) -> tuple[int, list[str], dict]:
    """
    Run test process and read stdout (use PIPE).
    """
def _warning(stream, msg):
    ...
def escape_for_fnmatch(s: str) -> str:
    ...
def gather_with_concurrency(n, *tasks):
    ...
def get_registry_extensions(max_attempts: int, delay: float, backoff_factor: float):
    ...
def is_matching_list(ext_id, ext_name, ext_list):
    ...
def kill_process_recursive(pid, stream):
    ...
def match(s: str, patterns: list[str]) -> bool:
    ...
def matched_patterns(s: str, patterns: list[str]) -> list[str]:
    ...
def run_ext_tests(test_exts, on_finish_fn = None, on_status_report_fn = None, exclude_exts = list()):
    ...
def run_serial_and_parallel_tasks(parallel_tasks, serial_tasks, max_parallel_tasks: int):
    ...
def unescape_fnmatch(s: str) -> str:
    ...
BEGIN_SEPARATOR: str = '\n||||||||||||||||||||||||||||||  [EXTENSION TEST START: {0}]  ||||||||||||||||||||||||||||||\n'
DEFAULT_TEST_NAME: str = 'default'
END_SEPARATOR: str = '\n{2}||||||||||||||||||||||||||||||  [EXTENSION TEST {0}: {1}]  ||||||||||||||||||||||||||||||{3}\n'
FLAKY_TESTS_QUERY_DAYS: int = 30
KEY_FAILING_TESTS: str = 'Failing tests'
PRAGMA_REGEX: re.Pattern  # value = re.compile('^##omni\\.kit\\.test\\[(.*)\\]')
STARTED_UNITTEST: str = 'started '
STARTUP_ONLY_TEST_MARKER: str = '_startup_only_test'
_debug_log: bool = False
