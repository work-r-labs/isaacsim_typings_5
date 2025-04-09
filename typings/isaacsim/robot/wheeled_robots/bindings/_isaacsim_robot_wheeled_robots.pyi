"""
pybind11 isaacsim.robot.wheeled_robots bindings
"""
from __future__ import annotations
__all__ = ['IWheeledRobots', 'acquire_wheeled_robots_interface', 'release_wheeled_robots_interface']
class IWheeledRobots:
    pass
def acquire_wheeled_robots_interface(plugin_name: str = None, library_path: str = None) -> IWheeledRobots:
    ...
def release_wheeled_robots_interface(arg0: IWheeledRobots) -> None:
    ...
