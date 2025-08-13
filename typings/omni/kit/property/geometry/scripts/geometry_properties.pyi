from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from pxr import Sdf
from pxr import Tf
import pxr.Tf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUI
import typing
from typing import Any
__all__: list[str] = ['Any', 'GeometryPropertyExtension', 'PrimSelectionPayload', 'Sdf', 'Tf', 'Usd', 'UsdGeom', 'UsdUI', 'carb', 'deregister_custom_visual_attribute', 'get_instance', 'omni', 'partial', 'register_custom_visual_attribute']
class GeometryPropertyExtension(omni.ext._extensions.IExt):
    """
    A class for extending and modifying geometry properties in the USD stage.
    
        This extension registers widgets and menu entries to manage geometry and visual attributes associated with prims. It integrates with the application window to provide interactive controls for toggling various rendering and property settings such as instanceable state, wireframe display, and shadow properties, among others. The extension also supports the registration of custom visual attributes, allowing dynamic updates to prim properties based on user interaction.
    
        Designed to interface with the Omniverse Kit SDK, the class carefully validates prim selection and type before executing property commands. It leverages the underlying command system to update attribute states and ensures the property widgets are correctly registered and unregistered during the extension lifecycle.
    
        Example usage:
        .. code-block:: python
    
            extension = GeometryPropertyExtension()
            extension.on_startup('my_extension')
        
    """
    def __init__(self):
        """
        Initializes a new GeometryPropertyExtension instance.
        """
    def _click_set_primvar(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, prim_name: str):
        ...
    def _click_toggle_instanceable(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload):
        ...
    def _get_primvar_state(self, objects: dict, prim_name: str, text_prefix: str = '', text_name: str = '') -> str:
        ...
    def _is_prim_selected(self, objects: dict):
        """
        
                Checks if any prims are selected
                
        """
    def _prim_is_type(self, objects: dict, prim_type: pxr.Tf.Type) -> bool:
        """
        
                Checks if prims are given class/schema
                
        """
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def deregister_custom_visual_attribute(self, attribute_name: str):
        """
        Removes the custom visual attribute from the visual property widget.
        
                Args:
                    attribute_name (str): Name of the attribute to remove.
                
        """
    def on_shutdown(self):
        """
        Handles shutdown operations by unregistering widgets and releasing the extension instance.
        """
    def on_startup(self, ext_id):
        """
        Handles startup operations including widget registration and menu entry creation.
        
                Args:
                    ext_id (str): Extension identifier for startup configuration.
                
        """
    def register_custom_visual_attribute(self, attribute_name: str, display_name: str, type_name: str, default_value: typing.Any, predicate: typing.Callable[[typing.Any], bool] = None):
        """
        Add custom attribute with placeholder.
        
                Args:
                    attribute_name (str): Name of the attribute.
                    display_name (str): Display name for the attribute.
                    type_name (str): Type name of the attribute.
                    default_value (Any): Default value assigned to the attribute.
                    predicate (Callable[[Any], bool]): Function returning a boolean for attribute condition.
                
        """
def deregister_custom_visual_attribute(attribute_name: str):
    ...
def get_instance():
    """
    Return the current instance of the extension.
    
        Returns:
            Any: The current extension instance if set; otherwise, None.
        
    """
def register_custom_visual_attribute(attribute_name: str, display_name: str, type_name: str, default_value: typing.Any, predicate: typing.Callable[[typing.Any], bool] = None):
    ...
_extension_instance: GeometryPropertyExtension  # value = <omni.kit.property.geometry.scripts.geometry_properties.GeometryPropertyExtension object>
