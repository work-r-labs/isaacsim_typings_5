"""
 Prompt window class to show when opening a read only file. 
"""
from __future__ import annotations
from omni import ui
__all__: list = ['ReadOnlyOptionsWindow']
class ReadOnlyOptionsWindow:
    """
    
        Prompt window class to show when opening a read only file.
    
        Args:
            open_with_new_edit_fn (Callable): function to call when opening with a new edit layer.
            open_original_fn (Callable): function to call when opening original file.
        Keyword Args:
            modal (bool): True if window is modal.
        
    """
    def __init__(self, open_with_new_edit_fn: typing.Callable[[], NoneType], open_original_fn: typing.Callable[[], NoneType], modal = False):
        ...
    def _build_ui(self):
        ...
    def destroy(self):
        """
         Destructor. 
        """
    def hide(self):
        """
         Hide the window. 
        """
    def is_visible(self):
        """
        
                Return:
                    Return True if window is visible.
                
        """
    def show(self):
        """
         Show the window. 
        """
ICON_PATH: str = '${omni.kit.window.file}/icons'
