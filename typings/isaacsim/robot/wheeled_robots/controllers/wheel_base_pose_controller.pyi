from __future__ import annotations
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
from isaacsim.core.utils.rotations import quat_to_euler_angles
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import math as math
import numpy as np
import numpy
import typing
__all__ = ['ArticulationAction', 'BaseController', 'WheelBasePoseController', 'math', 'np', 'quat_to_euler_angles']
class WheelBasePoseController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    
        This controller closes the control loop, returning the wheel commands that will drive the robot to a desired pose. It does this by exploiting an open loop controller for the robot passed at class initialization.
    
        .. hint::
    
            The logic for this controller is the following:
    
            * calculate the difference between the current position and the target position, amd compare against the postion tolerance. If the result is inside the tolerance, stop forward motion (ie. stop if closer than position tolerance)
    
            * calculate the difference between the current heading and the target heading, and compare against the heading tolerance. If the result is outside the tolerance, stop forward motion and turn to align with the target heading (ie. dont bother turning unless it's by more than the heading tolerance)
    
            * otherwise proceed forward
    
        Args:
            name (str): [description]
            open_loop_wheel_controller (BaseController): A controller that takes in a command of
                                                        [longitudinal velocity, steering angle] and returns the
                                                        ArticulationAction to be applied to the wheels if non holonomic.
                                                        and [longitudinal velocity, latitude velocity, steering angle]
                                                        if holonomic.
            is_holonomic (bool, optional): [description]. Defaults to False.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, open_loop_wheel_controller: isaacsim.core.api.controllers.base_controller.BaseController, is_holonomic: bool = False) -> None:
        ...
    def forward(self, start_position: numpy.ndarray, start_orientation: numpy.ndarray, goal_position: numpy.ndarray, lateral_velocity: float = 0.2, yaw_velocity: float = 0.5, heading_tol: float = 0.05, position_tol: float = 0.04) -> isaacsim.core.utils.types.ArticulationAction:
        """
        
                Use the specified open loop controller to compute speed commands to the wheel joints of the robot that will move it towards the specified goal position
        
                Args:
                    start_position (np.ndarray): The current position of the robot, (X, Y, Z)
                    start_orientation (np.ndarray): The current orientation quaternion of the robot, (W, X, Y, Z)
                    goal_position (np.ndarray): The desired target position, (X, Y, Z)
                    lateral_velocity (float, optional): How fast the robot will move forward. Defaults to 20.0.
                    yaw_velocity (float, optional): How fast the robot will turn. Defaults to 0.5.
                    heading_tol (float, optional): The heading tolerance. Defaults to 0.05.
                    position_tol (float, optional): The position tolerance. Defaults to 4.0.
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def reset(self) -> None:
        """
        [summary]
        """
