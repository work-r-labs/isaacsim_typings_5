"""
This module defines the CreateMenuExtension class to enhance the 'Create' menu in Omniverse Kit, adding menu items for creating various types of primitives and handling their associated actions.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.menu.create.create_actions import _get_action_name
from omni.kit.menu.create.create_actions import deregister_actions
from omni.kit.menu.create.create_actions import register_actions
from omni.kit.menu.utils.app_menu import MenuItemOrder
from omni.kit.menu.utils.builder_utils import MenuItemDescription
import os as os
__all__: list = ['get_action_name', 'CreateMenuExtension', 'rebuild_menus']
class CreateMenuExtension(omni.ext._extensions.IExt):
    """
    A class designed to extend Omniverse Kit's menu capabilities, specifically for creating various types of primitives.
    
        This class manages the creation and organization of menu items related to creating different types of primitives, such as shapes, lights, audio sources, cameras, and more. It dynamically builds a 'Create' menu based on settings and available options, allowing users to quickly access tools for adding new elements into their scene. The class also handles custom actions for creating these items with specific attributes or settings.
        
    """
    @staticmethod
    def on_create_light(light_type, attributes):
        """
        Executes the command to create a light with the specified type and attributes.
        
                Args:
                    light_type (str): The type of the light to create.
                    attributes (dict): The attributes to apply to the light.
        """
    @staticmethod
    def on_create_prim(prim_type, attributes, use_settings: bool = False):
        """
        Executes the command to create a primitive with the specified type and attributes.
        
                Args:
                    prim_type (str): The type of the primitive to create.
                    attributes (dict): The attributes to apply to the primitive.
                    use_settings (bool, optional): Whether to use the settings for the primitive creation. Defaults to False.
        """
    @staticmethod
    def on_create_prims():
        """
        Executes the command to create a set of predefined primitives.
        """
    def __init__(self):
        """
        Initializes the CreateMenuExtension and sets the default menu priority for the 'Create' menu.
        """
    def _build_create_menu(self):
        ...
    def _high_quality_option_toggle(self):
        ...
    def _rebuild_menus(self):
        ...
    def on_shutdown(self):
        """
        Called when the extension shuts down. Deregisters actions and removes the 'Create' menu items.
        """
    def on_startup(self, ext_id):
        """
        Called when the extension starts up. Registers actions and builds the create menu.
        
                Args:
                    ext_id (str): The ID of the extension that is starting up.
        """
def get_extension_path(sub_directory):
    """
    Retrieves the full path to a specified subdirectory within the extension's directory.
    
        Args:
            sub_directory (str): The name of the subdirectory within the extension's directory. If empty, returns the path to the extension's root directory.
    
        Returns:
            str: The normalized full path to the specified subdirectory within the extension's directory.
    """
def rebuild_menus():
    """
    Rebuilds the 'Create' menu in the extension.
    
        This function will trigger a rebuild of the 'Create' menu, ensuring that any
        changes in menu items or settings are reflected in the user interface. It is
        called when external changes necessitate a refresh of the menu structure.
        
    """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
_extension_instance: CreateMenuExtension  # value = <omni.kit.menu.create.create.CreateMenuExtension object>
_extension_path: str = '/home/chris/isaacsim/extscache/omni.kit.menu.create-1.0.17+d02c707b'
