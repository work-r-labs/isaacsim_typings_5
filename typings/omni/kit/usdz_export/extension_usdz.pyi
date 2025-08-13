from __future__ import annotations
from carb.eventdispatcher import get_eventdispatcher
import omni as omni
from omni.kit.usdz_export.layers_menu import LayersMenu
from omni.kit.usdz_export.layers_menu import layers_available
__all__: list[str] = ['LayersMenu', 'UsdzExportExtension', 'get_eventdispatcher', 'layers_available', 'omni']
class UsdzExportExtension(omni.ext._extensions.IExt):
    """
    Extension for handling USDZ export operations in Omni UI.
    
        This extension subscribes to global events to monitor script and folder changes. It manages the lifecycle of a layers menu used for USDZ export. On startup, the extension registers event listeners that trigger the creation or destruction of the layers menu based on the current availability of layers. When layers are available, it creates an instance of the layers menu; when they are not, it destroys any existing instance.
    
        On shutdown, the extension removes the event subscriptions and ensures that the layers menu is properly cleaned up. This allows the USDZ export functionality to adapt dynamically to changes in the workspace state.
        
    """
    def _on_event(self, _):
        ...
    def on_shutdown(self):
        """
        Handles extension shutdown. Clears event subscriptions and destroys Layers menu if it exists.
        """
    def on_startup(self, ext_id):
        """
        Handles extension startup. Sets up event callbacks for global events and initializes Layers menu state.
        
                Args:
                    ext_id (str): Extension identifier.
                
        """
