"""
This module provides utility functions for managing windows, extensions, subprocesses, settings, and clipboard operations within the omni.kit application environment.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import contextlib as contextlib
from functools import lru_cache
import glob as glob
import omni as omni
import os as os
import platform as platform
import shutil as shutil
import subprocess as subprocess
__all__: list = list()
def _load_popup_dialog_ext():
    ...
def _search_path_entry_up(path, entry, max_steps_up = 3):
    ...
def call_once_with_delay(fn: typing.Callable, delay: float):
    """
    Call function once after `delay` seconds.
        If this function called again before `delay` is passed the timer gets reset.
    
        Args:
            fn (Callable): The function to be called.
            delay (float): The time in seconds to wait before calling `fn`.
    """
def cleanup_folder(path):
    """
    Removes all files and folders within the specified directory.
    
        Args:
            path (str): The directory path to clean up.
    """
def clip_text(s, max_count = 80):
    """
    Clips a text to a specified maximum length.
    
        Args:
            s (str): The string to be clipped.
            max_count (int, optional): The maximum allowed length of the string. Defaults to 80.
    """
def copy_text(text):
    """
    Copies the given text to the clipboard.
    
        Args:
            text (str): The text to be copied.
    """
def ext_id_to_fullname(ext_id: str) -> str:
    """
    Converts an extension ID to its full name.
    
        Args:
            ext_id (str): The unique identifier for the extension.
    
        Returns:
            str: The full name of the extension.
    """
def ext_id_to_name_version(ext_id: str) -> typing.Tuple[str, str]:
    """
    Convert 'omni.foo-tag-1.2.3' to 'omni.foo-tag' and '1.2.3'
    
        Args:
            ext_id (str): The unique identifier of the extension.
    
        Returns:
            Tuple[str, str]: A tuple containing the extension name and version.
    """
def get_ext_info_dict(ext_manager, ext_info) -> typing.Tuple[carb.dictionary._dictionary.Item, bool]:
    """
    Gets a dictionary containing extension information.
    
        Args:
            ext_manager: The manager responsible for extensions.
            ext_info: Information about the specific extension.
    
        Returns:
            Tuple[carb.dictionary.Item, bool]: A tuple containing the extension dictionary and a boolean indicating existence.
        
    """
def get_extpath_git_ext(*args, **kwargs):
    ...
def get_setting(path, default = None):
    """
    Retrieves a setting value based on its path, or returns a default value if not found.
    
        Args:
            path (str): The path of the setting to retrieve.
            default: The default value to return if the setting is not found.
    """
def is_vscode_installed(*args, **kwargs):
    """
    is vscode installed.
    """
def is_windows(*args, **kwargs):
    ...
def open_file_using_os_default(path: str):
    """
    Opens a file using the OS's default program.
    
        Args:
            path (str): The file system path to the file to be opened.
    """
def open_in_vscode(path: str):
    """
    Opens the given file or directory in VSCode.
    
        Args:
            path (str): The file or directory path to open.
    """
def open_in_vscode_if_enabled(path: str, prefer_vscode: bool = True):
    """
    Opens the specified path in VSCode if preferred and installed, otherwise using the OS default.
    
        Args:
            path (str): The filesystem path to be opened.
            prefer_vscode (bool): Flag indicating if VSCode should be preferred.
    """
def open_url(url):
    """
    Opens the given URL in the default web browser.
    
        Args:
            url (str): The URL to be opened.
    """
def open_using_os_default(path: str):
    """
    Opens the specified path using the OS default program.
    
        Args:
            path (str): The file or directory path to open.
    """
def run_process(args):
    """
    Runs a subprocess with the provided arguments.
    
        Args:
            args (List[str]): The command line arguments for the subprocess.
    """
def set_default_and_get_setting(path, default = None):
    """
    Sets a default value for a given setting path and retrieves the current setting.
    
        Args:
            path (str): The settings path to query.
            default: The default value to set if the setting isn't already set.
    """
def show_ok_popup(title, message, **dialog_kwargs):
    """
    Displays an OK popup dialog with a title and message.
    
        Args:
            title (str): The title of the popup.
            message (str): The content message of the popup.
    
        Keyword Args:
            disable_cancel_button (bool): If True, the cancel button will be hidden.
    """
def show_user_input_popup(title, label, default):
    """
    Displays a popup dialog for user input.
    
        Args:
            title (str): The title of the popup dialog.
            label (str): The label displayed above the input field.
            default (str): The default value populated in the input field.
        
    """
def version_to_str(version: typing.Tuple[int, int, int, str, str]) -> str:
    """
    Generate string `0.0.0-tag+tag`
    
        Args:
            version (Tuple[int, int, int, str, str]): Version info to convert to string.
    
        Returns:
            str: String representation of the version.
    """
