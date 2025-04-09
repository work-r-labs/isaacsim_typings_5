from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput as Key
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
import typing
__all__: list = ['WindowExtension']
class MenuItemPriDescription(omni.kit.menu.utils.builder_utils.MenuItemDescription):
    def __init__(self, *argv, **kwargs):
        ...
class WindowExtension:
    """
    A class to manage window-related extensions and menu items.
    
        This class provides functionalities to handle window-specific menu items, including toggling UI visibility, fullscreen mode, and DPI scaling options.
    
        The window menu items are initialized upon instantiation and removed upon deletion of the object.
        
    """
    SHOW_DPI_SCALE_MENU_SETTING: typing.ClassVar[str] = '/app/window/showDpiScaleMenu'
    @staticmethod
    def add_menu(*args, **kwargs):
        """
        Adds a menu to the window.
        
                Args:
                    argv (tuple): Positional arguments for the menu.
        
                Keyword Args:
                    name (str): The name of the menu item.
                    onclick_action (tuple): Action triggered on click.
                    hotkey (tuple): Hotkey for the menu item.
                    priority (int): Priority of the menu item.
                    sub_menu (list): Sub-menu items.
                
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the WindowExtension with default settings and menu items.
        """
