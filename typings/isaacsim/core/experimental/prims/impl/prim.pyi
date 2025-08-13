from __future__ import annotations
import abc
from abc import ABC
from isaacsim.core.experimental.utils import stage as stage_utils
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import prims as prims_utils
from pxr import Sdf
from pxr import Usd
import re as re
import typing
import warp as wp
__all__: list[str] = ['ABC', 'IsaacEvents', 'Prim', 'Sdf', 'SimulationManager', 'Usd', 'prims_utils', 're', 'stage_utils', 'wp']
class Prim(abc.ABC):
    """
    Base wrapper class to manage USD prims.
    
        Creates a wrapper over one or more USD prims in the stage.
        The prims are specified using paths that can include regular expressions for matching multiple prims.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            resolve_paths: Whether to resolve the given paths (true) or use them as is (false).
    
        Raises:
            ValueError: If no prims are found matching the specified path(s).
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.prims import Prim
            >>>
            >>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # - create wrapper over single prim
            >>> prim = Prim("/World/prim_0")  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex
            >>> prims = Prim("/World/prim_.*")  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def ensure_api(prims: list[Usd.Prim], api: type, *args, **kwargs) -> list[type['UsdAPISchemaBase']]:
        """
        Ensure that all prims have the specified API schema applied.
        
                Backends: :guilabel:`usd`.
        
                If a prim doesn't have the API schema, it will be applied.
                If it already has it, the existing API schema will be returned.
        
                Args:
                    prims: List of USD Prims to ensure API schema on.
                    api: The API schema type to ensure.
                    *args: Additional positional arguments passed to API schema when applying it.
                    **kwargs: Additional keyword arguments passed to API schema when applying it.
        
                Returns:
                    List of API schema objects, one for each input prim.
        
                Example:
        
                .. code-block:: python
        
                    >>> import isaacsim.core.experimental.utils.prim as prim_utils
                    >>> from pxr import UsdPhysics
                    >>> from isaacsim.core.experimental.prims import Prim
                    >>>
                    >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
                    >>> # ensure all prims have physics API schema
                    >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
                    >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
                
        """
    @staticmethod
    def resolve_paths(paths: str | list[str], raise_on_mixed_paths: bool = True) -> tuple[list[str], list[str]]:
        """
        Resolve paths to prims in the stage to get existing and non-existing paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
                    raise_on_mixed_paths: Whether to raise an error if resulting paths are mixed or invalid.
        
                Returns:
                    Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.
        
                Raises:
                    ValueError: If resulting paths are mixed or invalid and ``raise_on_mixed_paths`` is True.
                
        """
    def __del__(self) -> None:
        """
        Clean up instance by deregistering callbacks and resetting internal state.
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True) -> None:
        ...
    def __len__(self) -> int:
        """
        Get the number of prims encapsulated by the wrapper.
        
                Returns:
                    Number of prims in the wrapper.
        
                Example:
        
                .. code-block:: python
        
                    >>> len(prims)
                    3
                
        """
    def _deregister_callbacks(self) -> None:
        """
        Deregister all internal callbacks.
        """
    def _on_physics_ready(self, event) -> None:
        """
        Handle physics ready event.
        """
    def _on_prim_deletion(self, prim_path: str) -> None:
        """
        Handle prim deletion event.
        
                Args:
                    prim_path: Path of the deleted prim.
                
        """
    @property
    def paths(self) -> list[str]:
        """
        Prim paths in the stage encapsulated by the wrapper.
        
                Returns:
                    List of prim paths as strings.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.paths
                    ['/World/prim_0', '/World/prim_1', '/World/prim_2']
                
        """
    @property
    def prims(self) -> list[Usd.Prim]:
        """
        USD Prim objects encapsulated by the wrapper.
        
                Returns:
                    List of USD Prim objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.prims
                    [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
                
        """
    @property
    def valid(self) -> bool:
        """
        Whether all prims in the wrapper are valid.
        
                Returns:
                    True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.valid
                    True
                
        """
_MSG_PHYSICS_TENSOR_ENTITY_NOT_INITIALIZED: str = "Instance's physics tensor entity is not initialized. Play the simulation/timeline to initialize it"
_MSG_PHYSICS_TENSOR_ENTITY_NOT_VALID: str = "Instance's physics tensor entity is not valid. Play the simulation/timeline to re-initialize it"
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
