from __future__ import annotations
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.property.usd.variants_model import VariantSetModel
from omni import ui
from pxr import Tf
from pxr import Usd
__all__: list = ['VariantsWidget']
class VariantsWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    def __init__(self):
        ...
    def _build_variant_set(self, stage, prim_path, name):
        ...
    def build_items(self):
        ...
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
    def reset(self):
        ...
