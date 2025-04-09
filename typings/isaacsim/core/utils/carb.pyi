from __future__ import annotations
import carb as carb
__all__ = ['carb', 'get_carb_setting', 'set_carb_setting']
def get_carb_setting(carb_settings: carb.settings._settings.ISettings, setting: str) -> typing.Any:
    """
    Convenience function to get settings.
    
        Args:
            carb_settings (carb.settings.ISettings): The interface to carb settings.
            setting (str): Name of setting to change.
    
        Returns:
            Any: Value for the setting.
    
        Example:
    
        .. code-block:: python
    
            >>> import carb
            >>> import isaacsim.core.utils.carb as carb_utils
            >>>
            >>> settings = carb.settings.get_settings()
            >>> carb_utils.get_carb_setting(settings, "/physics/updateToUsd")
            False
        
    """
def set_carb_setting(carb_settings: carb.settings._settings.ISettings, setting: str, value: typing.Any) -> None:
    """
    Convenience to set the carb settings.
    
        Args:
            carb_settings (carb.settings.ISettings): The interface to carb settings.
            setting (str): Name of setting to change.
            value (Any): New value for the setting.
    
        Raises:
            TypeError: If the type of value does not match setting type.
    
        Example:
    
        .. code-block:: python
    
            >>> import carb
            >>> import isaacsim.core.utils.carb as carb_utils
            >>>
            >>> settings = carb.settings.get_settings()
            >>> carb_utils.set_carb_setting(settings, "/physics/updateToUsd", True)
        
    """
