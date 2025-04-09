"""
Provides a customizable popup menu with a delegate system for handling menu items and actions in the Omniverse Kit.
"""
from __future__ import annotations
import abc as abc
import carb as carb
from omni import ui
import omni.ui._ui
__all__ = ['AbstractPopupMenu', 'OPTIONS_MENU_STYLE', 'PopupMenuDelegate', 'PopupMenuItemDelegate', 'abc', 'carb', 'ui']
class AbstractPopupMenu(omni.ui._ui.Menu):
    """
    Represent a popup menu.
        A popup menu includes a header and a list of menu items.
    
        Args:
            title (str): Title in header
            delegate (Optional[PopupMenuDelegate]): Menu delegate. Default None to use PopupMenuDelegate
            style (dict): Additional style. Default empty.
    """
    def __init__(self, title: str, delegate: typing.Optional[omni.kit.widget.options_menu.popup_menu.PopupMenuDelegate] = None, style: dict = {}):
        """
        Initializes an abstract popup menu instance.
        """
    def build_menu_items(self):
        """
        Abstract method to build menu items for the popup menu.
        """
    def destroy(self):
        """
        Destroys the popup menu and its delegate.
        """
    def show_by_widget(self, widget: omni.ui._ui.Widget, alignment: omni.ui._ui.Alignment = ...) -> None:
        """
        Displays the popup menu adjacent to the specified widget.
        
                Args:
                    widget (ui.Widget): The widget to align the popup menu with.
                    alignment (ui.Alignment): The preferred alignment for the popup menu.
        """
class PopupMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    Delegate for popup menu.
        It has a header to show label and reset button.
    
            Keyword Args:
                propagate (bool): Whether the event propagation is allowed. Default True.
                style_type_name_override (str): The name of the style type override. Default None.
    """
    def __init__(self, **kwargs):
        """
        Initializes the popup menu delegate.
        """
    def build_title(self, item: omni.ui._ui.Menu) -> None:
        """
        Builds the title section of the popup menu.
        
                Args:
                    item (ui.Menu): The menu item for which to build the title.
        """
    def destroy(self) -> None:
        """
        Cleans up any resources held by the delegate.
        """
    def enable_reset_all(self, enabled: bool) -> None:
        """
        Enables or disables the reset all button.
        
                Args:
                    enabled (bool): True to enable, False to disable the reset all button.
        """
    def get_title(self, item: omni.ui._ui.Menu) -> str:
        """
        Retrieves the title for the given menu item.
        
                Args:
                    item (ui.Menu): The menu item to retrieve the title for.
        
                Returns:
                    str: The title of the menu item.
        """
    def on_reset_all(self) -> None:
        """
        Handles the reset all action.
        """
class PopupMenuItemDelegate(omni.ui._ui.MenuDelegate):
    """
    Delegate for general popup menu item.
        A general popup item includes a selected icon and item text.
    
        Args:
            width (ui.Length): Menu item width. Default ui.Fraction(1).
    """
    def __init__(self, width: omni.ui._ui.Length = ...):
        """
        Initializes the popup menu item delegate.
        """
    def _on_mouse_hovered(self, hovered: bool) -> None:
        ...
    def build_item(self, item: omni.ui._ui.MenuItem):
        """
        Builds UI components for the menu item.
        
                Args:
                    item (ui.MenuItem): The menu item to build UI components for.
        """
    def destroy(self):
        """
        Cleans up resources used by the delegate.
        """
    def on_trigger(self) -> None:
        """
        Handles the trigger action for the menu item.
        """
OPTIONS_MENU_STYLE: dict  # value = {'Title.Background': {'background_color': 4280492319, 'corner_flag': <CornerFlag.TOP: 3>, 'margin': 0}, 'Title.Header': {'margin_width': 3, 'margin_height': 0}, 'Title.Label': {'background_color': 0, 'color': 'shade:4288782753', 'margin_width': 5}, 'ResetButton': {'background_color': 0}, 'ResetButton:hovered': {'background_color': 'shade:4281611314'}, 'ResetButton.Label': {'color': 'shade:4294952756'}, 'ResetButton.Label:disabled': {'color': 'shade:4285427310'}, 'ResetButton.Label:hovered': {'color': 'shade:4291137818'}, 'MenuItem.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/check_solid.svg', 'color': 0, 'margin': 7}, 'MenuItem.Icon:checked': {'color': 'shade:4294952756'}, 'MenuItem.Icon:selected': {'color': 'shade:4280492319'}, 'MenuItem.Icon::disabled:disabled': {'color': 'shade:4285427310', 'margin': 7}, 'MenuItem.Radio': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/radiomark.svg', 'color': 0, 'margin': 7}, 'MenuItem.Radio:checked': {'color': 'shade:4294952756'}, 'MenuItem.Radio:selected': {'color': 'shade:4280492319'}, 'MenuItem.Label::title': {'color': 'shade:4288782753', 'margin_width': 5}, 'MenuItem.Label:disabled': {'color': 'shade:4285427310'}, 'MenuItem.Separator': {'color': 'shade:4284703586', 'border_width': 1.5}}
