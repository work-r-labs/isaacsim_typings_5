from __future__ import annotations
import isaacsim.core.experimental.objects.impl.lights.light
from isaacsim.core.experimental.objects.impl.lights.light import Light
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from pxr import Usd
from pxr import UsdLux
import typing
import warp as wp
__all__: list[str] = ['DistantLight', 'Light', 'Usd', 'UsdLux', 'np', 'ops_utils', 'stage_utils', 'wp']
class DistantLight(isaacsim.core.experimental.objects.impl.lights.light.Light):
    """
    High level class for creating/wrapping USD Distant Light (light emitted from a distant source along the -Z axis) prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Distant Light prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Distant Light prims.
            * If the prim paths do not exist, USD Distant Light prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            angles: Angles (shape ``(N, 1)``). The values are assumed to be in the range ``[0, 2 * pi)``.
                If a value is 0, the light represents a perfectly parallel light source.
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
            AssertionError: If wrapped prims are not USD Distant Light.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import DistantLight
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create distant lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = DistantLight(paths)  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating Light instances of this type.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Since this method is static, the output is always on the CPU.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating Light instances.
        
                Example:
        
                .. code-block:: python
        
                    >>> # check if the following prims at paths are valid for creating instances
                    >>> result = DistantLight.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    def __init__(self, paths: str | list[str], *, angles: list | np.ndarray | wp.array | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_angles(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the angles (angular diameter of the light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The angles (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the angles of all prims
                    >>> angles = prims.get_angles()
                    >>> angles.shape
                    (3, 1)
                    >>>
                    >>> # get the angles of the first and last prims
                    >>> angles = prims.get_angles(indices=[0, 2])
                    >>> angles.shape
                    (2, 1)
                
        """
    def set_angles(self, angles: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the angles (angular diameter of the light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    angles: Angles (shape ``(N, 1)``). The values are assumed to be in the range ``[0, 2 * pi)``.
                        If a value is 0, the light represents a perfectly parallel light source.
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same angles for all prims
                    >>> prims.set_angles(angles=[0.5236])
                    >>>
                    >>> # set only the angle for the second prim
                    >>> prims.set_angles(angles=[0.7854], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
