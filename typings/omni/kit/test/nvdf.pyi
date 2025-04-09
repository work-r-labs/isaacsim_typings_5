from __future__ import annotations
import carb as carb
from collections import defaultdict
from functools import lru_cache
import itertools as itertools
import json as json
import logging as logging
import omni as omni
from omni.kit.test.gitlab import get_gitlab_build_url
from omni.kit.test.gitlab import is_running_in_gitlab
from omni.kit.test.teamcity import get_teamcity_build_url
from omni.kit.test.teamcity import is_running_in_teamcity
from omni.kit.test.utils import call_git
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import is_running_on_ci
import os as os
from pathlib import Path
import re as re
import sys as sys
import time as time
import urllib as urllib
__all__ = ['Path', 'call_git', 'carb', 'defaultdict', 'get_app_info', 'get_gitlab_build_url', 'get_global_test_output_path', 'get_nvdf_report_filepath', 'get_teamcity_build_url', 'is_running_in_gitlab', 'is_running_in_teamcity', 'is_running_on_ci', 'itertools', 'json', 'logger', 'logging', 'lru_cache', 'omni', 'os', 'post_coverage_to_nvdf', 'post_to_nvdf', 'query_nvdf', 're', 'remove_nvdf_form', 'sys', 'time', 'to_nvdf_form', 'urllib']
def _can_post_to_nvdf() -> bool:
    ...
def _detect_kit_branch_and_mr(*args, **kwargs):
    ...
def _find_repository_info(*args, **kwargs):
    """
    Get repo remote origin url, fallback on yaml if not found
    """
def _get_ci_info(*args, **kwargs):
    ...
def _get_json_data(report_data: typing.List[typing.Dict[str, str]], app_info: dict, ci_info: dict) -> typing.Dict:
    """
    Transform report_data into json data
    
        Input:
        {"event": "start", "test_id": "omni.kit.viewport", "ext_name": "omni.kit.viewport", "start_time": 1664831914.002093}
        {"event": "stop", "test_id": "omni.kit.viewport", "ext_name": "omni.kit.viewport", "success": true, "skipped": false, "stop_time": 1664831927.1145973, "duration": 13.113}
        ...
    
        Output:
        {
            "omni.kit.viewport+omni.kit.viewport": {
                "app": { ... },
                "teamcity": { ... },
                "test": {
                    "b_success": false,
                    "d_duration": 1.185,
                    "s_ext_name": "omni.kit.viewport",
                    "s_name": "omni.kit.viewport",
                    "s_type": "exttest",
                    "ts_start_time": 1664893802530,
                    "ts_stop_time": 1664893803715
                    "result": { ... },
                },
            },
        }
        
    """
def _partition(pred, iterable):
    """
    Use a predicate to partition entries into false entries and true entries
    """
def _post_json(project: str, json_str: str):
    ...
def get_app_info(*args, **kwargs):
    """
    This should be part of omni.kit.app.
    
        Example response:
            {
                "app_name": "omni.app.full.kit",
                "app_version": "1.0.1",
                "kit_version_full": "103.1+release.10030.f5f9dcab.tc",
                "kit_version": "103.1",
                "kit_build_number": 10030,
                "branch": "master"
                "config": "release",
                "platform": "windows-x86_64",
                "python_version": "cp37"
            }
        
    """
def get_nvdf_report_filepath(*args, **kwargs):
    ...
def post_coverage_to_nvdf(coverage_data: typing.Dict[str, typing.Dict]):
    ...
def post_to_nvdf(report_data: typing.List[typing.Dict[str, str]]):
    ...
def query_nvdf(query: str) -> dict:
    ...
def remove_nvdf_form(data: dict):
    ...
def to_nvdf_form(data: dict) -> typing.Dict:
    """
    Convert dict to NVDF-compliant form.
        https://confluence.nvidia.com/display/nvdataflow/NVDataFlow#NVDataFlow-PostingPayload
        
    """
logger: logging.Logger  # value = <Logger omni.kit.test.nvdf (DEBUG)>
