"""
This module provides functions to register and deregister a variety of editing-related actions for extensions using the omni.kit.actions.core module.
"""
from __future__ import annotations
import asyncio as asyncio
import omni as omni
__all__: list = ['register_actions', 'deregister_actions']
def deregister_actions(extension_id):
    """
    Deregisters all actions associated with a given extension ID from the action registry.
    
        Args:
            extension_id (str): The unique identifier of the extension whose actions are to be deregistered.
    """
def register_actions(extension_id, cls, get_self_fn):
    """
    Registers actions related to editing operations for a given extension.
    
        This function sets up a series of editing actions and associates them with callback functions,
        which are intended to be triggered by the user through the application's UI. It uses the action
        registry provided by the omni.kit.actions.core module to register each action with a unique name,
        a callback, a display name for the UI, a description, and a tag to categorize the action.
    
        Args:
            extension_id (str): The identifier of the extension for which the actions are to be registered.
            cls: The class that contains the implementation of the actions. This class should provide methods that correspond to the actions being registered.
            get_self_fn (callable): A function that, when called, returns an instance of the class that contains the action implementations.
    
        Returns:
            None
    """
