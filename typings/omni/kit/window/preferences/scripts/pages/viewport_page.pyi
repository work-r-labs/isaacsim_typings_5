from __future__ import annotations
from omni.kit.widget.settings.settings_widget import SettingType
import omni.kit.window.preferences.scripts.preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
__all__ = ['PreferenceBuilder', 'SettingType', 'ViewportPreferences']
class ViewportPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def build(self):
        ...
    def show_page(self) -> bool:
        ...
