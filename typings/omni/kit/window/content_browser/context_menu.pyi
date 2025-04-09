from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import log_info
from carb import log_warn
from collections import OrderedDict
from collections import namedtuple
from datetime import datetime
from functools import lru_cache
from functools import partial
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.clipboard import clear_clipboard
from omni.kit.widget.filebrowser.clipboard import get_clipboard_items
from omni.kit.widget.filebrowser.clipboard import is_clipboard_cut
from omni.kit.widget.filebrowser.clipboard import save_items_to_clipboard
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.window.content_browser.file_ops import FileOpenAction
from omni.kit.window.content_browser.file_ops import add_file_open_handler
from omni.kit.window.content_browser.file_ops import copy_item_async
from omni.kit.window.content_browser.file_ops import copy_items
from omni.kit.window.content_browser.file_ops import copy_items_with_callback
from omni.kit.window.content_browser.file_ops import cut_items
from omni.kit.window.content_browser.file_ops import delete_file_open_handler
from omni.kit.window.content_browser.file_ops import download_items
from omni.kit.window.content_browser.file_ops import drop_items
from omni.kit.window.content_browser.file_ops import get_file_open_handler
from omni.kit.window.content_browser.file_ops import open_file
from omni.kit.window.content_browser.file_ops import open_stage
from omni.kit.window.content_browser.file_ops import open_stage_async
from omni.kit.window.content_browser.file_ops import open_stage_with_new_edit_layer
from omni.kit.window.content_browser.file_ops import paste_items
from omni.kit.window.content_browser.prompt import Prompt
from omni.kit.window.file_exporter import get_file_exporter
from omni.kit.window.filepicker.context_menu import BookmarkContextMenu
from omni.kit.window.filepicker.context_menu import CollectionContextMenu
from omni.kit.window.filepicker.context_menu import ConnectionContextMenu
from omni.kit.window.filepicker.context_menu import ContextMenu as FilePickerContextMenu
from omni.kit.window.filepicker.context_menu import LocalContextMenu
from omni.kit.window.filepicker.context_menu import UdimContextMenu
from omni.kit.window.filepicker.file_ops import move_items
from omni.kit.window.filepicker.item_deletion_dialog import ConfirmItemDeletionDialog
from omni.kit.window.filepicker.utils import get_user_folders_dict
from omni.kit.window.filepicker.view import FilePickerView
import os as os
import pathlib as pathlib
__all__ = ['BookmarkContextMenu', 'CollectionContextMenu', 'ConfirmItemDeletionDialog', 'ConnectionContextMenu', 'ContextMenu', 'FILE_TYPE_IMAGE', 'FILE_TYPE_SOUND', 'FILE_TYPE_TEXT', 'FILE_TYPE_USD', 'FILE_TYPE_VOLUME', 'FileBrowserItem', 'FileBrowserItemFields', 'FileOpenAction', 'FilePickerContextMenu', 'FilePickerView', 'ICON_COMMON_PATH', 'LocalContextMenu', 'OrderedDict', 'Prompt', 'UdimContextMenu', 'add_file_open_handler', 'asset_types', 'asyncio', 'carb', 'clear_clipboard', 'copy_item_async', 'copy_items', 'copy_items_with_callback', 'cut_items', 'datetime', 'delete_file_open_handler', 'download_items', 'drop_items', 'get_clipboard_items', 'get_file_exporter', 'get_file_open_handler', 'get_user_folders_dict', 'is_clipboard_cut', 'log_info', 'log_warn', 'lru_cache', 'move_items', 'namedtuple', 'omni', 'open_file', 'open_stage', 'open_stage_async', 'open_stage_with_new_edit_layer', 'os', 'partial', 'paste_items', 'pathlib', 'save_items_to_clipboard']
class ContextMenu(omni.kit.window.filepicker.context_menu.ContextMenu):
    """
    
        Creates popup menu for the hovered FileBrowserItem.  In addition to the set of default actions below,
        users can add more via the add_menu_item API.
    
        
    """
    def __init__(self, **kwargs):
        ...
FILE_TYPE_IMAGE: int = 2
FILE_TYPE_SOUND: int = 3
FILE_TYPE_TEXT: int = 4
FILE_TYPE_USD: int = 1
FILE_TYPE_VOLUME: int = 5
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.content_browser-2.10.3+d02c707b/icons/common')
