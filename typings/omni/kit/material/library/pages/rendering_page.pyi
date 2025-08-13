from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
from typing import Any
__all__: list[str] = ['Any', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'RenderingPreferences', 'SettingType', 'carb', 'omni', 'ui']
class RenderingPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def build(self):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
