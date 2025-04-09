from __future__ import annotations
from omni.kit.viewport.menubar.core.model.setting_model import SettingModel
from omni import ui
import omni.ui._ui
import typing
__all__: list = ['CategoryStatus', 'BaseCategoryItem', 'CategoryStateItem', 'CategoryCustomItem', 'CategoryCollectionItem', 'SimpleCategoryModel']
class BaseCategoryItem(omni.ui._ui.AbstractItem):
    """
    
        Base category item.
        
    """
    def __init__(self, text: str):
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
                
        """
class CategoryCollectionItem(BaseCategoryItem):
    """
    Collection category item. It could includes a set of other category items.
    
        This item has 3 different states:
            CategoryStatus.ALL: All child items checked.
            CategoryStatus.EMPTY: None child items checked.
            CategoryStatus.MIXED: Some child items checked while others not.
        
    """
    def __init__(self, text: str, items: typing.Optional[typing.List[omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem]] = None, shown_changed_fn: typing.Callable = None):
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
        
                Keyword Args:
                    items (Optional[List[BaseCategoryItem]]): List of child items, defaults to None.
                    shown_changed_fn (Callable): Callback when item visibility changed, defaults to None.
                
        """
    def _on_child_changed(self, model: omni.ui._ui.SimpleStringModel):
        ...
    def _on_status_changed(self, model: omni.ui._ui.SimpleStringModel):
        ...
    def add_item(self, item: BaseCategoryItem):
        """
        
                Append child item.
        
                Args:
                    item (BaseCategoryItem): Item to add as child.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    @property
    def status(self) -> CategoryStatus:
        """
        Category status
        """
    @status.setter
    def status(self, value: CategoryStatus) -> None:
        ...
class CategoryCustomItem(BaseCategoryItem):
    """
    A data item for user-defined category.
    """
    def __init__(self, text: str, build_fn: typing.Callable[[NoneType], NoneType]):
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
        
                Keyword Args:
                    build_fn (Callable[[None], None]): Callback function to create menu item.
                
        """
class CategoryStateItem(BaseCategoryItem):
    """
    A data item for category state (checked/unchecked)
    """
    def __init__(self, text: str, value_model: omni.ui._ui.SimpleBoolModel = None, setting_path: typing.Optional[str] = None, hotkey_text: str = '', show_hotkey_placeholder: bool = False):
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
                Keyword Args:
                    value_model (ui.SimpleBoolModel): Value model for item state, defaults to None.
                    setting_path (str): Setting path for item state, defaults to None.
                    hotkey_text (str): Hotkey text show in menu item, defaults to "".
                    show_hotkey_placeholder (bool): Show placeholder for hotkey text, defaults to False. Used to align with other menu items which have hotkeys.
                
        """
    @property
    def checked(self) -> bool:
        """
        Item checked state
        """
    @checked.setter
    def checked(self, value: bool) -> None:
        ...
class CategoryStatus:
    """
    Status for a category menu
    """
    ALL: typing.ClassVar[str] = 'Category.All'
    EMPTY: typing.ClassVar[str] = 'Category.None'
    MIXED: typing.ClassVar[str] = 'Category.Mixed'
class SimpleCategoryModel(omni.ui._ui.AbstractItemModel):
    """
    A data model for category items
    """
    def __init__(self, text: str, items: typing.Optional[typing.List[omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem]] = None, root: CategoryCollectionItem = None):
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
        
                Keyword Args:
                    items (Optional[List[BaseCategoryItem]]): Category items, defaults to None.
                    root (CategoryCollectionItem): Root category collection item, defaults to None.
                
        """
    def add_item(self, item: BaseCategoryItem, parent: BaseCategoryItem = None):
        """
        
                Add a new category item.
        
                Args:
                    item (BaseCategoryItem): Category item to add.
        
                Keyword Args:
                    parent (BaseCategoryItem): Parent category item, default to None to add as root.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def get_item_children(self, item: typing.Optional[omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem] = None) -> typing.List[omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem]:
        """
        
                Returns all the children when the widget asks it.
        
                Keyword Args:
                    item (Optional[BaseCategoryItem]): Parent item, defaults to None means to retrieve root items.
                
        """
