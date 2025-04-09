"""
Provides a model for managing and interacting with a collection of option items in a menu.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import AbstractOptionItem
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'OptionsModel', 'ui']
class OptionsModel(omni.ui._ui.AbstractItemModel):
    """
    Model for options items.
    
        This class represents a model for managing a collection of option items within a menu.
        The model provides functionality to manage the lifecycle of the items, track changes, and notify subscribers of updates.
    
        Args:
            name (str): Model name to display in the menu header.
            items (List[AbstractOptionItem]): Items to be displayed in the menu.
    """
    def _OptionsModel__clean_items(self):
        ...
    def _OptionsModel__on_value_changed(self, item: omni.kit.widget.options_menu.option_item.AbstractOptionItem, model: omni.ui._ui.SimpleBoolModel):
        ...
    def __init__(self, name: str, items: typing.List[omni.kit.widget.options_menu.option_item.AbstractOptionItem]):
        """
        Initializes the OptionsModel.
        """
    def destroy(self):
        """
        Cleans up the model, preparing for destruction.
        """
    def get_item_children(self, item: typing.Optional[omni.kit.widget.options_menu.option_item.AbstractOptionItem] = None) -> typing.List[omni.kit.widget.options_menu.option_item.AbstractOptionItem]:
        """
        Retrieves the children of a given item or all items if none specified.
        
                Args:
                    item (Optional[AbstractOptionItem]): The parent item whose children to retrieve.
        """
    def rebuild_items(self, items: typing.List[omni.kit.widget.options_menu.option_item.AbstractOptionItem]) -> None:
        """
        Rebuilds the internal list of option items.
        
                Args:
                    items (List[AbstractOptionItem]): The new list of items to show in the model.
        """
    def reset(self) -> None:
        """
        Resets all items in the model to their default values.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty state of the options model.
        
                Returns:
                    bool: True if any item is not in its default value, False otherwise.
        """
