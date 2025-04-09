from __future__ import annotations
import carb as carb
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import numpy
import typing
__all__ = ['AckermannController', 'ArticulationAction', 'BaseController', 'carb', 'np']
class AckermannController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    
        This controller uses a bicycle model for Ackermann drive. The controller computes the left turning angle, right turning angle, and wheel rotation velocity of a robot's angular wheels. The controller can be used to find the appropriate joint values of a wheeled robot when it is being steered at a specific speed. The conversions are
    
            .. math::
    
                	heta_R = \\arctan[frac{1}{R + t}(b)] 
    
                	heta_L = \\arctan[frac{1}{R - t}(b)] 
    
    
                \\pi_wRV = \\frac{1}{r}(s)
    
        where :math:`	heta` is the desired angle, `\\pi` is the desired wheel rotation velocity, :math:`R` is the turning radius, :math:`b` is the distance between rear and front axles, :math:`t` is the wheel turning distance, :math:`r` is the wheel turning radius, and :math:`s` is the speed of the robot.
    
    
        Args:
            name (str): [description]
            wheel_base (float): Distance between front and rear axles in m
            track_width (float): Distance between left and right rear wheels of the robot in m
            turning_wheel_radius (float): Radius of the front wheels of the robot in m
            acceleration (float): Desired forward acceleration for the robot in m/s^2
            max_wheel_velocity (float): Maximum angular velocity of the robot wheel in rad/s
            use_acceleration (bool): Default set to false to use speed as input instead; use acceleration as an input when set to True
            invert_steering_angle (bool): Flips the sign of the steering angle; set to true for rear wheel steering
            max_wheel_rotation_angle (float): limits the maximum linear speed that will be produced by the controller. Defaults to 6.28 rad.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, wheel_base: float, track_width: float, turning_wheel_radius: float, max_wheel_velocity: float = 1e+20, use_acceleration: bool = False, invert_steering_angle: bool = False, max_wheel_rotation_angle: float = 6.28) -> None:
        ...
    def forward(self, command: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Calculate right and left wheel angles given wheel rotation and velocity. If use_acceleration flag is enabled, desired velocity command (index 1) will be ignored.
        
                Args:
                    command (np.ndarray): steering angle (rad), linear velocity [speed] (m/s), current linear velocity [current speed y] (m/s), delta time (s), acceleration (m/s^2)
        
                Returns:
                    ArticulationAction: the articulation action to be applied to the robot.
                
        """
