from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit import notification_manager as nm
from omni.kit.usd import layers
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.actions import ActionManager
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_link_window import LayerLinkWindow
from omni.kit.widget.layers.layer_model import LayerModel
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni.kit.widget.layers.window import LayerWindow
from omni import ui
import os as os
import pathlib
from pathlib import Path
from pxr import Sdf
import typing
__all__: list = ['LayerExtension']
class LayerExtension(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    """
    The entry point for Layer 2
    """
    CONTEXT_MENU_ITEM_INSERT_SUBLAYER: typing.ClassVar[str] = 'Insert As Sublayer'
    MENU_GROUP: typing.ClassVar[str] = 'Window'
    WINDOW_NAME: typing.ClassVar[str] = 'Layer'
    @staticmethod
    def _is_show_insert_visible(content_url):
        ...
    @staticmethod
    def get_instance():
        """
        
                Returns the instance of the extension.
        
                Returns:
                    The instance of the extension.
                
        """
    def _destroy_window_async(self):
        ...
    def _get_content_window(self):
        ...
    def _on_event(self, event):
        ...
    def _on_icon_menu_click(self, menu, value):
        ...
    def _on_layer_edit_mode_update(self, edit_mode):
        ...
    def _on_layer_events(self, event: carb.events._events.IEvent):
        ...
    def _register_menus(self):
        ...
    def _unregister_menus(self):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def add_layer_selection_changed_fn(self, fn: typing.Callable[[omni.kit.widget.layers.layer_item.LayerItem], NoneType]):
        """
        
                Add a layer selection changed function to the selection listeners.
        
                Args:
                    fn (Callable[[LayerItem], None]): The function to add.
        
                Returns:
                    Any: The result of the window's `add_layer_selection_changed_fn` method.
        
                
        """
    def get_current_focused_layer_item(self) -> omni.kit.widget.layers.layer_item.LayerItem:
        """
        
                Get the current focused layer item in the Layer Window.
        
                Returns:
                    LayerItem or None: The current focused layer item, or None if the window is not available.
        
                
        """
    def get_layer_model(self) -> omni.kit.widget.layers.layer_model.LayerModel:
        """
        
                Get the layer model from the window.
        
                Returns:
                    LayerModel or None: The layer model from the window, or None if the window is not available.
        
                
        """
    def get_selected_items(self) -> typing.List[omni.ui._ui.AbstractItem]:
        """
        
                Get the selected items from the layer view in the window.
        
                Returns:
                    List[ui.AbstractItem]: The selected items, or an empty list if the window is not available.
        
                
        """
    def on_shutdown(self):
        """
        Called on extension shutdown.
        """
    def on_startup(self, ext_id):
        """
        
                Called on extension startup.
        
                Args:
                    ext_id (int): The ID of the extension.
        
                
        """
    def remove_layer_selection_changed_fn(self, fn: typing.Callable[[omni.kit.widget.layers.layer_item.LayerItem], NoneType]):
        """
        
                Remove a selection listener.
        
                Args:
                    fn (Callable[[LayerItem], None]): The selection listener function to remove.
        
                
        """
    def set_current_focused_layer_item(self, layer_identifier: str):
        """
        
                Set the focused layer item in the Layer Window.
        
                Args:
                    layer_identifier (str): The identifier of the layer item to set as focused.
        
                
        """
    def show_window(self, value):
        """
        
                Show or hide the Layer Window.
        
                Args:
                    value (bool): True to show the window, False to hide it.
        
                
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.layers-1.8.2+d02c707b/icons')
_extension_instance: LayerExtension  # value = <omni.kit.widget.layers.extension.LayerExtension object>
