from __future__ import annotations
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
from isaacsim.core.utils.types import ArticulationActions
import numpy as np
import numpy
__all__ = ['ArticulationAction', 'ArticulationActions', 'ArticulationController', 'np']
class ArticulationController:
    """
    PD Controller of all degrees of freedom of an articulation, can apply position targets, velocity targets and efforts.
    
        Checkout the required tutorials at
         https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html
        
    """
    def __init__(self) -> None:
        ...
    def apply_action(self, control_actions: isaacsim.core.utils.types.ArticulationAction) -> None:
        """
        [summary]
        
                Args:
                    control_actions (ArticulationAction): actions to be applied for next physics step.
                    indices (Optional[Union[list, np.ndarray]], optional): degree of freedom indices to apply actions to.
                                                                           Defaults to all degrees of freedom.
        
                Raises:
                    Exception: [description]
                
        """
    def get_applied_action(self) -> isaacsim.core.utils.types.ArticulationAction:
        """
        
        
                Raises:
                    Exception: [description]
        
                Returns:
                    ArticulationAction: Gets last applied action.
                
        """
    def get_effort_modes(self) -> typing.List[str]:
        """
        [summary]
        
                Raises:
                    Exception: [description]
                    NotImplementedError: [description]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_gains(self) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: [description]
                
        """
    def get_joint_limits(self) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: [description]
                
        """
    def get_max_efforts(self) -> numpy.ndarray:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def initialize(self, articulation_view) -> None:
        """
        [summary]
        
                Args:
                    articulation_view ([type]): [description]
                
        """
    def set_effort_modes(self, mode: str, joint_indices: typing.Union[numpy.ndarray, list, NoneType] = None) -> None:
        """
        [summary]
        
                Args:
                    mode (str): [description]
                    indices (Optional[Union[np.ndarray, list]], optional): [description]. Defaults to None.
        
                Raises:
                    Exception: [description]
                    Exception: [description]
                
        """
    def set_gains(self, kps: typing.Optional[numpy.ndarray] = None, kds: typing.Optional[numpy.ndarray] = None, save_to_usd: bool = False) -> None:
        """
        [summary]
        
                Args:
                    kps (Optional[np.ndarray], optional): [description]. Defaults to None.
                    kds (Optional[np.ndarray], optional): [description]. Defaults to None.
        
                Raises:
                    Exception: [description]
                
        """
    def set_max_efforts(self, values: numpy.ndarray, joint_indices: typing.Union[numpy.ndarray, list, NoneType] = None) -> None:
        """
        [summary]
        
                Args:
                    value (float, optional): [description]. Defaults to None.
                    indices (Optional[Union[np.ndarray, list]], optional): [description]. Defaults to None.
        
                Raises:
                    Exception: [description]
                
        """
    def switch_control_mode(self, mode: str) -> None:
        """
        [summary]
        
                Args:
                    mode (str): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def switch_dof_control_mode(self, dof_index: int, mode: str) -> None:
        """
        [summary]
        
                Args:
                    dof_index (int): [description]
                    mode (str): [description]
        
                Raises:
                    Exception: [description]
                
        """
