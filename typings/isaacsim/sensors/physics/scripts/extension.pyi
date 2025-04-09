from __future__ import annotations
import gc as gc
from isaacsim.sensors.physics import _sensor
import omni as omni
__all__ = ['EXTENSION_NAME', 'Extension', 'gc', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
EXTENSION_NAME: str = 'Isaac Sensor'
