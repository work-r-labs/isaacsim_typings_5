from __future__ import annotations
import carb as carb
from isaacsim.asset.browser.window import AssetBrowserWindow
import omni as omni
from omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex import TreeFolderBrowserWidgetEx
from omni import ui
__all__ = ['AssetBrowserExtension', 'AssetBrowserWindow', 'BROWSER_MENU_ROOT', 'EXTENSION_NAME', 'SETTING_ROOT', 'SETTING_VISIBLE_AFTER_STARTUP', 'TreeFolderBrowserWidgetEx', 'carb', 'get_instance', 'omni', 'ui']
class AssetBrowserExtension(omni.ext._extensions.IExt):
    def _is_visible(self):
        ...
    def _on_visibility_changed(self, visible):
        ...
    def _register_menuitem(self):
        ...
    def _show_window(self, visible) -> None:
        ...
    def _toggle_window(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    @property
    def browser_widget(self) -> typing.Optional[omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex.TreeFolderBrowserWidgetEx]:
        ...
    @property
    def window(self) -> typing.Optional[isaacsim.asset.browser.window.AssetBrowserWindow]:
        ...
def get_instance():
    ...
BROWSER_MENU_ROOT: str = 'Window'
EXTENSION_NAME: str = 'Isaac Sim Asset Browser'
SETTING_ROOT: str = '/exts/isaacsim.asset.browser/'
SETTING_VISIBLE_AFTER_STARTUP: str = '/exts/isaacsim.asset.browser/visible_after_startup'
_extension_instance: AssetBrowserExtension  # value = <isaacsim.asset.browser.extension.AssetBrowserExtension object>
