from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.browser.core.widgets.search_bar import OptionMenuDescription
from omni import ui
__all__ = ['ASSETS_GUIDE_URL', 'DOCS_URL', 'FolderOptionsMenu', 'OptionMenuDescription', 'asyncio', 'carb', 'omni', 'ui']
class FolderOptionsMenu(omni.kit.browser.folder.core.widgets.options_menu.FolderOptionsMenu):
    """
    
        Represent options menu used in SimReady browser.
        
    """
    def __init__(self, *args, **kwargs):
        ...
    def _assets_check_success_window(self):
        ...
    def _assets_check_window(self):
        ...
    def _menu_callback(self):
        ...
    def _open_browser(self, path):
        ...
    def _set_defaults(self):
        ...
    def destroy(self) -> None:
        ...
    def set_add_collection_fn(self, on_add_collection_fn: callable) -> None:
        ...
ASSETS_GUIDE_URL: str = 'https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_faq.html#setting-the-default-nuc-short-server'
DOCS_URL: str = 'https://docs.omniverse.nvidia.com'
