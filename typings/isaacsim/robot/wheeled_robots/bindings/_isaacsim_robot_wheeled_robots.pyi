"""

        Internal interface that is automatically called when the extension is loaded so that Omnigraph nodes are registered.

        Example:

            # import  isaacsim.robot.wheeled_robots.bindings._isaacsim_robot_wheeled_robots as _isaacsim_robot_wheeled_robots

            # Acquire the interface
            interface = _isaacsim_robot_wheeled_robots.acquire_wheeled_robots_interface()

            # Use the interface
            # ...

            # Release the interface
            _isaacsim_robot_wheeled_robots.release_wheeled_robots_interface(interface)
    
"""
from __future__ import annotations
__all__: list[str] = ['IWheeledRobots', 'acquire_wheeled_robots_interface', 'release_wheeled_robots_interface']
class IWheeledRobots:
    pass
def acquire_wheeled_robots_interface(plugin_name: str = None, library_path: str = None) -> IWheeledRobots:
    ...
def release_wheeled_robots_interface(arg0: IWheeledRobots) -> None:
    ...
