from __future__ import annotations
import carb as carb
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils.prims import find_matching_prim_paths
from isaacsim.core.utils.prims import get_prim_at_path
import numpy as np
import omni as omni
from pxr import Usd
import re as re
import torch as torch
import warp as wp
__all__ = ['IsaacEvents', 'Prim', 'SimulationManager', 'Usd', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'np', 'omni', 're', 'torch', 'wp']
class Prim:
    def __del__(self):
        ...
    def __init__(self, prim_paths_expr: str, name: str = 'prim_view') -> None:
        ...
    def _on_physics_ready(self, event):
        ...
    def _on_post_reset(self, event) -> None:
        ...
    def _on_prim_deletion(self, prim_path):
        ...
    def _remove_callbacks(self) -> None:
        ...
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and set other properties using the PhysX tensor API
        
                .. note::
        
                    For this particular class, calling this method will do nothing
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.initialize()
                
        """
    def is_valid(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> bool:
        """
        Check that all prims have a valid USD Prim
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    bool: True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.is_valid()
                    True
                
        """
    def post_reset(self) -> None:
        """
        Reset the prims to its default state
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.post_reset()
                
        """
    @property
    def count(self) -> int:
        """
        
                Returns:
                    int: Number of prims encapsulated in this view.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.count
                    5
                
        """
    @property
    def initialized(self) -> bool:
        """
        Check if prim view is initialized
        
                Returns:
                    bool: True if the view object was initialized (after the first call of .initialize()). False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given an initialized articulation view
                    >>> prims.initialized
                    True
                
        """
    @property
    def name(self) -> str:
        """
        
                Returns:
                    str: name given to the prims view when instantiating it.
                
        """
    @property
    def prim_paths(self) -> typing.List[str]:
        """
        
                Returns:
                    List[str]: list of prim paths in the stage encapsulated in this view.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.prim_paths
                    ['/World/envs/env_0', '/World/envs/env_1', '/World/envs/env_2', '/World/envs/env_3', '/World/envs/env_4']
                
        """
    @property
    def prims(self) -> typing.List[pxr.Usd.Prim]:
        """
        
                Returns:
                    List[Usd.Prim]: List of USD Prim objects encapsulated in this view.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.prims
                    [Usd.Prim(</World/envs/env_0>), Usd.Prim(</World/envs/env_1>), Usd.Prim(</World/envs/env_2>),
                     Usd.Prim(</World/envs/env_3>), Usd.Prim(</World/envs/env_4>)]
                
        """
