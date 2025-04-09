"""
Material library MaterialUtils class. Provides upto date cache of known materials in stage.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import Enum
import omni as omni
from omni.usd._impl.utils import PrimCaching
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import typing
import weakref as weakref
__all__: list = ['UpdateState', 'MaterialUtils', 'initalize_material_utils', 'destroy_material_utils', 'add_cache_changed_fn', 'remove_cache_changed_fn', 'get_materials_from_stage', 'get_materials_from_stage_async', 'add_materials_from_stage_filter_func', 'remove_materials_from_stage_filter_func', 'get_prim_children_paths']
class MaterialUtils:
    """
    Material library MaterialUtils class. Provides upto date cache of known materials in stage.
    """
    @staticmethod
    def is_valid_material(prim, filter_funcs, ext_filter_func = None):
        """
        
                Is prim a valid material.
        
                Args:
                    filter_funcs (list): List of additional functions to validate material prim.
                    ext_filter_func (callable): Additional function to validate material prim.
                Returns:
                    (bool): True if valid material otherwise False.
                
        """
    def _MaterialUtils__get_materials_from_stage_async(self, stage: pxr.Usd.Stage, stop_event: asyncio.locks.Event, full_list_event: asyncio.locks.Event, update_func: callable, wait_frames: int, ext_filter_func: callable):
        ...
    def __init__(self):
        ...
    def _on_prim_cache_changed_func(self):
        ...
    def add_cache_changed_fn(self, cache_changed_fn: callable):
        """
        
                Adds callback to material cache changed list.
        
                Args:
                    cache_changed_fn (callable): Callback.
                
        """
    def add_materials_from_stage_filter_func(self, filter_fn: callable):
        """
        
                Add filter callback function to get_materials_from_stage_async() callback.
        
                Args:
                    filter_fn (callable): Filter function.
                
        """
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def flush_material_cache(self):
        """
        Clear material cache.
        """
    def get_materials_from_stage(self, ext_filter_func = None):
        """
        
                Get list of materials for stage. NOTE: This function can block on large stages.
        
                Args:
                    ext_filter_func (callable): filter function to remove material names from list. Optional.
                Returns:
                    (list): list of materials names
                
        """
    def get_materials_from_stage_async(self, update_func: callable, wait_frames: int, ext_filter_func: callable):
        """
        
                Get list of materials for stage asynchronously.
        
                Args:
                    update_func (callable): function to call when new material names are available.
                    wait_frames (int): number of frames to wait before starting to get materials list.
                    ext_filter_func (callable): filter function to remove material names from list. Optional.
                
        """
    def remove_cache_changed_fn(self, cache_changed_fn: callable):
        """
        
                Remove callback to material cache changed list.
        
                Args:
                    cache_changed_fn (callable): Callback.
                
        """
    def remove_materials_from_stage_filter_func(self, filter_fn: callable):
        """
        
                Remove filter callback function from get_materials_from_stage_async() callback.
        
                Args:
                    filter_fn (callable): Filter function.
                
        """
    def stop(self):
        """
        Stop traversing the stage
        """
class UpdateState(enum.Enum):
    """
    State of cache of known materials in stage, passed to update_func.
    """
    COMPLETE_LIST: typing.ClassVar[UpdateState]  # value = <UpdateState.COMPLETE_LIST: 3>
    UPDATE: typing.ClassVar[UpdateState]  # value = <UpdateState.UPDATE: 1>
    UPDATE_COMPLETE: typing.ClassVar[UpdateState]  # value = <UpdateState.UPDATE_COMPLETE: 2>
def add_cache_changed_fn(cache_changed_fn: callable):
    """
    
        Adds callback to material cache changed list.
    
        Args:
            cache_changed_fn (callable): Callback.
        
    """
def add_materials_from_stage_filter_func(filter_fn: callable):
    """
    
        Add filter callback function to get_materials_from_stage_async() callback.
    
        Args:
            filter_fn (callable): Filter function.
        
    """
def destroy_material_utils():
    """
    Destroy material_utils. This should only be called from omni.kit.material.library on_shutdown.
    """
def get_materials_from_stage(none_string: str):
    """
    
        Get list of materials for stage. NOTE: This function can block on large stages.
    
        Args:
            none_string (str): name of "None" material to be added to list
        Returns:
            (list): list of materials names
        
    """
def get_materials_from_stage_async(update_func: callable, wait_frames: int = 1, ext_filter_func: callable = None):
    """
    
        Get list of materials for stage asynchronously.
    
        Args:
            update_func (callable): function to call when new material names are available.
            wait_frames (int): number of frames to wait before starting to get materials list.
            ext_filter_func (callable): filter function to remove material names from list. Optional.
        
    """
def get_prim_children_paths(prim_path: pxr.Sdf.Path):
    """
    
        Get all child prims from prim_path.
    
        Args:
            prim_path (str): prim path.
        Returns:
            (list): list of child prims
        
    """
def initalize_material_utils():
    """
    Initialize material_utils. This should only be called from omni.kit.material.library on_startup.
    """
def remove_cache_changed_fn(cache_changed_fn: callable):
    """
    
        Remove callback to material cache changed list.
    
        Args:
            cache_changed_fn (callable): Callback.
        
    """
def remove_materials_from_stage_filter_func(filter_fn: callable):
    """
    
        Remove filter callback function from get_materials_from_stage_async() callback.
    
        Args:
            filter_fn (callable): Filter function.
        
    """
g_singleton: MaterialUtils  # value = <omni.kit.material.library.material_utils.MaterialUtils object>
