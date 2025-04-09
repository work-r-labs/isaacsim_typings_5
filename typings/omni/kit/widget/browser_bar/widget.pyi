"""
This module defines the BrowserBar class, which extends the PathField UI widget with navigation history and branching options for directory browsing.
"""
from __future__ import annotations
from omni.kit.widget.browser_bar.model import StringQueueModel
from omni.kit.widget.browser_bar.model import VisitedHistory
from omni.kit.widget.path_field.widget import PathField
from omni import ui
import omni.ui._ui
import os as os
import pathlib
import sys as sys
__all__ = ['BrowserBar', 'ICON_PATH', 'PathField', 'StringQueueModel', 'UI_STYLES', 'VisitedHistory', 'os', 'sys', 'ui']
class BrowserBar:
    """
    A class that extends the :obj:`PathField` UI widget for navigating tree views via
        the keyboard by adding navigation history, similar to modern-day browsers. This allows users
        to directly jump to any previously visited path.
    
        Keyword Args:
            visited_history_size (int): Maximum number of previously visited paths to queue up. Default is 10.
            apply_path_handler (Callable): Function called when the user updates the path, expected to
                update the caller app accordingly. The path can be updated by hitting Enter on the
                input field, selecting a path from the dropdown, or clicking on the "prev" or "next"
                buttons. Function signature: void apply_path_handler(path: str).
            branching_options_handler (Callable): Function required to provide a list of possible branches
                whenever prompted with a path. For example, if path = "C:", the list of values might be
                ["Program Files", "temp", ..., "Users"]. Function signature: list(str)
                branching_options_handler(path: str, callback: func).
            modal (bool): Indicates if this is used for a modal window. Default is False.
    """
    def __init__(self, **kwargs):
        """
        Initializes the BrowserBar with optional UI customization parameters.
        """
    def _build_ui(self):
        ...
    def _build_visited_menu(self):
        ...
    def _on_menu_item_selected(self, model: omni.ui._ui.SimpleIntModel):
        ...
    def _on_next_button_pressed(self):
        ...
    def _on_prev_button_pressed(self):
        ...
    def _update_nav_buttons(self):
        ...
    def _update_visited(self, path: str):
        ...
    def destroy(self):
        """
        Cleans up the BrowserBar, destroying UI components and clearing memory.
        """
    def set_path(self, path: str):
        """
        Sets the path and adds it to the history queue.
        
                Args:
                    path (str): The full path name.
        """
    @property
    def path(self) -> str:
        """
        Gets the current path as entered in the field box.
        
                Returns:
                    str: The current path if available, otherwise None.
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.browser_bar-2.0.10+d02c707b/icons')
UI_STYLES: dict = {'NvidiaLight': {'Rectangle': {'background_color': 4283650900}, 'Button': {'background_color': 4292927712, 'margin': 4, 'padding': 0, 'border_width': 0}, 'Button:hovered': {'background_color': 4289506479}, 'Button:selected': {'background_color': 4289506479}, 'Button:disabled': {'background_color': 4292927712}, 'Button.Image': {'color': 4285427310}, 'Button.Image:disabled': {'color': 0}, 'ComboBox': {'background_color': 4283650900, 'selected_color': 4289506479, 'color': 4292269782}, 'ComboBox:hovered': {'background_color': 4289506479}, 'ComboBox:selected': {'background_color': 4289506479}}, 'NvidiaDark': {'Rectangle': {'background_color': 4280492319}, 'Button': {'background_color': 0, 'margin': 4, 'padding': 0}, 'Button:disabled': {'background_color': 0}, 'Button.Image': {'color': 4294967295}, 'Button.Image:disabled': {'color': 4287137928}, 'ComboBox': {'background_color': 4280492319, 'selected_color': 0, 'color': 4283058762, 'border_radius': 0, 'margin': 0, 'padding': 4, 'secondary_color': 4280492319}, 'ComboBox.Active': {'background_color': 4280492319, 'selected_color': 4282006074, 'color': 4288585374, 'border_radius': 0, 'margin': 0, 'padding': 4, 'secondary_selected_color': 4288585374, 'secondary_color': 4280492319}, 'ComboBox.Active:hovered': {'color': 4283058762, 'secondary_color': 0}, 'ComboBox.Active:pressed': {'color': 4283058762, 'secondary_color': 0}, 'ComboBox.Bg': {'background_color': 0, 'margin': 0, 'padding': 2}, 'ComboBox.Bg.Active': {'background_color': 0, 'margin': 0, 'padding': 2}, 'ComboBox.Bg.Active:hovered': {'background_color': 4285427310}, 'ComboBox.Bg.Active:pressed': {'background_color': 4285427310}}}
