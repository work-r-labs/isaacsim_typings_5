"""
This module provides the LightPropertyExtension class for adding a custom light properties widget to the Omniverse Kit.
"""
from __future__ import annotations
import omni as omni
from pxr import Usd
from pxr import UsdLux
__all__ = ['LightPropertyExtension', 'Usd', 'UsdLux', 'omni']
class LightPropertyExtension(omni.ext._extensions.IExt):
    """
    A class that extends the Omniverse Kit by registering a custom widget for light properties.
    
        This class is an extension for the Omniverse Kit, designed to enhance the user interface by adding a custom widget that allows for easy manipulation of light properties in a 3D scene. It leverages USD and UsdLux for defining and managing these properties. Upon startup, the class registers the widget and sets up a path for test data. On shutdown, it ensures the widget is properly unregistered.
    
        It is important to note that the visibility of this widget is contingent on the presence of the property window within the Omniverse Kit. The widget is specifically tailored for light primitives and includes a comprehensive set of light attributes for various light types supported by UsdLux. The class also handles version-specific features of USD, ensuring compatibility across different versions of the software.
        
    """
    def __init__(self):
        """
        Initializes the LightPropertyExtension.
        """
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        """
        Cleans up resources and unregisters widgets before the extension shuts down.
        """
    def on_startup(self, ext_id):
        """
        This method is called when the extension is started.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
