from __future__ import annotations
from functools import partial
import omni.kit.widget.layers.context_menu
from omni.kit.widget.layers.context_menu import ContextMenu
import omni.kit.widget.layers.layer_item
from omni.kit.widget.layers.layer_item import LayerItem
import omni.kit.widget.layers.layer_model
from omni.kit.widget.layers.layer_model import LayerModel
from omni.kit.widget.layers.path_utils import PathUtils
import omni.kit.widget.layers.prim_spec_item
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni.kit.widget.layers.prim_spec_item import PrimSpecSpecifier
from omni import ui
import weakref as weakref
__all__: list = ['get_type_icon', 'create_icon_images', 'build_prim_spec_widget', 'create_layer_name_widget', 'build_layer_widget']
def _build_live_users_tooltip(live_session, icon_size):
    ...
def build_layer_widget(context_menu: omni.kit.widget.layers.context_menu.ContextMenu, model: omni.kit.widget.layers.layer_model.LayerModel, item: omni.kit.widget.layers.layer_item.LayerItem, column_id: int, expanded: bool):
    ...
def build_prim_spec_widget(context_menu: omni.kit.widget.layers.context_menu.ContextMenu, model: omni.kit.widget.layers.layer_model.LayerModel, item: omni.kit.widget.layers.prim_spec_item.PrimSpecItem, column_id: int, expanded: bool):
    ...
def create_icon_images(layout, item: omni.kit.widget.layers.prim_spec_item.PrimSpecItem):
    ...
def create_layer_name_widget(model: omni.kit.widget.layers.layer_model.LayerModel, value_model, item: omni.kit.widget.layers.layer_item.LayerItem, context_menu: omni.kit.widget.layers.context_menu.ContextMenu, expanded: bool):
    ...
def get_type_icon(node_type):
    """
    Convert USD Type to icon file name
    """
TOOLTIP_STYLE: dict = {'color': 4288124823, 'Tooltip': {'background_color': 3995214370}}
have_session_management: bool = False
