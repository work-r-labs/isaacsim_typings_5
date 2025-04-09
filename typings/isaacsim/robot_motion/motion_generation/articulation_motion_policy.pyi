from __future__ import annotations
import carb as carb
import isaacsim.core.api.articulations.articulation_subset
from isaacsim.core.api.articulations.articulation_subset import ArticulationSubset
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot_motion.motion_generation.motion_policy_interface
from isaacsim.robot_motion.motion_generation.motion_policy_interface import MotionPolicy
import torch as torch
__all__ = ['ArticulationAction', 'ArticulationMotionPolicy', 'ArticulationSubset', 'MotionPolicy', 'SingleArticulation', 'carb', 'torch']
class ArticulationMotionPolicy:
    """
    Wrapper class for running MotionPolicy on simulated robots.
    
        Args:
            robot_articulation (SingleArticulation): an initialized robot Articulation object
            motion_policy (MotionPolicy): an instance of a class that implements the MotionPolicy interface
            default_physics_dt (float): Default physics step size to use when computing actions. A MotionPolicy computes a target
                position/velocity for the next frame of the simulation using the provided physics dt to know how far in the future that will be.
                Isaac Sim can be run with a constant or variable physics framerate.
                When not specified on an individual frame, the dt of the frame is assumed
                to be the provided default value.
    
        Returns:
            None
    
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, motion_policy: isaacsim.robot_motion.motion_generation.motion_policy_interface.MotionPolicy, default_physics_dt: float = 0.016666666666666666) -> None:
        ...
    def get_active_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        Get view into active joints
        
                Returns:
                    ArticulationSubset: returns robot states for active joints in an order compatible with the MotionPolicy
                
        """
    def get_default_physics_dt(self) -> float:
        """
        Get the default value of the physics dt that is used to compute actions when none is provided
        
                Returns:
                    float: Default physics dt
                
        """
    def get_motion_policy(self) -> isaacsim.robot_motion.motion_generation.motion_policy_interface.MotionPolicy:
        """
        Get MotionPolicy that is being used to compute ArticulationActions
        
                Returns:
                    MotionPolicy: MotionPolicy being used to compute ArticulationActions
                
        """
    def get_next_articulation_action(self, physics_dt: float = None) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Use underlying MotionPolicy to compute joint targets for the robot over the next frame.
        
                Args:
                    physics_dt (float): Physics dt to use on this frame to calculate the next action.  This overrides
                        the default_physics_dt argument, but does not change the default on future calls.
        
                Returns:
                    ArticulationAction: Desired position/velocity target for the robot in the next frame
                
        """
    def get_robot_articulation(self) -> isaacsim.core.prims.impl.single_articulation.SingleArticulation:
        """
        Get the underlying Articulation object representing the robot.
        
                Returns:
                    SingleArticulation: Articulation object representing the robot.
                
        """
    def get_watched_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        Get view into watched joints
        
                Returns:
                    ArticulationSubset: returns robot states for watched joints in an order compatible with the MotionPolicy
                
        """
    def move(self, physics_dt: float = None) -> None:
        """
        Use underlying MotionPolicy to compute and apply joint targets to the robot over the next frame.
        
                Args:
                    physics_dt (float): Physics dt to use on this frame to calculate the next action.  This overrides
                        the default_physics_dt argument, but does not change the default on future calls.
        
                Return:
                    None
                
        """
    def set_default_physics_dt(self, physics_dt: float) -> None:
        """
        Set the default value of the physics dt that is used to compute actions when none is provided
        
                Args:
                    physics_dt (float): Default physics dt
        
                Returns:
                    None
                
        """
