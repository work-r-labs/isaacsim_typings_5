from __future__ import annotations
import omni as omni
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni import ui
import pathlib
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
__all__ = ['ADD_BUTTON_STYLE', 'ArrayBaseItem', 'ArrayPropertiesWidget', 'ArrayWidgetBuilder', 'BaseMultiField', 'CustomMultiFloatField', 'CustomMultiIntField', 'Gf', 'HORIZONTAL_SPACING', 'ICON_PATH', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'REMOVE_BUTTON_STYLE', 'Sdf', 'Tf', 'Usd', 'UsdArrayAttributeModel', 'UsdAttributeModel', 'UsdPropertiesWidget', 'UsdPropertiesWidgetBuilder', 'UsdPropertyUiEntry', 'omni', 'style', 'ui']
class ArrayBaseItem:
    def __init__(self, type_name, model, index = None, frame = None):
        ...
    def create_list_item(self, button_style, callback):
        ...
class ArrayPropertiesWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    @classmethod
    def _array_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    def _filter_props_to_build(self, props):
        ...
    def build_property_item(self, stage, ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry, prim_paths: typing.List[pxr.Sdf.Path]):
        ...
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
class ArrayWidgetBuilder:
    def __init__(self, stage, attr_name, type_name, model):
        ...
    def _create_edit_window(self):
        ...
class BaseMultiField:
    def __init__(self, model, index, count, frame, button_style, callback, field_type, default):
        ...
    def append(self):
        ...
    def get_tuple(self):
        ...
    def remove(self):
        ...
class CustomMultiFloatField(BaseMultiField):
    def __init__(self, model, index, count, frame, button_style, callback):
        ...
    def get_field_value(self, index):
        ...
class CustomMultiIntField(BaseMultiField):
    def __init__(self, model, index, count, frame, button_style, callback):
        ...
    def get_field_value(self, index):
        ...
class UsdArrayAttributeModel(omni.kit.property.usd.usd_attribute_model.UsdAttributeModel):
    def add_item(self, item):
        ...
    def get_item(self, index):
        ...
    def get_length(self):
        ...
    def get_value(self):
        ...
    def remove_item(self, index):
        ...
    def set_item(self, index, item):
        ...
ADD_BUTTON_STYLE: dict = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/plus.svg', 'margin': 1, 'padding': 0}
HORIZONTAL_SPACING: int = 4
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons')
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
REMOVE_BUTTON_STYLE: dict = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/remove.svg', 'margin': 0, 'padding': 0}
style: dict = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/plus.svg', 'margin': 1, 'padding': 0}
