from __future__ import annotations
import abc as abc
import asyncio as asyncio
import carb as carb
import omni as omni
import os as os
from pathlib import Path
import re as re
__all__ = ['AbstractBrowserFolder', 'BrowserFile', 'FileSystemFile', 'FileSystemFolder', 'MAX_RETRY_COUNT', 'Path', 'THUMBNAIL_FULL_PATH', 'THUMBNAIL_PATH', 'THUMBNAIL_SIZE', 'abc', 'asyncio', 'carb', 'omni', 'os', 're']
class AbstractBrowserFolder:
    """
    
        Represents the abstract folder. Following functions need to be reimplemented:
            void start_traverse(): Start traverse folder to get sub folders and files
    
        Args:
            name (str): Folder name
            url (str): Folder url
    
        Keyword Args:
            ignore_folder_names (Optional[List[str]]): List of folder names. Sub folder with name in this list will be ignored.
                Default is None, means all folders will appear.
            filter_file_fn (callable): Determines a file will appear or not. Return true if appear, otherwise ingored. Default is None. Function signature:
                bool filter_file(url: str)
            on_traversed_fn (callable): Function to notify folder traverse done. Default is None. Function signature:
                void on_traversed_fn(folder: AbstractBrowserFolder)
            list_entry (Optional[omni.client.ListEntry]): folder list entry information. It is read while traversing, save for future usage. Default is None.
            timeout (Optional[float]): Number of seconds to wait for to list/reading from folder. If timeout is None, block until the future completes. Default is 5.
    
        Overridden functions:
            void start_traverse(): Start travserse to get all sub folders and filess in this folder.
                If traverse done, must set prepared = True and call on_traversed_fn to notify model.
        
    """
    def __init__(self, name: str, url: str, ignore_folder_names: typing.Optional[typing.List[str]] = None, filter_file_fn: callable = None, on_traversed_fn: callable = None, list_entry: typing.Optional[omni.client.impl._omniclient.ListEntry] = None, timeout: typing.Optional[float] = 5.0):
        ...
    def _filter_folder(self, folder_name: str) -> bool:
        """
        
                Filter folder by name.
                Args:
                    folder_name: Name of folder.
                Returns True if valid. Otherwise return False.
                
        """
    def _init_data(self) -> None:
        ...
    def _on_file_found_async(self, url: str) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile]:
        """
        Function when a new file found during traversing.
        """
    def _on_sub_folder_found_async(self, url: str, entry) -> typing.Optional[ForwardRef('AbstractBrowserFolder')]:
        """
        Function when a new sub folder found during traversing.
        """
    def create_file_object(self, url: str) -> BrowserFile:
        """
        
                Create file object.
                Args:
                    url: File Url.
                Return file object.
                
        """
    def destroy(self):
        ...
    def start_traverse(self) -> None:
        """
        Start traverse folder to get sub folders and files
        """
    @property
    def file_item_count(self) -> int:
        """
        Count of file items in this folder displayed in detail view
        """
class BrowserFile:
    """
    
        Represents a single file.
        Args:
            url (str): file url.
            thumbnail (Optional[str]): thumbnail url of file. Default is None.
        
    """
    def __init__(self, url: str, thumbnail: typing.Optional[str] = None):
        ...
    def equals(self, other: BrowserFile) -> bool:
        """
        
                Check if two file objects are same.
                Returns True means same otherwise False.
                
        """
    def get_default_thumbnail_url(self) -> str:
        """
        
                Get default thumbnail url.
                
        """
    def set_thumbnail(self, thumbnail_url: str) -> bool:
        """
        
                Check and set thumbnail.
                Args:
                    thumbnail (str): Url of thumbnail.
                Return True if the thumbnail belongs to this file, otherwise False.
                
        """
class FileSystemFile(BrowserFile):
    """
    
        Represents a single file system file.
        Args:
            url (str): file url.
            list_entry (Optional[omni.client.ListEntry]): file list entry information. It is read while traversing, save for future usage. Default is None.
            thumbnail (Optional[str]): thumbnail url of file. Default is None.
            thumbnail_list_entry ((Optional[omni.client.ListEntry]): thumbnail list entry information. It is read while traversing, save for future usage. Default is None.
        
    """
    def __init__(self, url: str, list_entry: typing.Optional[omni.client.impl._omniclient.ListEntry] = None, thumbnail: typing.Optional[str] = None, thumbnail_list_entry: typing.Optional[omni.client.impl._omniclient.ListEntry] = None):
        ...
class FileSystemFolder(AbstractBrowserFolder):
    """
    
        Represents a folder in file system. Could be local folder or folder on omniverse server.
        Kwargs:
            root (bool): If a root folder need to check connection status. Default False
            ignore_empty_folder (bool): Ignore empty folder. Default False
            ignore_file_without_thumbnail (bool): Ignore file without thumbnail. Default False
    
        Overridden functions:
            async bool start_traverse(): Start travserse to get all sub folders and filess in this folder.
                Notices: This is a coroutine and needs to be called in the correct way.
                for example, use await in other coroutine,or use asyncio.ensure_furture.
    
        Other args and Keyword args: Please refer to AbstractBrowserFolder.
        
    """
    def _FileSystemFolder__traverse_thumbnail(self, url: str, files: typing.List[omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile]):
        """
        
                List all thumbnails and assign to file
                
        """
    def __init__(self, *args, **kwargs):
        ...
    def _is_folder_updated(self):
        """
        
                Check if folder udpated after traverse.
                Changes in either files or sub folder means updated.
                
        """
    def _list_folder_async(self, url: str) -> typing.Optional[typing.Tuple[omni.client.impl._omniclient.ListEntry]]:
        """
        List files on a omniverse server folder
        """
    def _on_server_status_changed(self, url, status):
        ...
    def _on_traverse_async_done(self, loading_completed = True) -> None:
        """
        Callback when folder traverse done
        """
    def _traverse_folder_async(self, url: str, recurse: bool = True):
        """
        
                Traverse folder to list files with thumbnail and sub folders
                
        """
    def create_file_object(self, url: str) -> FileSystemFile:
        """
        
                Create file object.
                Args:
                    url: File Url.
                Return file object.
                
        """
    def create_folder_object(self, name: str, url: str, **kwargs) -> AbstractBrowserFolder:
        """
        
                Create a folder object when a sub folder found. Default using FileSystemFolder.
                User could overridden to create own folder object for special usage.
                Args and keyword args please reference to FileSystemFolder.
                
        """
    def destroy(self) -> None:
        ...
    def start_traverse(self, try_connect_nucleus: bool = True, on_connected_fn: typing.Callable[[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, bool], NoneType] = None) -> bool:
        """
        
                Start traverse folder to get sub folders and files
                Kwargs:
                    try_connect_nucleus (bool): Try connection to nucleus if not connected. Default True.
                    on_connected_fn (Callable): Callback function on connection result.
                Return True if traverse done. Otherwise False means waiting for connection result.
                
        """
MAX_RETRY_COUNT: int = 3
THUMBNAIL_FULL_PATH: str = '/.thumbs/256x256'
THUMBNAIL_PATH: str = '.thumbs'
THUMBNAIL_SIZE: int = 256
