from __future__ import annotations
import asyncio as asyncio
from isaacsim.core.utils.stage import get_next_free_path
from isaacsim.core.utils.stage import open_stage
import omni as omni
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.browser.folder.core.property.browser_property_delegate import BrowserPropertyDelegate
from omni.kit.notification_manager.extension import post_notification
from omni import ui
import os as os
from pxr import Usd
import requests as requests
import typing
__all__ = ['BrowserPropertyDelegate', 'FileDetailItem', 'PropAssetPropertyDelegate', 'Usd', 'asyncio', 'get_next_free_path', 'omni', 'open_stage', 'os', 'post_notification', 'requests', 'ui']
class PropAssetPropertyDelegate(omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate):
    """
    
        A delegate to show properties of assets of type Prop.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _build_thumbnail(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        ...
    def _build_variant_options(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        ...
    def _on_thumbnail_frame_size_changed(self):
        ...
    def accepted(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> bool:
        """
        BrowserPropertyDelegate method override
        """
    def build_widgets(self, items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        ...
    def download_file(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        ...
    def load_as_reference(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        ...
    def open_asset(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem):
        ...
