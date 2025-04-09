from __future__ import annotations
import carb as carb
from omni.kit.widget.toolbar.builtin_tools.play_button_group import PlayButtonGroup
from omni.kit.widget.toolbar.builtin_tools.select_button_group import SelectButtonGroup
from omni.kit.widget.toolbar.builtin_tools.snap_button_group import LegacySnapButtonGroup
from omni.kit.widget.toolbar.builtin_tools.transform_button_group import TransformButtonGroup
import typing as typing
__all__: list = ['BuiltinTools']
class BuiltinTools:
    def __del__(self):
        ...
    def __init__(self, toolbar: Toolbar):
        ...
    def _add_snap_button(self):
        ...
    def _on_legacy_snap_setting_changed(self, *args, **kwargs):
        ...
    def _on_legacy_snap_setting_changed_window(self, *args, **kwargs):
        """
        
                If the old setting is set, we forward it into the new settings.
                
        """
    def _remove_snap_button(self):
        ...
    def add_custom_move_type(self, entry_name: str, move_type: str):
        ...
    def add_custom_select_type(self, entry_name: str, selection_types: list):
        ...
    def destroy(self):
        ...
    def remove_custom_move(self, entry_name: str):
        ...
    def remove_custom_select(self, entry_name):
        ...
LEGACY_SNAP_BUTTON_ENABLED_SETTING_PATH_WIDGET: str = '/exts/omni.kit.widget.toolbar/legacySnapButton/enabled'
LEGACY_SNAP_BUTTON_ENABLED_SETTING_PATH_WINDOW: str = '/exts/omni.kit.window.toolbar/legacySnapButton/enabled'
PLAY_BUTTON_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/PlayButton/enabled'
SELECT_BUTTON_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/SelectionButton/enabled'
TRANSFORM_BUTTON_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/TransformButton/enabled'
