"""
This module provides a widget for editing USD light schema attributes in the Omniverse Kit user interface.
"""
from __future__ import annotations
import carb as carb
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import MultiSchemaPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget import create_primspec_bool
from pxr import Usd
from pxr import UsdLux
__all__ = ['LightSchemaAttributesWidget', 'MultiSchemaPropertiesWidget', 'PERSISTENT_SETTINGS_PREFIX', 'Usd', 'UsdLux', 'UsdPropertyUiEntry', 'carb', 'create_primspec_bool']
class LightSchemaAttributesWidget(omni.kit.property.usd.usd_property_widget.MultiSchemaPropertiesWidget):
    """
    A widget for editing light schema attributes in a user interface.
    
        This widget is designed to work with USD's lighting schemas, allowing for the manipulation of various light attributes such as color, intensity, and shadow properties. It supports a range of light types including dome, disk, rect, sphere, and cylinder lights. Custom schema attributes can also be added for more specialized control over USD light properties.
    
        Args:
            title (str): Title of the widgets on the Collapsable Frame.
            schema: The USD IsA schema or applied API schema to filter attributes.
            schema_subclasses (list): List of subclasses to include.
            include_list (list, optional): List of additional schema names to add.
            exclude_list (list, optional): List of additional schema names to remove.
    """
    def __init__(self, title: str, schema, schema_subclasses: list, include_list: list = None, exclude_list: list = None):
        """
        Initializes a new instance of LightSchemaAttributesWidget.
        """
    def _create_property(self, name: str, display_name: str, prim, has_authored_inputs):
        ...
    def _customize_props_layout(self, attrs):
        ...
    def _on_change(self, item, event_type):
        ...
    def has_authored_inputs_attr(self, prim):
        """
        Checks if given prim has authored input attributes.
        
                Args:
                    prim (:obj:`Usd.Prim`): The USD primitive to check for authored input attributes.
        
                Returns:
                    bool: True if any authored input attributes are found, False otherwise.
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (:obj:'PrimSelectionPayload'): The new payload to be handled by the widget.
        
                Returns:
                    bool: False if the payload is not handled, otherwise a list of used attributes.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
