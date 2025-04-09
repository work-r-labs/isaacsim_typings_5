from __future__ import annotations
import omni as omni
from omni.kit.property.usd.usd_property_widget import MultiSchemaPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget import create_primspec_bool
from omni.kit.property.usd.usd_property_widget import create_primspec_float
from omni.kit.property.usd.usd_property_widget import create_primspec_string
from omni.kit.property.usd.usd_property_widget import create_primspec_token
from pxr import Sdf
from pxr import UsdGeom
from pxr import Vt
__all__ = ['CameraPropertyExtension', 'CameraSchemaAttributesWidget', 'MultiSchemaPropertiesWidget', 'Sdf', 'UsdGeom', 'UsdPropertyUiEntry', 'Vt', 'create_primspec_bool', 'create_primspec_float', 'create_primspec_string', 'create_primspec_token', 'omni']
class CameraPropertyExtension(omni.ext._extensions.IExt):
    def __init__(self):
        ...
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
class CameraSchemaAttributesWidget(omni.kit.property.usd.usd_property_widget.MultiSchemaPropertiesWidget):
    """
    A widget for editing and displaying camera schema attributes within a property window.
    
        This widget is designed to manage and display properties specific to camera schemas, including standard attributes and custom fisheye lens settings. It supports filtering attributes based on the schema, including or excluding specific ones, and adds custom schema attributes related to camera projection types and sensor models.
    
            Args:
                title (str): Title of the widgets on the Collapsable Frame.
                schema: The USD IsA schema or applied API schema to filter attributes.
                schema_subclasses (list): List of subclasses to include in the schema filtering.
                include_list (list, optional): List of additional schema names to add to the filter. Defaults to None.
                exclude_list (list, optional): List of schema names to remove from the filter. Defaults to None.
    """
    def __init__(self, title: str, schema, schema_subclasses: list, include_list: list = None, exclude_list: list = None):
        """
        Initialize the widget.
        """
    def _customize_props_layout(self, attrs):
        ...
    def get_additional_kwargs(self, ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry):
        """
        Get additional kwargs for building the label or UI widget.
        
                Args:
                    ui_prop (UsdPropertyUiEntry): The UI property entry to process.
                
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (dict): The new payload to be handled by the widget.
                
        """
