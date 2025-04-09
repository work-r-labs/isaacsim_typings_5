from __future__ import annotations
import omni as omni
from omni.kit.manipulator.prim.core.global_registry import get_prim_data_accessor_registry
from omni.kit.manipulator.prim.usd.data_accessor import UsdDataAccessor
__all__ = ['ManipulatorPrim2UsdExt', 'UsdDataAccessor', 'get_prim_data_accessor_registry', 'omni']
class ManipulatorPrim2UsdExt(omni.ext._extensions.IExt):
    """
    A class for registering and unregistering a USD data accessor.
    
        This class extends the `omni.ext.IExt` interface and is used to integrate a USD data accessor into the global registry. It handles the lifecycle of the USD data accessor by registering it on startup and unregistering it on shutdown.
        
    """
    def on_shutdown(self):
        """
        Cleans up the extension by unregistering the data accessor and resetting the registry.
        """
    def on_startup(self, ext_id):
        """
        Initializes the extension with a specific extension identifier.
        
                Args:
                    ext_id (str): The identifier for the extension being started.
        """
