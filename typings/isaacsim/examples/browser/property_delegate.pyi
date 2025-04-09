from __future__ import annotations
import omni.kit.browser.folder.core.models.folder_browser_item
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
import omni.kit.browser.folder.core.property.browser_property_delegate
from omni.kit.browser.folder.core.property.browser_property_delegate import BrowserPropertyDelegate
from omni import ui
import typing
__all__ = ['BrowserPropertyDelegate', 'EmptyPropertyDelegate', 'FileDetailItem', 'MultiPropertyDelegate', 'PropAssetPropertyDelegate', 'ui']
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
class MultiPropertyDelegate(omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate):
    """
    
        A delegate to show when multiple items are selected.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def accepted(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> bool:
        """
        BrowserPropertyDelegate method override
        """
    def build_widgets(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        """
        BrowserPropertyDelegate method override
        """
class PropAssetPropertyDelegate(omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate):
    """
    
        A delegate to show properties of assets of type Prop.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _build_thumbnail(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        """
        Builds thumbnail frame and resizes
        """
    def _on_thumbnail_frame_size_changed(self):
        ...
    def accepted(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> bool:
        """
        BrowserPropertyDelegate method override
        """
    def build_widgets(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        ...
