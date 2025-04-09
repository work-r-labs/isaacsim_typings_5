"""
Transform manipulator extension
"""
from __future__ import annotations
import omni as omni
from omni.kit.manipulator.transform.style import get_default_style
__all__ = ['SHOW_EXAMPLE', 'TransformManipulatorExt', 'get_default_style', 'omni']
class TransformManipulatorExt(omni.ext._extensions.IExt):
    """
    A class that represents the Transform Manipulator Extension.
    
        This class handles the lifecycle of the transform manipulator extension by defining startup and shutdown behaviors.
        
    """
    def on_shutdown(self):
        """
        Performs cleanup operations as the extension shuts down.
        """
    def on_startup(self, ext_id):
        """
        Initializes the extension.
        
                Args:
                    ext_id (str): The ID of the current extension used with the extension manager.
                
        """
SHOW_EXAMPLE: bool = False
