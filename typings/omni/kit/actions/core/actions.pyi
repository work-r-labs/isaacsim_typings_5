from __future__ import annotations
import omni as omni
from omni.kit.actions.core._kit_actions_core import Action
from omni.kit.actions.core._kit_actions_core import IActionRegistry
from omni.kit.actions.core._kit_actions_core import acquire_action_registry
from omni.kit.actions.core._kit_actions_core import release_action_registry
__all__ = ['Action', 'ActionsExtension', 'IActionRegistry', 'acquire_action_registry', 'execute_action', 'get_action_registry', 'omni', 'release_action_registry']
class ActionsExtension(omni.ext._extensions.IExt):
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
def execute_action(extension_id: str, action_id: str, *args, **kwargs):
    """
    
        Find and execute an action.
    
        Args:
            extension_id: The id of the source extension that registered the action.
            action_id: Id of the action, unique to the extension that registered it.
            *args: Variable length argument list which will be forwarded to execute.
            **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
    
        Return:
            The result of executing the action, which is an arbitrary Python object
            that could be None (will also return None if the action was not found).
        
    """
def get_action_registry() -> omni.kit.actions.core._kit_actions_core.IActionRegistry:
    """
    
        Get the action registry.
    
        Return:
            ActionRegistry object which implements the IActionRegistry interface.
        
    """
_action_registry: omni.kit.actions.core._kit_actions_core.IActionRegistry  # value = <omni.kit.actions.core._kit_actions_core.IActionRegistry object>
