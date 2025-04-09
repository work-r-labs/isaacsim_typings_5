from __future__ import annotations
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import MultiSchemaPropertiesWidget
from pxr import UsdRender
__all__ = ['MultiSchemaPropertiesWidget', 'ProductSchemaAttributesWidget', 'UsdRender']
class ProductSchemaAttributesWidget(omni.kit.property.usd.usd_property_widget.MultiSchemaPropertiesWidget):
    def _customize_props_layout(self, attrs):
        ...
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
