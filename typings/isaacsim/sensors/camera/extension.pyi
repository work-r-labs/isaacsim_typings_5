from __future__ import annotations
import omni as omni
__all__ = ['EXTENSION_NAME', 'Extension', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
EXTENSION_NAME: str = 'Isaac Sensor'
