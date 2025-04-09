"""
This module provides classes and functionality for managing data accessors and transforming USD prims within the Omniverse Kit.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.prim.core.global_registry import get_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.settings_constants import DataAccessorConstants as da_c
from omni.kit.manipulator.prim.core.settings_constants import DataRegistryEventTypes as da_ev_c
import pxr as pxr
import typing
import usdrt as usdrt
__all__ = ['PrimDataAccessorSelector', 'TransformData', 'carb', 'da_c', 'da_ev_c', 'get_prim_data_accessor_registry', 'omni', 'pxr', 'usdrt']
class PrimDataAccessorSelector:
    """
    A class to select and manage data accessors for USD prims.
    
        This class is responsible for storing and managing different data accessors for prims in a USD scene. It allows for
        the retrieval and modification of prim data based on the type of data accessor. The class also handles
        registration for data accessor changes and updates the transformations of selected prims.
    
        Args:
            model: The model associated with the data accessors.
            usd_context_name (str): The name of the USD context to be used. Defaults to an empty string.
            dataTypes (List[str]): A list of data types that the data accessor should handle. Defaults to ['FABRIC', 'USD'].
        
    """
    @staticmethod
    def do_transform_selected_prims(*args, **kwds):
        """
        Transforms the selected prims.
        
                Args:
                    args (List): The arguments for the transformation.
        
                Keyword Args:
                    paths (List): The paths of the prims to transform.
                    paths_c (List): The compact paths of the prims to transform.
                    new_translations (List): The new translation values.
                    new_rotation_eulers (List): The new rotation euler angles.
                    new_rotation_orders (List): The new rotation orders.
                    new_scales (List): The new scale values.
        """
    def __init__(self, model, usd_context_name = '', dataTypes = ['FABRIC', 'USD']):
        """
        Constructor for PrimDataAccessorSelector.
        """
    def _add_data_accessor(self, data_tag: str):
        ...
    def _euler_from_quaternion_ro(self, q, conv_order):
        ...
    def _get_sdf_path_data_tag(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> str:
        ...
    def _on_data_accessor_changed(self, event: carb.events.IEvent):
        ...
    def _prim_data_type(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim) -> type:
        ...
    def _process(self):
        ...
    def _quaternion_from_euler(self, eulers: tuple[float, ...], ro: usdrt.Gf.Vec3i):
        ...
    def _remove_data_accessor(self, data_tag: str):
        ...
    def _sdf_path_data_type(self, path) -> type:
        ...
    def _set_def_type(self):
        ...
    def _str_path_data_type(self, path) -> type:
        ...
    def _upd_data_accessors(self):
        ...
    def add_data(self, path: usdrt.Sdf.Path | pxr.Sdf.Path, translation: usdrt.Gf.Vec3d, rotation: usdrt.Gf.Vec3d, ro: usdrt.Gf.Vec3i, scale: usdrt.Gf.Vec3d):
        """
        Adds transformation data for a given path.
        
                Args:
                    path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The path of the USD prim.
                    translation (usdrt.Gf.Vec3d): The translation vector.
                    rotation (usdrt.Gf.Vec3d): The rotation vector (euler angles).
                    ro (usdrt.Gf.Vec3i): The rotation order.
                    scale (usdrt.Gf.Vec3d): The scaling vector.
        """
    def add_data_full(self, path: usdrt.Sdf.Path | pxr.Sdf.Path, translation: usdrt.Gf.Vec3d, rotation: usdrt.Gf.Vec3d, ro: usdrt.Gf.Vec3i, scale: usdrt.Gf.Vec3d, translation_old: usdrt.Gf.Vec3d, rotation_old: usdrt.Gf.Vec3d, ro_old: usdrt.Gf.Vec3i, scale_old: usdrt.Gf.Vec3d):
        """
        Adds full transformation data including old and new values for a given path.
        
                Args:
                    path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The path of the USD prim.
                    translation (usdrt.Gf.Vec3d): The new translation vector.
                    rotation (usdrt.Gf.Vec3d): The new rotation vector (euler angles).
                    ro (usdrt.Gf.Vec3i): The new rotation order.
                    scale (usdrt.Gf.Vec3d): The new scaling vector.
                    translation_old (usdrt.Gf.Vec3d): The old translation vector.
                    rotation_old (usdrt.Gf.Vec3d): The old rotation vector (euler angles).
                    ro_old (usdrt.Gf.Vec3i): The old rotation order.
                    scale_old (usdrt.Gf.Vec3d): The old scaling vector.
        """
    def cache_prim_data(self, paths):
        """
        Cache the prim data for the given paths.
        
                Args:
                    paths (List[Union[usdrt.Sdf.Path, pxr.Sdf.Path]]): The list of paths to cache.
        """
    def clear_xform_cache(self):
        """
        Clears the transformation cache.
        """
    def destroy(self):
        """
        Destroy the PrimDataAccessorSelector and its resources.
        """
    def do_transform_all_selected_prims_to_manipulator_pivot(self, paths: list[usdrt.Sdf.Path | pxr.Sdf.Path], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float]):
        """
        Transforms all selected prims to the manipulator pivot.
        
                Args:
                    paths (List[Union[usdrt.Sdf.Path, pxr.Sdf.Path]]): The paths of prims to transform.
                    new_translations (List[float]): The new translation values.
                    new_rotation_eulers (List[float]): The new rotation euler angles.
                    new_rotation_orders (List[int]): The new rotation orders.
                    new_scales (List[float]): The new scale values.
        """
    def free_stage(self):
        """
        Frees the USD stage.
        """
    def free_xform_cache(self):
        """
        Frees the transformation cache.
        """
    def get_current_time_code(self, currentTime: float) -> pxr.Usd.TimeCode:
        """
        Gets the current time code.
        
                Args:
                    currentTime (float): The current time to retrieve the time code for.
        """
    def get_data_accessor(self, data_type: str):
        """
        Get the data accessor for a given data type.
        
                Args:
                    data_type (str): The data type to retrieve the accessor for.
        """
    def get_data_accessors(self):
        """
        Retrieve sorted list of data accessors based on priority.
        """
    def get_data_accessors_write_priority(self):
        """
        Retrieve list of data accessors sorted by write priority.
        """
    def get_data_types(self):
        """
        Get a mapping of SDF path types to data accessor tags.
        """
    def get_local_to_world_transform(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim, use_cache: bool = False) -> usdrt.Gf.Matrix4d:
        """
        Get the local to world transform matrix for a prim, with optional caching.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The prim to get the transform for.
                    use_cache (bool): Flag to indicate whether to use cached data.
        """
    def get_local_transform_SRT(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim, time: float) -> tuple[usdrt.Gf.Vec3d, usdrt.Gf.Vec3d, usdrt.Gf.Vec3i, usdrt.Gf.Vec3d]:
        """
        Get the local transform SRT (Scale, Rotate, Translate) for a prim at a given time.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The prim to get the transform for.
                    time (float): The time at which to get the transform.
        """
    def get_local_transform_pivot_inv(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim, time = pxr.Usd.TimeCode) -> usdrt.Gf.Matrix4d:
        """
        Get the inverse of the local transform pivot for a prim at a given time.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The prim to get the pivot for.
                    time (pxr.Usd.TimeCode): The time at which to get the pivot.
        """
    def get_parent_to_world_transform(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim, use_cache: bool = False) -> usdrt.Gf.Matrix4d:
        """
        Get the parent to world transform matrix for a prim, with optional caching.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The prim to get the transform for.
                    use_cache (bool): Flag to indicate whether to use cached data.
        """
    def get_prim_at_path(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path, use_cache: bool = False) -> usdrt.Usd.Prim | pxr.Usd.Prim:
        """
        Get the prim at the specified SDF path, with optional caching.
        
                Args:
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path where the prim is located.
                    use_cache (bool): Flag to indicate whether to use cached data.
        """
    def get_sdf_path(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> usdrt.Sdf.Path | pxr.Sdf.Path:
        """
        Get the SDF path.
        
                Args:
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path.
        """
    def get_sdf_path_by_priority(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> usdrt.Sdf.Path | pxr.Sdf.Path:
        """
        Get the SDF path by priority.
        
                Args:
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path to prioritize.
        """
    def get_stage(self) -> usdrt.Usd.Stage | pxr.Usd.Stage:
        """
        Retrieves the USD stage.
        """
    def get_stage_up_axis(self) -> str:
        """
        Retrieves the up axis of the stage.
        """
    def get_string_path(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> str:
        """
        Get the string representation of an SDF path.
        
                Args:
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path.
        """
    def has_prim_at_path(self, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> bool:
        """
        Check if a prim exists at the given SDF path.
        
                Args:
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path to check.
        """
    def is_a_xformable(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim) -> bool:
        """
        Checks if the prim can be transformed.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The USD prim to check.
        """
    def is_instance_proxy(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim) -> bool:
        """
        Checks if the prim is an instance proxy.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The USD prim to check.
        """
    def is_prim_active(self, prim: usdrt.Usd.Prim | pxr.Usd.Prim) -> bool:
        """
        Checks if the prim is active.
        
                Args:
                    prim (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The USD prim to check.
        """
    def is_ready(self) -> bool:
        """
        Check if the data accessor selector is ready for operation.
        """
    def is_sdf_path_in_set(self, path: usdrt.Sdf.Path | pxr.Sdf.Path, array = ...) -> usdrt.Usd.Prim | pxr.Usd.Prim:
        """
        Check if the SDF path is in a given set or list.
        
                Args:
                    path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The path to check.
                    array (Union[Set, List]): The set or list to check against.
        """
    def is_transformation_affected_by_attr_named(self, sdf_path: usdrt.Usd.Prim | pxr.Usd.Prim) -> bool:
        """
        Checks if the prim's transformation is affected by an attribute.
        
                Args:
                    sdf_path (Union[usdrt.Usd.Prim, pxr.Usd.Prim]): The USD prim to check.
        """
    def on_ended_transform(self):
        """
        Ends the transform operation.
        """
    def prim_has_prefix(self, sdf_path0: usdrt.Sdf.Path | pxr.Sdf.Path, sdf_path: usdrt.Sdf.Path | pxr.Sdf.Path) -> bool:
        """
        Check if the given SDF path has the specified prefix.
        
                Args:
                    sdf_path0 (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The prefix path.
                    sdf_path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The SDF path to check.
        """
    def remove_descendent_paths(self, paths) -> usdrt.Sdf.Path | pxr.Sdf.Path:
        """
        Remove descendant paths from a list.
        
                Args:
                    paths (List[Union[usdrt.Sdf.Path, pxr.Sdf.Path]]): The list of paths to process.
        """
    def remove_update_callback(self, listener: pxr.Tf.Listener = None) -> usdrt.Rt.ChangeTracker | pxr.Tf.Listener:
        """
        Removes an update callback.
        
                Args:
                    listener (:obj:`pxr.Tf.Listener`): The listener to be removed.
        """
    def remove_update_callback_ref_prim_maker(self, listener: pxr.Tf.Listener = None) -> usdrt.Rt.ChangeTracker | pxr.Tf.Listener:
        """
        Removes an update callback for reference prim maker.
        
                Args:
                    listener (:obj:`pxr.Tf.Listener`): The listener to be removed.
        """
    def reset_data(self):
        """
        Resets the transform data map.
        """
    def set_stage(self):
        """
        Sets the USD stage.
        """
    def setup_update_callback(self):
        """
        Sets up the update callback.
        """
    def setup_update_callback_ref_prim_maker(self, func: typing.Callable[[list, list[usdrt.Sdf.Path | pxr.Sdf.Path], list[usdrt.Sdf.Path | pxr.Sdf.Path], str], None]) -> usdrt.Rt.ChangeTracker | pxr.Tf.Listener:
        """
        Sets up an update callback for reference prim maker.
        
                Args:
                    func (:obj:`Callable`): The function to call when the update occurs.
        """
    def update_xform_cache(self):
        """
        Updates the transformation cache.
        """
    def xform_set_time(self):
        """
        Sets the time for the transform.
        """
    @property
    def Sdf(self):
        """
        Gets the Sdf module.
        
                Returns:
                    The Sdf module.
        """
    @property
    def Tf(self):
        """
        Gets the Tf module.
        
                Returns:
                    The Tf module.
        """
    @property
    def Usd(self):
        """
        Gets the Usd module.
        
                Returns:
                    The Usd module.
        """
    @property
    def UsdGeom(self):
        """
        Gets the UsdGeom module.
        
                Returns:
                    The UsdGeom module.
        """
    @property
    def usd_context(self):
        """
        Gets the USD context.
        
                Returns:
                    The USD context.
        """
class TransformData:
    """
    A class for storing transformation data for USD prims.
    
        This class holds lists of transformation-related data such as paths, translations, rotations, scales, and their old values before the transformation. It is intended to be used by higher-level classes or functions performing transformations on USD prims to keep track of the initial and resulting state of each transformed prim.
        
    """
    def __init__(self):
        """
        Initializes the TransformData instance.
        """
