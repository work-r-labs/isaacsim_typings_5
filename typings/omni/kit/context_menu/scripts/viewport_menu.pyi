"""

Viewport context menu implementation with own styling
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.context_menu.scripts.context_menu import get_instance
from omni.kit.usd import layers
from omni.kit.widget.context_menu.context_menu import DefaultMenuDelegate
from omni import ui
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['ViewportMenu']
class ViewportMenu:
    """
    
        Viewport context menu implementation with own styling
        
    """
    class ViewportMenuDelegate(omni.kit.widget.context_menu.context_menu.DefaultMenuDelegate):
        def get_style(self):
            ...
    menu_delegate: typing.ClassVar[ViewportMenu.ViewportMenuDelegate]  # value = <omni.kit.context_menu.scripts.viewport_menu.ViewportMenu.ViewportMenuDelegate object>
    @staticmethod
    def bind_material_to_prim_dialog(objects):
        ...
    @staticmethod
    def can_show_clear_clipboard(objects, menu_item):
        ...
    @staticmethod
    def clear_clipboard(objects):
        ...
    @staticmethod
    def copy_prim_to_clipboard(objects):
        ...
    @staticmethod
    def is_material_bindable(objects):
        ...
    @staticmethod
    def is_on_clipboard(objects, name):
        ...
    @staticmethod
    def is_prim_on_clipboard(objects):
        ...
    @staticmethod
    def paste_prim_from_clipboard(objects):
        ...
    @staticmethod
    def set_prim_to_pos(path, new_pos):
        ...
    @staticmethod
    def show_create_menu(objects):
        ...
    @staticmethod
    def show_menu(usd_context_name: str, prim_path: str = None, world_pos: typing.Sequence[float] = None, stage = None):
        ...
MENU_STYLE: dict = {'Menu.Title': {'color': 'shade:4280952869', 'background_color': 0}, 'Menu.Title:hovered': {'background_color': 'shade:1006618420', 'border_width': 1, 'border_color': 'shade:4294952756'}, 'Menu.Title:pressed': {'background_color': 'shade:1006618420'}, 'Menu.Item': {'color': 'shade:4292269782', 'margin_width': 'shade:5', 'margin_HEIGHT': 'shade:3'}, 'Menu.Item.CheckMark': {'color': 'shade:4294952756'}, 'Menu.Separator': {'color': 'shade:4285427310', 'margin_HEIGHT': 'shade:3', 'border_width': 1.5}, 'Menu.Window': {'background_color': 'shade:3425314853', 'border_width': 0, 'border_radius': 0, 'background_selected_color': 'shade:1006618420', 'secondary_padding': 1, 'secondary_selected_color': 'shade:4294952756', 'margin': 2}, 'MenuItem': {'background_selected_color': 'shade:1006618420', 'secondary_padding': 1, 'secondary_selected_color': 'shade:4294952756'}}
