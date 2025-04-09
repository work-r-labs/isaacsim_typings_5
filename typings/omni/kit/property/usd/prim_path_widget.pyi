from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import lru_cache
import omni as omni
from omni.kit.property.usd.add_attribute_popup import AddAttributePopup
from omni.kit.property.usd.context_menu import ContextMenu
from omni.kit.property.usd.context_menu import ContextMenuEvent
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni import ui
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import typing
import weakref as weakref
__all__: list = ['ButtonMenuEntry', 'PrimPathWidget']
class ButtonMenuEntry:
    def __init__(self, path: str, glyph: str = None, name_fn: typing.Callable = None, show_fn: typing.Callable = None, enabled_fn: typing.Callable = None, onclick_fn: typing.Callable = None, add_to_context_menu: bool = False):
        ...
    def clean(self):
        ...
    def get_context_menu(self):
        ...
    def get_dict(self, payload, name = None):
        ...
class Constant:
    ADD_BUTTON_SIZE: typing.ClassVar[int] = 52
    LABEL_COLOR: typing.ClassVar[int] = 4288585374
    LABEL_FONT_SIZE: typing.ClassVar[int] = 14
    LABEL_WIDTH: typing.ClassVar[int] = 80
    MIXED: typing.ClassVar[str] = 'Mixed'
    MIXED_COLOR: typing.ClassVar[int] = 4291599969
    def __setattr__(self, name, value):
        ...
class MenuDelegate(omni.ui._ui.MenuDelegate):
    def get_parameters(self, name, kwargs):
        ...
class PrimPathWidget(omni.kit.window.property.templates.simple_property_widget.SimplePropertyWidget):
    """
    A widget for displaying and interacting with USD Prim paths in Omniverse Kit applications.
    
        This widget extends the SimplePropertyWidget to provide a comprehensive interface for USD Prim path manipulation and visualization. It includes features such as renaming Prims, adding attributes, and displaying various Prim properties like instanceability and path. It supports large selection handling and integrates with the application's notification system for feedback. The widget also incorporates a context menu for additional actions and utilizes a caching mechanism for performance optimization.
        
    """
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        ...
    @staticmethod
    def add_button_menu_entry(path: str, glyph: str = None, name_fn = None, show_fn: typing.Callable = None, enabled_fn: typing.Callable = None, onclick_fn: typing.Callable = None, add_to_context_menu: bool = True):
        """
        Adds a new button menu entry.
        
                Args:
                    path (str): The path where the menu entry will be added.
                    glyph (str, optional): The icon glyph for the menu entry.
                    name_fn (Callable, optional): Function to generate the name of the menu entry.
                    show_fn (Callable, optional): Function to determine if the menu entry should be shown.
                    enabled_fn (Callable, optional): Function to determine if the menu entry should be enabled.
                    onclick_fn (Callable, optional): Function to be executed when the menu entry is clicked.
                    add_to_context_menu (bool, optional): Indicates if the entry should be added to the context menu.
        """
    @staticmethod
    def add_path_item(draw_fn: typing.Callable):
        """
        Adds a new path item.
        
                Args:
                    draw_fn (Callable): The function used to draw the path item.
        """
    @staticmethod
    def get_button_menu_entries():
        """
        Retrieves all button menu entries.
        
                Returns:
                    list: A list of button menu entries.
        """
    @staticmethod
    def get_path_item_padding(padding: float):
        """
        Gets the padding for path items.
        
                Args:
                    padding (float): The padding value to query.
        """
    @staticmethod
    def get_path_items():
        """
        Retrieves all path items.
        
                Returns:
                    list: A list of path items.
        """
    @staticmethod
    def payload_wrapper(objects, onclick_fn_weak):
        """
        Wraps the payload for onclick events.
        
                Args:
                    objects (dict): Objects associated with the onclick event.
                    onclick_fn_weak (Callable): Weakref to the onclick function to be executed.
        """
    @staticmethod
    def rebuild():
        """
        Requests a rebuild of the widget.
        """
    @staticmethod
    def remove_button_menu_entry(item: ButtonMenuEntry):
        """
        Removes a button menu entry.
        
                Args:
                    item (:obj:`ButtonMenuEntry`): The menu entry to be removed.
        """
    @staticmethod
    def remove_path_item(draw_fn: typing.Callable):
        """
        Removes a path item.
        
                Args:
                    draw_fn (Callable): The function used to draw the path item that will be removed.
        """
    @staticmethod
    def set_path_item_padding(padding: float):
        """
        Sets the padding for path items.
        
                Args:
                    padding (float): The padding value to be set.
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the PrimPathWidget.
        """
    def _add_create_attribute_menu(self):
        ...
    def _build_copy_menu(self, buttons, context_menu, copy_fn):
        ...
    def _build_prim_instanceable_widget(self):
        ...
    def _build_prim_large_selection_widget(self):
        ...
    def _build_prim_name_widget(self):
        ...
    def _build_prim_path_widget(self):
        ...
    def _build_prim_stage_widget(self):
        ...
    def _copy_to_clipboard(self, to_copy):
        ...
    def _edit_field(self, model, frame, tooltip, buttons):
        ...
    def _on_mouse_pressed(self, button, context_menu, widget):
        """
        Called when the user press the mouse button on the item
        """
    def _on_rename_setting_changed(self, item, event_type):
        ...
    def _prim_name_begin_edit(self, model):
        ...
    def _prim_name_end_edit(self, model):
        ...
    def build_items(self):
        """
        Builds the items for the widget based on the current payload.
        """
    def clean(self):
        """
        Cleans up resources managed by the widget.
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (dict): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if the payload is handled successfully, otherwise False.
        """
    def reset(self):
        """
        Resets the widget to its initial state.
        """
def _get_plus_glyph(*args, **kwargs):
    ...
def post_notification(message: str, info: bool = False, duration: int = 3, hide_after_timeout: bool = True):
    ...
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
g_singleton: PrimPathWidget  # value = <omni.kit.property.usd.prim_path_widget.PrimPathWidget object>
