from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.material.library.pages.material_config_widget import EditableListWidget
from omni.kit.material.library.pages.material_path_widget import MdlCustomPathListWidget
from omni.kit.material.library.pages.material_path_widget import MdlDefaultPathListWidget
from omni.kit.material.library.pages.render_context_widget import RenderContextWidget
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
import os as os
__all__ = ['EditableListWidget', 'MaterialPreferences', 'MdlCustomPathListWidget', 'MdlDefaultPathListWidget', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'RenderContextWidget', 'SETTING_USERALLOWLIST', 'SETTING_USERBLOCKLIST', 'SettingType', 'asyncio', 'carb', 'omni', 'os', 'ui']
class MaterialPreferences(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    def __init__(self):
        ...
    def _isExtensionEnabled(self, name):
        ...
    def _show_message(self, msg: str, hide_after_timeout: bool = False):
        ...
    def build(self):
        """
         Material 
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
SETTING_USERALLOWLIST: str = '/materialConfig/materialGraph/userAllowList'
SETTING_USERBLOCKLIST: str = '/materialConfig/materialGraph/userBlockList'
