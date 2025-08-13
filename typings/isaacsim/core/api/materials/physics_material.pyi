from __future__ import annotations
import carb as carb
from isaacsim.core.utils import stage as stage_utils
import omni as omni
from pxr import Usd
import pxr.Usd
from pxr import UsdPhysics
import pxr.UsdShade
from pxr import UsdShade
__all__: list[str] = ['PhysicsMaterial', 'Usd', 'UsdPhysics', 'UsdShade', 'carb', 'omni', 'stage_utils']
class PhysicsMaterial:
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "physics_material".
            static_friction (Optional[float], optional): [description]. Defaults to None.
            dynamic_friction (Optional[float], optional): [description]. Defaults to None.
            restitution (Optional[float], optional): [description]. Defaults to None.
        
    """
    def __init__(self, prim_path: str, name: str = 'physics_material', static_friction: typing.Optional[float] = None, dynamic_friction: typing.Optional[float] = None, restitution: typing.Optional[float] = None) -> None:
        ...
    def get_dynamic_friction(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def get_restitution(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def get_static_friction(self) -> float:
        """
        [summary]
        
                Returns:
                    float: [description]
                
        """
    def set_dynamic_friction(self, friction: float) -> None:
        """
        [summary]
        
                Args:
                    friction (float): [description]
                
        """
    def set_restitution(self, restitution: float) -> None:
        """
        [summary]
        
                Args:
                    restitution (float): [description]
                
        """
    def set_static_friction(self, friction: float) -> None:
        """
        [summary]
        
                Args:
                    friction (float): [description]
                
        """
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
