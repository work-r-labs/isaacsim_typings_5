from __future__ import annotations
import gc as gc
import omni as omni
from omni.isaac.dynamic_control import _dynamic_control
__all__ = ['EXTENSION_NAME', 'Extension', 'gc', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
EXTENSION_NAME: str = 'Dynamic Control'
