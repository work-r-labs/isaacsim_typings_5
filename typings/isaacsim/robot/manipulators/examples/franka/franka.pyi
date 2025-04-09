from __future__ import annotations
import carb as carb
import isaacsim.core.api.robots.robot
from isaacsim.core.api.robots.robot import Robot
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.stage import get_stage_units
import isaacsim.robot.manipulators.grippers.parallel_gripper
from isaacsim.robot.manipulators.grippers.parallel_gripper import ParallelGripper
from isaacsim.storage.native.nucleus import get_assets_root_path
import numpy as np
__all__ = ['Franka', 'ParallelGripper', 'Robot', 'SingleRigidPrim', 'add_reference_to_stage', 'carb', 'get_assets_root_path', 'get_prim_at_path', 'get_stage_units', 'np']
class Franka(isaacsim.core.api.robots.robot.Robot):
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            name (str, optional): [description]. Defaults to "franka_robot".
            usd_path (Optional[str], optional): [description]. Defaults to None.
            position (Optional[np.ndarray], optional): [description]. Defaults to None.
            orientation (Optional[np.ndarray], optional): [description]. Defaults to None.
            end_effector_prim_name (Optional[str], optional): [description]. Defaults to None.
            gripper_dof_names (Optional[List[str]], optional): [description]. Defaults to None.
            gripper_open_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            gripper_closed_position (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    def __init__(self, prim_path: str, name: str = 'franka_robot', usd_path: typing.Optional[str] = None, position: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, end_effector_prim_name: typing.Optional[str] = None, gripper_dof_names: typing.Optional[typing.List[str]] = None, gripper_open_position: typing.Optional[numpy.ndarray] = None, gripper_closed_position: typing.Optional[numpy.ndarray] = None, deltas: typing.Optional[numpy.ndarray] = None) -> None:
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
    def end_effector(self) -> isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim:
        """
        [summary]
        
                Returns:
                    SingleRigidPrim: [description]
                
        """
    @property
    def gripper(self) -> isaacsim.robot.manipulators.grippers.parallel_gripper.ParallelGripper:
        """
        [summary]
        
                Returns:
                    ParallelGripper: [description]
                
        """
