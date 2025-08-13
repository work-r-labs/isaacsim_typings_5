from __future__ import annotations
import carb as carb
import isaacsim.core.experimental.materials.impl.physics_materials.physics_material
from isaacsim.core.experimental.materials.impl.physics_materials.physics_material import PhysicsMaterial
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import prim as prim_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from omni.physx.bindings import _physx as physx_bindings
from omni.physx.scripts import deformableUtils
from pxr import Usd
import typing
import warp as wp
__all__: list[str] = ['PhysicsMaterial', 'Usd', 'VolumeDeformableMaterial', 'carb', 'deformableUtils', 'np', 'ops_utils', 'physx_bindings', 'prim_utils', 'stage_utils', 'wp']
class VolumeDeformableMaterial(isaacsim.core.experimental.materials.impl.physics_materials.physics_material.PhysicsMaterial):
    """
    High level wrapper for creating/encapsulating Volume Deformable material prims.
    
        .. warning::
    
            The deformable materials require the Deformable feature (beta) to be enabled.
            Deformable feature (beta) can be enabled in *apps/.kit* experience files by setting
            ``physics.enableDeformableBeta = true`` under the ``[settings.persistent]`` section.
    
        .. note::
    
            This class creates or wraps (one of both) Volume Deformable material prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the Volume Deformable material prims.
            * If the prim paths do not exist, Volume Deformable material prims are created at each path
              and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            static_frictions: Static friction coefficients (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            dynamic_frictions: Dynamic friction coefficients (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            youngs_moduli: Young's moduli (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            poissons_ratios: Poisson's ratios (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            densities: Densities (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
    
        Raises:
            RuntimeError: If the Deformable feature (beta) is disabled.
            ValueError: If material type is invalid.
            ValueError: If resulting paths are mixed or invalid.
            AssertionError: If the created/wrapped prims are not valid USD Materials.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.materials import VolumeDeformableMaterial
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create volume deformable material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = VolumeDeformableMaterial(paths)  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating material instances of this type.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Since this method is static, the output is always on the CPU.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating material instances (shape ``(N, 1)``).
        
                Example:
        
                .. code-block:: python
        
                    >>> # check if the following prims at paths are valid for creating instances
                    >>> result = VolumeDeformableMaterial.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [[False]
                     [ True]]
                
        """
    def __init__(self, paths: str | list[str], *, static_frictions: list | np.ndarray | wp.array | None = None, dynamic_frictions: list | np.ndarray | wp.array | None = None, youngs_moduli: list | np.ndarray | wp.array | None = None, poissons_ratios: list | np.ndarray | wp.array | None = None, densities: list | np.ndarray | wp.array | None = None) -> None:
        ...
    def get_densities(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the densities of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The densities (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the densities of all prims
                    >>> densities = prims.get_densities()
                    >>> densities.shape
                    (3, 1)
                    >>>
                    >>> # get the densities of the first and last prims
                    >>> densities = prims.get_densities(indices=[0, 2])
                    >>> densities.shape
                    (2, 1)
                
        """
    def get_friction_coefficients(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the friction coefficients of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The static friction coefficients (shape ``(N, 1)``).
                    2) The dynamic friction coefficients (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the friction coefficients of all prims
                    >>> static_frictions, dynamic_frictions = prims.get_friction_coefficients()
                    >>> static_frictions.shape, dynamic_frictions.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the friction coefficients of the first and last prims
                    >>> static_frictions, dynamic_frictions = prims.get_friction_coefficients(indices=[0, 2])
                    >>> static_frictions.shape, dynamic_frictions.shape
                    ((2, 1), (2, 1))
                
        """
    def get_poissons_ratios(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the Poisson's ratios of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The Poisson's ratios (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the Poisson's ratios of all prims
                    >>> ratios = prims.get_poissons_ratios()
                    >>> ratios.shape
                    (3, 1)
                    >>>
                    >>> # get the Poisson's ratios of the first and last prims
                    >>> ratios = prims.get_poissons_ratios(indices=[0, 2])
                    >>> ratios.shape
                    (2, 1)
                
        """
    def get_youngs_moduli(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the Young's moduli of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The Young's moduli (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the Young's moduli of all prims
                    >>> moduli = prims.get_youngs_moduli()
                    >>> moduli.shape
                    (3, 1)
                    >>>
                    >>> # get the Young's moduli of the first and last prims
                    >>> moduli = prims.get_youngs_moduli(indices=[0, 2])
                    >>> moduli.shape
                    (2, 1)
                
        """
    def set_densities(self, densities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the densities of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    densities: Densities (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same densities for all prims
                    >>> prims.set_densities(densities=[1000])
                    >>>
                    >>> # set only the density for the second prim
                    >>> prims.set_densities(densities=[1500], indices=[1])
                
        """
    def set_friction_coefficients(self, static_frictions: list | np.ndarray | wp.array = None, dynamic_frictions: list | np.ndarray | wp.array = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the friction coefficients of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    static_frictions: Static friction coefficients (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dynamic_frictions: Dynamic friction coefficients (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither static_frictions nor dynamic_frictions are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same friction coefficients (static: 0.5, dynamic: 0.2) for all prims
                    >>> prims.set_friction_coefficients(static_frictions=[0.5], dynamic_frictions=[0.2])
                    >>>
                    >>> # set only the dynamic friction coefficient for the second prim
                    >>> prims.set_friction_coefficients(dynamic_frictions=[0.3], indices=[1])
                
        """
    def set_poissons_ratios(self, poissons_ratios: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the Poisson's ratio of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    poissons_ratios: Poisson's ratios (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same Poisson's ratio for all prims
                    >>> prims.set_poissons_ratios(poissons_ratios=[0.45])
                    >>>
                    >>> # set only the Poisson's ratio for the second prim
                    >>> prims.set_poissons_ratios(poissons_ratios=[0.4], indices=[1])
                
        """
    def set_youngs_moduli(self, youngs_moduli: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the Young's modulus of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    youngs_moduli: Young's moduli (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same Young's modulus for all prims
                    >>> prims.set_youngs_moduli(youngs_moduli=[500000.0])
                    >>>
                    >>> # set only the Young's modulus for the second prim
                    >>> prims.set_youngs_moduli(youngs_moduli=[600000.0], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
