from __future__ import annotations
import carb as carb
from isaacsim.core.api.materials.particle_material_view import ParticleMaterialView
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
from isaacsim.core.utils import prims as prim_utils
from isaacsim.core.utils import stage as stage_utils
import omni as omni
from pxr import PhysxSchema
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import pxr.UsdShade
__all__ = ['ParticleMaterial', 'ParticleMaterialView', 'PhysxSchema', 'SimulationContext', 'Usd', 'UsdShade', 'carb', 'omni', 'prim_utils', 'stage_utils']
class ParticleMaterial:
    """
    A wrapper around position-based-dynamics (PBD) material for particles used to
        simulate fluids, cloth and inflatables.
    
        Note:
            Currently, only a single material per particle system is supported which applies
            to all objects that are associated with the system.
        
    """
    def __init__(self, prim_path: str, name: typing.Optional[str] = 'particle_material', friction: typing.Optional[float] = None, particle_friction_scale: typing.Optional[float] = None, damping: typing.Optional[float] = None, viscosity: typing.Optional[float] = None, vorticity_confinement: typing.Optional[float] = None, surface_tension: typing.Optional[float] = None, cohesion: typing.Optional[float] = None, adhesion: typing.Optional[float] = None, particle_adhesion_scale: typing.Optional[float] = None, adhesion_offset_scale: typing.Optional[float] = None, gravity_scale: typing.Optional[float] = None, lift: typing.Optional[float] = None, drag: typing.Optional[float] = None):
        """
        Applies the `PhysxSchema.PhysxPBDMaterialAPI` to a material prim.
                Note:
                    If a prim does not exist at specified path, then a new UsdShade.Material prim is created.
        
                Args:
                    prim_path (str): The prim path to create/apply PBD material properties.
                    friction (float, optional): The friction coefficient.
                    particle_friction_scale (float, optional): The coefficient that scales friction for
                        solid particle-particle interactions.
                    damping (float, optional): The global velocity damping coefficient
                    viscosity (float, optional): The viscosity of fluid particles.
                    vorticity_confinement (float, optional): The vorticity confinement for fluid particles.
                    surface_tension (float, optional): The surface tension.
                    cohesion (float, optional): The cohesion for interaction between fluid particles.
                    adhesion (float, optional): The adhesion for interaction between particles (solid or fluid),
                        and rigid or deformable objects.
                    particle_adhesion_scale (float, optional): The coefficient that scales adhesion for solid
                        particle-particle iterations.
                    adhesion_offset_scale (float, optional): The offset scale defines at which adhesion ceases
                        to take effect.
                    gravity_scale (float, optional): The gravitational acceleration scaling factor. It can be used
                        to approximate lighter-than-air inflatables.
                    lift (float, optional): The lift coefficient for cloth and inflatable particle objects.
                    drag (float, optional): The drag coefficient for cloth and inflatable particle objects.
                
        """
    def get_adhesion(self) -> float:
        """
        
                Returns:
                    float: The adhesion for interaction between particles (solid or fluid), and rigids or deformables.
                
        """
    def get_adhesion_offset_scale(self) -> float:
        """
        
                Returns:
                    float: The adhesion offset scale.
                
        """
    def get_cohesion(self) -> float:
        """
        
                Returns:
                    float: The cohesion for interaction between fluid particles.
                
        """
    def get_damping(self) -> float:
        """
        
                Returns:
                    float: The global velocity damping coefficient.
                
        """
    def get_drag(self) -> float:
        """
        
                Returns:
                    float: The drag coefficient, basic aerodynamic drag model coefficient.
                
        """
    def get_friction(self) -> float:
        """
        
                Returns:
                    float: The friction coefficient.
                
        """
    def get_gravity_scale(self) -> float:
        """
        
                Returns:
                    float: The gravitational acceleration scaling factor.
                
        """
    def get_lift(self) -> float:
        """
        
                Returns:
                    float: The lift coefficient, basic aerodynamic lift model coefficient.
                
        """
    def get_particle_adhesion_scale(self) -> float:
        """
        
                Returns:
                    float: The particle adhesion scale.
                
        """
    def get_particle_friction_scale(self) -> float:
        """
        
                Returns:
                    float: The particle friction scale.
                
        """
    def get_surface_tension(self) -> float:
        """
        
                Returns:
                    float: The surface tension for fluid particles.
                
        """
    def get_viscosity(self) -> float:
        """
        
                Returns:
                    float: The viscosity.
                
        """
    def get_vorticity_confinement(self) -> float:
        """
        
                Returns:
                    float: The vorticity confinement for fluid particles.
                
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
    def set_adhesion(self, value: float) -> None:
        """
        Sets the adhesion for interaction between particles (solid or fluid), and rigid or deformable objects.
        
                Note:
                    Adhesion also applies to solid-solid particle interactions, but is multiplied with the
                    particle adhesion scale.
        
                Args:
                    value (float): The adhesion.
                        Range: [0, inf), Units: dimensionless
        
                
        """
    def set_adhesion_offset_scale(self, value: float) -> None:
        """
        Sets the adhesion offset scale.
        
                It defines the offset at which adhesion ceases to take effect. For interactions between
                particles (fluid or solid), and rigids or deformables, the adhesion offset is defined
                relative to the rest offset. For solid particle-particle interactions, the adhesion
                offset is defined relative to the solid rest offset.
        
                Args:
                    value (float): The adhesion offset scale.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_cohesion(self, value: float) -> None:
        """
        Sets the cohesion for interaction between fluid particles.
        
                Args:
                    value (float): The cohesion.
                        Range: [0, inf), Units: dimensionless
        
                
        """
    def set_damping(self, value: float) -> None:
        """
        Sets the global velocity damping coefficient.
        
                Args:
                    value (float): The damping coefficient.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_drag(self, value: float) -> None:
        """
        Sets the drag coefficient, i.e. basic aerodynamic drag model coefficient.
        
                It is useful for cloth and inflatable particle objects.
        
                Args:
                    value (float): The drag coefficient.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_friction(self, value: float) -> None:
        """
        Sets the friction coefficient.
        
                The friction takes effect in all interactions between particles and rigids or deformables.
                For solid particle-particle interactions it is multiplied by the particle friction scale.
        
                Args:
                    value (float): The friction coefficient.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_gravity_scale(self, value: float) -> None:
        """
        Sets the gravitational acceleration scaling factor.
        
                It can be used to approximate lighter-than-air inflatable.
                For example (-1.0 would invert gravity).
        
                Args:
                    value (float): The gravity scale.
                        Range: (-inf , inf), Units: dimensionless
                
        """
    def set_lift(self, value: float) -> None:
        """
        Sets the lift coefficient, i.e. basic aerodynamic lift model coefficient.
        
                It is useful for cloth and inflatable particle objects.
        
                Args:
                    value (float): The lift coefficient.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_particle_adhesion_scale(self, value: float) -> None:
        """
        Sets the particle adhesion scale.
        
                This coefficient scales the adhesion for solid particle-particle interaction.
        
                Args:
                    value (float): The adhesion scale.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_particle_friction_scale(self, value: float) -> None:
        """
        Sets the particle friction scale.
        
                The coefficient that scales friction for solid particle-particle interaction.
        
                Args:
                    value (float): The particle friction scale.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_surface_tension(self, value: float) -> None:
        """
        Sets the surface tension for fluid particles.
        
                Args:
                    value (float): The surface tension.
                        Range: [0, inf), Units: 1 / (distance * distance * distance)
                
        """
    def set_viscosity(self, value: float) -> None:
        """
        Sets the viscosity for fluid particles.
        
                Args:
                    value (float): The viscosity.
                        Range: [0, inf), Units: dimensionless
                
        """
    def set_vorticity_confinement(self, value: float) -> None:
        """
        Sets the vorticity confinement for fluid particles.
        
                This helps prevent energy loss due to numerical solver by adding vortex-like
                accelerations to the particles.
        
                Args:
                    value (float): The vorticity confinement.
                        Range: [0, inf), Units: dimensionless
                
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
