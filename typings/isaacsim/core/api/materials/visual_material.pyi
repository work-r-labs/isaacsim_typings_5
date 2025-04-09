from __future__ import annotations
import pxr.Usd
from pxr import Usd
import pxr.UsdShade
from pxr import UsdShade
__all__ = ['Usd', 'UsdShade', 'VisualMaterial']
class VisualMaterial:
    """
    [summary]
    
        Args:
            name (str): [description]
            prim_path (str): [description]
            prim (Usd.Prim): [description]
            shaders_list (list[UsdShade.Shader]): [description]
            material (UsdShade.Material): [description]
        
    """
    def __init__(self, name: str, prim_path: str, prim: pxr.Usd.Prim, shaders_list: typing.List[pxr.UsdShade.Shader], material: pxr.UsdShade.Material) -> None:
        ...
    @property
    def material(self) -> pxr.UsdShade.Material:
        """
        [summary]
        
                Returns:
                    UsdShade.Material: [description]
                
        """
    @property
    def name(self) -> str:
        """
        [summary]
        
                Returns:
                    str: [description]
                
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        [summary]
        
                Returns:
                    Usd.Prim: [description]
                
        """
    @property
    def prim_path(self) -> str:
        """
        [summary]
        
                Returns:
                    str: [description]
                
        """
    @property
    def shaders_list(self) -> typing.List[pxr.UsdShade.Shader]:
        """
        [summary]
        
                Returns:
                    [type]: [description]
                
        """
