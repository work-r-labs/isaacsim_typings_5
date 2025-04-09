from __future__ import annotations
import omni.kit.widget.path_field.model
from omni.kit.widget.path_field.model import PathFieldModel
from omni import ui
import os as os
import platform as platform
import sys as sys
__all__ = ['PathField', 'PathFieldModel', 'UI_STYLES', 'os', 'platform', 'sys', 'ui']
class PathField:
    """
    
        Main class for the PathField widget. This widget is a UI alternative to omni.ui.StringField
        for navigating tree views with the keyboard. As the user navigates the tree using TAB,
        Backspace, and Arrow keys, they are constantly provided branching options via auto-filtered
        tooltips.
    
        Args:
            None
    
        Keyword Args:
            apply_path_handler (Callable): This function is called when the user hits Enter on the input
                field, signaling that they want to apply the path. This handler is expected to update
                the caller's app accordingly. Function signature: void apply_path_handler(path: str)
            branching_options_handler (Callable): This function is required to provide a list of possible
                branches whenever prompted with a path.  For example, if path = "C:", then the list of values
                produced might be ["Program Files", "temp", ..., "Users"]. Function signature:
                list(str) branching_options_provider(path: str, callback: func)
            separator (str): Character used to split a path into list of branches. Default '/'.
            modal (bool): Used for modal window. Default False.
            begin_edit_handler (callable): A callback for path string field begin edit. Default None.
    
        
    """
    def __init__(self, **kwargs):
        """
        Constructor for the PathField class.
        """
    def _build_input_field(self):
        ...
    def _build_ui(self):
        ...
    def _on_begin_edit(self, model: omni.kit.widget.path_field.model.PathFieldModel):
        ...
    def _parse_path(self, full_path: str):
        ...
    def _update_breadcrumbs(self, path: str):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def set_path(self, full_path: str):
        """
        Sets the path.
        
                Args:
                    full_path (str): The full path name to set.
        """
    @property
    def path(self) -> str:
        """
        Gets the current path as entered in the field box.
        
                Returns:
                    str: The current path.
        """
UI_STYLES: dict  # value = {'NvidiaLight': {'Window': {'secondary_background_color': 0}, 'ScrollingFrame': {'background_color': 4283650900, 'margin': 0, 'padding': 0}, 'Rectangle': {'background_color': 4283650900}, 'InputField': {'background_color': 4283650900, 'color': 4292269782, 'padding': 0}, 'BreadCrumb': {'background_color': 0, 'padding': 0}, 'BreadCrumb.Label': {'color': 4292269782}, 'BreadCrumb:hovered': {'background_color': 4291808447}, 'BreadCrumb.Label:hovered': {'color': 4280952869}, 'BreadCrumb:selected': {'background_color': 4283650900}, 'Tooltips.Menu': {'background_color': 4292927712, 'border_color': 4292927712, 'border_width': 0.5}, 'Tooltips.Item': {'background_color': 4283650900, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4285427310}, 'Tooltips.Item:checked': {'background_color': 4285427310}, 'Tooltips.Item.Label': {'color': 4292269782, 'alignment': <Alignment.LEFT: 2>}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0}}, 'NvidiaDark': {'Window': {'secondary_background_color': 0}, 'ScrollingFrame': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'InputField': {'background_color': 0, 'color': 4288585374, 'padding': 0, 'margin': 0}, 'BreadCrumb': {'background_color': 0, 'padding': 0}, 'BreadCrumb:hovered': {'background_color': 4287268727}, 'BreadCrumb:selected': {'background_color': 4287268727}, 'BreadCrumb.Label': {'color': 4288585374}, 'BreadCrumb.Label:hovered': {'color': 4280952869}, 'Tooltips.Menu': {'background_color': 3710066975, 'border_color': 2861205367, 'border_width': 0.5}, 'Tooltips.Item': {'background_color': 0, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4287268727}, 'Tooltips.Item:checked': {'background_color': 4287268727}, 'Tooltips.Item.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT: 2>}, 'Tooltips.Item.Label:hovered': {'color': 4280952869}, 'Tooltips.Item.Label:checked': {'color': 4280952869}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0, 'margin': 0}}}
