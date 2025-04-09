from __future__ import annotations
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.widgets.category_delegate import CategoryDelegate
from omni import ui
import omni.ui._ui
__all__ = ['CategoryDelegate', 'CategoryItem', 'CategoryView', 'ui']
class CategoryView(omni.ui._ui.TreeView):
    """
    
        TreeView to represent categories.
        Keyword Args:
            delegate (CatetoryDelegate): delegate object to represent category item. Default using CategoryDelegate
            on_category_selected_fn (func): Function called when category item selected (None if nothing selected). Default is None.
                Function signature: void on_category_selected_fn(item: CategoryItem)
        
    """
    def __init__(self, model, delegate = ..., on_category_selected_fn = None):
        ...
    def _on_selection_changed(self, selections: typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]):
        ...
