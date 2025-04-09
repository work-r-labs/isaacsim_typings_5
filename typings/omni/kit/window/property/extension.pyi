"""

omni.kit.window.property PropertyExtension class.
"""
from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenu
from omni.kit.window.property.window import PropertyWindow
from omni import ui
import pathlib
from pathlib import Path
import typing
import weakref as weakref
__all__: list = ['get_window', 'PropertyExtension', 'PropertyWindow']
class PropertyExtension(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    """
    Property window extension class.
    """
    MENU_GROUP: typing.ClassVar[str] = 'Window'
    WINDOW_NAME: typing.ClassVar[str] = 'Property'
    def __init__(self):
        """
        Initialize PropertyExtension
        """
    def _visiblity_changed_fn(self, visible):
        ...
    def on_shutdown(self):
        """
        Shutdown function
        """
    def on_startup(self, ext_id):
        """
        Startup function
        
                Args:
                    ext_id (str): Extension id.
                
        """
    def show_window(self, value: bool):
        """
        Show/hide property window function
        
                Args:
                    value (bool): True if window will be shown or False if window will be hidden.
                
        """
def get_window():
    """
    Get property window.
    """
TEST_DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.property-1.11.5+d02c707b/data/tests')
_property_window_instance: weakref.ReferenceType  # value = <weakref at 0x709fe542ebb0; to 'PropertyWindow' at 0x709fe54b09d0>
