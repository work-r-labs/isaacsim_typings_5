from __future__ import annotations
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni import ui
import omni.ui._ui
__all__ = ['CategoryDelegate', 'CategoryItem', 'ui']
class CategoryDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate to represent category item.
        Args:
            teee_mode: Show categories in tree mode. Default flat mode (no branches)
        
    """
    def __init__(self, tree_mode: bool = False):
        ...
    def build_branch(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.CategoryItem, column_id: int = 0, level: int = 0, expanded: bool = False):
        """
        
                Create a branch widget that opens or closes subtree
                Args:
                    model (AbstractItemModel): Category data model
                    item (CategoryItem): Category item
                    column_id (int): ignore
                    level (int): ignore
                    expand (int): ignore
                
        """
    def build_widget(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.CategoryItem, index: int = 0, level: int = 0, expanded: bool = False):
        """
        
                Create a widget per catetory item
                Args:
                    model (AbstractItemModel): Category data model
                    item (CategoryItem): Category item
                    index (int): ignore
                    level (int): ignore
                    expand (int): ignore
                
        """
    def get_count(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> str:
        ...
    def get_label(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> str:
        ...
