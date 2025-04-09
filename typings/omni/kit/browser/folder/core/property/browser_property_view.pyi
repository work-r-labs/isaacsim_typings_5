from __future__ import annotations
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.browser.folder.core.property.browser_property_delegate import BrowserPropertyDelegate
from omni import ui
__all__ = ['BrowserPropertyDelegate', 'BrowserPropertyView', 'FileDetailItem', 'ui']
class BrowserPropertyView:
    """
    
        View to show properties of an item from the browser.
        This view represents a container (frame) into which the delegates
        registered with class BrowserPropertyDelegate will be added.
        
    """
    def __init__(self, property_delegates: typing.List[omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate] = list(), style: typing.Optional[dict] = None):
        ...
    def _build_ui(self):
        ...
    def destroy(self):
        ...
    def show(self, detail_items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]):
        """
        Various aspects of an item's properties can be shown by different delegates.
                The delegates that accept the item will be shown, and the others will be hidden.
        """
    @property
    def visible(self) -> bool:
        ...
    @visible.setter
    def visible(self, value) -> None:
        ...
