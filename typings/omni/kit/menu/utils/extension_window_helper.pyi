"""

Simple helper class for adding/removing "Window" menu to your extension. ui.Window creation/show/hide is still down to user to provide functionally.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni import ui
__all__ = ['MenuHelperExtension', 'MenuItemDescription', 'carb', 'omni', 'ui']
class MenuHelperExtension:
    """
    
        Simple helper class for adding/removing "Window" menu to your extension. ui.Window creation/show/hide is still down to user to provide functionally.
        
    """
    @staticmethod
    def _is_visible(verbose, window_name) -> bool:
        ...
    @staticmethod
    def _toggle_window(verbose, window_name):
        ...
    def _MenuHelperExtension__get_action_name(self, menu_path):
        ...
    def __init__(self):
        ...
    def menu_refresh(self):
        ...
    def menu_shutdown(self):
        ...
    def menu_startup(self, window_name, menu_desc, menu_group, appear_after = '', header = None, verbose = False) -> bool:
        ...
