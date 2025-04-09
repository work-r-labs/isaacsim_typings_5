from __future__ import annotations
import carb as carb
import omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
import omni.kit.viewport.menubar.core.model.category_model
from omni.kit.viewport.menubar.core.model.category_model import CategoryStatus
from omni import ui
import omni.ui._ui
__all__: list = ['CategoryMenuDelegate']
class CategoryMenuDelegate(omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate.ViewportMenuDelegate):
    """
    
        A menu delegate that show icon for category status within a viewport menubar.
        
    """
    def __init__(self, status: omni.kit.viewport.menubar.core.model.category_model.CategoryStatus, icon_clicked_fn: typing.Callable[[NoneType], NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    status (CategoryStatus): Current category status.
                    icon_clicked_fn (Callable[[None], None]): Callback when icon clicked, defaults to None.
                
        """
    def _on_icon_hovered(self, hovered) -> None:
        ...
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Build icon for category status.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    @property
    def status(self) -> omni.kit.viewport.menubar.core.model.category_model.CategoryStatus:
        """
        Category status
        """
    @status.setter
    def status(self, value: omni.kit.viewport.menubar.core.model.category_model.CategoryStatus) -> None:
        ...
