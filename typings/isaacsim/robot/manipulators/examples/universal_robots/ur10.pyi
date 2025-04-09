from __future__ import annotations
import carb as carb
import isaacsim.core.api.robots.robot
from isaacsim.core.api.robots.robot import Robot
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import add_reference_to_stage
import isaacsim.robot.manipulators.grippers.surface_gripper
from isaacsim.robot.manipulators.grippers.surface_gripper import SurfaceGripper
from isaacsim.storage.native.nucleus import get_assets_root_path
import numpy as np
__all__ = ['Robot', 'SingleRigidPrim', 'SurfaceGripper', 'UR10', 'add_reference_to_stage', 'carb', 'get_assets_root_path', 'get_prim_at_path', 'np']
class UR10(isaacsim.core.api.robots.robot.Robot):
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "ur10_robot".
            usd_path (Optional[str], optional): [description]. Defaults to None.
            position (Optional[np.ndarray], optional): [description]. Defaults to None.
            orientation (Optional[np.ndarray], optional): [description]. Defaults to None.
            end_effector_prim_name (Optional[str], optional): [description]. Defaults to None.
            attach_gripper (bool, optional): [description]. Defaults to False.
            gripper_usd (Optional[str], optional): [description]. Defaults to "default".
    
        Raises:
            NotImplementedError: [description]
        
    """
    def __init__(self, prim_path: str, name: str = 'ur10_robot', usd_path: typing.Optional[str] = None, position: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, end_effector_prim_name: typing.Optional[str] = None, attach_gripper: bool = False, gripper_usd: typing.Optional[str] = 'default') -> None:
        ...
    def initialize(self, physics_sim_view = None) -> None:
        """
        [summary]
        """
    def post_reset(self) -> None:
        """
        [summary]
        """
    @property
    def attach_gripper(self) -> bool:
        """
        [summary]
        
                Returns:
                    bool: [description]
                
        """
    @property
    def end_effector(self) -> isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim:
        """
        [summary]
        
                Returns:
                    SingleRigidPrim: [description]
                
        """
    @property
    def gripper(self) -> isaacsim.robot.manipulators.grippers.surface_gripper.SurfaceGripper:
        """
        [summary]
        
                Returns:
                    SurfaceGripper: [description]
                
        """
