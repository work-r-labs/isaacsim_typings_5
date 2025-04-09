from __future__ import annotations
import asyncio as asyncio
import carb as carb
from isaacsim.examples.browser.context_menu import ContextMenu
import isaacsim.examples.browser.model
from isaacsim.examples.browser.model import ExampleBrowserModel
import omni as omni
from omni.kit.browser.core import create_drop_helper
from omni.kit.browser.core.models.browser_item import DetailItem
from omni.kit.browser.folder.core.widgets.folder_detail_delegate import FolderDetailDelegate
from omni import ui
import pathlib
from pathlib import Path
__all__ = ['AssetDetailDelegate', 'CURRENT_PATH', 'ContextMenu', 'DetailItem', 'ExampleBrowserModel', 'FolderDetailDelegate', 'ICON_PATH', 'Path', 'asyncio', 'carb', 'create_drop_helper', 'omni', 'ui']
class AssetDetailDelegate(omni.kit.browser.folder.core.widgets.folder_detail_delegate.FolderDetailDelegate):
    """
    
        Delegate to show asset item in detail view
        Args:
            model (ExampleBrowserModel): Example browser model
        
    """
    def __init__(self, model: isaacsim.examples.browser.model.ExampleBrowserModel):
        ...
    def _on_drop(self, url, target, viewport_name, context_name):
        ...
    def _on_drop_accepted(self, url):
        ...
    def destroy(self):
        ...
    def on_drag(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> str:
        """
        Could be dragged to viewport window
        """
    def on_right_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        Show context menu
        """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.examples.browser/isaacsim/examples/browser')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.examples.browser/icons')
