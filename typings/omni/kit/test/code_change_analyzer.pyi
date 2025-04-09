from __future__ import annotations
import json as json
import logging as logging
import omni as omni
from omni.kit.test.repo_test_context import RepoTestContext
from omni.kit.test.utils import get_global_test_output_path
from omni.kit.test.utils import sha1_list
from omni.kit.test.utils import sha1_path
import os as os
__all__ = ['ChangeAnalyzerResult', 'CodeChangeAnalyzer', 'KNOWN_EXT_SOURCE_PATH', 'RepoTestContext', 'STARTUP_SEQUENCE_EXCLUDE', 'get_global_test_output_path', 'json', 'logger', 'logging', 'omni', 'os', 'sha1_list', 'sha1_path']
class ChangeAnalyzerResult:
    def __init__(self):
        ...
class CodeChangeAnalyzer:
    """
    repo_test can provide (if in MR and on TC) with a list of changed files using env var.
        Check if changed ONLY extensions. If any change is not in `source/extensions` -> run all tests
        If changed ONLY extensions than for each test solve list of ALL enabled extensions and check against that list.
        
    """
    def __init__(self, repo_test_context: omni.kit.test.repo_test_context.RepoTestContext):
        ...
    def _build_startup_sequence(self, result: ChangeAnalyzerResult, ext_name: str, exts: typing.List):
        ...
    def _gather_changed_extensions(self, repo_test_context: omni.kit.test.repo_test_context.RepoTestContext):
        ...
    def allow_sampling(self) -> bool:
        ...
    def analyze(self, test_id: str, ext_name: str, exts_to_enable: typing.List[str]) -> ChangeAnalyzerResult:
        ...
    def get_changed_extensions(self) -> typing.List[str]:
        ...
def _get_extension_hash(package_id, path):
    ...
def _get_extension_name_for_file(file):
    ...
def _print(str, *argv):
    ...
KNOWN_EXT_SOURCE_PATH: list = ['kit/source/extensions/', 'source/extensions/']
STARTUP_SEQUENCE_EXCLUDE: list = ['omni.rtx.shadercache.d3d12', 'omni.rtx.shadercache.vulkan']
logger: logging.Logger  # value = <Logger omni.kit.test.code_change_analyzer (DEBUG)>
