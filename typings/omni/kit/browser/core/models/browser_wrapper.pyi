from __future__ import annotations
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import BaseItem
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_item import CollectionItem
from omni.kit.browser.core.models.browser_model import AbstractBrowserModel
from omni import ui
import omni.ui._ui
__all__ = ['AbstractBrowserModel', 'BaseItem', 'CategoryItem', 'ChildrenModelWrapper', 'CollectionItem', 'CollectionModelWrapper', 'SingleLevelWrapper', 'ui']
class ChildrenModelWrapper(SingleLevelWrapper):
    """
    
        This model represents a data model to get children of item.
        Note:
            Current only category item has children.
        
    """
    def get_item_children(self, item = None) -> typing.List[omni.ui._ui.AbstractItem]:
        """
        
                Returns all the children when the widget asks it.
                Return empty list if source model not defined.
                
        """
class CollectionModelWrapper(SingleLevelWrapper):
    """
    
        The model that has int value in the root, so it's acceptable by combo box.
        Args:
            source_model (Optional[AbstractBrowserModel]): source data model. None for empty wrapper.
            root_item (Optional[BaseItem]): using children item list of this item as data items, comes from source_model.
        
    """
    current_index: int
    def __init__(self, source_model, root_item):
        ...
    def _get_current_item(self) -> omni.kit.browser.core.models.browser_item.CollectionItem:
        """
        Get Current selected collection item
        """
    def _on_current_index_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def add_selection_changed_fn(self, on_selection_changed_fn: callable) -> int:
        """
        
                Add notification when current selected collection changed.
                Args:
                    on_selection_changed_fn (func): Function called when current selected collection changed. Return notificaation
                        id used for remove_selection_changed_fn. Function signature:
                        int on_selection_changed_fn(collection_item: CollectionItem)
                
        """
    def get_item_value_model(self, item = None, column_id = 0) -> omni.ui._ui.AbstractValueModel:
        ...
    def remove_selection_changed_fn(self, id: int) -> bool:
        """
        
                Remove notification on current selected collection changed.
                Args:
                    id (int): Notification id returned from add_selection_changed_fn.
                
        """
class SingleLevelWrapper(omni.ui._ui.AbstractItemModel):
    """
    
        The model pretends a source model with one single level of children
        Args:
            source_model (Optional[AbstractBrowserModel]): source data model. None for empty wrapper.
            root_item (Optional[BaseItem]): using children item list of this item as data items, comes from source_model.
        
    """
    def __init__(self, source_model: typing.Optional[omni.kit.browser.core.models.browser_model.AbstractBrowserModel] = None, root_item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None):
        ...
    def get_item_children(self, item = None) -> typing.List[omni.ui._ui.AbstractItem]:
        """
        
                Returns all the children when the widget asks it.
                Return empty list if source model not defined.
                
        """
    def get_item_value_model(self, item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None, column_id: int = 0) -> typing.Optional[omni.ui._ui.AbstractValueModel]:
        """
        
                Get the item name model.
                Args:
                    item (Optional[BaseItem]): item to query. If not None, return its name model. Otherwise return None.
                    column_id (int): ignored.
                
        """
    def get_item_value_model_count(self, item = None) -> int:
        """
        The number of columns
        """
    def set_sources(self, source_model: typing.Optional[omni.kit.browser.core.models.browser_model.AbstractBrowserModel] = None, root_item: typing.Optional[omni.kit.browser.core.models.browser_item.BaseItem] = None):
        """
        
                Update data source and trigger item changed for binded widget
                Args:
                    source_model (Optional[AbstractBrowserModel]): source data model. None for empty wrapper.
                    root_item (Optional[BaseItem]): using children item list of this item as data items, comes from source_model.
                
        """
