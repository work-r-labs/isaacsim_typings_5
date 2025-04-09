from __future__ import annotations
import carb as carb
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
from isaacsim.core.utils.math import cross
from isaacsim.core.utils.rotations import euler_angles_to_quat
from isaacsim.core.utils.rotations import quat_to_rot_matrix
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import numpy
from numpy import linalg
import omni as omni
import osqp as osqp
from pxr import Gf
from scipy import sparse
import typing
__all__ = ['ArticulationAction', 'BaseController', 'Gf', 'HolonomicController', 'carb', 'cross', 'euler_angles_to_quat', 'linalg', 'np', 'omni', 'osqp', 'quat_to_rot_matrix', 'sparse']
class HolonomicController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    
    
        This controller computes the joint drive commands required to produce the commanded forward, lateral, and yaw speeds of the robot. The problem is framed as a quadratic program to minimize the residual "net force" acting on the center of mass.
    
        .. hint::
    
            The wheel joints of the robot prim must have additional attributes to definine the roller angles and radii of the mecanum wheels.
    
            .. code-block:: python
    
                stage = omni.usd.get_context().get_stage()
                joint_prim = stage.GetPrimAtPath("/path/to/wheel_joint")
                joint_prim.CreateAttribute("isaacmecanumwheel:radius",Sdf.ValueTypeNames.Float).Set(0.12)
                joint_prim.CreateAttribute("isaacmecanumwheel:angle",Sdf.ValueTypeNames.Float).Set(10.3)
    
            The :class:`HolonomicRobotUsdSetup` class automates this process.
    
    
        Args:
            name (str): [description]
            wheel_radius (np.ndarray): radius of the wheels, array of 1 can be used if all wheels are the same size
            wheel_positions (np.ndarray): position of the wheels relative to center of mass of the vehicle. number of wheels x [x,y,z]
            wheel_orientations (np.ndarray): orientation of the wheels in quaternions relative to center of mass frame of the vehicle. number of wheels x [quaternions]
            mecanum_angles (np.ndarray): mecanum wheel angles. Array of 1 can be used if all wheels have the same angle.
            wheel_axis (np.ndarray): the spinning axis of the wheels. Defaults to [1,0,0]
            up_axis (np.ndarray): Defaults to z- axis
            max_linear_speed (float): maximum "forward" speed (default: 1.0e20)
            max_angular_speed (float): maximum "turning" speed (default: 1.0e20)
            max_wheel_speed (float): maximum "twisting" speed (default: 1.0e20)
            linear_gain (float): Multiplicative factor. How much the solver should "care" about the linear components of the solution. (default: 1.0)
            linear_gain (float): Multiplicative factor. How much the solver should "care" about the angular components of the solution. (default: 1.0)
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, wheel_radius: typing.Optional[numpy.ndarray] = None, wheel_positions: typing.Optional[numpy.ndarray] = None, wheel_orientations: typing.Optional[numpy.ndarray] = None, mecanum_angles: typing.Optional[numpy.ndarray] = None, wheel_axis: float = ..., up_axis: float = ..., max_linear_speed: float = 1e+20, max_angular_speed: float = 1e+20, max_wheel_speed: float = 1e+20, linear_gain: float = 1.0, angular_gain: float = 1.0) -> None:
        ...
    def build_base(self):
        ...
    def forward(self, command: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Calculate wheel speeds given the desired signed vehicle speeds.
        
                Args:
                    command (np.ndarray): [forward speed, lateral speed, yaw speed].
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def reset(self) -> None:
        """
        [summary]
        """
