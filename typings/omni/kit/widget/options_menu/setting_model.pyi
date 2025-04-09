"""
This module defines a custom UI value model for observing and interacting with application settings.
"""
from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
__all__ = ['SettingModel', 'carb', 'ui']
class SettingModel(omni.ui._ui.AbstractValueModel):
    """
    A value model that is reimplemented in Python to watch a setting path.
    
        This model is responsible for observing a specific setting and notifying subscribers about any changes to the setting's value.
    
            Args:
                setting_path (str): The path of the setting to be monitored.
    """
    def __init__(self, setting_path: str):
        """
        Initializes the SettingModel.
        """
    def _on_change(self, item, event_type):
        ...
    def destroy(self):
        """
        Cleans up resources and subscriptions.
        """
    def get_value_as_bool(self):
        """
        Returns the setting value as a boolean.
        """
    def get_value_as_float(self):
        """
        Returns the setting value as a float.
        """
    def get_value_as_int(self):
        """
        Returns the setting value as an integer.
        """
    def get_value_as_string(self):
        """
        Returns the setting value as a string.
        """
    def set_value(self, value):
        """
        Updates the setting with a new value.
        
                Args:
                    value: The new value to set.
        """
