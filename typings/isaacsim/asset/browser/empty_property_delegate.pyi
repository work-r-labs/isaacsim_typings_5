from __future__ import annotations
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
import omni.kit.browser.folder.core.property.browser_property_delegate
from omni.kit.browser.folder.core.property.browser_property_delegate import BrowserPropertyDelegate
from omni import ui
import typing
__all__ = ['BrowserPropertyDelegate', 'EmptyPropertyDelegate', 'FileDetailItem', 'ui']
class EmptyPropertyDelegate(omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate):
    """
    
        A delegate to show when no asset selected.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def accepted(self, items: typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> bool:
        """
        BrowserPropertyDelegate method override
        """
    def build_widgets(self, items: typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        """
        BrowserPropertyDelegate method override
        """
