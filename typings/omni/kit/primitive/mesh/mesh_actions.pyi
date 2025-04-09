"""
This module provides functionalities to register and deregister actions for creating mesh primitives and managing settings within the Omniverse Kit.
"""
from __future__ import annotations
import omni as omni
from omni.kit.primitive.mesh.evaluators import get_geometry_mesh_prim_list
__all__ = ['deregister_actions', 'get_geometry_mesh_prim_list', 'omni', 'register_actions']
def deregister_actions(extension_id):
    """
    Unregisters all actions associated with the given extension ID.
    
        Args:
            extension_id (str): Identifier of the extension whose actions are to be deregistered.
    """
def register_actions(extension_id, cls, get_self_fn):
    """
    Registers actions for creating mesh primitives and showing the settings window.
    
        Args:
            extension_id (str): The identifier of the extension registering the actions.
            cls (type): The class type that provides the actions.
            get_self_fn (Callable): Function to get the instance of the class 'cls'.
    """
