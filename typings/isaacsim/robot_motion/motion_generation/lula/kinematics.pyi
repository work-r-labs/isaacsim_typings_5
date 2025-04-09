from __future__ import annotations
from isaacsim.core.utils.numpy.rotations import quats_to_rot_matrices
from isaacsim.core.utils.stage import get_stage_units
import isaacsim.robot_motion.motion_generation.kinematics_interface
from isaacsim.robot_motion.motion_generation.kinematics_interface import KinematicsSolver
from isaacsim.robot_motion.motion_generation.lula.interface_helper import LulaInterfaceHelper
from isaacsim.robot_motion.motion_generation.lula import utils as lula_utils
import lula as lula
import numpy
import numpy as np
__all__ = ['KinematicsSolver', 'LulaInterfaceHelper', 'LulaKinematicsSolver', 'get_stage_units', 'lula', 'lula_utils', 'np', 'quats_to_rot_matrices']
class LulaKinematicsSolver(isaacsim.robot_motion.motion_generation.kinematics_interface.KinematicsSolver):
    """
    A Lula-based implementaion of the KinematicsSolver interface.  Lula uses a URDF file describing the robot and
        a custom yaml file that specifies the cspace of the robot and other parameters.
    
        This class provides functions beyond the KinematicsSolver interface for getting and setting solver parameters.
        Inverse kinematics is solved quickly by first approximating a solution with cyclic coordinate descent (CCD) and then
        refining the solution with a second-order method (bfgs).  As such, parameters for both solvers are available and changable
        as properties of this class.
    
        Args:
            robot_description_path (str): path to a robot description yaml file describing the cspace of the robot and other relevant parameters
            urdf_path (str): path to a URDF file describing the robot
            robot_description (Optional[lula.RobotDescription]):  An initialized lula.RobotDescription object.  Other Lula-based classes such as RmpFlow may use
                a lula.RobotDescription object that they have already created to initialize a LulaKinematicsSolver.  When specified, the provided file paths are unused.
                Defaults to None.
        
    """
    def __init__(self, robot_description_path: str, urdf_path: str, robot_description: typing.Optional[lula.RobotDescription] = None):
        ...
    def _lula_orientation_tol_to_rad_tol(self, tol):
        ...
    def _rad_tol_to_lula_orientation_tol(self, tol):
        ...
    def compute_forward_kinematics(self, frame_name: str, joint_positions: numpy.array, position_only: typing.Optional[bool] = False) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Compute the position of a given frame in the robot relative to the USD stage global frame
        
                Args:
                    frame_name (str): Name of robot frame on which to calculate forward kinematics
                    joint_positions (np.array): Joint positions for the joints returned by get_joint_names()
                    position_only (bool): Lula Kinematics ignore this flag and always computes both position and orientation
        
                Returns:
                    Tuple[np.array,np.array]:
                    frame_positions: (3x1) vector describing the translation of the frame relative to the USD stage origin
        
                    frame_rotation: (3x3) rotation matrix describing the rotation of the frame relative to the USD stage global frame
                
        """
    def compute_inverse_kinematics(self, frame_name: str, target_position: numpy.array, target_orientation: numpy.array = None, warm_start: numpy.array = None, position_tolerance: float = None, orientation_tolerance: float = None) -> typing.Tuple[<built-in function array>, bool]:
        """
        Compute joint positions such that the specified robot frame will reach the desired translations and rotations.
                Lula Kinematics interpret the orientation tolerance as being the maximum rotation separating any standard axes.
                e.g. For a tolerance of .1: The X axes, Y axes, and Z axes of the rotation matrices may independently be as far as .1 radians apart
        
                Default values for position and orientation tolerances may be seen and changed with setter and getter functions.
        
                Args:
                    frame_name (str): name of the target frame for inverse kinematics
                    target_position (np.array): target translation of the target frame (in stage units) relative to the USD stage origin
                    target_orientation (np.array): target orientation of the target frame relative to the USD stage global frame. Defaults to None.
                    warm_start (np.array): a starting position that will be used when solving the IK problem.  If default cspace seeds have been set,
                        the warm start will be given priority, but the default seeds will still be used. Defaults to None.
                    position_tolerance (float): l-2 norm of acceptable position error (in stage units) between the target and achieved translations. Defaults to None.
                    orientation tolerance (float): magnitude of rotation (in radians) separating the target orientation from the achieved orienatation.
                        orientation_tolerance is well defined for values between 0 and pi.  Defaults to None.
        
                Returns:
                    Tuple[np.array,bool]:
                    joint_positions: in the order specified by get_joint_names() which result in the target frame acheiving the desired position
        
                    success: True if the solver converged to a solution within the given tolerances
                
        """
    def get_all_frame_names(self) -> typing.List[str]:
        ...
    def get_cspace_acceleration_limits(self) -> numpy.array:
        """
        Get the default acceleration limits of the active joints.
                Default acceleration limits are read from the robot_description YAML file.
                Any acceleration limits that are not specified in the robot_description YAML file will
                be None.
        
                Returns:
                    np.array: Default acceleration limits of the active joints.
                
        """
    def get_cspace_jerk_limits(self) -> numpy.array:
        """
        Get the default jerk limits of the active joints.
                Default jerk limits are read from the robot_description YAML file.
                Any jerk limits that are not specified in the robot_description YAML file will
                be None.
        
                Returns:
                    np.array: Default jerk limits of the active joints.
                
        """
    def get_cspace_position_limits(self) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Get the default upper and lower joint limits of the active joints.
        
                Returns:
                    Tuple[np.array, np.array]:
                    default_lower_joint_position_limits : Default lower position limits of active joints
        
                    default_upper_joint_position_limits : Default upper position limits of active joints
                
        """
    def get_cspace_velocity_limits(self) -> numpy.array:
        """
        Get the default velocity limits of the active joints
        
                Returns:
                    np.array: Default velocity limits of the active joints
                
        """
    def get_default_cspace_seeds(self) -> typing.List[<built-in function array>]:
        """
        Get a list of cspace seeds that the solver may use as starting points for solutions
        
                Returns:
                    List[np.array]: An N x num_dof list of cspace seeds
                
        """
    def get_default_orientation_tolerance(self) -> float:
        """
        Get the default orientation tolerance to be used when calculating IK when none is specified
        
                Returns:
                    float: magnitude of rotation (in radians) separating the target orientation from the achieved orienatation.
                        orientation_tolerance is well defined for values between 0 and pi.
                
        """
    def get_default_position_tolerance(self) -> float:
        """
        Get the default position tolerance to be used when calculating IK when none is specified
        
                Returns:
                    float: l-2 norm of acceptable position error (in stage units) between the target and achieved translations
                
        """
    def get_joint_names(self) -> typing.List[str]:
        ...
    def set_default_cspace_seeds(self, seeds: numpy.array) -> None:
        """
        Set a list of cspace seeds that the solver may use as starting points for solutions
        
                Args:
                    seeds (np.array): An N x num_dof list of cspace seeds
                
        """
    def set_default_orientation_tolerance(self, tolerance: float) -> None:
        """
        Default orientation tolerance to be used when calculating IK when none is specified
        
                Args:
                    tolerance (float): magnitude of rotation (in radians) separating the target orientation from the achieved orienatation.
                        orientation_tolerance is well defined for values between 0 and pi.
                
        """
    def set_default_position_tolerance(self, tolerance: float) -> None:
        """
        Default position tolerance to be used when calculating IK when none is specified
        
                Args:
                    tolerance (float): l-2 norm of acceptable position error (in stage units) between the target and achieved translations
                
        """
    def set_robot_base_pose(self, robot_position: numpy.array, robot_orientation: numpy.array) -> None:
        ...
    def supports_collision_avoidance(self) -> bool:
        """
        Lula Inverse Kinematics do not support collision avoidance with USD obstacles
        
                Returns:
                    bool: Always False
                
        """
    @property
    def bfgs_cspace_limit_biasing(self):
        """
        Indicate whether c-space limit avoidance is active for BFGS descent
        """
    @bfgs_cspace_limit_biasing.setter
    def bfgs_cspace_limit_biasing(self, value):
        ...
    @property
    def bfgs_cspace_limit_biasing_weight(self):
        """
        Relative weight applied to c-space limit error (if active).
        """
    @bfgs_cspace_limit_biasing_weight.setter
    def bfgs_cspace_limit_biasing_weight(self, value):
        ...
    @property
    def bfgs_cspace_limit_penalty_region(self):
        """
        Region near c-space limits which will induce penalties when c-space limit biasing is active.
        """
    @bfgs_cspace_limit_penalty_region.setter
    def bfgs_cspace_limit_penalty_region(self, value):
        ...
    @property
    def bfgs_gradient_norm_termination(self):
        """
        Minimal change in L2-norm of the error function gradient for early descent termination from BFGS descent.
        """
    @bfgs_gradient_norm_termination.setter
    def bfgs_gradient_norm_termination(self, value):
        ...
    @property
    def bfgs_gradient_norm_termination_coarse_scale_factor(self):
        """
        Ratio between 'bfgs_gradient_norm_termination' for coarse and fine stagesof BFGS descent.
        """
    @bfgs_gradient_norm_termination_coarse_scale_factor.setter
    def bfgs_gradient_norm_termination_coarse_scale_factor(self, value):
        ...
    @property
    def bfgs_max_iterations(self):
        """
        Number of iterations used for each BFGS descent.
        """
    @bfgs_max_iterations.setter
    def bfgs_max_iterations(self, value):
        ...
    @property
    def bfgs_orientation_weight(self):
        """
        Weight for the relative importance of orientation error during BFGS descent.
        """
    @bfgs_orientation_weight.setter
    def bfgs_orientation_weight(self, value):
        ...
    @property
    def bfgs_position_weight(self):
        """
        Weight for the relative importance of position error during BFGS descent.
        """
    @bfgs_position_weight.setter
    def bfgs_position_weight(self, value):
        ...
    @property
    def ccd_bracket_search_num_uniform_samples(self):
        """
        Number of samples used to identify valid three-point bracket for numerical optimization of c-space updates.
        """
    @ccd_bracket_search_num_uniform_samples.setter
    def ccd_bracket_search_num_uniform_samples(self, value):
        ...
    @property
    def ccd_descent_termination_delta(self):
        """
        Minimal change in c-space coordinates for early descent termination.
        """
    @ccd_descent_termination_delta.setter
    def ccd_descent_termination_delta(self, value):
        ...
    @property
    def ccd_max_iterations(self):
        """
        Number of iterations used for each cyclic coordinate descent.
        """
    @ccd_max_iterations.setter
    def ccd_max_iterations(self, value):
        ...
    @property
    def ccd_orientation_weight(self):
        """
        Weight for the relative importance of orientation error during CCD.
        """
    @ccd_orientation_weight.setter
    def ccd_orientation_weight(self, value):
        ...
    @property
    def ccd_position_weight(self):
        """
        Weight for the relative importance of position error during CCD.
        """
    @ccd_position_weight.setter
    def ccd_position_weight(self, value):
        ...
    @property
    def irwin_hall_sampling_order(self):
        """
        Sampling distribution for initial c-space positions.
        """
    @irwin_hall_sampling_order.setter
    def irwin_hall_sampling_order(self, value):
        ...
    @property
    def max_num_descents(self):
        """
        Maximum number of c-space positions that will be used as seeds.
        """
    @max_num_descents.setter
    def max_num_descents(self, value):
        ...
    @property
    def sampling_seed(self):
        """
        Seed for Irwin-Hall sampling of initial c-space positions
        """
    @sampling_seed.setter
    def sampling_seed(self, value):
        ...
