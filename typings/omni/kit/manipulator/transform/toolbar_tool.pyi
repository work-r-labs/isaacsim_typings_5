from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.manipulator.transform.manipulator import TransformManipulator
from omni.kit.manipulator.transform.types import Operation
from omni import ui
from pathlib import Path
import typing
import weakref as weakref
from weakref import ProxyType
__all__ = ['ABC', 'DefaultMenuDelegate', 'Operation', 'Path', 'ProxyType', 'SimpleToolButton', 'ToolbarTool', 'TransformManipulator', 'abstractmethod', 'asyncio', 'carb', 'omni', 'ui', 'weakref']
class DefaultMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    A delegate for default menu that handles the style of the context menu.
    
        This delegate provides a default style configuration for context menus used within the application.
    """
    def get_style(self):
        """
        Gets the style configuration for the context menu.
        
                Returns:
                    The style configuration dictionary for the menu.
        """
class SimpleToolButton(ToolbarTool):
    """
    A toolbar button with optional context menu for transform manipulators.
    
        This class provides a button for the toolbar that can interact with transform manipulators and optionally display a context menu.
    
        Args:
            menu_delegate (ui.MenuDelegate, optional): Delegate for styling the context menu associated with the button.
            *args: Variable length argument list for parent class initialization.
            **kwargs: Arbitrary keyword arguments for parent class initialization.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'can_build'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, menu_delegate: ui.MenuDelegate = None, *args, **kwargs):
        """
        Initializes a new instance of a simple tool button with an optional context menu.
        """
    def _build_flyout_indicator(self, width, height, index: str, extension_id: str, padding = -8, min_menu_count = 1):
        """
        Builds an indicator for the flyout menu.
        
                Args:
                    width: The width of the area where the indicator will be placed.
                    height: The height of the area where the indicator will be placed.
                    index (str): The index used for context menu retrieval.
                    extension_id (str): The extension ID related to the context menu.
                    padding (int, optional): The padding offset for the indicator's position.
                    min_menu_count (int, optional): The minimum number of menu entries required for the indicator to be visible.
        
                Returns:
                    Subscription: A subscription to the menu event stream to update the indicator visibility.
        """
    def _build_widget(self, button_name: str, model: ui.AbstractValueModel, enabled_img_url: str, disabled_img_url: str = None, menu_index: str = None, menu_extension_id: str = None, no_toggle: bool = False, menu_on_left_click: bool = False, menu_payload: dict[str, typing.Any] = {}, tooltip: str = '', disabled_tooltip: str = ''):
        """
        Builds the button widget with an optional context menu.
        
                Args:
                    button_name (str): The name of the button.
                    model (ui.AbstractValueModel): The model that holds the button state.
                    enabled_img_url (str): The URL to the image displayed when the button is enabled.
                    disabled_img_url (str, optional): The URL to the image displayed when the button is disabled.
                    menu_index (str, optional): Identifier for the context menu.
                    menu_extension_id (str, optional): Extension ID related to the context menu.
                    no_toggle (bool, optional): If True, the button doesn't toggle state on click.
                    menu_on_left_click (bool, optional): If True, displays the context menu on left click.
                    menu_payload (Dict[str, Any], optional): Additional payload for the context menu.
                    tooltip (str, optional): The tooltip text when the button is enabled.
                    disabled_tooltip (str, optional): The tooltip text when the button is disabled.
        """
    def _get_style(self) -> dict:
        """
        Gets the style configuration for the button.
        
                Returns:
                    Dict: The style configuration dictionary for the button.
        """
    def _invoke_context_menu(self, button_id: str, right_click: bool, min_menu_entries: int = 1):
        """
        Invokes the context menu for the button.
        
                Args:
                    button_id (str): The identifier of the button.
                    right_click (bool): Indicates whether the menu is invoked by a right click.
                    min_menu_entries (int, optional): The minimum number of entries required for the menu to be visible.
        """
    def _on_hovered(self, state: bool):
        """
        Callback function that is called when the button is hovered.
        
                Args:
                    state (bool): The hover state of the button.
        """
    def _on_model_changed(self, model):
        """
        Callback function that is called when the button's model value changes.
        
                Args:
                    model: The model associated with the button.
        """
    def _on_mouse_pressed(self, button, button_id: str, min_menu_entries: int = 1):
        """
        Function to handle flyout menu. Either with LMB long press or RMB click.
        
                Args:
                    button: Mouse button that was pressed.
                    button_id (str): The identifier of the button.
                    min_menu_entries (int, optional): The minimum number of entries required for the menu to be visible.
        """
    def _on_mouse_released(self, button):
        """
        Handler for button release events, potentially canceling the display of the context menu.
        
                Args:
                    button: Mouse button that was released.
        """
    def _schedule_show_menu(self, button_id: str, min_menu_entries: int = 1, wait_seconds: float = 0.3):
        """
        Schedules the display of the context menu after a delay.
        
                Args:
                    button_id (str): The identifier of the button for the context menu.
                    min_menu_entries (int, optional): The minimum number of entries required for the menu to be visible.
                    wait_seconds (float, optional): The time to wait before showing the menu.
        """
    def _update_name(self, button: ui.ToolButton, enabled: bool):
        """
        Updates the button's name based on its enabled state.
        
                Args:
                    button (ui.ToolButton): The button to update.
                    enabled (bool): The enabled state of the button.
        """
    def destroy(self):
        """
        Cleans up resources and references held by the simple tool button.
        """
class ToolbarTool(abc.ABC):
    """
    An abstract base class for creating toolbar tools that interact with TransformManipulators.
    
        This class provides foundational structure and common functionality for specialized toolbar tools. It is not intended to be instantiated directly but subclassed by concrete tool implementations.
    
        Args:
            manipulator (ProxyType[TransformManipulator]): A weak reference proxy to the TransformManipulator.
            operation (Operation): The operation type that the toolbar tool is associated with.
            toolbar_height (int): The height of the toolbar to which the tool belongs.
            toolbar_payload (Dict[str, Any]): Optional; A dictionary of payload items for the toolbar.
            tooltip_update_fn (Callable[[str, bool, float], None]): Optional; Function to call for updating tooltips.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'can_build'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def can_build(cls, manipulator: TransformManipulator, operation: Operation) -> bool:
        """
        
                Called right before a tool instance is to be instantiated to determine if this tool can be built on current toolbar.
        
                Args:
                    manipulator (TransformManipulator): manipulator that hosts the toolbar
                    operation (Operation): The transform Operation the tool will be built for.
        
                Return:
                    bool: True if the tool can be built, its constructor will be called. False if not, the tool will be skipped and not placed on toolbar.
                
        """
    def __del__(self):
        ...
    def __init__(self, manipulator: ProxyType[TransformManipulator], operation: Operation, toolbar_height: int, toolbar_payload: dict[str, typing.Any] = {}, tooltip_update_fn: typing.Callable[[str, bool, float], None] = None):
        """
        Initializes a new instance of a toolbar tool.
        """
    def destroy(self):
        """
        Cleans up resources and references held by the toolbar tool.
        """
