from __future__ import annotations
import asyncio as asyncio
import carb as carb
import math as math
import omni as omni
from omni.kit.manipulator.tool.snap.models import SettingModel
from omni.kit.manipulator.tool.snap.provider import SnapProvider
from omni.kit.manipulator.tool.snap.registry import SnapProviderRegistry
from omni.kit.manipulator.transform.settings_constants import Constants as transform_c
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_radio import OptionRadios
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.widget.options_menu.options_menu import OptionsMenu
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni import ui
import typing
__all__ = ['CONFORM_TO_TARGET_SETTING_PATH', 'CONFORM_UP_AXIS_SETTING_PATH', 'ExplicitTransformItem', 'KEEP_SPACING_SETTING_PATH', 'MENU_SUFFIX_ROTATE', 'MENU_SUFFIX_SCALE', 'MENU_SUFFIX_TRANSLATE', 'OP_TO_NAME', 'OptionItem', 'OptionRadios', 'OptionSeparator', 'OptionsMenu', 'OptionsModel', 'ProviderItem', 'SNAP_ENABLED_SETTING', 'SNAP_PROVIDER_NAME_SETTING_PATH', 'SNAP_ROTATE_SETTING_PATH', 'SNAP_SCALE_SETTING_PATH', 'SNAP_SETTING_PREFIX', 'SNAP_TRANSLATE_SETTING_PATH', 'SettingModel', 'SnapMenu', 'SnapProvider', 'SnapProviderRegistry', 'TRANSFORM_OP_SETTING', 'asyncio', 'carb', 'math', 'omni', 'transform_c', 'ui']
class ExplicitTransformItem(omni.kit.widget.options_menu.option_item.OptionItem):
    """
    A menu item for explicitly setting transform values in a snap options menu.
    
        This class extends OptionItem to provide a UI component that allows users to enter specific transform values (like translation, rotation, and scale) when snapping objects in the scene. The behavior and default value are adjusted depending on the type of transformation.
    
        Args:
            suffix: str
                A string that represents the suffix for the transform operation (e.g., 'translate', 'rotate', 'scale').
    
        
    """
    def __init__(self, suffix: str):
        """
        Initializes an ExplicitTransformItem with a specific suffix.
        
                Args:
                    suffix (str): A string that represents the suffix for the transform operation (e.g., 'translate', 'rotate', 'scale').
                
        """
    def build_custom_widget(self, item: ui.MenuItem):
        """
        Builds the custom widget for the menu item.
        
                Args:
                    item (ui.MenuItem): The UI menu item that this custom widget is associated with.
        """
    def destroy(self):
        """
        Cleans up the resources and subscriptions associated with this item.
        """
    def on_triggered(self):
        """
        Handles the action when the menu item is triggered.
        
                This method performs specific actions based on the suffix of the transform operation.
        """
    def reset(self) -> None:
        """
        Resets the item to its default state, both the check status and the explicit transform value.
        """
    @property
    def dirty(self) -> bool:
        """
        Indicates whether the item's value has changed from its default.
        
                Returns:
                    bool: True if the value has changed, False otherwise.
        """
class ProviderItem(omni.kit.widget.options_menu.option_item.OptionItem):
    """
    A menu item representing a snap provider in a snap options menu.
    
        This class extends OptionItem to create an interactive menu entry for enabling or
         disabling a snap provider within the application.
    
        Args:
            name: str
                The name of the snap provider.
            provider_class: Type[SnapProvider]
                The class type of the snap provider.
            enabled: bool
                Indicates whether the provider is initially enabled.
    """
    def __init__(self, name: str, provider_class: Type[SnapProvider], enabled: bool):
        """
        Initializes a menu item for a snap provider.
        
                Args:
                    name (str): The name of the snap provider.
                    provider_class (Type[SnapProvider]): The class of the snap provider.
                    enabled (bool): A flag indicating if the provider is enabled.
        """
    def _enable_provider(self, enabled: bool) -> None:
        """
        Enables or disables the snap provider based on the provided boolean value.
        
                Args:
                    enabled (bool): A boolean indicating whether to enable or disable the provider.
        """
    def is_checked(self) -> bool:
        """
        Checks if the provider is enabled in the settings.
        
                Returns:
                    bool: True if the provider is enabled, False otherwise.
        """
class SnapMenu:
    """
    A class responsible for creating and managing the snap options menu in the application.
    
        This class provides functionality to build and display menus for translating, rotating, and scaling objects using snap providers. It also handles the creation of menu items related to snapping such as 'Align to Target' and 'Keep Spacing'.
        
    """
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _build_rotate_menu(self) -> OptionsMenu:
        """
        Builds the rotate options menu with relevant items.
        
                Returns:
                    OptionsMenu: The constructed rotate options menu.
        """
    def _build_scale_menu(self) -> OptionsMenu:
        """
        Builds the scale options menu with relevant items.
        
                Returns:
                    OptionsMenu: The constructed scale options menu.
        """
    def _build_translate_menu(self) -> OptionsMenu:
        """
        Builds the translate options menu with relevant items.
        
                Returns:
                    OptionsMenu: The constructed translate options menu.
        """
    def _can_conform(self) -> bool:
        """
        Determines if any of the snap providers can orient.
        
                Returns:
                    bool: True if at least one provider can orient, otherwise False.
        """
    def _on_align_by_target_changed(self, value: bool) -> None:
        """
        Handles changes to the 'Align to Target' setting, enabling or disabling the 'Align by Axis' item.
        
                Args:
                    value (bool): The new value of the 'Align to Target' setting.
        """
    def _on_snap_targets_changed(self, *args, **kwargs):
        """
        Callback to update the UI based on changes in the snap targets settings.
        
                This method is called asynchronously to ensure that it processes changes
                only after all other events have been handled.
        """
    def _on_transform_op_changed(self, item, event_type):
        """
        Callback to handle changes in the transform operation settings.
        
                This method updates the visibility of the snap options menu based on the current
                transform operation. If a different snap options menu is open, it will be closed.
        
                Args:
                    item: The settings item that changed.
                    event_type: The type of the event that triggered the change.
        """
    def destroy(self, menu_only: bool = False):
        """
        Destroys the snap menu, cleaning up resources.
        
                Args:
                    menu_only (bool): If True, only destroy the menu components, not the subscriptions.
        """
    def get_options_menu(self, suffix: str | None = None) -> OptionsMenu | None:
        """
        Retrieves the options menu corresponding to the provided suffix.
        
                Args:
                    suffix (Optional[str]): A string representing the suffix for the options menu to retrieve.
        
                Returns:
                    Optional[OptionsMenu]: The requested options menu or None if not found.
        """
CONFORM_TO_TARGET_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/conformToTarget'
CONFORM_UP_AXIS_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/conformUpAxis'
KEEP_SPACING_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/keepSpacing'
MENU_SUFFIX_ROTATE: str = 'rotate'
MENU_SUFFIX_SCALE: str = 'scale'
MENU_SUFFIX_TRANSLATE: str = 'translate'
OP_TO_NAME: dict = {'move': 'translate', 'rotate': 'rotate', 'scale': 'scale'}
SNAP_ENABLED_SETTING: str = '/app/viewport/snapEnabled'
SNAP_PROVIDER_NAME_SETTING_PATH: str = '/exts/omni.kit.manipulator.tool.snap/providerNames'
SNAP_ROTATE_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/explicitTransform/rotate'
SNAP_SCALE_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/explicitTransform/scale'
SNAP_SETTING_PREFIX: str = '/persistent/exts/omni.kit.manipulator.tool.snap/explicitTransform/'
SNAP_TRANSLATE_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/explicitTransform/translate'
TRANSFORM_OP_SETTING: str = '/app/transform/operation'
