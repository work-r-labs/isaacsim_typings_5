from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
import os as os
import shutil as shutil
import sys as sys
import tempfile as tempfile
__all__ = ['ScriptEditor', 'asyncio', 'carb', 'omni', 'os', 'shutil', 'sys', 'tempfile']
class ScriptEditor:
    def __init__(self):
        ...
    def _is_exe(self, path):
        ...
    def _run_editor_async(self, cmd, path):
        ...
    def create_script_file(self, basepath: str, template_file_path: str):
        """
        Creates a new script file
                Args:
                    basepath: folder where the file will be created
                
        """
    def open_script_file(self, path):
        """
        Opens a script file with a python script editor.
                Args:
                    path: the url of the file.
                
        """
