from __future__ import annotations
import carb as carb
import isaacsim.core.api.robots.robot
from isaacsim.core.api.robots.robot import Robot
from isaacsim.core.utils.prims import define_prim
from isaacsim.core.utils.prims import get_prim_at_path
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import re as re
__all__ = ['ArticulationAction', 'Robot', 'WheeledRobot', 'carb', 'define_prim', 'get_prim_at_path', 'np', 're']
class WheeledRobot(isaacsim.core.api.robots.robot.Robot):
    """
    
        This class wraps and manages the articualtion for a two wheeled differential robot base. It is designed to be managed by the `World` simulation context and provides and API for applying actions, retrieving dof parameters, etc...
    
        Creating a wheeled robot can be done in a number of different ways, depending on the use case.
    
        * Most commonly, the robot and stage are preloaded, in which case only the prim path to the articualtion root and the joint labels are required. Joint labels can take the form of either the joint names or the joint indices in the articulation.
    
        .. code-block:: python
    
            jetbot = WheeledRobot(prim_path="/path/to/jetbot",
                                name="Joan",
                                wheel_dof_names=["left_wheel_joint", "right_wheel_joint"]
                                )
    
            armbot = WheeledRobot(prim_path="path/to/armbot"
                                    name="Weird_Arm_On_Wheels_Bot",
                                    wheel_dof_indices=[7, 8]
                                )
    
        * Alternatively, this class can create and populate a new reference on the stage.  This is done with the `create_robot` parameter set to True.
    
        .. code-block:: python
    
            carter = WheeledRobot(prim_path="/desired/path/to/carter",
                                    name = "Jimmy",
                                    wheel_dof_names=["joint_wheel_left", "joint_wheel_right"],
                                    create_robot = True,
                                    usd_path = "/Isaac/Robots/NVIDIA/Carter/nova_carter/nova_carter.usd",
                                    position = np.array([0,1,0])
                                )
    
        .. hint::
    
            In all cases, either `wheel_dof_names` or `wheel_dof_indices` must be specified!
    
    
        Args:
            prim_path (str): The stage path to the root prim of the articulation.
            name ([str]): The name used by `World` to identify the robot. Defaults to "wheeled_robot"
            robot_path (optional[str]): relative path from prim path to the robot.
            wheel_dof_names (semi-optional[str]): names of the wheel joints. Either this or the wheel_dof_indicies must be specified.
            wheel_dof_indices: (semi-optional[int]): indices of the wheel joints in the articulation. Either this or the wheel_dof_names must be specified.
            usd_path (optional[str]): nucleus path to the robot asset. Used if create_robot is True
            create_robot (bool): create robot at prim_path using asset from usd_path. Defaults to False
            position (Optional[np.ndarray], optional): The location to create the robot when create_robot is True. Defaults to None.
            orientation (Optional[np.ndarray], optional): The orientation of the robot when crate_robot is True. Defaults to None.
        
    """
    def __init__(self, prim_path: str, name: str = 'wheeled_robot', robot_path: typing.Optional[str] = None, wheel_dof_names: typing.Optional[str] = None, wheel_dof_indices: typing.Optional[int] = None, usd_path: typing.Optional[str] = None, create_robot: typing.Optional[bool] = False, position: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def apply_wheel_actions(self, actions: isaacsim.core.utils.types.ArticulationAction) -> None:
        """
        applying action to the wheels to move the robot
        
                Args:
                    actions (ArticulationAction): [description]
                
        """
    def get_articulation_controller_properties(self):
        ...
    def get_wheel_positions(self):
        """
        [summary]
        
                Returns:
                    List[float]: [description]
                
        """
    def get_wheel_velocities(self):
        """
        [summary]
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: [description]
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        """
        [summary]
        """
    def post_reset(self) -> None:
        """
        [summary]
        """
    def set_wheel_positions(self, positions) -> None:
        """
        [summary]
        
                Args:
                    positions (Tuple[float, float]): [description]
                
        """
    def set_wheel_velocities(self, velocities) -> None:
        """
        [summary]
        
                Args:
                    velocities (Tuple[float, float]): [description]
                
        """
    @property
    def wheel_dof_indices(self):
        """
        [summary]
        
                Returns:
                    int: [description]
                
        """
