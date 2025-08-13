from __future__ import annotations
from omni.kit.widget.settings.settings_widget import SettingType
import omni.kit.window.preferences.scripts.preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
__all__: list = ['PropertyUsdPreferences']
class PropertyUsdPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    """
    A class to build the property preferences page.
    """
    def __init__(self):
        ...
    def build(self):
        """
        Builds the property preferences page.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
