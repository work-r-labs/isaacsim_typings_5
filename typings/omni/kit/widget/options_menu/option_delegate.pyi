"""
This module provides a custom menu item delegate with additional spacing for use in UI menus.
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['OptionLabelMenuItemDelegate', 'ui']
class OptionLabelMenuItemDelegate(omni.ui._ui.MenuDelegate):
    """
    A delegate class for a normal menu item with an additional spacer at the end.
    
        This class inherits from ui.MenuDelegate and is specialized to provide a custom appearance
        for menu items in a UI. It includes a spacer at the end to ensure proper layout
        within the menu.
    
            Args:
                width (ui.Length): Menu item width.
    """
    def __init__(self, width: omni.ui._ui.Length = ...):
        """
        Initializer for OptionLabelMenuItemDelegate.
        """
    def build_item(self, item: omni.ui._ui.MenuItem):
        """
        Builds the menu item visual representation.
        
                Args:
                    item (ui.MenuItem): The menu item to build a visual for.
        """
    def build_widget(self, item: omni.ui._ui.MenuItem) -> None:
        """
        Builds the widget for the given menu item.
        
                Args:
                    item (ui.MenuItem): The menu item to create a widget for.
        """
