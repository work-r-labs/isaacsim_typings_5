from __future__ import annotations
import isaacsim.core.api.controllers.articulation_controller
from isaacsim.core.api.controllers.articulation_controller import ArticulationController
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import numpy
__all__ = ['ArticulationAction', 'ArticulationController', 'ArticulationGripper', 'SingleArticulation', 'np']
class ArticulationGripper:
    """
    [summary]
    
        Args:
            gripper_dof_names (list): [description]
            gripper_open_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            gripper_closed_position (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    def __init__(self, gripper_dof_names: list, gripper_open_position: typing.Optional[numpy.ndarray] = None, gripper_closed_position: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def apply_action(self, action: isaacsim.core.utils.types.ArticulationAction) -> None:
        """
        [summary]
        
                Args:
                    action (ArticulationAction): [description]
                
        """
    def get_positions(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def get_velocities(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    def initialize(self, root_prim_path: str, articulation_controller: isaacsim.core.api.controllers.articulation_controller.ArticulationController) -> None:
        """
        [summary]
        
                Args:
                    root_prim_path (str): [description]
                    articulation_controller (ArticulationController): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_positions(self, positions: numpy.ndarray) -> None:
        """
        [summary]
        
                Args:
                    positions (np.ndarray): [description]
                
        """
    def set_velocities(self, velocities: numpy.ndarray) -> None:
        """
        [summary]
        
                Args:
                    velocities (np.ndarray): [description]
                
        """
    @property
    def closed_position(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    @property
    def dof_indices(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
    @property
    def open_position(self) -> numpy.ndarray:
        """
        [summary]
        
                Returns:
                    np.ndarray: [description]
                
        """
