from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.audiodeviceenum._audiodeviceenum import Direction
from omni.kit.audiodeviceenum._audiodeviceenum import SampleType
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni.kit.window.preferences.scripts.preferences_window import show_file_importer
from omni import ui
import os as os
import platform as platform
__all__ = ['AudioPreferences', 'Direction', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'SampleType', 'SettingType', 'carb', 'omni', 'os', 'partial', 'platform', 'show_file_importer', 'ui']
class AudioPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def _on_apply_button_fn(self):
        """
         Called when the user clicks on the 'Apply' button. 
        """
    def _on_browse_button_fn(self, origin):
        """
         Called when the user picks the Browse button. 
        """
    def _on_file_pick(self, full_path):
        """
         Called when the user accepts filename in the Select Filename dialog. 
        """
    def _on_refresh_button_fn(self):
        """
         Called when the user clicks on the 'Refresh' button. 
        """
    def build(self):
        ...
    def get_device_list(self, direction):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
