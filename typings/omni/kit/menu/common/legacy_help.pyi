from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput as Key
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
import webbrowser as webbrowser
__all__: list = ['HelpExtension']
class HelpExtension:
    """
    A class to manage help menu actions and items.
    
        This class is responsible for registering and managing help-related
        menu items and their associated actions within the application.
        It dynamically configures menu items based on application settings
        and provides functionalities to open various documentation URLs.
    
        
    """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the HelpExtension and sets up help menu items.
        """
    def _deregister_actions(self, extension_id):
        ...
    def _register_actions(self, extension_id, discover_reference_guide_path, discover_kit_sdk_path, manual_url_path):
        ...
