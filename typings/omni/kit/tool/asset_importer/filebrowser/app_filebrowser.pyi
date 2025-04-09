from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.client.utils import utils as clientutils
from omni.kit.tool.asset_importer.filebrowser import FileBrowserMode
from omni.kit.tool.asset_importer.filebrowser import FileBrowserSelectionType
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.dialog import FilePickerDialog
import os as os
import psutil as psutil
import re as re
import urllib as urllib
__all__ = ['FileBrowserItem', 'FileBrowserMode', 'FileBrowserSelectionType', 'FileBrowserUI', 'FilePickerApp', 'FilePickerDialog', 'asyncio', 'carb', 'clientutils', 'omni', 'os', 'psutil', 're', 'urllib']
class FileBrowserUI:
    def __init__(self, title: str, mode: omni.kit.tool.asset_importer.filebrowser.FileBrowserMode, selection_type: omni.kit.tool.asset_importer.filebrowser.FileBrowserSelectionType, filter_options: typing.List[typing.Tuple[str, str]], save_extensions: typing.List[str] = list(), apply_button_name: str = '', allow_multi_selection = False, build_options_pane_fn: typing.Callable[[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]], bool] = None, on_selection_changed: typing.Callable[[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]], bool] = None):
        ...
    def destroy(self):
        ...
    def open(self, select_fn: typing.Callable[[typing.List[str]], NoneType], cancel_fn: typing.Callable[[], NoneType]):
        ...
    def set_current_directory(self, dir: str):
        ...
    def set_current_filename(self, filename: str):
        ...
class FilePickerApp:
    """
    
        Standalone app to demonstrate the use of the FilePicker dialog.
    
        Args:
            title (str): Title of the window.
            apply_button_name (str): Name of the confirm button.
            mode (FileBrowserMode): The file picker mode that whether it's to open or save.
            selection_type (FileBrowserSelectionType): The file type that confirm event will respond to.
            item_filter_options (list): Array of filter options. Element of array
            is a tuple that first element of this tuple is the regex string for filtering,
            and second element of this tuple is the descriptions, like ("*.*", "All Files").
            By default, it will list all files.
            save_extensions: The real extension name that will be saved.
            allow_multi_selections: Allow to select multiple files.
            build_options_pane_fn (Callable[[List[FileBrowserItem]], bool]): Function to
            build options panel.
            on_selection_changed (Callable[[List[FileBrowserItem]], bool]): Function to
            monitor selection changed.
        
    """
    def __init__(self, title: str, apply_button_name: str, mode: omni.kit.tool.asset_importer.filebrowser.FileBrowserMode, selection_type: omni.kit.tool.asset_importer.filebrowser.FileBrowserSelectionType = 2, item_filter_options: list = [('*.*', 'All Files (*.*)')], save_extensions: list = ['.usd'], allow_multi_selections: bool = False, build_options_pane_fn: typing.Callable[[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]], bool] = None, on_selection_changed: typing.Callable[[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]], bool] = None):
        ...
    def _build_ui(self):
        ...
    def _on_click_cancel(self, filename: str, dirname: str):
        """
        
                This function is called when the user clicks 'Cancel'.
                
        """
    def _on_click_open(self, filepath: str, dirname: str):
        """
        
                The meat of the App is done in this callback when the user clicks 'Accept'. This is
                a potentially costly operation so we implement it as an async operation.  The inputs
                are the filename and directory name. Together they form the fullpath to the selected
                file.
                
        """
    def _on_error(self, msg: str):
        ...
    def _on_filename_changed(self, filename):
        ...
    def _on_filter_item(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        ...
    def _on_selection_changed(self, items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def _update_import_btn_state(self, filepath):
        """
        
                Enable or disable the import button state based on whether the file path is valid
                
        """
    def destroy(self):
        ...
    def hide_dialog(self):
        ...
    def set_current_directory(self, dir: str):
        ...
    def set_current_filename(self, filename: str):
        ...
    def set_custom_fn(self, select_fn: typing.Callable[[typing.List[str]], NoneType], cancel_fn: typing.Callable[[], NoneType]):
        ...
    def show_dialog(self):
        ...
