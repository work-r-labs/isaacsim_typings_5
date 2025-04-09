"""
This module defines classes for managing property schemes of material and shader prims in a USD stage, providing functionality to determine appropriate UI widgets.
"""
from __future__ import annotations
import omni.kit.window.property.property_scheme_delegate
from omni.kit.window.property.property_scheme_delegate import PropertySchemeDelegate
from pxr import UsdShade
__all__ = ['MaterialPrimSchemeDelegate', 'PropertySchemeDelegate', 'ShaderPrimSchemeDelegate', 'UsdShade']
class MaterialPrimSchemeDelegate(omni.kit.window.property.property_scheme_delegate.PropertySchemeDelegate):
    """
    A delegate class for managing the property scheme of material prims in a USD stage.
    
        This class inherits from PropertySchemeDelegate and provides specific implementations for determining which widgets to enable or disable based on the properties of material prims. It's tailored to work with the unique requirements of material prims by implementing custom logic within its methods.
        
    """
    def _should_enable_delegate(self, payload):
        ...
    def get_unwanted_widgets(self, payload):
        """
        Returns a list of unwanted widgets based on the payload.
        
                Args:
                    payload (dict): The payload based on which unwanted widgets are determined.
        
                Returns:
                    list: A list of unwanted widget names.
        """
    def get_widgets(self, payload):
        """
        Returns a list of widgets to be built based on the payload.
        
                Args:
                    payload (dict): The payload based on which widgets are determined.
        
                Returns:
                    list: A list of widget names to build.
        """
class ShaderPrimSchemeDelegate(omni.kit.window.property.property_scheme_delegate.PropertySchemeDelegate):
    """
    A class for managing property scheme delegation for Shader prims.
    
        This class is responsible for determining the appropriate widgets to display
        in a UI based on the Shader prim's properties within a USD stage. It extends the
        PropertySchemeDelegate interface to tailor widget selection for Shader prims specifically.
    """
    def _should_enable_delegate(self, payload):
        ...
    def get_unwanted_widgets(self, payload):
        """
        Returns a list of unwanted widgets based on the payload.
        
                Args:
                    payload (dict): The payload containing necessary information.
        
                Returns:
                    list: A list containing the names of unwanted widgets.
        """
    def get_widgets(self, payload):
        """
        Returns a list of widgets to be built based on the payload.
        
                Args:
                    payload (dict): The payload containing necessary information.
        
                Returns:
                    list: A list containing the names of widgets to be built.
        """
