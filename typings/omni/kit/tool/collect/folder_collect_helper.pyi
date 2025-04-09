"""
This module provides a helper class for collecting files from a folder with filtering and custom collection logic, and a UI class for file selection.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
import traceback as traceback
import typing
import urllib as urllib
import weakref as weakref
__all__ = ['CheckBoxStatus', 'FolderCollectHelper', 'SelectFileDialog', 'asyncio', 'carb', 'functools', 'handle_exception', 'omni', 'run_coroutine', 'traceback', 'urllib', 'weakref']
class CheckBoxStatus:
    """
    A class to manage the status of a checkbox.
    
        This class holds the state of a checkbox and its associated file path, providing a structured way to manage checkbox states within UI components.
    
        Args:
            checkbox: The checkbox UI element this status is associated with.
            file_path: The file path related to the checkbox, used to identify it uniquely.
    """
    def __init__(self, checkbox, file_path):
        """
        Initializes a new instance of CheckBoxStatus.
        """
class FolderCollectHelper:
    """
    A helper class for collecting files from a specified folder with filtering and custom collection logic.
    
        The class is designed to process a folder, apply a filter to the files within, perform a collection operation, and execute a callback once file collection is finished. It also manages a progress popup to inform the user about the ongoing operation.
    
        Args:
            folder (str): The path of the folder from which to collect files.
            filter_fn (Callable): A function to filter files. It should return True for files to be collected.
            collect_fn (Callable): A function to execute on the collected files.
            finish_get_files_callback (Callable): A callback function to execute after file collection is completed.
            progress_popup: An object to show progress and status during the file collection operation.
    """
    @staticmethod
    def _FolderCollectHelper__get_files(*args, **kwargs):
        ...
    def __init__(self, folder: str, filter_fn: typing.Callable, collect_fn: typing.Callable, finish_get_files_callback: typing.Callable, progress_popup):
        ...
    def _get_files_by_client(self, directory: str, recursive: int):
        ...
    def _get_selected_window(self):
        ...
    def destroy(self):
        ...
class SelectFileDialog:
    """
    A user interface class for selecting files from a dialog window.
    
        This class creates a modal dialog window that allows users to select multiple files and perform actions such as collecting the selected files or cancelling the selection.
    
        Args:
          on_collect_fn (Callable, optional): Function to call with selected files when 'Collect Selected' is clicked.
          on_cancel_fn (Callable, optional): Function to call when 'Cancel' is clicked.
    """
    MAX_VISIBLE_FILE_COUNT: typing.ClassVar[int] = 10
    WINDOW_WIDTH: typing.ClassVar[int] = 580
    def __del__(self):
        ...
    def __init__(self, on_collect_fn = None, on_cancel_fn = None):
        ...
    def _check_and_select_all(self, select_all_check_box):
        ...
    def _on_cancel_fn(self):
        ...
    def _on_checkbox_fn(self, model, check_box_index, select_all_check_box):
        ...
    def _on_collect_fn(self):
        ...
    def _on_select_all_fn(self, model):
        ...
    def destroy(self):
        ...
    def is_visible(self):
        ...
    def show(self, file_paths = None):
        ...
def handle_exception(func):
    """
    Decorator that catches and logs exceptions in asynchronous functions.
    
        Args:
            func (Callable): The asynchronous function to be wrapped by the decorator.
        
    """
