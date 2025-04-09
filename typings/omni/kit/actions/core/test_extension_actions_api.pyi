from __future__ import annotations
import difflib as difflib
import logging as logging
import omni as omni
from omni.kit.actions.core.actions import get_action_registry
import os as os
__all__ = ['ActionsAPIDoc', 'difflib', 'get_action_registry', 'logger', 'logging', 'omni', 'os']
class ActionsAPIDoc:
    def __init__(self, tested_ext):
        ...
    def compare_and_update(self):
        ...
    def generate_content(self):
        ...
    def read_content(self):
        ...
def _diff_textfiles(file_content1: str, file_content2: str) -> str:
    """
    
        Compare two strings (file contents) and return a string with differences.
    
        Args:
            file_content1 (str): Content of the first file.
            file_content2 (str): Content of the second file.
    
        Returns:
            str: A string containing the line-by-line differences.
        
    """
logger: logging.Logger  # value = <Logger test_extension_actions_api.py (DEBUG)>
