from __future__ import annotations
import asyncio as asyncio
import carb as carb
from datetime import datetime
import omni as omni
from omni.kit.widget.filebrowser.filesystem_model import FileSystemItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
from omni.kit.window.filepicker.utils import get_user_folders_dict
from omni import ui
import os as os
import pathlib
import platform as platform
import traceback as traceback
import typing
from typing import Any
__all__: list[str] = ['Any', 'CollectionItem', 'FileBrowserItemFields', 'FileSystemCollectionItem', 'FileSystemItem', 'ICON_PATH', 'asyncio', 'carb', 'datetime', 'get_user_folders_dict', 'omni', 'os', 'platform', 'traceback', 'ui']
class FileSystemCollectionItem(omni.kit.window.filepicker.collections.collection_item.CollectionItem):
    def __init__(self):
        """
        
                Collection for local drives and mounted folders.
                
        """
    def accept_url(self, url: str) -> bool:
        """
        
                Check if the url is accepted by the collection.
        
                Args:
                    url (str): Url to check.
        
                Returns:
                    bool: True if the url is accepted, False otherwise.
                
        """
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.widget.filebrowser.filesystem_model.FileSystemItem]:
        """
        
                Create a connection item.
        
                Args:
                    name (str): Name of the connection.
                    path (str): Path of the connection.
                    is_folder (bool): Whether the connection is a folder.
        
                Returns:
                    :obj:`FileSystemItem`: The created connection item.
                
        """
    def mount_user_folders(self, folders: typing.Dict[str, str]) -> None:
        """
        
                Mounts given set of user folders under the local collection.
        
                Args:
                    folders (dict): Name, path pairs.
        
                
        """
    def populate_children_async(self) -> typing.Any:
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
