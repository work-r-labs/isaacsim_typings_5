from __future__ import annotations
import carb as carb
from isaacsim.core.version.extension import get_version
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.utils import add_menu_items
from omni.kit.menu.utils.utils import build_submenu_dict
from omni import ui
from pathlib import Path
__all__ = ['AboutExtension', 'DISCONNECTED', 'MenuItemDescription', 'Path', 'QUERYING', 'WINDOW_NAME', 'add_menu_items', 'build_submenu_dict', 'carb', 'get_instance', 'get_version', 'omni', 'ui']
class AboutExtension(omni.ext._extensions.IExt):
    @staticmethod
    def _resize_window(window: omni.ui._ui.Window, scrolling_frame: omni.ui._ui.ScrollingFrame):
        ...
    def _on_menu_show_about(self):
        ...
    def get_values(self):
        ...
    def menu_show_about(self, plugins):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_instance():
    ...
DISCONNECTED: str = '** disconnected **'
QUERYING: str = '** querying **'
WINDOW_NAME: str = 'About'
_extension_instance: AboutExtension  # value = <isaacsim.app.about.extension.AboutExtension object>
