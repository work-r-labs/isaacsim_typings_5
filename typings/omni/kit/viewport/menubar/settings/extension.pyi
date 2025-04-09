from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.settings.setting_menu_container import SettingMenuContainer
__all__: list = ['ViewportSettingsMenuBarExtension']
class ViewportSettingsMenuBarExtension(omni.ext._extensions.IExt):
    """
    The Entry Point for the Viewport Settings in Viewport Menu Bar
    """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
