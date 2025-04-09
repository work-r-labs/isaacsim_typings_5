from __future__ import annotations
import carb as carb
import isaacsim.core.api.articulations.articulation_subset
from isaacsim.core.api.articulations.articulation_subset import ArticulationSubset
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot_motion.motion_generation.path_planning_interface
from isaacsim.robot_motion.motion_generation.path_planning_interface import PathPlanner
import numpy as np
import numpy
__all__ = ['ArticulationAction', 'ArticulationSubset', 'PathPlanner', 'PathPlannerVisualizer', 'SingleArticulation', 'carb', 'np']
class PathPlannerVisualizer:
    """
    A helper class for quickly visualizing the plans output by a PathPlanner.
        The main utility of this class lies in the compute_plan_as_articulation_actions() function, which returns a sequence of
        ArticulationActions that may be directly sent to the robot Articulation in order to visualize the planned path.
    
        Args:
            robot_articulation (SingleArticulation): An Articulation object describing a single simulated robot.
            path_planner (PathPlanner):  A PathPlanner object that has been configured to compute plans for the robot
                represented by the robot Articulation.
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, path_planner: isaacsim.robot_motion.motion_generation.path_planning_interface.PathPlanner) -> None:
        ...
    def compute_plan_as_articulation_actions(self, max_cspace_dist: float = 0.05) -> typing.List[isaacsim.core.utils.types.ArticulationAction]:
        """
        Compute plan using a PathPlanner and linearly interpolate the result to enforce that the maximum
                distance (l2 norm) between any two points is max_cspace_dist.
        
                Args:
                    max_cspace_dist (float, optional): Maximum distance between adjacent points in the path. Defaults to 0.05.
        
                Returns:
                    List[ArticulationAction]: Linearly interpolated path given as a sequence of ArticulationActions that can be
                        passed directly to the robot Articulation.  This may rearrange and augment the plan output by the PathPlanner to
                        match the number of DOFs available for control in the robot Articulation.
                
        """
    def get_active_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        Get view into active joints
        
                Returns:
                    ArticulationSubset: Returns robot states for active joints in an order compatible with the PathPlanner
                
        """
    def get_path_planner(self) -> isaacsim.robot_motion.motion_generation.path_planning_interface.PathPlanner:
        """
        Get the PathPlanner that is being used to generate paths
        
                Returns:
                    PathPlanner: An instance of the PathPlanner interface for generating sparse paths to a target pose
                
        """
    def get_robot_articulation(self) -> isaacsim.core.prims.impl.single_articulation.SingleArticulation:
        """
        Get the robot Articulation
        
                Returns:
                    SingleArticulation: Articulation object describing the robot.
                
        """
    def get_watched_joints_subset(self) -> isaacsim.core.api.articulations.articulation_subset.ArticulationSubset:
        """
        Get view into watched joints
        
                Returns:
                    ArticulationSubset: Returns robot states for watched joints in an order compatible with the PathPlanner
                
        """
    def interpolate_path(self, path: numpy.array, max_cspace_dist: float = 0.05) -> numpy.array:
        """
        Linearly interpolate a sparse path such that the maximum distance (l2 norm) between any two points is max_cspace_dist
        
                Args:
                    path (np.array): Sparse cspace path with shape (N x num_dofs) where N is number of points in the path
                    max_cspace_dist (float, optional): _description_. Defaults to 0.05.
        
                Returns:
                    np.array: Linearly interpolated path with shape (M x num_dofs)
                
        """
