from __future__ import annotations
import carb as carb
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.notification_manager.extension import post_notification
from omni import ui
import omni.ui._ui
import os as os
import requests as requests
import toml as toml
from urllib.parse import unquote
__all__ = ['CONTEXT_MENU_STYLE', 'ContextMenu', 'FileDetailItem', 'carb', 'get_content_folder', 'os', 'post_notification', 'requests', 'toml', 'ui', 'unquote']
class ContextMenu(omni.ui._ui.Menu):
    """
    
        Context menu for asset browser.
        
    """
    def _ContextMenu__add_at_current_selection(self):
        ...
    def _ContextMenu__copy_url_link(self):
        ...
    def _ContextMenu__download_item(self, url):
        ...
    def _ContextMenu__replace_current_selection(self):
        ...
    def __init__(self):
        ...
    def _collect(self):
        ...
def get_content_folder():
    ...
CONTEXT_MENU_STYLE: dict  # value = {'Menu': {'background_color': 'context_menu_background_color', 'color': 'context_menu_text', 'border_radius': 2}, 'Menu.Item': {'background_color': 0, 'margin': 0}, 'Separator': {'background_color': 0, 'color': 'context_menu_separator'}}
