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
    
        This controller uses a bicycle model for Ackermann steering. The controller computes the left turning angle, right turning angle, and the rotation velocity of each wheel of a robot with no slip angle. The controller can be used to find the appropriate joint values of a wheeled robot with an Ackermann steering mechanism.
    
        Args:
    
            name (str): [description]
            wheel_base (float): Distance between front and rear axles in m
            track_width (float): Distance between left and right wheels of the robot in m
            front_wheel_radius (float): Radius of the front wheels of the robot in m. Defaults to 0.0 m but will equal back_wheel_radius if no value is inputted.
            back_wheel_radius (float): Radius of the back wheels of the robot in m. Defaults to 0.0 m but will equal front_wheel_radius if no value is inputted.
            max_wheel_velocity (float): Maximum angular velocity of the robot wheel in rad/s. Parameter is ignored if set to 0.0.
            invert_steering (bool): Set to true for rear wheel steering
            max_wheel_rotation_angle (float): The maximum wheel steering angle for the steering wheels. Defaults to 6.28 rad. Parameter is ignored if set to 0.0.
            max_acceleration (float): The maximum magnitude of acceleration for the robot in m/s^2. Parameter is ignored if set to 0.0.
            max_steering_angle_velocity (float): The maximum magnitude of desired rate of change for steering angle in rad/s. Parameter is ignored if set to 0.0.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, wheel_base: float, track_width: float, front_wheel_radius: float = 0.0, back_wheel_radius: float = 0.0, max_wheel_velocity: float = 0.0, invert_steering: bool = False, max_wheel_rotation_angle: float = 6.28, max_acceleration: float = 0.0, max_steering_angle_velocity: float = 0.0) -> None:
        ...
    def forward(self, command: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Calculate right and left wheel angles and angular velocity of each wheel given steering angle and desired forward velocity.
        
                Args:
                    command (np.ndarray): [desired steering angle (rad), steering_angle_velocity (rad/s), desired velocity of robot (m/s), acceleration (m/s^2), delta time (s)]
        
                Returns:
                    ArticulationAction: joint_velocities = [front left wheel, front right wheel, back left wheel, back right wheel]; joint_positions = [left wheel angle, right wheel angle]
                
        """
