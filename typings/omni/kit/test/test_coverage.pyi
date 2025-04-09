from __future__ import annotations
import carb as carb
import coverage as coverage
from datetime import datetime
from functools import lru_cache
import omni as omni
from omni.kit.test.teamcity import teamcity_publish_artifact
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import get_setting
import os as os
import pathlib
from pathlib import Path
import shutil as shutil
__all__ = ['COV_OUTPUT_DATAFILE_EXTENSION', 'COV_OUTPUT_DATAFILE_PREFIX', 'CURRENT_PATH', 'HTML_LOCAL_PATH', 'Path', 'PyCoverageReporterResult', 'PyCoverageReporterSettings', 'carb', 'coverage', 'datetime', 'generate_coverage_report', 'get_global_test_output_path', 'get_setting', 'lru_cache', 'omni', 'os', 'read_coverage_collector_settings', 'read_coverage_reporter_settings', 'report_coverage_results', 'shutil', 'teamcity_publish_artifact']
class PyCoverageReporterResult:
    def __init__(self):
        ...
class PyCoverageReporterSettings:
    def __init__(self):
        ...
class _PyCoverageCollector:
    """
    Initializes code coverage collections and saves collected data at Python interpreter exit
    """
    class PyCoverageSettings:
        def __init__(self):
            ...
    def __init__(self):
        ...
    def _read_collector_settings(self) -> typing.Optional[omni.kit.test.test_coverage._PyCoverageCollector.PyCoverageSettings]:
        """
        
                Reads coverage settings and returns non None PyCoverageSettings if Python coverage is required
                
        """
    def shutdown(self, _ = None):
        ...
    def startup(self):
        ...
class _PyCoverageCollectorSettings:
    def __init__(self):
        ...
def _get_coverage_enabled() -> bool:
    """
    Return true if coverage is enabled, false otherwise
    """
def _get_coverage_env_var(*args, **kwargs):
    """
    Provide env var to globally enable/disable coverage, return true/false or None if not set
    """
def _get_coverage_output_dir(*args, **kwargs):
    ...
def _modify_html_report(output_path: str):
    ...
def _report_single_coverage_result(cov, src_path: str, std_output: bool = True, json_output_file: typing.Optional[str] = None, title: typing.Optional[str] = None, html_output_path: typing.Optional[str] = None):
    """
    
        Creates single report and returns path for created json file (or None if it wasn't created)
        
    """
def generate_coverage_report() -> PyCoverageReporterResult:
    ...
def read_coverage_collector_settings() -> _PyCoverageCollectorSettings:
    ...
def read_coverage_reporter_settings() -> typing.Optional[omni.kit.test.test_coverage.PyCoverageReporterSettings]:
    ...
def report_coverage_results(reporter_settings: typing.Optional[omni.kit.test.test_coverage.PyCoverageReporterSettings] = None) -> PyCoverageReporterResult:
    """
    
        Processes previously collected coverage data according to settings in the 'reporter_settings'
        
    """
COV_OUTPUT_DATAFILE_EXTENSION: str = '.pycov'
COV_OUTPUT_DATAFILE_PREFIX: str = 'py_cov'
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.test-1.1.2+d02c707b.lx64.r.cp310/omni/kit/test')
HTML_LOCAL_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.test-1.1.2+d02c707b.lx64.r.cp310/html/coverage')
