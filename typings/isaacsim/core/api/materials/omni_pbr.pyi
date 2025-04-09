from __future__ import annotations
import carb as carb
import isaacsim.core.api.materials.visual_material
from isaacsim.core.api.materials.visual_material import VisualMaterial
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
import numpy as np
import numpy
from pxr import Gf
from pxr import Sdf
from pxr import UsdShade
__all__ = ['Gf', 'OmniPBR', 'Sdf', 'UsdShade', 'VisualMaterial', 'carb', 'get_current_stage', 'get_prim_at_path', 'is_prim_path_valid', 'np']
class OmniPBR(isaacsim.core.api.materials.visual_material.VisualMaterial):
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "omni_pbr".
            shader (Optional[UsdShade.Shader], optional): [description]. Defaults to None.
            texture_path (Optional[str], optional): [description]. Defaults to None.
            texture_scale (Optional[np.ndarray], optional): [description]. Defaults to None.
            texture_translate (Optional[np.ndarray, optional): [description]. Defaults to None.
            color (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    def __init__(self, prim_path: str, name: str = 'omni_pbr', shader: typing.Optional[pxr.UsdShade.Shader] = None, texture_path: typing.Optional[str] = None, texture_scale: typing.Optional[numpy.ndarray] = None, texture_translate: typing.Optional[numpy.ndarray] = None, color: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def get_color(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_metallic_constant(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def get_project_uvw(self) -> bool:
        """
        [summary]
        
                Returns:
                    bool: [description]
                
        """
    def get_reflection_roughness(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def get_texture(self) -> str:
        """
        [summary]
        
                Returns:
                    str: [description]
                
        """
    def get_texture_scale(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_texture_translate(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def set_color(self, color: numpy.ndarray) -> None:
        """
        [summary]
        
                Args:
                    color (np.ndarray): [description]
                
        """
    def set_metallic_constant(self, amount: float) -> None:
        """
        [summary]
        
                Args:
                    amount (float): [description]
                
        """
    def set_project_uvw(self, flag: bool) -> None:
        """
        [summary]
        
                Args:
                    flag (bool): [description]
                
        """
    def set_reflection_roughness(self, amount: float) -> None:
        """
        [summary]
        
                Args:
                    amount (float): [description]
                
        """
    def set_texture(self, path: str) -> None:
        """
        [summary]
        
                Args:
                    path (str): [description]
                
        """
    def set_texture_scale(self, x: float, y: float) -> None:
        """
        [summary]
        
                Args:
                    x (float): [description]
                    y (float): [description]
                
        """
    def set_texture_translate(self, x: float, y: float) -> None:
        """
        [summary]
        
                Args:
                    x (float): [description]
                    y (float): [description]
                
        """
