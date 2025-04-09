"""

preference window class
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import IntFlag
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilderUI
from omni.kit.window.preferences.scripts.preferences_actions import deregister_actions
from omni.kit.window.preferences.scripts.preferences_actions import register_actions
import typing
__all__: list = ['PreferenceBuilder', 'PreferenceBuilderUI', 'register_actions', 'deregister_actions', 'PERSISTENT_SETTINGS_PREFIX', 'DEVELOPER_PREFERENCE_PATH', 'GLOBAL_PREFERENCES_PATH', 'RENDERING_PREFERENCES_PATH', 'PreferencesExtension', 'get_instance', 'show_preferences_window', 'hide_preferences_window', 'get_page_list', 'get_shown_page_list', 'register_page', 'select_page', 'rebuild_pages', 'unregister_page', 'show_file_importer']
class PreferencesExtension(omni.ext._extensions.IExt):
    """
    
        Preference window class.
        
    """
    class PreferencesState(enum.IntFlag):
        """
        
                Preference startup state, either Invalid or Created.
                
        """
        Created: typing.ClassVar[PreferencesExtension.PreferencesState]  # value = <PreferencesState.Created: 1>
        Invalid: typing.ClassVar[PreferencesExtension.PreferencesState]  # value = <PreferencesState.Invalid: 0>
    def _create_menu(self):
        ...
    def _on_developer_preference_section_changed(self, item, event_type):
        ...
    def _on_visibility_changed_fn(self, visible):
        ...
    def _rebuild_after_loading(self, event):
        ...
    def _refresh_menu_async(self):
        ...
    def _register_pages(self):
        ...
    def _register_resourcemonitor_preferences(self):
        ...
    def _remove_menu(self):
        ...
    def _toggle_preferences_window(self):
        ...
    def _unregister_resourcemonitor_preferences(self):
        ...
    def hide_preferences_window(self):
        """
        Hide the Preferences window from the User.
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def rebuild_pages(self):
        """
        
                Rebuild UI.
                
        """
    def select_page(self, page):
        """
        
                Select page to display and refresh.
                
        """
    def show_preferences_window(self):
        """
        Show the Preferences window to the User.
        """
def get_instance():
    """
    
        Get instance of preference window class.
        
    """
def get_page_list():
    """
    
        Get list of all available pages.
        
    """
def get_shown_page_list():
    """
    
        Gets list of pages that are visible. IE list of pages that PreferenceBuilder.show_page() returned True.
        
    """
def hide_preferences_window():
    """
    
        Hide the Preferences window from the User.
        
    """
def rebuild_pages():
    """
    
        rebuild UI
        
    """
def register_page(page):
    """
    
        Add new custom page to preference window list.
        
    """
def select_page(page):
    """
    
        Select page to display and refresh.
        
    """
def show_file_importer(title: str, file_exts: list = [('All Files(*)', '')], filename_url: str = None, click_apply_fn: typing.Callable = None, show_only_folders: bool = False):
    """
    
        Shows file importer.
        
    """
def show_preferences_window():
    """
    
        Show the Preferences window to the User.
        
    """
def unregister_page(page, rebuild: bool = True):
    """
    
        Remove custom page from preference window list.
        
    """
DEVELOPER_PREFERENCE_PATH: str = '/app/show_developer_preference_section'
GLOBAL_PREFERENCES_PATH: str = '/exts/omni.kit.window.preferences/show_globals'
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
RENDERING_PREFERENCES_PATH: str = '/exts/omni.kit.window.preferences/show_rendering'
_extension_instance: PreferencesExtension  # value = <omni.kit.window.preferences.scripts.preferences_window.PreferencesExtension object>
_preferences_page_list: list  # value = [<omni.kit.window.preferences.scripts.pages.globals.GlobalPreferences object>, <omni.kit.audiodeviceenum.audio_page.AudioPreferences object>, <isaacsim.gui.menu.edit_menu.screenshot_page.ScreenshotPreferences object>, <omni.kit.window.preferences.scripts.pages.datetime_format_page.DatetimeFormatPreferences object>, <omni.kit.window.preferences.scripts.pages.developer_page.DeveloperPreferences object>, <omni.ui.pages_developer.DeveloperPreferences object>, <omni.kit.material.library.pages.material_page.MaterialPreferences object>, <omni.metrics.assembler.ui.settings.MetricsAssemblerPreferences object>, <omni.physxui.scripts.settings.PhysicsPreferences object>, <omni.kit.property.usd.property_preferences_page.PropertyUsdPreferences object>, <omni.kit.window.preferences.scripts.pages.rendering_page.RenderingPreferences object>, <omni.kit.material.library.pages.rendering_page.RenderingPreferences object>, <omni.resourcemonitor.scripts.resourcemonitor_page.ResourceMonitorPreferences object>, <omni.kit.window.preferences.scripts.pages.stage_page.StagePreferences object>, <omni.kit.stage_templates.stage_templates_page.StageTemplatesPreferences object>, <omni.kit.window.preferences.scripts.pages.viewport_page.ViewportPreferences object>, <omni.kit.viewport.menubar.core.preference.menubar_page.ViewportMenubarPage object>]
