"""

Model and Item classes for navigating the local file system on the machine.
"""
from __future__ import annotations
import asyncio as asyncio
from carb import log_warn
from datetime import datetime
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.model import handle_item_creation_exception
from omni import ui
import os as os
import pathlib
import posix
import stat as stat
__all__: list = ['FileSystemItem', 'FileSystemItemFactory', 'FileSystemModel']
class FileSystemItem(omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        A Filebrowser item class for navigating a the local filesystem in a Filebrowser view.
        Sub-classed from :obj:`FileBrowserItem`.
    
        Args:
            path (str): Path of the item.
            fields (:obj:`FileBrowserItemFields`): Fields of the item.
            is_folder (bool): Specify the item as a folder.
        
    """
    @staticmethod
    def keep_entry(entry: posix.DirEntry) -> bool:
        """
        
                Return True if we want to keep the given entry.
        
                Args:
                    entry (:obj:`os.DirEntry`): directory entry.
                
        """
    def __init__(self, path: str, fields: omni.kit.widget.filebrowser.model.FileBrowserItemFields, is_folder: bool = False):
        ...
    def on_list_change_event(self, event: omni.client.impl._omniclient.ListEvent, entry: omni.client.impl._omniclient.ListEntry) -> bool:
        """
        
                Handle ListEvent changes, should update this item's children list with the corresponding ListEntry.
        
                Args:
                    event (:obj:`omni.client.ListEvent`): One of of {UNKNOWN, CREATED, UPDATED, DELETED, METADATA, LOCKED, UNLOCKED}.
                    entry (:obj:`omni.client.ListEntry`): Updated entry as defined by omni.client.
        
                
        """
    def populate_async(self, callback_async: typing.Callable, timeout: float = 10.0) -> typing.Any:
        """
        
                Populate current item asynchronously if not already. Overrides base method.
        
                Args:
                    callback_async (Callable): Function signature is void callback(result, children: [FileBrowserItem]),
                        where result is an Exception type upon error.
                    timeout (float): Time out duration on failed server connections. Default 10.0.
        
                Returns:
                    Any: Result of executing callback.
        
                
        """
    @property
    def readable(self) -> bool:
        """
        
                Return True if the item is readable.
                
        """
    @property
    def writeable(self) -> bool:
        """
        
                Return True if the item is writable.
                
        """
class FileSystemItemFactory:
    """
    
        Factory to create :obj:`FileSystemItem` instances.
        
    """
    @staticmethod
    def create_entry_item(*args, **kwargs):
        ...
    @staticmethod
    def create_group_item(*args, **kwargs):
        ...
    @staticmethod
    def create_omni_entry_item(*args, **kwargs):
        ...
class FileSystemModel(omni.kit.widget.filebrowser.model.FileBrowserModel):
    """
    
        A Filebrowser model class for navigating a the local filesystem in a Filebrowser view.
        Sub-classed from :obj:`FileBrowserModel`.
    
        Args:
            name (str): Name of root item..
            root_path (str): Root path. If None, then create empty model. Default "C:".
    
        Keyword Args:
            drop_fn (Callable): Function called to handle drag-n-drops. Function signature:
                void drop_fn(dst_item: :obj:`FileBrowserItem`, src_item: :obj:`FileBrowserItem`)
            filter_fn (Callable): This handler should return True if the given Filebrowser view item is visible,
                False otherwise. Function signature: bool filter_fn(item: :obj:`FileBrowserItem`)
            sort_by_field (str): Name of column by which to sort items in the same folder. Default "name".
            sort_ascending (bool): Sort in ascending order. Default True.
        
    """
    def __init__(self, name: str, root_path: str = 'C:', **kwargs):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.filebrowser-2.10.52+d02c707b/icons')
