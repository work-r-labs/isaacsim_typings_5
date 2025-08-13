from __future__ import annotations
import gc as gc
from isaacsim.robot.surface_gripper import _surface_gripper
import omni as omni
__all__: list[str] = ['EXTENSION_NAME', 'Extension', 'gc', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
EXTENSION_NAME: str = 'Surface Gripper'
