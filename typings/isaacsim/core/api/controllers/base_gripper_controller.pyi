from __future__ import annotations
from abc import abstractmethod
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import numpy as np
import numpy
import typing
__all__ = ['ArticulationAction', 'BaseController', 'BaseGripperController', 'abstractmethod', 'np']
class BaseGripperController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    [summary]
    
        Args:
            name (str): [description]
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'close', 'open'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str) -> None:
        ...
    def close(self, current_joint_positions: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        [summary]
        
                Args:
                    current_joint_positions (np.ndarray): [description]
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def forward(self, action: str, current_joint_positions: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Action has be "open" or "close"
        
                Args:
                    action (str): "open" or "close"
                    current_joint_positions (np.ndarray): [description]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def open(self, current_joint_positions: numpy.ndarray) -> isaacsim.core.utils.types.ArticulationAction:
        """
        [summary]
        
                Args:
                    current_joint_positions (np.ndarray): [description]
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def reset(self) -> None:
        """
        [summary]
        """
