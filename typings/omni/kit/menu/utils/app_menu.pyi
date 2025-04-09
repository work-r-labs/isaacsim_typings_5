"""

ui.Menu and ui.MenuItem menu libraries
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import IntFlag
import omni as omni
from omni.kit.menu.core.core import IconMenuBaseDelegate
from omni.kit.menu.core.core import has_delegate_func
from omni.kit.menu.core.core import uiMenu
from omni.kit.menu.core.core import uiMenuItem
from omni.kit.menu.utils.builder_utils import MenuAlignment
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.builder_utils import PrebuiltItemOrder
from omni.kit.menu.utils.builder_utils import create_prebuild_entry
from omni.kit.menu.utils.builder_utils import get_action_path
from omni.kit.menu.utils.builder_utils import get_menu_name
from omni.kit.menu.utils.layout import MenuLayout
from omni import ui
import sys as sys
import typing
import weakref as weakref
__all__: list = ['MenuItemOrder', 'MenuState', 'MenuActionControl', 'IconMenuDelegate', 'AppMenu']
class AppMenu:
    _AppMenu__logged_no_window: typing.ClassVar[bool] = False
    @staticmethod
    def set_default_menu_proirity(*args, **kwargs):
        ...
    @staticmethod
    def sort_menu_hook(merged_menu):
        ...
    def _AppMenu__on_ext_changed(self, ext_id: str, *_):
        ...
    def __init__(self, get_instance: typing.Optional[<built-in function callable>] = None, menu_bar: typing.Optional[omni.ui._ui.MenuBar] = None):
        """
        
                Create app menu for menu bar.
        
                Args:
                    get_instance (Optional[callable]): Callback to get extension instance, defaults to None. Deprecated.
                    menu_bar (Optional[ui.MenuBar]): Menu bar to create menus, defaults to None which means use menu bar in main window.
                
        """
    def _build_menu(self, prebuilt_menus, prebuilt_menus_root, is_root_menu, parent_menu, visible_override = None, menu_checkable = False, menu_hotkey_text = False, glyph = None) -> int:
        ...
    def _clear_hotkey(self, menu_entry):
        ...
    def _execute_action(self, action: typing.Tuple):
        ...
    def _mainwindow_loaded(self):
        ...
    def _on_hotkey_changed(self, name: str, event: carb.events._events.IEvent) -> None:
        ...
    def _refresh_menu(self, action_prefix, prebuilt_menus, prebuilt_menus_root, action_path_items = None, visible_override = None):
        ...
    def _refresh_menu_item(self, action_path: str, menus: list, action_path_items: list):
        ...
    def _register_hotkey(self, menu_entry: omni.kit.menu.utils.builder_utils.MenuItemDescription):
        ...
    def _set_ready_state(self, event):
        ...
    def _setup_hotkey(self, menu_entry: omni.kit.menu.utils.builder_utils.MenuItemDescription, action_path: str) -> str:
        ...
    def _submenu_is_shown(self, action_prefix: str, visible: bool, delegate: typing.Any, refresh: bool):
        ...
    def _unregister_hotkey(self, menu_entry: omni.kit.menu.utils.builder_utils.MenuItemDescription):
        ...
    def add_hook(self, callback: typing.Callable):
        ...
    def add_layout(self, layout: typing.List[typing.Union[omni.kit.menu.utils.layout.MenuLayout.Menu, omni.kit.menu.utils.layout.MenuLayout.SubMenu, omni.kit.menu.utils.layout.MenuLayout.Item, omni.kit.menu.utils.layout.MenuLayout.Seperator, omni.kit.menu.utils.layout.MenuLayout.Group]]):
        ...
    def add_menu_items(self, menu: list, name: str, menu_index: int, can_rebuild_menus: bool, delegate = None) -> list:
        ...
    def build_menus_after_loading(self):
        ...
    def clear_menu_data(self):
        ...
    def create_menu(self):
        ...
    def destroy(self):
        ...
    def get_fn_result(self, menu_entry: omni.kit.menu.utils.builder_utils.MenuItemDescription, name: str, default: bool = True):
        ...
    def get_menu_data(self):
        ...
    def get_menu_layout(self):
        ...
    def get_merged_menus(self):
        ...
    def merge_menus(self, menu_keys: list, menu_defs: list, menu_order: list, delegates = None):
        ...
    def prebuild_menu(self, menus, prefix_name, action_prefix, delegate):
        ...
    def rebuild_menus(self):
        ...
    def refresh_menu_items(self, name: str, action_path: str = ''):
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
    def set_right_padding(self, padding):
        ...
class IconMenuDelegate(omni.kit.menu.core.core.IconMenuBaseDelegate):
    def __init__(self, **kwargs):
        ...
class MenuActionControl:
    """
    
        Setting for executing actions. Either NODELAY which is executed instantly or NONE which is async with 1 frame delay
        
    """
    NODELAY: typing.ClassVar[str] = '@MenuActionControl.NODELAY'
    NONE: typing.ClassVar[str] = '@MenuActionControl.NONE'
class MenuItemOrder:
    """
    
        "appear_after" values. FIRST will be top of list and LAST will be bottom of list.
        
    """
    FIRST: typing.ClassVar[str] = '@first'
    LAST: typing.ClassVar[str] = '@last'
class MenuState(enum.IntFlag):
    """
    
        Internal state. Invalid is before EVENT_APP_READY event received and Created is after.
        
    """
    Created: typing.ClassVar[MenuState]  # value = <MenuState.Created: 1>
    Invalid: typing.ClassVar[MenuState]  # value = <MenuState.Invalid: 0>
