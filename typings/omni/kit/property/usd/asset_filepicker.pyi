from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni import ui
import os as os
from pxr import Sdf
import typing
from typing import Any
__all__: list = list()
def check_paths_with_callback(paths, file_exts = (('*.*', 'All Files')), callback = None):
    """
    
        Utility function that checks paths with callback if paths pass check.
    
        Args:
            paths (List[str]): The paths to check.
            file_exts (Tuple[Tuple[str, str]]): The file extensions.
            callback (Callable[[List[str]], None]): The callback to call if the paths pass the check.
        
    """
def replace_query(url, new_query):
    """
    
        Replace the query of the URL.
    
        Args:
            url (str): The URL to replace the query of.
            new_query (str): The new query to replace the query of the URL with.
    
        Returns:
            str: The URL with the new query.
        
    """
def show_asset_file_picker(title: str, assign_value_fn: typing.Callable[[typing.Any, str], None], model_weak, stage_weak, layer_weak = None, file_exts: tuple[tuple[str, str]] = None, frame = None, multi_selection: bool = False, on_selected_fn = None):
    """
    
        Show the asset file picker.
    
        Args:
            title (str): The title of the file picker.
            assign_value_fn (Callable[[Any, str], None]): The function to assign the value.
            model_weak (WeakRef): The weak reference to the model.
            stage_weak (WeakRef): The weak reference to the stage.
            layer_weak (WeakRef): The weak reference to the layer.
            file_exts (Tuple[Tuple[str, str]]): The file extensions.
        
    """
DEFAULT_FILE_EXTS: tuple = ('*.*', 'All Files')
