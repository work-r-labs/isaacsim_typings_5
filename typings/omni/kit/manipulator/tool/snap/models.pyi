from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
__all__ = ['SettingModel', 'carb', 'ui']
class SettingModel(omni.ui._ui.AbstractValueModel):
    """
    A UI model for synchronizing with application settings.
    
        This model tracks a specific setting within the application and updates its value based on changes to that setting. It allows for the setting's value to be updated both in the UI and the application settings, ensuring synchronization between the two.
    
        Args:
            setting_path: str
                The path to the setting which this model will represent.
    """
    def __del__(self):
        """
        Automatic destructor that calls the destroy method upon deletion.
        """
    def __init__(self, setting_path: str):
        """
        Initializes the SettingModel object.
        
                Args:
                    setting_path (str): The path to the setting which this model will represent.
        """
    def _on_change(self, item, event_type):
        """
        Internal callback for when the subscribed setting changes.
        
                Args:
                    item: The item that has changed.
                    event_type: The type of change event that has occurred.
        """
    def destroy(self):
        """
        Unsubscribes from setting change events and cleans up resources.
        """
    def get_value_as_bool(self) -> bool:
        """
        Returns the current value of the setting as a boolean.
        
                Returns:
                    bool: The boolean representation of the setting value.
        """
    def get_value_as_float(self) -> float:
        """
        Returns the current value of the setting as a float.
        
                Returns:
                    float: The float representation of the setting value.
        """
    def set_value(self, value):
        """
        Sets the value of the setting.
        
                Args:
                    value: The new value to set for the setting.
        """
