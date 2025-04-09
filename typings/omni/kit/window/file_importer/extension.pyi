from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import events
from carb import log_warn
from functools import partial
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.detail_view import DetailFrameController as ImportOptionsDelegate
from omni.kit.window.filepicker.dialog import FilePickerDialog
import os as os
__all__ = ['DEFAULT_FILE_EXTENSION_TYPES', 'DEFAULT_FILE_POSTFIX_OPTIONS', 'FileBrowserItem', 'FileImporterExtension', 'FilePickerDialog', 'ImportOptionsDelegate', 'UI_READY_EVENT', 'WINDOW_NAME', 'asyncio', 'carb', 'default_filter_handler', 'events', 'g_singleton', 'get_instance', 'log_warn', 'omni', 'on_filter_item', 'on_import', 'os', 'partial']
class FileImporterExtension(omni.ext._extensions.IExt):
    """
    A Standardized file import dialog.
    """
    def __init__(self):
        ...
    def _is_nucleus_server_url(self, url: str):
        ...
    def _load_default_settings(self) -> dict:
        ...
    def _on_apply_path(self, url: str, file_extension_types: typing.List[typing.Tuple[str, str]], file_filter_handler: typing.Callable[[str, str, str], bool]):
        ...
    def _on_client_bookmarks_changed(self, client_bookmarks: typing.Dict):
        ...
    def _on_filename_changed(self, filename, show_only_folders = False):
        ...
    def _on_selection_changed(self, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], show_only_folders = False, allow_multi_files_selection = False):
        ...
    def _on_ui_ready(self, event: carb.events._events.IEvent):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def add_import_options_frame(self, name: str, delegate: omni.kit.window.filepicker.detail_view.DetailFrameController):
        """
        
                Adds a set of import options to the dialog.  Should be called after show_window.
        
                Args:
                    name (str): Title of the options box.
                    delegate (ImportOptionsDelegate): Subclasses specified delegate and overrides the
                        _build_ui_impl method to provide a custom widget for getting user input.
        
                
        """
    def click_apply(self, filename_url: str = None, postfix: str = None, extension: str = None):
        """
        Helper function to progammatically execute the apply callback.  Useful in unittests
        """
    def click_cancel(self, cancel_handler: typing.Callable[[str, str], NoneType] = None):
        """
        Helper function to progammatically execute the cancel callback.  Useful in unittests
        """
    def destroy_dialog(self):
        ...
    def detach_from_main_window(self):
        """
        Detach the current file importer dialog from main window.
        """
    def get_dialog(self):
        ...
    def hide_window(self):
        """
        Hides and destroys the dialog window.
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def select_items_async(self, url: str, filenames: typing.List[str] = list()) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        Helper function to programatically select multiple items in filepicker. Useful in unittests.
        """
    def show_window(self, title: str = None, width: int = 1080, height: int = 450, show_only_collections: typing.List[str] = None, show_only_folders: bool = False, file_postfix_options: typing.List[str] = None, file_extension_types: typing.List[typing.Tuple[str, str]] = None, file_filter_handler: typing.Callable[[str, str, str], bool] = None, import_button_label: str = 'Import', import_handler: typing.Callable[[str, str, typing.List[str]], NoneType] = None, filename_url: str = None, file_postfix: str = None, file_extension: str = None, hide_window_on_import: bool = True, should_validate: bool = False, focus_filename_input: bool = True, allow_multi_files_selection: bool = False):
        """
        
                Displays the import dialog with the specified settings.
        
                Keyword Args:
                    title (str): The name of the dialog
                    width (int): Width of the window (Default=1250)
                    height (int): Height of the window (Default=450)
                    show_only_collections (List[str]): Which of these collections, ["bookmarks", "omniverse", "my-computer"] to display.
                    show_only_folders (bool): Show only folders in the list view.
                    file_postfix_options (List[str]): A list of filename postfix options. Nvidia defaults.
                    file_extension_types (List[Tuple[str, str]]): A list of filename extension options.  Each list
                        element is a (extension name, description) pair, e.g. (".usd", "USD format"). Nvidia defaults.
                    file_filter_handler (Callable): The filter handler that is called to decide whether or not to display a file.
                        Function signature is filter_handler(filename: str, filter_postfix: str, filter_ext: str) -> bool
                    import_button_label (str): Label for the import button (Default="Import")
                    import_handler (Callable): The callback to handle the import, filename is the name of the file,
                        and dirname being the containing directory path with a ending slash.  Function signature is
                        import_handler(filename: str, dirname: str, selections: List[str]) -> None
                    filename_url (str): Url of the file to import, if any.
                    file_postfix (str): Sets selected postfix to this value if specified.
                    file_extension (str): Sets selected extension to this value if specified.
                    hide_window_on_import (bool): Whether the dialog hides on apply; if False, it means that whether to hide the
                        dialog should be decided by import handler.
                    should_validate (bool): Whether filename validation should be performed.
        
                
        """
    @property
    def is_ui_ready(self) -> bool:
        ...
    @property
    def is_window_visible(self) -> bool:
        ...
def _filename_validator(filename: str):
    """
    Validates filename has invalid chars.
    """
def _filepath_validation_handler(filepath: str):
    """
    Validates the filename being imported exists.
    """
def _get_usd_file_exts():
    ...
def _save_default_settings(default_settings: typing.Dict):
    ...
def default_filter_handler(filename: str, filter_postfix: str, filter_ext: str) -> bool:
    """
    
        Show only files whose names end with: *<postfix>.<ext>.
        Args:
            filename (str): The item's file name .
            filter_postfix (str): Whether file name match this filter postfix.
            filter_ext (str): Whether file name match this filter extension.
        Returns:
            True if file could show in dialog. Otherwise Flase.
        
    """
def get_instance():
    ...
def on_filter_item(filter_fn: typing.Callable[[str], bool], dialog: omni.kit.window.filepicker.dialog.FilePickerDialog, item: omni.kit.widget.filebrowser.model.FileBrowserItem, show_only_folders: bool = True) -> bool:
    """
    
        Filter the items shown in the import file picker dialog.
        Args:
            dialog (FilePickerDialog): The import file dialog.
            show_only_folders (bool): Whether only folder should be show.
            item (FileBrowserItem): The file browser item show in import file dialog.
        Returns:
            True if item could show in dialog. Otherwise Flase.
        
    """
def on_import(import_fn: typing.Callable[[str, str, typing.List[str]], NoneType], dialog: omni.kit.window.filepicker.dialog.FilePickerDialog, filename: str, dirname: str, hide_window_on_import: bool = True, should_validate: bool = False):
    """
    
        Called when import file, it's a wrapper to import_fn.
        Args:
            import_fn (Callable): The callback to handle the import,
                filename being the name of the file, and dirname being the containing directory path with an ending slash.  Function signature is
                import_fn(filename: str, dirname: str, extension: str, selections: List[str]) -> None
            dialog (FilePickerDialog): The import file dialog.
            filename (str): Name of the target file, excluding filename extension.
            dirname (str): The target folder name to import to.
        Keyword Args:
            hide_window_on_import (bool):Whether hide the dialog when import.
            should_validate (bool): Whether filename validation should be performed.
        
    """
DEFAULT_FILE_EXTENSION_TYPES: list = [('*.usd, *.usda, *.usdc, *.usdz', 'USD Files'), ('*.*', 'All files')]
DEFAULT_FILE_POSTFIX_OPTIONS: list = [None, 'anim', 'cache', 'curveanim', 'geo', 'material', 'project', 'seq', 'skel', 'skelanim']
UI_READY_EVENT: int = 284649323482245942
WINDOW_NAME: str = 'File Importer'
_usd_file_exts = None
g_singleton: FileImporterExtension  # value = <omni.kit.window.file_importer.extension.FileImporterExtension object>
