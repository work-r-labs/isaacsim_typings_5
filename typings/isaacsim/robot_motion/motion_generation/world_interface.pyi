from __future__ import annotations
import carb as carb
import isaacsim as isaacsim
from isaacsim.core.api.objects import capsule
from isaacsim.core.api.objects import cone
from isaacsim.core.api.objects import cuboid
from isaacsim.core.api.objects import cylinder
from isaacsim.core.api.objects import ground_plane
from isaacsim.core.api.objects import sphere
__all__ = ['WorldInterface', 'capsule', 'carb', 'cone', 'cuboid', 'cylinder', 'ground_plane', 'isaacsim', 'sphere']
class WorldInterface:
    """
    Interface for translating USD world to a generic world-aware algorithm such as a MotionPolicy
    """
    def __init__(self) -> None:
        ...
    def add_capsule(self, capsule: typing.Union[isaacsim.core.api.objects.capsule.DynamicCapsule, isaacsim.core.api.objects.capsule.VisualCapsule], static: bool = False) -> bool:
        """
        Add a capsule obstacle.
        
                Args:
                    capsule (core.objects.capsule): Wrapper object for handling capsule Usd Prims.
                    static (bool, optional): If True, indicate that capsule will never change pose, and may be ignored in internal
                        world updates. Defaults to False.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_capsule()
                
        """
    def add_cone(self, cone: typing.Union[isaacsim.core.api.objects.cone.DynamicCone, isaacsim.core.api.objects.cone.VisualCone], static: bool = False) -> bool:
        """
        Add a cone obstacle.
        
                Args:
                    cone (core.objects.cone): Wrapper object for handling cone Usd Prims.
                    static (bool, optional): If True, indicate that cone will never change pose, and may be ignored in internal
                        world updates. Defaults to False.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_cone()
                
        """
    def add_cuboid(self, cuboid: typing.Union[isaacsim.core.api.objects.cuboid.DynamicCuboid, isaacsim.core.api.objects.cuboid.FixedCuboid, isaacsim.core.api.objects.cuboid.VisualCuboid], static: bool = False) -> bool:
        """
        Add a block obstacle.
        
                Args:
                    cuboid (core.objects.cuboid): Wrapper object for handling rectangular prism Usd Prims.
                    static (bool, optional): If True, indicate that cuboid will never change pose, and may be ignored in internal
                        world updates. Defaults to False.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_cuboid()
                
        """
    def add_cylinder(self, cylinder: typing.Union[isaacsim.core.api.objects.cylinder.DynamicCylinder, isaacsim.core.api.objects.cylinder.VisualCylinder], static: bool = False) -> bool:
        """
        Add a cylinder obstacle.
        
                Args:
                    cylinder (core.objects.cylinder): Wrapper object for handling rectangular prism Usd Prims.
                    static (bool, optional): If True, indicate that cuboid will never change pose, and may be ignored in internal
                        world updates. Defaults to False.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_cylinder()
                
        """
    def add_ground_plane(self, ground_plane: isaacsim.core.api.objects.ground_plane.GroundPlane) -> bool:
        """
        Add a ground_plane
        
                Args:
                    ground_plane (core.objects.ground_plane.GroundPlane): Wrapper object for handling ground_plane Usd Prims.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_ground_plane()
                
        """
    def add_obstacle(self, obstacle: isaacsim.core.api.objects, static: typing.Optional[bool] = False) -> bool:
        """
        Add an obstacle
        
                Args:
                    obstacle (isaacsim.core.api.objects): An obstacle from the package isaacsim.core.api.obstacles
                                    The type of the obstacle will be checked, and the appropriate add function will be called 
        
                    static (Optional[bool]): When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time
        
                Returns:
                    success (bool): Returns True if the obstacle type is valid and the appropriate add function has been implemented
                
        """
    def add_sphere(self, sphere: typing.Union[isaacsim.core.api.objects.sphere.DynamicSphere, isaacsim.core.api.objects.sphere.VisualSphere], static: bool = False) -> bool:
        """
        Add a sphere obstacle.
        
                Args:
                    sphere (core.objects.sphere): Wrapper object for handling sphere Usd Prims.
                    static (bool, optional): If True, indicate that sphere will never change pose, and may be ignored in internal
                        world updates. Defaults to False.
        
                Returns:
                    bool: Return True if underlying WorldInterface has implemented add_sphere()
                
        """
    def disable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Disable collision avoidance for obstacle.
        
                Args:
                    obstacle (core.object): obstacle to be disabled.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully disabled.
                
        """
    def enable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Enable collision avoidance for obstacle.
        
                Args:
                    obstacle (core.object): obstacle to be enabled.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully enabled.
                
        """
    def remove_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        """
        Remove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after
                removal.
        
                Args:
                    obstacle (core.object): obstacle to be removed.
        
                Returns:
                    bool: Return True if obstacle was identified and successfully removed.
                
        """
    def reset(self) -> None:
        """
        Reset all state inside the WorldInterface to its initial values
        """
    def update_world(self, updated_obstacles: typing.Optional[typing.List] = None) -> None:
        """
        Applies all necessary updates to the internal world representation.
        
                Args:
                    updated_obstacles (list, optional): If provided, only the given obstacles will have their poses updated.
                        For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies),
                        this list will be ignored if the robot base has moved because all object poses will have changed
                        relative to the robot. Defaults to None.
        
                Returns:
                    None
                
        """
