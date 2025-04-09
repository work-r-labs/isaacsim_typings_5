from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni.kit.window.preferences.scripts.preferences_window import show_file_importer
from omni import ui
import os as os
import re as re
__all__ = ['PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'SettingType', 'StageTemplatesPreferences', 'carb', 'omni', 'os', 'partial', 're', 'show_file_importer', 'ui']
class StageTemplatesPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def _on_browse_button_fn(self, path, index, widget):
        """
         Called when the user picks the Browse button. 
        """
    def _on_file_pick(self, full_path, index, widget):
        """
         Called when the user accepts directory in the Select Directory dialog. 
        """
    def build(self):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
