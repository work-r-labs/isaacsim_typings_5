from __future__ import annotations
import carb as carb
from isaacsim.core.api import objects
import isaacsim.core.api.objects.cuboid
import isaacsim.core.api.objects.ground_plane
from isaacsim.core.utils.math import normalized
from isaacsim.core.utils.numpy.rotations import quats_to_rot_matrices
from isaacsim.core.utils.numpy.rotations import rot_matrices_to_quats
from isaacsim.core.utils.prims import delete_prim
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.string import find_unique_string_name
import isaacsim.robot_motion.motion_generation.lula.interface_helper
from isaacsim.robot_motion.motion_generation.lula.interface_helper import LulaInterfaceHelper
import isaacsim.robot_motion.motion_generation.lula.kinematics
from isaacsim.robot_motion.motion_generation.lula.kinematics import LulaKinematicsSolver
import isaacsim.robot_motion.motion_generation.motion_policy_interface
from isaacsim.robot_motion.motion_generation.motion_policy_interface import MotionPolicy
import lula as lula
import numpy
import numpy as np
from pxr import Sdf
import time as time
__all__ = ['LulaInterfaceHelper', 'LulaKinematicsSolver', 'MotionPolicy', 'RmpFlow', 'RmpFlowSmoothed', 'Sdf', 'carb', 'delete_prim', 'find_unique_string_name', 'is_prim_path_valid', 'lula', 'normalized', 'np', 'objects', 'quats_to_rot_matrices', 'rot_matrices_to_quats', 'time']
class RmpFlow(isaacsim.robot_motion.motion_generation.lula.interface_helper.LulaInterfaceHelper, isaacsim.robot_motion.motion_generation.motion_policy_interface.MotionPolicy):
    """
    
        RMPflow is a real-time, reactive motion policy that smoothly guides a robot to task space targets while avoiding dynamic obstacles.
        This class implements the MotionPolicy interface, as well as providing a number of RmpFlow-specific functions such as visualizing
        the believed robot position and changing internal settings.
    
        Args:
            robot_description_path (str): Path to a robot description yaml file
            urdf_path (str): Path to robot urdf
            rmpflow_config_path (str): Path to an rmpflow parameter yaml file
            end_effector_frame_name (str): Name of the robot end effector frame (must be present in the robot urdf)
            maximum_substep_size (float): Maximum substep size [sec] that RmpFlow will use when internally integrating between steps of a simulation.  For stability and performance,
                RmpFlow rolls out the robot actions at a higher framerate than Isaac Sim.  For example, while Isaac Sim may be running at 60 Hz, RmpFlow can be set to take internal
                steps that are no larger than 1/300 seconds.  In this case, RmpFlow will perform 5 sub-steps every time it returns an action to the 60 Hz simulation.
    
                In general, the maximum_substep_size argument should be at most 1/200.  Choosing a very small maximum_substep_size such as 1/1000 is unnecessary, as the resulting actions will not
                significantly differ from a choice of 1/500, but it will internally require twice the steps to compute.
            ignore_robot_state_updates (bool): Defaults to False.
                If False: RmpFlow will set the internal robot state to match the arguments to compute_joint_targets().  When paired with ArticulationMotionPolicy, this means that RMPflow uses the simulated robot's state at every frame.
                If True: RmpFlow will roll out the robot state internally after it is initially specified in the first call to compute_joint_targets().
        
    """
    def __init__(self, robot_description_path: str, urdf_path: str, rmpflow_config_path: str, end_effector_frame_name: str, maximum_substep_size: float, ignore_robot_state_updates = False) -> None:
        ...
    def _create_collision_sphere_prims(self, is_visible):
        ...
    def _create_ee_visual(self, is_visible):
        ...
    def _euler_integration(self, joint_positions, joint_velocities, frame_duration):
        ...
    def _evaluate_acceleration(self, joint_positions, joint_velocities):
        ...
    def _set_end_effector_target(self):
        ...
    def _update_collision_sphere_prims(self):
        ...
    def _update_end_effector_prim(self):
        ...
    def _update_robot_joint_states(self, joint_positions, joint_velocities, frame_duration):
        ...
    def _update_visuals(self):
        ...
    def add_capsule(self, capsule: typing.Union[isaacsim.core.api.objects.capsule.DynamicCapsule, isaacsim.core.api.objects.capsule.VisualCapsule], static: bool = False) -> bool:
        ...
    def add_cuboid(self, cuboid: typing.Union[isaacsim.core.api.objects.cuboid.DynamicCuboid, isaacsim.core.api.objects.cuboid.FixedCuboid, isaacsim.core.api.objects.cuboid.VisualCuboid], static: bool = False) -> bool:
        ...
    def add_ground_plane(self, ground_plane: isaacsim.core.api.objects.ground_plane.GroundPlane) -> bool:
        ...
    def add_obstacle(self, obstacle: isaacsim.core.api.objects, static: bool = False) -> bool:
        ...
    def add_sphere(self, sphere: typing.Union[isaacsim.core.api.objects.sphere.DynamicSphere, isaacsim.core.api.objects.sphere.VisualSphere], static: bool = False) -> bool:
        ...
    def compute_joint_targets(self, active_joint_positions: numpy.array, active_joint_velocities: numpy.array, watched_joint_positions: numpy.array, watched_joint_velocities: numpy.array, frame_duration: float) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Compute robot joint targets for the next frame based on the current robot position.
                RmpFlow will ignore active joint positions and velocities if it has been set to ignore_robot_state_updates
                RmpFlow does not currently support watching joints that it is not actively controlling.
        
                Args:
                    active_joint_positions (np.array): current positions of joints specified by get_active_joints()
                    active_joint_velocities (np.array): current velocities of joints specified by get_active_joints()
                    watched_joint_positions (np.array): current positions of joints specified by get_watched_joints()
                        This will always be empty for RmpFlow.
                    watched_joint_velocities (np.array): current velocities of joints specified by get_watched_joints()
                        This will always be empty for RmpFlow.
                    frame_duration (float): duration of the physics frame
        
                Returns:
                    Tuple[np.array,np.array]:
                    active_joint_position_targets : Position targets for the robot in the next frame
        
                    active_joint_velocity_targets : Velocity targets for the robot in the next frame
                
        """
    def delete_collision_sphere_prims(self) -> None:
        """
        An RmpFlow specific debugging method.  This function deletes any prims that have been created by RmpFlow to visualize its internal collision spheres
        """
    def delete_end_effector_prim(self) -> None:
        """
        An RmpFlow specific debugging method.  If RmpFlow is maintaining a prim for its believed end effector position, this function will delete the prim.
        """
    def disable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        ...
    def enable_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        ...
    def get_active_joints(self) -> typing.List[str]:
        """
        Returns a list of joint names that RmpFlow is controlling.
        
                Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used
                to follow targets, and the RmpFlow config files excludes the joints in the gripper from the list of active
                joints.
        
                Returns:
                    active_joints (List[str]): Names of active joints.
                        The order of the joints in this list matches the order that the joints are expected
                        in functions like RmpFlow.compute_joint_targets(active_joint_positions, active_joint_velocities,...)
                
        """
    def get_collision_spheres_as_prims(self) -> typing.List:
        """
        An RmpFlow specific debugging method.  This function is similar to RmpFlow.visualize_collision_spheres().  If the collision spheres have already been added to the stage as prims,
                they will be returned.  If the collision spheres have not been added to the stage as prims, they will be created and returned.  If created in this function, the spheres will be invisible
                until RmpFlow.visualize_collision_spheres() is called.
        
                Visualizing collision spheres on the stage is likely to significantly slow down the framerate of the simulation.  This function should only be used for debugging purposes
        
                Returns:
                    collision_spheres (List[core.objects.sphere.VisualSphere]): List of prims representing RmpFlow's internal collision spheres
        
                
        """
    def get_default_cspace_position_target(self):
        """
        An RmpFlow specific method; this function returns the default cspace position specified in the
                    Lula robot_description YAML file
        
                Returns:
                    np.array: Default cspace position target used by RMPflow when none is specified.
                
        """
    def get_end_effector_as_prim(self) -> isaacsim.core.api.objects.cuboid.VisualCuboid:
        """
        An RmpFlow specific debugging method.  This function is similar to RmpFlow.visualize_end_effector_position().  If the end effector has already been visualized as a prim,
                it will be returned.  If the end effector is not being visualized, a cuboid will be created and returned.  If created in this function, the end effector will be invisible
                until RmpFlow.visualize_end_effector_position() is called.
        
                Returns:
                    end_effector_prim (objects.cuboid.VisualCuboid): Cuboid whose translation and orientation match RmpFlow's believed robot end effector position.
                
        """
    def get_end_effector_pose(self, active_joint_positions: numpy.array) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        ...
    def get_internal_robot_joint_states(self) -> typing.Tuple[<built-in function array>, <built-in function array>, <built-in function array>, <built-in function array>]:
        """
        An RmpFlow specific method; this function returns the internal robot state that is believed by RmpFlow
        
                Returns:
                    Tuple[np.array,np.array,np.array,np.array]:
        
                    active_joint_positions: believed positions of active joints
        
                    active_joint_velocities: believed velocities of active joints
        
                    watched_joint_positions: believed positions of watched robot joints.  This will always be empty for RmpFlow.
        
                    watched_joint_velocities: believed velocities of watched robot joints.  This will always be empty for RmpFlow.
        
                
        """
    def get_kinematics_solver(self) -> isaacsim.robot_motion.motion_generation.lula.kinematics.LulaKinematicsSolver:
        """
        Return a LulaKinematicsSolver that uses the same robot description as RmpFlow.  The robot base pose of the LulaKinematicsSolver
                will be set to the same base pose as RmpFlow, but the two objects must then have their base poses updated separately.
        
                Returns:
                    LulaKinematicsSolver: Kinematics solver using the same cspace as RmpFlow
                
        """
    def get_watched_joints(self) -> typing.List[str]:
        """
        Currently, RmpFlow is not capable of watching joint states that are not being directly controlled (active joints)
                If RmpFlow is controlling a robot arm at the end of an externally controlled body, set_robot_base_pose() can be used to make RmpFlow aware of the robot position
                This means that RmpFlow is not currently able to support controlling a set of DOFs in a robot that are not sequentially linked to each other or are not connected
                via fixed transforms to the end effector.
        
                Returns:
                    watched_joints (List[str]): Empty list
                
        """
    def remove_obstacle(self, obstacle: isaacsim.core.api.objects) -> bool:
        ...
    def reset(self) -> None:
        """
        Reset RmpFlow to its initial state
        """
    def set_cspace_target(self, active_joint_targets) -> None:
        """
        Set a cspace target for RmpFlow.  RmpFlow always has a cspace target, and setting a new cspace target does not override a position target.
                RmpFlow uses the cspace target to help resolve null space behavior when a position target can be acheived in a variety of ways.
                If the end effector target is explicitly set to None, RmpFlow will move the robot to the cspace target
        
                Args:
                    active_joint_targets (np.array): cspace position target for active joints in the robot
                
        """
    def set_end_effector_target(self, target_position = None, target_orientation = None) -> None:
        ...
    def set_ignore_state_updates(self, ignore_robot_state_updates) -> None:
        """
        An RmpFlow specific method; set an internal flag in RmpFlow: ignore_robot_state_updates
        
                Args:
                    ignore_robot_state_updates (bool):
                        If False:
                            RmpFlow will set the internal robot state to match the arguments to compute_joint_targets().
                            When paired with ArticulationMotionPolicy, this means that RMPflow uses the simulated robot's state at every frame.
                        If True:
                            RmpFlow will roll out the robot state internally after it is initially specified in the first call to compute_joint_targets().
                            The caller may override this flag and directly change the internal robot state with RmpFlow.set_internal_robot_joint_states().
                
        """
    def set_internal_robot_joint_states(self, active_joint_positions: numpy.array, active_joint_velocities: numpy.array, watched_joint_positions: numpy.array, watched_joint_velocities: numpy.array) -> None:
        """
        An RmpFlow specific method; this function overwrites the robot state regardless of the ignore_robot_state_updates flag.
                RmpFlow does not currently support watching joints that it is not actively controlling.
        
                Args:
                    active_joint_positions (np.array): current positions of joints specified by get_active_joints()
                    active_joint_velocities (np.array): current velocities of joints specified by get_active_joints()
                    watched_joint_positions (np.array): current positions of joints specified by get_watched_joints().
                        This will always be empty for RmpFlow.
                    watched_joint_velocities (np.array): current velocities of joints specified by get_watched_joints()
                        This will always be empty for RmpFlow.
                
        """
    def set_robot_base_pose(self, robot_position: numpy.array, robot_orientation: numpy.array) -> None:
        ...
    def stop_visualizing_collision_spheres(self) -> None:
        """
        An RmpFlow specific debugging method.  This function removes the collision sphere prims created by either RmpFlow.visualize_collision_spheres() or
                RmpFlow.get_collision_spheres_as_prims().  Rather than making the prims invisible, they are deleted from the stage to increase performance
                
        """
    def stop_visualizing_end_effector(self) -> None:
        """
        An RmpFlow specific debugging method.  This function removes the end effector prim that can be created by visualize_end_effector_position() or
                get_end_effector_position_as_prim()
                
        """
    def update_world(self, updated_obstacles: typing.List = None) -> None:
        ...
    def visualize_collision_spheres(self) -> None:
        """
        An RmpFlow specific debugging method.  This function creates visible sphere prims that match the locations and radii
                of the collision spheres that RmpFlow uses to prevent robot collisions.  Once created, RmpFlow will update the sphere locations
                whenever its internal robot state changes.  This can be used alongside RmpFlow.ignore_robot_state_updates(True) to validate RmpFlow's
                internal representation of the robot as well as help tune the PD gains on the simulated robot; i.e. the simulated robot should
                match the positions of the RmpFlow collision spheres over time.
        
                Visualizing collision spheres as prims on the stage is likely to significantly slow down the framerate of the simulation.  This function should only be used for debugging purposes
                
        """
    def visualize_end_effector_position(self) -> None:
        """
        An RmpFlow specific debugging method.  This function creates a visible cube whose translation and orientation match where RmpFlow
                believes the robot end effector to be.  Once created, RmpFlow will update the position of the cube whenever its internal robot state changes.
                
        """
class RmpFlowSmoothed(RmpFlow):
    def __init__(self, *args, **kwargs):
        ...
    def _euler_integration(self, joint_positions, joint_velocities, frame_duration):
        ...
    def _eval_speed_scaled_accel(self, joint_positions, joint_velocities):
        ...
