"""
This module provides functionalities to manage a global singleton instance of PrimDataAccessorRegistry, including getting, setting, and resetting the registry.
"""
from __future__ import annotations
import omni.kit.manipulator.prim.core.prim_data_accessor_registry
from omni.kit.manipulator.prim.core.prim_data_accessor_registry import PrimDataAccessorRegistry
__all__ = ['PrimDataAccessorRegistry', 'clean_prim_data_accessor_registry', 'get_prim_data_accessor_registry', 'set_prim_data_accessor_registry']
def clean_prim_data_accessor_registry():
    """
    Resets the global `PrimDataAccessorRegistry` instance to `None`.
    
        This function is intended to clear the current prim data accessor registry in
        the system, effectively resetting its state for purposes such as
        reinitialization or cleanup at the end of a session.
    """
def get_prim_data_accessor_registry() -> omni.kit.manipulator.prim.core.prim_data_accessor_registry.PrimDataAccessorRegistry:
    """
    Returns the singleton instance of the PrimDataAccessorRegistry.
    
        Returns:
            :obj:`PrimDataAccessorRegistry`: The singleton instance of the PrimDataAccessorRegistry.
    """
def set_prim_data_accessor_registry(obj: omni.kit.manipulator.prim.core.prim_data_accessor_registry.PrimDataAccessorRegistry):
    """
    Sets the global PrimDataAccessorRegistry instance.
    
        Args:
            obj (:obj:`PrimDataAccessorRegistry`): The PrimDataAccessorRegistry instance to set as the global registry.
    """
__prim_data_accessor_registry: omni.kit.manipulator.prim.core.prim_data_accessor_registry.PrimDataAccessorRegistry  # value = <omni.kit.manipulator.prim.core.prim_data_accessor_registry.PrimDataAccessorRegistry object>
