from __future__ import annotations
import carb as carb
from omni.kit.widget.settings.settings_widget import SettingType
import omni.kit.window.preferences.scripts.preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
__all__: list[str] = ['PreferenceBuilder', 'SettingType', 'ViewportPreferences', 'carb']
class ViewportPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def _ViewportPreferences__on_change_picking_occluded(self, item, event_type):
        ...
    def __del__(self):
        ...
    def __init__(self):
        ...
    def build(self):
        ...
    def show_page(self) -> bool:
        ...
