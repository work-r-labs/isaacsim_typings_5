from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.utils import add_menu_items
from omni.kit.menu.utils.utils import remove_menu_items
from omni.kit.primitive.mesh.evaluators import _get_all_evaluators
from omni.kit.primitive.mesh.evaluators import get_geometry_mesh_prim_list
from omni import ui
__all__ = ['MenuItemDescription', 'MeshGenerator', 'add_menu_items', 'carb', 'get_geometry_mesh_prim_list', 'omni', 'remove_menu_items', 'ui']
class MeshGenerator:
    def __init__(self):
        ...
    def _create_shape(self):
        ...
    def _reset_settings(self):
        ...
    def destroy(self):
        ...
    def on_primitive_type_selected(self, model, item):
        ...
    def register_menu(self):
        ...
    def show_setting_window(self):
        ...
