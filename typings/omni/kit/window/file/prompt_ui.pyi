"""
A pop up window class to show while waiting operations to be done.
"""
from __future__ import annotations
import carb as carb
from omni import ui
import urllib as urllib
__all__ = ['Prompt', 'carb', 'ui', 'urllib']
class Prompt:
    """
    
        A pop up window in context manager style to perform operations when inside the context.
    
        Args:
            title (str): window title.
            text (str): decription of the operation to perform when in context.
            button_text (List[str]): text of buttons to create.
            button_fn (List[Callable]): functions to call after clicking buttons.
        Keyword Args:
            modal (bool): True to disable hang detection when in context.
            callback_addons (List[Callable]): callbacks to perform after initializing the window.
            callback_destroy (List[Callable]): callbacks to perform after destroying the window.
            decode_text (bool): unwrap quotes if set.
        
    """
    def __del__(self):
        ...
    def __enter__(self):
        ...
    def __exit__(self, type, value, trace):
        ...
    def __init__(self, title: str, text: str, button_text: typing.List[str], button_fn: typing.List[typing.Callable[[], NoneType]], modal: bool = False, callback_addons: typing.List[typing.Callable[[], NoneType]] = list(), callback_destroy: typing.List[typing.Callable[[], NoneType]] = list(), decode_text: bool = True):
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
    def set_text(self, text):
        """
         Set the operation description. 
        """
    def show(self):
        """
         Show the window. 
        """
