from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.window.console.scripts.console_window import ConsoleWindow
from omni import ui
import typing
__all__: list = ['ConsoleExtension', 'get_instance']
class ConsoleExtension(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    """
    The entry point for Console Window
    
        This class handles the initialization and management of the Console Window in the application. It integrates with the UI workspace to show or hide the window based on user actions and settings.
        
    """
    MENU_GROUP: typing.ClassVar[str] = 'Window'
    WINDOW_NAME: typing.ClassVar[str] = 'Console'
    def _destroy_window_async(self):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def show_window(self, value):
        """
        Shows or hides the console window.
        
                Args:
                    value (bool): Whether to show the window.
                
        """
def get_instance():
    ...
STARTUP_SHOW_WINDOW: str = '/exts/omni.kit.window.console/startup/show_window'
_extension_instance: ConsoleExtension  # value = <omni.kit.window.console.scripts.console_extension.ConsoleExtension object>
