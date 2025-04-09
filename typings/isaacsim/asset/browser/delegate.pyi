from __future__ import annotations
import asyncio as asyncio
import carb as carb
from isaacsim.asset.browser.context_menu import ContextMenu
import isaacsim.asset.browser.model
from isaacsim.asset.browser.model import AssetBrowserModel
import omni as omni
from omni.kit.browser.core import create_drop_helper
from omni.kit.browser.core.models.browser_item import DetailItem
from omni.kit.browser.folder.core.widgets.folder_detail_delegate import FolderDetailDelegate
from omni import ui
import pathlib
from pathlib import Path
__all__ = ['AssetBrowserModel', 'AssetDetailDelegate', 'CURRENT_PATH', 'ContextMenu', 'DetailItem', 'FolderDetailDelegate', 'ICON_PATH', 'Path', 'asyncio', 'carb', 'create_drop_helper', 'omni', 'ui']
class AssetDetailDelegate(omni.kit.browser.folder.core.widgets.folder_detail_delegate.FolderDetailDelegate):
    """
    
        Delegate to show asset item in detail view
        Args:
            model (AssetBrowserModel): Asset browser model
        
    """
    def __init__(self, model: isaacsim.asset.browser.model.AssetBrowserModel):
        ...
    def _on_drop(self, url, target, viewport_name, context_name):
        ...
    def _on_drop_accepted(self, url):
        ...
    def destroy(self):
        ...
    def get_thumbnail(self, item) -> str:
        """
        Set default sky thumbnail if thumbnail is None
        """
    def on_drag(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> str:
        """
        Could be dragged to viewport window
        """
    def on_right_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        Show context menu
        """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.asset.browser/isaacsim/asset/browser')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.asset.browser/icons')
