from __future__ import annotations
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_item import DetailItem
import omni.kit.browser.folder.core.models.folder_browser_data
from omni.kit.browser.folder.core.models.folder_browser_data import AbstractBrowserFolder
from omni.kit.browser.folder.core.models.folder_browser_data import BrowserFile
__all__ = ['AbstractBrowserFolder', 'BrowserFile', 'CategoryItem', 'CollectionItem', 'DetailItem', 'FileDetailItem', 'FolderCategoryItem', 'FolderCollectionItem']
class FileDetailItem(omni.kit.browser.core.models.browser_item.DetailItem):
    """
    
        Represents a single file detail item.
        Args:
            name (str): file name.
            url (str): file url.
            file (BrowserFile): file object linked to this item.
            thumbnail (Optional[str]): thumbnail url of file. Default is None.
        
    """
    def __init__(self, name: str, url: str, file: omni.kit.browser.folder.core.models.folder_browser_data.BrowserFile, thumbnail: typing.Optional[str] = None):
        ...
class FolderCategoryItem(omni.kit.browser.core.models.browser_item.CategoryItem):
    """
    
        Represents a single folder category item.
        Args:
            name (str): folder name.
            count (int): count of files in this folder.
            folder (AbstractBrowserFolder): folder object linked to this item.
            parent (CategoryItem): parent category item, to get sibling info.
            is_last_child (bool): Is last child of siblings, for drawing purposes.
        
    """
    def __init__(self, name: str, count: int, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder, parent: typing.Optional[omni.kit.browser.core.models.browser_item.CategoryItem] = None, is_last_child: typing.Optional[bool] = False):
        ...
class FolderCollectionItem(omni.kit.browser.core.models.browser_item.CollectionItem):
    """
    
        Represents a single folder collection item.
        Args:
            name (str): collection name.
            url (str): folder url.
            folder (AbstractBrowserFolder): folder object linked to this item.
        
    """
    def __init__(self, name: str, url: str, folder: omni.kit.browser.folder.core.models.folder_browser_data.AbstractBrowserFolder):
        ...
