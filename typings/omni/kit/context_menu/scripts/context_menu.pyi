"""

Context menu implementation classes.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.context_menu.scripts.singleton import Singleton
from omni.kit.usd import layers
from omni.kit.widget.context_menu.context_menu import ContextMenuWidgetExtension
from omni.kit.widget.context_menu.context_menu import get_instance as get_widget_instance
from omni.kit.widget.context_menu.context_menu import reorder_menu_dict
from omni.kit.widget.context_menu.custom_menu_dict import add_menu
from omni.kit.widget.context_menu.custom_menu_dict import get_menu_dict
from omni.kit.widget.context_menu.custom_menu_dict import get_menu_event_stream
from omni import ui
import os as os
import pathlib
from pathlib import Path
import pxr.Gf
from pxr import Gf
from pxr import Kind
import pxr.Sdf
from pxr import Sdf
import pxr.Tf
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
from pxr import UsdUtils
import sys as sys
import typing
import weakref as weakref
__all__: list = ['get_widget_instance', 'SETTING_HIDE_CREATE_MENU', 'ContextMenuExtension', 'get_instance', 'close_menu', 'reorder_menu_dict', 'post_notification', 'get_hovered_prim', 'add_menu', 'get_menu_dict', 'get_menu_event_stream']
class ContextMenuExtension(omni.ext._extensions.IExt):
    """
    Context menu core functionality.
    
        Example using viewport mouse event to trigger:
    
        .. code-block:: python
    
            class ContextMenu:
                def on_startup(self):
                    # get window event stream
                    import omni.kit.viewport_legacy
                    viewport_win = get_viewport_interface().get_viewport_window()
                    # on_mouse_event called when event dispatched
                    self._stage_event_sub = viewport_win.get_mouse_event_stream().create_subscription_to_pop(self.on_mouse_event)
    
                def on_shutdown(self):
                    # remove event
                    self._stage_event_sub = None
    
                def on_mouse_event(self, event):
                    import omni.kit.menu.core
    
                    # check its expected event
                    if event.type != int(omni.kit.menu.core.MenuEventType.ACTIVATE):
                        return
    
                    # get context menu core functionality & check its enabled
                    context_menu = omni.kit.context_menu.get_instance()
                    if context_menu is None:
                        carb.log_error("context_menu is disabled!")
                        return
    
                    # get parameters passed by event
                    objects = {}
                    objects["test_path"] = event.payload["test_path"]
                    # setup objects, this is passed to all functions
                    objects["test"] = "this is a test"
    
                    # setup menu
                    menu_list = [
                        # "name" is name shown on menu. (if name is "" then a menu ui.Separator is added. Can be combined with show_fn)
                        # "glyph" is icon shown on menu, can use full paths to extensions
                        # "name_fn" function to get menu item name
                        # "show_fn" function or list of functions used to decide if menu item is shown. All functions must return True to show
                        # "enabled_fn" function or list of functions used to decide if menu item is enabled. All functions must return True to be enabled
                        # "onclick_fn" function to be called when user clicks menu item
                        # "onclick_action" action to be called when user clicks menu item
                        # "checked_fn" function returns True/False and shows solid/grey tick
                        # "header" as be used with name of "" to use named ui.Separator
                        # "populate_fn" a function to be called to populate the menu. Can be combined with show_fn
                        # "appear_after" a identifier of menu name. Used by custom menus and will allow custom menu to change order
                        # "show_fn_async" this is async function to set items visible flag. These behave differently to show functions as the item will be created regardless and have its
                        #   visibility set to False and its upto show_fn_async callback to set the visible flag to True if required
    
                        {"name": "Test Menu", "glyph": "question.svg", "show_fn": [ContextMenu.has_reason_to_show, ContextMenu.has_another_reason_to_show],
                                 "onclick_fn": ContextMenu.clear_default_prim },
                        {"name": "", "show_fn": ContextMenu.has_another_reason_to_show},
                        {"populate_fn": context_menu.show_create_menu},
                        {"name": ""},
                        {"name": "Copy URL Link", "glyph": "menu_link.svg", "onclick_fn": ContextMenu.copy_prim_url},
                    ]
    
                    # add custom menus
                    menu_list += omni.kit.context_menu.get_menu_dict("MENU", "")
                    menu_list += omni.kit.context_menu.get_menu_dict("MENU", "stagewindow")
                    omni.kit.context_menu.reorder_menu_dict(menu_dict)
    
                    # show menu
                    context_menu.show_context_menu("stagewindow", objects, menu_list)
    
                # show_fn functions
                def has_reason_to_show(objects: dict):
                    if not "test_path" in objects:
                        return False
                    return True
    
                def has_another_reason_to_show(objects: dict):
                    if not "test_path" in objects:
                        return False
                    return True
    
                def copy_prim_url(objects: dict):
                    try:
                        import omni.kit.clipboard
    
                        omni.kit.clipboard.copy("My hovercraft is full of eels")
                    except ImportError:
                        carb.log_warn("Could not import omni.kit.clipboard.")
        
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
    default_delegate: typing.ClassVar[omni.kit.widget.context_menu.context_menu.DefaultMenuDelegate]  # value = <omni.kit.widget.context_menu.context_menu.DefaultMenuDelegate object>
    @staticmethod
    def _set_prim_translation(stage, prim_path: pxr.Sdf.Path, translate: pxr.Gf.Vec3d):
        ...
    @staticmethod
    def bind_material_to_prims_dialog(*args, **kwargs):
        """
        
                [deprecated]
                Shows bind_material_to_prims_dialog.
        
                Replaced by omni.kit.material.library.bind_material_to_prims_dialog()
                
        """
    @staticmethod
    def create_mesh_prim(objects: dict, prim_type: str) -> None:
        """
        
                Create mesh prims
        
                Args:
                    objects: context_menu data
                    prim_type: created prim's type
                
        """
    @staticmethod
    def create_prim(objects: dict, prim_type: str, attributes: dict, create_group_xform: bool = False) -> None:
        """
        
                Create prims
        
                Args:
                    objects: context_menu data
                    prim_type: created prim's type
                    attributes: created prim's custom attributes
                    create_group_xform: passed to CreatePrimWithDefaultXformCommand
                
        """
    def __init__(self):
        """
        
                ContextMenuExtension init function.
                
        """
    def _build_menu(self, menu_entry: dict, objects: dict, delegate) -> bool:
        ...
    def _execute_action(self, action: typing.Tuple, objects):
        ...
    def _get_fn_result(self, menu_entry: dict, name: str, objects: list):
        ...
    def _group_list(self, objects: dict):
        ...
    def _has_click_fn(self, menu_entry):
        ...
    def _is_menu_visible(self, menu_entry: dict, objects: dict):
        ...
    def _prims_have_payloads(self, prim_list):
        ...
    def _prims_have_references(self, prim_list):
        ...
    def _set_hotkey_for_action(self, menu_entry: dict, menu_item: omni.ui._ui.MenuItem):
        ...
    def _ungroup_list(self, objects: dict):
        ...
    def build_add_menu(self, objects: dict, prim_list: list, custom_menu: list = None, delegate = None):
        """
        
                Builds "Add" context sub-menu items
                
        """
    def build_create_menu(self, objects: dict, prim_list: list, custom_menu: dict = list(), delegate = None):
        """
        
                Builds "Create" context sub-menu items
                
        """
    def can_assign_material_async(self, objects: dict, menu_item: omni.ui._ui.Widget):
        """
        
                async show function. The `menu_item` is created but not visible, if this item is shown then `menu_item.visible = True`
                This scans all the prims in the stage looking for a material, if one is found then it can "assign material"
                and `menu_item.visible = True`
        
                Args:
                    objects (dict): context_menu data.
                    menu_item: (uiMenuItem): menu item.
                
        """
    def can_be_copied(self, objects: dict):
        """
        
                Checks if prims can be copied
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims can be copied else False.
                
        """
    def can_convert_references_or_payloads(self, objects):
        """
        
                Checks if references can be converted into payloads or vice versa.
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims can be converted from to payload/reference otherwise False.
                
        """
    def can_delete(self, objects: dict):
        """
        
                Checks if prims can be deleted
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prim can be deleted otherwise False.
                
        """
    def can_show_find_in_browser(self, objects: dict):
        """
        
                Checks if "find" can be shown in browser. IE one prim is selected and is authored.
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if authored and has URL that is saved otherwise False.
                
        """
    def can_use_find_in_browser(self, objects: dict):
        """
        
                Checks if "find" can be used in browser.
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims are authored else False.
                
        """
    def close_menu(self):
        """
        
                [omni.kit.widget.context_menu bridge function] Close currently open context menu. Used by tests not to leave context menu in bad state.
                
        """
    def convert_payload_to_reference(self, objects: dict):
        """
        
                Converts selected prims from payload(s) to reference(s).
                
        """
    def convert_reference_to_payload(self, objects: dict):
        """
        
                Converts selected prims from reference(s) to payload(s).
                
        """
    def copy_prim_path(self, objects: dict) -> None:
        """
        
                Copy prims path to clipboard
        
                Args:
                    objects: context_menu data
                
        """
    def copy_prim_url(self, objects: dict):
        """
        
                Copies URL of Prim in USDA references format.
                @planet.usda@</Planet>
                
        """
    def delete_prim(self, objects: dict, destructive = False):
        """
        
                Delete prims
        
                Args:
                    objects: context_menu data
                    destructive: If it's true, it will remove all corresponding prims in all layers.
                                 Otherwise, it will deactivate the prim in current edit target if its def is not in the current edit target.
                                 By default, it will be non-destructive.
                
        """
    def duplicate_prim(self, objects: dict):
        """
        
                Duplicate prims
        
                Args:
                    objects: context_menu data
                
        """
    def find_in_browser(self, objects: dict) -> None:
        """
        
                Select prim in content_browser
        
                Args:
                    objects: context_menu data
                
        """
    def get_context_menu(self):
        """
        
                [omni.kit.widget.context_menu bridge function] Gets current context_menu.
        
                Returns:
                    (str): Current context_menu.
                
        """
    def get_prim_group(self, prim):
        """
        
                If the prim is or has a parent prim that is a group Kind, returns that prim otherwise None
        
                Args:
                    prim (Usd.Prim): prim to get group from.
        
                Returns:
                    (Usd.Prim) Group prim or None.
                
        """
    def group_selected_prims(self, objects: dict):
        """
        
                Group prims
        
                Args:
                    prims: list of prims
                
        """
    def has_payload(self, objects: dict):
        """
        
                Checks if prims have payload.
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims has payload otherwise False.
                
        """
    def has_payload_or_reference(self, objects: dict):
        """
        
                Checks if prims have payloads or references
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims have payload or references otherwise False.
                
        """
    def has_reference(self, objects: dict):
        """
        
                Checks if prims have references.
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims have reference otherwise False.
                
        """
    def is_material(self, objects: dict):
        """
        
                Checks if prims are UsdShade.Material
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prim is UsdShade.Material else False.
                
        """
    def is_material_bindable(self, objects: dict):
        """
        
                Checks if prims support material binding.
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims can have bound materials otherwise False.
                
        """
    def is_one_prim_selected(self, objects: dict):
        """
        
                Checks if one prim is selected.
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if one prim is selected otherwise False.
                
        """
    def is_prim_in_group(self, objects: dict):
        """
        
                Checks if any prims are in group(s)
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if prims are part of group otherwise False.
                
        """
    def is_prim_selected(self, objects: dict):
        """
        
                Checks if any prims are selected
        
                Args:
                    objects (dict): context_menu data
                Returns:
                    (bool): True if one or more prim is selected otherwise False.
                
        """
    def menu(self, *args, **kwargs):
        """
        
                [omni.kit.widget.context_menu bridge function]
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
    def menu_item(self, *args, **kwargs):
        """
        
                [omni.kit.widget.context_menu bridge function]
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
        
                ContextMenuExtension shutdown function.
                
        """
    def on_startup(self, ext_id):
        """
        
                ContextMenuExtension startup function.
        
                Args:
                    ext_id (str): Extension identifier.
                
        """
    def prim_is_type(self, objects: dict, type: pxr.Tf.Type) -> bool:
        """
        
                Checks if prims are given class/schema
        
                Args:
                    objects (dict): context_menu data.
                    type (Tf.Type): prim type to check.
                Returns:
                    (bool): True if prims are of type `type` otherwise False.
                
        """
    def refresh_payload_or_reference(self, objects: dict):
        """
        
                Find layers containing prims and triggers reload.
                
        """
    def refresh_reference_payload_name(self, objects: dict):
        """
        
                Checks if prims have references/payload and returns name
        
                Returns:
                    (str): Name of payload/reference or None
                
        """
    def select_prims_using_material(self, objects: dict):
        """
        
                Select stage prims using material
        
                Args:
                    objects: context_menu data
                
        """
    def separator(self, name: str = '') -> bool:
        """
        
                [omni.kit.widget.context_menu bridge function] Creates a ui.Separator named `name`.
        
                Args:
                    name (str): Name of the menu separator. Optional.
                
        """
    def show_context_menu(self, menu_name: str, objects: dict, menu_list: typing.List[dict], min_menu_entries: int = 1, **kwargs) -> None:
        """
        
                [omni.kit.widget.context_menu bridge function]
                build context menu from menu_list
        
                Args:
                    menu_name: menu name
                    objects: context_menu data
                    menu_list: list of dictionaries containing context menu values
                    min_menu_entries: minimal number of menu needed for menu to be visible
                
        """
    def show_create_menu(self, objects: dict):
        """
        
                Populate function that builds create menu
        
                Args:
                    objects: context_menu data
                
        """
    def show_selected_prims_names(self, objects: dict, delegate = None) -> None:
        """
        
                Populate function that builds menu items with selected prim info
        
                Args:
                    objects: context_menu data
                
        """
    def ungroup_selected_prims(self, objects: dict):
        """
        
                Ungroup prims
        
                Args:
                    prims: list of prims
                
        """
    @property
    def menu_item_count(self) -> int:
        """
        
                [omni.kit.widget.context_menu bridge function] Number of items in context menu.
        
                Returns:
                    (int): number of menu items.
                
        """
    @menu_item_count.setter
    def menu_item_count(self, value):
        """
        
                [omni.kit.widget.context_menu bridge function] Number of items in context menu.
        
                Args:
                    value (int): new number of menu items.
                
        """
    @property
    def name(self) -> str:
        """
        
                [omni.kit.widget.context_menu bridge function] Name of current context menu.
        
                Returns:
                    (str): Name of current context menu.
                
        """
def close_menu():
    """
    
        Close currently open context menu. Used by tests not to leave context menu in bad state.
        
    """
def get_hovered_prim(objects):
    """
    
        Get prim currently under mouse cursor or None.
    
        Args:
            objects (dict): context_menu data
    
        Returns:
            (Usd.Prim): Prim that is hovered by mouse cursor or None.
        
    """
def get_instance():
    """
    
        Get instance of context menu class
    
        Returns:
            (ContextMenuExtension): Instance of class.
        
    """
def post_notification(message: str, info: bool = False, duration: int = 3):
    """
    
        Post a notification via omni.kit.notification_manager.
    
        Args:
            message (str): The notification text.
            info (bool): notification is NotificationStatus.INFO when True otherwise NotificationStatus.WARNING
            duration (int): The duration (in seconds) after which the notification will be hidden.
                            This duration only works if hide_after_timeout is True.
        
    """
SETTING_HIDE_CREATE_MENU: str = '/exts/omni.kit.context_menu/hideCreateMenu'
TEST_DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.context_menu-1.8.3+d02c707b/data/tests')
_extension_instance: ContextMenuExtension  # value = <omni.kit.context_menu.scripts.context_menu.ContextMenuExtension object>
