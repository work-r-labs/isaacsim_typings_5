"""
Context menu core functionality
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import copy as copy
from functools import partial
import omni as omni
from omni.kit.menu.core.core import IconMenuBaseDelegate
from omni.kit.menu.core.core import uiMenu as _uiMenu
from omni.kit.menu.core.core import uiMenuItem as _uiMenuItem
from omni import ui
import pathlib
from pathlib import Path
import typing
__all__: list = ['ContextMenuWidgetExtension', 'DefaultMenuDelegate', 'get_instance', 'close_menu', 'reorder_menu_dict']
class ContextMenuWidgetExtension(omni.ext._extensions.IExt):
    """
    Context menu core functionality
    """
    class DefaultMenuDelegate(omni.kit.menu.core.core.IconMenuBaseDelegate):
        def __init__(self, **kwargs):
            ...
        def _build_item_get_style(self, item: omni.ui._ui.Menu) -> dict:
            ...
        def _build_item_hotkey(self, item):
            ...
        def _build_item_label(self, item):
            ...
    class uiMenu(omni.ui._ui.Menu):
        """
        ui.Menu subclass. Has glyph, menu_checkable, menu_hotkey_text, submenu and parent_menu properties
        
            Args:
                args: Arguments for the ui.Menu constructor.
        
            Keyword Args:
                glyph: The glyph associated with the menu.
                menu_checkable: If the menu is checkable.
                menu_hotkey_text: The hotkey text for the menu.
                submenu: If the menu is a submenu.
                parent_menu: The parent menu.
            
        """
        def __init__(self, *args, **kwargs):
            """
            Initializes the uiMenu instance.
            """
    class uiMenuItem(omni.ui._ui.MenuItem):
        """
        ui.MenuItem subclass. Has glyph, menu_checkable, menu_hotkey_text, and parent_menu properties
        
            Args:
                args: Positional arguments passed to the parent class.
        
            Keyword Args:
                glyph: Custom glyph for the menu item.
                menu_checkable: Indicates if the menu item is checkable.
                menu_hotkey_text: Hotkey text for the menu item.
                parent_menu: Reference to the parent menu.
                radio_group: Radio group to which this menu item belongs.
            
        """
        def __init__(self, *args, **kwargs):
            """
            Initializes a new instance of the uiMenuItem class.
            """
    default_delegate: typing.ClassVar[DefaultMenuDelegate]  # value = <omni.kit.widget.context_menu.context_menu.DefaultMenuDelegate object>
    def __init__(self):
        """
        
                ContextMenuWidgetExtension init function.
                
        """
    def _build_menu(self, menu_entry: dict, objects: dict, delegate) -> bool:
        ...
    def _execute_action(self, action: typing.Tuple, objects):
        ...
    def _get_fn_result(self, menu_entry: dict, name: str, objects: list):
        ...
    def _has_click_fn(self, menu_entry):
        ...
    def _set_hotkey_for_action(self, menu_entry: dict, menu_item: omni.ui._ui.MenuItem):
        ...
    def close_menu(self):
        """
        
                Close currently open context menu. Used by tests not to leave context menu in bad state.
                
        """
    def get_context_menu(self):
        """
        
                Gets current context_menu.
        
                Returns:
                    (str): Current context_menu.
                
        """
    def menu(self, name: str, delegate = None, glyph = '', submenu = False, tearable = False, **kwargs):
        """
        
                Creates a menu.
        
                Args:
                    name (str): Name of the menu.
                    delegate (ui.MenuDelegate): Specify the delegate to create a custom menu. Optional.
                    glyph (str): Path of the glyph image to show before the menu name. Optional.
                    submenu (bool): Enables the submenu marker. Optional.
                    tearable (bool): The ability to tear the window off. Optional.
        
                Returns:
                    (uiMenu): Menu item created.
                
        """
    def menu_item(self, name: str, triggered_fn: typing.Callable = None, enabled: bool = True, checkable: bool = False, checked: bool = False, is_async_func = False, delegate = None, additional_kwargs = None, glyph = ''):
        """
        
                Creates a menu item.
        
                Args:
                    name (str): Name of the menu item.
                    triggered_fn (Callable): Function to call when menu item is clicked. Optional.
                    enabled (bool): Enable the menu item. Optional.
                    checkable (bool): This property holds whether this menu item is checkable. A checkable item is one which has an on/off state. Optional.
                    checked (bool): This property holds a flag that specifies the widget has to use eChecked state of the style. It's on the Widget level because the button can have sub-widgets that are also should be checked. Optional.
                    is_async_func (bool): Optional.
                    delegate (ui.MenuDelegate): Specify the delegate to create a custom menu. Optional.
                    additional_kwargs (dict): Additional keyword arguments to pass to ui.MenuItem. Optional.
                    glyph (str): Path of the glyph image to show before the menu name. Optional.
        
                Returns:
                    (uiMenuItem): Menu item created.
                
        """
    def on_shutdown(self):
        """
        
                ContextMenuWidgetExtension shutdown function.
                
        """
    def on_startup(self, ext_id):
        """
        
                ContextMenuWidgetExtension startup function.
        
                Args:
                    ext_id (str): Extension identifier.
                
        """
    def separator(self, name: str = '') -> bool:
        """
        
                Creates a menu separator.
        
                Args:
                    name (str): Name of the menu separator. Optional.
                
        """
    def show_context_menu(self, menu_name: str, objects: dict, menu_list: typing.List[dict], min_menu_entries: int = 1, delegate = None) -> None:
        """
        
                build context menu from menu_list
        
                Args:
                    menu_name (str): menu name
                    objects (dict): context_menu data
                    menu_list (list): list of dictionaries containing context menu values
                    min_menu_entries (int): minimal number of menu needed for menu to be visible
                
        """
    @property
    def name(self) -> str:
        """
        
                Name of current context menu.
        
                Returns:
                    (str): Name of current context menu.
                
        """
class DefaultMenuDelegate(omni.kit.menu.core.core.IconMenuBaseDelegate):
    def __init__(self, **kwargs):
        ...
    def _build_item_get_style(self, item: omni.ui._ui.Menu) -> dict:
        ...
    def _build_item_hotkey(self, item):
        ...
    def _build_item_label(self, item):
        ...
def close_menu():
    """
    
        Close currently open context menu. Used by tests not to leave context menu in bad state.
        
    """
def get_instance():
    """
    
        Get instance of context menu class
    
        Returns:
            (ContextMenuWidgetExtension): Instance of class.
        
    """
def reorder_menu_dict(menu_dict: typing.List[dict]):
    """
    
        Reorder menus using "appear_after" value in menu
    
        Args:
            menu_dict (list): list of dictionaries
        
    """
TEST_DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.context_menu-1.2.4+d02c707b/data/tests')
_extension_instance: ContextMenuWidgetExtension  # value = <omni.kit.widget.context_menu.context_menu.ContextMenuWidgetExtension object>
