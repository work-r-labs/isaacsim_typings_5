"""
This module defines the ExtStatusBar class which provides a custom status bar for the Omniverse application, displaying messages and colors based on application events such as syncing the registry and installing extensions.
"""
from __future__ import annotations
from datetime import datetime
import omni as omni
from omni import ui
__all__: list = ['ExtStatusBar']
class ExtStatusBar:
    """
    A custom status bar extension for the Omniverse application.
    
        This class creates a status bar that listens to specific events in the Omniverse application and updates its display message and color accordingly. It subscribes to events related to the syncing of the registry and the installation of extensions, and it displays success or failure messages with corresponding colors based on the event outcomes.
    
        The status bar can be destroyed when it is no longer needed, which cleans up any subscriptions it has made to the application's message bus.
        
    """
    def __init__(self):
        """
        Initializes the status bar with subscriptions to various events.
        """
    def _refresh_ui(self):
        ...
    def _set_status(self, status, color = 4294967295, evt = None):
        ...
    def destroy(self):
        """
        Cleans up the subscriptions.
        """
FAILURE: int = 4278190284
NEUTRAL: int = 4294967295
SUCCESS: int = 4294939703
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
