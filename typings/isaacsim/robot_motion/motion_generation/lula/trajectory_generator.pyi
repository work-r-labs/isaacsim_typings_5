from __future__ import annotations
import carb as carb
from isaacsim.robot_motion.motion_generation.lula.kinematics import LulaKinematicsSolver
from isaacsim.robot_motion.motion_generation.lula.utils import get_pose3
import isaacsim.robot_motion.motion_generation.trajectory
from isaacsim.robot_motion.motion_generation.trajectory import Trajectory
import lula as lula
import numpy as np
import numpy
__all__ = ['LulaCSpaceTrajectoryGenerator', 'LulaKinematicsSolver', 'LulaTaskSpaceTrajectoryGenerator', 'LulaTrajectory', 'Trajectory', 'carb', 'get_pose3', 'lula', 'np']
class LulaCSpaceTrajectoryGenerator:
    """
    LulaCSpaceTrajectoryGenerator is a class for generating time-optimal trajectories that connect a series of
        provided c-space waypoints.
    
        Args:
            robot_description_path (str): path to a robot description yaml file
            urdf_path (str): path to robot urdf
        
    """
    def __init__(self, robot_description_path: str, urdf_path: str) -> None:
        ...
    def compute_c_space_trajectory(self, waypoint_positions: numpy.array) -> LulaTrajectory:
        """
        Produce a trajectory from a set of provided c_space waypoint positions.  The resulting trajectory
                will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0.  The trajectory is time-optimal:
                i.e. either the velocity, acceleration, or jerk limits are saturated at any given time to produce as trajectory with as short a duration as possible.
        
                Args:
                    waypoint_positions (np.array): Set of c-space coordinates cooresponding to the output of get_active_joints().
                        The expected shape is (N x k) where N is the number of waypoints and k is the number of active joints.
        
                Returns:
                    LulaTrajectory: Instance of the Trajectory class which specifies continuous joint_targets for the active joints over a span of time.
                        If a trajectory could not be produced, None will be returned.
                
        """
    def compute_timestamped_c_space_trajectory(self, waypoint_positions: numpy.array, timestamps: numpy.array, interpolation_mode: str = 'cubic_spline') -> LulaTrajectory:
        """
        Compute a trajectory where each c_space waypoint has a corresponding timestamp that will be exactly matched.
                The resulting trajectory will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0.
        
        
                Args:
                    waypoint_positions (np.array): Set of c-space coordinates cooresponding to the output of get_active_joints().
                        The expected shape is (N x k) where N is the number of waypoints and k is the number of active joints.
                    timestamps (np.array): Set of timestamps corresponding to the waypoint positions argument with an expected shape of (Nx1).
                    interpolation_mode (str, optional): The type of interpolation to be used between waypoints.
                        The available options are "cubic_spline" and "linear". Defaults to "cubic".
        
                Returns:
                    LulaTrajectory: Instance of the Trajectory class which specifies continuous joint_targets for the active joints over a span of time.
                        If a trajectory could not be produced, None will be returned.
                
        """
    def get_active_joints(self) -> typing.List[str]:
        """
        Return the list of joints by name that are considered to be controllable by the TrajectoryGenerator.
                All inputs and outputs of the LulaTrajectoryGenerator correspond to the joints specified by get_active_joints().
        
                Returns:
                    List[str]: List of joints that are used to generate the desired trajectory.
                
        """
    def get_c_space_acceleration_limits(self):
        """
        Get the acceleration limits of the active joints that are used when generating a trajectory
        
                Returns:
                    acceleration limits (np.array): Acceleration limits of active joints.
                
        """
    def get_c_space_jerk_limits(self):
        """
        Get the jerk limits of the active joints that are used when generating a trajectory
        
                Returns:
                    jerk limits (np.array): Jerk limits of active joints.
                
        """
    def get_c_space_position_limits(self):
        """
        Get the position limits of the active joints that are used when generating a trajectory
        
                Returns:
                    position limits (np.array): Position limits of active joints.
                
        """
    def get_c_space_velocity_limits(self):
        """
        Get the velocity limits of the active joints that are used when generating a trajectory
        
                Returns:
                    velocity limits (np.array): Velocity limits of active joints.
                
        """
    def set_c_space_acceleration_limits(self, acceleration_limits: numpy.array) -> None:
        """
        Set the acceleration limits of the active joints to be used when generating a trajectory.
        
                Args:
                    acceleration_limits (np.array): Acceleration limits of active joints.
                
        """
    def set_c_space_jerk_limits(self, jerk_limits: numpy.array) -> None:
        """
        Set the jerk limits of the active joints to be used when generating a trajectory.
        
                Args:
                    jerk_limits (np.array): Jerk limits of active joints.
                
        """
    def set_c_space_position_limits(self, lower_position_limits: numpy.array, upper_position_limits: numpy.array) -> None:
        """
        Set the lower and upper position limits of the active joints to be used when generating a trajectory.
        
                Args:
                    lower_position_limits (np.array): Lower position limits of active joints.
                    upper_position_limits (np.array): Upper position limits of active joints.
                
        """
    def set_c_space_velocity_limits(self, velocity_limits: numpy.array) -> None:
        """
        Set the velocity limits of the active joints to be used when generating a trajectory.
        
                Args:
                    velocity_limits (np.array): Velocity limits of active joints.
                
        """
    def set_solver_param(self, param_name: str, param_val: typing.Union[int, float, str]):
        """
        Set solver parameters for the cspace trajectory generator.  A complete list of
                parameters is provided in this docstring.
        
                'max_segment_iterations': (int)
                    In general, a trajectory is locally time-optimal if at least one derivative for one of the
                    c-space coordinates is fully saturated, with no derivative limits for any of the c-space
                    coordinates exceeded.
        
                    This time-optimality can be enforced for each `CubicSpline` segment or for each
                    `PiecewiseCubicSpline` as a whole. The former will, in general, generate trajectories with
                    smaller spans, but will require more expensive iterations (and thus more time) to converge.
                    The latter will, in general, require less iterations (and thus less time) to converge, but
                    the generated trajectories will tend to have longer spans.
        
                    When attempting to find a time-optimal trajectory, the (more expensive) per-segment method
                    will first be attempted for `max_per_segment_iterations`. Then, if not yet converged, the
                    method acting on the entire spline will be attempted for `max_aggregate_iterations`.
        
                    To maximize speed, `max_segment_iterations` should be relatively low (or even zero to remove
                    this search completely). To maximize time-optimality of the generated trajectory,
                    `max_segment_iterations` should be relatively high.
        
                    The sum of `max_segment_iterations` and `max_aggregate_iterations` must be at least 1
        
                'max_aggragate_iterations': (int)
                    See max_segment_iterations
        
                'convergence_dt': (float)
                    The search for optimal time values will terminate if the maximum change to any time value
                    during a given iteration is less than the `convergence_dt`.
        
                    `convergence_dt` must be positive.
        
                'max_dilation_iterations': (int)
                    After the segment-wise and/or aggregate time-optimal search has converged or reached maximum
                    iterations, the resulting set of splines will be tested to see if any derivative limits are
                    exceeded.
        
                    If any derivative limits are exceeded, the splines will be iteratively scaled in time to
                    reduce the maximum achieved derivative. This process will repeat until no derivative limits
                    are exceeded (success) or `max_dilation_iterations_` are reached (failure).
                    For a well-tuned set of solver parameters, very few dilation steps should be required
                    (often none will be required or a single iteration is sufficient to bring a slightly
                    over-saturated trajectory within the derivative limits).
        
                'dilation_dt': (float)
                    For the iterative dilation step described in `setMaxDilationIterations()` documentation, the
                    `dilation_dt` is the "epsilon" value added to the span of the trajectory that exceeds
                    derivative limits.
        
                    `dilation_dt` must be positive.
        
                'min_time_span': (float)
                    Specify the minimum allowable time span between adjacent waypoints/endpoints.
                    `min_time_span` must be positive.
        
                    This is most likely to affect the time span between the endpoints and "free-position" points
                    that are used to enable acceleration bound constraints. If no jerk limit is provided, these free-position points may
                    tend to become arbitrarily close in position and time to the endpoints. This `min_time_span`
                    prevents this time span from approaching zero.
        
                    In general, a jerk limit is recommended for preventing abrupt changes in acceleration rather
                    than relying on the `min_time_span` for this purpose.
        
                'time_split_method': (string)
                    Often waypoints for a trajectory may specify positions without providing time values for when
                    these waypoint position should be attained. In this case, we can use the distance between
                    waypoints to assign time values for each waypoint.
        
                    Assuming a unitary time domain s.t. t_0 = 0 and t_N = 1, we can assign the intermediate time
                    values according to:
        
                      t_k = t_(k-1) + (d_k / d),
        
                    where d = sum(d_k) for k = [0, N-1] and N is the number of points.
        
                    Many options exist for the computing the distance metric d_k, with common options described
                    below (and implemented in `ComputeTimeValues()`.
                    See Eqn 4.37 in "Trajectory Planning for Automatic Machines and Robots" (2008) by
                    Biagiotti & Melchiorri for more detailed motivations.
                    Valid distribution choices are given below:
        
                    'uniform':
                        For a "uniform distribution" w.r.t time, the positions are ignored and d_k can simply be
                        computed as:
        
                          d_k = 1 / (N - 1)
        
                        resulting in uniform time intervals between all points.
        
                    'chord_length':
                        For a "chord length distribution", the time intervals between waypoints are proportional to
                        the Euclidean distance between waypoints:
        
                          d_k = \\|q_(k+1) - q_k\\|
        
                        where q represents the position of the waypoint.
        
                    'centripetal':
                        For a "centripetal distribution", the time intervals between waypoints are proportional to the
                        square root of the Euclidean distance between waypoints:
        
                          d_k = \\|q_(k+1) - q_k\\|^(1/2)
        
                        where q represents the position of the waypoint.
        
                Args:
                    param_name (str): Parameter name from the above list of parameters
                    param_val (Union[int, float, str]): Value to which the given parameter will be set
                
        """
class LulaTaskSpaceTrajectoryGenerator:
    def __init__(self, robot_description_path: str, urdf_path: str) -> None:
        ...
    def compute_task_space_trajectory_from_path_spec(self, path_spec: typing.Union[lula.CompositePathSpec, lula.TaskSpacePathSpec], frame_name: str) -> LulaTrajectory:
        """
        Return a LulaTrajectory that follows the path specified by the provided TaskSpacePathSpec
        
                Args:
                    task_space_path_spec (lula.TaskSpacePathSpec, lula.CompositePathSpec): An object describing a taskspace path
                    frame_name (str): Name of the end effector frame
        
                Returns:
                    LulaTrajectory: Instance of the isaacsim.robot_motion.motion_generation.Trajectory class.  If no trajectory could be generated, None is returned.
                
        """
    def compute_task_space_trajectory_from_points(self, positions: numpy.array, orientations: numpy.array, frame_name: str) -> LulaTrajectory:
        """
        Return a LulaTrajectory that connects the provided positions and orientations at the specified frame in the robot.  Points will be connected linearly in space.
        
                Args:
                    positions (np.array): Taskspace positions that the robot end effector should pass through with shape (N x 3) where N is the number of provided positions.
                        Positions is assumed to be in meters.
                    orientations (np.array): Taskspace quaternion orientations that the robot end effector should pass through with shape (N x 4) where N is the number of provided
                        orientations.  The length of this argument must match the length of the positions argument.
                    frame_name (str): Name of the end effector frame in the robot URDF.
        
                Returns:
                    LulaTrajectory: Instance of the isaacsim.robot_motion.motion_generation.Trajectory class.  If no trajectory could be generated, None is returned.
                
        """
    def get_active_joints(self) -> typing.List[str]:
        """
        Return the list of joints by name that are considered to be controllable by the TrajectoryGenerator.
                All inputs and outputs of the LulaTrajectoryGenerator correspond to the joints specified by get_active_joints().
        
                Returns:
                    List[str]: List of joints that are used to generate the desired trajectory.
                
        """
    def get_all_frame_names(self) -> typing.List[str]:
        """
        Return a list of all frames in the robot URDF that may be used to follow a trajectory
        
                Returns:
                    List[str]: List of all frame names in the robot URDF
                
        """
    def get_c_space_acceleration_limits(self):
        """
        Get the acceleration limits of the active joints that are used when generating a trajectory
        
                Returns:
                    acceleration limits (np.array): Acceleration limits of active joints.
                
        """
    def get_c_space_jerk_limits(self):
        """
        Get the jerk limits of the active joints that are used when generating a trajectory
        
                Returns:
                    jerk limits (np.array): Jerk limits of active joints.
                
        """
    def get_c_space_position_limits(self):
        """
        Get the position limits of the active joints that are used when generating a trajectory
        
                Returns:
                    position limits (np.array): Position limits of active joints.
                
        """
    def get_c_space_velocity_limits(self):
        """
        Get the velocity limits of the active joints that are used when generating a trajectory
        
                Returns:
                    velocity limits (np.array): Velocity limits of active joints.
                
        """
    def get_path_conversion_config(self) -> lula.TaskSpacePathConversionConfig:
        """
        Get a reference to the config object that lula uses to convert task-space paths to c-space paths.
        
                The values of the returned TaskSpacePathConversionConfig object can be modified directly to affect lula task-space path conversions.
                See help(lula.TaskSpacePathConversionConfig) for a detailed description of the editable parameters.
        
                Returns:
                    lula.TaskSpacePathConversionConfig: Configuration class for converting from task-space paths to c-space paths.
                
        """
    def set_c_space_acceleration_limits(self, acceleration_limits: numpy.array) -> None:
        """
        Set the acceleration limits of the active joints to be used when generating a trajectory.
        
                Args:
                    acceleration_limits (np.array): Acceleration limits of active joints.
                
        """
    def set_c_space_jerk_limits(self, jerk_limits: numpy.array) -> None:
        """
        Set the jerk limits of the active joints to be used when generating a trajectory.
        
                Args:
                    jerk_limits (np.array): Jerk limits of active joints.
                
        """
    def set_c_space_position_limits(self, lower_position_limits: numpy.array, upper_position_limits: numpy.array) -> None:
        """
        Set the lower and upper position limits of the active joints to be used when generating a trajectory.
        
                Args:
                    lower_position_limits (np.array): Lower position limits of active joints.
                    upper_position_limits (np.array): Upper position limits of active joints.
                
        """
    def set_c_space_trajectory_generator_solver_param(self, param_name: str, param_val: typing.Union[int, float, str]):
        """
        Set solver parameters for the cspace trajectory generator.  A complete list of
                parameters is provided in this docstring.
        
                'max_segment_iterations': (int)
                    In general, a trajectory is locally time-optimal if at least one derivative for one of the
                    c-space coordinates is fully saturated, with no derivative limits for any of the c-space
                    coordinates exceeded.
        
                    This time-optimality can be enforced for each `CubicSpline` segment or for each
                    `PiecewiseCubicSpline` as a whole. The former will, in general, generate trajectories with
                    smaller spans, but will require more expensive iterations (and thus more time) to converge.
                    The latter will, in general, require less iterations (and thus less time) to converge, but
                    the generated trajectories will tend to have longer spans.
        
                    When attempting to find a time-optimal trajectory, the (more expensive) per-segment method
                    will first be attempted for `max_per_segment_iterations`. Then, if not yet converged, the
                    method acting on the entire spline will be attempted for `max_aggregate_iterations`.
        
                    To maximize speed, `max_segment_iterations` should be relatively low (or even zero to remove
                    this search completely). To maximize time-optimality of the generated trajectory,
                    `max_segment_iterations` should be relatively high.
        
                    The sum of `max_segment_iterations` and `max_aggregate_iterations` must be at least 1
        
                'max_aggragate_iterations': (int)
                    See max_segment_iterations
        
                'convergence_dt': (float)
                    The search for optimal time values will terminate if the maximum change to any time value
                    during a given iteration is less than the `convergence_dt`.
        
                    `convergence_dt` must be positive.
        
                'max_dilation_iterations': (int)
                    After the segment-wise and/or aggregate time-optimal search has converged or reached maximum
                    iterations, the resulting set of splines will be tested to see if any derivative limits are
                    exceeded.
        
                    If any derivative limits are exceeded, the splines will be iteratively scaled in time to
                    reduce the maximum achieved derivative. This process will repeat until no derivative limits
                    are exceeded (success) or `max_dilation_iterations_` are reached (failure).
                    For a well-tuned set of solver parameters, very few dilation steps should be required
                    (often none will be required or a single iteration is sufficient to bring a slightly
                    over-saturated trajectory within the derivative limits).
        
                'dilation_dt': (float)
                    For the iterative dilation step described in `setMaxDilationIterations()` documentation, the
                    `dilation_dt` is the "epsilon" value added to the span of the trajectory that exceeds
                    derivative limits.
        
                    `dilation_dt` must be positive.
        
                'min_time_span': (float)
                    Specify the minimum allowable time span between adjacent waypoints/endpoints.
                    `min_time_span` must be positive.
        
                    This is most likely to affect the time span between the endpoints and "free-position" points
                    that are used to enable acceleration bound constraints. If no jerk limit is provided, these free-position points may
                    tend to become arbitrarily close in position and time to the endpoints. This `min_time_span`
                    prevents this time span from approaching zero.
        
                    In general, a jerk limit is recommended for preventing abrupt changes in acceleration rather
                    than relying on the `min_time_span` for this purpose.
        
                'time_split_method': (string)
                    Often waypoints for a trajectory may specify positions without providing time values for when
                    these waypoint position should be attained. In this case, we can use the distance between
                    waypoints to assign time values for each waypoint.
        
                    Assuming a unitary time domain s.t. t_0 = 0 and t_N = 1, we can assign the intermediate time
                    values according to:
        
                      t_k = t_(k-1) + (d_k / d),
        
                    where d = sum(d_k) for k = [0, N-1] and N is the number of points.
        
                    Many options exist for the computing the distance metric d_k, with common options described
                    below (and implemented in `ComputeTimeValues()`.
                    See Eqn 4.37 in "Trajectory Planning for Automatic Machines and Robots" (2008) by
                    Biagiotti & Melchiorri for more detailed motivations.
                    Valid distribution choices are given below:
        
                    'uniform':
                        For a "uniform distribution" w.r.t time, the positions are ignored and d_k can simply be
                        computed as:
        
                          d_k = 1 / (N - 1)
        
                        resulting in uniform time intervals between all points.
        
                    'chord_length':
                        For a "chord length distribution", the time intervals between waypoints are proportional to
                        the Euclidean distance between waypoints:
        
                          d_k = \\|q_(k+1) - q_k\\|
        
                        where q represents the position of the waypoint.
        
                    'centripetal':
                        For a "centripetal distribution", the time intervals between waypoints are proportional to the
                        square root of the Euclidean distance between waypoints:
        
                          d_k = \\|q_(k+1) - q_k\\|^(1/2)
        
                        where q represents the position of the waypoint.
        
                Args:
                    param_name (str): Parameter name from the above list of parameters
                    param_val (Union[int, float, str]): Value to which the given parameter will be set
                
        """
    def set_c_space_velocity_limits(self, velocity_limits: numpy.array) -> None:
        """
        Set the velocity limits of the active joints to be used when generating a trajectory.
        
                Args:
                    velocity_limits (np.array): Velocity limits of active joints.
                
        """
class LulaTrajectory(isaacsim.robot_motion.motion_generation.trajectory.Trajectory):
    """
    Instance of Trajectory interface class for handling lula.Trajectory objects
    
        Args:
            trajectory (lula.Trajectory): C-space trajectory defined continuously
        
    """
    def __init__(self, trajectory, active_joints):
        ...
    def get_active_joints(self) -> typing.List[str]:
        ...
    def get_joint_targets(self, time) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        ...
    @property
    def end_time(self) -> float:
        ...
    @property
    def start_time(self) -> float:
        ...
