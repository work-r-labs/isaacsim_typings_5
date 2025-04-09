from __future__ import annotations
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot.manipulators.controllers.pick_place_controller
from isaacsim.robot.manipulators.controllers.pick_place_controller import PickPlaceController
import numpy as np
import typing as typing
__all__ = ['ArticulationAction', 'BaseController', 'PickPlaceController', 'StackingController', 'np', 'typing']
class StackingController(isaacsim.core.api.controllers.base_controller.BaseController):
    """
    [summary]
    
        Args:
            name (str): [description]
            pick_place_controller (PickPlaceController): [description]
            picking_order_cube_names (typing.List[str]): [description]
            robot_observation_name (str): [description]
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, pick_place_controller: isaacsim.robot.manipulators.controllers.pick_place_controller.PickPlaceController, picking_order_cube_names: typing.List[str], robot_observation_name: str) -> None:
        ...
    def forward(self, observations: dict, end_effector_orientation: typing.Optional[numpy.ndarray] = None, end_effector_offset: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        ...
    def is_done(self) -> bool:
        """
        [summary]
        
                Returns:
                    bool: [description]
                
        """
    def reset(self, picking_order_cube_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        [summary]
        
                Args:
                    picking_order_cube_names (typing.Optional[typing.List[str]], optional): [description]. Defaults to None.
                
        """
