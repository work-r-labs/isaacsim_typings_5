from __future__ import annotations
import asyncio as asyncio
import carb as carb
from itertools import chain
import omni as omni
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.folder.core.models.folder_browser_data import AbstractBrowserFolder
from omni.kit.browser.folder.core.models.folder_browser_data import BrowserFile
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCategoryItem
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCollectionItem
from omni.kit.browser.folder.core.models.folder_browser_model import FolderBrowserModel
import os as os
from unicodedata import category
__all__ = ['AbstractBrowserFolder', 'BrowserFile', 'CategoryItem', 'FileDetailItem', 'FileSystemFolder', 'FolderBrowserModel', 'FolderCategoryItem', 'FolderCollectionItem', 'TreeFolderBrowserModel', 'asyncio', 'carb', 'category', 'chain', 'omni', 'os']
class TreeFolderBrowserModel(omni.kit.browser.folder.core.models.folder_browser_model.FolderBrowserModel):
    def _TreeFolderBrowserModel__find_category_item_by_name(self, name: str, root_category_items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        ...
    def _TreeFolderBrowserModel__refresh_category_item(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem) -> None:
        ...
    def __init__(self, *args, **kwargs):
        ...
    def _create_category_item_chain(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, root_category_items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        ...
    def _create_folder_category_item(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        """
        
                Create category item for a folder.
                Return None if no sub folder and files in folder.
                Otherwise return created category item.
                
        """
    def _get_summary_detail_items(self) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]:
        ...
    def _load_file_from_json(self, data: typing.Dict, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile]:
        ...
    def _load_folder_from_json(self, data: typing.Dict, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder):
        ...
    def _on_folder_traversed(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, loading_completed = True, updated: bool = True) -> None:
        """
        
                Folder traversed,
                - Update category and detail widgets
                - Save data to cache
                
        """
    def _save_file_to_json(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, file: omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile) -> typing.Dict:
        ...
    def _save_folder_to_json(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, parent: typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder] = None) -> typing.Dict:
        ...
    def folder_changed(self, item: typing.Union[omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile, NoneType]) -> None:
        """
        
                Notify folder or file changed.
                Args:
                    item (Union[AbstractBrowserFolder, BrowserFile]): Changed folder or file object.
                
        """
    def get_category_items(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        """
        
                Create category item for every root folder.
                Also create category items for sub folders as children of parent category item.
                Summary category item will be created if required.
                
        """
    def get_collection_items(self) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem]:
        """
        Override to get list of collection items
        """
    def get_detail_items(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]:
        """
        Override to get list of detail items
        """
    def process_root_folder(self, root_folder: str, sync: bool = True) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder]:
        ...
    def remove_collection(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCollectionItem) -> bool:
        ...
