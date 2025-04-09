"""
This module defines the LocalGlobalModeModel class for managing and interacting with local and global operation space settings in a UI context.
"""
from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import typing
__all__ = ['LocalGlobalModeModel', 'carb', 'ui']
class LocalGlobalModeModel(omni.ui._ui.AbstractValueModel):
    """
    A model for managing local and global operation space settings.
    
        This class extends `omni.ui.AbstractValueModel` and provides mechanisms to interact with
        operation space settings, allowing the user to switch between local and global transform modes.
        It subscribes to changes in operation space settings and updates the internal state accordingly.
    
        Args:
            op_space_setting_path (str): The path to the operation space setting in the application settings.
        
    """
    TRANSFORM_MODE_GLOBAL: typing.ClassVar[str] = 'global'
    TRANSFORM_MODE_LOCAL: typing.ClassVar[str] = 'local'
    def __del__(self):
        ...
    def __init__(self, op_space_setting_path):
        """
        Initializes the LocalGlobalModeModel with operational space setting path.
        """
    def _on_op_space_changed(self, item, event_type):
        ...
    def destroy(self):
        """
        Cleans up resources and subscriptions.
        """
    def get_value_as_bool(self):
        """
        Determines if the operational space is set to global mode.
        
                Returns:
                    bool: True if the operational space is global, False if local.
        """
    def set_value(self, value):
        """
        Sets the operational space mode based on a boolean value.
        
                Args:
                    value (bool): True to set global mode, False for local mode.
        """
