from __future__ import annotations
import carb as carb
from carb.eventdispatcher import get_eventdispatcher
import omni as omni
from omni.kit.property.usd.attribute_context_menu import AttributeContextMenu
from omni.kit.property.usd.control_state_manager import ControlStateManager
from omni.kit.property.usd.prim_path_widget import PrimPathWidget
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.usd_style import Styles
from omni import ui
import pathlib
from pathlib import Path
from pxr import Sdf
from pxr import UsdGeom
import weakref as weakref
__all__: list = list()
class Examples:
    """
    
        Examples of showing how to use PropertyWindow APIs.
        
    """
    def __del__(self):
        """
        
                Deletes the examples.
                
        """
    def __init__(self, w):
        """
        
                Initializes the examples.
        
                Args:
                    w: The property window.
                
        """
    def clean(self, w):
        """
        
                Cleans the examples.
        
                Args:
                    w: The property window.
                
        """
class SelectionNotifier:
    """
    
        A class to represent the selection notifier.
        
    """
    def __init__(self, usd_context_id = '', property_window_context_id = ''):
        """
        
                Initializes the selection notifier.
        
                Args:
                    usd_context_id: The USD context ID.
                    property_window_context_id: The property window context ID.
                
        """
    def _keep_scroll_pos(self, w, old_payload, new_payload):
        ...
    def _notify_property_window(self, save_scroll_pos: bool = False):
        """
        
                Notifies the property window.
        
                Args:
                    save_scroll_pos: Whether to save the scroll position.
                
        """
    def _on_selection_changed(self):
        """
        Handles stage selection changed event
        """
    def _on_stage_closing(self):
        """
        Handles stage closing or closed
        """
    def notify_property_window(self, save_scroll_pos: bool = False):
        """
        
                Notifies the property window.
        
                Args:
                    save_scroll_pos: Whether to save the scroll position.
                
        """
    def start(self):
        """
        
                Starts the selection notifier.
                
        """
    def stop(self):
        """
        
                Stops the selection notifier.
                
        """
class UsdPropertyWidgets(omni.ext._extensions.IExt):
    """
    A class that extends the OmniKit extension interface to provide USD property widgets.
    
        UsdPropertyWidgets is responsible for managing the registration and unregistration of various USD related widgets in the OmniKit application. It utilizes a selection notification system to update property windows when USD stage selection changes occur. This class also handles startup and shutdown logic for USD property widgets, ensuring that preferences and widgets are appropriately registered or unregistered with the application. It interacts with other custom classes, such as AttributeContextMenu and ControlStateManager, to offer a comprehensive user interface for USD property manipulation.
        
    """
    def __init__(self):
        """
        Initializes the USD Property Widgets extension.
        """
    def _register_preferences(self):
        ...
    def _register_widget(self):
        ...
    def _unregister_preferences(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        """
        Method called when the extension is shutting down.
        """
    def on_startup(self, ext_id):
        """
        Method called when the extension starts up.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
EXTENSION_PATH: str = '/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.property.usd-4.5.11+8131b85d'
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.property.usd-4.5.11+8131b85d/data/icons')
SHOW_PREFERENCES_PATH: str = '/exts/omni.kit.property.usd/show_prefs'
