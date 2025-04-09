from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
__all__ = ['DatetimeFormatPreferences', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'carb', 'omni', 'partial']
class DatetimeFormatPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __del__(self):
        ...
    def __init__(self):
        ...
    def build(self):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
