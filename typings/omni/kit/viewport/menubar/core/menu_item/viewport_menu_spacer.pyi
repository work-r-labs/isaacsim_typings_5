from __future__ import annotations
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_item
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni import ui
__all__: list = ['ViewportMenuSpacer']
class ViewportMenuSpacer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem):
    """
    A simple spacer in viewport menu bar
    """
    def __init__(self):
        """
        Constructor
        """
    def build_fn(self, factory_args: typing.Dict):
        """
        
                BUild a simple spacer.
        
                Args:
                    factory_args (dict): Argument related to viewport.
                
        """
    def get_computed_width(self, factory_args: typing.Dict) -> float:
        """
        Retrieve the spacer computed width
        """
