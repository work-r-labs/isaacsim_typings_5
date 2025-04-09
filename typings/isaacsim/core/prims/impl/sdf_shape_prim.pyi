from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl.geometry_prim
from isaacsim.core.prims.impl.geometry_prim import GeometryPrim
from isaacsim.core.utils.prims import find_matching_prim_paths
from isaacsim.core.utils.prims import get_prim_at_path
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import torch as torch
import warp as wp
__all__ = ['GeometryPrim', 'PhysxSchema', 'SdfShapePrim', 'Usd', 'UsdGeom', 'UsdPhysics', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'np', 'omni', 'torch', 'wp']
class SdfShapePrim(isaacsim.core.prims.impl.geometry_prim.GeometryPrim):
    """
    High level functions to deal with geometry prims that provide their Signed Distance Field (SDF).
    
        This object wraps all matching mesh geometry prims found at the regex provided at the prim_paths_expr.
    
        Args:
    
            prim_paths_expr (str): prim paths regex to encapsulate all prims that match it.
                                    example: "/World/Env[1-5]/Microwave" will match /World/Env1/Microwave,
                                    /World/Env2/Microwave..etc.
                                    (a non regex prim path can also be used to encapsulate one XForm).
            num_query_points (int): number of points queried by this view object
            prepare_sdf_schemas (bool, optional): apply PhysxSDFMeshCollisionAPI to prims in prim_paths_expr. Defaults to True.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "sdf_shape_view".
            positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                            default positions in the world frame of the prim.
                                                            shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                            default translations in the local frame of the prims
                                                            (with respect to its parent prims). shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                            default quaternion orientations in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (N, 4).
                                                            Defaults to None, which means left unchanged.
            scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): local scales to be applied to
                                                            the prim's dimensions. shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array], optional): set to false for an invisible prim in
                                                                                the stage while rendering. shape is (N,).
                                                                                Defaults to None.
            reset_xform_properties (bool, optional): True if the prims don't have the right set of xform properties
                                                    (i.e: translate, orient and scale) ONLY and in that order.
                                                    Set this parameter to False if the object were cloned using using
                                                    the cloner api in isaacsim.core.cloner. Defaults to True.
            collisions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): Set to True if the geometry already have/
                                                        should have a collider (i.e not only a visual geometry). shape is (N,).
                                                        Defaults to None.
            track_contact_forces (bool, Optional) : if enabled, the view will track the net contact forces on each geometry prim
                                                    in the view. Note that the collision flag should be set to True to report
                                                    contact forces. Defaults to False.
            prepare_contact_sensors (bool, Optional): applies contact reporter API to the prim if it already does not have one.
                                                        Defaults to False.
            disable_stablization (bool, optional): disables the contact stabilization parameter in the physics context.
                                                    Defaults to True.
            contact_filter_prim_paths_expr (Optional[List[str]], Optional): a list of filter expressions which allows for tracking
                                                                            contact forces between the geometry prim and this subset
                                                                            through get_contact_force_matrix().
    
        
    """
    def __init__(self, prim_paths_expr: str, num_query_points: int, prepare_sdf_schemas: bool = True, name: str = 'sdf_shape_view', positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, reset_xform_properties: bool = True, collisions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, track_contact_forces: bool = False, prepare_contact_sensors: bool = False, disable_stablization: bool = True, contact_filter_prim_paths_expr: typing.Optional[typing.List[str]] = list()) -> None:
        ...
    def _apply_sdf_schema(self, prim_at_path):
        """
        apply appropriate sdf schemas to prims.
        """
    def _invalidate_physics_handle_callback(self, event):
        ...
    def get_sdf_and_gradients(self, points: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Get the SDF values and gradients of the query points
        
                Args:
                    points ([Union[np.ndarray, torch.Tensor]]): points (represented in the local frames of meshes) to be queried for sdf and gradients.
                                                                                  shape is (self.num_shapes, self.num_query_points, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: SDF values and gradients of points for prims with shape (self.num_shapes, self.num_query_points, 4).
                    The first component is the SDF value while the last three represent the gradient
                
        """
    def get_sdf_margins(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets sdf margin values.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: margins of the sdf collision apis for prims in the view. shape is (M,).
                
        """
    def get_sdf_narrow_band_thickness(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets sdf collision narrow band thickness values.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: narrow band thickness of the sdf collision apis for prims in the view. shape is (M,).
                
        """
    def get_sdf_resolution(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets sdf collision resolution values.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: resolutions of the sdf collision apis for prims in the view. shape is (M,).
                
        """
    def get_sdf_subgrid_resolution(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets sdf collision subgrid resolution values.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: subgrid resolutions of the sdf collision apis for prims in the view. shape is (M,).
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a sdf shape view in physX.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
                
        """
    def set_sdf_margins(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Sets signed distance field margins for prims in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): sdf margins to be set. shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_sdf_narrow_band_thickness(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Sets signed distance field narrow band thicknesses for prims in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): sdf margins to be set. shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_sdf_resolution(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Sets signed distance field subgrid resolutions for prims in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): sdf margins to be set. shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_sdf_subgrid_resolution(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None) -> None:
        """
        Sets signed distance field subgrid resolutions for prims in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor]): sdf margins to be set. shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    @property
    def num_query_points(self) -> int:
        """
        
                Returns:
                    int: number of points queried by this view object.
                
        """
