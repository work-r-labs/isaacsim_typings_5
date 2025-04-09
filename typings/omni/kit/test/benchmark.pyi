from __future__ import annotations
import json as json
import omni as omni
from omni.kit.test.async_unittest import AsyncTestCase
from omni.kit.test.async_unittest import OmniTestResult
from omni.kit.test.reporter import TestReporter
from omni.kit.test.test_reporters import TestRunStatus
from omni.kit.test.utils import get_ext_test_id
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import get_setting
import os as os
import sys as sys
from time import perf_counter_ns
import typing
__all__ = ['AsyncTestCase', 'BenchmarkReporter', 'BenchmarkResult', 'BenchmarkTestCase', 'OmniTestResult', 'TestReporter', 'TestRunStatus', 'get_ext_test_id', 'get_global_test_output_path', 'get_setting', 'json', 'omni', 'os', 'perf_counter_ns', 'sys']
class BenchmarkReporter(omni.kit.test.reporter.TestReporter):
    """
    
        Benchmark reporter class to generate the JSON report for reggie.
        * Collects default metrics such as `duration`, `passed` and `skipped`.
        * Collects custom metrics from `BenchmarkTestCase`
        * Collects fingerprints that are passed by CLI arguments.
        * Detects platorm and config and sets it as fingerprint.
        
    """
    @staticmethod
    def _add_samples_from_benchmark(samples: dict, test):
        """
        
                Collect custom metric samples from `BenchmarkTestCase`.
                
        """
    @staticmethod
    def _collect_fingerprints():
        """
        
                Internal method to collect benchmark finger prints for reggie.
                Detects platform and config at runtime.
                Collects custom fingerprints from CLI and merges them with the detected ones.
                
        """
    @staticmethod
    def _get_benchmark_and_suite(test_id: str, ext_test_id: str) -> typing.Tuple[str, str]:
        """
        
                Generates slightly shorter benchmark and benchmark_suite names for reggie
                from the strings found in test_id and ext_test_id.
                They are for example used in reggie's HTML reports (drop-down list)
        
                Example:
                    input:
                    test_id = "example.python_ext.tests.test_benchmarks.TestBenchmarks.benchmark_sleepy_with_custom_metrics"
                    ext_test_id = "example.python_ex"
        
                    output:
                    benchmark = "TestBenchmarks.benchmark_sleepy_with_custom_metrics"
                    benchmark_suite = "tests.test_benchmarks"
                
        """
    def __init__(self, stream = ...):
        ...
    def _get_bm_duration_ns(self, test_id: str) -> int:
        ...
    def _write_bm_report(self, test_id, test, passed, skipped):
        """
        
                Generate the JSON report for reggie.
                
        """
    def benchmark_begin(self, test_id):
        ...
    def benchmark_end(self, test_id, test, passed = False, skipped = False, skip_reason = ''):
        ...
class BenchmarkResult(omni.kit.test.async_unittest.OmniTestResult):
    """
    
        Base class for benchmark results.
        
    """
    def __init__(self, stream, descriptions, verbosity):
        ...
    def testMethodBegin(self, test):
        ...
    def testMethodEnd(self, test):
        ...
class BenchmarkTestCase(omni.kit.test.async_unittest.AsyncTestCase):
    """
    
        Base class for benchmark tests.
        Benchmarks have to derive from this class to be able to set samples for custom metrics.
        
    """
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def __init__(self, tests = tuple(), methodName = 'runTest'):
        ...
    def _clear_metric_samples(self):
        """
        
                Cleanup metrics dict.
                Has to run before or after each benchmark run to ensure no leakage of metrics to another benchmark.
                
        """
    def _get_metric_samples_dict(self) -> dict:
        """
        
                Expose the custom metric samples. Used to generate the final reports.
                
        """
    def set_metric_sample(self, name: str, value: typing.Union[int, float, bool], unit: typing.Optional[str] = None):
        """
        
                Set a sample for a custom metric. Providing the unit is optional.
                
        """
    def set_metric_sample_array(self, name: str, values: typing.Union[typing.List[int], typing.List[float]], unit: typing.Optional[str] = None):
        """
        
                Set a sample array for a custom metric. Providing the unit is optional.
                
        """
