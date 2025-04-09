"""
Implementation of omni.kit.menu.common. This adds Help & Window menus.
"""
from __future__ import annotations
import omni as omni
from omni.kit.menu.common.legacy_help import HelpExtension
from omni.kit.menu.common.legacy_window import WindowExtension
__all__ = ['CommonMenuExtension', 'HelpExtension', 'WindowExtension', 'omni']
class CommonMenuExtension(omni.ext._extensions.IExt):
    """
    A class for managing common menu extensions.
    
        This class is responsible for initializing and shutting down legacy help and window extensions within the application. It extends the omni.ext.IExt interface and provides mechanisms to handle startup and shutdown events.
        
    """
    def __init__(self):
        """
        Initializes the CommonMenuExtension instance.
        """
    def on_shutdown(self):
        """
        Handles shutdown procedures for the extension.
        """
    def on_startup(self, ext_id):
        """
        Handles startup procedures for the extension.
        
                Args:
                    ext_id (str): The extension ID.
                
        """
