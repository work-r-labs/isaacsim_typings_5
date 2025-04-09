from __future__ import annotations
import carb as carb
import omni as omni
from omni.client.utils import utils as clientutils
import os as os
import pathlib
from pathlib import Path
import re as re
import typing
__all__ = ['Path', 'Utils', 'carb', 'clientutils', 'omni', 'os', 're']
class Utils:
    SUPPORTED_FORMAT_RE: typing.ClassVar[re.Pattern]  # value = re.compile('.*.fbx$|.*.obj$|.*.gltf$|.*.lxo$|.*.md5$', re.IGNORECASE)
    @staticmethod
    def compute_absolute_path(base_path, is_base_path_folder, path, is_path_folder):
        ...
    @staticmethod
    def is_folder(path):
        ...
    @staticmethod
    def list_folder_async(folder_path):
        ...
    @staticmethod
    def remove_prefix(text, prefix):
        ...
    @staticmethod
    def strip_file_regex(input_path: pathlib.Path, file_regex_patterns) -> [str, str]:
        """
        Strips the input_path regex from input_path file; else, returns stem
        
                Args:
                    input_path (Path): input file path (i.e., 'cad_part.asm.42')
                    file_regex_patterns: regex patterns to strip from input_path (i.e., 'r"\\.(asm|prt)(\\.[0-9]+)?$"')
        
                Returns:
                    stripped_path (str): name of file without suffix (i.e., 'cad_part')
                    file_regex (str): returns file suffix from input_path (i.e., '.asm.42')
                
        """
