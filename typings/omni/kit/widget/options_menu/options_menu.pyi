"""
Provides a customizable options menu widget for the Omniverse Kit UI.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import AbstractOptionItem
import omni.kit.widget.options_menu.options_model
from omni.kit.widget.options_menu.options_model import OptionsModel
import omni.kit.widget.options_menu.popup_menu
from omni.kit.widget.options_menu.popup_menu import AbstractPopupMenu
from omni.kit.widget.options_menu.popup_menu import PopupMenuDelegate
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'AbstractPopupMenu', 'OPTIONS_MENU_STYLE', 'OptionsMenu', 'OptionsMenuDelegate', 'OptionsModel', 'PopupMenuDelegate', 'ui']
class OptionsMenu(omni.kit.widget.options_menu.popup_menu.AbstractPopupMenu):
    """
    Represent a menu to show options.
    
        A options menu includes a header and a list of menu items for options.
    
            Args:
                model (OptionsModel): Model of option items to show in this menu.
                hide_on_click (bool): Hide menu when item clicked. Default False.
                width (ui.Length): Width of menu item. Default ui.Fraction(1).
                style (dict): Additional style. Default empty.
    """
    def _OptionsMenu__on_model_changed(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, item: typing.Optional[omni.kit.widget.options_menu.option_item.AbstractOptionItem]) -> None:
        ...
    def __init__(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, hide_on_click: bool = False, width: omni.ui._ui.Length = ..., style: dict = {}):
        """
        Initializes the options menu with the given parameters.
        """
    def build_menu_items(self):
        """
        Builds the menu items from the model's item children.
        """
    def destroy(self):
        """
        Cleans up the resources and subscriptions.
        """
    def rebuild_items(self, items: typing.List[omni.kit.widget.options_menu.option_item.AbstractOptionItem]) -> None:
        """
        Rebuilds the menu items based on the provided items list.
        
                Args:
                    items (List[AbstractOptionItem]): The items to rebuild the menu with.
        """
    @property
    def model(self) -> omni.kit.widget.options_menu.options_model.OptionsModel:
        """
        Gets the model associated with the options menu.
        
                Returns:
                    OptionsModel: The model of the options menu.
        """
class OptionsMenuDelegate(omni.kit.widget.options_menu.popup_menu.PopupMenuDelegate):
    """
    Delegate for options menu.
        It has a header to show label and reset button.
    
        Args:
            model (OptionsModel): Model for options to show in this menu.
    """
    def _OptionsMenuDelegate__on_item_changed(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, item: omni.kit.widget.options_menu.option_item.AbstractOptionItem) -> None:
        ...
    def __init__(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, **kwargs):
        """
        Initializes the options menu delegate.
        """
    def build_title(self, item: omni.ui._ui.Menu) -> None:
        """
        Builds the title for the given menu item.
        
                Args:
                    item (ui.Menu): The menu item to build the title for.
        """
    def destroy(self) -> None:
        """
        Cleans up resources.
        """
    def get_title(self, item: omni.ui._ui.Menu) -> str:
        """
        Retrieves the title for the given menu item.
        
                Args:
                    item (ui.Menu): The menu item to get the title for.
        """
    def on_reset_all(self) -> None:
        """
        Resets all options to their default values.
        """
OPTIONS_MENU_STYLE: dict  # value = {'Title.Background': {'background_color': 4280492319, 'corner_flag': <CornerFlag.TOP: 3>, 'margin': 0}, 'Title.Header': {'margin_width': 3, 'margin_height': 0}, 'Title.Label': {'background_color': 0, 'color': 'shade:4288782753', 'margin_width': 5}, 'ResetButton': {'background_color': 0}, 'ResetButton:hovered': {'background_color': 'shade:4281611314'}, 'ResetButton.Label': {'color': 'shade:4294952756'}, 'ResetButton.Label:disabled': {'color': 'shade:4285427310'}, 'ResetButton.Label:hovered': {'color': 'shade:4291137818'}, 'MenuItem.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/check_solid.svg', 'color': 0, 'margin': 7}, 'MenuItem.Icon:checked': {'color': 'shade:4294952756'}, 'MenuItem.Icon:selected': {'color': 'shade:4280492319'}, 'MenuItem.Icon::disabled:disabled': {'color': 'shade:4285427310', 'margin': 7}, 'MenuItem.Radio': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/radiomark.svg', 'color': 0, 'margin': 7}, 'MenuItem.Radio:checked': {'color': 'shade:4294952756'}, 'MenuItem.Radio:selected': {'color': 'shade:4280492319'}, 'MenuItem.Label::title': {'color': 'shade:4288782753', 'margin_width': 5}, 'MenuItem.Label:disabled': {'color': 'shade:4285427310'}, 'MenuItem.Separator': {'color': 'shade:4284703586', 'border_width': 1.5}}
