from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_item import DetailItem
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
from omni.kit.browser.folder.core.models.tree_folder_browser_model import TreeFolderBrowserModel
import os as os
from pxr import Sdf
from pxr import Tf
from pxr import Usd
__all__ = ['CategoryItem', 'CollectionItem', 'DetailItem', 'Example', 'ExampleBrowserModel', 'ExampleCategoryItem', 'ExampleDetailItem', 'FileSystemFolder', 'SETTING_FOLDER', 'Sdf', 'Tf', 'TreeFolderBrowserModel', 'Usd', 'carb', 'omni', 'os']
class Example:
    def __init__(self, name: str = '', execute_entrypoint: callable = None, ui_hook: callable = None, category: str = '', thumbnail: typing.Optional[str] = None):
        ...
class ExampleBrowserModel(omni.kit.browser.folder.core.models.tree_folder_browser_model.TreeFolderBrowserModel):
    """
    
        Represent asset browser model
        
    """
    def __init__(self, *args, **kwargs):
        ...
    def deregister_example(self, name: str, category: str):
        ...
    def execute(self, item: ExampleDetailItem) -> None:
        ...
    def get_category_items(self, item: omni.kit.browser.core.models.browser_item.CollectionItem) -> typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]:
        """
        Override to get list of category items
        """
    def get_detail_items(self, item: ExampleCategoryItem) -> typing.List[isaacsim.examples.browser.model.ExampleDetailItem]:
        """
        Override to get list of detail items
        """
    def refresh_browser(self):
        ...
    def register_example(self, **kwargs):
        ...
class ExampleCategoryItem(omni.kit.browser.core.models.browser_item.CategoryItem):
    def __init__(self, name: str):
        ...
    def add_child(self, child_name: str):
        ...
class ExampleDetailItem(omni.kit.browser.core.models.browser_item.DetailItem):
    def __init__(self, example: Example):
        ...
SETTING_FOLDER: str = '/exts/isaacsim.examples.browser/folders'
