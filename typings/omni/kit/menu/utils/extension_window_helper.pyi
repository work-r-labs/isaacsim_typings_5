"""

Simple helper class for adding/removing "Window" menu to your extension. ui.Window creation/show/hide is still down to user to provide functionally.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni import ui
__all__: list[str] = ['MenuHelperExtension', 'MenuItemDescription', 'carb', 'omni', 'registered_windows', 'ui']
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
    def _MenuHelperExtension__register_window(self, window_name):
        ...
    def _MenuHelperExtension__unregister_window(self, window_name):
        ...
    def __init__(self):
        ...
    def menu_refresh(self):
        ...
    def menu_shutdown(self) -> bool:
        ...
    def menu_startup(self, window_name, menu_desc, menu_group, appear_after = '', header = None, verbose = False) -> bool:
        ...
registered_windows: dict = {'Property': 'unknown', 'Content': 'unknown', 'Stage': 'unknown', 'Extensions': 'unknown', 'Console': 'unknown', 'Render Settings': 'unknown', 'Main ToolBar': 'unknown'}
