from __future__ import annotations
import carb as carb
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot.manipulators.grippers.gripper
from isaacsim.robot.manipulators.grippers.gripper import Gripper
from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper
from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper_Properties
import numpy as np
import omni as omni
__all__ = ['ArticulationAction', 'Gripper', 'SurfaceGripper', 'Surface_Gripper', 'Surface_Gripper_Properties', 'carb', 'np', 'omni']
class SurfaceGripper(isaacsim.robot.manipulators.grippers.gripper.Gripper):
    """
    Provides high level functions to set/ get properties and actions of a surface gripper
        (a suction cup for example).
    
        Args:
            end_effector_prim_path (str): prim path of the Prim that corresponds to the gripper root/ end effector.
            translate (float, optional): _description_. Defaults to 0.
            direction (str, optional): _description_. Defaults to "x".
            grip_threshold (float, optional): _description_. Defaults to 0.01.
            force_limit (float, optional): _description_. Defaults to 1.0e6.
            torque_limit (float, optional): _description_. Defaults to 1.0e4.
            bend_angle (float, optional): _description_. Defaults to np.pi/24.
            kp (float, optional): _description_. Defaults to 1.0e2.
            kd (float, optional): _description_. Defaults to 1.0e2.
            disable_gravity (bool, optional): _description_. Defaults to True.
        
    """
    def __init__(self, end_effector_prim_path: str, translate: float = 0, direction: str = 'x', grip_threshold: float = 0.01, force_limit: float = 1000000.0, torque_limit: float = 10000.0, bend_angle: float = 0.1308996938995747, kp: float = 100.0, kd: float = 100.0, disable_gravity: bool = True) -> None:
        ...
    def close(self) -> None:
        """
        Applies actions to the articulation that closes the gripper (ex: to hold an object).
        """
    def forward(self, action: str) -> isaacsim.core.utils.types.ArticulationAction:
        """
        calculates the ArticulationAction for all of the articulation joints that corresponds to "open"
                   or "close" actions.
        
                Args:
                    action (str): "open" or "close" as an abstract action.
        
                Raises:
                    Exception: _description_
        
                Returns:
                    ArticulationAction: articulation action to be passed to the articulation itself
                                        (includes all joints of the articulation).
                
        """
    def get_default_state(self) -> dict:
        """
        Gets the default state of the gripper
        
                Returns:
                    dict: key is "opened" and value would be true if the surface gripper should start in an opened state. False otherwise.
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None, articulation_num_dofs: int = None) -> None:
        """
        Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
                    This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any
                    of the functions of this class.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None
                    articulation_num_dofs (int, optional): num of dofs of the Articulation. Defaults to None.
                
        """
    def is_closed(self) -> bool:
        ...
    def open(self) -> None:
        """
        Applies actions to the articulation that opens the gripper (ex: to release an object held).
        """
    def post_reset(self):
        ...
    def set_default_state(self, opened: bool):
        """
        Sets the default state of the gripper
        
                Args:
                    opened (bool): True if the surface gripper should start in an opened state. False otherwise.
                
        """
    def set_direction(self, value: float) -> None:
        ...
    def set_force_limit(self, value: float) -> None:
        ...
    def set_torque_limit(self, value: float) -> None:
        ...
    def set_translate(self, value: float) -> None:
        ...
    def update(self) -> None:
        ...
