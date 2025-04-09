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
import numpy
import typing
__all__ = ['ABC', 'BaseTask', 'DynamicCuboid', 'Scene', 'Stacking', 'abstractmethod', 'find_unique_string_name', 'get_stage_units', 'is_prim_path_valid', 'np']
class Stacking(abc.ABC, isaacsim.core.api.tasks.base_task.BaseTask):
    """
    [summary]
    
        Args:
            name (str): [description]
            cube_initial_positions (np.ndarray): [description]
            cube_initial_orientations (Optional[np.ndarray], optional): [description]. Defaults to None.
            stack_target_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            cube_size (Optional[np.ndarray], optional): [description]. Defaults to None.
            offset (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'set_robot'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, cube_initial_positions: numpy.ndarray, cube_initial_orientations: typing.Optional[numpy.ndarray] = None, stack_target_position: typing.Optional[numpy.ndarray] = None, cube_size: typing.Optional[numpy.ndarray] = None, offset: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def calculate_metrics(self) -> dict:
        """
        [summary]
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    dict: [description]
                
        """
    def get_cube_names(self) -> typing.List[str]:
        """
        [summary]
        
                Returns:
                    List[str]: [description]
                
        """
    def get_observations(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def get_params(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def is_done(self) -> bool:
        """
        [summary]
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    bool: [description]
                
        """
    def post_reset(self) -> None:
        """
        [summary]
        """
    def pre_step(self, time_step_index: int, simulation_time: float) -> None:
        """
        [summary]
        
                Args:
                    time_step_index (int): [description]
                    simulation_time (float): [description]
                
        """
    def set_params(self, cube_name: typing.Optional[str] = None, cube_position: typing.Optional[str] = None, cube_orientation: typing.Optional[str] = None, stack_target_position: typing.Optional[str] = None) -> None:
        """
        [summary]
        
                Args:
                    cube_name (Optional[str], optional): [description]. Defaults to None.
                    cube_position (Optional[str], optional): [description]. Defaults to None.
                    cube_orientation (Optional[str], optional): [description]. Defaults to None.
                    stack_target_position (Optional[str], optional): [description]. Defaults to None.
                
        """
    def set_robot(self) -> None:
        """
        [summary]
        
                Raises:
                    NotImplementedError: [description]
                
        """
    def set_up_scene(self, scene: isaacsim.core.api.scenes.scene.Scene) -> None:
        """
        [summary]
        
                Args:
                    scene (Scene): [description]
                
        """
