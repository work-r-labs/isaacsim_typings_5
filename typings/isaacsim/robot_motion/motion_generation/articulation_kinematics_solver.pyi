from __future__ import annotations
import carb as carb
import isaacsim.core.api.articulations.articulation_subset
from isaacsim.core.api.articulations.articulation_subset import ArticulationSubset
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot_motion.motion_generation.kinematics_interface
from isaacsim.robot_motion.motion_generation.kinematics_interface import KinematicsSolver
import numpy as np
import numpy
__all__ = ['ArticulationAction', 'ArticulationKinematicsSolver', 'ArticulationSubset', 'KinematicsSolver', 'SingleArticulation', 'carb', 'np']
class ArticulationKinematicsSolver:
    """
    Wrapper class for computing robot kinematics in a way that is easily transferable to the simulated robot Articulation.  A KinematicsSolver
        computes FK and IK at any frame, possibly only using a subset of joints available on the simulated robot.
        This wrapper simplifies computing the current position of the simulated robot's end effector, as well as wrapping an IK result in an ArticulationAction that is
        recognized by the robot Articulation
    
        Args:
            robot_articulation (SingleArticulation): Initialized robot Articulation object representing the simulated USD robot
            kinematics_solver (KinematicsSolver): An instance of a class that implements the KinematicsSolver
            end_effector_frame_name (str): The name of the robot's end effector frame.  This frame must appear in kinematics_solver.get_all_frame_names()
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, kinematics_solver: isaacsim.robot_motion.motion_generation.kinematics_interface.KinematicsSolver, end_effector_frame_name: str):
        ...
    def compute_end_effector_pose(self, position_only = False) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Compute the pose of the robot end effector using the simulated robot's current joint positions
        
                Args:
                    position_only (bool): If True, only the frame positions need to be calculated.  The returned rotation may be left undefined.
        
                Returns:
                    Tuple[np.array,np.array]:
                    position: Translation vector describing the translation of the robot end effector relative to the USD global frame (in stage units)
        
                    rotation: (3x3) rotation matrix describing the rotation of the frame relative to the USD stage global frame
                
        """
    def compute_inverse_kinematics(self, target_position: numpy.array, target_orientation: typing.Optional[<built-in function array>] = None, position_tolerance: typing.Optional[float] = None, orientation_tolerance: typing.Optional[float] = None) -> typing.Tuple[isaacsim.core.utils.types.ArticulationAction, bool]:
        """
        
                Compute inverse kinematics for the end effector frame using the current robot position as a warm start.  The result is returned
                in an articulation action that can be directly applied to the robot.
        
                Args:
                    target_position (np.array): target translation of the target frame (in stage units) relative to the USD stage origin
                    target_orientation (np.array): target orientation of the target frame relative to the USD stage global frame. Defaults to None.
                    position_tolerance (float): l-2 norm of acceptable position error (in stage units) between the target and achieved translations. Defaults to None.
                    orientation tolerance (float): magnitude of rotation (in radians) separating the target orientation from the achieved orienatation.
                        orientation_tolerance is well defined for values between 0 and pi. Defaults to None.
        
                Returns:
                    Tuple[ArticulationAction, bool]:
                    ik_result: An ArticulationAction that can be applied to the robot to move the end effector frame to the desired position.
        
                    success: Solver converged successfully
                
        """
    def get_end_effector_frame(self) -> str:
        """
        Get the end effector frame
        
                Returns:
                    str: Name of the end effector frame
                
        """
    def get_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        
                Returns:
                    ArticulationSubset: A wrapper class for querying USD robot joint states in the order expected by the kinematics solver
                
        """
    def get_kinematics_solver(self) -> isaacsim.robot_motion.motion_generation.kinematics_interface.KinematicsSolver:
        """
        Get the underlying KinematicsSolver instance used by this class.
        
                Returns:
                    KinematicsSolver: A class that can solve forward and inverse kinematics for a specified robot.
                
        """
    def set_end_effector_frame(self, end_effector_frame_name: str) -> None:
        """
        Set the name for the end effector frame.  If the frame is not recognized by the internal KinematicsSolver instance, an error will be thrown
        
                Args:
                    end_effector_frame_name (str): Name of the robot end effector frame.
                
        """
