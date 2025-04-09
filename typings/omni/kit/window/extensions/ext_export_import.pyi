"""
This module provides functionality to export and import extensions via a user interface in the omni.kit.window.extensions package.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.window.extensions.common import get_omni_documents_path
from omni.kit.window.extensions.utils import get_setting
import os as os
__all__: list = list()
def _ask_user_for_path(is_export: bool, apply_button_label = 'Choose', title = None):
    ...
def _export(ext_id: str):
    ...
def _import():
    ...
def _print_and_log(message):
    ...
def export_ext(ext_id: str):
    """
    Exports the specified extension.
    
        Args:
            ext_id (str): The identifier of the extension to export.
    """
def import_ext():
    """
    Imports an extension from a user-selected zip archive.
    
        This function asynchronously triggers the import operation. It prompts the user to select an extension archive (.zip) using a file picker dialog. Once selected, it proceeds to unpack the extension into the registry cache folder. The function ensures the operation runs in the background without blocking the main thread.
    
        This is part of a larger system managing extensions, including exporting and maintaining a registry of available extensions.
    
        This function does not accept any arguments.
    """
RECENT_EXPORT_PATH_KEY: str = '/persistent/exts/omni.kit.window.extensions/recentExportPath'
