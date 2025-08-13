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
__all__: list[str] = ['Light', 'SphereLight', 'Usd', 'UsdLux', 'np', 'ops_utils', 'stage_utils', 'wp']
class SphereLight(isaacsim.core.experimental.objects.impl.lights.light.Light):
    """
    High level class for creating/wrapping USD Sphere Light (Light emitted outward from a sphere) prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Sphere Light prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Sphere Light prims.
            * If the prim paths do not exist, USD Sphere Light prims are created at each path and a wrapper is placed over them.
    
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
            AssertionError: If wrapped prims are not USD Sphere Light.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import SphereLight
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create sphere lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = SphereLight(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = SphereLight.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    def __init__(self, paths: str | list[str], *, radii: list | np.ndarray | wp.array | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_enabled_treat_as_points(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the treat as points (effectively, a zero-radius sphere) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Renderers that do not support non-area lighting can ignore this.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if treat as points is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the treat as points enabled state of all prims after enabling it for the second prim
                    >>> prims.set_enabled_treat_as_points([True], indices=[1])
                    >>> print(prims.get_enabled_treat_as_points())
                    [[False]
                     [ True]
                     [False]]
                
        """
    def get_radii(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the radii of the prims.
        
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
    def set_enabled_treat_as_points(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the treat as points (effectively, a zero-radius sphere) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Renderers that do not support non-area lighting can ignore this.
        
                Args:
                    enabled: Boolean flags to enable/disable treat as points (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the treat as points for all prims
                    >>> prims.set_enabled_treat_as_points([True])
                    >>>
                    >>> # disable the treat as points for the first and last prims
                    >>> prims.set_enabled_treat_as_points([False], indices=[0, 2])
                
        """
    def set_radii(self, radii: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the radii of the prims.
        
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
