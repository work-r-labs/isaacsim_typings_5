from __future__ import annotations
import numpy as np
__all__ = ['Trajectory', 'np']
class Trajectory:
    """
    Interface class for defining a continuous-time trajectory for a robot in Isaac Sim.
        A Trajectory may be passed to an ArticulationTrajectory to have its continuous-time output discretized and converted
        to a ArticulationActions.
        
    """
    def __init__(self):
        ...
    def get_active_joints(self) -> typing.List[str]:
        """
        Active joints are directly controlled by this Trajectory
        
                A Trajectory may be specified for only a subset of the joints in a robot Articulation.  For example, it may include the DOFs in a robot
                arm, but not in the gripper.
        
                Returns:
                    List[str]: Names of active joints.  The order of joints in this list determines the order in which a
                        Trajectory will return joint targets for the robot.
                
        """
    def get_joint_targets(self, time: float) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Return joint targets for the robot at the given time.  The Trajectory interface assumes trajectories to
                be represented continuously between a start time and end time.  In instance of this class that internally generates discrete time
                trajectories will need to implement some form of interpolation for times that have not been computed.
        
                Args:
                    time (float): Time in trajectory at which to return joint targets.
        
                Returns:
                    Tuple[np.array,np.array]:
                    joint position targets for the active robot joints
        
                    joint velocity targets for the active robot joints
                
        """
    @property
    def end_time(self) -> float:
        """
        Return the end time of the trajectory
        
                Returns:
                    float: End time of the trajectory
                
        """
    @property
    def start_time(self) -> float:
        """
        Return the start time of the trajectory.
        
                Returns:
                    float: Start time of the trajectory.
                
        """
