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
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the WindowExtension with default settings and menu items.
        """
