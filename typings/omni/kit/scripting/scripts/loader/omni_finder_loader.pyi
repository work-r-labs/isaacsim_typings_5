from __future__ import annotations
from _frozen_importlib import ModuleSpec
import _frozen_importlib_external
from _frozen_importlib_external import SourceFileLoader
import ast as ast
import copy as copy
import importlib as importlib
from importlib.abc import MetaPathFinder
from omni.kit.scripting.scripts.loader import io
from omni.kit.scripting.scripts.loader.omni_cache import OmniCache
import os as os
import re as re
import sys as sys
import typing
__all__ = ['MetaPathFinder', 'ModuleSpec', 'OmniCache', 'OmniFinder', 'OmniLoader', 'SourceFileLoader', 'argsort', 'ast', 'copy', 'disable_omni_finder_loader', 'enable_omni_finder_loader', 'get_dependency_list', 'get_dependency_module_name', 'get_local_path', 'import_file', 'importlib', 'io', 'os', 're', 'remove_file', 'sys']
class OmniFinder(importlib.abc.MetaPathFinder):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _collect_dependencies = None
    _dependencies: typing.ClassVar[dict] = {}
    _dependency_module_names: typing.ClassVar[dict] = {}
    _module_paths: typing.ClassVar[dict] = {}
    @classmethod
    def add_fix_missing_dependency_path(cls):
        ...
    @classmethod
    def add_folder(cls, path, module_name):
        ...
    @classmethod
    def file_was_loaded_by_finder(cls, filename: str):
        ...
    @classmethod
    def find_spec(cls, fullname, path, target = None):
        """
        
                Try to find a spec for the specified module.
        
                Returns the matching spec, or None if not found.
                
        """
    @classmethod
    def remove_folder(cls, module_name):
        ...
    @classmethod
    def reset(cls):
        ...
    @classmethod
    def spec_from_module(cls, fullname, path):
        ...
    @classmethod
    def spec_from_namespace(cls, fullname, path, name):
        ...
    @classmethod
    def spec_from_package(cls, fullname, path):
        ...
class OmniLoader(_frozen_importlib_external.SourceFileLoader):
    """
    
        Implements a source loader for files that can come from any data source implemented by data.io.
        Fully supports the Python import system, including namespaces.
    
        The primary use of this class is to import modules from Omniverse or the local file system
        
    """
    def __init__(self, fullname, path):
        ...
    def create_module(self, spec):
        ...
    def get_data(self, path):
        ...
    def path_mtime(self, path):
        ...
    def path_stats(self, path):
        ...
    def set_data(self, path, data, *, _mode = 438):
        ...
def _find_imported_dependencies(file: str):
    ...
def _import_module(path, module_name, is_dir = False):
    ...
def _make_import_friendly(path):
    ...
def _remove_redundant_path_seperator(path: str):
    """
     remove path seperators. Assume the path ends with .py file
            convert 'omniverse://ov-content/Users/tingwuw@nvidia.com/fix_and_play/../../basics.py'
            into 'omniverse://ov-content/Users/tingwuw@nvidia.com/basics.py'
        
    """
def _resolve_dependencies(modules_path: str):
    """
     For every modules from files, register and check for
            dependencies between them
        
    """
def argsort(seq):
    ...
def disable_omni_finder_loader():
    ...
def enable_omni_finder_loader():
    ...
def get_dependency_list(path: str) -> typing.List[typing.Tuple[str, str]]:
    ...
def get_dependency_module_name(path: str) -> str:
    ...
def get_local_path(path: str) -> str:
    ...
def import_file(path: str) -> str:
    """
    
        Imports a single file and sets up the loader so it can find relative files. Returns the fullname of the module.
        
    """
def remove_file(path: str) -> str:
    ...
_email_regex: re.Pattern  # value = re.compile('.*(([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\\.[A-Z|a-z]{2,})+).*')
