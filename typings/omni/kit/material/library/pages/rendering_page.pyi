from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
__all__ = ['PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'RenderingPreferences', 'SettingType', 'carb', 'omni', 'ui']
class RenderingPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def build(self):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
