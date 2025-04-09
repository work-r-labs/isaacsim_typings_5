from __future__ import annotations
import carb as carb
from datetime import datetime
from functools import lru_cache
import glob as glob
import hashlib as hashlib
import omni as omni
from omni.kit.test.gitlab import is_running_in_gitlab
from omni.kit.test.teamcity import is_running_in_teamcity
import os as os
from pathlib import Path
import shutil as shutil
import sys as sys
import typing
__all__ = ['Colors', 'Path', 'TestReturnCode', 'call_git', 'carb', 'clamp', 'cleanup_folder', 'datetime', 'ext_id_to_fullname', 'get_argv', 'get_ext_test_id', 'get_global_test_output_path', 'get_local_timestamp', 'get_setting', 'get_test_output_path', 'get_unprocessed_argv', 'glob', 'hash_file', 'hashlib', 'is_etm_run', 'is_running_in_gitlab', 'is_running_in_teamcity', 'is_running_on_ci', 'lru_cache', 'omni', 'os', 'resolve_path', 'sha1_list', 'sha1_path', 'shutil', 'sys']
class Colors:
    """
    ANSI colors to change TTY font color. Using the high intensity colors, they look nicer
    """
    BLUE: typing.ClassVar[str] = '\x1b[94m'
    GREEN: typing.ClassVar[str] = '\x1b[92m'
    RED: typing.ClassVar[str] = '\x1b[91m'
    RESET: typing.ClassVar[str] = '\x1b[0m'
    YELLOW: typing.ClassVar[str] = '\x1b[93m'
class TestReturnCode:
    """
    Return codes used by omni.kit.test
    """
    EXT_TESTS_FAILED: typing.ClassVar[int] = 21
    UNIT_TESTS_FAILED: typing.ClassVar[int] = 13
    UNIT_TEST_TIMEOUT: typing.ClassVar[int] = 15
def _get_passed_test_output_path(*args, **kwargs):
    ...
def _hash_file_impl(path, hash, as_text):
    ...
def _split_argv(*args, **kwargs):
    """
    Return list of argv before `--` and after (processed and unprocessed)
    """
def call_git(args, cwd = None):
    ...
def clamp(value, min_value, max_value):
    ...
def cleanup_folder(path):
    ...
def ext_id_to_fullname(ext_id: str) -> str:
    ...
def get_argv() -> typing.List[str]:
    ...
def get_ext_test_id(*args, **kwargs):
    ...
def get_global_test_output_path(*args, **kwargs):
    """
    Get global extension test output path. It is shared for all extensions.
    """
def get_local_timestamp():
    ...
def get_setting(path, default = None):
    ...
def get_test_output_path(*args, **kwargs):
    """
    Get local extension test output path. It is unique for each extension test process.
    """
def get_unprocessed_argv() -> typing.List[str]:
    ...
def hash_file(path, hash):
    ...
def is_etm_run(*args, **kwargs):
    ...
def is_running_on_ci(*args, **kwargs):
    ...
def resolve_path(path, root) -> str:
    ...
def sha1_list(strings: typing.List[str], hash_length = 16) -> str:
    ...
def sha1_path(path, hash_length = 16) -> str:
    ...
_settings_iface: carb.settings._settings.ISettings  # value = <carb.settings._settings.ISettings object>
