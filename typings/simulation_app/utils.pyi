from __future__ import annotations
import carb as carb
from omni.kit.usd import layers
import typing
__all__ = ['carb', 'create_new_stage', 'is_stage_loading', 'layers', 'open_stage', 'save_stage', 'set_carb_setting', 'set_livesync_stage']
def create_new_stage() -> Usd.Stage:
    """
    [summary]
    
        Returns:
            bool: [description]
        
    """
def is_stage_loading() -> bool:
    """
    
        bool: Convenience function to see if any files are being loaded. True if loading, False otherwise
        
    """
def open_stage(usd_path: str) -> bool:
    """
    
        Open the given usd file and replace currently opened stage
        Args:
            usd_path (str): Path to open
        
    """
def save_stage(usd_path: str) -> bool:
    """
    
        Save usd file to path, it will be overwritten with the current stage
        Args:
            usd_path (str): Path to save the current stage to
        
    """
def set_carb_setting(carb_settings: carb.settings.ISettings, setting: str, value: typing.Any) -> None:
    """
    Convenience function to set settings.
    
        Arguments:
            setting (str): Name of setting to change.
            value (Any): New value for the setting.
    
        Raises:
            TypeError: If the type of value does not match setting type.
        
    """
def set_livesync_stage(usd_path: str, enable: bool) -> bool:
    """
    [summary]
    
        Args:
            usd_path (str): path to enable live sync for, it will be overwritten with the current stage
            enable (bool): True to enable livesync, false to disable livesync
    
        Returns:
            bool: [description]
        
    """
