from __future__ import annotations
import carb as carb
from isaacsim.core.utils.extensions import get_extension_path_from_name
import json as json
import os as os
__all__ = ['carb', 'get_extension_path_from_name', 'get_supported_robot_path_planner_pairs', 'get_supported_robot_policy_pairs', 'get_supported_robots_with_lula_kinematics', 'json', 'load_supported_lula_kinematics_solver_config', 'load_supported_motion_policy_config', 'load_supported_path_planner_config', 'os']
def _process_policy_config(mg_config_file):
    ...
def get_supported_robot_path_planner_pairs() -> dict:
    """
    Get a dictionary of PathPlanner names that are supported for each given robot name
    
        Returns:
            supported_planner_names_by_robot (dict): dictionary mapping robot names (keys) to a list of supported PathPlanner config files (values)
        
    """
def get_supported_robot_policy_pairs() -> dict:
    """
    Get a dictionary of MotionPolicy names that are supported for each given robot name
    
        Returns:
            supported_policy_names_by_robot (dict): dictionary mapping robot names (keys) to a list of supported MotionPolicy config files (values)
        
    """
def get_supported_robots_with_lula_kinematics() -> typing.List[str]:
    ...
def load_supported_lula_kinematics_solver_config(robot_name: str, policy_config_dir = None) -> dict:
    """
    Load lula kinematics solver for a supported robot.
        Use get_supported_robots_with_lula_kinematics() to get a list of robots with supported kinematics.
    
        Args:
            robot_name (str): name of robot
    
        Returns:
            solver_config (dict): a dictionary whose keyword arguments are sufficient to load the lula kinematics solver.
                e.g. lula.LulaKinematicsSolver(**load_supported_lula_kinematics_solver_config("Franka"))
    
        
    """
def load_supported_motion_policy_config(robot_name: str, policy_name: str, policy_config_dir: str = None) -> dict:
    """
    Load a MotionPolicy object by specifying the robot name and policy name
        For a dictionary mapping supported robots to supported policies on those robots,
        use get_supported_robot_policy_pairs()
    
        To use this loader for a new policy, a user may copy the config file structure found under /motion_policy_configs/
        in the motion_generation extension, passing in a path to a directory containing a "policy_map.json"
    
        Args:
            robot_name (str): name of robot
            policy_name (str): name of MotionPolicy
            policy_config_dir (str): path to directory where a policy_map.json file is stored,
                defaults to ".../isaacsim.robot_motion.motion_generation/motion_policy_configs"
    
        Returns:
            policy_config (dict): a dictionary whose keyword arguments are sufficient to load the desired motion policy
                e.g. lula.motion_policies.RmpFlow(**load_supported_motion_policy_config("Franka","RMPflow"))
        
    """
def load_supported_path_planner_config(robot_name: str, planner_name: str, policy_config_dir: str = None) -> dict:
    ...
