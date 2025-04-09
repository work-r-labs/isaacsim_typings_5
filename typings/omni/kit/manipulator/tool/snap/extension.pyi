from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.tool.snap.hotkey import SnapHotkey
from omni.kit.manipulator.tool.snap.menu import SnapMenu
from omni.kit.manipulator.tool.snap.provider import SnapProvider
from omni.kit.manipulator.tool.snap.registry import RegistrationHelper
from omni.kit.manipulator.tool.snap.registry import SnapProviderRegistry
import traceback as traceback
__all__ = ['LEGACY_SNAP_BUTTON_ENABLED_SETTING_PATH', 'RegistrationHelper', 'SnapHotkey', 'SnapMenu', 'SnapProvider', 'SnapProviderRegistry', 'SnapToolExt', 'carb', 'n', 'omni', 'traceback']
class SnapToolExt(omni.ext._extensions.IExt):
    """
    An extension for enabling and managing snap tools in the application.
    
        This class is responsible for the initialization, management, and cleanup of snap tools. It registers and unregisters toolbar buttons, handles hotkeys, and sets up the necessary providers and menus for the snap tool functionality.
        
    """
    def _register_main_toolbar_button(self):
        """
        Registers the main toolbar button for the snap tool.
        
                This private method creates and adds the snap button group to the main toolbar.
                It also handles the state of the legacy snap button.
        """
    def _unregister_main_toolbar_button(self):
        """
        Unregisters the main toolbar button for the snap tool.
        
                This private method removes the snap button group from the main toolbar and restores
                the state of the legacy snap button if it was enabled prior to the registration of
                this tool.
        """
    def on_shutdown(self):
        """
        Cleans up the snap tool extension.
        
                This method unsubscribes from extension hooks, and destroys the snap button group,
                registration helper, snap menu, hotkey, and registry if they exist.
        """
    def on_startup(self, ext_id):
        """
        Initializes the snap tool extension.
        
                This method sets up the snap provider registry, registration helper, snap menu, hotkey,
                and hooks for the toolbar button.
        
                Args:
                    ext_id (str): The identifier for the extension.
        """
LEGACY_SNAP_BUTTON_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/legacySnapButton/enabled'
n: str = 'omni.kit.manipulator.tool.snap.builtin_snap_tools'
