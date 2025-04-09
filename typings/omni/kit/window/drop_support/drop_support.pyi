"""
This module provides the ExternalDragDrop class to handle external drag and drop events for application windows in the omni.kit.window.drop_support package.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni import ui
import os as os
__all__ = ['ExternalDragDrop', 'asyncio', 'carb', 'omni', 'os', 'ui']
class ExternalDragDrop:
    """
    A class to handle external drag and drop events for a specified window.
    
        The class subscribes to drag and drop events on the application's main window and invokes a callback function when an event is detected over the specified window area. It also provides utility functions to check mouse coordinates and expand drag and drop payloads that contain directories.
    
        Args:
            window_name (str): The name of the window to monitor for drag/drop events.
            drag_drop_fn (callable): The callback function to invoke on a drag/drop event.
    """
    def __init__(self, window_name: str, drag_drop_fn: callable):
        """
        Initializes the ExternalDragDrop with a window name and a drag and drop function.
        """
    def _on_drag_drop_external(self, e: carb.events._events.IEvent):
        ...
    def destroy(self):
        """
        Cleans up the resources and subscriptions held by the class instance.
        """
    def expand_payload(self, payload):
        """
        Expands payload to include all files within any directories.
        
                Args:
                    payload (list of str): A list of file paths to expand.
        
                Returns:
                    list of str: A new list of file paths including files within directories in the payload.
        """
    def get_current_mouse_coords(self):
        """
        Retrieves the current mouse coordinates scaled by the DPI scale.
        """
    def is_window_hovered(self, pos_x, pos_y, window_name):
        """
        Checks if the mouse is hovering over the specified window.
        
                Args:
                    pos_x (float): The x-coordinate of the mouse position.
                    pos_y (float): The y-coordinate of the mouse position.
                    window_name (str): The name of the window to check against.
        
                Returns:
                    bool: True if the mouse is hovering over the window, False otherwise.
        """
