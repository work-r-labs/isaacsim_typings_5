from __future__ import annotations
import carb as carb
from isaacsim.core.prims.impl.particle_system import ParticleSystem
from isaacsim.core.utils import prims as prim_utils
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils import stage as stage_utils
import pxr.PhysxSchema
from pxr import PhysxSchema
import pxr.Usd
from pxr import Usd
__all__ = ['ParticleSystem', 'PhysxSchema', 'SingleParticleSystem', 'Usd', 'carb', 'get_prim_at_path', 'is_prim_path_valid', 'prim_utils', 'stage_utils']
class SingleParticleSystem:
    """
    A wrapper around PhysX particle system.
    
        PhysX uses GPU-accelerated position-based-dynamics (PBD) particle simulation [1]. The particle system
        can be used to simulate fluids, cloth and inflatables [2].
    
        The wrapper is useful for creating and setting solver parameters common to the particle objects
        associated with the system. The particle system's solver parameters cannot be changed once the scene
        is playing.
    
        Note:
            CPU simulation of particles is not supported. PhysX must be simulated with GPU enabled.
    
        Reference:
            [1] https://mmacklin.com/pbf_sig_preprint.pdf
            [2] https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_physics.html#particle-simulation
        
    """
    def __init__(self, prim_path: str, name: typing.Optional[str] = 'particle_system', particle_system_enabled: typing.Optional[bool] = None, simulation_owner: typing.Optional[str] = None, contact_offset: typing.Optional[float] = None, rest_offset: typing.Optional[float] = None, particle_contact_offset: typing.Optional[float] = None, solid_rest_offset: typing.Optional[float] = None, fluid_rest_offset: typing.Optional[float] = None, enable_ccd: typing.Optional[bool] = None, solver_position_iteration_count: typing.Optional[float] = None, max_depenetration_velocity: typing.Optional[float] = None, wind: typing.Sequence[float] = None, max_neighborhood: typing.Optional[int] = None, max_velocity: typing.Optional[float] = None, global_self_collision_enabled: typing.Optional[bool] = None, non_particle_collision_enabled: typing.Optional[bool] = None):
        """
        Initializes and Applies PhysxSchema.PhysxParticleSystem to the prim at prim_path
        
                All arguments are accepted as :obj:`None`. In this case, they either have the default values from
                `PhysxParticleSystem` schema (in case a new particle system is created), or the values present in the
                existing particle system.
        
                Args:
                    prim_path (str): The path to the particle system.
                    particle_system_enabled (Optional[bool], optional): Whether to enable or disable the particle system.
                    simulation_owner (Optional[str], optional): Single PhysicsScene that simulates this particle system.
                    contact_offset (Optional[float], optional): Contact offset used for collisions with non-particle
                        objects such as rigid or deformable bodies.
                    rest_offset (Optional[float], optional): Rest offset used for collisions with non-particle objects
                        such as rigid or deformable bodies.
                    particle_contact_offset (Optional[float], optional): Contact offset used for interactions
                        between particles. Must be larger than solid and fluid rest offsets.
                    solid_rest_offset (Optional[float], optional): Rest offset used for solid-solid or solid-fluid
                        particle interactions. Must be smaller than particle contact offset.
                    fluid_rest_offset (Optional[float], optional): Rest offset used for fluid-fluid particle interactions.
                        Must be smaller than particle contact offset.
                    enable_ccd (Optional[bool], optional): Enable continuous collision detection for particles to help
                        avoid tunneling effects.
                    solver_position_iteration_count (Optional[int], optional): Number of solver iterations for position.
                    max_depenetration_velocity (Optional[float], optional): The maximum velocity permitted to be introduced
                        by the solver to depenetrate intersecting particles.
                    wind (Sequence[float], optional):The wind applied to the current particle system.
                    max_neighborhood (Optional[int], optional): The particle neighborhood size.
                    max_velocity (Optional[float], optional): Maximum particle velocity.
                    global_self_collision_enabled (Optional[bool], optional): If True, self collisions follow
                        particle-object-specific settings. If False, all particle self collisions are disabled, regardless
                        of any other settings. Improves performance if self collisions are not needed.
                    non_particle_collision_enabled (Optional[bool], optional): Enable or disable particle collision with
                        non-particle objects for all particles in the system. Improves performance if non-particle collisions
                        are not needed.
                
        """
    def apply_particle_anisotropy(self) -> pxr.PhysxSchema.PhysxParticleAnisotropyAPI:
        """
        Applies anisotropy to the particle system.
        
                This is used to compute anisotropic scaling of particles in a post-processing step.
                It only affects the rendering output including iso-surface generation.
                
        """
    def apply_particle_isotropy(self) -> pxr.PhysxSchema.PhysxParticleAnisotropyAPI:
        """
        Applies iso-surface extraction to the particle system.
        
                This is used to define settings to extract an iso-surface from the particles
                in a post-processing step. It only affects the rendering output including iso-surface generation.
                
        """
    def apply_particle_material(self, particle_materials: ParticleMaterial) -> None:
        ...
    def apply_particle_smoothing(self) -> pxr.PhysxSchema.PhysxParticleSmoothingAPI:
        """
        Applies smoothing to the simulated particle system.
        
                This is used to control smoothing of particles in a post-processing step.
                It only affects the rendering output including iso-surface generation.
                
        """
    def get_applied_particle_material(self) -> ParticleMaterial:
        ...
    def get_contact_offset(self) -> float:
        """
        
                Returns:
                    float: The contact offset  used for collisions with non-particle objects.
                
        """
    def get_enable_ccd(self) -> bool:
        """
        
                Returns:
                    bool: Whether continuous collision detection for particles is enabled or disabled.
                
        """
    def get_fluid_rest_offset(self) -> float:
        """
        
                Returns:
                    float: The rest offset used for fluid-fluid particle interactions.
                
        """
    def get_global_self_collision_enabled(self) -> bool:
        """
        
                Returns:
                    bool: Whether self collisions to follow particle-object-specific settings
                        is enabled or disabled.
                
        """
    def get_max_depenetration_velocity(self) -> None:
        """
        
                Returns:
                    float: The maximum velocity permitted between intersecting particles.
                
        """
    def get_max_neighborhood(self) -> int:
        """
        
                Returns:
                    int: The particle neighborhood size.
                
        """
    def get_max_velocity(self) -> float:
        """
        
                Returns:
                    float: The maximum particle velocity.
                
        """
    def get_particle_contact_offset(self) -> float:
        """
        
                Returns:
                    float: The contact offset used for interactions between particles.
                
        """
    def get_particle_system_enabled(self) -> bool:
        """
        
                Returns:
                    bool: Whether particle system is enabled or not.
                
        """
    def get_rest_offset(self) -> float:
        """
        
                Returns:
                    float: The rest offset used for collisions with non-particle objects.
                
        """
    def get_simulation_owner(self) -> pxr.Usd.Prim:
        """
        
                Returns:
                    Usd.Prim: The physics scene prim attached to particle system.
                
        """
    def get_solid_rest_offset(self) -> float:
        """
        
                Returns:
                    float: The rest offset used for solid-solid or solid-fluid particle interactions.
                
        """
    def get_solver_position_iteration_count(self) -> int:
        """
        
                Returns:
                    int: The number of solver iterations for positions.
                
        """
    def get_wind(self) -> typing.Sequence[float]:
        """
        
                Returns:
                    Sequence[float]: The wind applied to the current particle system.
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        ...
    def is_valid(self) -> bool:
        """
        
                Returns:
                    bool: True is the current prim path corresponds to a valid prim in stage. False otherwise.
                
        """
    def post_reset(self) -> None:
        ...
    def set_contact_offset(self, value: float) -> None:
        """
        Set the contact offset used for collisions with non-particle objects such as rigid or deformable bodies.
        
                Args:
                    value (float): The contact offset.
                
        """
    def set_enable_ccd(self, value: bool) -> None:
        """
        Enable continuous collision detection for particles.
        
                Args:
                    value (bool): Whether to enable or disable.
                
        """
    def set_fluid_rest_offset(self, value: float) -> None:
        """
        Set the rest offset used for fluid-fluid particle interactions.
        
                Note: Must be smaller than particle contact offset.
        
                Args:
                    value (float): The rest offset.
                
        """
    def set_global_self_collision_enabled(self, value: bool) -> None:
        """
        Enable self collisions to follow particle-object-specific settings.
        
                If True, self collisions follow particle-object-specific settings. If False,
                all particle self collisions are disabled, regardless of any other settings.
        
                Note: Improves performance if self collisions are not needed.
        
                Args:
                    value (bool): Whether to enable or disable.
                
        """
    def set_max_depenetration_velocity(self, value: float) -> None:
        """
        Set the maximum velocity permitted to be introduced by the solver to
                depenetrate intersecting particles.
        
                Args:
                    value (float): The maximum depenetration velocity.
                
        """
    def set_max_neighborhood(self, value: int) -> None:
        """
        Set the particle neighborhood size.
        
                Args:
                    value (int): The neighborhood size.
                
        """
    def set_max_velocity(self, value: float) -> None:
        """
        Set the maximum particle velocity.
        
                Args:
                    value (float): The maximum velocity.
                
        """
    def set_particle_contact_offset(self, value: float) -> None:
        """
        Set the contact offset used for interactions between particles.
        
                Note: Must be larger than solid and fluid rest offsets.
        
                Args:
                    value (float): The contact offset.
                
        """
    def set_particle_system_enabled(self, value: bool) -> None:
        """
        Set enabling of the particle system.
        
                Args:
                    value (bool): Whether to enable or disable.
                
        """
    def set_rest_offset(self, value: float) -> None:
        """
        Set the rest offset used for collisions with non-particle objects such as rigid or deformable bodies.
        
                Args:
                    value (float): The rest offset.
                
        """
    def set_simulation_owner(self, value: str) -> None:
        """
        Set the PhysicsScene that simulates this particle system.
        
                Args:
                    value (str): The prim path to the physics scene.
                
        """
    def set_solid_rest_offset(self, value: float) -> None:
        """
        Set the rest offset used for solid-solid or solid-fluid particle interactions.
        
                Note: Must be smaller than particle contact offset.
        
                Args:
                    value (float): The rest offset.
                
        """
    def set_solver_position_iteration_count(self, value: int) -> None:
        """
        Set the number of solver iterations for position.
        
                Args:
                    value (int): Number of solver iterations.
                
        """
    def set_wind(self, value: typing.Sequence[float]) -> None:
        """
        Set the wind velocity applied to the current particle system.
        
                Args:
                    value (Sequence[float]): The wind applied to the current particle system.
                
        """
    @property
    def name(self) -> typing.Optional[str]:
        """
        
                Returns:
                    str: name given to the prim when instantiating it. Otherwise None.
                
        """
    @property
    def particle_system(self) -> pxr.PhysxSchema.PhysxParticleSystem:
        """
        
                Returns:
                    PhysxSchema.PhysxParticleSystem: The particle system.
                
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
                    str: The stage path to the particle system.
                
        """
