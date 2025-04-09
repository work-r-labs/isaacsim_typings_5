from __future__ import annotations
import carb as carb
from collections import OrderedDict
from collections import defaultdict
import dataclasses
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import fnmatch as fnmatch
from functools import lru_cache
import glob as glob
import json as json
import omni as omni
from omni.kit.test.nvdf import post_coverage_to_nvdf
from omni.kit.test.nvdf import post_to_nvdf
from omni.kit.test.teamcity import is_running_in_teamcity
from omni.kit.test.teamcity import teamcity_message
from omni.kit.test.teamcity import teamcity_publish_artifact
from omni.kit.test.teamcity import teamcity_status
from omni.kit.test.test_coverage import generate_coverage_report
from omni.kit.test.utils import ext_id_to_fullname
from omni.kit.test.utils import get_ext_test_id
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import get_setting
from omni.kit.test.utils import get_test_output_path
from omni.kit.test.utils import is_running_on_ci
import os as os
import pathlib as pathlib
from pathlib import Path
import platform as platform
import psutil as psutil
import shutil as shutil
import sys as sys
import time as time
import typing
from xml.etree import ElementTree as ET
import xml.etree.ElementTree
__all__ = ['CURRENT_PATH', 'ET', 'Enum', 'ExtCoverage', 'HTML_PATH', 'OrderedDict', 'Path', 'REPORT_FILENAME', 'RESULTS_FILENAME', 'Stats', 'TestReporter', 'carb', 'dataclass', 'datetime', 'defaultdict', 'ext_id_to_fullname', 'fnmatch', 'generate_coverage_report', 'generate_report', 'get_ext_test_id', 'get_global_test_output_path', 'get_report_filepath', 'get_results_filepath', 'get_setting', 'get_test_output_path', 'glob', 'is_running_in_teamcity', 'is_running_on_ci', 'json', 'lru_cache', 'omni', 'os', 'pathlib', 'platform', 'post_coverage_to_nvdf', 'post_to_nvdf', 'psutil', 'shutil', 'sys', 'teamcity_message', 'teamcity_publish_artifact', 'teamcity_status', 'time']
class ExtCoverage:
    def __init__(self):
        ...
    def mean_cov(self):
        ...
    def sum_covered_lines(self):
        ...
    def sum_statements(self):
        ...
class Stats:
    """
    Stats(passed: int = 0, failure: int = 0, error: int = 0, skipped: int = 0)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'passed': Field(name='passed',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'failure': Field(name='failure',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'error': Field(name='error',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'skipped': Field(name='skipped',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('passed', 'failure', 'error', 'skipped')
    error: typing.ClassVar[int] = 0
    failure: typing.ClassVar[int] = 0
    passed: typing.ClassVar[int] = 0
    skipped: typing.ClassVar[int] = 0
    def __eq__(self, other):
        ...
    def __init__(self, passed: int = 0, failure: int = 0, error: int = 0, skipped: int = 0) -> None:
        ...
    def __repr__(self):
        ...
    def get_total(self):
        ...
class TestReporter:
    """
    Combines TC reports to stdout and JSON lines report to a file
    """
    def __init__(self, stream = ...):
        ...
    def _get_duration_ns(self, test_id: str) -> int:
        ...
    def _get_duration_s(self, test_id: str) -> float:
        ...
    def _is_unreliable(self, test_id):
        ...
    def _write_report(self, data: dict):
        ...
    def exttest_fail(self, test_id, tc_test_id, fail_type: str, fail_message: str):
        ...
    def exttest_start(self, test_id, tc_test_id, ext_id, ext_name, captureStandardOutput = 'false', report = True):
        ...
    def exttest_stop(self, test_id, tc_test_id, passed = False, skipped = False, report = True):
        ...
    def report_result(self, test):
        """
        Write tests results data we want to later show on the html report and in elastic
        """
    def set_output_path(self, output_path: str):
        ...
    def unittest_fail(self, test_id, tc_test_id, fail_type: str, fail_message: str, ext_test_id: str = ''):
        ...
    def unittest_start(self, test_id, tc_test_id, captureStandardOutput = 'false'):
        ...
    def unittest_stop(self, test_id, tc_test_id, passed = False, skipped = False, skip_reason = '', ext_test_id: str = ''):
        ...
def _build_ext_coverage(coverage_data: dict, ext_id_to_name: dict) -> typing.Dict[str, omni.kit.test.reporter.ExtCoverage]:
    ...
def _build_test_data_html(report_data):
    ...
def _calculate_durations(report_data: list):
    """
    
        Calculate startup time of each extension and time taken by each individual test
        We count the time between the extension start_time to the start_time of the first test
        
    """
def _generate_html_report(report_data, merged_results):
    ...
def _generate_report_internal():
    ...
def _get_coverage_for_nvdf(merged_results: dict, coverage_results: dict) -> dict:
    ...
def _get_extension_name(path: str, ext_id_to_name: dict):
    ...
def _get_tc_test_id(test_id):
    ...
def _kill_kit_processes():
    """
    Kill all Kit processes except self
    """
def _load_coverage_results(report_data, read_coverage = True) -> typing.Tuple[dict, dict]:
    ...
def _load_report_data(report_path):
    ...
def _post_build_status(report_data: list):
    ...
def _report_data_to_junit_report(report_data: list) -> xml.etree.ElementTree.Element:
    ...
def _report_unreliable_tests(report_data):
    ...
def _write_html_artifact(base_path: pathlib.Path, testcase: xml.etree.ElementTree.Element):
    ...
def _write_html_report(html, output_path):
    ...
def _write_junit_results(report_data: list):
    """
    Write a JUnit XML from our report data
    """
def generate_report():
    """
    After running tests this function will generate html report / post to nvdf / publish artifacts
    """
def get_report_filepath(*args, **kwargs):
    ...
def get_results_filepath(*args, **kwargs):
    ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.test-1.1.2+d02c707b.lx64.r.cp310/omni/kit/test')
HTML_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.test-1.1.2+d02c707b.lx64.r.cp310/html')
REPORT_FILENAME: str = 'report.jsonl'
RESULTS_FILENAME: str = 'results.xml'
