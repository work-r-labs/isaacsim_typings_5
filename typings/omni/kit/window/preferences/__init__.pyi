"""

Preference window classes.
"""
from __future__ import annotations
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts import preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilderUI
from omni.kit.window.preferences.scripts import preferences_actions
from omni.kit.window.preferences.scripts.preferences_actions import deregister_actions
from omni.kit.window.preferences.scripts.preferences_actions import register_actions
from omni.kit.window.preferences.scripts import preferences_window
from omni.kit.window.preferences.scripts.preferences_window import PreferencesExtension
from omni.kit.window.preferences.scripts.preferences_window import get_instance
from omni.kit.window.preferences.scripts.preferences_window import get_page_list
from omni.kit.window.preferences.scripts.preferences_window import get_shown_page_list
from omni.kit.window.preferences.scripts.preferences_window import hide_preferences_window
from omni.kit.window.preferences.scripts.preferences_window import rebuild_pages
from omni.kit.window.preferences.scripts.preferences_window import register_page
from omni.kit.window.preferences.scripts.preferences_window import select_page
from omni.kit.window.preferences.scripts.preferences_window import show_file_importer
from omni.kit.window.preferences.scripts.preferences_window import show_preferences_window
from omni.kit.window.preferences.scripts.preferences_window import unregister_page
from . import scripts
__all__ = ['DEVELOPER_PREFERENCE_PATH', 'GLOBAL_PREFERENCES_PATH', 'PERSISTENT_SETTINGS_PREFIX', 'PreferenceBuilder', 'PreferenceBuilderUI', 'PreferencesExtension', 'RENDERING_PREFERENCES_PATH', 'SettingType', 'deregister_actions', 'get_instance', 'get_page_list', 'get_shown_page_list', 'hide_preferences_window', 'preference_builder', 'preferences_actions', 'preferences_window', 'rebuild_pages', 'register_actions', 'register_page', 'scripts', 'select_page', 'show_file_importer', 'show_preferences_window', 'unregister_page']
DEVELOPER_PREFERENCE_PATH: str = '/app/show_developer_preference_section'
GLOBAL_PREFERENCES_PATH: str = '/exts/omni.kit.window.preferences/show_globals'
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
RENDERING_PREFERENCES_PATH: str = '/exts/omni.kit.window.preferences/show_rendering'
