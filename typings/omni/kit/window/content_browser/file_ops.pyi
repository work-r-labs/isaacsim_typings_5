from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import log_info
from carb import log_warn
import collections
from collections import OrderedDict
from collections import namedtuple
from datetime import datetime
from functools import lru_cache
from functools import partial
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.clipboard import clear_clipboard
from omni.kit.widget.filebrowser.clipboard import is_clipboard_cut
from omni.kit.widget.filebrowser.clipboard import save_items_to_clipboard
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.window.content_browser.prompt import Prompt
from omni.kit.window.file_exporter import get_file_exporter
from omni.kit.window.filepicker.file_ops import move_items
from omni.kit.window.filepicker.item_deletion_dialog import ConfirmItemDeletionDialog
from omni.kit.window.filepicker.utils import get_user_folders_dict
from omni.kit.window.filepicker.view import FilePickerView
import os as os
import pathlib as pathlib
import typing
__all__ = ['ConfirmItemDeletionDialog', 'FILE_TYPE_IMAGE', 'FILE_TYPE_SOUND', 'FILE_TYPE_TEXT', 'FILE_TYPE_USD', 'FILE_TYPE_VOLUME', 'FileBrowserItem', 'FileBrowserItemFields', 'FileOpenAction', 'FilePickerView', 'OrderedDict', 'Prompt', 'add_file_open_handler', 'asset_types', 'asyncio', 'carb', 'clear_clipboard', 'copy_item_async', 'copy_items', 'copy_items_with_callback', 'cut_items', 'datetime', 'delete_file_open_handler', 'download_items', 'drop_items', 'get_file_exporter', 'get_file_open_handler', 'get_user_folders_dict', 'is_clipboard_cut', 'log_info', 'log_warn', 'lru_cache', 'move_items', 'namedtuple', 'omni', 'open_file', 'open_stage', 'open_stage_async', 'open_stage_with_new_edit_layer', 'os', 'partial', 'paste_items', 'pathlib', 'save_items_to_clipboard']
class FileOpenAction(tuple):
    """
    FileOpenAction(name, open_fn, matching_type)
    """
    __match_args__: typing.ClassVar[tuple] = ('name', 'open_fn', 'matching_type')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('name', 'open_fn', 'matching_type')
    @staticmethod
    def __new__(_cls, name, open_fn, matching_type):
        """
        Create new instance of FileOpenAction(name, open_fn, matching_type)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new FileOpenAction object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new FileOpenAction object replacing specified fields with new values
        """
def __get_input(*args, **kwargs):
    ...
def _is_ctrl_down() -> bool:
    ...
def _show_readonly_usd_prompt(ok_fn, middle_fn):
    ...
def add_file_open_handler(name: str, open_fn: typing.Callable, file_type: typing.Union[int, typing.Callable]) -> str:
    """
    
        Registers callback/handler to open a file of matching type.
    
        Args:
            name (str): Unique name of handler.
            open_fn (Callable): This function is executed when a matching file is selected for open, i.e. double clicked,
                right mouse menu open, or url submitted to browser bar.  Function signature: void open_fn(url: str).
            file_type (Union[int, func]): Can either be an enumerated int that is one of: [FILE_TYPE_USD,
                FILE_TYPE_IMAGE, FILE_TYPE_SOUND, FILE_TYPE_TEXT, FILE_TYPE_VOLUME] or a more general boolean function
                that returns True if this function should be activated on the given file.  Function
                signature: bool file_type(url: str).
    
        Returns:
            str: Name if successful, None otherwise.
    
        
    """
def copy_item_async(src_path: str, dst_path: str, timeout: float = 300.0, callback: typing.Callable[[str, str, omni.client.impl._omniclient.Result], NoneType] = None) -> str:
    """
    
        Async function.  Copies item (recursively) from one path to another. Note: this function simply
        uses the copy function from omni.client and makes no attempt to optimize for copying from one
        Omniverse server to another.  For that, use the Copy Service.  Example usage:
        await copy_item_async("my_file.usd", "C:/tmp", "omniverse://ov-content/Users/me")
    
        Args:
            src_path (str): Source path to item being copied.
            dst_path (str): Destination path to copy the item.
            timeout (float): Number of seconds to try before erroring out.  Default 10.
            callback (func): Callback to copy result.
    
        Returns:
            str: Destination path name
    
        Raises:
            :obj:`RuntimeWarning`: If error or timeout.
    
        
    """
def copy_items(dst_item: omni.kit.widget.filebrowser.model.FileBrowserItem, src_paths: typing.List[str]):
    ...
def copy_items_with_callback(src_paths: typing.List[str], dst_paths: typing.List[str], callback: typing.Callable = None, copy_callback: typing.Callable[[str, str, omni.client.impl._omniclient.Result], NoneType] = None):
    """
    
        Copies items. Upon success, executes the given callback.
    
        Args:
            src_pathss ([str]): Paths of items to download.
            dst_paths ([str]): Destination paths.
            callback (func): Callback to execute upon success.  Function signature is void callback(List[Union[Exception, str]).
            copy_callback (func): Callback per every copy. Function signature is void callback([str, str, omni.client.Result]).
    
        Raises:
            :obj:`Exception`
    
        
    """
def cut_items(src_items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], view: omni.kit.window.filepicker.view.FilePickerView):
    ...
def delete_file_open_handler(name: str):
    """
    
        Unregisters the named file open handler.
    
        Args:
            name (str): Name of the handler.
    
        
    """
def download_items(selections: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
    ...
def drop_items(dst_item: omni.kit.widget.filebrowser.model.FileBrowserItem, src_paths: typing.List[str], callback: typing.Callable = None, force_drop = False):
    ...
def get_file_open_handler(url: str) -> typing.Callable:
    """
    
        Returns the matching file open handler for the given item.
    
        Args:
            url str: The url of the item to open.
    
        
    """
def open_file(url: str, load_all = True):
    ...
def open_stage(url, load_all = True):
    ...
def open_stage_async(url: str, load_all = True):
    """
    
        Async function for opening a USD file.
    
        Args:
            url (str): Url to file.
    
        
    """
def open_stage_with_new_edit_layer(url: str, load_all = True):
    """
    
        Async function for opening a USD file, then creating a new layer.
    
        Args:
            url (str): Url to file.
    
        
    """
def paste_items(dst_item: omni.kit.widget.filebrowser.model.FileBrowserItem, src_items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], view: omni.kit.window.filepicker.view.FilePickerView, force_drop: bool = False):
    ...
FILE_TYPE_IMAGE: int = 2
FILE_TYPE_SOUND: int = 3
FILE_TYPE_TEXT: int = 4
FILE_TYPE_USD: int = 1
FILE_TYPE_VOLUME: int = 5
_file_open_dict: collections.OrderedDict  # value = OrderedDict([('usd', FileOpenAction(name='usd', open_fn=<function open_stage at 0x709f441daa70>, matching_type=1)), ('Open Python Script Handler', FileOpenAction(name='Open Python Script Handler', open_fn=<function Extension._add_content_browser_ui.<locals>.<lambda> at 0x709ef39b7d90>, matching_type=<function Extension._add_content_browser_ui.<locals>.<lambda> at 0x709ef39b7e20>)), ('Convert to USD', FileOpenAction(name='Convert to USD', open_fn=<function AssetImporterExtension._register_menus.<locals>.<lambda> at 0x709ef299a3b0>, matching_type=<bound method AssetImporterExtension._is_show_open_visible of <omni.kit.tool.asset_importer.extension.AssetImporterExtension object>>))])
_open_readonly_usd_prompt = None
