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
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.prim.core.settings_constants import DataAccessorConstants as da_c
from omni.kit.viewport.manipulator.transform.model import DataAccessor
from omni.ui import scene as sc
import pxr as pxr
import traceback as traceback
import typing
import usdrt as usdrt
__all__: list = ['UsdDataAccessor']
class UsdDataAccessor(omni.kit.viewport.manipulator.transform.model.DataAccessor):
    """
    A class for handling data access in USD contexts.
    
        This class extends the DataAccessor to provide specific functionalities for working with
        Universal Scene Description (USD) stages and primitives. It encapsulates operations such
        as obtaining USD stage references, transforming USD primitives, and managing USD-specific
        callbacks and cache mechanisms.
    
        Args:
            usd_context_name (str): An optional name identifier for the USD context.
            model: An optional reference to the model associated with the USD context.
    """
    Gf = pxr.Gf
    Sdf = pxr.Sdf
    Tf = pxr.Tf
    Usd = pxr.Usd
    UsdGeom = pxr.UsdGeom
    UsdUtils = pxr.UsdUtils
    def __init__(self, usd_context_name: str = '', model = None):
        """
        Initializes the USD data accessor with optional context name and model.
        """
    def _on_objects_changed(self, notice, sender):
        ...
    def _on_objects_changed_ref_prim_maker(self, notice, sender):
        ...
    def clear_xform_cache(self):
        """
        Clears the transform cache.
        """
    def destroy(self):
        """
        Cleans up the data accessor, clearing all references and settings.
        """
    def do_transform_all_selected_prims_to_manipulator_pivot(self, paths: list[str], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float]):
        """
        Transforms all selected prims to the manipulator pivot.
        
                Args:
                    paths (List[str]): Paths to the prims to transform.
                    paths_c (List[int]): Component counts of the paths.
                    new_translations (List[float]): New translations for the prims.
                    new_rotation_eulers (List[float]): New rotation Eulers for the prims.
                    new_rotation_orders (List[int]): New rotation orders for the prims.
                    new_scales (List[float]): New scales for the prims.
        """
    def do_transform_selected_prims(self, paths: list[str], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float]):
        """
        Transforms selected prims.
        
                Args:
                    paths (List[str]): Paths to the prims to transform.
                    paths_c (List[int]): Component counts of the paths.
                    new_translations (List[float]): New translations for the prims.
                    new_rotation_eulers (List[float]): New rotation Eulers for the prims.
                    new_rotation_orders (List[int]): New rotation orders for the prims.
                    new_scales (List[float]): New scales for the prims.
        """
    def free_stage(self):
        """
        Frees the current Usd.Stage.
        """
    def free_xform_cache(self):
        """
        Frees the transform cache.
        """
    def get_current_time_code(self, currentTime: float) -> pxr.Usd.TimeCode:
        """
        Gets the current time code based on given currentTime.
        
                Args:
                    currentTime (float): The current time to convert to time code.
        
                Returns:
                    pxr.Usd.TimeCode: The time code corresponding to the given currentTime.
        """
    def get_data_tag(self) -> str:
        """
        Gets the data tag associated with USD.
        
                Returns:
                    str: The data tag for USD.
        """
    def get_local_to_world_transform(self, prim: pxr.Usd.Prim) -> usdrt.Gf.Matrix4d:
        """
        Gets the local to world transform matrix of a prim.
        
                Args:
                    prim (pxr.Usd.Prim): The prim to get the transform of.
        
                Returns:
                    usdrt.Gf.Matrix4d: The local to world transform matrix.
        """
    def get_local_transform_SRT(self, prim: pxr.Usd.Prim, time: float = None) -> tuple[usdrt.Gf.Vec3d, usdrt.Gf.Vec3d, usdrt.Gf.Vec3i, usdrt.Gf.Vec3d]:
        """
        Gets the local transform SRT (scale, rotate, translate) of a prim at a given time.
        
                Args:
                    prim (pxr.Usd.Prim): The prim to get the transform of.
                    time (float): The time at which to get the transform.
        
                Returns:
                    Tuple[usdrt.Gf.Vec3d, usdrt.Gf.Vec3d, usdrt.Gf.Vec3i, usdrt.Gf.Vec3d]: The SRT values.
        """
    def get_local_transform_pivot_inv(self, prim: pxr.Usd.Prim, time: float = None) -> usdrt.Gf.Matrix4d:
        """
        Computes the inverse of the local transformation pivot matrix.
        
                Args:
                    prim (:obj:`pxr.Usd.Prim`): The primitive to compute the local transformation pivot for.
                    time (float, optional): The time at which to compute the pivot.
        
                Returns:
                    :obj:`usdrt.Gf.Matrix4d`: The inverse of the local transformation pivot matrix.
        """
    def get_parent_to_world_transform(self, prim: pxr.Usd.Prim) -> usdrt.Gf.Matrix4d:
        """
        Gets the parent to world transform matrix of a prim.
        
                Args:
                    prim (pxr.Usd.Prim): The prim to get the transform of.
        
                Returns:
                    usdrt.Gf.Matrix4d: The parent to world transform matrix.
        """
    def get_prim_at_path(self, path: pxr.Sdf.Path) -> pxr.Usd.Prim:
        """
        Retrieves the prim at the specified path.
        
                Args:
                    path (:obj:`Sdf.Path`): The path where the prim is located.
        
                Returns:
                    :obj:`Usd.Prim`: The prim at the given path.
        """
    def get_sdf_path(self, path: pxr.Sdf.Path) -> pxr.Sdf.Path:
        """
        Converts the given path to an SDF path.
        
                Args:
                    path (:obj:`Sdf.Path`): The path to convert.
        
                Returns:
                    :obj:`Sdf.Path`: The converted SDF path.
        """
    def get_sdf_path_type(self) -> type:
        """
        Returns the type used for SDF paths.
        
                Returns:
                    type: The SDF path type.
        """
    def get_stage(self):
        """
        Returns the current Usd.Stage.
        
                Returns:
                    The current Usd.Stage.
        """
    def get_stage_up_axis(self) -> str:
        """
        Gets the up axis of the current stage.
        
                Returns:
                    str: The up axis ('Y' or 'Z').
        """
    def get_string_path(self, path: pxr.Sdf.Path | str) -> str:
        """
        Converts the given path to a string representation.
        
                Args:
                    path (Union[:obj:`Sdf.Path`, str]): The path to convert.
        
                Returns:
                    str: The string representation of the path.
        """
    def has_prim_at_path(self, path: pxr.Sdf.Path) -> bool:
        """
        Checks if there is a prim at the specified path.
        
                Args:
                    path (:obj:`Sdf.Path`): The path to check.
        
                Returns:
                    bool: True if there is a prim, False otherwise.
        """
    def is_a_xformable(self, prim: pxr.Usd.Prim) -> bool:
        """
        Checks if the given prim is a Xformable type.
        
                Args:
                    prim (:obj:`Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if the prim is a Xformable, False otherwise.
        """
    def is_instance_proxy(self, prim: pxr.Usd.Prim) -> bool:
        """
        Determines if the given prim is an instance proxy.
        
                Args:
                    prim (:obj:`Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if it is an instance proxy, False otherwise.
        """
    def is_prim_active(self, prim: pxr.Usd.Prim) -> bool:
        """
        Checks if the specified prim is active.
        
                Args:
                    prim (:obj:`Usd.Prim`): The prim to check.
        
                Returns:
                    bool: True if the prim is active, False otherwise.
        """
    def is_transformation_affected_by_attr_named(self, name: str) -> bool:
        """
        Checks if transformation is affected by the specified attribute name.
        
                Args:
                    name (str): The name of the attribute.
        
                Returns:
                    bool: True if affected, False otherwise.
        """
    def is_valid_path(self, path: typing.Any) -> bool:
        """
        Checks if the given path is a valid SDF path.
        
                Args:
                    path (Any): The path to check.
        
                Returns:
                    bool: True if the path is valid, False otherwise.
        """
    def on_ended_transform(self, paths: list[pxr.Sdf.Path], paths_c: list[int], new_translations: list[float], new_rotation_eulers: list[float], new_rotation_orders: list[int], new_scales: list[float], old_translations: list[float], old_rotation_eulers: list[float], old_rotation_orders: list[int], old_scales: list[float]):
        """
        Handles the end of a transformation operation.
        
                Args:
                    paths (List[pxr.Sdf.Path]): Paths to the prims that were transformed.
                    paths_c (List[int]): Component counts of the paths.
                    new_translations (List[float]): New translations for the prims.
                    new_rotation_eulers (List[float]): New rotation Eulers for the prims.
                    new_rotation_orders (List[int]): New rotation orders for the prims.
                    new_scales (List[float]): New scales for the prims.
                    old_translations (List[float]): Previous translations for the prims.
                    old_rotation_eulers (List[float]): Previous rotation Eulers for the prims.
                    old_rotation_orders (List[int]): Previous rotation orders for the prims.
                    old_scales (List[float]): Previous scales for the prims.
        """
    def path_to_int(self, path: pxr.Sdf.Path) -> int:
        """
        Converts the given SDF path to an integer representation.
        
                Args:
                    path (:obj:`Sdf.Path`): The SDF path to convert.
        
                Returns:
                    int: The integer representation of the path.
        """
    def prim_has_prefix(self, path: pxr.Sdf.Path, prim_path: pxr.Sdf.Path) -> bool:
        """
        Checks if the given path has the specified prefix.
        
                Args:
                    path (pxr.Sdf.Path): The path to check.
                    prim_path (pxr.Sdf.Path): The prefix to look for.
        
                Returns:
                    bool: True if path has the prefix, False otherwise.
        """
    def remove_descendent_paths(self, paths: list[pxr.Sdf.Path]) -> list[pxr.Sdf.Path]:
        """
        Removes descendent paths from the given list of paths.
        
                Args:
                    paths (List[:obj:`Sdf.Path`]): The list of paths to process.
        
                Returns:
                    List[:obj:`Sdf.Path`]: The list of paths without descendants.
        """
    def remove_update_callback(self, listener: pxr.Tf.Listener) -> pxr.Tf.Listener:
        """
        Removes the update callback.
        
                Args:
                    listener (pxr.Tf.Listener): The listener to remove.
        """
    def remove_update_callback_ref_prim_maker(self, listener: pxr.Tf.Listener):
        """
        Removes the update callback for reference prim maker.
        
                Args:
                    listener (pxr.Tf.Listener): The listener to remove.
        """
    def set_stage(self) -> pxr.Usd.Stage:
        """
        Sets the current stage to the USD context's stage.
        """
    def setup_update_callback(self) -> pxr.Tf.Listener:
        """
        Sets up a callback for USD object changes.
        """
    def setup_update_callback_ref_prim_maker(self, func: typing.Callable[[list, list[usdrt.Sdf.Path | pxr.Sdf.Path], list[usdrt.Sdf.Path | pxr.Sdf.Path], str], None]) -> pxr.Tf.Listener:
        """
        Sets up a callback for reference prim maker.
        
                Args:
                    func (Callable): The function to call on update.
        """
    def to_pxr_path(self, path: usdrt.Sdf.Path | pxr.Sdf.Path) -> pxr.Sdf.Path:
        """
        Converts given path to pxr.Sdf.Path format.
        
                Args:
                    path (Union[usdrt.Sdf.Path, pxr.Sdf.Path]): The path to convert.
        
                Returns:
                    pxr.Sdf.Path: The converted path in pxr.Sdf.Path format.
        """
    def update_xform_cache(self):
        """
        Updates the transform cache with the current time and stage.
        """
    def xform_set_time(self):
        """
        Updates the transform cache to the current time.
        """
    @property
    def is_inited(self):
        """
        Gets the initialization state of the data accessor.
        
                Returns:
                    bool: True if the data accessor is initialized, False otherwise.
        """
    @property
    def priority(self) -> int:
        """
        Gets the priority level for the data accessor.
        
                Returns:
                    int: The priority level.
        """
    @property
    def priority_write(self) -> int:
        """
        Gets the write priority level for the data accessor.
        
                Returns:
                    int: The write priority level.
        """
    @property
    def usd_context(self):
        """
        Gets the USD context used by the data accessor.
        
                Returns:
                    :obj:`Usd.Context`: The USD context.
        """
