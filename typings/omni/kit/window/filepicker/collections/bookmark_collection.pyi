from __future__ import annotations
from datetime import datetime
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.thumbnails import find_thumbnails_for_files_async
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
from omni import ui
import pathlib
import re as re
import typing
__all__: list = ['BookmarkItem', 'BookmarkCollectionItem']
class BookmarkCollectionItem(omni.kit.window.filepicker.collections.collection_item.CollectionItem):
    def __init__(self):
        ...
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.window.filepicker.collections.bookmark_collection.BookmarkItem]:
        ...
class BookmarkItem(omni.kit.widget.filebrowser.model.FileBrowserItem):
    _thumbnail_dict: typing.ClassVar[dict] = {}
    expandable: bool
    @staticmethod
    def is_bookmark_folder(path: str):
        """
        Helper method to check if a given path is a bookmark of a folder.
        """
    @staticmethod
    def is_local_path(path: str) -> bool:
        """
        Returns True if given path is a local path
        """
    def __init__(self, path: str, fields: typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItemFields] = None, is_folder: bool = True, name: typing.Optional[str] = None):
        ...
    def format_bookmark_path(self, path: str):
        """
        Helper method to generate a bookmark path from the given path.
        """
    def get_custom_thumbnails_for_folder_async(self) -> typing.Dict:
        """
        
                Returns the thumbnail dictionary for this (folder) item.
        
                Returns:
                    Dict: With children url's as keys, and url's to thumbnail files as values.
        
                
        """
    def on_list_change_event(self, event: omni.client.impl._omniclient.ListEvent, entry: omni.client.impl._omniclient.ListEntry) -> bool:
        """
        
                Handles ListEvent changes, should update this item's children list with the corresponding ListEntry.
        
                Args:
                    event (:obj:`omni.client.ListEvent`): One of of {UNKNOWN, CREATED, UPDATED, DELETED, METADATA, LOCKED, UNLOCKED}.
                    entry (:obj:`omni.client.ListEntry`): Updated entry as defined by omni.client.
        
                
        """
    def set_bookmark_path(self, path: str) -> None:
        """
        Sets the bookmark item path
        """
    @property
    def hideable(self) -> bool:
        ...
    @property
    def readable(self) -> bool:
        ...
    @property
    def writeable(self) -> bool:
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
