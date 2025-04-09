from __future__ import annotations
import omni.kit.browser.core.widgets.tree_category_delegate
from omni.kit.browser.core.widgets.tree_category_delegate import TreeCategoryDelegate
import omni.kit.browser.folder.core.models.folder_browser_item
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCategoryItem
import omni.kit.browser.folder.core.models.tree_folder_browser_model
from omni.kit.browser.folder.core.models.tree_folder_browser_model import TreeFolderBrowserModel
from omni.kit.browser.folder.core.widgets.context_menu import ContextMenu
__all__ = ['ContextMenu', 'FolderCategoryDelegate', 'FolderCategoryItem', 'TreeCategoryDelegate', 'TreeFolderBrowserModel']
class FolderCategoryDelegate(omni.kit.browser.core.widgets.tree_category_delegate.TreeCategoryDelegate):
    def __init__(self, **kwargs):
        ...
    def _get_collect_urls(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem) -> typing.Optional[typing.List[str]]:
        """
        
                Query folder category local collected urls.
                Args:
                    item (FolderCategoryItem): category item to query
                Return:
                    collected urls if found. Else None.
                
        """
    def _on_item_right_click(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem):
        """
        Show category item's menu
        """
    def bind_model(self, model: omni.kit.browser.folder.core.models.tree_folder_browser_model.TreeFolderBrowserModel):
        ...
    def get_count(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem) -> str:
        ...
