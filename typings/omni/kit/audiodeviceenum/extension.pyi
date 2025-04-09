from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
__all__ = ['asyncio', 'carb', 'omni']
class _AudioExtension(omni.ext._extensions.IExt):
    """
    
        Extension startup and shutdown event handler.  This handles installing and removing the audio
        preferences page from the app's main preferences window when this extension loads and unloads.
        
    """
    def __init__(self):
        ...
    def _register_page(self):
        ...
    def _unregister_page(self):
        ...
    def on_shutdown(self):
        """
        
                Extension shutdown callback function.  This is called automatically when the Python side of
                this extension unloads.  This will always attempt to remove the audio preferences page.  This
                operation will be ignored if the page was not originally installed.
                
        """
    def on_startup(self, ext_id):
        """
        
                Extension startup callback function.  This is called automatically when the Python side of
                this extension loads.  If enabled, the audio preferences page will be installed when this
                extension is later enabled (usually happens automatically after extension load).  The audio
                preferences page will be removed when this extension is unloaded or disabled.
        
                Args:
                    ext_id: The ID of this extension.  This will be a string containing the extension's name
                            and version.
                
        """
