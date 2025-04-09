from __future__ import annotations
import carb as carb
import omni as omni
__all__ = ['Extension', 'carb', 'omni']
class Extension(omni.ext._extensions.IExt):
    """
    Renderer capture extension
    """
    def on_shutdown(self):
        """
        Called when the extension is shut down.
        """
    def on_startup(self):
        """
        Called when the extension is started up.
        """
