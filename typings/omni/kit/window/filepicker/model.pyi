from __future__ import annotations
import asyncio as asyncio
from carb import log_warn
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.model import FileBrowserItem
import pathlib
import re as re
import urllib as urllib
__all__: list = ['FilePickerModel']
class FilePickerModel:
    """
    The model class for :obj:`FilePickerWidget`.
    """
    @staticmethod
    def is_local_path(path: str) -> bool:
        """
        Returns True if given path is a local path
        """
    def __init__(self, **kwargs):
        ...
    def _correct_filename_case(self, file: str) -> str:
        """
        
                Helper function to workaround problem of windows paths getting lowercased
        
                Args:
                    path (str): Raw path
        
                Returns:
                    str
        
                
        """
    def destroy(self):
        """
         Destructor 
        """
    def find_item_async(self, url: str, callback: typing.Callable = None) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
        
                Searches model for the given path and executes callback on found item.
        
                Args:
                    url (str): Url of item to search for.
                    callback (Callable):  Invokes this callback on found item or None if not found. Function signature is
                        void callback(item: FileBrowserItem)
        
                
        """
    def find_item_in_subtree_async(self, root: omni.kit.widget.filebrowser.model.FileBrowserItem, path: str) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
        
                Finds the given item in the current model recursively asynchronously.
        
                Args:
                    root (:obj: 'FileBrowserItem'): The root item to search.
                    path (str): Path of item to search for.
        
                Returns:
                    :obj: 'FileBrowserItem': item that has the path and under the root item.    
                
        """
    def find_item_with_callback(self, url: str, callback: typing.Callable = None):
        """
        
                Searches filebrowser model for the item with the given url. Executes callback on found item.
        
                Args:
                    url (str): Url of item to search for.
                    callback (Callable):  Invokes this callback on found item or None if not found. Function signature is
                        void callback(item: FileBrowserItem)
        
                
        """
    def get_badges(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> typing.List[typing.Tuple[str, str]]:
        """
        
                Returns fullpaths to badges for given item. Override this method to implement custom badges.
        
                Args:
                    item (:obj:`FileBrowseritem`): Item in question.
        
                Returns:
                    List[Tuple[str, str]]: Where each tuple is an (icon path, tooltip string) pair.
        
                
        """
    def get_icon(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, expanded: bool) -> str:
        """
        
                Returns fullpath to icon for given item. Override this method to implement custom icons.
        
                Args:
                    item (:obj:`FileBrowseritem`): Item in question.
                    expanded (bool): True if item is expanded.
        
                Returns:
                    str
        
                
        """
    def get_thumbnail(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> str:
        """
        
                Returns fullpath to thumbnail for given item.
        
                Args:
                    item (:obj:`FileBrowseritem`): Item in question.
        
                Returns:
                    str: Fullpath to the thumbnail file, None if not found.
        
                
        """
    def sanitize_path(self, path: str) -> str:
        """
        
                Helper function for normalizing a path that may have been copied and pasted int to browser
                bar. This makes the tool more resiliant to user inputs from other apps.
        
                Args:
                    path (str): Raw path
        
                Returns:
                    str
        
                
        """
    @property
    def collections(self) -> dict:
        """
        [:obj:`FileBrowseItem`]: The collections loaded for this widget
        """
    @collections.setter
    def collections(self, collections: dict):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
THUMBNAIL_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/data/thumbnails')
