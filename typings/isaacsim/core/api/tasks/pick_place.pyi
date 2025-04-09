from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
from isaacsim.core.api.objects.cuboid import DynamicCuboid
import isaacsim.core.api.scenes.scene
from isaacsim.core.api.scenes.scene import Scene
import isaacsim.core.api.tasks.base_task
from isaacsim.core.api.tasks.base_task import BaseTask
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.string import find_unique_string_name
import numpy as np
import typing
__all__ = ['ABC', 'BaseTask', 'DynamicCuboid', 'PickPlace', 'Scene', 'abstractmethod', 'find_unique_string_name', 'get_stage_units', 'is_prim_path_valid', 'np']
class PickPlace(abc.ABC, isaacsim.core.api.tasks.base_task.BaseTask):
    """
    [summary]
    
        Args:
            name (str): [description]
            cube_initial_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            cube_initial_orientation (Optional[np.ndarray], optional): [description]. Defaults to None.
            target_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            cube_size (Optional[np.ndarray], optional): [description]. Defaults to None.
            offset (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'set_robot'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, cube_initial_position: typing.Optional[numpy.ndarray] = None, cube_initial_orientation: typing.Optional[numpy.ndarray] = None, target_position: typing.Optional[numpy.ndarray] = None, cube_size: typing.Optional[numpy.ndarray] = None, offset: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def calculate_metrics(self) -> dict:
        """
        [summary]
        """
    def get_observations(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def get_params(self) -> dict:
        ...
    def is_done(self) -> bool:
        """
        [summary]
        """
    def post_reset(self) -> None:
        ...
    def pre_step(self, time_step_index: int, simulation_time: float) -> None:
        """
        [summary]
        
                Args:
                    time_step_index (int): [description]
                    simulation_time (float): [description]
                
        """
    def set_params(self, cube_position: typing.Optional[numpy.ndarray] = None, cube_orientation: typing.Optional[numpy.ndarray] = None, target_position: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def set_robot(self) -> None:
        ...
    def set_up_scene(self, scene: isaacsim.core.api.scenes.scene.Scene) -> None:
        """
        [summary]
        
                Args:
                    scene (Scene): [description]
                
        """
