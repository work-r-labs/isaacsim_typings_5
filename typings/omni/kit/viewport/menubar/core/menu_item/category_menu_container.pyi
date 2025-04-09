from __future__ import annotations
from omni.kit.viewport.menubar.core.menu_item.category_menu_collection import CategoryMenuCollection
from omni.kit.viewport.menubar.core.menu_item.selectable_menu_item import SelectableMenuItem
import omni.kit.viewport.menubar.core.model.category_model
from omni.kit.viewport.menubar.core.model.category_model import CategoryCollectionItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCustomItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStateItem
from omni.kit.viewport.menubar.core.model.category_model import SimpleCategoryModel
__all__: list = ['CategoryMenuContainer']
class CategoryMenuContainer:
    """
    A menu container for category menu items.
    """
    def __init__(self, model: omni.kit.viewport.menubar.core.model.category_model.SimpleCategoryModel, identifier: typing.Optional[str] = None, trigger_fns: typing.Optional[typing.Dict[str, typing.Callable]] = None):
        """
        
                Constructor.
        
                Args:
                    model (SimpleCategoryModel): Category data model.
        
                Keyword Args:
                    identifier (Optional[str]): Widget identifier, defaults to None.
                    trigger_fns (Optional[Dict[str, Callable]]): Callbacks when menu item clicked, defaults to None.
                
        """
    def build(self, trigger_fns: typing.Optional[typing.Dict[str, typing.Callable]] = None):
        """
        
                Build category menu items.
        
                Keyword Args:
                    trigger_fns (Optional[Dict[str, Callable]]): Callbacks when menu item clicked by item text, defaults to None
                
        """
