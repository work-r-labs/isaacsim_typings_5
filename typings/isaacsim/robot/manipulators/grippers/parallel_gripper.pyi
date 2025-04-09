from __future__ import annotations
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot.manipulators.grippers.gripper
from isaacsim.robot.manipulators.grippers.gripper import Gripper
import numpy
import numpy as np
import omni as omni
__all__ = ['ArticulationAction', 'Gripper', 'ParallelGripper', 'np', 'omni']
class ParallelGripper(isaacsim.robot.manipulators.grippers.gripper.Gripper):
    """
    Provides high level functions to set/ get properties and actions of a parllel gripper
        (a gripper that has two fingers).
    
        Args:
            end_effector_prim_path (str): prim path of the Prim that corresponds to the gripper root/ end effector.
            joint_prim_names (List[str]): the left finger joint prim name and the right finger joint prim name respectively.
            joint_opened_positions (np.ndarray): joint positions of the left finger joint and the right finger joint respectively when opened.
            joint_closed_positions (np.ndarray): joint positions of the left finger joint and the right finger joint respectively when closed.
            action_deltas (np.ndarray, optional): deltas to apply for finger joint positions when openning or closing the gripper. Defaults to None.
        
    """
    def __init__(self, end_effector_prim_path: str, joint_prim_names: typing.List[str], joint_opened_positions: numpy.ndarray, joint_closed_positions: numpy.ndarray, action_deltas: numpy.ndarray = None) -> None:
        ...
    def apply_action(self, control_actions: isaacsim.core.utils.types.ArticulationAction) -> None:
        """
        Applies actions to all the joints of an articulation that corresponds to the ArticulationAction of the finger joints only.
        
                Args:
                    control_actions (ArticulationAction): ArticulationAction for the left finger joint and the right finger joint respectively.
                
        """
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
    def get_action_deltas(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: deltas that will be applied for finger joint positions when openning or closing the gripper.
                                [left, right]. Defaults to None.
                
        """
    def get_default_state(self) -> numpy.ndarray:
        """
        Gets the default state of the gripper
        
                Returns:
                    np.ndarray: joint positions of the left finger joint and the right finger joint respectively.
                
        """
    def get_joint_positions(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: joint positions of the left finger joint and the right finger joint respectively.
                
        """
    def initialize(self, articulation_apply_action_func: typing.Callable, get_joint_positions_func: typing.Callable, set_joint_positions_func: typing.Callable, dof_names: typing.List, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
                    This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any
                    of the functions of this class.
        
                Args:
                    articulation_apply_action_func (Callable): apply_action function from the Articulation class.
                    get_joint_positions_func (Callable): get_joint_positions function from the Articulation class.
                    set_joint_positions_func (Callable): set_joint_positions function from the Articulation class.
                    dof_names (List): dof names from the Articulation class.
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None
        
                Raises:
                    Exception: _description_
                
        """
    def open(self) -> None:
        """
        Applies actions to the articulation that opens the gripper (ex: to release an object held).
        """
    def post_reset(self):
        ...
    def set_action_deltas(self, value: numpy.ndarray) -> None:
        """
        
                Args:
                    value (np.ndarray): deltas to apply for finger joint positions when openning or closing the gripper.
                                       [left, right]. Defaults to None.
                
        """
    def set_default_state(self, joint_positions: numpy.ndarray) -> None:
        """
        Sets the default state of the gripper
        
                Args:
                    joint_positions (np.ndarray): joint positions of the left finger joint and the right finger joint respectively.
                
        """
    def set_joint_positions(self, positions: numpy.ndarray) -> None:
        """
        
                Args:
                    positions (np.ndarray): joint positions of the left finger joint and the right finger joint respectively.
                
        """
    @property
    def joint_closed_positions(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: joint positions of the left finger joint and the right finger joint respectively when closed.
                
        """
    @property
    def joint_dof_indicies(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: joint dof indices in the articulation of the left finger joint and the right finger joint respectively.
                
        """
    @property
    def joint_opened_positions(self) -> numpy.ndarray:
        """
        
                Returns:
                    np.ndarray: joint positions of the left finger joint and the right finger joint respectively when opened.
                
        """
    @property
    def joint_prim_names(self) -> typing.List[str]:
        """
        
                Returns:
                    List[str]: the left finger joint prim name and the right finger joint prim name respectively.
                
        """
