from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.prim.core.global_registry import get_prim_data_accessor_registry
from omni.kit.manipulator.prim.fabric.data_accessor import FabricDataAccessor
__all__: list = ['ManipulatorPrim2FabricExt']
class ManipulatorPrim2FabricExt(omni.ext._extensions.IExt):
    """
    An extension class for manipulating primitive to Fabric data accessor registration.
    
        This class implements the `omni.ext.IExt` interface and is responsible for managing the
        registration and unregistration of a Fabric data accessor based on application settings.
        It watches for changes in the application's usage of the Fabric Scene Delegate and
        updates the registration status of the data accessor accordingly.
    """
    def _on_fabric_delegate_changed(self, value: str, event_type: carb.settings._settings.ChangeEventType):
        ...
    def on_shutdown(self):
        """
        Shuts down the extension and cleans up resources.
        """
    def on_startup(self, ext_id):
        """
        Initializes the extension with the given extension ID.
        
                Args:
                    ext_id (str): The unique identifier for the extension.
        """
    def register_data_accessor(self):
        """
        Registers the Fabric data accessor with the global registry.
        """
    def unregister_data_accessor(self):
        """
        Unregisters the Fabric data accessor from the global registry.
        """
