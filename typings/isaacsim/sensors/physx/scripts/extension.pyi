from __future__ import annotations
from isaacsim.sensors.physx import _range_sensor
from isaacsim.sensors.physx.scripts.proximity_sensor import ProximitySensorManager
from isaacsim.sensors.physx.scripts.proximity_sensor import clear_sensors
import omni as omni
from omni.physx import get_physx_interface
__all__ = ['Extension', 'ProximitySensorManager', 'clear_sensors', 'get_physx_interface', 'omni']
class Extension(omni.ext._extensions.IExt):
    def _on_update(self, dt):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
