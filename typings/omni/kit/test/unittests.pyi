from __future__ import annotations
import asyncio as asyncio
from builtins import module as ModuleType
import carb as carb
from contextlib import suppress
import fnmatch as fnmatch
from genericpath import isfile
from glob import glob
from importlib import import_module
from itertools import islice
import omni as omni
from omni.kit.test.async_unittest import AsyncTestCase
from omni.kit.test.async_unittest import AsyncTestSuite
from omni.kit.test.async_unittest import AsyncTextTestRunner
from omni.kit.test.async_unittest import OmniTestResult
from omni.kit.test.benchmark import BenchmarkResult
from omni.kit.test.exttests import RunExtTests
from omni.kit.test.reporter import TestReporter
from omni.kit.test.sampling import SamplingFactor
from omni.kit.test.sampling import get_tests_sampling_to_skip
from omni.kit.test.teamcity import teamcity_message
from omni.kit.test.test_reporters import _test_status_report
from omni.kit.test.utils import get_argv
from omni.kit.test.utils import get_ext_test_id
from omni.kit.test.utils import get_setting
from omni.kit.test.utils import get_test_output_path
import os as os
from posixpath import basename
from posixpath import dirname
from posixpath import join
from posixpath import splitext
import random as random
import sys as sys
import traceback as traceback
import unittest as unittest
__all__ = ['AsyncTestCase', 'AsyncTestSuite', 'AsyncTextTestRunner', 'BenchmarkResult', 'ModuleType', 'OmniTestResult', 'RunExtTests', 'SCANNED_TEST_MODULES', 'SamplingFactor', 'TestReporter', 'add_test_case_to_tested_extension', 'asyncio', 'basename', 'carb', 'dirname', 'dynamic_test_modules', 'fnmatch', 'get_argv', 'get_ext_test_id', 'get_setting', 'get_test_output_path', 'get_tests', 'get_tests_from_enabled_extensions', 'get_tests_from_modules', 'get_tests_sampling_to_skip', 'get_tests_to_remove_from_modules', 'glob', 'import_module', 'isfile', 'islice', 'join', 'omni', 'os', 'print_tests', 'random', 'remove_from_dynamic_test_cache', 'run_tests', 'run_tests_in_modules', 'splitext', 'suppress', 'sys', 'teamcity_message', 'traceback', 'unittest']
def _get_enabled_extension_modules(filter_fn: typing.Callable[[str], bool] = None):
    ...
def _get_tests_from_file(filepath: str) -> list:
    ...
def _get_tests_override(tests: list) -> list:
    """
    Apply some override/modifiers to get the proper list of tests in that order:
        1. Add/Remove unreliable tests depending on testExtRunUnreliableTests value
        2. Get list of failed tests if present (if enabled, used with retry-on-failure)
        3. Get list of tests from a file (if enabled, generated when running tests)
        4. Get list of tests from sampling (if enabled)
        5. Shuffle (random order) is applied last
        
    """
def _import_if_exist(module: str):
    ...
def _on_ext_disabled(ext_id, *_):
    """
    Callback executed when an extension has been disabled - scan for tests to remove
    """
def _setup_output_path(test_output_path: str):
    ...
def _write_tests_playlist(test_output_path: str, tests: list):
    ...
def add_test_case_to_tested_extension(test_case: omni.kit.test.async_unittest.AsyncTestCase, phony_submodule: str = ''):
    ...
def dynamic_test_modules(module_root: str, module_file: str) -> typing.List[module]:
    """
    Import all of the test modules and return a list of the imports so that automatic test recognition works
    
        The normal test recognition mechanism relies on knowing all of the file names at build time. This function is
        used to support automatic recognition of all test files in a certain directory at run time.
    
        Args:
            module_root: Name of the module for which tests are being imported, usually just __name__ of the caller
            module_file: File from which the import is happening, usually just __file__ of the caller
    
        Usage:
            In the directory containing your tests add this line to the __init__.py file (creating the file if necessary):
                scan_for_test_modules = True
            It will pick up any Python files names testXXX.py or TestXXX.py and scan them for tests when the extension
            is loaded.
    
        Important:
            The __init__.py file must be imported with the extension. If you have a .tests module or .ogn.tests module
            underneath your main module this will happen automatically for you.
    
        Returns:
            List of modules that were added, each pointing to a file in which tests are contained
        
    """
def get_tests(tests_filter = '') -> typing.List:
    """
    Default function to get all current tests.
    
        It gets tests from all enabled extensions, but also included include and exclude settings to filter them
    
        Args:
            tests_filter(str): Additional filter string to apply on list of tests.
    
        Returns:
            List of tests.
        
    """
def get_tests_from_enabled_extensions():
    ...
def get_tests_from_modules(modules, log = False):
    """
    Return the list of tests registered or dynamically discovered from the list of modules
    """
def get_tests_to_remove_from_modules(modules, log = False):
    """
    Return the list of tests to be removed when a module is unloaded.
        This includes all tests registered or dynamically discovered from the list of modules and their .tests or
        .ogn.tests submodules. Keeping this separate from get_tests_from_modules() allows the import of all three related
        modules, while preventing duplication of their tests when all extension module tests are requested.
    
        Args:
            modules: List of modules to
        
    """
def print_tests():
    ...
def remove_from_dynamic_test_cache(module_root):
    """
    Get the list of tests dynamically added to the given module directory (via "scan_for_test_modules")
    """
def run_tests(tests = None, on_finish_fn = None, on_status_report_fn = None):
    ...
def run_tests_in_modules(modules, on_finish_fn = None):
    ...
SCANNED_TEST_MODULES: dict = {}
_EXTENSION_DISABLED_HOOK = None
_LOG: bool = False
_extra_tests: list  # value = [<.tests.TestExtensionActionsAPI testMethod=test_extensions_api_md_is_uptodate>]
