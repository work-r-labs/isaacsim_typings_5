from __future__ import annotations
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
from isaacsim.core.utils.rotations import euler_angles_to_quat
from isaacsim.core.utils.stage import get_stage_units
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot.manipulators.grippers.gripper
from isaacsim.robot.manipulators.grippers.gripper import Gripper
import numpy as np
import numpy
import typing as typing
__all__ = ['ArticulationAction', 'BaseController', 'Gripper', 'PickPlaceController', 'euler_angles_to_quat', 'get_stage_units', 'np', 'typing']
class PickPlaceController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    
        A simple pick and place state machine for tutorials
    
        Each phase runs for 1 second, which is the internal time of the state machine
    
        Dt of each phase/ event step is defined
    
        - Phase 0: Move end_effector above the cube center at the 'end_effector_initial_height'.
        - Phase 1: Lower end_effector down to encircle the target cube
        - Phase 2: Wait for Robot's inertia to settle.
        - Phase 3: close grip.
        - Phase 4: Move end_effector up again, keeping the grip tight (lifting the block).
        - Phase 5: Smoothly move the end_effector toward the goal xy, keeping the height constant.
        - Phase 6: Move end_effector vertically toward goal height at the 'end_effector_initial_height'.
        - Phase 7: loosen the grip.
        - Phase 8: Move end_effector vertically up again at the 'end_effector_initial_height'
        - Phase 9: Move end_effector towards the old xy position.
    
        Args:
            name (str): Name id of the controller
            cspace_controller (BaseController): a cartesian space controller that returns an ArticulationAction type
            gripper (Gripper): a gripper controller for open/ close actions.
            end_effector_initial_height (typing.Optional[float], optional): end effector initial picking height to start from (more info in phases above). If not defined, set to 0.3 meters. Defaults to None.
            events_dt (typing.Optional[typing.List[float]], optional): Dt of each phase/ event step. 10 phases dt has to be defined. Defaults to None.
    
        Raises:
            Exception: events dt need to be list or numpy array
            Exception: events dt need have length of 10
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, cspace_controller: isaacsim.core.api.controllers.base_controller.BaseController, gripper: isaacsim.robot.manipulators.grippers.gripper.Gripper, end_effector_initial_height: typing.Optional[float] = None, events_dt: typing.Optional[typing.List[float]] = None) -> None:
        ...
    def _combine_convex(self, a, b, alpha):
        ...
    def _get_alpha(self):
        ...
    def _get_interpolated_xy(self, target_x, target_y, current_x, current_y):
        ...
    def _get_target_hs(self, target_height):
        ...
    def _mix_sin(self, t):
        ...
    def forward(self, picking_position: numpy.ndarray, placing_position: numpy.ndarray, current_joint_positions: numpy.ndarray, end_effector_offset: typing.Optional[numpy.ndarray] = None, end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Runs the controller one step.
        
                Args:
                    picking_position (np.ndarray): The object's position to be picked in local frame.
                    placing_position (np.ndarray):  The object's position to be placed in local frame.
                    current_joint_positions (np.ndarray): Current joint positions of the robot.
                    end_effector_offset (typing.Optional[np.ndarray], optional): offset of the end effector target. Defaults to None.
                    end_effector_orientation (typing.Optional[np.ndarray], optional): end effector orientation while picking and placing. Defaults to None.
        
                Returns:
                    ArticulationAction: action to be executed by the ArticulationController
                
        """
    def get_current_event(self) -> int:
        """
        
        
                Returns:
                    int: Current event/ phase of the state machine
                
        """
    def is_done(self) -> bool:
        """
        
                Returns:
                    bool: True if the state machine reached the last phase. Otherwise False.
                
        """
    def is_paused(self) -> bool:
        """
        
        
                Returns:
                    bool: True if the state machine is paused. Otherwise False.
                
        """
    def pause(self) -> None:
        """
        Pauses the state machine's time and phase.
        """
    def reset(self, end_effector_initial_height: typing.Optional[float] = None, events_dt: typing.Optional[typing.List[float]] = None) -> None:
        """
        Resets the state machine to start from the first phase/ event
        
                Args:
                    end_effector_initial_height (typing.Optional[float], optional): end effector initial picking height to start from. If not defined, set to 0.3 meters. Defaults to None.
                    events_dt (typing.Optional[typing.List[float]], optional):  Dt of each phase/ event step. 10 phases dt has to be defined. Defaults to None.
        
                Raises:
                    Exception: events dt need to be list or numpy array
                    Exception: events dt need have length of 10
                
        """
    def resume(self) -> None:
        """
        Resumes the state machine's time and phase.
        """
