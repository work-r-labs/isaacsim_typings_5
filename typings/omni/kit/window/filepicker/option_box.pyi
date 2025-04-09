from __future__ import annotations
from omni.kit.window.filepicker.style import get_style
from omni import ui
__all__: list = ['OptionBox']
class OptionBox:
    @staticmethod
    def create_option_box(build_fn: typing.Callable) -> OptionBox:
        """
        
                 Create and return OptionBox widget. 
        
                 Args:
                      build_fn (Callable): Function that used to build the real part.
                        Function signature: void build_fn(list[str])
                 
                 Returns: 
                      An instance of  OptionBox.
                
        """
    @staticmethod
    def delete_option_box(widget: OptionBox):
        """
        
                 Delete option box and its contents.
                 
                 Args:
                      widget (:obj: 'OptionBox'): The widget to be delete.
                
        """
    @staticmethod
    def on_selection_changed(widget: OptionBox, selected: typing.List[str]):
        """
        
                 Rebuild option box when selection changes. 
                 
                 Args:
                      widget (:obj: 'OptionBox'): the widget that emitted the signal. 
                      selected (List[str]): the list of selected filepath
                
        """
    def __init__(self, build_fn: typing.Callable, **kwargs):
        """
        
                 A helper class to initialize the OptionBox.
                 
                 Args:
                      build_fn (Callable): Function that build real part in frame.
                        Function signature: void build_fn(list[str])
                
        """
    def _build_ui(self):
        ...
    def destroy(self):
        """
         Destroy the widget. 
        """
    def rebuild(self, selected: typing.List[str]):
        """
        
                 Clear and rebuild the frame. 
                 
                 Args:
                      selected (List[str]): List of filepath to show in option box.
                
        """
