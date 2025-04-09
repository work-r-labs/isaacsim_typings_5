"""
 Dialog class for saving stage. 
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
import typing
import urllib as urllib
import weakref as weakref
__all__: list = ['StageSaveDialog']
class StageSaveDialog:
    """
    
        Dialog class for saving stage.
    
        Keyword Args:
            on_save_fn (Callable): function to call when clicking 'Save Selected' button.
            on_dont_save_fn (Callable): function to call when clicking 'Don't Save' button.
            on_cancel_fn (Callable): function to call when clicking cancel button.
            enable_dont_save (bool): Disable 'Don't Save' button.
        
    """
    _MAX_VISIBLE_LAYER_COUNT: typing.ClassVar[int] = 10
    _WINDOW_WIDTH: typing.ClassVar[int] = 580
    def __del__(self):
        ...
    def __init__(self, on_save_fn: typing.Optional[typing.Callable[[], NoneType]] = None, on_dont_save_fn: typing.Optional[typing.Callable[[], NoneType]] = None, on_cancel_fn: typing.Optional[typing.Callable[[], NoneType]] = None, enable_dont_save = False):
        ...
    def _check_and_select_all(self, select_all_check_box):
        ...
    def _check_checkpoint_enabled(self, url):
        ...
    def _on_cancel_fn(self):
        ...
    def _on_checkbox_fn(self, model, check_box_index, select_all_check_box):
        ...
    def _on_description_begin_edit(self, model):
        ...
    def _on_description_end_edit(self, model):
        ...
    def _on_dont_save_fn(self):
        ...
    def _on_save_fn(self):
        ...
    def _on_select_all_fn(self, model):
        ...
    def destroy(self):
        """
         Destructor. 
        """
    def is_visible(self):
        """
        
                Return:
                    Return True if dialog is visible.
                
        """
    def show(self, layer_identifiers: typing.List[str] = list()):
        """
        
                Show the dialog.
                Keyword Args:
                    layer_identifiers(List[str]): list of layer identifier URLs.
                
        """
class _CheckBoxStatus:
    def __init__(self, checkbox, layer_identifier, layer_is_writable):
        ...
have_versioning: bool = False
