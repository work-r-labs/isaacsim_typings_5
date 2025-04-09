from __future__ import annotations
import carb as carb
import isaacsim.core.api.materials.visual_material
from isaacsim.core.api.materials.visual_material import VisualMaterial
import numpy as np
import numpy
import omni as omni
from pxr import Gf
from pxr import Sdf
from pxr import UsdShade
__all__ = ['Gf', 'PreviewSurface', 'Sdf', 'UsdShade', 'VisualMaterial', 'carb', 'np', 'omni']
class PreviewSurface(isaacsim.core.api.materials.visual_material.VisualMaterial):
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "preview_surface".
            shader (Optional[UsdShade.Shader], optional): [description]. Defaults to None.
            color (Optional[np.ndarray], optional): [description]. Defaults to None.
            roughness (Optional[float], optional): [description]. Defaults to None.
            metallic (Optional[float], optional): [description]. Defaults to None.
        
    """
    def __init__(self, prim_path: str, name: str = 'preview_surface', shader: typing.Optional[pxr.UsdShade.Shader] = None, color: typing.Optional[numpy.ndarray] = None, roughness: typing.Optional[float] = None, metallic: typing.Optional[float] = None) -> None:
        ...
    def get_color(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_metallic(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def get_roughness(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def set_color(self, color: numpy.ndarray) -> None:
        """
        [summary]
        
                Args:
                    color (np.ndarray): [description]
                
        """
    def set_metallic(self, metallic: float) -> None:
        """
        [summary]
        
                Args:
                    metallic (float): [description]
                
        """
    def set_roughness(self, roughness: float) -> None:
        """
        [summary]
        
                Args:
                    roughness (float): [description]
                
        """
