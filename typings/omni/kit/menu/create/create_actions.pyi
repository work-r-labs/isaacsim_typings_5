"""
This module defines functions to register and deregister create actions for USD prims, cameras, shapes, lights, and audio prims in Omniverse Kit.
"""
from __future__ import annotations
import omni as omni
__all__: list = list()
def _get_action_name(name):
    """
    Converts a given name to a format suitable for action identifiers.
    
        Args:
            name (str): The original name string to be converted.
    
        Returns:
            str: The converted string with spaces and hyphens replaced by underscores and in lowercase.
    """
def deregister_actions(extension_id):
    """
    Deregisters all actions associated with a given extension ID.
    
        This function unregisters all actions that were previously registered for a specific extension.
        This is typically called when an extension is being unloaded to clean up any actions it
        contributed to the application's UI or action registry.
    
        Args:
            extension_id (str): The identifier for the extension whose actions are to be deregistered.
    """
def register_actions(extension_id, cls, get_self_fn):
    """
    Registers multiple create actions to the Omniverse Kit action registry.
    
        Args:
            extension_id (str): The ID of the extension registering these actions.
            cls: The class that contains callback methods for the actions being registered.
            get_self_fn (Callable): Function that returns an instance of the class containing the action callbacks.
    
        This function registers several actions related to creating USD prims, including general prims, camera, scope, xform, various shapes, lights, and audio prims. It also includes a toggle for high-quality options. Each action is associated with a display name, description, and belongs to a specified tag group for organization.
        
    """
