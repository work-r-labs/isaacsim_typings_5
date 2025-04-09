"""

Layout implementation class. See "Layouts and & Hooks" section
"""
from __future__ import annotations
import carb as carb
import copy as copy
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.builder_utils import PrebuiltItemOrder
from omni.kit.menu.utils.builder_utils import create_prebuild_entry
from omni.kit.menu.utils.builder_utils import get_action_path
__all__ = ['LayoutSourceSearch', 'MenuItemDescription', 'MenuLayout', 'PrebuiltItemOrder', 'carb', 'copy', 'create_prebuild_entry', 'get_action_path']
class MenuLayout:
    """
    
        Layout implementation class. See "Layouts and & Hooks" section
        
    """
    class Group(MenuLayout.MenuLayoutItem):
        def __init__(self, name, items = None, source = None, source_search = 0):
            ...
    class Item(MenuLayout.MenuLayoutItem):
        def __init__(self, name, source = None, source_search = 0, remove = False, duplicate = False, glyph = None):
            ...
        def __repr__(self):
            ...
    class Menu(MenuLayout.MenuLayoutItem):
        def __init__(self, name, items = None, source = None, source_search = 0, remove = False):
            ...
    class MenuLayoutItem:
        def __init__(self, name = None, source = None, source_search = 0):
            ...
        def __repr__(self):
            ...
        def json_enc(self):
            ...
    class Seperator(MenuLayout.MenuLayoutItem):
        def __init__(self, name = None, source = None, source_search = 0):
            ...
    class Sort(MenuLayout.MenuLayoutItem):
        def __init__(self, name = None, source = None, source_search = 0, exclude_items = None, sort_submenus = False):
            ...
        def __repr__(self):
            ...
    class SubMenu(MenuLayout.MenuLayoutItem):
        def __init__(self, name, items = None, source = None, source_search = 0, remove = False, glyph = None):
            ...
    @staticmethod
    def find_menu_item(menu_items: typing.List, menu_items_root: typing.List, layout_item: MenuLayout.MenuLayoutItem, sub_menu = False, use_original_location = False):
        ...
    @staticmethod
    def process_layout(prebuilt_menus: dict, menu_layout: typing.List, menu_name: str, submenu_name: str, parent_layout_offset: int, parent_layout_index: int, debuglog: bool):
        ...
    def __del__(self):
        ...
    def __init__(self, debuglog = False):
        ...
    def add_layout(self, layout: typing.List[omni.kit.menu.utils.layout.MenuLayout.MenuLayoutItem]):
        ...
    def apply_layout(self, prebuilt_menus: dict):
        ...
    def destroy(self):
        ...
    def get_layout(self):
        ...
    def menus_created(self):
        ...
    def remove_layout(self, layout: typing.List[omni.kit.menu.utils.layout.MenuLayout.MenuLayoutItem]):
        ...
