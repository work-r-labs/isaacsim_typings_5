from __future__ import annotations
import omni as omni
from omni.kit.window.console._console import ConsoleWidget
from omni import ui
__all__: list = ['ConsoleWindow']
class ConsoleWindow(omni.ui._ui.Window):
    """
    The Console window
    
        This class represents a console window in the UI. It provides functionality for displaying and interacting with console output.
        
    """
    def __init__(self):
        """
        Initializes the ConsoleWindow class.
        """
    def _visibility_changed_fn(self, visible):
        ...
    def destroy(self):
        """
        Called by extension before destroying this object. It doesn't happen automatically.
                Without this, hot reloading doesn't work.
                
        """
    def set_visibility_changed_listener(self, listener):
        """
        Sets the listener for visibility changes.
        
                Args:
                    listener (function): Callback called when visibility changes.
                
        """
