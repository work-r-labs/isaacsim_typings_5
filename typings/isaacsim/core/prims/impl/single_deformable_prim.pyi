from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl._impl.single_prim_wrapper
from isaacsim.core.prims.impl._impl.single_prim_wrapper import _SinglePrimWrapper
from isaacsim.core.prims.impl.deformable_prim import DeformablePrim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.utils.stage import get_current_stage
import isaacsim.core.utils.types
from isaacsim.core.utils.types import DynamicState
import numpy as np
from omni.physx.scripts import deformableUtils
from omni.physx.scripts import physicsUtils
from pxr import Gf
from pxr import PhysxSchema
from pxr import Sdf
from pxr import UsdGeom
import pxr.UsdGeom
from pxr import UsdPhysics
from pxr import UsdShade
import torch as torch
__all__ = ['DeformablePrim', 'DynamicState', 'Gf', 'PhysxSchema', 'Sdf', 'SingleDeformablePrim', 'SingleXFormPrim', 'UsdGeom', 'UsdPhysics', 'UsdShade', 'carb', 'deformableUtils', 'get_current_stage', 'np', 'physicsUtils', 'torch']
class SingleDeformablePrim(isaacsim.core.prims.impl._impl.single_prim_wrapper._SinglePrimWrapper):
    """
    Deformable primitive object provide functionalities to create and control deformable objects
    """
    def __init__(self, prim_path: str, deformable_material: typing.Optional[ForwardRef('DeformableMaterial')] = None, name: typing.Optional[str] = 'deformable', position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None, vertex_velocity_damping: typing.Optional[float] = None, sleep_damping: typing.Optional[float] = None, sleep_threshold: typing.Optional[float] = None, settling_threshold: typing.Optional[float] = None, self_collision: typing.Optional[bool] = True, self_collision_filter_distance: typing.Optional[float] = None, solver_position_iteration_count: typing.Optional[int] = None, kinematic_enabled: typing.Optional[bool] = False, simulation_rest_points: typing.Optional[typing.Sequence[float]] = None, simulation_indices: typing.Optional[typing.Sequence[int]] = None, simulation_hexahedral_resolution: typing.Optional[int] = 10, collision_rest_points: typing.Optional[typing.Sequence[float]] = None, collision_indices: typing.Optional[typing.Sequence[int]] = None, collision_simplification: typing.Optional[bool] = True, collision_simplification_remeshing: typing.Optional[bool] = True, collision_simplification_remeshing_resolution: typing.Optional[int] = 0, collision_simplification_target_triangle_count: typing.Optional[int] = 0, collision_simplification_force_conforming: typing.Optional[bool] = False, embedding: typing.Optional[typing.Sequence[int]] = None) -> None:
        """
        Creates a deformable body at prim_path given the deformable parameters.
                Note that although this class provide methods for retrieving the rest points and element indices of the underlying mesh, using the constructor of the class is the only way to set the rest points and element indices of the underlying mesh. This is to ensure the compatibility of the relevant input parameters and to avoid corrupting the mesh.
                Note also that this class does not provide methods to change USD attributes related to meshing, because once those are used for constructing the mesh, changing the parameters at runtime does not have any effect. Using the constructor of the class is the only way to set desired values for such parameters.
                TODO: indicated the range and dimensions of the input parameters
                Args:
                    prim_path (str): The absolute path that the prim is supposed to be registered in.
                    name (str, optional): Name given to the prim, this can be different than the prim path. Defaults to None.
                    position (Sequence[float], optional): The position of the center of the deformable.
                    orientation (Sequence[float], optional): The initial orientation of the deformable, assuming deformable is flat.
                    scale (Sequence[float], optional): The scale of the deformable.
                    visible (bool, optional): True if the deformable is supposed to be visible, False otherwise.
                    vertex_velocity_damping (float, optional): Velocity damping parameter controlling how much after every time step the nodal velocity is reduced
                    sleep_damping (float, optional): Damping value that damps the motion of bodies that move slow enough to be candidates for sleeping (see sleep_threshold)
                    sleep_threshold (float, optional): Threshold that defines the maximal magnitude of the linear motion a soft body can move in one second such that it can go to sleep in the next frame
                    settling_threshold (float, optional): Threshold that defines the maximal magnitude of the linear motion a fem body can move in one second before it becomes a candidate for sleeping
                    self_collision (bool, optional): Enables the self collision for the deformable body based on the rest position distances.
                    self_collision_filter_distance (float, optional): Penetration value that needs to get exceeded before contacts for self collision are generated. Will only have an effect if self collisions are enabled based on the rest position distances.
                    solver_position_iteration_count (int, optional): Number of the solver's positional iteration counts
                    kinematic_enabled (bool, optional): Enables kinematic body.
                    simulation_rest_points (Sequence[float], optional): List of vertices of the simulation tetrahedral mesh at rest. If a simulation mesh is provided, the collision mesh needs to be provided too. If no simulation mesh is provided it will be computed implicitly based on simulation_hexahedral_resolution
                    simulation_indices (Sequence[int], optional): List of indices of the simulation tetrahedral mesh. It is mandatory to provide this list if simulation_rest_points is specified as well.
                    simulation_hexahedral_resolution (int, optional): The parameter controlling the resolution of the soft body simulation mesh
                    collision_rest_points (Sequence[float], optional): List of vertices of the collision tetrahedral mesh at rest. If a simulation mesh is provided, the collision mesh needs to be provided too.
                    collision_indices (Sequence[int], optional): List of indices of the simulation tetrahedral mesh. It is mandatory to provide this list if collision_rest_points is specified as well.
                    collision_simplification (bool, optional): Flag indicating if simplification should be applied to the mesh before creating a soft body out of it. This is ignored if simulation mesh has been provided.
                    collision_simplification_remeshing (bool, optional): Flag indicating if the simplification should be based on remeshing. This is ignored if collision_simplification is False.
                    collision_simplification_remeshing_resolution (int, optional): The resolution used for remeshing. A value of 0 indicates that a heuristic is used to determine the resolution. Ignored if collision_simplification_remeshing is False.
                    collision_simplification_target_triangle_count (int, optional): The target triangle count used for the simplification. A value of 0 indicates that a heuristic based on the simulation_hexahedral_resolution is to determine the target count. This is ignored if collision_simplification equals False.
                    collision_simplification_force_conforming (bool, optional): Flag indicating that the tretrahedralizer used to generate the collision mesh should produce tetrahedra that conform to the triangle mesh. If False the implementation chooses the tretrahedralizer used.
                    embedding (Sequence[int], optional):embedding information mapping collision points to the containing simulation tetrahedra.
                
        """
    def _get_points_pose(self):
        """
        Return the position of the points of the deformable prim with respect to the center of the deformable prim
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: position of the points that the deformable is composed of.
                
        """
    def apply_deformable_material(self, deformable_materials: DeformableMaterial) -> None:
        ...
    def get_applied_deformable_material(self) -> DeformableMaterial:
        ...
    def get_collision_mesh_indices(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Gets the collision mesh element indices
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: collision mesh element indices
                
        """
    def get_current_dynamic_state(self) -> isaacsim.core.utils.types.DynamicState:
        """
        Return the DynamicState that contains the position and orientation of the underlying xform prim
        
                Returns:
                    DynamicState:
                        position (np.ndarray, optional):
                                    position in the world frame of the prim. shape is (3, ).
                                    Defaults to None, which means left unchanged.
                        orientation (np.ndarray, optional):
                                    quaternion orientation in the world frame of the prim.
                                    quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                    Defaults to None, which means left unchanged.
                
        """
    def get_self_collision(self) -> bool:
        """
        
                Gets the deformable body self collision
        
                Returns:
                    float: self collision
                
        """
    def get_self_collision_filter_distance(self) -> float:
        """
        
                Gets the deformable body self collision filter distance
        
                Returns:
                    float: self collision filter distance
                
        """
    def get_settling_threshold(self) -> float:
        """
        
                Gets the deformable body settling threshold
        
                Returns:
                    float: settling threshold
                
        """
    def get_simulation_mesh_indices(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Gets the simulation mesh element indices
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: simulation mesh element indices
                
        """
    def get_simulation_mesh_rest_points(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Gets the simulation mesh rest positions
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: simulation mesh vertices rest positions
                
        """
    def get_sleep_damping(self) -> float:
        """
        
                Gets the deformable body sleep damping parameter
        
                Returns:
                    float: sleep damping
                
        """
    def get_sleep_threshold(self) -> float:
        """
        
                Gets the deformable body sleep threshold
        
                Returns:
                    float: sleep threshold
                
        """
    def get_solver_position_iteration_count(self) -> int:
        """
        
                Gets the solver's positional iteration count
        
                Returns:
                    int: positional iteration count
                
        """
    def get_vertex_velocity_damping(self) -> float:
        """
        
                Gets the deformable body vertex velocity damping parameter
        
                Returns:
                    float: vertex velocity damping
                
        """
    def set_self_collision(self, self_collision: bool) -> None:
        """
        
                Args:
                    self_collision(bool): deformable body self collision parameter.
                
        """
    def set_self_collision_filter_distance(self, self_collision_filter_distance: float) -> None:
        """
        
                Args:
                    self_collision_filter_distance(float): deformable body self collision filter distance parameter.
                
        """
    def set_settling_threshold(self, settling_threshold: float) -> None:
        """
        
                Args:
                    settling_threshold(float): deformable body settling threshold parameter.
                
        """
    def set_sleep_damping(self, sleep_damping: float) -> None:
        """
        
                Args:
                    sleep_damping(float): deformable body sleep damping parameter.
                
        """
    def set_sleep_threshold(self, sleep_threshold: float) -> None:
        """
        
                Args:
                    sleep_threshold(float): deformable body sleep threshold parameter.
                
        """
    def set_solver_position_iteration_count(self, iterations: int) -> None:
        """
        
                Args:
                    iterations(float): solver position iteration count
                
        """
    def set_vertex_velocity_damping(self, vertex_velocity_damping: float) -> None:
        """
        
                Args:
                    vertex_velocity_damping(float): deformable body vertex velocity damping parameter.
                
        """
    @property
    def mesh(self) -> pxr.UsdGeom.Mesh:
        """
        
                Returns:
                    Usd.Prim: USD Prim object that this object tracks.
                
        """
