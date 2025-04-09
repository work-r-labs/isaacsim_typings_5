"""
Pip Omniverse Kit API

Module to enable usage of ``pip install`` in Omniverse Kit environment. It wraps ``pip install`` calls and reroutes package installation into
user specified environment folder.

Package folder is selected from config string at path: `/app/omni.kit.pipapi/archiveDirs` and added into :mod:`sys.path`.
"""
from __future__ import annotations
import carb as carb
from contextlib import contextmanager
import functools as functools
import importlib as importlib
import json as json
import logging as logging
import omni as omni
import os as os
from pathlib import Path
import sys as sys
import typing as typing
__all__: list = ['ExtensionManagerPip', 'install', 'call_pip', 'remove_archive_directory', 'add_archive_directory']
class ExtensionManagerPip(omni.ext._extensions.IExt):
    @staticmethod
    def _process_ext_pipapi_config(ext_id: str):
        ...
    @staticmethod
    def on_before_ext_enabled(*args, **kwds):
        ...
    def on_startup(self, ext_id):
        ...
def _add_to_cache(package):
    ...
def _change_envvar(*args, **kwds):
    """
    Change environment variable for the execution block and then revert it back.
    
        This function is a context manager.
    
        Example:
    
        .. code-block:: python
    
            with _change_envvar("PYTHONPATH", "C:/hello"):
                print(os.environ.get("PYTHONPATH"))
    
        Args:
            name (str): Env var to change.
            value: new value
        
    """
def _get_setting(path, default = None):
    ...
def _initialize(*args, **kwargs):
    ...
def _is_in_cache(package) -> bool:
    ...
def _load_cache():
    ...
def _log_error(s):
    ...
def _log_info(s):
    ...
def _try_import(module: str, log_error: bool = False):
    ...
def add_archive_directory(path: str, root: str = None):
    """
    
        Add pip additional dirs/links (for pip install --find-links).
        
    """
def call_pip(args: typing.List[str], surpress_output: bool = False) -> int:
    """
    Call pip with given arguments.
    
        Args:
            args (list): list of arguments to pass to pip
            surpress_output (bool): if True, surpress pip output
        Returns:
                int: return code of pip call
    """
def install(*args, **kwds) -> bool:
    """
    
        Install pacakage using pip into user specified env path. Install calls for particular package name persistently cache
        to avoid overhead for future calls when package is already installed. Cache is stored in the `.install_cache.json` file in the user specified env path folder.
    
        Args:
            package(str): Package name to install. It is basically a command to pip install, it can include version and other flags.
            module(str): Module name to import, by default module assumed to be equal to package.
            ignore_import_check(bool, optional): If ``True`` ignore attempt to import module and call to ``pip`` anyway - can be slow.
            ignore_cache(bool, optional): If ``True`` ignore caching and call to ``pip`` anyway - can be slow.
            version (str, optional): Package version.
            use_online_index(bool, optional): If ``True`` and package can't be found in any of archive directories try to use default pip index.
            surpress_output(bool, optional): If ``True`` pip process output to stdout and stderr will be surpressed, as well as warning when install failed.
            extra_args(List[str], optional): a list of extra arguments to pass to the Pip process
    
        Returns:
            ``True`` if installation was successfull.
        
    """
def profile(f = None, mask = 1, zone_name = None, add_args = True):
    ...
def remove_archive_directory(path: str):
    """
    
        Remove pip additional dirs/links.
        
    """
ALLOW_ONLINE_INDEX_KEY: str = '/exts/omni.kit.pipapi/allowOnlineIndex'
CACHE_FILE_NAME: str = '.install_cache.json'
DEFAULT_ENV_PATH: str = '../../target-deps/pip3-envs/default'
USE_INTERNAL_PIP: bool = False
_archive_dirs: set = set()
_attempted_to_upgrade_pip: bool = False
_cached_install_calls: dict = {}
_cached_install_calls_file = None
_debug_log: bool = False
_install_check_ignore_version: bool = True
_settings_iface = None
_started: bool = True
_user_env_path: str = ''
logger: logging.Logger  # value = <Logger omni.kit.pipapi.pipapi (DEBUG)>
