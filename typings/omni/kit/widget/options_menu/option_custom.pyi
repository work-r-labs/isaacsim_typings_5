"""
This module defines a custom option item class for user interfaces, supporting custom build functions and optional models for value storage.
"""
from __future__ import annotations
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import AbstractOptionItem
from omni import ui
import omni.ui._ui
__all__ = ['AbstractOptionItem', 'OptionCustom', 'ui']
class OptionCustom(omni.kit.widget.options_menu.option_item.AbstractOptionItem):
    """
    A class that represents a custom option item with a build function and a model.
    
        This class allows for the creation of a custom option item within a user interface, using
        a provided build function to construct the menu item. It supports an optional model
        to hold the value of the option and an optional default value to be used when resetting.
    
            Args:
                build_fn (callable): The function used to build the menu item.
                model (Optional[ui.AbstractValueModel]): The model used to store the value of the option item.
                default (Optional[Any]): The default value of the option item if not provided by the model.
    """
    def __init__(self, build_fn: callable, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, default: typing.Optional[typing.Any] = None):
        """
        Initializes the custom option with the provided build function and model.
        """
    def build_menu_item(self, **kwargs) -> None:
        """
        Builds a menu item with the specified attributes.
        """
    def reset(self) -> None:
        """
        Resets the custom option's value to its default.
        """
    @property
    def dirty(self) -> bool:
        """
        Gets the dirty status of the custom option.
        
                Returns:
                    bool: True if the value has changed from the default, False otherwise.
        """
    @property
    def model(self) -> omni.ui._ui.SimpleBoolModel:
        """
        Gets the model associated with the custom option.
        
                Returns:
                    ui.SimpleBoolModel: The current model of the custom option.
        """
    @property
    def name(self) -> str:
        """
        Gets the name of the custom option.
        
                Returns:
                    str: The name of the custom option.
        """
