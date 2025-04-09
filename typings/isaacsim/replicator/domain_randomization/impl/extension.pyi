from __future__ import annotations
import omni as omni
__all__ = ['Extension', 'omni']
class Extension(omni.ext._extensions.IExt):
    """
    Object that tracks the lifetime of the Python part of the extension loading
    """
    def on_shutdown(self):
        """
        Shutting down this part of the extension prepares it for hot reload
        """
    def on_startup(self):
        """
        Set up initial conditions for the Python part of the extension
        """
