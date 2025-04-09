"""

Menu implementation class.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.utils.actions import ActionMenuSubscription
from omni.kit.menu.utils.actions import add_action_to_menu
from omni.kit.menu.utils.app_menu import IconMenuDelegate
from omni.kit.menu.utils.app_menu import MenuActionControl
from omni.kit.menu.utils.app_menu import MenuItemOrder
from omni.kit.menu.utils.app_menu import MenuState
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuAlignment
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.builder_utils import PrebuiltItemOrder
from omni.kit.menu.utils.builder_utils import get_action_path
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.menu.utils.extension_window_helper_full import MenuHelperExtensionFull
from omni.kit.menu.utils.extension_window_helper_full import MenuHelperWindow
from omni.kit.menu.utils.layout import MenuLayout
__all__: list = ['ActionMenuSubscription', 'add_action_to_menu', 'IconMenuDelegate', 'MenuActionControl', 'MenuItemOrder', 'MenuState', 'LayoutSourceSearch', 'MenuAlignment', 'MenuItemDescription', 'PrebuiltItemOrder', 'get_action_path', 'MenuHelperExtension', 'MenuHelperExtensionFull', 'MenuHelperWindow', 'MenuLayout', 'MenuUtilsExtension', 'get_instance', 'add_menu_items', 'replace_menu_items', 'remove_menu_items', 'refresh_menu_items', 'add_hook', 'remove_hook', 'rebuild_menus', 'set_default_menu_proirity', 'set_default_menu_priority', 'add_layout', 'remove_layout', 'get_menu_layout', 'get_merged_menus', 'get_debug_stats', 'build_submenu_dict']
class MenuUtilsExtension(omni.ext._extensions.IExt):
    """
    
        Menu implementation class.
        
    """
    @staticmethod
    def set_default_menu_proirity(*args, **kwargs):
        ...
    def __init__(self):
        ...
    def add_hook(self, callback: typing.Callable):
        ...
    def add_layout(self, layout: typing.List[typing.Union[omni.kit.menu.utils.layout.MenuLayout.Menu, omni.kit.menu.utils.layout.MenuLayout.SubMenu, omni.kit.menu.utils.layout.MenuLayout.Item, omni.kit.menu.utils.layout.MenuLayout.Seperator, omni.kit.menu.utils.layout.MenuLayout.Group]]):
        ...
    def add_menu_items(self, menu: list, name: str, menu_index: int, can_rebuild_menus: bool, delegate = None) -> list:
        ...
    def clear_menu_data(self):
        ...
    def get_debug_stats(self) -> dict:
        """
        
                gets debug stats as dictionary, info on what functions called and how many times.
                
        """
    def get_menu_data(self):
        ...
    def get_menu_layout(self):
        ...
    def get_merged_menus(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def rebuild_menus(self):
        ...
    def refresh_menu_items(self, name: str, immediately: bool = False):
        ...
    def remove_hook(self, callback: typing.Callable):
        ...
    def remove_layout(self, layout: typing.List[typing.Union[omni.kit.menu.utils.layout.MenuLayout.Menu, omni.kit.menu.utils.layout.MenuLayout.SubMenu, omni.kit.menu.utils.layout.MenuLayout.Item, omni.kit.menu.utils.layout.MenuLayout.Seperator, omni.kit.menu.utils.layout.MenuLayout.Group]]):
        ...
    def remove_menu_items(self, menu: list, name: str, can_rebuild_menus: bool):
        ...
    def replace_menu_items(self, new_menu: list, old_menu: list, name: str) -> list:
        ...
    def set_default_menu_priority(self, name: str, menu_index: int):
        ...
def add_hook(callback: typing.Callable):
    """
    
        add a menu modification callback hook
        callback is function to be called when menus are re-generated
        
    """
def add_layout(layout: typing.List[typing.Union[omni.kit.menu.utils.layout.MenuLayout.Menu, omni.kit.menu.utils.layout.MenuLayout.SubMenu, omni.kit.menu.utils.layout.MenuLayout.Item, omni.kit.menu.utils.layout.MenuLayout.Seperator, omni.kit.menu.utils.layout.MenuLayout.Group]]):
    """
    
        add a menu layout.
        
    """
def add_menu_items(menu: list, name: str, menu_index: int = 0, can_rebuild_menus: bool = True, delegate = None):
    """
    
        add a list of menus items to menu.
        menu is list of MenuItemDescription()
        name is name to appear when menu is collapsed
        menu_index is horizontal positioning
        can_rebuild_menus is flag to call rebuild_menus when True
        delegate ui.MenuDelegate delegate
        
    """
def build_submenu_dict(menu_list: list, glyph: str = None):
    """
    
        builds a dictionary of List[MenuItemDescription] with sub_menus from List[MenuItemDescription] with full paths. EG: "/Window/Viewport/Viewport 1"
        
    """
def get_debug_stats() -> dict:
    """
    
        gets debug stats as dictionary, info on what functions called and how many times.
        
    """
def get_instance():
    """
    
        get MenuUtilsExtension class ptr
        
    """
def get_menu_layout():
    """
    
        get menu layouts.
        
    """
def get_merged_menus() -> dict:
    """
    
        get combined menus as dictionary
        
    """
def rebuild_menus():
    """
    
        force menus to rebuild, triggering hooks
        
    """
def refresh_menu_items(name: str, immediately = None):
    """
    
        update menus enabled state
        menu is list of MenuItemDescription()
        name is name to appear when menu is collapsed
        immediately is deprecated and not used
        
    """
def remove_hook(callback: typing.Callable):
    """
    
        remove a menu modification callback hook
        callback is function to be called when menus are re-generated
        
    """
def remove_layout(layout: typing.List[typing.Union[omni.kit.menu.utils.layout.MenuLayout.Menu, omni.kit.menu.utils.layout.MenuLayout.SubMenu, omni.kit.menu.utils.layout.MenuLayout.Item, omni.kit.menu.utils.layout.MenuLayout.Seperator, omni.kit.menu.utils.layout.MenuLayout.Group]]):
    """
    
        remove a menu layout.
        
    """
def remove_menu_items(menu: list, name: str, can_rebuild_menus: bool = True):
    """
    
        remove  a list of menus items to menu.
        menu is list of MenuItemDescription()
        name is name to appear when menu is collapsed
        can_rebuild_menus is flag to call rebuild_menus when True
        
    """
def replace_menu_items(new_menu: list, old_menu: list, name: str):
    """
    
        replace a existing list of menus items to menu.
        menu is list of MenuItemDescription()
        name is name to appear when menu is collapsed
        
    """
def set_default_menu_priority(name, menu_index):
    """
    
        set default menu priority
        
    """
_extension_instance: MenuUtilsExtension  # value = <omni.kit.menu.utils.utils.MenuUtilsExtension object>
