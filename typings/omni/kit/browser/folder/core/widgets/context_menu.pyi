from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
__all__ = ['CONTEXT_MENU_STYLE', 'ContextMenu', 'carb', 'ui']
class ContextMenu(omni.ui._ui.Menu):
    """
    
        Context menu for folder browser's category item right click.
        
    """
    def __init__(self):
        ...
    def _collect(self):
        ...
    def show_menu(self):
        ...
CONTEXT_MENU_STYLE: dict  # value = {'Menu': {'background_color': 'context_menu_background_color', 'color': 'context_menu_text', 'border_radius': 2}, 'Menu.Item': {'background_color': 0, 'margin': 0}, 'Separator': {'background_color': 0, 'color': 'context_menu_separator'}}
