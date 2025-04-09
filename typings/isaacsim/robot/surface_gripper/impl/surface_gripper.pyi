from __future__ import annotations
import carb as carb
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper
from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper_Properties
import numpy as np
import omni as omni
__all__ = ['SurfaceGripper', 'Surface_Gripper', 'Surface_Gripper_Properties', 'add_reference_to_stage', 'carb', 'np', 'omni']
class SurfaceGripper:
    """
    [summary]
    
        Args:
            usd_path (Optional[str], optional): [description]. Defaults to None.
            translate (float, optional): [description]. Defaults to 0.
            direction (str, optional): [description]. Defaults to "x".
            grip_threshold (float, optional): [description]. Defaults to 1.
            force_limit (float, optional): [description]. Defaults to 1.0e6.
            torque_limit (float, optional): [description]. Defaults to 1.0e6.
            bend_angle (float, optional): [description]. Defaults to np.pi/24.
            kp (float, optional): [description]. Defaults to 1.0e5.
            kd (float, optional): [description]. Defaults to 1.0e4.
            disable_gravity (bool, optional): [description]. Defaults to True.
        
    """
    def __init__(self, usd_path: typing.Optional[str] = None, translate: float = 0, direction: str = 'x', grip_threshold: float = 0.01, force_limit: float = 1000000.0, torque_limit: float = 10000.0, bend_angle: float = 0.1308996938995747, kp: float = 100.0, kd: float = 100.0, disable_gravity: bool = True) -> None:
        ...
    def close(self) -> None:
        """
        [summary]
        """
    def initialize(self, root_prim_path: str) -> None:
        """
        [summary]
        
                Args:
                    root_prim_path (str): [description]
                
        """
    def is_closed(self) -> bool:
        """
        [summary]
        
                Returns:
                    bool: [description]
                
        """
    def open(self) -> None:
        """
        [summary]
        """
    def set_direction(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
                
        """
    def set_force_limit(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
                
        """
    def set_torque_limit(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
                
        """
    def set_translate(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
                
        """
    def update(self) -> None:
        """
        [summary]
        """
