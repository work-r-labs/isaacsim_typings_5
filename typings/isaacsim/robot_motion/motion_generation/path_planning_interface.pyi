from __future__ import annotations
import isaacsim.robot_motion.motion_generation.world_interface
from isaacsim.robot_motion.motion_generation.world_interface import WorldInterface
import numpy as np
import numpy
__all__ = ['PathPlanner', 'WorldInterface', 'np']
class PathPlanner(isaacsim.robot_motion.motion_generation.world_interface.WorldInterface):
    """
    Interface for implementing a PathPlanner: An algorithm that outputs a series of configuration space waypoints, which
        when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
        
    """
    def __init__(self) -> None:
        ...
    def compute_path(self, active_joint_positions: numpy.array, watched_joint_positions: numpy.array) -> numpy.array:
        """
        Compute a set of c-space waypoints, which when linearly interpolated,
                produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
        
                Args:
                    active_joint_positions (np.array): current positions of joints specified by get_active_joints()
                    watched_joint_positions (np.array): current positions of joints specified by get_watched_joints()
        
                Returns:
                    np.array or None:
                    path: An (N x m) sequence of joint positions for the active joints in the robot where N is the path length and
                        m is the number of active joints in the robot.  If no plan is found, or no target positions have been set, None is returned
                
        """
    def get_active_joints(self) -> typing.List[str]:
        """
        Active joints are directly controlled by this PathPlanner
        
                Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used
                to follow targets, and the RMPflow config files excludes the joints in the gripper from the list of articulated
                joints.
        
                Returns:
                    List[str]: names of active joints.  The order of joints in this list determines the order in which a
                    PathPlanner expects joint states to be specified in functions like compute_path(active_joint_positions,...)
                
        """
    def get_watched_joints(self) -> typing.List[str]:
        """
        Watched joints are joints whose position matters to the PathPlanner, but are not directly controlled.
                e.g.  A robot may have a watched joint in the middle of its kinematic chain. Watched joints will be assumed
                to remain watched during the rollout of a path.
        
                Returns:
                    List[str]: Names of joints that are being watched by this PathPlanner. The order of joints in this list determines the order in which a
                    PathPlanner expects joint states to be specified in functions like compute_path(...,watched_joint_positions,...).
                
        """
    def set_cspace_target(self, active_joint_targets: numpy.array) -> None:
        """
        Set configuration space target for the robot.
        
                Args:
                    active_joint_target (np.array): Desired configuration for the robot as (m x 1) vector where m is the number of active
                        joints.
        
                Returns:
                    None
                
        """
    def set_end_effector_target(self, target_translation, target_orientation = None) -> None:
        """
        Set end effector target.
        
                Args:
                    target_translation (nd.array): Translation vector (3x1) for robot end effector.
                        Target translation should be specified in the same units as the USD stage, relative to the stage origin.
                    target_orientation (nd.array): Quaternion of desired rotation for robot end effector relative to USD stage global frame
        
                Returns:
                    None
                
        """
    def set_robot_base_pose(self, robot_translation: numpy.array, robot_orientation: numpy.array):
        """
        Set the position of the robot base. Computed paths will assume that the robot base remains stationary.
        
                Args:
                    robot_translation (np.array): (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin.
                        The translation vector should be specified in the units of the USD stage
                    robot_orientation (np.array): (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame
                
        """
