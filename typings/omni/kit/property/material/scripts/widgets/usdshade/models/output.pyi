"""
This module provides the UsdShadeOutputModel class to represent USD Shade Outputs in a property view, with functionality to get a string representation of the output's value.
"""
from __future__ import annotations
import omni.kit.property.usd.usd_attribute_model
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from pxr import Sdr
from pxr import UsdShade
__all__: list = ['UsdShadeOutputModel']
class UsdShadeOutputModel(omni.kit.property.usd.usd_attribute_model.UsdAttributeModel):
    """
    A class to represent a USD Shade Output in a property view.
    
        This class overrides the widget representation for a UsdShade.Output to display a simple string that indicates the output type.
        
    """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Returns a string representation of the UsdShade.Output's value.
        
                Args:
                    elide_big_array (bool): If True, elide arrays larger than a threshold.
        
                Returns:
                    str: Render type as a string.
        """
