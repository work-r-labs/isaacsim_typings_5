from __future__ import annotations
import carb as carb
from omni.kit.usd.collect.async_utils import _re_find_all as aio_re_find_all
from omni.kit.usd.collect.omni_client_wrapper import OmniClientWrapper
from omni.kit.usd.collect.utils import Utils
import os as os
import time as time
__all__: list = ['MDLImportItem', 'MDLParser']
class MDLImportItem:
    def __init__(self):
        ...
    def __repr__(self):
        ...
class MDLParser:
    """
    A parser of mdl file, for get the relative texture files.
    
        Args:
            mdl_file_path (str): Human readable string describing the exception.
            mdl_content(bytes): MDL content in bytes array.
        
    """
    def __init__(self, mdl_file_path, mdl_content, path_cache: dict = None):
        ...
    def _convert_packages(self, packages):
        ...
    def _parse_internal(self):
        ...
    def parse(self):
        ...
    @property
    def content(self):
        ...
