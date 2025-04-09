"""
This module defines the action management system for the Collect Tool in the Omniverse Kit, encapsulating action registration, execution, and lifecycle management within a tool or application.
"""
from __future__ import annotations
import carb as carb
import omni as omni
import weakref as weakref
__all__ = ['ACTIONS_TAG', 'ACTION_COLLECT_STAGE', 'Action', 'ActionManager', 'carb', 'omni', 'weakref']
class Action:
    """
    Represents a single action provided by an extension.
    
        This class encapsulates an action including its registration and lifecycle management. It associates an action with a callable function that executes when the action is triggered.
    
        Args:
            extension_name: str
                The name of the extension providing the action.
            action_name: str
                The unique name identifying the action.
            action_display_name: str
                The name displayed in the UI for the action.
            action_description: str
                A brief description of what the action does.
            on_action_fn: Callable[[], None]
                The function to be called when the action is executed.
    """
    def __init__(self, extension_name: str, action_name: str, action_display_name: str, action_description: str, on_action_fn: typing.Callable[[], NoneType]):
        ...
    def _register(self):
        ...
    def destroy(self):
        ...
class ActionManager:
    """
    A class that manages the lifecycle of actions within a tool or application.
    
        This class is responsible for initializing actions when the tool starts up and properly cleaning them up on shutdown. It dynamically registers actions to an extension and ensures they are unregistered when no longer needed. The class also maintains a list of all actions it manages, providing a central point for action management within the application.
        
    """
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, collect_tool_extension):
        ...
ACTIONS_TAG: str = 'Collect Tool Actions'
ACTION_COLLECT_STAGE: str = 'collect_stage'
