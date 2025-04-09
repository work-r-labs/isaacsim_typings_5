from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.omni_test_registry.omni_test_registry import omni_test_registry
from omni.kit.test.async_unittest import AsyncTestCase
from omni.kit.test.async_unittest import AsyncTestCaseFailOnLogError
from omni.kit.test.async_unittest import AsyncTestSuite
from omni.kit.test.benchmark import BenchmarkTestCase
from omni.kit.test.exttests import ExtTest
from omni.kit.test.exttests import ExtTestResult
from omni.kit.test.exttests import run_ext_tests
from omni.kit.test.reporter import generate_report
from omni.kit.test.test_coverage import _PyCoverageCollector
from omni.kit.test.test_populators import TestPopulateAll
from omni.kit.test.test_populators import TestPopulateDisabled
from omni.kit.test.test_populators import TestPopulator
from omni.kit.test.test_reporters import TestRunStatus
from omni.kit.test.test_reporters import add_test_status_report_cb
from omni.kit.test.unittests import add_test_case_to_tested_extension
from omni.kit.test.unittests import get_tests
from omni.kit.test.unittests import get_tests_from_modules
from omni.kit.test.unittests import run_tests
from omni.kit.test.utils import TestReturnCode
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import get_setting
from omni.kit.test.utils import get_test_output_path
from omni.kit.test.utils import is_etm_run
from . import async_unittest
from . import benchmark
from . import code_change_analyzer
from . import crash_process
from . import ext_utils
from . import exttests
from . import flaky
from . import gitlab
from . import nvdf
from . import repo_test_context
from . import reporter
from . import sampling
from . import teamcity
from . import test_coverage
from . import test_populators
from . import test_reporters
from . import unittests
from . import utils
__all__: list = ['AsyncTestCase', 'AsyncTestCaseFailOnLogError', 'AsyncTestSuite', 'BenchmarkTestCase', 'DEFAULT_POPULATOR_NAME', 'ExtTest', 'ExtTestResult', 'TestPopulateAll', 'TestPopulateDisabled', 'TestPopulator', 'TestReturnCode', 'TestRunStatus', 'add_test_status_report_cb', 'add_test_case_to_tested_extension', 'decompose_test_list', 'get_global_test_output_path', 'get_setting', 'get_test_output_path', 'get_tests', 'get_tests_from_modules', 'is_etm_run', 'run_tests']
class _TestAutoRunner(omni.ext._extensions.IExt):
    """
    Automatically run tests based on setting
    """
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
def _auto_run_tests(run_tests_and_exit: bool):
    ...
DEFAULT_POPULATOR_NAME: str = 'All Tests'
