from __future__ import annotations
import carb as carb
import omni as omni
import os as os
__all__: list[str] = ['Extension', 'carb', 'omni', 'os']
class Extension(omni.ext._extensions.IExt):
    def _authenticate(self, prefix):
        """
        Authentication callback for Omniverse client.
        
                Args:
                    prefix: URL prefix for authentication.
        
                Returns:
                    tuple: (username, password) if credentials are available, None otherwise.
                
        """
    def on_shutdown(self):
        """
        Clean up resources when the extension is shut down.
        """
    def on_startup(self, ext_id):
        """
        Initialize the extension.
        
                Args:
                    ext_id: The extension ID.
                
        """
