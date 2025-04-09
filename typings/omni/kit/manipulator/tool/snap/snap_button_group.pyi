from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.tool.snap.menu import SnapMenu
from omni.kit.manipulator.tool.snap.models import SettingModel
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import pathlib
from pathlib import Path
__all__ = ['ICON_FOLDER_PATH', 'Path', 'SNAP_ENABLED_SETTING', 'SNAP_TOOL_NAME', 'SettingModel', 'SnapButtonGroup', 'SnapMenu', 'WidgetGroup', 'carb', 'omni', 'ui']
class SnapButtonGroup(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    """
    A class that represents a group of buttons for snap functionality in a UI toolbar.
    
        This class is responsible for creating and managing a UI button that interacts with the snap settings and functionality. It utilizes a SnapMenu to provide additional options and settings for the snap tool.
    
        Args:
            hotkey: str
                The key combination used to activate the snap functionality.
            menu: SnapMenu
                An instance of the SnapMenu class that provides additional options for the snap tool.
    """
    def __del__(self):
        ...
    def __init__(self, hotkey, menu: omni.kit.manipulator.tool.snap.menu.SnapMenu):
        """
        Initializes the SnapButtonGroup with a hotkey and a SnapMenu.
        
                Args:
                    hotkey: The hotkey associated with the snap functionality.
                    menu (SnapMenu): An instance of the SnapMenu to be used with the button group.
        """
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        Invokes the context menu for the given button id.
        
                Args:
                    button_id (str): The identifier of the button for which to invoke the context menu.
                    min_menu_entries (int, optional): The minimum number of menu entries required for the menu to be visible. Defaults to 1.
                
        """
    def clean(self):
        """
        Cleans up the SnapButtonGroup by destroying the snap setting model.
        """
    def create(self, default_size):
        """
        Creates the UI tool button for the snap functionality with the specified default size.
        
                Args:
                    default_size (int): The default width and height for the button.
        
                Returns:
                    dict: A dictionary containing the created ui.ToolButton with 'snap' as the key.
        """
    def get_button(self) -> omni.ui._ui.ToolButton:
        """
        Retrieves the UI tool button associated with the snap functionality.
        
                Returns:
                    ui.ToolButton: The UI tool button instance.
        """
    def get_style(self):
        """
        Returns the style of the snap button.
        
                Returns:
                    dict: A dictionary representing the style of the snap button.
        """
ICON_FOLDER_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.manipulator.tool.snap-1.5.12+d02c707b/data/icons')
SNAP_ENABLED_SETTING: str = '/app/viewport/snapEnabled'
SNAP_TOOL_NAME: str = 'Snap'
