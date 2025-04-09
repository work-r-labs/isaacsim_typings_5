from __future__ import annotations
import carb as carb
from isaacsim.core.utils.stage import open_stage
import omni as omni
from omni.kit.browser.core.models.browser_item import DetailItem
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
from omni.kit.browser.folder.core.models.tree_folder_browser_model import TreeFolderBrowserModel
import os as os
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
__all__ = ['AssetBrowserModel', 'DetailItem', 'FileSystemFolder', 'SETTING_FOLDER', 'Sdf', 'Tf', 'TreeFolderBrowserModel', 'Usd', 'carb', 'omni', 'open_stage', 'os']
class AssetBrowserModel(omni.kit.browser.folder.core.models.tree_folder_browser_model.TreeFolderBrowserModel):
    """
    
        Represent asset browser model
        
    """
    def __init__(self, *args, **kwargs):
        ...
    def _make_prim_path(self, stage: pxr.Usd.Stage, url: str, prim_path: pxr.Sdf.Path = None, prim_name: str = None):
        """
        Make a new/unique prim path for the given url
        """
    def create_folder_object(self, name: str, url: str, **kwargs) -> omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder:
        """
        
                Create a folder object when a root folder appended. Default using FileSystemFolder.
                User could overridden to create own folder object for special usage.
                Args and keyword args please reference to FileSystemFolder.
                
        """
    def execute(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        
                action when double clicked on an item: open the original file
                
        """
SETTING_FOLDER: str = '/exts/isaacsim.asset.browser/folders'
