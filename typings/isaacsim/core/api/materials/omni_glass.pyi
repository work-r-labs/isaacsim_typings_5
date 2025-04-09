from __future__ import annotations
import carb as carb
import isaacsim.core.api.materials.visual_material
from isaacsim.core.api.materials.visual_material import VisualMaterial
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.prims import move_prim
import numpy as np
import numpy
import omni as omni
from pxr import Gf
from pxr import Sdf
from pxr import UsdShade
__all__ = ['Gf', 'OmniGlass', 'Sdf', 'UsdShade', 'VisualMaterial', 'carb', 'get_prim_at_path', 'is_prim_path_valid', 'move_prim', 'np', 'omni']
class OmniGlass(isaacsim.core.api.materials.visual_material.VisualMaterial):
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "omni_glass".
            shader (Optional[UsdShade.Shader], optional): [description]. Defaults to None.
            color (Optional[np.ndarray], optional): [description]. Defaults to None.
            ior (Optional[float], optional): [description]. Defaults to None.
            depth (Optional[float], optional): [description]. Defaults to None.
            thin_walled (Optional[bool], optional): [description]. Defaults to None.
    
        Raises:
            Exception: [description]
        
    """
    def __init__(self, prim_path: str, name: str = 'omni_glass', shader: typing.Optional[pxr.UsdShade.Shader] = None, color: typing.Optional[numpy.ndarray] = None, ior: typing.Optional[float] = None, depth: typing.Optional[float] = None, thin_walled: typing.Optional[bool] = None) -> None:
        ...
    def get_color(self) -> typing.Optional[numpy.ndarray]:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_depth(self) -> typing.Optional[float]:
        ...
    def get_ior(self) -> typing.Optional[float]:
        ...
    def get_thin_walled(self) -> typing.Optional[float]:
        ...
    def set_color(self, color: numpy.ndarray) -> None:
        """
        [summary]
        
                Args:
                    color (np.ndarray): [description]
                
        """
    def set_depth(self, depth: float) -> None:
        ...
    def set_ior(self, ior: float) -> None:
        ...
    def set_thin_walled(self, thin_walled: float) -> None:
        ...
