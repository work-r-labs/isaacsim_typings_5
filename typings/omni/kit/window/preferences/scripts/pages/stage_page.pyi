from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
__all__ = ['PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'SettingType', 'StagePreferences', 'carb', 'omni', 'partial']
class StagePreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _create_prim_creation_settings_widgets(self):
        ...
    def _setup_time_code_range_constraint(self, model):
        ...
    def _update_prim_creation_with_default_xform_ops(self):
        ...
    def build(self):
        ...
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
