from __future__ import annotations
from functools import lru_cache
import os as os
import pathlib as pathlib
import sys as sys
import time as time
__all__ = ['escape_value', 'get_teamcity_build_url', 'is_running_in_teamcity', 'lru_cache', 'os', 'pathlib', 'sys', 'teamcity_log_fail', 'teamcity_message', 'teamcity_metadata_message', 'teamcity_publish_artifact', 'teamcity_publish_image_artifact', 'teamcity_show_image', 'teamcity_status', 'teamcity_test_retry_support', 'time']
def escape_value(value):
    ...
def get_teamcity_build_url(*args, **kwargs):
    ...
def is_running_in_teamcity(*args, **kwargs):
    ...
def teamcity_log_fail(teamCityName, msg, stream = ...):
    ...
def teamcity_message(message_name, stream = ..., **properties):
    ...
def teamcity_metadata_message(metadata_value, stream = ..., metadata_name = '', metadata_testname = ''):
    ...
def teamcity_publish_artifact(artifact_path: str, stream = ...):
    ...
def teamcity_publish_image_artifact(src_path: str, dest_path: str, inline_image_label: str = None, stream = ...):
    ...
def teamcity_show_image(label: str, image_path: str, stream = ...):
    ...
def teamcity_status(text, status: str = 'success', stream = ...):
    ...
def teamcity_test_retry_support(enabled: bool, stream = ...):
    """
    
        With this option enabled, the successful run of a test will mute its previous failure,
        which means that TeamCity will mute a test if it fails and then succeeds within the same build.
        Such tests will not affect the build status.
        
    """
_quote: dict = {"'": "|'", '|': '||', '\n': '|n', '\r': '|r', '[': '|[', ']': '|]'}
