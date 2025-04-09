"""
Async version of python unittest module.

AsyncTestCase, AsyncTestSuite and AsyncTextTestRunner classes were copied from python unittest source and async/await
keywords were added.

There are two ways of registering tests, which must all be in the 'tests' submodule of your python module.

    1. 'from X import *" from every file containing tests
    2. Add the line 'scan_for_test_modules = True' in your __init__.py file to pick up tests in every file starting
       with 'test_'
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.test.reporter import TestReporter
from omni.kit.test.test_reporters import TestRunStatus
from omni.kit.test.utils import Colors
from omni.kit.test.utils import get_ext_test_id
from omni.kit.test.utils import is_running_on_ci
import time as time
import typing
import unittest as unittest
from unittest.case import _Outcome
import warnings as warnings
__all__ = ['AsyncTestCase', 'AsyncTestCaseFailOnLogError', 'AsyncTestSuite', 'AsyncTextTestRunner', 'Colors', 'KEY_FAILING_TESTS', 'LogErrorChecker', 'OmniTestResult', 'STARTED_UNITTEST', 'TeamcityTestResult', 'TestReporter', 'TestRunStatus', 'asyncio', 'await_or_call', 'carb', 'get_ext_test_id', 'is_running_on_ci', 'omni', 'time', 'unittest', 'warnings']
class AsyncTestCase(unittest.case.TestCase):
    """
    Base class for all async test cases.
    
        Derive from it to make your tests auto discoverable. Test methods must start with `test_` prefix.
    
        Test cases allow for generation and/or adaptation of tests at runtime. See testing_exts_python.md for more details.
        
    """
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    fail_on_log_error: typing.ClassVar[bool] = False
    def assertEqualWithRetry(self, operation: typing.Callable[[], typing.Any], expected: typing.Any, wait_frames: int = 2, max_retries: int = 50):
        """
        Like assertEqual except it retries `operation` until it returns an equivalent value to `expected`
                or the retry limit is reached.
        
                Parameters:
                * operation: a function that takes no arguments and returns a value.
                * expected: the expected value.
                * wait_frames: the number of frames to wait after a failed call of `operation`.
                * max_retries: the maximum number of retries.
        
                The function will keep calling `operation` until the returned value equals to `expected`.
                If the maximum number of retries is reached, make a failed assertion to show the last returned
                value and the expected value.
        
                Please use this function to wrap your operation and minimize waiting time instead of using
                `wait_n_updates()` directly.
                
        """
    def assertTrueWithRetry(self, operation: typing.Callable[[], typing.Any], wait_frames: int = 2, max_retries: int = 50):
        """
        Like assertTrue except it retries `operation` until it returns a truthy value or the retry limit is reached.
        
                Parameters:
                * operation: a function that takes no arguments and returns a value.
                * wait_frames: the number of frames to wait after a failed call of `operation`.
                * max_retries: the maximum number of retries.
        
                The function will keep calling `operation` until it returns a truthy value
                (e.g., True, non-empty collection, and non-zero number).
                If the maximum number of retries is reached, make a failed assertion to stop the test.
        
                Please use this function to wrap your operation and minimize waiting time instead of using
                `wait_n_updates()` directly.
                
        """
    def retry_until_success(self, operation: typing.Callable[[], typing.Any], wait_frames: int = 2, max_retries: int = 50) -> typing.Any:
        """
        Retry the operation until it returns a truthy value or exceeds the max retries.
        
                Parameters:
                * operation: a function that takes no arguments and returns a value.
                * wait_frames: the number of frames to wait after a failed call of `operation`.
                * max_retries: the maximum number of retries.
        
                Return:
                The first truthy value returned by `operation`.
        
                The function will keep calling `operation` until it returns a truthy value
                (e.g., True, non-empty collection, and non-zero number).
                If the maximum number of retries is reached, make a failed assertion to stop the test.
        
                Please use this function to wrap your operation and minimize waiting time instead of using
                `wait_n_updates()` directly.
                
        """
    def run(self, result = None):
        ...
    def wait_n_updates(self, n_frames: int = 3):
        ...
class AsyncTestCaseFailOnLogError(AsyncTestCase):
    """
    Test Case which automatically subscribes to logging events and fails if any error were produced during the test.
    
        This class is for backward compatibility, you can also just change value of `fail_on_log_error`.
        
    """
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    fail_on_log_error: typing.ClassVar[bool] = True
class AsyncTestSuite(unittest.suite.TestSuite):
    """
    A test suite is a composite test consisting of a number of TestCases.
    
        For use, create an instance of TestSuite, then add test case instances.
        When all tests have been added, the suite can be passed to a test
        runner, such as TextTestRunner. It will run the individual test cases
        in the order in which they were added, aggregating the results. When
        subclassing, do not forget to call the base class constructor.
        
    """
    def run(self, result, debug = False):
        ...
class AsyncTextTestRunner(unittest.runner.TextTestRunner):
    """
    A test runner class that displays results in textual form.
    
        It prints out the names of tests as they are run, errors as they
        occur, and a summary of the results at the end of the test run.
        
    """
    def run(self, test, on_status_report_fn = None):
        """
        Run the given test case or test suite.
        """
class LogErrorChecker:
    """
    Automatically subscribes to logging events and monitors if error were produced during the test.
    """
    def __init__(self):
        ...
    def get_error_count(self):
        ...
    def shutdown(self):
        ...
class OmniTestResult(unittest.runner.TextTestResult):
    @staticmethod
    def get_tc_test_id(test):
        ...
    def __init__(self, stream, descriptions, verbosity):
        ...
    def _get_error_message(self, test, fail_type: str, errors: list) -> str:
        ...
    def _report_status(self, *args, **kwargs):
        ...
    def addError(self, test, err, *k):
        ...
    def addFailure(self, test, err, *k):
        ...
    def addSuccess(self, test):
        ...
    def printErrorList(self, flavour, errors):
        ...
    def report_fail(self, test, fail_type: str, err, fail_message: str):
        ...
    def startTest(self, test):
        ...
    def stopTest(self, test):
        ...
class TeamcityTestResult(OmniTestResult):
    def __init__(self, stream, descriptions, verbosity):
        ...
def _isnotsuite(test):
    """
    A crude way to tell apart testcases and suites with duck-typing
    """
def await_or_call(func):
    """
    
        Awaits on function if it is a coroutine, calls it otherwise.
        
    """
KEY_FAILING_TESTS: str = 'Failing tests'
STARTED_UNITTEST: str = 'started '
