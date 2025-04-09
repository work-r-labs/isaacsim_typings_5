from __future__ import annotations
import asyncio as asyncio
import carb as carb
from itertools import chain
import json as json
import omni as omni
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_model import AbstractBrowserModel
from omni.kit.browser.folder.core.models.folder_browser_data import AbstractBrowserFolder
from omni.kit.browser.folder.core.models.folder_browser_data import BrowserFile
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCategoryItem
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCollectionItem
import os as os
import time as time
import toml as toml
import traceback as traceback
import typing
__all__ = ['AbstractBrowserFolder', 'AbstractBrowserModel', 'BrowserFile', 'CategoryItem', 'FileDetailItem', 'FileSystemFolder', 'FolderBrowserModel', 'FolderCategoryItem', 'FolderCollectionItem', 'PERSISTENT_SETTING_PREFIX', 'REMOTE_FOLDER_PREFIX', 'asyncio', 'carb', 'chain', 'json', 'omni', 'os', 'time', 'toml', 'traceback']
class FolderBrowserModel(omni.kit.browser.core.models.browser_model.AbstractBrowserModel):
    """
    
        Represents the browser model for folders.
    
        Keyword Args:
            filter_file_suffixes (Optional[List[str]]): List of file suffixes. Files with suffix not in this list will be ignored.
                Default is None, means all file suffixes will appear.
            ignore_folder_names (Optional[List[str]]): List of folder names. Folder with name in this list will be ignored.
                Default is None, means all folders will appear.
            show_empty_folders (bool): If true, show empty folders (no files in the folder). Otherwise, hide empty folders. Default is False.
            show_summary_folder (bool): If true, show a summary folder (named "ALL") with all files in all folders.
                Otherwise, donot show such a folder. Default is True.
            setting_folders (Optional[str]): Setting path to save/load root folders
            create_file_object_fn (callable): Function called when creating a file object. Default is creating a BrowserFile. Function siginature:
                Optional[BrowserFile] create_file_object_fn(url: str)
            timeout (Optional[float]): Number of seconds to wait for to list/reading from folder. If timeout is None, block until the future completes. Default is 5.
            category_tree_mode (bool): Show collections/categories in treeview mode
            local_cache_file(str):  Define the local cache file name for the model to be cached locally. If it is None, no local file cache will be stored.
            run_warmup (bool): If run in warmup. Default False.
            return None
    
        Overridden functions:
            bool filter_file(url: str): Determines a file will appear or not. Return true if appear, otherwise ingored.
                Default check file suffix with keyword args filter_file_suffixes.
                Args:
                    url (str): Url of file.
            void execute(self, item: FileDetailItem): Execute a file.
                Args:
                    item: File detail item to be executed.
            void sort_items(items: List[Union[FolderCollectionItem, FolderCollectionItem, DetailItem]]): Sort kinds of browser items.
                Default sort by name.
                Args:
                    items (List[Union[FolderCollectionItem, FolderCollectionItem, DetailItem]]): List of browser items to be sorted.
            FolderCollectionItem create_collection_item(folder: AbstractBrowserFolder):  Create a collection item from a folder.
                Args:
                    folder (AbstractBrowserFolder): Folder object to create collection item
            FolderCategoryItem create_category_item(folder: AbstractBrowserFolder): Create a category item from a folder.
                Args:
                    folder (AbstractBrowserFolder): Folder object to create category item
            Union[FileDetailItem, List[FileDetailItem] create_detail_item(file: BrowserFile): Create detail item(s) from a file
                Args:
                    file (BrowserFile): File object to create detail item
            AbstractBrowserFolder create_folder_object(*args, **kwargs): Create folder object when a root folder appended.
                Args and keyword args: please refer to FileSystemFolder
        
    """
    COUNT_LOADING: typing.ClassVar[str] = '...'
    COUNT_TIMEOUT: typing.ClassVar[str] = 'Timeout'
    SUMMARY_FOLDER_NAME: typing.ClassVar[str] = 'All'
    def _FolderBrowserModel__clear_folder_cache(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> None:
        ...
    def _FolderBrowserModel__get_folder_count(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> int:
        ...
    def _FolderBrowserModel__on_server_connected(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, result: bool) -> None:
        ...
    def _FolderBrowserModel__warmup(self):
        ...
    def __init__(self, filter_file_suffixes: typing.Optional[typing.List[str]] = None, ignore_folder_names: typing.Optional[typing.List[str]] = None, show_empty_folders: bool = False, show_summary_folder: bool = True, setting_folders: typing.Optional[str] = None, create_file_object_fn: callable = None, hide_file_without_thumbnails: bool = False, show_category_subfolders: bool = False, timeout: typing.Optional[float] = 5.0, category_tree_mode: bool = False, local_cache_file: str = None, run_warmup: bool = False, ignore_sub_folder_with_files: bool = False, custom_folders_setting: typing.Optional[str] = None):
        ...
    def _create_folder_object_by_url(self, name: str, url: str, **kwargs) -> omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder:
        ...
    def _get_folder_detail_items(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]:
        """
        Get list of detail items from a folder
        """
    def _load_data_from_json(self, check_only: bool = False):
        ...
    def _load_folder_from_json(self, data: typing.Dict, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder):
        ...
    def _on_custom_folders_changed(self, item, event):
        """
        
                Remove and Add folders that change between updates
                
        """
    def _on_folder_traversed(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, loading_completed = True, updated: bool = True) -> None:
        """
        Callback when folder traverse done
        """
    def _run(self):
        ...
    def _save_data_to_json(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder):
        ...
    def _save_folder_to_json(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, parent: typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder] = None) -> typing.Dict:
        ...
    def _save_root_folders(self):
        ...
    def append_root_folder(self, url: str, name: typing.Optional[str] = None, save: bool = True, sync: bool = True) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder]:
        """
        
                Append a root folder.
                Return FileSystemFolder object is appended, otherwise None means url already exists.
                Args:
                    url (str): Url of folder
                    name (Optional[str]): Name of folder. Default is None, means use last directory name as collection name.
                    save (bool): True to save current root folder to settings if setting path defined. False means nothing saved.
                
        """
    def create_category_item(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, parent: typing.Optional[omni.kit.browser.core.models.browser_item.CategoryItem] = None) -> omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem:
        """
        
                Create a category item from a folder.
                Args:
                    folder (AbstractBrowserFolder): Folder object to create category item
                
        """
    def create_collection_item(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem:
        """
        
                Create a collection item from a folder.
                Args:
                    folder (AbstractBrowserFolder): Folder object to create collection item
                
        """
    def create_detail_item(self, file: omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile) -> typing.Union[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem, typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]]:
        """
        
                Create detail item(s) from a file.
                A file may includs multi detail items.
                Args:
                    file (BrowserFile): File object to create detail item(s)
                
        """
    def create_folder_object(self, *args, **kwargs) -> omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder:
        """
        
                Create a folder object when a root folder appended. Default using FileSystemFolder.
                User could overridden to create own folder object for special usage.
                Args and keyword args please reference to FileSystemFolder.
                
        """
    def destroy(self):
        ...
    def filter_file(self, url: str) -> bool:
        """
        
                Check a file if valid or not.
                Return true if valid, otherwise false.
                If filter_file_suffixes not defined, always valid. Otherwise only valid if in valid_file_suffixed.
                Args:
                    url (str): Url of file.
                
        """
    def folder_changed(self, item: typing.Union[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile, NoneType]) -> None:
        """
        
                Notify folder or file changed.
                Args:
                    item (Union[AbstractBrowserFolder, BrowserFile]): Changed folder or file object.
                
        """
    def get_category_items(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        """
        Override to get list of category items
        """
    def get_collection_items(self) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem]:
        """
        Override to get list of collection items
        """
    def get_detail_items(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]:
        """
        Override to get list of detail items
        """
    def get_folder_item(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder) -> omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem:
        ...
    def get_root_folder(self, url: str) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder]:
        """
        
                Find a root folder
                Return folder object if succeeded, otherwise False.
                Args:
                    url (str): Url of root folder to find.
                
        """
    def process_root_folder(self, root_folder: str, sync: bool = True) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder]:
        """
        
                Process a root folder name and url and add it to the list of root folders.
        
                Args:
                    root_folder: Name of root folder with optional prepended collection name.
                
        """
    def register_folder(self, url: str, name: typing.Optional[str] = None) -> None:
        """
        
                Register a folder path with the model.
                Args:
                    url (str): Url of folder
                    name (Optional[str]): Name of folder. Default is None.
                
        """
    def remove_collection(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem) -> bool:
        ...
    def remove_root_folder(self, url: str) -> bool:
        """
        
                Remove a root folder
                Return True if succeeded, otherwise False.
                Args:
                    url (str): Url of root folder to be removed.
                
        """
    def sort_items(self, items: typing.List[typing.Union[omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem, omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]]) -> None:
        """
        
                Sort kinds of browser items by name.
                Args:
                    items (List[Union[FolderCollectionItem, FolderCollectionItem, FileDetailItem]]): List of browser items to be sorted.
                
        """
    def start_traverse(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder, force: bool = False):
        ...
    def unregister_folder(self, url: str) -> None:
        """
        
                Unregister a folder path with the model when finished with it.
                Args:
                    url (str): Url of folder
                
        """
PERSISTENT_SETTING_PREFIX: str = '/persistent'
REMOTE_FOLDER_PREFIX: str = 'omniverse://'
