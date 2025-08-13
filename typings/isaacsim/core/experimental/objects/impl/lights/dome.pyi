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
__all__: list[str] = ['DomeLight', 'Light', 'Usd', 'UsdLux', 'np', 'ops_utils', 'stage_utils', 'wp']
class DomeLight(isaacsim.core.experimental.objects.impl.lights.light.Light):
    """
    High level class for creating/wrapping USD Dome Light (light emitted inward from a distant external environment) prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Dome Light prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Dome Light prims.
            * If the prim paths do not exist, USD Dome Light prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            radii: Guide radii (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            texture_files: Color texture files (shape ``(N,)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            texture_formats: Texture formats (shape ``(N,)``).
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
            AssertionError: If wrapped prims are not USD Dome Light.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import DomeLight
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create dome lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = DomeLight(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = DomeLight.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    def __init__(self, paths: str | list[str], *, radii: list | np.ndarray | wp.array | None = None, texture_files: str | list[str] | None = None, texture_formats: typing.Literal['automatic', 'latlong', 'mirroredBall', 'angular', 'cubeMapVerticalCross'] | list[typing.Literal['automatic', 'latlong', 'mirroredBall', 'angular', 'cubeMapVerticalCross']] | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_guide_radii(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the guide radii (use to visualize the dome light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The guide radii (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the guide radii of all prims
                    >>> radii = prims.get_guide_radii()
                    >>> radii.shape
                    (3, 1)
                    >>>
                    >>> # get the guide radii of the first and last prims
                    >>> radii = prims.get_guide_radii(indices=[0, 2])
                    >>> radii.shape
                    (2, 1)
                
        """
    def get_texture_files(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[str]:
        """
        Get the color texture files (e.g.: High Dynamic Range (HDR) texture intended for Image Based Lighting (IBL)) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The color texture files (shape ``(N,)``).
        
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
    def get_texture_formats(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[typing.Literal['automatic', 'latlong', 'mirroredBall', 'angular', 'cubeMapVerticalCross']]:
        """
        Get the texture formats (parameterization of the color map file) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The texture formats (shape ``(N,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the texture formats of all prims
                    >>> prims.get_texture_formats()
                    ['automatic', 'automatic', 'automatic']
                
        """
    def set_guide_radii(self, radii: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the guide radii (use to visualize the dome light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    radii: Guide radii (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same guide radii for all prims
                    >>> prims.set_guide_radii(radii=[0.1])
                    >>>
                    >>> # set only the guide radius for the second prim
                    >>> prims.set_guide_radii(radii=[0.2], indices=[1])
                
        """
    def set_texture_files(self, texture_files: str | list[str], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the color texture files (e.g.: High Dynamic Range (HDR) texture intended for Image Based Lighting (IBL)) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    texture_files: Color texture files (shape ``(N,)``).
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
    def set_texture_formats(self, texture_formats: typing.Literal['automatic', 'latlong', 'mirroredBall', 'angular', 'cubeMapVerticalCross'] | list[typing.Literal['automatic', 'latlong', 'mirroredBall', 'angular', 'cubeMapVerticalCross']], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the texture formats (parameterization of the color map file) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    texture_formats: Texture formats (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the texture formats for the second prim
                    >>> prims.set_texture_formats(texture_formats=["latlong"], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
