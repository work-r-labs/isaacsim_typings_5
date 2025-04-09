from __future__ import annotations
import isaacsim as isaacsim
from isaacsim.core.api.controllers.base_controller import BaseController
from isaacsim.core.utils.rotations import euler_angles_to_quat
from isaacsim.core.utils.types import ArticulationAction
from isaacsim.robot_motion.motion_generation.articulation_motion_policy import ArticulationMotionPolicy
from isaacsim.robot_motion.motion_generation.motion_policy_interface import MotionPolicy
import numpy as np
import numpy
import typing
__all__ = ['ArticulationAction', 'ArticulationMotionPolicy', 'BaseController', 'MotionPolicy', 'MotionPolicyController', 'euler_angles_to_quat', 'isaacsim', 'np']
class MotionPolicyController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    A Controller that steps using an arbitrary MotionPolicy
    
        Args:
            name (str): name of this controller
            articulation_motion_policy (ArticulationMotionPolicy): a wrapper around a MotionPolicy for computing ArticulationActions that can be directly applied to the robot
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, articulation_motion_policy: isaacsim.robot_motion.motion_generation.articulation_motion_policy.ArticulationMotionPolicy) -> None:
        ...
    def add_obstacle(self, obstacle: isaacsim.core.api.objects, static: bool = False) -> None:
        """
        Add an object from isaacsim.core.api.objects as an obstacle to the motion_policy
        
                Args:
                    obstacle (isaacsim.core.api.objects): Dynamic, Visual, or Fixed object from isaacsim.core.api.objects
                    static (bool): If True, the obstacle may be assumed by the MotionPolicy to remain stationary over time
                
        """
    def forward(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Compute an ArticulationAction representing the desired robot state for the next simulation frame
        
                Args:
                    target_translation (nd.array): Translation vector (3x1) for robot end effector.
                        Target translation should be specified in the same units as the USD stage, relative to the stage origin.
                    target_orientation (Optional[np.ndarray], optional): Quaternion of desired rotation for robot end effector relative to USD stage global frame.
                        Target orientation defaults to None, which means that the robot may reach the target with any orientation.
        
                Returns:
                    ArticulationAction: A wrapper object containing the desired next state for the robot
                
        """
    def get_articulation_motion_policy(self) -> isaacsim.robot_motion.motion_generation.articulation_motion_policy.ArticulationMotionPolicy:
        """
        Get ArticulationMotionPolicy that was passed to this class on initialization
        
                Returns:
                    ArticulationMotionPolicy: a wrapper around a MotionPolicy for computing ArticulationActions that can be directly applied to the robot
                
        """
    def get_motion_policy(self) -> isaacsim.robot_motion.motion_generation.motion_policy_interface.MotionPolicy:
        """
        Get MotionPolicy object that is being used to generate robot motions
        
                Returns:
                    MotionPolicy: An instance of a MotionPolicy that is being used to compute robot motions
                
        """
    def remove_obstacle(self, obstacle: isaacsim.core.api.objects) -> None:
        """
        Remove and added obstacle from the motion_policy
        
                Args:
                    obstacle (isaacsim.core.api.objects): Object from isaacsim.core.api.objects that has been added to the motion_policy
                
        """
    def reset(self) -> None:
        """
         
        """
