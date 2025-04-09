from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
from collections import OrderedDict
from isaacsim.core.api.objects.cuboid import DynamicCuboid
from isaacsim.core.api.objects.cuboid import VisualCuboid
import isaacsim.core.api.scenes.scene
from isaacsim.core.api.scenes.scene import Scene
import isaacsim.core.api.tasks.base_task
from isaacsim.core.api.tasks.base_task import BaseTask
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.rotations import euler_angles_to_quat
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.string import find_unique_string_name
import numpy as np
import numpy
import typing
__all__ = ['ABC', 'BaseTask', 'DynamicCuboid', 'FollowTarget', 'OrderedDict', 'Scene', 'SingleXFormPrim', 'VisualCuboid', 'abstractmethod', 'euler_angles_to_quat', 'find_unique_string_name', 'get_stage_units', 'is_prim_path_valid', 'np']
class FollowTarget(abc.ABC, isaacsim.core.api.tasks.base_task.BaseTask):
    """
    [summary]
    
        Args:
            name (str): [description]
            target_prim_path (Optional[str], optional): [description]. Defaults to None.
            target_name (Optional[str], optional): [description]. Defaults to None.
            target_position (Optional[np.ndarray], optional): [description]. Defaults to None.
            target_orientation (Optional[np.ndarray], optional): [description]. Defaults to None.
            offset (Optional[np.ndarray], optional): [description]. Defaults to None.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'set_robot'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, target_prim_path: typing.Optional[str] = None, target_name: typing.Optional[str] = None, target_position: typing.Optional[numpy.ndarray] = None, target_orientation: typing.Optional[numpy.ndarray] = None, offset: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def add_obstacle(self, position: numpy.ndarray = None):
        """
        [summary]
        
                Args:
                    position (np.ndarray, optional): [description]. Defaults to np.array([0.1, 0.1, 1.0]).
                
        """
    def calculate_metrics(self) -> dict:
        """
        [summary]
        """
    def cleanup(self) -> None:
        """
        [summary]
        """
    def get_observations(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def get_obstacle_to_delete(self) -> None:
        """
        [summary]
        
                Returns:
                    [type]: [description]
                
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
        """
    def obstacles_exist(self) -> bool:
        """
        [summary]
        
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
    def remove_obstacle(self, name: typing.Optional[str] = None) -> None:
        """
        [summary]
        
                Args:
                    name (Optional[str], optional): [description]. Defaults to None.
                
        """
    def set_params(self, target_prim_path: typing.Optional[str] = None, target_name: typing.Optional[str] = None, target_position: typing.Optional[numpy.ndarray] = None, target_orientation: typing.Optional[numpy.ndarray] = None) -> None:
        """
        [summary]
        
                Args:
                    target_prim_path (Optional[str], optional): [description]. Defaults to None.
                    target_name (Optional[str], optional): [description]. Defaults to None.
                    target_position (Optional[np.ndarray], optional): [description]. Defaults to None.
                    target_orientation (Optional[np.ndarray], optional): [description]. Defaults to None.
                
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
    def target_reached(self) -> bool:
        """
        [summary]
        
                Returns:
                    bool: [description]
                
        """
