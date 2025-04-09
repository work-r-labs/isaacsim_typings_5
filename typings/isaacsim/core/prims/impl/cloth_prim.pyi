from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl.xform_prim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import UsdPhysics
from pxr import Vt
import torch as torch
__all__ = ['ClothPrim', 'PhysxSchema', 'UsdPhysics', 'Vt', 'XFormPrim', 'carb', 'np', 'omni', 'torch']
class ClothPrim(isaacsim.core.prims.impl.xform_prim.XFormPrim):
    """
    The view class for cloth prims.
    """
    def __init__(self, prim_paths_expr: str, particle_systems: typing.Union[numpy.ndarray, torch.Tensor] = None, particle_materials: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, name: str = 'cloth_prim_view', reset_xform_properties: bool = True, positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, particle_masses: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, pressures: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, particle_groups: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, self_collisions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, self_collision_filters: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, stretch_stiffnesses: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, bend_stiffnesses: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, shear_stiffnesses: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, spring_dampings: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None):
        """
        
                Provides high level functions to deal with cloths (1 or more cloths)
                as well as its attributes/ properties. This object wraps all matching cloths found at the regex provided at the prim_paths_expr.
                This object wraps all matching Cloth Prims found at the regex provided at the prim_paths_expr.
        
                Note: - if the prim does not already have a rigid body api applied to it before init, it will apply it.
                Args:
                    prim_paths_expr(str): Prim paths regex to encapsulate all prims that match it.
                    name(str): Shortname to be used as a key by Scene class.
                    positions: (Union[np.ndarray, torch.Tensor], optional): Default positions in the world frame of the prim. shape is (N, 3).
                    translations: (Union[np.ndarray, torch.Tensor], optional): Default translations in the local frame of the
                                                                                prims (with respect to its parent prims). shape is (N, 3).
                    orientations: (Union[np.ndarray, torch.Tensor], optional): Default quaternion orientations in the world/
                                                                                local frame of the prim (depends if translation or position is specified).
                                                                                quaternion is scalar-first (w, x, y, z). shape is (N, 4).
                    scales: (Union[np.ndarray, torch.Tensor], optional): Local scales to be applied to the prim's dimensions. shape is (N, 3).
                    visibilities: (Union[np.ndarray, torch.Tensor], optional): Set to false for an invisible prim in the stage while rendering. shape is (N,).
                    particle_masses (Union[np.ndarray, torch.Tensor], optional): particle masses to be applied to each prim.
                    pressures (Union[np.ndarray, torch.Tensor], optional): pressures to be applied to each prim. if > 0, a particle
                                                                        cloth has an additional pressure constraint that provides
                                                                        inflatable (i.e. balloon-like) dynamics. The pressure
                                                                        times the rest volume defines the volume the inflatable
                                                                        tries to match. Pressure only works well for closed or
                                                                        approximately closed meshes, range: [0, inf), units: dimensionless
                    particle_groups (Union[np.ndarray, torch.Tensor], optional): group Id of the particles of each prim, range: [0, 2^20)
                    self_collisions (Union[np.ndarray, torch.Tensor], optional): enable self collision of the particles of each prim.
                    self_collision_filters (Union[np.ndarray, torch.Tensor], optional): whether the simulation should filter
                                                                                        particle-particle collisions based on the
                                                                                        rest position distances of each prim. shape is (N,).
                    stretch_stiffnesses (Union[np.ndarray, torch.Tensor], optional): represents the stretch spring stiffnesses for
                                                                                    linear springs placed between particles to counteract
                                                                                    stretching, shape is (N,). range: [0, inf), units:
                                                                                    force / distance = mass / second / second
                    bend_stiffnesses (Union[np.ndarray, torch.Tensor], optional): represents the spring bend stiffnesses for linear
                                                                                 springs placed in a way to counteract bending,  shape is (N,).
                                                                                 range: [0, inf), units: force / distance = mass / second / second
                    shear_stiffnesses (Union[np.ndarray, torch.Tensor], optional): represents the shear stiffnesses for linear
                                                                                    springs placed in a way to counteract shear,  shape is (N,).
                                                                                    range: [0, inf), units: force / distance = mass / second / second
                    spring_dampings (Union[np.ndarray, torch.Tensor], optional): damping on cloth spring constraints. Applies to all constraints
                                                                                parameterized by stiffness attributes, range: [0, inf),  shape is (N,).
                                                                                units: force * second / distance = mass / second
                
        """
    def _apply_cloth_api(self, index):
        ...
    def _apply_cloth_auto_api(self, index):
        ...
    def _apply_particle_api(self, index):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def get_cloths_bend_stiffnesses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the value of bend stiffness set to all the springs within cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: bend stiffness tensor with shape (M, )
                
        """
    def get_cloths_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the value of damping set for all the springs within cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: damping tensor with shape (M, )
                
        """
    def get_cloths_shear_stiffnesses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the value of shear stiffness set to all the springs within cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: shear stiffness tensor with shape (M, )
                
        """
    def get_cloths_stretch_stiffnesses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the value of stretch stiffness set to all the springs within cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: stretch stiffness tensor with shape (M, )
                
        """
    def get_particle_groups(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the particle groups of the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: particle groups with shape (M, ).
                
        """
    def get_particle_masses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the particle masses for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: mass tensor with shape (M, max_particles_per_cloth)
                
        """
    def get_pressures(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the pressures of the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: cloths pressure with shape (M, ).
                
        """
    def get_self_collision_filters(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the self collision filters for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the self collision filters tensor with shape (M, )
                
        """
    def get_self_collisions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the self collision for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the self collision tensor with shape (M, )
                
        """
    def get_spring_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the spring damping for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: damping tensor with shape (M, max_springs_per_cloth)
                
        """
    def get_stretch_stiffnesses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the spring stretch stiffness for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: stiffness tensor with shape (M, max_springs_per_cloth)
                
        """
    def get_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the particle velocities for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: velocity tensor with shape (M, max_particles_per_cloth, 3)
                
        """
    def get_world_positions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the particle world positions for the cloths indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: position tensor with shape (M, max_particles_per_cloth, 3)
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a rigid body view in physX.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
                
        """
    def set_cloths_bend_stiffnesses(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets a single value of bend stiffnesses to all the springs within cloths indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): cloth spring bend stiffness values with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_cloths_dampings(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets a single value of damping to all the springs within cloths indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): cloth spring damping with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_cloths_shear_stiffnesses(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets a single value of shear stiffnesses to all the springs within cloths indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): cloth spring shear stiffness values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_cloths_stretch_stiffnesses(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets a single value of stretch stiffnesses to all the springs within cloths indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): cloth spring stretch stiffness values with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_groups(self, particle_groups: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle group of the cloths indicated by the indices.
        
                Args:
                    particle_groups (Union[np.ndarray, torch.Tensor]): particle group with shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_masses(self, masses: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle masses for the cloths indicated by the indices.
        
                Args:
                    masses (Union[np.ndarray, torch.Tensor]): cloth particle masses with the shape
                                                                                        (M, max_particles_per_cloth, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_pressures(self, pressures: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the pressures of the cloths indicated by the indices.
        
                Args:
                    pressures (Union[np.ndarray, torch.Tensor]): cloths pressure with shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_self_collision_filters(self, self_collision_filters: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the self collision filters for the cloths indicated by the indices.
        
                Args:
                    self_collision_filters (Union[np.ndarray, torch.Tensor]): self collision filters with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_self_collisions(self, self_collisions: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the self collision flags for the cloths indicated by the indices.
        
                Args:
                    self_collisions (Union[np.ndarray, torch.Tensor]): self collision flag with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_spring_dampings(self, damping: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the spring damping for the cloths indicated by the indices.
        
                Args:
                    damping (Union[np.ndarray, torch.Tensor]): cloth spring damping with the shape
                                                                                    (M, max_springs_per_cloth).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_stretch_stiffnesses(self, stiffness: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the spring stretch stiffness values for springs within the cloths indicated by the indices.
        
                Args:
                    stiffness (Union[np.ndarray, torch.Tensor]): cloth spring stiffness with the shape  (M, max_springs_per_cloth).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle velocities for the cloths indicated by the indices.
        
                Args:
                    velocities (Union[np.ndarray, torch.Tensor]): particle velocities with the shape
                                                                                        (M, max_particles_per_cloth, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_world_positions(self, positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle world positions for the cloths indicated by the indices.
        
                Args:
                    positions (Union[np.ndarray, torch.Tensor]): particle positions with the shape
                                                                                        (M, max_particles_per_cloth, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which cloth prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    @property
    def count(self) -> int:
        """
        
                Returns:
                    int: cloth counts.
                
        """
    @property
    def max_particles_per_cloth(self) -> int:
        """
        
                Returns:
                    int: maximum number of particles per cloth.
                
        """
    @property
    def max_springs_per_cloth(self) -> int:
        """
        
                Returns:
                    int: maximum number of springs per cloth.
                
        """
