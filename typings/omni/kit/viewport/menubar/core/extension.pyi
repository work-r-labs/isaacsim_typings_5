from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer import ViewportMenuSpacer
from omni.kit.viewport.menubar.core.menu_item.viewport_menubar_item import ViewportMenubar
from omni.kit.viewport.menubar.core.preference.menubar_page import ViewportMenubarPage
from omni.kit.viewport.menubar.core.utils.usd_watch import start as usd_watch_start
from omni.kit.viewport.menubar.core.utils.usd_watch import stop as usd_watch_stop
from omni.kit.viewport.menubar.core.viewport_layer import MenuBarViewportLayer
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenubarItem
from omni.kit.viewport.menubar.core.viewport_menu_model import destroy as destroy_menu_model
from omni.kit.window.preferences.scripts.preferences_window import register_page
from omni.kit.window.preferences.scripts.preferences_window import unregister_page
__all__: list = ['ViewportMenuBarExtension']
class ViewportMenuBarExtension(omni.ext._extensions.IExt):
    """
    Manages the lifecycle of the viewport menu bar and its items.
    """
    def __init__(self):
        """
        Constructor
        """
    def get_menubar(self, name: str) -> typing.Optional[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenubarItem]:
        """
        
                Retrieve menu bar in viewport by name.
        
                Args:
                    name (str): Name of menu bar
                
        """
    def get_menubars(self) -> typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenubarItem]:
        """
        
                Retrieve all menu bars in viewport.
                
        """
    def init_shades(self):
        """
        Style colors
        """
    def on_shutdown(self):
        """
        Callback when extension shut down
        """
    def on_startup(self):
        """
        Callback when extension startup
        """
def get_instance() -> typing.Optional[omni.kit.viewport.menubar.core.extension.ViewportMenuBarExtension]:
    """
    
        Retrieves the singleton instance of the viewport menu bar core extension.
        
    """
DEFAULT_MENUBAR_NAME: str = '__DEFAULT__MENUBAR__'
_extension_instance: ViewportMenuBarExtension  # value = <omni.kit.viewport.menubar.core.extension.ViewportMenuBarExtension object>
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
fl: omni.ui.constant_utils.FloatShade  # value = <omni.ui.constant_utils.FloatShade object>
