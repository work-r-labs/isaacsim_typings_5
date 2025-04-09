"""
This module provides a UsdShadeShaderWidget class for representing and interacting with USD Shade shaders in a user interface.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.material.scripts.widgets.usdshade.base_widget import UsdShadeBaseWidget
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
import pxr.Sdf
from pxr import Sdf
from pxr import UsdShade
__all__: list = ['UsdShadeShaderWidget']
class UsdShadeShaderWidget(omni.kit.property.material.scripts.widgets.usdshade.base_widget.UsdShadeBaseWidget):
    """
    A widget class for representing and interacting with USD Shade shaders.
    
        This widget is specifically designed for working with shading elements within a USD scene. It extends the capabilities of the UsdShadeBaseWidget to provide a user interface component that allows for the selection and manipulation of Shader prims. The widget can be titled for context within the UI.
    
        Args:
            title (str): The title of the shader widget. Defaults to 'Shader'.
    """
    def __init__(self, title: str = 'Shader'):
        """
        Initializes the UsdShadeShaderWidget.
        """
    def _on_info_property_changed(self, changed_property_name: str) -> None:
        """
        
                If 'info:mdl:sourceAsset' property has changed, clear 'info:mdl:sourceAsset:subIdentifier'
                
        """
    def _path_requires_rebuild(self, path: pxr.Sdf.Path) -> bool:
        """
        
                If one of the info: attributes has changed, we will force a rebuild of the widget.
                
        """
    def on_new_payload(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload) -> bool:
        """
        Processes the given payload and updates the shader widget if necessary.
        
                Args:
                    payload (:obj:`PrimSelectionPayload`): The payload containing prims to represent.
        
                Returns:
                    bool: True if the prims can be represented, False otherwise.
        """
