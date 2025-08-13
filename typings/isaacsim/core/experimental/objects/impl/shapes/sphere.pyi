from __future__ import annotations
import isaacsim.core.experimental.objects.impl.shapes.shape
from isaacsim.core.experimental.objects.impl.shapes.shape import Shape
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
import typing
import warp as wp
__all__: list[str] = ['Gf', 'Shape', 'Sphere', 'Usd', 'UsdGeom', 'np', 'ops_utils', 'stage_utils', 'wp']
class Sphere(isaacsim.core.experimental.objects.impl.shapes.shape.Shape):
    """
    High level class for creating/wrapping USD Sphere (primitive sphere centered at the origin) prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Sphere prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Sphere prims.
            * If the prim paths do not exist, USD Sphere prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            radii: Radii (sphere's radius) (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
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
            AssertionError: If wrapped prims are not USD Sphere.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import Sphere
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create spheres at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = Sphere(paths)  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating Shape instances of this type.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Since this method is static, the output is always on the CPU.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating Shape instances.
        
                Example:
        
                .. code-block:: python
        
                    >>> # check if the following prims at paths are valid for creating instances
                    >>> result = Sphere.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    @staticmethod
    def update_extents(geoms: list[UsdGeom.Sphere]) -> None:
        """
        Update the gprims' extents.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    geoms: Geoms to process.
                
        """
    def __init__(self, paths: str | list[str], *, radii: list | np.ndarray | wp.array | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_radii(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the radii (sphere's radius) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The radii (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the radii of all prims
                    >>> radii = prims.get_radii()
                    >>> radii.shape
                    (3, 1)
                    >>>
                    >>> # get the radii of the first and last prims
                    >>> radii = prims.get_radii(indices=[0, 2])
                    >>> radii.shape
                    (2, 1)
                
        """
    def set_radii(self, radii: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the radii (sphere's radius) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    radii: Radii (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same radii for all prims
                    >>> prims.set_radii(radii=[0.1])
                    >>>
                    >>> # set only the radius for the second prim
                    >>> prims.set_radii(radii=[0.2], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
