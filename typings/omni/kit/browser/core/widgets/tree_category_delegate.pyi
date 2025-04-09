from __future__ import annotations
import asyncio as asyncio
from functools import partial
from itertools import chain
import omni as omni
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.widgets.category_delegate import CategoryDelegate
from omni import ui
from omni.ui import scene as sc
import pathlib
__all__ = ['CategoryDelegate', 'CategoryItem', 'FULL_LINE_HEIGHT', 'ICON_PATH', 'TreeCategoryDelegate', 'VLine', 'asyncio', 'chain', 'omni', 'partial', 'sc', 'ui']
class TreeCategoryDelegate(omni.kit.browser.core.widgets.category_delegate.CategoryDelegate):
    """
    
        Delegate to represent category items in a hierarchical structure.
    
        Kwargs:
            hide_zero_count (bool): Hide category count if count is 0. Default False.
        
    """
    def __init__(self, hide_zero_count: bool = False, *args, **kwargs):
        ...
    def _on_category_item_click(self, item: omni.kit.browser.core.models.browser_item.CategoryItem, x, y, button, key_mod):
        ...
    def _on_item_right_click(self, item: omni.kit.browser.core.models.browser_item.CategoryItem):
        ...
    def build_branch(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.CategoryItem, column_id: int = 0, level: int = 0, expanded: bool = False):
        """
        
                Create a branch widget that opens or closes subtree
                Args:
                    model (AbstractItemModel): Category data model
                    item (CategoryItem): Category item
                    column_id (int): ignore
                    level (int): Level of the hierarchy the current item is at, from 0 to n.
                    expand (int): Indicates whether we will see child categories expanded or not.
                
        """
    def build_widget(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.CategoryItem, index: int = 0, level: int = 0, expanded: bool = False):
        """
        
                Create a widget per category item
                Args:
                    model (AbstractItemModel): Category data model
                    item (CategoryItem): Category item
                    index (int): ignore
                    level (int): ignore
                    expand (int): ignore
                
        """
    def draw_expanded_symbol(self, expanded: bool) -> None:
        ...
    def get_label(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> str:
        ...
class VLine(omni.ui._ui.Line):
    def __init__(self, half: bool = False):
        ...
FULL_LINE_HEIGHT: int = 20
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons')
