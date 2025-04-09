from __future__ import annotations
from omni.kit.viewport.menubar.settings.menu_item.custom_resolution.custom_resolution_delegate import CustomResolutionDelegate
from omni import ui
import omni.ui._ui
__all__ = ['CustomResolutionDelegate', 'CustomResolutionMenuItem', 'ui']
class CustomResolutionMenuItem(omni.ui._ui.MenuItem):
    """
    
        Menu item to edit/save custom resolution.
        
    """
    resolution: typing.Tuple[int, int]
    def __init__(self, res_model, res_setter):
        ...
    def destroy(self):
        ...
