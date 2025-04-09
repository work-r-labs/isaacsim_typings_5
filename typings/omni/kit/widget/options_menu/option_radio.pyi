"""
This module provides UI components to create radio button options menus within the Omniverse Kit.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.checkable_delegate
from omni.kit.widget.options_menu.checkable_delegate import CheckableMenuItemDelegate
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import AbstractOptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparatorMenuItem
from omni.kit.widget.options_menu.setting_model import SettingModel
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'CheckableMenuItemDelegate', 'OptionRadios', 'OptionSeparatorMenuItem', 'RadioDelegate', 'SettingModel', 'ui']
class OptionRadios(omni.kit.widget.options_menu.option_item.AbstractOptionItem):
    """
    Item for a list of radios.
    
        Args:
            radios (List[Union[str, Tuple[str]]]): List of radios.
                Could be a simple string where text and value are the same,
                or a Tuple in the format (text, value).
                If the Tuple's value is None, it signifies a separator with 'text' as the title.
            model (Optional[ui.SimpleStringModel]): String model representing the radio value.
            setting_path (Optional[str]): Setting path representing the radio value.
            default (Optional[str]): Default radio value. None uses the current value from the radio model.
            menu_text (Optional[str]): None to show radios directly. If not None, show radios as a menu with radios as sub-menu items.
            enabled (bool): Whether the menu item is enabled. Defaults to True.
            tooltips (Optional[List[str]]): Tooltips for each radio. None means no tooltips.
            hide_on_click (bool): Whether to hide the menu item when clicked. Defaults to False.
    """
    def _OptionRadios__on_radio_changed(self, model: omni.ui._ui.SimpleStringModel) -> None:
        ...
    def __init__(self, radios: typing.List[typing.Union[str, typing.Tuple[str]]], model: typing.Optional[omni.ui._ui.SimpleStringModel] = None, setting_path: typing.Optional[str] = None, default: typing.Optional[str] = None, menu_text: typing.Optional[str] = None, enabled: bool = True, tooltips: typing.Optional[typing.List[str]] = None, hide_on_click: bool = False):
        """
        Initializes the OptionRadios item with provided parameters.
        """
    def _build_radio_items(self, **menu_item_kwargs: dict) -> typing.List[omni.ui._ui.MenuItem]:
        ...
    def build_menu_item(self, **menu_item_kwargs: dict) -> None:
        """
        Builds a menu item with the given radio options.
        
                Keyword Args:
                    enabled (bool): Whether the menu item is enabled.
                    hide_on_click (bool): Whether to hide the menu on item click.
                    text (str): The text to display for the menu item.
                    checkable (bool): If the menu item is checkable.
        """
    def destroy(self):
        """
        Cleans up the resources and delegates associated with the OptionRadios item.
        """
    def reset(self) -> None:
        """
        Resets the OptionRadios to its default value.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty state indicating if the OptionRadios value has changed.
        
                Returns:
                    bool: Whether the OptionRadios value has changed.
        """
    @property
    def enabled(self) -> bool:
        """
        Gets the enabled state of the OptionRadios item.
        
                Returns:
                    bool: The current enabled state.
        """
    @enabled.setter
    def enabled(self, value: bool) -> None:
        """
        Sets the enabled state of the OptionRadios item.
        
                Args:
                    value (bool): The enabled state to set.
        """
    @property
    def model(self) -> omni.ui._ui.SimpleStringModel:
        """
        Gets the model associated with the OptionRadios item.
        
                Returns:
                    ui.SimpleStringModel: The current model.
        """
class RadioDelegate(omni.kit.widget.options_menu.checkable_delegate.CheckableMenuItemDelegate):
    """
    Delegate for a radio menu item.
    
        This delegate manages the state and behavior of a radio menu item, ensuring that only one item in a group can be selected at a time.
    
        Args:
            model (RadioModel): The model containing the radio items.
            item (RadioItem): The specific radio item to delegate.
            enabled (bool): Specifies whether the radio item is enabled. Defaults to True.
    """
    def __init__(self, model: omni.ui._ui.SimpleStringModel, value: str, enabled: bool = True):
        """
        Constructor for RadioDelegate.
        """
    def build_item_icon(self):
        """
        Creates the icon for the menu item.
        """
    def on_triggered(self):
        """
        Action performed when the radio item is triggered.
        """
