"""
This module provides an extension for adding audio property functionalities to Omniverse Kit applications.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.audio.scripts.audio_settings_widget import AudioSettingsWidget
from pxr import UsdMedia
__all__ = ['AudioPropertyExtension', 'AudioSettingsWidget', 'UsdMedia', 'omni']
class AudioPropertyExtension(omni.ext._extensions.IExt):
    """
    A class designed to extend Omniverse Kit applications with audio property functionalities.
    
        This extension class manages the registration and unregistration of custom widgets related to audio properties within the Omniverse Kit property window. It extends the 'omni.ext.IExt' interface, which allows it to integrate seamlessly into the Omniverse extension system. Upon startup, it registers widgets for handling media, sound, and audio listener properties, and provides a dedicated audio settings layer. It cleans up by unregistering these widgets upon shutdown.
        
    """
    def __init__(self):
        """
        Constructor for AudioPropertyExtension.
        """
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        """
        Cleans up resources and unregisters widgets when the extension is shutting down.
        """
    def on_startup(self, ext_id):
        """
        Initializes extension and sets up necessary paths.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
