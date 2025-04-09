from __future__ import annotations
import carb as carb
from omni.kit.widget.settings.settings_widget import SettingType
import omni.kit.window.preferences.scripts.preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni.kit.window.preferences.scripts.preferences_window import show_file_importer
from omni import ui
import os as os
__all__: list = ['ScreenshotPreferences']
class ScreenshotPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def _add_ansel_settings(self):
        ...
    def _create_ansel_super_resolution_settings(self):
        ...
    def _is_ansel_enabled(self):
        ...
    def _on_browse_button_fn(self, owner):
        """
        Called when the user picks the Browse button.
        """
    def _on_dir_pick(self, real_path):
        """
        Called when the user accepts directory in the Select Directory dialog.
        """
    def build(self):
        """
        Capture Screenshot
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
