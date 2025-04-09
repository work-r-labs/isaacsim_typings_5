from __future__ import annotations
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import numpy
import typing
__all__ = ['ArticulationAction', 'BaseController', 'DifferentialController', 'np']
class DifferentialController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    
    
    
        This controller uses a unicycle model of a differential drive. The Controller consumes a command in the form of a linear and angular velocity, and then computes the circular arc that satisfies this command given the distance between the wheels.  This can then be used to compute the necessary angular velocities of the joints that will propell the midpoint between the wheels along the curve. The conversion is
    
            .. math::
    
                \\omega_R = \\frac{1}{2r}(2V + \\omega b) 
    
                \\omega_L = \\frac{1}{2r}(2V - \\omega b)
    
        where :math:`\\omega` is the desired angular velocity, :math:`V` is the desired linear velocity, :math:`r` is the radius of the wheels, and :math:`b` is the distance between them.
    
    
        Args:
            name (str): [description]
            wheel_radius (float): Radius of left and right wheels in cms
            wheel_base (float): Distance between left and right wheels in cms
            max_linear_speed (float): OPTIONAL: limits the maximum linear speed that will be produced by the controller. Defaults to 1E20.
            max_angular_speed (float): OPTIONAL: limits the maximum angular speed that will be produced by the controller. Defaults to 1E20.
            max_wheel_speed (float): OPTIONAL: limits the maximum wheel speed that will be produced by the controller. Defaults to 1E20.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, wheel_radius: float, wheel_base: float, max_linear_speed: float = 1e+20, max_angular_speed: float = 1e+20, max_wheel_speed: float = 1e+20) -> None:
        ...
    def forward(self, command: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        convert from desired [signed linear speed, signed angular speed] to [Left Drive, Right Drive] joint targets.
        
                Args:
                    command (np.ndarray): desired vehicle [forward, rotation] speed
        
                Returns:
                    ArticulationAction: the articulation action to be applied to the robot.
                
        """
