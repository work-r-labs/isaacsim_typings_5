from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import typing
__all__ = ['ABC', 'ArticulationAction', 'BaseController', 'abstractmethod']
class BaseController(abc.ABC):
    """
    [summary]
    
        Args:
            name (str): [description]
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'forward'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str) -> None:
        ...
    def forward(self, *args, **kwargs) -> isaacsim.core.utils.types.ArticulationAction:
        """
        A controller should take inputs and returns an ArticulationAction to be then passed to the
                   ArticulationController.
        
                Args:
                    observations (dict): [description]
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    ArticulationAction: [description]
                
        """
    def reset(self) -> None:
        """
        Resets state of the controller.
        """
