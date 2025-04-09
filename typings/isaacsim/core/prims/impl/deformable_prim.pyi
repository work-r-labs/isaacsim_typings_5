from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl.xform_prim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import UsdShade
import torch as torch
__all__ = ['DeformablePrim', 'PhysxSchema', 'UsdShade', 'XFormPrim', 'carb', 'np', 'omni', 'torch']
class DeformablePrim(isaacsim.core.prims.impl.xform_prim.XFormPrim):
    """
    The view class for deformable prims.
    """
    def __init__(self, prim_paths_expr: str, deformable_materials: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, name: str = 'deformable_prim_view', reset_xform_properties: bool = True, positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, vertex_velocity_dampings: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, sleep_dampings: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, sleep_thresholds: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, settling_thresholds: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, self_collisions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, self_collision_filter_distances: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, solver_position_iteration_counts: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None):
        """
        
                Provides high level functions to deal with deformable bodies (1 or more deformable bodies)
                as well as its attributes/ properties. This object wraps all matching deformable bodies found at the regex provided at the prim_paths_expr.
        
                Note: - if the underlying UsdGeom.Mesh.Get does not already have appropriate USD deformable body apis applied to it before init, this class will apply it.
                Args:
                    prim_paths_expr (str): Prim paths regex to encapsulate all prims that match it.
                    name (str): Shortname to be used as a key by Scene class.
                    positions (Union[np.ndarray, torch.Tensor], optional): Default positions in the world frame of the prim. shape is (N, 3).
                    translations (Union[np.ndarray, torch.Tensor], optional): Default translations in the local frame of the
                                                                                prims (with respect to its parent prims). shape is (N, 3).
                    orientations (Union[np.ndarray, torch.Tensor], optional): Default quaternion orientations in the world/
                                                                                local frame of the prim (depends if translation or position is specified).
                                                                                quaternion is scalar-first (w, x, y, z). shape is (N, 4).
                    scales (Union[np.ndarray, torch.Tensor], optional): Local scales to be applied to the prim's dimensions. shape is (N, 3).
                    visibilities (Union[np.ndarray, torch.Tensor], optional): Set to false for an invisible prim in the stage while rendering. shape is (N,).
                    vertex_velocity_dampings (Union[np.ndarray, torch.Tensor], optional): Velocity damping parameter controlling how much after every time step the nodal velocity is reduced
                    sleep_dampings (Union[np.ndarray, torch.Tensor], optional): Damping value that damps the motion of bodies that move slow enough to be candidates for sleeping (see sleep_threshold)
                    sleep_thresholds (Union[np.ndarray, torch.Tensor], optional): Threshold that defines the maximal magnitude of the linear motion a soft body can move in one second such that it can go to sleep in the next frame
                    settling_thresholds (Union[np.ndarray, torch.Tensor], optional): Threshold that defines the maximal magnitude of the linear motion a fem body can move in one second before it becomes a candidate for sleeping
                    self_collisions (Union[np.ndarray, torch.Tensor], optional): Enables the self collision for the deformable body based on the rest position distances.
                    self_collision_filter_distances (Union[np.ndarray, torch.Tensor], optional): Penetration value that needs to get exceeded before contacts for self collision are generated. Will only have an effect if self collisions are enabled based on the rest position distances.
                    solver_position_iteration_counts (Union[np.ndarray, torch.Tensor], optional): Number of the solver's positional iteration counts
                
        """
    def _apply_deformable_api(self, index):
        ...
    def _apply_deformable_body_api(self, index):
        ...
    def _apply_material_binding_api(self, index):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def apply_deformable_materials(self, deformable_materials: typing.Union[ForwardRef('DeformableMaterial'), typing.List[ForwardRef('DeformableMaterial')]], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Used to apply deformable material to prims in the view.
        
                Args:
                    deformable_materials (Union[DeformableMaterial, List[DeformableMaterial]]): deformable materials to be applied to prims in the view.
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
    def get_applied_deformable_materials(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> typing.List[ForwardRef('DeformableMaterial')]:
        """
        Gets the applied deformable material to prims in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                        to query. Shape (M,).
                                                                                        Where M <= size of the encapsulated prims in the view.
                                                                                        Defaults to None (i.e: all prims in the view).
        
                Returns:
                    List[DeformableMaterial]: the current applied deformable materials for prims in the view.
                
        """
    def get_collision_mesh_element_deformation_gradients(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the collision mesh element-wise second-order deformation gradient tensors for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: collision mesh deformation gradients with shape (M, max_collision_mesh_elements_per_body, 3, 3)
                
        """
    def get_collision_mesh_element_rest_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the collision mesh rest poses for the deformable bodies indicated by the indices.
                This method will return the 3x3 matrix inv([x1-x0, x2-x0, x3-x0]) where x0, x1, x2, x3 are the rest points of collision mesh elements
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: collision mesh rest poses with shape (M, max_collision_mesh_elements_per_body, 3, 3)
                
        """
    def get_collision_mesh_element_rotations(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the collision mesh element-wise rotations as quaternions for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: collision mesh rotations with shape (M, max_collision_mesh_elements_per_body, 4)
                
        """
    def get_collision_mesh_element_stresses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the collision mesh element-wise second-order stress tensors for bodies indicated by the indices.
                This method will return the collision mesh element-wise stresses of the deformable bodies
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: collision mesh stresses with shape (M, max_collision_mesh_elements_per_body, 3, 3)
                
        """
    def get_collision_mesh_indices(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the collision mesh element indices of the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: deformable bodies collision mesh element indices
                                                                                with shape (M,  self.max_collision_mesh_elements_per_body, 4).
                
        """
    def get_collision_mesh_nodal_positions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the nodal positions of the collision mesh for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: position tensor with shape (M, max_collision_mesh_vertices_per_body, 3)
                
        """
    def get_self_collision_filter_distances(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the self collision filter distance for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the self collision filter distance tensor with shape (M, )
                
        """
    def get_self_collisions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the self collision parameters for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the self collision tensor with shape (M, )
                
        """
    def get_settling_thresholds(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the settling threshold for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the settling threshold tensor with shape (M, )
                
        """
    def get_simulation_mesh_element_deformation_gradients(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh element-wise second-order deformation gradient tensors for the deformable bodies indicated by the indices.
                This method will return the simulation mesh element-wise deformation gradient of the deformable bodies
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: simulation mesh element-wise deformation gradients with shape (M, max_simulation_mesh_elements_per_body, 3, 3)
                
        """
    def get_simulation_mesh_element_rest_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh rest poses for the deformable bodies indicated by the indices.
                This method will return the 3x3 matrix inv([x1-x0, x2-x0, x3-x0]) where x0, x1, x2, x3 are the rest points of the simulation mesh elements
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: simulation mesh rest poses with
                                                                                            shape (M, max_simulation_mesh_elements_per_body, 3, 3)
                
        """
    def get_simulation_mesh_element_rotations(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh element-wise rotations as quaternions for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]:  simulation mesh element-wise rotations with shape (M, max_simulation_mesh_elements_per_body, 4)
                
        """
    def get_simulation_mesh_element_stresses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh element-wise second-order stress tensors for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]:
                    simulation mesh element-wise stresses with shape (M, max_simulation_mesh_elements_per_body, 3, 3)
                
        """
    def get_simulation_mesh_indices(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh element indices of the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: deformable bodies simulation mesh element indices
                                                                                 with shape (M, self.max_simulation_mesh_elements_per_body, 4).
                
        """
    def get_simulation_mesh_kinematic_targets(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the nodal kinematic targets of the simulation mesh for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: kinematic targets tensor,
                                                                                            with shape (M, max_simulation_mesh_vertices_per_body, 4)
                                                                                            the first three components are the position targets and the last value (0 or 1)
                                                                                            indicate whether the node is kinematically driven or not.
                
        """
    def get_simulation_mesh_nodal_positions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the nodal positions of the simulation mesh for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: position tensor with shape (M, max_simulation_mesh_vertices_per_body, 3)
                
        """
    def get_simulation_mesh_nodal_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the vertex velocities for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: velocity tensor with shape (M, max_simulation_mesh_vertices_per_body, 3)
                
        """
    def get_simulation_mesh_rest_points(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the simulation mesh rest points of the deformable bodies indicated by the indices.
                    rest point are the nodal positions with respect to the local prim transform, while the values returned by get_simulation_mesh_nodal_positions
                    are the nodal positions with respect to the origin
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: deformable bodies simulation mesh rest points
                                                                                            with shape (M, self.max_simulation_mesh_vertices_per_body, 3).
                
        """
    def get_sleep_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the sleep damping for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the sleep damping tensor with shape (M, )
                
        """
    def get_sleep_thresholds(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the sleep threshold for the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: the sleep threshold tensor with shape (M, )
                
        """
    def get_solver_position_iteration_counts(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the solver's positional iteration counts of the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (int, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: solver's positional iteration counts with shape (M, ).
                
        """
    def get_vertex_velocity_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the vertex velocity dampings of the deformable bodies indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (float, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]: deformable bodies vertex velocity dampings with shape (M, ).
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a deformable body view in physX.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
                
        """
    def set_collision_mesh_indices(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the collision mesh element indices of the deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): element indices with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_collision_mesh_rest_points(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the collision mesh vertices rest positions of the deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): vertices rest positions values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_self_collision_filter_distances(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the self collisions filter distance values for deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_self_collisions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the self collisions values for deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_settling_thresholds(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the settling threshold values for deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_mesh_indices(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the simulation mesh element indices of the deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): element indices with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_mesh_kinematic_targets(self, positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the kinematic targets of the simulation mesh for the deformable bodies indicated by the indices.
        
                Args:
                    positions (Union[np.ndarray, torch.Tensor]): kinematic targets with the shape (M, max_simulation_mesh_vertices_per_body, 4).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_mesh_nodal_positions(self, positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the nodal positions of the simulation mesh for the deformable bodies indicated by the indices.
        
                Args:
                    positions (Union[np.ndarray, torch.Tensor]): nodal positions with the shape (M, max_simulation_mesh_vertices_per_body, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_mesh_nodal_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the vertex velocities for the deformable bodies indicated by the indices.
        
                Args:
                    velocities (Union[np.ndarray, torch.Tensor]): vertex velocities with the shape
                                                                                        (M, max_simulation_mesh_vertices_per_body, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_simulation_mesh_rest_points(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the simulation mesh vertices rest positions of the deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): vertices rest positions values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_sleep_dampings(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the sleep dampings values for deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_sleep_thresholds(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the sleep threshold values for deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_solver_position_iteration_counts(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets values of the solver position iteration counts to deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_vertex_velocity_dampings(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets values of the vertex velocity damping values to deformable bodies indicated by the indices.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): solver position iteration counts values with the shape  (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which deformable prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    @property
    def count(self) -> int:
        """
        
                Returns:
                    int: deformable counts.
                
        """
    @property
    def max_collision_mesh_elements_per_body(self) -> int:
        """
        
                Returns:
                    int: maximum number of collision mesh elements per deformable body.
                
        """
    @property
    def max_collision_mesh_vertices_per_body(self) -> int:
        """
        
                Returns:
                    int: maximum number of collision mesh vertices per deformable body.
                
        """
    @property
    def max_simulation_mesh_elements_per_body(self) -> int:
        """
        
                Returns:
                    int: maximum number of simulation mesh elements per deformable body.
                
        """
    @property
    def max_simulation_mesh_vertices_per_body(self) -> int:
        """
        
                Returns:
                    int: maximum number of simulation mesh vertices per deformable body.
                
        """
