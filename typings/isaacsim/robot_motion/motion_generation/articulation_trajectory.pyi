from __future__ import annotations
import carb as carb
import isaacsim.core.api.articulations.articulation_subset
from isaacsim.core.api.articulations.articulation_subset import ArticulationSubset
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot_motion.motion_generation.trajectory
from isaacsim.robot_motion.motion_generation.trajectory import Trajectory
import numpy as np
__all__ = ['ArticulationAction', 'ArticulationSubset', 'ArticulationTrajectory', 'SingleArticulation', 'Trajectory', 'carb', 'np']
class ArticulationTrajectory:
    """
    Wrapper class which takes in a Trajectory object and converts the output to discrete ArticulationActions that may be sent to the provided robot Articulation.
    
        Args:
            robot_articulation (SingleArticulation): Initialized robot Articulation object representing the simulated USD robot
            trajectory (Trajectory): An instance of a class that implements the Trajectory interface.
            physics_dt (float): Duration of a physics step in Isaac Sim (typically 1/60 s).
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, trajectory: isaacsim.robot_motion.motion_generation.trajectory.Trajectory, physics_dt: float) -> None:
        ...
    def get_action_at_time(self, time: float) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Get an ArticulationAction that will send the robot to the desired position/velocity at a given time in the provided Trajectory.
        
                Args:
                    time (float): Time between the start and end times in the provided Trajectory.  If the time is out of bounds, an error will be thrown.
        
                Returns:
                    ArticulationAction: ArticulationAction that may be passed directly to the robot Articulation to send it to the desired position/velocity at the given time.
                
        """
    def get_action_sequence(self, timestep: float = None) -> typing.List[isaacsim.core.utils.types.ArticulationAction]:
        """
        Get a sequence of ArticulationActions which sample the entire Trajectory according to the provided timestep.
        
                Args:
                    timestep (float, optional): Timestep used for sampling the provided Trajectory.
                        A vlue of 1/60, for example, returns ArticulationActions that represent the desired position/velocity of
                        the robot at 1/60 second intervals.  I.e. a one second trajectory with timestep=1/60 would result in 60 ArticulationActions.
                        When not provided, the framerate of Isaac Sim is used. Defaults to None.
        
                Returns:
                    List[ArticulationAction]: Sequence of ArticulationActions that may be passed to the robot Articulation to produce the desired trajectory.
                
        """
    def get_active_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        Get view into active joints
        
                Returns:
                    ArticulationSubset: Returns robot states for active joints in an order compatible with the TrajectoryGenerator
                
        """
    def get_robot_articulation(self) -> isaacsim.core.prims.impl.single_articulation.SingleArticulation:
        """
        Get the robot Articulation
        
                Returns:
                    SingleArticulation: Articulation object describing the robot.
                
        """
    def get_trajectory(self) -> isaacsim.robot_motion.motion_generation.trajectory.Trajectory:
        ...
    def get_trajectory_duration(self) -> float:
        """
        Returns the duration of the provided Trajectory
        
                Returns:
                    float: Duration of the provided trajectory
                
        """
