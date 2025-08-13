from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from pxr import Usd
from pxr import UsdGeom
import typing
import warp as wp
__all__: list[str] = ['ABC', 'Shape', 'Usd', 'UsdGeom', 'XformPrim', 'abstractmethod', 'np', 'stage_utils', 'wp']
class Shape(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim, abc.ABC):
    """
    Base class for creating/wrapping USD Geom shape prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Cube prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Cube prims.
            * If the prim paths do not exist, USD Cube prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            resolve_paths: Whether to resolve the given paths (true) or use them as is (false).
            positions: Positions in the world frame (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            translations: Translations in the local frame (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            orientations: Orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            scales: Scales to be applied to the prims (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            reset_xform_op_properties: Whether to reset the transformation operation attributes of the prims to a standard set.
                See :py:meth:`reset_xform_op_properties` for more details.
    
        Raises:
            ValueError: If resulting paths are mixed (existing and non-existing prims) or invalid.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'update_extents', 'are_of_type'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating Shape instances of this type.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating Shape instances.
                
        """
    @staticmethod
    def fetch_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Shape | None]:
        """
        Fetch instances of Shape from prims (or prim paths) at the given paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Prim paths (or prims) to get Shape instances from.
        
                Returns:
                    List of Shape instances or ``None`` if the prim is not a supported Shape type.
        
                Example:
        
                .. code-block:: python
        
                    >>> import isaacsim.core.experimental.utils.stage as stage_utils
                    >>> from isaacsim.core.experimental.objects import Shape
                    >>>
                    >>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
                    >>> stage_utils.define_prim(f"/World/A", "Cube")  # doctest: +NO_CHECK
                    >>> stage_utils.define_prim(f"/World/B", "Sphere")  # doctest: +NO_CHECK
                    >>>
                    >>> # fetch shape instances
                    >>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
                    [None,
                     <isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
                     <isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
                
        """
    @staticmethod
    def update_extents(geoms: list[UsdGeom.Gprim]) -> None:
        """
        Update the gprims' extents.
        
                Args:
                    geoms: Geoms to process.
                
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    @property
    def geoms(self) -> list[UsdGeom.Gprim]:
        """
        USD geometric primitives encapsulated by the wrapper.
        
                Returns:
                    List of USD geometric primitives.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.geoms  # doctest: +NO_CHECK
                    [UsdGeom.Gprim(Usd.Prim(</World/prim_0>)),
                     UsdGeom.Gprim(Usd.Prim(</World/prim_1>)),
                     UsdGeom.Gprim(Usd.Prim(</World/prim_2>))]
                
        """
