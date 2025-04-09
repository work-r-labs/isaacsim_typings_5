from __future__ import annotations
import abc as abc
import carb as carb
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import BaseItem
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_item import DetailItem
from omni import ui
import omni.ui._ui
__all__ = ['AbstractBrowserModel', 'BaseItem', 'CategoryItem', 'CollectionItem', 'DetailItem', 'abc', 'carb', 'ui']
class AbstractBrowserModel(omni.ui._ui.AbstractItemModel):
    """
    
        Abstract model for the browser. User need to reimplement following functions:
            get_collection_items
            get_category_items
            get_detail_items
    
        This model uses a simple cache to get collection/category/detail items.
        Reimplement get_item_children if user wants own cache.
    
        Args:
            overview_name (str): Create a summary category and show all other categories as children if defined. Default None.
            always_realod_detail_items (bool): If True, always reload detail items. Otherwise, load detail items from cache if not updated. Default False
    
        Overridden functions:
            void execute(self, item: DetailItem): Execute a file.
                Args:
                    item: Detail item to be executed.
            bool remove_collection(self, item: CollectionItem): Remove a collection.
                Args:
                    item: Collection item to be removed.
    
        
    """
    def _AbstractBrowserModel__remove_from_cache(self, _, item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem]) -> None:
        ...
    def __init__(self, overview_name: typing.Optional[str] = None, always_realod_detail_items: bool = False):
        ...
    def execute(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        """
        
                Execute a detail item.
                Args:
                    item: Detail item to be executed.
                
        """
    def get_category_items(self, item: omni.kit.browser.core.models.browser_item.CollectionItem) -> typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]:
        """
        Get list of category items for category view
        """
    def get_collection_items(self) -> typing.List[omni.kit.browser.core.models.browser_item.CollectionItem]:
        """
        Get list of collection items for collection combobox
        """
    def get_detail_items(self, item: omni.kit.browser.core.models.browser_item.CategoryItem) -> typing.List[omni.kit.browser.core.models.browser_item.DetailItem]:
        """
        Get list of detail items for detail view
        """
    def get_item_children(self, item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None) -> typing.List[omni.ui._ui.AbstractItem]:
        """
        
                Returns all the children when the widget asks it.
                Args:
                    item (Optional[BaseItem]): parent item.
                        if None, return collection item list
                        if CollectionItem, return categorty item list
                        if CategoryItem, return detail item list
                        otherwise, return empty list
                
        """
    def get_item_value_model(self, item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None, index: int = 0) -> typing.Optional[omni.ui._ui.AbstractValueModel]:
        """
        
                Get the item name model.
                Args:
                    item (Optional[BaseItem]): item to query. If not None, return its name model. Otherwise return None.
                    index (int): ignored.
                
        """
    def get_item_value_model_count(self, item = None) -> int:
        """
        The number of columns
        """
    def get_sort_args(self) -> typing.Optional[typing.Dict]:
        """
        
                Get sort args to sort item list.
                In format {"key": key, "reverse": reverse}
                
        """
    def remove_collection(self, item: omni.kit.browser.core.models.browser_item.CollectionItem) -> bool:
        """
        
                Remove a collection item.
                Args:
                    item: CollectionItem to be removed.
                
        """
    def sort_changed(self) -> None:
        """
        
                Notify sort changed.
                
        """
