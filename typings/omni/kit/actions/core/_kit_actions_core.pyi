"""
pybind11 omni.kit.actions.core bindings
"""
from __future__ import annotations
import typing
__all__ = ['Action', 'IActionRegistry', 'acquire_action_registry', 'release_action_registry']
class Action:
    """
    Abstract action base class.
    """
    def __init__(self, extension_id: str, action_id: str, python_object: typing.Any, display_name: str = '', description: str = '', icon_url: str = '', tag: str = '') -> None:
        """
                     Create an action.
        
                     Args:
                         extension_id: The id of the source extension registering the action.
                         action_id: Id of the action, unique to the extension registering it.
                         python_object: The Python object called when the action is executed.
                         display_name: The name of the action for display purposes.
                         description: A brief description of what the action does.
                         icon_url: The URL of an image which represents the action.
                         tag: Arbitrary tag used to group sets of related actions.
        
                     Return:
                         The action that was created.
        """
    def execute(self, *args, **kwargs) -> typing.Any:
        """
                     Execute the action.
        
                     Args:
                         *args: Variable length argument list which will be forwarded to execute.
                         **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
        
                     Return:
                         The result of executing the action, converted to a Python object (could be None).
        """
    def invalidate(self) -> None:
        """
                     Invalidate this action so that executing it will not do anything.
                     This can be called if it is no longer safe to execute the action,
                     and by default is called when deregistering an action (optional).
        """
    @property
    def description(self) -> str:
        """
                     Get the description of this action.
        
                     Return:
                         str: The description of this action.
        """
    @property
    def display_name(self) -> str:
        """
                     Get the display name of this action.
        
                     Return:
                         str: The display name of this action.
        """
    @property
    def extension_id(self) -> str:
        """
                     Get the id of the source extension which registered this action.
        
                     Return:
                         str: The id of the source extension which registered this action.
        """
    @property
    def icon_url(self) -> str:
        """
                     Get the URL of the icon used to represent this action.
        
                     Return:
                         str: The URL of the icon used to represent this action.
        """
    @property
    def id(self) -> str:
        """
                     Get the id of this action, unique to the extension that registered it.
        
                     Return:
                         str: The id of this action, unique to the extension that registered it.
        """
    @property
    def parameters(self) -> dict:
        """
                     Get the parameters accepted by this action's execute function.
        
                     Return:
                         dict: The parameters accepted by this action's execute function.
        """
    @property
    def requires_parameters(self) -> bool:
        """
                     Query whether this action requires any parameters to be passed when executed?
        
                     Return:
                         bool: True if this action requires any parameters to be passed when executed, false otherwise.
        """
    @property
    def tag(self) -> str:
        """
                     Get the tag that this action is grouped with.
        
                     Return:
                         str: The tag that this action is grouped with.
        """
class IActionRegistry:
    """
    
                 Maintains a collection of all registered actions and allows any extension to discover them.
                 
    """
    @typing.overload
    def deregister_action(self, action: ..., invalidate: bool = True) -> None:
        """
                     Deregister an action.
        
                     Args:
                         action: The action to deregister.
                         invalidate: Should the action be invalidated so executing does nothing?
        """
    @typing.overload
    def deregister_action(self, extension_id: str, action_id: str, invalidate: bool = True) -> ...:
        """
                     Find and deregister an action.
        
                     Args:
                         extension_id: The id of the source extension that registered the action.
                         action_id: Id of the action, unique to the extension that registered it.
                         invalidate: Should the action be invalidated so executing does nothing?
        
                     Return:
                         The action if it exists and was deregistered, an empty object otherwise.
        """
    def deregister_all_actions_for_extension(self, extension_id: str, invalidate: bool = True) -> None:
        """
                     "Deregister all actions that were registered by the specified extension.
        
                     Args:
                         extension_id: The id of the source extension that registered the actions.
                         iinvalidate: Should the actions be invalidated so executing does nothing?
        """
    def execute_action(self, extension_id: str, action_id: str, *args, **kwargs) -> typing.Any:
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
    def get_action(self, extension_id: str, action_id: str) -> ...:
        """
                     Get an action.
        
                     Args:
                         extension_id: The id of the source extension that registered the action.
                         action_id: Id of the action, unique to the extension that registered it.
        
                     Return:
                         The action if it exists, an empty object otherwise.
        """
    def get_all_actions(self) -> list[...]:
        """
                     Get all registered actions.
        
                     Return:
                         All registered actions.
        """
    def get_all_actions_for_extension(self, extension_id: str) -> list[...]:
        """
                     Get all actions that were registered by the specified extension.
        
                     Args:
                         extension_id: The id of the source extension that registered the actions.
        
                     Return:
                         All actions that were registered by the specified extension.
        """
    @typing.overload
    def register_action(self, action: ...) -> None:
        """
                     Register an action.
        
                     Args:
                         action: The action to register.
        """
    @typing.overload
    def register_action(self, extension_id: str, action_id: str, python_object: typing.Any, display_name: str = '', description: str = '', icon_url: str = '', tag: str = '') -> ...:
        """
                     Create and register an action.
        
                     Args:
                         extension_id: The id of the source extension registering the action.
                         action_id: Id of the action, unique to the extension registering it.
                         python_object: The Python object called when the action is executed.
                         display_name: The name of the action for display purposes.
                         description: A brief description of what the action does.
                         icon_url: The URL of an image which represents the action.
                         tag: Arbitrary tag used to group sets of related actions.
        
                     Return:
                         The action if it was created and registered, an empty object otherwise.
        """
def acquire_action_registry(plugin_name: str = None, library_path: str = None) -> IActionRegistry:
    ...
def release_action_registry(arg0: IActionRegistry) -> None:
    ...
