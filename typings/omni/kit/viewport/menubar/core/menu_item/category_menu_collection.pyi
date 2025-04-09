from __future__ import annotations
from omni.kit.viewport.menubar.core.delegate.category_menu_delegate import CategoryMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.menu_item.selectable_menu_item import SelectableMenuItem
import omni.kit.viewport.menubar.core.model.category_model
from omni.kit.viewport.menubar.core.model.category_model import CategoryCollectionItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCustomItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStateItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStatus
from omni.kit.viewport.menubar.core.model.category_model import SimpleCategoryModel
from omni.kit.viewport.menubar.core.utils import menu_is_tearable
from omni import ui
import omni.ui._ui
__all__: list = ['CategoryMenuCollection']
class CategoryMenuCollection(omni.ui._ui.MenuItemCollection):
    """
    A menu collection for category items.
    """
    def __init__(self, model: omni.kit.viewport.menubar.core.model.category_model.SimpleCategoryModel, item: omni.kit.viewport.menubar.core.model.category_model.CategoryCollectionItem, identifier: typing.Optional[str] = None, trigger_fns: typing.Optional[typing.Dict[str, typing.Callable]] = None):
        """
        
                Constructor:
        
                Args:
                    model (SimpleCategoryModel): Category data model.
                    item (CategoryCollectionItem): Root category item in category model.
        
                Keyword Args:
                    identifier (Optional[str]): Menu collection identifier, defaults to None.
                    trigger_fns (Optional[Dict[str, Callable]]): Callbacks when menu item clicked, defaults to None.
                
        """
    def _build_menu_items(self):
        ...
    def _on_icon_clicked(self, x, y, button, modifiers) -> None:
        ...
    def _on_status_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def destroy(self) -> None:
        """
        Release resources.
        """
