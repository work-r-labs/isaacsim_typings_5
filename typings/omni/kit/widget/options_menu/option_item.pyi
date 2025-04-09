"""
Provides classes to represent and manage option items and delegates for an OptionsMenu in the Omniverse Kit.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.checkable_delegate
from omni.kit.widget.options_menu.checkable_delegate import CheckableMenuItemDelegate
from omni.kit.widget.options_menu.setting_model import SettingModel
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'CheckableMenuItemDelegate', 'OptionItem', 'OptionMenuItem', 'OptionMenuItemDelegate', 'SettingModel', 'ui']
class AbstractOptionItem(omni.ui._ui.AbstractItem):
    """
    Represents an abstract item for an OptionsMenu.
    """
    def build_menu_item(self, **menu_item_kwargs) -> None:
        """
        Builds a menu item for the option.
        
                Keyword Args:
                    enabled (bool): If the menu item is enabled.
                    checkable (bool): If the menu item is checkable.
                    hide_on_click (bool): If the menu item hides when clicked.
        """
    def destroy(self):
        """
        Destroys the option item.
        """
    def reset(self) -> None:
        """
        Resets the option item to its default state.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty flag indicating if the item's value has changed.
        
                Returns:
                    bool: True if the value has changed, False otherwise.
        """
    @property
    def model(self) -> omni.ui._ui.AbstractValueModel:
        """
        Gets the value model for this item.
        
                Returns:
                    ui.AbstractValueModel: The associated value model.
        """
class OptionItem(AbstractOptionItem):
    """
    Represents a general item for OptionsMenu.
    
        Args:
            name (str): The name of the menu item.
            text (str): The text to display for the menu item. Defaults to the name if not provided.
            default (bool): The initial value of the item. Defaults to False.
            on_value_changed_fn (Callable[[bool], None]): A callback function that is called when the item's value changes.
            model (Optional[ui.SimpleBoolModel]): The model associated with the item. If not provided, a new model is created.
            setting_path (Optional[str]): The path used to store the item's setting. If not provided, no setting is stored.
            enabled (bool): Indicates whether the menu item is enabled. Defaults to True.
            checkable (bool): Determines if the menu item can be checked. Defaults to True.
            hide_on_click (bool): Determines if the menu item should hide when clicked. Defaults to False.
    """
    def __init__(self, name: typing.Optional[str], text: typing.Optional[str] = None, default: bool = False, on_value_changed_fn: typing.Callable[[bool], NoneType] = None, model: typing.Optional[omni.ui._ui.SimpleBoolModel] = None, setting_path: typing.Optional[str] = None, enabled: bool = True, checkable: bool = True, hide_on_click: bool = False):
        """
        Constructor for OptionItem.
        """
    def build_custom_widget(self, item: omni.ui._ui.MenuItem) -> None:
        """
        Builds a custom widget for the associated menu item.
        
                Args:
                    item (ui.MenuItem): The menu item associated with this option.
        """
    def build_menu_item(self, **kwargs) -> None:
        """
        Builds the associated menu item with the given keyword arguments.
        
                Keyword Args:
                    enabled (bool): If the menu item is enabled.
        """
    def destroy(self):
        """
        Cleans up any resources held by the item.
        """
    def on_triggered(self):
        """
        Executes the action associated with the item when it is triggered.
        """
    def reset(self) -> None:
        """
        Resets the option item's value to its default state.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty state indicating if the item's value has changed.
        
                Returns:
                    bool: The current dirty state.
        """
    @property
    def enabled(self) -> bool:
        """
        Gets the enabled state of the option item.
        
                Returns:
                    bool: The current enabled state.
        """
    @enabled.setter
    def enabled(self, value: bool) -> None:
        """
        Sets the enabled state of the option item.
        
                Args:
                    value (bool): The new enabled state to set.
        """
    @property
    def model(self) -> omni.ui._ui.SimpleBoolModel:
        """
        Gets the value model of the option item.
        
                Returns:
                    ui.SimpleBoolModel: The current value model.
        """
    @property
    def value(self) -> bool:
        """
        Gets the current value of the option item.
        
                Returns:
                    bool: The current value.
        """
    @value.setter
    def value(self, new_value: bool) -> None:
        """
        Sets the current value of the option item.
        
                Args:
                    new_value (bool): The new value to set.
        """
class OptionMenuItem(omni.ui._ui.MenuItem):
    """
    Represent a menu item for a single option.
    
        Args:
            option_item (OptionItem): Option item to show as menu item.
            width (ui.Length): Menu item width. Default ui.Fraction(1).
            hide_on_click (bool): Whether the menu item should hide after a click. Default is False.
    
        Keyword Args:
            checkable (bool): If the menu item can be checked. Default True.
            enabled (bool): If the menu item is enabled. Default True.
            icon (Union[str, ui.Icon]): Icon to be displayed next to the menu item. Default None.
            shortcut (str): Shortcut key combination for the menu item. Default None.
            tooltip (str): Text to be displayed as a tooltip. Default None.
    """
    def __init__(self, option_item: OptionItem, width: omni.ui._ui.Length = ..., hide_on_click: bool = False, **kwargs):
        """
        Initialize the OptionMenuItem instance.
        """
    def destroy(self):
        """
        Destroy the OptionMenuItem, cleaning up any resources.
        """
class OptionMenuItemDelegate(omni.kit.widget.options_menu.checkable_delegate.CheckableMenuItemDelegate):
    """
    Delegate for a general option menu item.
        A general option item includes a selected icon and item text.
    
        Args:
            option_item (OptionItem): The option item to show as a menu item.
            width (ui.Length): The width of the menu item. Defaults to ui.Fraction(1).
    """
    def __init__(self, option_item: OptionItem, width: omni.ui._ui.Length = ...):
        """
        Initializer for OptionMenuItemDelegate.
        """
    def _on_mouse_hovered(self, hovered: bool) -> None:
        ...
    def _on_value_changed(self, model: omni.ui._ui.SimpleBoolModel) -> None:
        ...
    def build_item(self, item: omni.ui._ui.MenuItem):
        """
        Builds the UI representation for the menu item.
        
                Args:
                    item (ui.MenuItem): The menu item to build a UI for.
        """
    def build_widget(self, item: omni.ui._ui.MenuItem):
        """
        Builds the custom widget associated with the menu item.
        
                Args:
                    item (ui.MenuItem): The menu item to build a custom widget for.
        """
    def destroy(self):
        """
        Cleans up resources and subscriptions.
        """
    def on_triggered(self):
        """
        Executes the action associated with the menu item when triggered.
        """
