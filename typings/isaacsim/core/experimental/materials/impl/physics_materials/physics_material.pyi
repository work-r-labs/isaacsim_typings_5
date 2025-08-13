from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import isaacsim.core.experimental.prims.impl.prim
from isaacsim.core.experimental.prims.impl.prim import Prim
from isaacsim.core.experimental.utils import stage as stage_utils
from pxr import Usd
from pxr import UsdShade
import typing
import warp as wp
__all__: list[str] = ['ABC', 'PhysicsMaterial', 'Prim', 'Usd', 'UsdShade', 'abstractmethod', 'stage_utils', 'wp']
class PhysicsMaterial(isaacsim.core.experimental.prims.impl.prim.Prim, abc.ABC):
    """
    Base class for physics materials.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            resolve_paths: Whether to resolve the given paths (true) or use them as is (false).
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'are_of_type'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _get_material(stage: Usd.Stage, path: str) -> UsdShade.Material | None:
        """
        Get the material for a given material path.
        """
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating material instances of this type.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating material instances (shape ``(N, 1)``).
                
        """
    @staticmethod
    def fetch_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[PhysicsMaterial | None]:
        """
        Fetch instances of physics material from prims (or prim paths) at the given paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Prim paths (or prims) to get physics material instances from.
        
                Returns:
                    List of physics material instances or ``None`` if the prim is not a supported physics material type.
        
                Example:
        
                .. code-block:: python
        
                    >>> import omni.kit.commands
                    >>> import isaacsim.core.experimental.utils.stage as stage_utils
                    >>> from isaacsim.core.experimental.materials import PhysicsMaterial
                    >>>
                    >>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
                    >>> omni.kit.commands.execute(
                    ...     "AddRigidBodyMaterialCommand", stage=stage_utils.get_current_stage(), path="/World/A"
                    ... )  # doctest: +NO_CHECK
                    >>>
                    >>> # fetch physics material instances
                    >>> PhysicsMaterial.fetch_instances(["/World", "/World/A"])
                    [None, <isaacsim.core.experimental.materials.impl.physics_materials.rigid_body.RigidBodyMaterial object at 0x...>]
                
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True) -> None:
        ...
    @property
    def materials(self) -> list[UsdShade.Material]:
        """
        USD materials encapsulated by the wrapper.
        
                Returns:
                    List of USD materials.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.materials
                    [UsdShade.Material(Usd.Prim(</World/prim_0>)),
                     UsdShade.Material(Usd.Prim(</World/prim_1>)),
                     UsdShade.Material(Usd.Prim(</World/prim_2>))]
                
        """
