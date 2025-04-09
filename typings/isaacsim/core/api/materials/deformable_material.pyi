from __future__ import annotations
import carb as carb
from isaacsim.core.api.materials.deformable_material_view import DeformableMaterialView
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
from isaacsim.core.utils import prims as prim_utils
from isaacsim.core.utils import stage as stage_utils
import omni as omni
from pxr import PhysxSchema
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import pxr.UsdShade
__all__ = ['DeformableMaterial', 'DeformableMaterialView', 'PhysxSchema', 'SimulationContext', 'Usd', 'UsdShade', 'carb', 'omni', 'prim_utils', 'stage_utils']
class DeformableMaterial:
    """
    A wrapper around deformable material used to simulate soft bodies.
    """
    def __init__(self, prim_path: str, name: typing.Optional[str] = 'deformable_material', dynamic_friction: typing.Optional[float] = None, youngs_modulus: typing.Optional[float] = None, poissons_ratio: typing.Optional[float] = None, elasticity_damping: typing.Optional[float] = None, damping_scale: typing.Optional[float] = None):
        """
        Applies the PhysxSchema.PhysxDeformableSurfaceMaterialAPI to the prim at path
                Note:
                    If a prim does not exist at specified path, then a new UsdShade.Material prim is created.
        
                Args:
                    prim_path (str): The prim path to create/apply deformable material properties.
                    dynamic_friction (float, optional): The dynamic friction coefficient in range [0, inf)
                    youngs_modulus (float, optional): The Young's modulus coefficient controlling stiffness of the bodies in range [0, inf)
                    poissons_ratio (float, optional): The Possion ratio coefficient that is related to volume preservation in range [0, 0.5)
                    elasticity_damping (float, optional): Material damping parameter in [0, inf)
                    damping_scale (float, optional): The damping scale coefficient in [0, 1]
                
        """
    def get_damping_scale(self) -> float:
        """
        
                Returns:
                    float: The damping scale coefficient.
                
        """
    def get_dynamic_friction(self) -> float:
        """
        
                Returns:
                    float: The dynamic friction coefficient.
                
        """
    def get_elasticity_damping(self) -> float:
        """
        
                Returns:
                    float: The elasticity damping coefficient.
                
        """
    def get_poissons_ratio(self) -> float:
        """
        
                Returns:
                    float: The poissons ratio.
                
        """
    def get_youngs_modululs(self) -> float:
        """
        
                Returns:
                    float: The youngs modululs coefficient.
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        ...
    def is_valid(self) -> bool:
        """
        
                Returns:
                    bool: True is the current prim path corresponds to a valid prim in stage. False otherwise.
                
        """
    def post_reset(self) -> None:
        """
        Resets the prim to its default state.
        """
    def set_damping_scale(self, value: float) -> None:
        """
        Sets the damping scale coefficient.
        
                Args:
                    value (float): The damping scale coefficient Range: [0, inf)
                
        """
    def set_dynamic_friction(self, value: float) -> None:
        """
        Sets the dynamic_friction coefficient.
        
                The dynamic_friction takes effect in all interactions between particles and rigids or deformables.
                For solid particle-particle interactions it is multiplied by the particle dynamic_friction scale.
        
                Args:
                    value (float): The dynamic_friction coefficient. Range: [0, inf), Units: dimensionless
                
        """
    def set_elasticity_damping(self, value: float) -> None:
        """
        Sets the global velocity elasticity damping coefficient.
        
                Args:
                    value (float): The elasticity damping coefficient.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_poissons_ratio(self, value: float) -> None:
        """
        Sets the poissons ratio coefficient
        
                Args:
                    value (float): The poissons ratio. Range: (0 , 0.5)
                
        """
    def set_youngs_modululs(self, value: float) -> None:
        """
        Sets the youngs_modululs for fluid particles.
        
                Args:
                    value (float): The youngs_modululs. Range: [0, inf)
                
        """
    @property
    def material(self) -> pxr.UsdShade.Material:
        """
        
                Returns:
                    UsdShade.Material: The USD Material object.
                
        """
    @property
    def name(self) -> typing.Optional[str]:
        """
        
                Returns:
                    str: name given to the prim when instantiating it. Otherwise None.
                
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        
                Returns:
                    Usd.Prim: The USD prim present.
                
        """
    @property
    def prim_path(self) -> str:
        """
        
                Returns:
                    str: The stage path to the material.
                
        """
