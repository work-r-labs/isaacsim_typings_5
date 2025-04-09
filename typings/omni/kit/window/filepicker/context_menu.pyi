from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import log_warn
from datetime import datetime
from functools import partial
import omni as omni
from omni.kit.notification_manager.notification_info import NotificationStatus
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.nucleus_model import NucleusConnectionItem
from omni.kit.window.filepicker.about_dialog import AboutDialog
from omni.kit.window.filepicker.bookmark_model import BookmarkItem
from omni.kit.window.filepicker.file_ops import about_connection
from omni.kit.window.filepicker.file_ops import add_bookmark
from omni.kit.window.filepicker.file_ops import add_connection
from omni.kit.window.filepicker.file_ops import checkpoint_items
from omni.kit.window.filepicker.file_ops import copy_to_clipboard
from omni.kit.window.filepicker.file_ops import create_folder
from omni.kit.window.filepicker.file_ops import create_usd_file
from omni.kit.window.filepicker.file_ops import delete_bookmark
from omni.kit.window.filepicker.file_ops import delete_items
from omni.kit.window.filepicker.file_ops import edit_bookmark
from omni.kit.window.filepicker.file_ops import exec_tasks_async
from omni.kit.window.filepicker.file_ops import is_item_checkpointable
from omni.kit.window.filepicker.file_ops import is_usd_supported
from omni.kit.window.filepicker.file_ops import log_out_from_connection
from omni.kit.window.filepicker.file_ops import move_item_async
from omni.kit.window.filepicker.file_ops import move_items
from omni.kit.window.filepicker.file_ops import move_items_async
from omni.kit.window.filepicker.file_ops import obliterate_item_async
from omni.kit.window.filepicker.file_ops import obliterate_items
from omni.kit.window.filepicker.file_ops import open_in_file_browser
from omni.kit.window.filepicker.file_ops import refresh_connection
from omni.kit.window.filepicker.file_ops import refresh_item
from omni.kit.window.filepicker.file_ops import remove_connection
from omni.kit.window.filepicker.file_ops import rename_file
from omni.kit.window.filepicker.file_ops import rename_file_async
from omni.kit.window.filepicker.file_ops import rename_item
from omni.kit.window.filepicker.file_ops import restore_item_async
from omni.kit.window.filepicker.file_ops import restore_items
from omni.kit.window.filepicker.item_deletion_dialog import ConfirmItemDeletionDialog
from omni.kit.window.filepicker.versioning_helper import VersioningHelper
from omni.kit.window.filepicker.view import FilePickerView
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.input_dialog import InputDialog
from omni.kit.window.popup_dialog.message_dialog import MessageDialog
from omni import ui
import os as os
import pathlib
import subprocess as subprocess
import sys as sys
__all__: list = ['BaseContextMenu', 'ContextMenu', 'UdimContextMenu', 'CollectionContextMenu', 'ConnectionContextMenu', 'BookmarkContextMenu', 'LocalContextMenu']
class BaseContextMenu:
    """
    
        Base class popup menu for the hovered FileBrowserItem.  Provides API for users to add menu items.
    
        
    """
    def __init__(self, title: str = None, **kwargs):
        """
        
                Initialize the BaseContextMenu.
        
                Keyword Args:
                    title (Optional[str]): The title of the context menu default `None`.
                
        """
    def add_menu_item(self, name: str, glyph: str, onclick_fn: typing.Callable, show_fn: typing.Callable, index: int = -1, separator_name: typing.Optional[str] = None) -> str:
        """
        
                Adds menu item, with corresponding callbacks, to this context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open'), this name must be unique across the context menu.
                    glyph (str): Associated glyph to display for this menu item.
                    onclick_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(context: Dict)
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(context: Dict).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The position that this menu item will be inserted to.
                    separator_name (str): The separator name of the separator menu item. Default to '_placeholder_'. When the
                        index is not explicitly set, or if the index is out of range, this will be used to locate where to add
                        the menu item; if specified, the index passed in will be counted from the saparator with the provided
                        name. This is for OM-86768 as part of the effort to match Navigator and Kit UX for Filepicker/Content Browser for context menus.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def delete_menu_item(self, name: str):
        """
        
                Deletes the menu item, with the given name, from this context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open').
        
                
        """
    def destroy(self):
        """
        Destructor.
        """
    def hide(self):
        """
        
                Hides the popup menu if it is shown.
        
                
        """
    def show(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem] = list()):
        """
        
                Creates the popup menu from definition for immediate display. Receives as input, information about the
                item.  These values are made available to the callback via the 'context' dictionary.
        
                Args:
                    item (FileBrowseritem): Item for which to create menu.,
                    selected ([FileBrowserItem]): List of currently selected items. Default [].
        
                
        """
    @property
    def context(self) -> dict:
        """
        dict: Provides data to the callback.  Available keys are {'item', 'selected'}
        """
    @property
    def menu(self) -> omni.ui._ui.Menu:
        """
        Returns: obj:`omni.ui.Menu` The menu widget
        """
class BookmarkContextMenu(BaseContextMenu):
    """
    Creates popup menu for BookmarkItems.
    """
    def __init__(self, **kwargs):
        ...
class CollectionContextMenu(BaseContextMenu):
    """
    Creates popup menu for the hovered FileBrowserItem that are collection nodes.
    """
    def __init__(self, **kwargs):
        ...
class ConnectionContextMenu(BaseContextMenu):
    """
    Creates popup menu for the server connection FileBrowserItem grouped under Omniverse collection node.
    """
    def __init__(self, **kwargs):
        ...
class ContextMenu(BaseContextMenu):
    """
    
        Creates popup menu for the hovered FileBrowserItem.  In addition to the set of default actions below,
        users can add more via the add_menu_item API.
    
        
    """
    def __init__(self, **kwargs):
        """
         Creates the ContextMenu for the file picker, including all common menu items 
        """
class LocalContextMenu(BaseContextMenu):
    """
    
        Creates popup menu for the hovered FileBrowserItem.  In addition to the set of default actions below,
        users can add more via the add_menu_item API.
    
        
    """
    def __init__(self, **kwargs):
        ...
class UdimContextMenu(BaseContextMenu):
    """
    Creates popup menu for the hovered FileBrowserItem that are Udim nodes.
    """
    def __init__(self, **kwargs):
        ...
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/common')
