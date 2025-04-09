from __future__ import annotations
import abc as abc
import carb as carb
import omni as omni
from omni.kit.viewport.menubar.core.model.reset_button import ResetHelper
from omni import ui
__all__: list = ['SettingModel']
class AbstractSettingModelWithDefault(SettingModel, omni.kit.viewport.menubar.core.model.reset_button.ResetHelper):
    """
    
        Base class for setting model with default value and reset supported.
        
    """
    def __init__(self, setting_path: str, draggable: bool = False, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Path to carb setting.
        
                Keyword Args:
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                    min (Union[float, int, None]): Min value, defaults to None.
                    max (Union[float, int, None]): Max value, defaults to None.
                
        """
    def get_default(self) -> typing.Any:
        """
        Get default value
        """
    def get_value(self) -> typing.Any:
        """
        Get current value from carb setting
        """
    def on_value_changed(self):
        """
        Refresh reset button when value changed
        """
    def restore_default(self) -> None:
        """
        Restore default value
        """
class SettingModel(omni.ui._ui.AbstractValueModel):
    """
    
        A data model for simple scalar/POD carb.settings
    
        Taken from omni.kit.widget.settings
    
        TODO: Put it to omni.ui
        
    """
    @staticmethod
    def _on_change(owner, value, event_type) -> None:
        ...
    def __init__(self, setting_path: str, draggable: bool = False, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Path to carb setting.
        
                Keyword Args:
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                    min (Union[float, int, None]): Min value, defaults to None.
                    max (Union[float, int, None]): Max value. defaults to None.
                
        """
    def _cast_to_type(self, value: typing.Any, dflt: typing.Any, type_cast: type = None):
        ...
    def _on_dirty(self):
        ...
    def begin_edit(self) -> None:
        """
        Called when the user starts editing.
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
    def end_edit(self) -> None:
        """
        Called when the user finishes editing.
        """
    def get_value_as_bool(self) -> bool:
        """
        Get value as bool
        """
    def get_value_as_float(self) -> float:
        """
        Get value as float
        """
    def get_value_as_int(self) -> int:
        """
        Get value as int
        """
    def get_value_as_string(self) -> str:
        """
        Get value as string
        """
    def on_value_changed(self) -> None:
        """
        Callback when value changed
        """
    def set_value(self, value: typing.Any) -> None:
        """
        
                Set value.
        
                Args:
                    value (Any): Value to set.
                
        """
    @property
    def path(self) -> str:
        """
        Path to carb setting
        """
class SettingModelWithDefaultPath(AbstractSettingModelWithDefault):
    """
    
        A setting model to get default value from carb setting path and save/load persistent.
    
        Setting path starts with PERSISTENT_SETTINGS_PREFIX to save/load current value
        Setting path without PERSISTENT_SETTINGS_PREFIX for default value when reset
        
    """
    def __init__(self, setting_path: str, draggable: bool = False, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Path to carb setting.
        
                Keyword Args:
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                    min (Union[float, int, None]): Min value, defaults to None.
                    max (Union[float, int, None]): Max value, defaults to None.
                
        """
    def get_default(self):
        """
        Get Default value
        """
    def restore_default(self) -> None:
        """
        Restore default value
        """
class SettingModelWithDefaultValue(AbstractSettingModelWithDefault):
    """
    
        A setting model with default value.
        
    """
    def __init__(self, setting_path: str, default_value: typing.Any, draggable: bool = False, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Path to carb setting.
                    default_value (Any): Default value.
        
                Keyword Args:
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                    min (Union[float, int, None]): Min value, defaults to None.
                    max (Union[float, int, None]): Max value, defaults to None.
                
        """
    def get_default(self):
        """
        Get default value
        """
    def restore_default(self) -> None:
        """
        Restore default value
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
