from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
from enum import Enum
from enum import Flag
from enum import IntEnum
from enum import auto
import math as math
import omni as omni
from omni.kit.manipulator.prim.core.settings_constants import DataAccessorConstants as da_c
from omni.ui import scene as sc
import pxr as pxr
import traceback as traceback
import typing
import usdrt as usdrt
__all__: list = ['FabricDataAccessor']
class FabricDataAccessor:
    """
    A class for accessing and manipulating USD (Universal Scene Description) data in a fabric.
    
        This class handles the retrieval and alteration of scene graph information, including transformation matrices, stage access, and USD prim manipulation. It is designed to work within a fabric-based USD runtime and provides a range of methods to interact with USD stages and prims.
    
        Args:
            usd_context_name (str): The name of the USD context to associate with this data accessor. An empty string indicates no specific context.
            model: The model associated with the data accessor. The exact type of the model is not specified.
    
        This class also handles update callbacks for changes in the USD stage and provides utility functions for converting between different path and transform representations.
        
    """
    Rt = usdrt.Rt
    Sdf = usdrt.Sdf
    Usd = usdrt.Usd
    UsdGeom = usdrt.UsdGeom
    Vt = usdrt.Vt
    def __init__(self, usd_context_name: str = '', model = None):
        """
        Constructor for FabricDataAccessor.
        
                Initializes a new instance of the FabricDataAccessor with optional USD context and model.
        """
    def _construct_transfrom_matrix_from_SQT(self, t: usdrt.Gf.Vec3d, q: usdrt.Gf.Quatd, scale: usdrt.Gf.Vec3d) -> usdrt.Gf.Matrix4d:
        ...
    def _euler_from_quaternion(self, q: usdrt.Gf.Quatd, axes: list[usdrt.Gf.Vec3d]) -> list[float]:
        ...
    def _get_local_transform_matrix(self, prim: usdrt.Usd.Prim, time: float = None) -> usdrt.Gf.Matrix4d:
        ...
    def _on_tick(self, event: carb.events.IEvent):
        ...
    def _to_usdrt_path(self, path: usdrt.Sdf.Path | pxr.Sdf.Path) -> usdrt.Sdf.Path:
        ...
    def clear_xform_cache(self):
        """
        Clears the transform cache.
        """
    def destroy(self):
        """
        Cleans up resources and references held by the FabricDataAccessor instance.
        """
    def do_transform_all_selected_prims_to_manipulator_pivot(self, paths: list[str], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float]):
        """
        Transforms all selected prims to manipulator pivot.
        
                Args:
                    paths (List[str]): List of path strings for selected prims.
                    paths_c (List[int]): List of path hashes for selected prims.
                    new_translations (List[float]): List of new translation values for prims.
                    new_rotation_eulers (List[float]): List of new rotation euler angles for prims.
                    new_rotation_orders (List[int]): List of new rotation orders for prims.
                    new_scales (List[float]): List of new scale values for prims.
        """
    def do_transform_selected_prims(self, paths: list[str], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float]):
        """
        Transforms selected prims with the given transformations.
        
                Args:
                    paths (List[str]): List of path strings for selected prims.
                    paths_c (List[int]): List of path hashes for selected prims.
                    new_translations (List[float]): List of new translation values for prims.
                    new_rotation_eulers (List[float]): List of new rotation euler angles for prims.
                    new_rotation_orders (List[int]): List of new rotation orders for prims.
                    new_scales (List[float]): List of new scale values for prims.
        """
    def free_stage(self):
        """
        Frees the USD stage.
        """
    def free_xform_cache(self):
        """
        Frees the transform cache.
        """
    def get_current_time_code(self, currentTime: float) -> usdrt.Usd.TimeCode:
        """
        Gets the current time code.
        
                Args:
                    currentTime (float): The current time to get the time code for.
        
                Returns:
                    usdrt.Usd.TimeCode: The current time code.
        """
    def get_data_tag(self) -> str:
        """
        Gets the data tag that identifies FabricDataAccessor.
        
                Returns:
                    str: The data tag for FabricDataAccessor.
        """
    def get_local_to_world_transform(self, prim: usdrt.Usd.Prim) -> usdrt.Gf.Matrix4d:
        """
        Gets the local-to-world transform matrix of the USD Prim.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The USD Prim to get the transform for.
        
                Returns:
                    usdrt.Gf.Matrix4d: The local-to-world transform matrix.
        """
    def get_local_transform_SRT(self, prim: usdrt.Usd.Prim, time: float = None) -> tuple[usdrt.Gf.Vec3d, usdrt.Gf.Vec3d, usdrt.Gf.Vec3i, usdrt.Gf.Vec3d]:
        """
        Gets the local transform SRT (scale, rotation, translation) of the USD Prim.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The USD Prim to get the transform for.
                    time (float): The time at which to evaluate the transform.
        
                Returns:
                    Tuple[usdrt.Gf.Vec3d, usdrt.Gf.Vec3d, usdrt.Gf.Vec3i, usdrt.Gf.Vec3d]: The SRT components of the transform.
                
        """
    def get_local_transform_pivot_inv(self, prim: usdrt.Usd.Prim, time: float = None) -> usdrt.Gf.Matrix4d:
        """
        Returns the inverse of the local transformation pivot for a given prim.
        
                Args:
                    prim (:obj:`Usd.Prim`): The prim to calculate the inverse transform for.
                    time (float, optional): The time at which to evaluate the transformation.
        
                Returns:
                    :obj:`Gf.Matrix4d`: The inverse of the local transformation matrix.
        """
    def get_parent_to_world_transform(self, prim: usdrt.Usd.Prim) -> usdrt.Gf.Matrix4d:
        """
        Gets the parent-to-world transform matrix of the USD Prim.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The USD Prim to get the transform for.
        
                Returns:
                    usdrt.Gf.Matrix4d: The parent-to-world transform matrix.
        """
    def get_prim_at_path(self, path: usdrt.Sdf.Path) -> usdrt.Usd.Prim:
        """
        Returns the USD Prim at the specified path.
        
                Args:
                    path (:obj:`usdrt.Sdf.Path`): The path to the USD Prim.
        
                Returns:
                    usdrt.Usd.Prim: The USD Prim at the given path.
        """
    def get_sdf_path(self, path: usdrt.Sdf.Path) -> usdrt.Sdf.Path:
        """
        Returns the Sdf path for the given path.
        
                Args:
                    path (:obj:`usdrt.Sdf.Path`): The path to resolve.
        
                Returns:
                    :obj:`usdrt.Sdf.Path`: The resolved Sdf path.
        """
    def get_sdf_path_type(self) -> type:
        """
        Returns the type associated with Sdf paths used in FabricDataAccessor.
        
                Returns:
                    type: The Sdf path type used by FabricDataAccessor.
        """
    def get_stage(self) -> usdrt.Usd.Stage:
        """
        Gets the USD stage.
        
                Returns:
                    usdrt.Usd.Stage: The USD stage.
        """
    def get_stage_up_axis(self) -> str:
        """
        Retrieves the up-axis of the stage.
        
                Returns:
                    str: The up-axis of the stage.
        """
    def get_string_path(self, path: usdrt.Sdf.Path | str) -> str:
        """
        Converts an Sdf path to its string representation.
        
                Args:
                    path (Union[:obj:`usdrt.Sdf.Path`, str]): The path to convert.
        
                Returns:
                    str: The string representation of the path.
        """
    def has_prim_at_path(self, path: usdrt.Sdf.Path) -> bool:
        """
        Checks if a prim exists at the given path.
        
                Args:
                    path (:obj:`usdrt.Sdf.Path`): The path to check.
        
                Returns:
                    bool: True if a prim exists at the path, False otherwise.
        """
    def is_a_xformable(self, prim: usdrt.Usd.Prim) -> bool:
        """
        Determines if the provided prim is a xformable prim.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if it's a xformable prim, False otherwise.
        """
    def is_instance_proxy(self, prim: usdrt.Usd.Prim) -> bool:
        """
        Determines if the provided prim is an instance proxy.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if it is an instance proxy, False otherwise.
        """
    def is_prim_active(self, prim: usdrt.Usd.Prim) -> bool:
        """
        Determines if the provided prim is active.
        
                Args:
                    prim (:obj:`usdrt.Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if the prim is active, False otherwise.
        """
    def is_transformation_affected_by_attr_named(self, sdf_path: usdrt.Sdf.Path) -> bool:
        """
        Checks if transformation is affected by a specific attribute.
        
                Args:
                    sdf_path (:obj:`usdrt.Sdf.Path`): The Sdf path to check.
        
                Returns:
                    bool: True if transformation is affected, False otherwise.
        """
    def is_valid_path(self, path: typing.Any) -> bool:
        """
        Determines if the given path is a valid Sdf path.
        
                Args:
                    path (Any): The path to validate.
        
                Returns:
                    bool: True if the path is valid, False otherwise.
        """
    def on_ended_transform(self, paths: list[str], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float], old_translations: list[float], old_rotation_eulers: list[float], old_rotation_orders: list[int], old_scales: list[float]):
        """
        Applies transformations to multiple prims.
        
                Args:
                    paths (List[str]): Paths of prims to transform.
                    paths_c (List[int]): C++ compatible path representation.
                    new_translations (List[float]): New translations for the prims.
                    new_rotation_eulers (List[float]): New rotation angles in Euler form.
                    new_rotation_orders (List[int]): New rotation orders for the prims.
                    new_scales (List[float]): New scale values for the prims.
                    old_translations (List[float]): Previous translations for undo functionality.
                    old_rotation_eulers (List[float]): Previous rotations in Euler form for undo.
                    old_rotation_orders (List[int]): Previous rotation orders for undo functionality.
                    old_scales (List[float]): Previous scale values for undo functionality.
        """
    def path_to_int(self, path: usdrt.Sdf.Path) -> int:
        """
        Converts an Sdf path to an integer representation.
        
                Args:
                    path (:obj:`usdrt.Sdf.Path`): The path to convert.
        
                Returns:
                    int: The integer representation of the path.
        """
    def prim_has_prefix(self, path: usdrt.Sdf.Path, prim_path: usdrt.Sdf.Path) -> bool:
        """
        Checks if the given path has the specified prefix.
        
                Args:
                    path (:obj:`usdrt.Sdf.Path`): The path to check for the prefix.
                    prim_path (:obj:`usdrt.Sdf.Path`): The prefix to check against the path.
        
                Returns:
                    bool: True if the path has the prefix, False otherwise.
        """
    def remove_descendent_paths(self, paths: list[usdrt.Sdf.Path]) -> list[usdrt.Sdf.Path]:
        """
        Removes descendent paths from a list of paths.
        
                Args:
                    paths (List[:obj:`usdrt.Sdf.Path`]): The list of paths to process.
        
                Returns:
                    List[:obj:`usdrt.Sdf.Path`]: The list of paths without descendents.
        """
    def remove_update_callback(self, listener: pxr.Tf.Listener = None) -> usdrt.Rt.ChangeTracker:
        """
        Removes the update callback for changes.
        
                Args:
                    listener (Optional[:obj:`pxr.Tf.Listener`]): The listener to remove.
        
                Returns:
                    usdrt.Rt.ChangeTracker: None, indicating the callback has been removed.
        """
    def remove_update_callback_ref_prim_maker(self, listener: pxr.Tf.Listener = None) -> usdrt.Rt.ChangeTracker:
        """
        Removes the update callback reference to the prim maker.
        
                Args:
                    listener (Optional[:obj:`pxr.Tf.Listener`]): The listener to remove.
        
                Returns:
                    usdrt.Rt.ChangeTracker: None, indicating the callback has been removed.
        """
    def set_stage(self):
        """
        Sets the USD stage.
        """
    def setup_update_callback(self) -> usdrt.Rt.ChangeTracker:
        """
        Sets up the update callback for changes.
        
                Returns:
                    usdrt.Rt.ChangeTracker: The change tracker instance.
        """
    def setup_update_callback_ref_prim_maker(self, func: typing.Callable[[list, list[usdrt.Sdf.Path | pxr.Sdf.Path], list[usdrt.Sdf.Path | pxr.Sdf.Path], str], None]) -> usdrt.Rt.ChangeTracker:
        """
        Sets up the update callback with a reference to the prim maker function.
        
                Args:
                    func (Callable): The function to call when changes occur.
        
                Returns:
                    usdrt.Rt.ChangeTracker: The change tracker instance.
        """
    def to_pxr_path(self, path: usdrt.Sdf.Path | pxr.Sdf.Path) -> pxr.Sdf.Path:
        """
        Converts a path to a pxr.Sdf.Path type.
        
                Args:
                    path (Union[:obj:`usdrt.Sdf.Path`, pxr.Sdf.Path]): The path to convert.
        
                Returns:
                    pxr.Sdf.Path: The converted pxr path.
        """
    def update_changes(self):
        """
        Updates changes in the USD stage.
        """
    def update_xform_cache(self):
        """
        Updates the transform cache.
        """
    def xform_set_time(self):
        """
        Sets the time for the transform cache.
        """
    @property
    def is_inited(self):
        """
        Gets the initialization status of the FabricDataAccessor.
        
                Returns:
                    bool: The initialization status.
        """
    @property
    def priority(self) -> int:
        """
        Gets the priority value of the FabricDataAccessor.
        
                Returns:
                    int: The priority value.
        """
    @property
    def priority_write(self) -> int:
        """
        Gets the write priority value of the FabricDataAccessor.
        
                Returns:
                    int: The write priority value.
        """
    @property
    def usd_context(self):
        """
        Gets the USD context associated with the FabricDataAccessor.
        
                Returns:
                    omni.usd.UsdContext: The USD context.
        """
