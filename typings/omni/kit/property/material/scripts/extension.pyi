"""
This module defines the MaterialPropertyExtension which extends the OmniKit Editor by managing custom UI widgets for editing USD shade attributes and materials.
"""
from __future__ import annotations
import omni as omni
__all__: list = ['MaterialPropertyExtension']
class MaterialPropertyExtension(omni.ext._extensions.IExt):
    """
    A class that extends the OmniKit Editor by registering and managing custom widgets related to material properties.
    
        This extension is responsible for adding custom UI elements to the Properties Window within the OmniKit environment, specifically tailored for editing USD shade attributes and materials. It ensures the proper registration and unregistration of these widgets during the extension's startup and shutdown lifecycle events.
        
    """
    def __init__(self):
        """
        Initializes the extension and sets up necessary properties.
        """
    def _register_widgets(self, ext_id):
        ...
    def _unregister_widgets(self):
        ...
    def on_shutdown(self):
        """
        Called when the extension is being shut down.
        """
    def on_startup(self, ext_id):
        """
        Called when the extension is started.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
