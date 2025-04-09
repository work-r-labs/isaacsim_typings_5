from __future__ import annotations
import carb as carb
from isaacsim.core.utils.prims import find_matching_prim_paths
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import Usd
from pxr import UsdShade
import torch as torch
__all__ = ['ParticleSystem', 'PhysxSchema', 'Usd', 'UsdShade', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'is_prim_path_valid', 'np', 'omni', 'torch']
class ParticleSystem:
    """
    Provides high level functions to deal with particle systems (1 or more particle systems) as well as its attributes/ properties.
        This object wraps all matching particle systems found at the regex provided at the prim_paths_expr.
        Note: not all the attributes of the PhysxSchema.PhysxParticleSystem is currently controlled with this view class
        Tensor API support will be added in the future to extend the functionality of this class to applications beyond cloth.
        
    """
    def __init__(self, prim_paths_expr: str, name: str = 'particle_system_view', particle_systems_enabled: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, simulation_owners: typing.Optional[typing.Sequence[str]] = None, contact_offsets: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, rest_offsets: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, particle_contact_offsets: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, solid_rest_offsets: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, fluid_rest_offsets: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, enable_ccds: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, solver_position_iteration_counts: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, max_depenetration_velocities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, winds: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, max_neighborhoods: typing.Optional[int] = None, max_velocities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, global_self_collisions_enabled: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None):
        """
        high level functions to deal with one or more particleSystems.
        
                Args:
                    prim_paths_expr(str): Prim paths regex to encapsulate all prims that match it.
                    name(str): Shortname to be used as a key by Scene class.
                    particle_systems_enabled (Optional[Union[np.ndarray, torch.Tensor]], optional): Whether to enable or disable the particle system.
                    simulation_owners (Optional[Sequence[str]], optional): Single PhysicsScene that simulates this particle system.
                    contact_offsets (Optional[Union[np.ndarray, torch.Tensor]], optional): Contact offset used for collisions with non-particle
                        objects such as rigid or deformable bodies.
                    rest_offsets (Optional[Union[np.ndarray, torch.Tensor]], optional): Rest offset used for collisions with non-particle objects
                        such as rigid or deformable bodies.
                    particle_contact_offsets (Optional[Union[np.ndarray, torch.Tensor]], optional): Contact offset used for interactions
                        between particles. Must be larger than solid and fluid rest offsets.
                    solid_rest_offsets (Optional[Union[np.ndarray, torch.Tensor]], optional): Rest offset used for solid-solid or solid-fluid
                        particle interactions. Must be smaller than particle contact offset.
                    fluid_rest_offsets (Optional[Union[np.ndarray, torch.Tensor]], optional): Rest offset used for fluid-fluid particle interactions.
                        Must be smaller than particle contact offset.
                    enable_ccds (Optional[Union[np.ndarray, torch.Tensor]], optional): Enable continuous collision detection for particles to help
                        avoid tunneling effects.
                    solver_position_iteration_counts (Optional[Union[np.ndarray, torch.Tensor]], optional): Number of solver iterations for position.
                    max_depenetration_velocities (Optional[Union[np.ndarray, torch.Tensor]], optional): The maximum velocity permitted to be introduced
                        by the solver to depenetrate intersecting particles.
                    winds (Optional[Union[np.ndarray, torch.Tensor]], optional):The wind applied to the current particle system.
                    max_neighborhoods (Optional[int], optional): The particle neighborhood size.
                    max_velocities (Optional[Union[np.ndarray, torch.Tensor]], optional): Maximum particle velocity.
                    global_self_collisions_enabled (Optional[Union[np.ndarray, torch.Tensor]], optional): If True, self collisions follow
                        particle-object-specific settings. If False, all particle self collisions are disabled, regardless
                        of any other settings. Improves performance if self collisions are not needed.
                
        """
    def _apply_material_binding_api(self, index):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def apply_particle_materials(self, particle_materials: typing.Union[ForwardRef('ParticleMaterial'), typing.List[ForwardRef('ParticleMaterial')]], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Used to apply particle material to prims in the view.
        
                Args:
                    particle_materials (Union[ParticleMaterial, List[ParticleMaterial]]): particle materials to be applied to prims in the view.
                                                                                        Note: if a physics material is not defined,
                                                                                        the defaults will be used from PhysX.
                                                                                        If a list is provided then its size has to be equal
                                                                                        the view's size or indices size.
                                                                                        If one material is provided it will be applied to all prims in the view.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                Raises:
                    Exception: length of physics materials != length of prims indexed
                
        """
    def get_applied_particle_materials(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.List[ForwardRef('ParticleMaterial')]:
        """
        Gets the applied particle material to prims in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to query. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
        
                Returns:
                    List[ParticleMaterial]: the current applied particle materials for prims in the view.
                
        """
    def get_contact_offsets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The contact offset  used for collisions with non-particle objects for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_enable_ccds(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]:  Whether continuous collision detection for particles is enabled or disabled for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_fluid_rest_offsets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The rest offset used for fluid-fluid particle interactions. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                
        """
    def get_global_self_collisions_enabled(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]:  Whether self collisions to follow particle-object-specific settings
                                                        is enabled or disabled. for each particle system. shape is (M, ).
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_max_depenetration_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The maximum velocity permitted to be introduced by the solver to
                                                        depenetrate intersecting particles for particle systems for each particle system. shape is (M, ).
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_max_neighborhoods(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]:  The particle neighborhood size for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_max_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The maximum particle velocities for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_particle_contact_offsets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The contact offset used for interactions between particles in the view concatenated. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                
        """
    def get_particle_systems_enabled(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]:  Whether particle system is enabled or not for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_rest_offsets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The rest offset used for collisions with non-particle objects for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_simulation_owners(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Sequence[str]:
        """
        
                Returns:
                    Sequence[str]: The physics scene prim path attached to particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_solid_rest_offsets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The rest offset used for solid-solid or solid-fluid particle interactions. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                
        """
    def get_solver_position_iteration_counts(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The number of solver iterations for positions for each particle system. shape is (M, ).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                
        """
    def get_winds(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The winds applied to the current particle system. shape is (M, 3).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a Particle System View.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
                
        """
    def is_valid(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> bool:
        """
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                Returns:
                    bool: True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.
                
        """
    def post_reset(self) -> None:
        """
        Resets the particles to their initial states.
        """
    def set_contact_offsets(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the contact offset used for collisions with non-particle objects such as rigid or deformable bodies for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_enable_ccds(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Enable continuous collision detection for particles for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_fluid_rest_offsets(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the rest offset used for fluid-fluid particle interactions.
        
                Note: Must be smaller than particle contact offset.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]): fluid rest offset to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_global_self_collisions_enabled(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Enable self collisions to follow particle-object-specific settings for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_max_depenetration_velocities(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        
                Set the maximum velocity permitted to be introduced by the solver to depenetrate intersecting particles for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_max_neighborhoods(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the particle neighborhood size for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_max_velocities(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the maximum particle velocity for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_contact_offsets(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the contact offset used for interactions between particles.
        
                Note: Must be larger than solid and fluid rest offsets.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]): The contact offset.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_systems_enabled(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set enabling of the particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_rest_offsets(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the rest offset used for collisions with non-particle objects such as rigid or deformable bodies for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_owners(self, values: typing.Sequence[str], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the PhysicsScene that simulates particle systems.
        
                Args:
                    values (Sequence[str]): PhysicsScene list to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_solid_rest_offsets(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the rest offset used for solid-solid or solid-fluid particle interactions.
        
                Note: Must be smaller than particle contact offset.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]): solid rest offset to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_solver_position_iteration_counts(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the number of solver iterations for position for particle systems.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]):  maximum particle velocity tensor to set particle systems to. shape is (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    def set_winds(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Set the winds velocities applied to the current particle system.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]]): The wind applied to the current particle system. shape is (M, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to manipulate. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
                
        """
    @property
    def count(self) -> int:
        """
        
                Returns:
                    int: number of rigid shapes for the prims in the view.
                
        """
    @property
    def name(self) -> str:
        """
        
                Returns:
                    str: name given to the view when instantiating it.
                
        """
