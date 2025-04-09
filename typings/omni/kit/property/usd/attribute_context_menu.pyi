from __future__ import annotations
import carb as carb
import contextlib as contextlib
from functools import partial
import omni as omni
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeModel
from omni.kit.property.usd.usd_attribute_model import MdlEnumAttributeModel
from omni.kit.property.usd.usd_attribute_model import TfTokenAttributeModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.usd.layers._impl.extension import get_layers
from omni.kit.usd.layers._omni_kit_usd_layers import LayerEditMode
from pxr import Sdf
from pxr import UsdUtils
import typing
import usdrt as usdrt
import weakref as weakref
__all__: list = list()
class AttributeContextMenu:
    _instance: typing.ClassVar[AttributeContextMenu]  # value = <omni.kit.property.usd.attribute_context_menu.AttributeContextMenu object>
    @classmethod
    def get_instance(cls):
        ...
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _link_attributes(self, link_or_unlink, layer_identifier, objects):
        ...
    def _lock_attributes(self, lock_or_unlock, objects):
        ...
    def _register_context_menus(self):
        ...
    def _register_copy_paste_menus(self):
        ...
    def _register_copy_prop_path_menu(self):
        ...
    def _register_delete_prop_menu(self):
        ...
    def destroy(self):
        ...
    def on_mouse_event(self, event: AttributeContextMenuEvent):
        ...
class AttributeContextMenuEvent:
    def __init__(self, widget, attribute_paths, stage, time_code, model, comp_index):
        ...
