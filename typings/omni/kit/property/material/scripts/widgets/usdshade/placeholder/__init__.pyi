"""
This module provides functionality to retrieve UsdShadePropertyPlaceholder objects for USD prims to drive UI components.
"""
from __future__ import annotations
import carb as carb
from omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder import UsdShadePropertyPlaceholder
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
from . import placeholder
__all__: list = ['GetPlaceholderPropertiesForPrim']
def GetPlaceholderPropertiesForPrim(prim: pxr.Usd.Prim, args: typing.Optional[dict] = {}) -> typing.List[omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder.UsdShadePropertyPlaceholder]:
    """
    Retrieves a list of UsdShadePropertyPlaceholder objects for a given USD prim.
    
        This function builds placeholders used for driving the UI by examining the
        type of USD prim provided. Depending on whether the prim is a Shader, Material,
        or NodeGraph, it delegates to the corresponding builder class to construct
        the placeholders.
    
        Args:
            prim (Usd.Prim): The USD primitive for which to retrieve property placeholders.
            args (dict): A dictionary of arguments that are passed to the builder classes.
    
        Returns:
            List[:obj:`UsdShadePropertyPlaceholder`]: A list of UsdShadePropertyPlaceholder objects
            that represent the properties of the given prim within the UI.
    
        Raises:
            A warning is logged if the provided prim is not of type Shader, Material, or NodeGraph.
        
    """
