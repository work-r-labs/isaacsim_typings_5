"""
This module provides a radio menu widget for the Omniverse Kit with radio button groups, individual radio buttons, and their associated models and delegates.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.checkable_delegate
from omni.kit.widget.options_menu.checkable_delegate import CheckableMenuItemDelegate
from omni.kit.widget.options_menu.option_separator import OptionSeparatorMenuItem
import omni.kit.widget.options_menu.popup_menu
from omni.kit.widget.options_menu.popup_menu import AbstractPopupMenu
from omni.kit.widget.options_menu.popup_menu import PopupMenuDelegate
from omni import ui
import omni.ui._ui
__all__ = ['AbstractPopupMenu', 'CheckableMenuItemDelegate', 'OptionSeparatorMenuItem', 'PopupMenuDelegate', 'RadioItem', 'RadioMenu', 'RadioMenuDelegate', 'RadioMenuItem', 'RadioMenuItemDelegate', 'RadioModel', 'ui']
class RadioItem(omni.ui._ui.AbstractItem):
    """
    A class representing a single radio button item.
    
        This class is used to create an item that can be used in a radio button group, where only one item can be selected at a time.
    
            Args:
                text (str): The text label displayed next to the radio button.
    """
    def __init__(self, text: str):
        """
        Initializer for the RadioItem.
        """
    @property
    def text(self) -> str:
        """
        Gets the text of the RadioItem.
        
                Returns:
                    str: The text associated with the RadioItem.
        """
class RadioMenu(omni.kit.widget.options_menu.popup_menu.AbstractPopupMenu):
    """
    Represent a menu for radios.
    
        Args:
            title (str): Title shown in header.
            radio_model (Union[RadioModel, List[RadioModel]]): Radio Models.
    """
    def __init__(self, title: str, radio_model: typing.Union[omni.kit.widget.options_menu.radio_menu.RadioModel, typing.List[omni.kit.widget.options_menu.radio_menu.RadioModel]]):
        """
        Initializer for RadioMenu.
        """
    def build_menu_items(self):
        """
        Generates and populates the menu items for each radio model.
        """
    def destroy(self):
        """
        Cleans up resources used by the RadioMenu instance.
        """
class RadioMenuDelegate(omni.kit.widget.options_menu.popup_menu.PopupMenuDelegate):
    """
    Delegate for a radio menu.
    
        This delegate allows for managing multiple radio models within a menu, ensuring that only one radio item can be checked at a time.
    
            Args:
                radio_models (List[RadioModel]): List of RadioModels to be displayed in the menu.
    """
    def __init__(self, radio_models: typing.List[omni.kit.widget.options_menu.radio_menu.RadioModel]):
        """
        Constructor for RadioMenuDelegate.
        """
    def _on_index_changed(self, model: omni.ui._ui.SimpleIntModel) -> None:
        ...
    def build_title(self, item: omni.ui._ui.Menu) -> None:
        """
        Builds the title for the radio menu.
        
                Args:
                    item (ui.Menu): The menu to which the title will be built.
        """
    def destroy(self):
        """
        Clean up resources and subscriptions.
        """
    def on_reset_all(self) -> None:
        """
        Resets all radio models to their default indices.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty state of the radio models.
        
                Returns:
                    bool: True if any model's selected index is not default, else False.
        """
class RadioMenuItem(omni.ui._ui.MenuItem):
    """
    Represent a menu item for a single radio item.
    
        Args:
            model (RadioModel): Radio Model that includes the radio item.
            item (RadioItem): Radio item.
    """
    def __init__(self, model: RadioModel, item: RadioItem):
        """
        Constructor for RadioMenuItem.
        """
    def destroy(self):
        """
        Destroys the radio menu item and cleans up resources.
        """
class RadioMenuItemDelegate(omni.kit.widget.options_menu.checkable_delegate.CheckableMenuItemDelegate):
    """
    Delegate for radio menu item.
        While only one radio item in a radio model could be checked at the same time.
    
        Args:
            model (RadioModel): Radio Model includes the radio item.
            item (RadioItem): Radio item.
    """
    def __init__(self, model: RadioModel, item: RadioItem):
        """
        Constructor for RadioMenuItemDelegate.
        """
    def _on_index_changed(self, model: omni.ui._ui.SimpleIntModel):
        ...
    def destroy(self):
        """
        Cleans up the resources held by the delegate.
        """
    def on_triggered(self):
        """
        Sets the current index of the model to this item's index.
        """
class RadioModel(omni.ui._ui.AbstractItemModel):
    """
    A class that represents a model for radio buttons, allowing the selection of a single option from a list.
    
        Args:
            texts (List[str]): A list of strings representing the options.
            default_index (int): The index of the initially selected option.
    """
    def __init__(self, texts: typing.List[str], default_index: int = 0):
        """
        Initializes a new instance of RadioModel.
        """
    def get_item_children(self, item: typing.Optional[omni.kit.widget.options_menu.radio_menu.RadioItem] = None) -> typing.List[omni.kit.widget.options_menu.radio_menu.RadioItem]:
        """
        Gets the children items of a given item or all items if no item is provided.
        
                Args:
                    item (Optional[RadioItem]): The parent item or None for all items.
        
                Returns:
                    List[RadioItem]: A list of child items.
        """
    def reset(self) -> None:
        """
        Resets the index to the default value.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets whether the current selected index is not the default one.
        
                Returns:
                    bool: True if the current index is not the default, False otherwise.
        """
    @property
    def index(self) -> int:
        """
        Gets the current index value.
        
                Returns:
                    int: The current index value.
        """
    @index.setter
    def index(self, value: int) -> None:
        """
        Sets the current index to a new value.
        
                Args:
                    value (int): The new index to set.
        """
    @property
    def index_model(self) -> omni.ui._ui.SimpleIntModel:
        """
        Gets the model of the current index.
        
                Returns:
                    ui.SimpleIntModel: The model representing the current index.
        """
    @property
    def index_text(self) -> str:
        """
        Gets the text of the currently selected string.
        
                Returns:
                    str: The text of the current selection.
        """
