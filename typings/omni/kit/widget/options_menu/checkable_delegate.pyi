"""
This module provides a CheckableMenuItemDelegate class for creating checkable menu items with custom behavior in the Omni UI.
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['CheckableMenuItemDelegate', 'ui']
class CheckableMenuItemDelegate(omni.ui._ui.MenuDelegate):
    """
    Delegate for checkable menu item.
        A general checkable item includes a checked icon and item text.
    
        Args:
            checked (bool): If item is checked. Default False.
            width (ui.Length): Menu item width. Default ui.Fraction(1).
            enabled (bool): If item is enabled. Default True.
    """
    def __init__(self, checked: bool = False, width: omni.ui._ui.Length = ..., enabled: bool = True):
        """
        Constructor for CheckableMenuItemDelegate.
        """
    def _on_mouse_hovered(self, hovered: bool) -> None:
        ...
    def build_item(self, item: omni.ui._ui.MenuItem):
        """
        Builds the menu item with given properties.
        
                Args:
                    item (ui.MenuItem): The menu item to build.
        """
    def build_item_icon(self):
        """
        Builds the icon for the menu item.
        """
    def build_widget(self, item: omni.ui._ui.MenuItem) -> None:
        """
        Builds the widget for the menu item.
        
                Args:
                    item (ui.MenuItem): The menu item for which to build the widget.
        """
    def destroy(self):
        """
        Destroys the delegate and cleans up resources.
        """
    def get_icon_name(self):
        """
        Determines the icon name based on the item's state.
        
                Returns:
                    str: The name of the icon.
        """
    def on_triggered(self):
        """
        Callback method for when the menu item is triggered.
        """
    @property
    def checked(self) -> bool:
        """
        Gets the checked status of the menu item.
        
                Returns:
                    bool: The current checked status.
        """
    @checked.setter
    def checked(self, value: bool) -> None:
        """
        Sets the checked status of the menu item.
        
                Args:
                    value (bool): The new checked status to be set.
        """
    @property
    def enabled(self) -> bool:
        """
        Gets the enabled status of the menu item.
        
                Returns:
                    bool: The current enabled status.
        """
    @enabled.setter
    def enabled(self, value: bool) -> None:
        """
        Sets the enabled status of the menu item.
        
                Args:
                    value (bool): The new enabled status to be set.
        """
