from __future__ import annotations
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_item
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni import ui
__all__: list = ['ViewportMenuSeparator']
class ViewportMenuSeparator(omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem):
    """
    A simple separator in viewport menu bar
    """
    def build_fn(self, factory_args: typing.Dict):
        """
        
                Build a simple separator
        
                Args:
                    factory_args (dict): Argument related to viewport.
                
        """
