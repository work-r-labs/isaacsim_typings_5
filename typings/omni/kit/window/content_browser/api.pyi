from __future__ import annotations
import asyncio as asyncio
import carb as carb
from omni.kit.widget.filebrowser.clipboard import clear_clipboard
from omni.kit.widget.filebrowser.clipboard import get_clipboard_items
from omni.kit.widget.filebrowser.clipboard import is_clipboard_cut
from omni.kit.widget.filebrowser.clipboard import save_items_to_clipboard
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserUdimItem
from omni.kit.window.content_browser.file_ops import add_file_open_handler
from omni.kit.window.content_browser.file_ops import cut_items
from omni.kit.window.content_browser.file_ops import delete_file_open_handler
from omni.kit.window.content_browser.file_ops import get_file_open_handler
from omni.kit.window.content_browser.file_ops import paste_items
import omni.kit.window.filepicker.api
from omni.kit.window.filepicker.api import FilePickerAPI
from omni.kit.window.filepicker.file_ops import delete_items
from omni.kit.window.filepicker.file_ops import rename_item
__all__ = ['ContentBrowserAPI', 'FileBrowserItem', 'FileBrowserUdimItem', 'FilePickerAPI', 'LISTVIEW_PANE', 'add_file_open_handler', 'asyncio', 'carb', 'clear_clipboard', 'cut_items', 'delete_file_open_handler', 'delete_items', 'get_clipboard_items', 'get_file_open_handler', 'is_clipboard_cut', 'paste_items', 'rename_item', 'save_items_to_clipboard']
class ContentBrowserAPI(omni.kit.window.filepicker.api.FilePickerAPI):
    """
    This class defines the API methods for :obj:`ContentBrowserWidget`.
    """
    def _ContentBrowserAPI__get_valid_copy_cut_items(self):
        ...
    def __init__(self):
        ...
    def _notify_selection_subs(self, pane: int, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def _post_warning(self, message: str) -> None:
        ...
    def _set_checkpoint_widget(self, widget: CheckpointWidget):
        """
        Internal private API.
        """
    def add_checkpoint_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index = -1) -> str:
        """
        
                Adds menu item, with corresponding callbacks, to context menu of checkpoint items.
        
                Args:
                    name (str): Name of the menu item, this name must be unique across the menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The position that this menu item will be inserted to. By default, the item will be appended.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def add_file_open_handler(self, name: str, open_fn: typing.Callable, file_type: typing.Union[int, typing.Callable]) -> str:
        """
        
                Registers callback/handler to open a file of matching type.
        
                Args:
                    name (str): Unique name of handler.
                    open_fn (Callable): This function is executed when a matching file is selected for open, i.e. double clicked,
                        right mouse menu open, or path submitted to browser bar.  Function signature:
                        void open_fn(full_path: str), full_path is the file's system path.
                    file_type (Union[int, func]): Can either be an enumerated int that is one of: [FILE_TYPE_USD,
                        FILE_TYPE_IMAGE, FILE_TYPE_SOUND, FILE_TYPE_TEXT, FILE_TYPE_VOLUME] or a more general boolean function
                        that returns True if this function should be activated on the given file.  Function
                        signature: bool file_type(full_path: str).
        
                Returns:
                    str: Name if successful, None otherwise.
        
                
        """
    def add_import_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable) -> str:
        """
        
                Adds menu item, with corresponding callbacks, to the Import combo box.
        
                Args:
                    name (str): Name of the menu item, this name must be unique across the menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def clear_clipboard(self):
        ...
    def copy_selected_items(self):
        ...
    def cut_selected_items(self):
        ...
    def delete_checkpoint_menu(self, name: str):
        """
        
                Deletes the menu item, with the given name, from the context menu of checkpoint items.
        
                Args:
                    name (str): Name of the menu item.
        
                
        """
    def delete_file_open_handler(self, name: str):
        """
        
                Unregisters the named file open handler.
        
                Args:
                    name (str): Name of the handler.
        
                
        """
    def delete_import_menu(self, name: str):
        """
        
                Deletes the menu item, with the given name, from the Import combo box.
        
                Args:
                    name (str): Name of the menu item.
        
                
        """
    def delete_selected_items(self):
        ...
    def destroy(self):
        ...
    def get_file_open_handler(self, url: str) -> typing.Callable:
        """
        
                Returns the matching file open handler for the given file path.
        
                Args:
                    url str: The url of the file to open.
        
                
        """
    def paste_items(self):
        ...
    def rename_selected_item(self):
        ...
    def subscribe_selection_changed(self, fn: typing.Callable):
        """
        
                Subscribes to file selection changes.
        
                Args:
                    fn (Callable): callback function when file selection changed.
        
                
        """
    def unsubscribe_selection_changed(self, fn: typing.Callable):
        """
        
                Unsubscribe this callback from selection changes.
        
                Args:
                    fn (Callable): callback function when file selection changed.
        
                
        """
LISTVIEW_PANE: int = 2
