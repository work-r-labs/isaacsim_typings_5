"""
This module extends the Omniverse Kit editor with enhanced file operation capabilities, including handling recent files, saving and opening scenes, and managing USD stage events.
"""
from __future__ import annotations
import carb as carb
from isaacsim.gui.menu.file_menu.file_actions import deregister_actions
from isaacsim.gui.menu.file_menu.file_actions import register_actions
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.helper.file_utils import get_latest_urls_from_event_queue
from omni.kit.menu.utils.app_menu import IconMenuDelegate
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
import os as os
import urllib as urllib
__all__: list = ['FileMenuDelegate', 'FileMenuExtension']
class FileMenuDelegate(omni.kit.menu.utils.app_menu.IconMenuDelegate):
    """
    A delegate class for customizing the appearance and behavior of the File menu.
    
        This class provides methods to determine the length of displayed text in the menu, specifically
        for the 'Open Recent' menu, allowing for an ellipsis to be used on longer file paths.
    """
    def get_elided_length(self, menu_name):
        """
        Determines the maximum pixel width of text that can be displayed for a given menu.
        
                Args:
                    menu_name (str): The name of the menu to check for text elision.
        
                Returns:
                    int: The maximum pixel width of the text allowed in the menu or 0 if no limit.
        """
class FileMenuExtension:
    """
    A class that extends the Omniverse Kit editor with file menu functionalities.
    
        This class provides enhanced file operation capabilities within the Omniverse Kit editor's file menu, including the ability to handle recent files, save and open scenes, and manage USD stage events. It is responsible for registering file actions, constructing the file menu, and updating the recent files list based on file events.
        
    """
    @staticmethod
    def can_close():
        """
        Checks if the USD stage is in a state where it can be closed.
        
                Returns:
                    bool: True if the stage can be closed, False otherwise.
        """
    @staticmethod
    def can_close_and_not_is_new_stage():
        """
        Checks if the USD stage can be closed and is not a new, unsaved stage.
        
                Returns:
                    bool: True if the stage can be closed and is not new, False otherwise.
        """
    @staticmethod
    def can_open():
        """
        Checks if the USD stage is in a state where it can be opened.
        
                Returns:
                    bool: True if the stage can be opened, False otherwise.
        """
    @staticmethod
    def can_save():
        """
        Checks if the USD stage is in a state where it can be saved.
        
                Returns:
                    bool: True if the stage can be saved, False otherwise.
        """
    @staticmethod
    def is_new_stage():
        """
        Determines if the current USD stage is a new, unsaved stage.
        
                Returns:
                    bool: True if the stage is new and unsaved, False otherwise.
        """
    def __del__(self):
        ...
    def __init__(self, ext_id = ''):
        ...
    def _build_file_menu(self):
        ...
    def _build_recent_menu(self):
        ...
    def _build_sample_menu(self):
        ...
    def _on_stage_event(self, event):
        ...
def get_extension_path(sub_directory):
    """
    
        Returns the normalized path by joining the given sub-directory with the extension's base path.
    
        Args:
            sub_directory (str): The sub-directory to append to the base path of the extension. If empty, the base path is returned as is.
    
        Returns:
            str: The normalized path combining the extension's base path with the provided sub-directory.
        
    """
FILE_EVENT_QUEUE_UPDATED: int = 4806079216508642737
INTERACTIVE_TEXT: str = 'shade:4291137818'
_extension_instance: FileMenuExtension  # value = <isaacsim.gui.menu.file_menu.file_menu.FileMenuExtension object>
_extension_path: str = '/home/chris/isaacsim/exts/isaacsim.gui.menu'
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
