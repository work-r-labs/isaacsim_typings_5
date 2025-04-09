from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import os as os
import toml as toml
from urllib.parse import unquote
__all__ = ['CONTEXT_MENU_STYLE', 'ContextMenu', 'carb', 'get_content_folder', 'os', 'toml', 'ui', 'unquote']
class ContextMenu(omni.ui._ui.Menu):
    """
    
        Context menu for asset browser.
        
    """
    def _ContextMenu__add_at_current_selection(self):
        ...
    def _ContextMenu__copy_url_link(self):
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
