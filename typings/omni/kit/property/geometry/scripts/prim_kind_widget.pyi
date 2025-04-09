from __future__ import annotations
import carb as carb
from omni.kit.property.usd.usd_object_model import MetadataObjectModel
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni import ui
from pxr import Kind
from pxr import Usd
from pxr import UsdGeom
import typing
__all__ = ['Constant', 'HORIZONTAL_SPACING', 'Kind', 'MetadataObjectModel', 'PrimKindWidget', 'Usd', 'UsdGeom', 'UsdPropertiesWidget', 'UsdPropertiesWidgetBuilder', 'carb', 'ui']
class Constant:
    FONT_SIZE: typing.ClassVar[float] = 14.0
    MIXED: typing.ClassVar[str] = 'Mixed'
    MIXED_COLOR: typing.ClassVar[int] = 4291599969
    def __setattr__(self, name, value):
        ...
class PrimKindWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    def __init__(self):
        ...
    def _get_prim(self, prim_path):
        ...
    def _get_shared_properties_from_selected_prims(self, anchor_prim):
        ...
    def build_items(self):
        ...
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
    def reset(self):
        ...
HORIZONTAL_SPACING: int = 4
