from __future__ import annotations
import copy as copy
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_item import DetailItem
import omni.kit.browser.core.widgets.browser_widget
from omni.kit.browser.core.widgets.browser_widget import BrowserWidget
from omni.kit.browser.core.widgets.tree_category_delegate import TreeCategoryDelegate
__all__ = ['BrowserWidget', 'CategoryItem', 'CollectionItem', 'DetailItem', 'TREE_UI_STYLES', 'TreeBrowserWidget', 'TreeCategoryDelegate', 'copy']
class TreeBrowserWidget(omni.kit.browser.core.widgets.browser_widget.BrowserWidget):
    def __init__(self, *args, **kwargs):
        ...
    def _on_model_item_changed(self, item: typing.Union[omni.kit.browser.core.models.browser_item.CollectionItem, omni.kit.browser.core.models.browser_item.CategoryItem, omni.kit.browser.core.models.browser_item.DetailItem]) -> None:
        ...
TREE_UI_STYLES: dict = {'TreeView': {'background_selected_color': 'shade:4280821800'}, 'TreeView.Frame': {'padding': 8}, 'TreeView.Item.Name': {'color': 'shade:4286743170;light=4292927712'}, 'TreeView.Item.Name:selected': {'color': 'shade:4293105444;light=4291137818'}, 'TreeView.Item.Count:selected': {'color': 'shade:4286743170;light=4292927712'}}
