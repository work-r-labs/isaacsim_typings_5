from __future__ import annotations
import omni as omni
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
__all__ = ['Usd', 'UsdGeom', 'UsdLux', 'get_geometry_standard_prim_list', 'get_light_prim_list', 'omni']
def get_geometry_standard_prim_list(usd_context = None):
    """
    Gets a list of pre-defined geometry types.
    
        Args:
            usd_context (omni.usd.UsdContext, optional): UsdContext for those geometries to be defined. Defaults to None.
    
        Returns:
            list: A list of pre-defined geometry types.
        
    """
def get_light_prim_list(usd_context = None):
    """
    Gets a list of pre-defined light types.
    
        Args:
            usd_context (omni.usd.UsdContext, optional): UsdContext for those lights to be defined. Defaults to None.
    
        Returns:
            list: A list of pre-defined light types.
        
    """
