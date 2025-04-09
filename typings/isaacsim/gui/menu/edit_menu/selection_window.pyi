"""
This module provides a SelectionSetWindow class for creating a new selection set with a user-defined name through a UI window.
"""
from __future__ import annotations
from omni import ui
__all__: list = ['SelectionSetWindow']
class SelectionSetWindow:
    """
    A window to input and create a new selection set name.
    
        This class provides a UI window that allows users to enter a name for a new selection set and create it using a callback function. The window includes a label, a text field, and 'Create' and 'Cancel' buttons.
    
        Args:
            callback (Callable[[str], None]): Function to call with the new selection set name.
    """
    def __init__(self, callback):
        """
        Initializes the SelectionSetWindow with a callback to be triggered upon creation.
        """
    def show(self):
        """
        Shows the SelectionSetWindow and resets the input field.
        """
    def shutdown(self):
        """
        Shuts down the SelectionSetWindow and cleans up resources.
        """
