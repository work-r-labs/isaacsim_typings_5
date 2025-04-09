from __future__ import annotations
from isaacsim.robot.wheeled_robots.bindings._isaacsim_robot_wheeled_robots import acquire_wheeled_robots_interface
from isaacsim.robot.wheeled_robots.bindings._isaacsim_robot_wheeled_robots import release_wheeled_robots_interface
import omni as omni
__all__ = ['Extension', 'acquire_wheeled_robots_interface', 'omni', 'release_wheeled_robots_interface']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
