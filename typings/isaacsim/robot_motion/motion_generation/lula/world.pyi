from __future__ import annotations
import carb as carb
from isaacsim.core.api import objects
import isaacsim.core.api.objects.ground_plane
from isaacsim.core.utils.prims import delete_prim
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.string import find_unique_string_name
from isaacsim.robot_motion.motion_generation.lula.utils import get_pose3
from isaacsim.robot_motion.motion_generation.lula.utils import get_prim_pose_in_meters_rel_robot_base
import isaacsim.robot_motion.motion_generation.world_interface
from isaacsim.robot_motion.motion_generation.world_interface import WorldInterface
import lula as lula
import numpy as np
__all__ = ['LulaWorld', 'WorldInterface', 'carb', 'delete_prim', 'find_unique_string_name', 'get_pose3', 'get_prim_pose_in_meters_rel_robot_base', 'get_stage_units', 'is_prim_path_valid', 'lula', 'np', 'objects']
class LulaWorld(isaacsim.robot_motion.motion_generation.world_interface.WorldInterface):
    def __init__(self):
        ...
    def add_capsule(self, capsule: typing.Union[isaacsim.core.api.objects.capsule.DynamicCapsule, isaacsim.core.api.objects.capsule.VisualCapsule], static: bool = False, robot_pos: typing.Optional[<built-in function array>] = ..., robot_rot: typing.Optional[<built-in function array>] = ...) -> bool:
        """
        Add a capsule obstacle.
        
                Args:
                    capsule (core.objects.capsule): Wrapper object for handling capsule Usd Prims.
                    static (bool, optional): If True, indicate that capsule will never change pose, and may be ignored in internal
                        world updates. Since Lula specifies object positions relative to the robot's frame
                        of reference, static obstacles will have their positions queried any time that
                        set_robot_base_pose() is called.  Defaults to False.
        
                Returns:
                    bool: Always True, indicating that this function has been implemented
                
        """
    def add_cuboid(self, cuboid: typing.Union[isaacsim.core.api.objects.cuboid.DynamicCuboid, isaacsim.core.api.objects.cuboid.FixedCuboid, isaacsim.core.api.objects.cuboid.VisualCuboid], static: typing.Optional[bool] = False, robot_pos: typing.Optional[<built-in function array>] = ..., robot_rot: typing.Optional[<built-in function array>] = ...):
        """
        Add a block obstacle.
        
                Args:
                    cuboid (core.objects.cuboid): Wrapper object for handling rectangular prism Usd Prims.
                    static (bool, optional): If True, indicate that cuboid will never change pose, and may be ignored in internal
                        world updates. Since Lula specifies object positions relative to the robot's frame
                        of reference, static obstacles will have their positions queried any time that
                        set_robot_base_pose() is called.  Defaults to False.
        
        
                Returns:
                    bool: Always True, indicating that this adder has been implemented
                
        """
    def add_ground_plane(self, ground_plane: isaacsim.core.api.objects.ground_plane.GroundPlane, plane_width: typing.Optional[float] = 50.0) -> bool:
        """
        Add a ground_plane.
                Lula does not support ground planes directly, and instead internally creates a cuboid with an
                expansive face (dimensions 200x200 stage units) coplanar to the ground_plane.
        
                Args:
                    ground_plane (core.objects.ground_plane.GroundPlane): Wrapper object for handling ground_plane Usd Prims.
                    plane_width (Optional[float]): The width of the ground plane (in meters) that Lula creates to constrain this robot.  Defaults to 50.0 m
        
                Returns:
                    bool: Always True, indicating that this adder has been implemented
                
        """
    def add_sphere(self, sphere: typing.Union[isaacsim.core.api.objects.sphere.DynamicSphere, isaacsim.core.api.objects.sphere.VisualSphere], static: bool = False, robot_pos: typing.Optional[<built-in function array>] = ..., robot_rot: typing.Optional[<built-in function array>] = ...) -> bool:
        """
        Add a sphere obstacle.
        
                Args:
                    sphere (core.objects.sphere): Wrapper object for handling sphere Usd Prims.
                    static (bool, optional): If True, indicate that sphere will never change pose, and may be ignored in internal
                        world updates. Since Lula specifies object positions relative to the robot's frame
                        of reference, static obstacles will have their positions queried any time that
                        set_robot_base_pose() is called.  Defaults to False.
        
        
                Returns:
                    bool: Always True, indicating that this adder has been implemented
                
        """
    def disable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Disable collision avoidance for obstacle.
        
                Args:
                    obstacle (core.objects): obstacle to be disabled.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully disabled.
                
        """
    def enable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Enable collision avoidance for obstacle.
        
                Args:
                    obstacle (core.objects): obstacle to be enabled.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully enabled.
                
        """
    def remove_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Remove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after
                removal.
        
                Args:
                    obstacle (core.objects): obstacle to be removed.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully removed.
                
        """
    def reset(self) -> None:
        """
        reset the world to its initial state
        """
    def update_world(self, updated_obstacles: typing.Optional[typing.List] = None, robot_pos: typing.Optional[<built-in function array>] = ..., robot_rot: typing.Optional[<built-in function array>] = ..., robot_base_moved: bool = False) -> None:
        """
        Update the internal world state of Lula.
                This function automatically tracks the positions of obstacles that have been added with add_obstacle()
        
                Args:
                    updated_obstacles (List[core.objects], optional): Obstacles that have been added by add_obstacle() that need to be updated.
                        If not specified, all non-static obstacle positions will be updated.
                        If specified, only the obstacles that have been listed will have their positions updated
                
        """
