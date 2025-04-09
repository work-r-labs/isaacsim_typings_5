"""
This module provides functions for file-related actions within the Omniverse Kit Menu such as posting notifications, quitting the application, handling USD stages, and registering or deregistering actions.
"""
from __future__ import annotations
import carb as carb
import omni as omni
__all__: list = ['register_actions', 'deregister_actions']
def deregister_actions(extension_id):
    """
    Removes all registered actions for a given extension from the action registry.
    
        Args:
            extension_id (str): The unique identifier of the extension whose actions are to be deregistered.
        
    """
def open_stage_with_new_edit_layer():
    """
    Opens the current USD stage with a new edit layer.
    
        This function retrieves the current stage from the USD context, checks if it is valid,
        and then opens it with a new edit layer using the 'open_with_new_edit_layer' method
        from 'omni.kit.window.file'. If the stage is not valid, a notification is posted.
    
        Raises:
            Posts a warning notification if no valid stage is available.
    """
def post_notification(message: str, info: bool = False, duration: int = 3):
    """
    Posts a notification with a given message.
    
        Args:
            message (str): The message to be displayed in the notification.
            info (bool, optional): If True, the notification is of type INFO. Otherwise, it's of type WARNING. Defaults to False.
            duration (int, optional): The duration in seconds for which the notification should be displayed. Defaults to 3.
        
    """
def quit_kit(fast: bool = False):
    """
    Initiates the application shutdown process.
    
        Args:
            fast (bool): If True, sets the application to fast shutdown mode before quitting.
                         Default is False, which means a regular shutdown.
        
    """
def register_actions(extension_id):
    """
    Registers file-related actions within an extension.
    
        Args:
            extension_id (str): The unique identifier for the extension that is registering the actions.
    
        This method registers several actions related to file operations, including exiting the application, exiting quickly, and opening the current stage with a new edit layer. These actions are tagged as 'File Actions' and are made available in the application's UI under the 'File' menu.
        
    """
