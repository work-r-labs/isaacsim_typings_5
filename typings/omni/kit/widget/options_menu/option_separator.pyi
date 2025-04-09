"""
This module provides classes for creating separators with optional titles for option menus in Omniverse Kit.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import AbstractOptionItem
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'OptionSeparator', 'OptionSeparatorMenuItem', 'SeparatorDelegate', 'ui']
class OptionSeparator(omni.kit.widget.options_menu.option_item.AbstractOptionItem):
    """
    A simple option item represents a separator in menu item.
    
        Args:
            title (str, optional): The title of the separator.
    """
    def __init__(self, title: str = None):
        """
        Initializes an OptionSeparator with optional title.
        """
    def build_menu_item(self, **menu_item_kwargs) -> None:
        """
        Creates a menu item for the OptionSeparator.
        
                Keyword Args:
                    **menu_item_kwargs: Additional keyword arguments for menu item customization.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the OptionSeparator.
        
                Returns:
                    str: The name of the OptionSeparator.
        """
class OptionSeparatorMenuItem(omni.ui._ui.MenuItem):
    """
    A class representing a menu item separator with an optional title.
    
        This class is a specialized menu item that acts as a visual separator. It can optionally include a title.
    
            Args:
                title (Optional[str]): The title text to display alongside the separator if provided.
    """
    def __init__(self, title: typing.Optional[str] = None):
        """
        Initializes a new instance of the OptionSeparatorMenuItem.
        """
class SeparatorDelegate(omni.ui._ui.MenuDelegate):
    """
    A delegate class for creating a menu separator with an optional title.
    
        This class is used to create a visual separator between menu items, which can be optionally accompanied by a title. It extends the ui.MenuDelegate from the omni.ui module.
    
            Args:
                title (Optional[str]): The title text to display alongside the separator. If None, no title is displayed.
    """
    def __init__(self, title: typing.Optional[str] = None):
        """
        Initializes the SeparatorDelegate.
        """
    def build_item(self, _):
        """
        Builds a UI item for the separator.
        
                Args:
                    _ : Used as a placeholder, no direct usage.
        """
