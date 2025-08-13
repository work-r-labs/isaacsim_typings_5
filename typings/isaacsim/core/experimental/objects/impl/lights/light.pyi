from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from pxr import Gf
from pxr import Usd
from pxr import UsdLux
import typing
import warp as wp
__all__: list[str] = ['ABC', 'Gf', 'Light', 'Usd', 'UsdLux', 'XformPrim', 'abstractmethod', 'np', 'ops_utils', 'stage_utils', 'wp']
class Light(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim, abc.ABC):
    """
    Base class for creating/wrapping USD Light prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Light prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Light prims.
            * If the prim paths do not exist, USD Light prims are created at each path and a wrapper is placed over them.
    
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
            AssertionError: If both positions and translations are specified.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'are_of_type'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating Light instances of this type.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating Light instances.
                
        """
    @staticmethod
    def fetch_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Light | None]:
        """
        Fetch instances of Light from prims (or prim paths) at the given paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Prim paths (or prims) to get Light instances from.
        
                Returns:
                    List of Light instances or ``None`` if the prim is not a supported Light type.
        
                Example:
        
                .. code-block:: python
        
                    >>> import isaacsim.core.experimental.utils.stage as stage_utils
                    >>> from isaacsim.core.experimental.objects import Light
                    >>>
                    >>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
                    >>> stage_utils.define_prim(f"/World/A", "CylinderLight")  # doctest: +NO_CHECK
                    >>> stage_utils.define_prim(f"/World/B", "SphereLight")  # doctest: +NO_CHECK
                    >>>
                    >>> # fetch light instances
                    >>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
                    [None,
                     <isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
                     <isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
                
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_color_temperatures(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the color temperatures (in degrees Kelvin) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer
                and higher values are cooler). The values only take effect when ``enableColorTemperature`` is set to true (see
                :py:meth:`set_enabled_color_temperatures`).
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The color temperatures (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the color temperatures of all prims
                    >>> color_temperatures = prims.get_color_temperatures()
                    >>> color_temperatures.shape
                    (3, 1)
                    >>>
                    >>> # get the color temperatures of the first and last prims
                    >>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
                    >>> color_temperatures.shape
                    (2, 1)
                
        """
    def get_colors(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The colors (shape ``(N, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the colors of all prims
                    >>> colors = prims.get_colors()
                    >>> colors.shape
                    (3, 3)
                    >>>
                    >>> # get the colors of the first and last prims
                    >>> colors = prims.get_colors(indices=[0, 2])
                    >>> colors.shape
                    (2, 3)
                
        """
    def get_enabled_color_temperatures(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the use of color temperatures is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
                    >>> prims.set_enabled_color_temperatures([True], indices=[1])
                    >>> print(prims.get_enabled_color_temperatures())
                    [[False]
                     [ True]
                     [False]]
                
        """
    def get_enabled_normalizations(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the power normalization (by the surface area of the light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the power normalization is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the power normalization enabled state of all prims after enabling it for the second prim
                    >>> prims.set_enabled_normalizations([True], indices=[1])
                    >>> print(prims.get_enabled_normalizations())
                    [[False]
                     [ True]
                     [False]]
                
        """
    def get_exposures(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the exposures (scale light power exponentially as a power of 2) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The result is multiplied against the intensity of the light.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The exposures (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the exposures of all prims
                    >>> exposures = prims.get_exposures()
                    >>> exposures.shape
                    (3, 1)
                    >>>
                    >>> # get the exposures of the first and last prim
                    >>> exposures = prims.get_exposures(indices=[0, 2])
                    >>> exposures.shape
                    (2, 1)
                
        """
    def get_intensities(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the intensities (scale light power linearly) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The intensities (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the intensities of all prims
                    >>> intensities = prims.get_intensities()
                    >>> intensities.shape
                    (3, 1)
                    >>>
                    >>> # get the intensities of the first and last prims
                    >>> intensities = prims.get_intensities(indices=[0, 2])
                    >>> intensities.shape
                    (2, 1)
                
        """
    def get_multipliers(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The diffuse multipliers (shape ``(N, 1)``).
                    2) The specular multipliers (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the multipliers of all prims
                    >>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
                    >>> diffuse_multipliers.shape, specular_multipliers.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the multipliers of the first and last prim
                    >>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
                    >>> diffuse_multipliers.shape, specular_multipliers.shape
                    ((2, 1), (2, 1))
                
        """
    def set_color_temperatures(self, color_temperatures: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the color temperatures (in degrees Kelvin) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer
                and higher values are cooler). The values only take effect when ``enableColorTemperature`` is set to true (see
                :py:meth:`set_enabled_color_temperatures`).
        
                Args:
                    color_temperatures: Color temperatures (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same color temperatures for all prims
                    >>> prims.set_color_temperatures([8000])
                    >>>
                    >>> # set only the color temperature for the second prim
                    >>> prims.set_color_temperatures([5000], indices=[1])
                
        """
    def set_colors(self, colors: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    colors: Colors (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same colors (red) for all prims
                    >>> prims.set_colors([1.0, 0.0, 0.0])
                    >>>
                    >>> # set only the color (green) for the second prim
                    >>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
                
        """
    def set_enabled_color_temperatures(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    enabled: Boolean flags to enable/disable color temperatures (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the use of color temperatures for all prims
                    >>> prims.set_enabled_color_temperatures([True])
                    >>>
                    >>> # disable the use of color temperatures for the first and last prims
                    >>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
                
        """
    def set_enabled_normalizations(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the power normalization (by the surface area of the light) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    enabled: Boolean flags to enable/disable power normalization (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the power normalization for all prims
                    >>> prims.set_enabled_normalizations([True])
                    >>>
                    >>> # disable the power normalization for the first and last prims
                    >>> prims.set_enabled_normalizations([False], indices=[0, 2])
                
        """
    def set_exposures(self, exposures: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the exposures (scale light power exponentially as a power of 2) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The result is multiplied against the intensity of the light.
        
                Args:
                    exposures: Exposures (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same exposures for all prims
                    >>> prims.set_exposures(exposures=[10])
                    >>>
                    >>> # set only the exposure for the second prim
                    >>> prims.set_exposures(exposures=[100], indices=[1])
                
        """
    def set_intensities(self, intensities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the intensities (scale light power linearly) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    intensities: Intensities (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same intensities for all prims
                    >>> prims.set_intensities(intensities=[1000])
                    >>>
                    >>> # set only the intensity for the second prim
                    >>> prims.set_intensities(intensities=[1500], indices=[1])
                
        """
    def set_multipliers(self, diffuse_multipliers: list | np.ndarray | wp.array = None, specular_multipliers: list | np.ndarray | wp.array = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    diffuse_multipliers: Diffuse multipliers (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    specular_multipliers: Specular multipliers (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither diffuse_multipliers nor specular_multipliers are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same multipliers for all prims
                    >>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
                    >>>
                    >>> # set only the specular multiplier for the second prim
                    >>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
                
        """
    @property
    def lights(self) -> list[UsdLux.Light]:
        """
        USD Light encapsulated by the wrapper.
        
                Returns:
                    List of USD Light.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.lights  # doctest: +NO_CHECK
                    [UsdLux.Light(Usd.Prim(</World/prim_0>)),
                     UsdLux.Light(Usd.Prim(</World/prim_1>)),
                     UsdLux.Light(Usd.Prim(</World/prim_2>))]
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
