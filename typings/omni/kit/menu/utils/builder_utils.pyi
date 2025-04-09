"""

Definition of MenuItemDescription and other menu classes

"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.core.core import has_delegate_func
import typing
__all__ = ['LayoutSourceSearch', 'MenuAlignment', 'MenuItemDescription', 'PrebuiltItemOrder', 'carb', 'create_prebuild_entry', 'get_action_path', 'get_menu_name', 'has_delegate_func', 'omni']
class LayoutSourceSearch:
    """
    
        Controls how layouts search for the menu item paths, either everywhere or just in the local menu group
        
    """
    EVERYWHERE: typing.ClassVar[int] = 0
    LOCAL_ONLY: typing.ClassVar[int] = 1
class MenuAlignment:
    """
    
        Menu alignment setting. Either left or right
        
    """
    DEFAULT: typing.ClassVar[int] = 0
    RIGHT: typing.ClassVar[int] = 1
class MenuItemDescription:
    """
    
        Class for creation of menu items
    
        - "name" is name shown on menu. (if name is "" then a menu spacer is added. Can be combined with show_fn)
        - "glyph" is icon shown on menu, full paths are allowed
        - "header" is None or string value & will add separator above item
        - "appear_after" is name of menu item to insert after. Used for appending menus, can be a list or string
        - "enabled" is True/False, True when item enabled
        - "ticked" menu item is ticked when True
        - "ticked_fn" function or list of functions used to decide if menu item is ticked
        - "ticked_value" is value used to decide if menu item is ticked
        - "radio_group" is name of group of ticked-radio buttons, setting one in group will clear the others
        - "sub_menu" is sub menu to this menu
        - "hotkey" is hotkey values for menu item
        - "name_fn" is function to get menu name
        - "show_fn" function or list of functions used to decide if menu item is shown. All functions must return True to show
        - "enable_fn" function or list of functions used to decide if menu item is enabled. All functions must return True to be enabled
        - "onclick_action" action called when user clicks menu item
        - "unclick_action" action called when user release's button on menu item
        - "onclick_fn" function called when user clicks menu item (deprecated)
        - "unclick_fn" function called when user releases click on menu item (deprecated)
        - "onclick_right_fn" function called when user right clicks menu item (deprecated)
        - "original_svg_color" isn't used (deprecated)
        - "user" is user dictionary that is passed to menu. NOTE: values will be added to this dictionary
        - *hotkey_window* is title of window where hotkey to be triggered
        
    """
    MAX_DEPTH: typing.ClassVar[int] = 16
    def __contains__(self, key):
        ...
    def __copy__(self):
        ...
    def __del__(self):
        ...
    def __getitem__(self, key, default_value = None):
        ...
    def __init__(self, name: str = '', glyph: str = '', header: typing.Optional[str] = None, appear_after: typing.Union[list, str] = '', enabled: bool = True, ticked: bool = False, ticked_value: typing.Optional[bool] = None, radio_group: typing.Optional[str] = '', sub_menu = None, hotkey: typing.Tuple[int, int] = None, name_fn: typing.Callable = None, show_fn: typing.Callable = None, enable_fn: typing.Callable = None, ticked_fn: typing.Callable = None, onclick_action: typing.Tuple = None, unclick_action: typing.Tuple = None, onclick_fn: typing.Callable = None, unclick_fn: typing.Callable = None, onclick_right_fn: typing.Callable = None, original_svg_color: bool = False, original_menu_item = None, user = None, hotkey_window: typing.Optional[str] = None):
        ...
    def __repr__(self):
        ...
    def add_on_delete_func(self, on_delete_fn: callable):
        ...
    def add_on_hotkey_update_func(self, hotkey_update_fn: callable):
        ...
    def destroy(self, recurse: bool = True):
        ...
    def get(self, key, default_value = None):
        ...
    def get_action_mapping_desc(self):
        ...
    def has_action(self):
        ...
    def json_enc(self):
        ...
    def remove_on_delete_func(self, on_delete_fn: callable):
        ...
    def remove_on_hotkey_update_func(self, hotkey_update_fn: callable):
        ...
    def set_hotkey(self, hotkey):
        ...
class PrebuiltItemOrder:
    """
    
        Internal flags used by layout for item ordering
        
    """
    LAYOUT_ITEM_SORTED: typing.ClassVar[int] = 8192
    LAYOUT_ORDERED: typing.ClassVar[int] = 0
    LAYOUT_SUBMENU_SORTED: typing.ClassVar[int] = 4096
    UNORDERED: typing.ClassVar[int] = 2147483647
def create_prebuild_entry(prebuilt_menus: dict, prefix_name: str, action_prefix: str):
    """
    
        internal function that creates a entry in prebuilt_menus dictionary
        
    """
def get_action_path(action_prefix: str, menu_entry_name: str):
    """
    
        converts menu path into internal path
        
    """
def get_menu_name(menu_entry):
    """
    
        gets menu name from menu_entry.name_fn or menu_entry.name
        
    """
