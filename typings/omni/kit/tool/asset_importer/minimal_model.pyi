from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['MinimalItem', 'MinimalModal', 'ui']
class MinimalItem(omni.ui._ui.AbstractItem):
    """
    
        Helper class for ui.AbstractItem implementations to create items for modal item model.
        
    """
    def __init__(self, text):
        ...
class MinimalModal(omni.ui._ui.AbstractItemModel):
    """
    
        Helper class for ui.AbstractItemModel implementations to store indexed items for use in Omniverse UI widgets.
        
    """
    def __init__(self, default_index, item_labels: list[str]):
        ...
    def get_item_children(self, _: omni.ui._ui.AbstractItem = None) -> typing.List[omni.ui._ui.AbstractItem]:
        ...
    def get_item_value_model(self, item: MinimalItem, _):
        ...
    @property
    def current_index(self) -> int:
        ...
