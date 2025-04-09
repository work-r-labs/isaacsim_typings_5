from __future__ import annotations
from functools import partial
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import DetailItem
import omni.kit.browser.core.models.browser_model
from omni.kit.browser.core.models.browser_model import AbstractBrowserModel
from omni import ui
import omni.ui._ui
__all__ = ['AbstractBrowserModel', 'DetailDelegate', 'DetailItem', 'partial', 'ui']
class DetailDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate to represent detail item.
        Keyword args:
            model: Browser model. Used to execute detail item when double click. Default is None.
        Overridden functions:
            str get_thumbnail(item: DetailItem): Function returns thumbnail url when the delegate asks it.
                Default using thumbnail defined in detail item.
            str get_label(item: DetailItem): Function returns label string when the delegate asks it.
                Default using name defined in detail item. Label will be invisible if returns None.
            int get_label_height(item: DetailItem): Function return label height when display item label. Default is 20.
            str get_tooltip(item: DetailItem): Function returns tooltip string when the detail delegate asks it.
            void on_click(item: DetailItem): Function called when clicked on the detail delegate.
            void on_right_click(item: DetailItem): Function called when right clicked on the detail delegate.
            void on_double_click(item: DetailItem) Function called when double clicked on the detail delegate. Default to execute the detail item.
            str on_drag(item: DetailItem): Function called when dragging the detail delegate.
            void build_thumbnail(item: DetailItem): Function called when drarwing thumbnail
        
    """
    def __init__(self, model: omni.kit.browser.core.models.browser_model.AbstractBrowserModel = None):
        ...
    def _build_label(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> omni.ui._ui.Label:
        """
        
                Display label per detail item
                Args:
                    item (DetailItem): detail item to display
                
        """
    def _clean_cached_widgets(self):
        ...
    def _on_mouse_double_clicked(self, btn: int, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _on_mouse_pressed(self, btn: int, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _single_item_changed(self, item: omni.kit.browser.core.models.browser_item.DetailItem):
        ...
    def build_branch(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.DetailItem, column_id: int = 0, level: int = 0, expanded: bool = False):
        """
        
                Create a branch widget that opens or closes subtree
                Args:
                    model (AbstractItemModel): Detail data model
                    item (CategoryItem): Detail item
                    column_id (int): ignore
                    level (int): ignore
                    expand (int): ignore
                
        """
    def build_thumbnail(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> typing.Optional[omni.ui._ui.Image]:
        """
        
                Display thumbnail per detail item
                Args:
                    item (DetailItem): detail item to display
                
        """
    def build_widget(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.DetailItem, index: int = 0, level: int = 0, expand: bool = False):
        """
        
                Create a widget per detail item
                Args:
                    model (AbstractItemModel): Detail data model
                    item (DetailItem): Detail item
                    index (int): ignore
                    level (int): ignore
                    expand (int): ignore
                
        """
    def destroy(self):
        """
        
                Clean up.
                
        """
    def get_label(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> typing.Optional[str]:
        """
        
                Returns label string of detail item when the delegate asks it.
                Returns None means do not display label.
                Default using item name
                Args:
                    item (DetailItem): detail item to display
                
        """
    def get_label_height(self) -> int:
        ...
    def get_thumbnail(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> typing.Optional[str]:
        """
        
                Returns thumbnail of detail item when the delegate asks it.
                Returns None means do not display thumbnail.
                Default using thumbnail defined in detail item.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def get_tooltip(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> typing.Optional[str]:
        """
        
                Returns tooltil of detail item when the delegate asks it.
                Returns None means do not display tooltip.
                Default is None.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def item_changed(self, model: omni.ui._ui.AbstractItemModel, item: typing.Optional[omni.kit.browser.core.models.browser_item.DetailItem]) -> None:
        """
        
                Update the widget when detail item changed.
                Now will update detail lable text and thumbail url.
                Args:
                    model (AbstractItemModel): Detail data model. Ignored now.
                    item (DetailItem): Detail item. None to change all items.
                
        """
    def on_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        
                Function called when clicking on the detail delegate.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def on_double_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        
                Function called when double clicking on the detail delegate.
                Default to execute this item
                Args:
                    item (DetailItem): detail item to display
                
        """
    def on_drag(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> str:
        """
        
                Function called when dragging on the detail delegate. Used to create widgets for dragged item.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def on_hover(self, item: omni.kit.browser.core.models.browser_item.DetailItem, hovered: bool) -> None:
        """
        
                Function called when hovering on the detail delegate.
                Args:
                    item (DetailItem): detail item to display
                    hovered (bool): hovered not not
                
        """
    def on_multiple_drag(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> str:
        """
        
                Function called when dragging on the detail delegate with other items. Default same as on_drag.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def on_right_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        
                Function called when right clicking on the detail delegate.
                Args:
                    item (DetailItem): detail item to display
                
        """
    def set_drag_fn(self, drag_fn: typing.Callable[[omni.kit.browser.core.models.browser_item.DetailItem], str]) -> None:
        ...
