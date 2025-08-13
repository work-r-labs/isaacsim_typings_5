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
__all__: list[str] = ['Light', 'RectLight', 'Usd', 'UsdLux', 'np', 'ops_utils', 'stage_utils', 'wp']
class RectLight(isaacsim.core.experimental.objects.impl.lights.light.Light):
    """
    High level class for creating/wrapping USD Rect Light (light emitted from one side of a rectangle) prims.
    
        The rectangle, centered in the XY plane, emits light along the -Z axis.
    
        .. note::
    
            This class creates or wraps (one of both) USD Rect Light prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Rect Light prims.
            * If the prim paths do not exist, USD Rect Light prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            widths: Widths (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            heights: Heights (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            texture_files: Color texture files (shape ``(N,)``). In the default position, the texture file's minimum
                and maximum coordinates should be at ``(+X, +Y)`` and ``(-X, -Y)`` respectively.
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
            AssertionError: If wrapped prims are not USD Rect Light.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import RectLight
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create rect lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = RectLight(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = RectLight.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    def __init__(self, paths: str | list[str], *, widths: list | np.ndarray | wp.array | None = None, heights: list | np.ndarray | wp.array | None = None, texture_files: str | list[str] | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_heights(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the heights of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The heights (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the heights of all prims
                    >>> heights = prims.get_heights()
                    >>> heights.shape
                    (3, 1)
                    >>>
                    >>> # get the heights of the first and last prims
                    >>> heights = prims.get_heights(indices=[0, 2])
                    >>> heights.shape
                    (2, 1)
                
        """
    def get_texture_files(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[str | None]:
        """
        Get the color texture files (to use on the rectangle) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The color texture files or ``None`` if no texture is set (shape ``(N,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the color texture file for the second prim
                    >>> prims.set_texture_files(["/local/path/to/texture_1"], indices=[1])
                    >>>
                    >>> # get the color texture files of all prims
                    >>> prims.get_texture_files()
                    [None, '/local/path/to/texture_1', None]
                
        """
    def get_widths(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the widths of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The widths (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the widths of all prims
                    >>> widths = prims.get_widths()
                    >>> widths.shape
                    (3, 1)
                    >>>
                    >>> # get the widths of the first and last prims
                    >>> widths = prims.get_widths(indices=[0, 2])
                    >>> widths.shape
                    (2, 1)
                
        """
    def set_heights(self, heights: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the heights of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    heights: Heights (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same heights for all prims
                    >>> prims.set_heights(heights=[0.1])
                    >>>
                    >>> # set only the height for the second prim
                    >>> prims.set_heights(heights=[0.2], indices=[1])
                
        """
    def set_texture_files(self, texture_files: str | list[str], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the color texture files (to use on the rectangle) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    texture_files: Color texture files (shape ``(N,)``). In the default position, the texture file's minimum
                        and maximum coordinates should be at ``(+X, +Y)`` and ``(-X, -Y)`` respectively.
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set color texture files for all prims
                    >>> prims.set_texture_files(texture_files=[
                    ...     "/local/path/to/texture_0",
                    ...     "/local/path/to/texture_1",
                    ...     "/local/path/to/texture_2",
                    ... ])
                
        """
    def set_widths(self, widths: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the widths of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    lengths: Lengths (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same widths for all prims
                    >>> prims.set_widths(widths=[0.1])
                    >>>
                    >>> # set only the width for the second prim
                    >>> prims.set_widths(widths=[0.2], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
