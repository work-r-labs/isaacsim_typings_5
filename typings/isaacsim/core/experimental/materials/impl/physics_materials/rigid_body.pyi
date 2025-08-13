from __future__ import annotations
import isaacsim.core.experimental.materials.impl.physics_materials.physics_material
from isaacsim.core.experimental.materials.impl.physics_materials.physics_material import PhysicsMaterial
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import prim as prim_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
from pxr import PhysxSchema
from pxr import Usd
from pxr import UsdPhysics
from pxr import UsdShade
import typing
import warp as wp
__all__: list[str] = ['PhysicsMaterial', 'PhysxSchema', 'RigidBodyMaterial', 'Usd', 'UsdPhysics', 'UsdShade', 'np', 'ops_utils', 'prim_utils', 'stage_utils', 'wp']
class RigidBodyMaterial(isaacsim.core.experimental.materials.impl.physics_materials.physics_material.PhysicsMaterial):
    """
    High level wrapper for creating/encapsulating Rigid Body material prims.
    
        .. note::
    
            This class creates or wraps (one of both) Rigid Body material prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the Rigid Body material prims.
            * If the prim paths do not exist, Rigid Body material prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            static_frictions: Static friction coefficients (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            dynamic_frictions: Dynamic friction coefficients (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            restitutions: Restitution coefficients (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            densities: Densities (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
    
        Raises:
            ValueError: If resulting paths are mixed or invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.materials import RigidBodyMaterial
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create rigid body material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = RigidBodyMaterial(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = RigidBodyMaterial.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [[False]
                     [ True]]
                
        """
    def __init__(self, paths: str | list[str], *, static_frictions: list | np.ndarray | wp.array | None = None, dynamic_frictions: list | np.ndarray | wp.array | None = None, restitutions: list | np.ndarray | wp.array | None = None, densities: list | np.ndarray | wp.array | None = None) -> None:
        ...
    def get_combine_modes(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[typing.Literal['average', 'max', 'min', 'multiply']], list[typing.Literal['average', 'max', 'min', 'multiply']], list[typing.Literal['average', 'max', 'min', 'multiply']]]:
        """
        Get the way two material properties will be combined to yield a coefficient for a collision.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Three-elements tuple. 1) The friction combine modes (shape ``(N,)``).
                    2) The restitution combine modes (shape ``(N,)``).
                    3) The damping combine modes (shape ``(N,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the combine modes of all prims
                    >>> frictions, restitutions, dampings = prims.get_combine_modes()
                    >>> frictions
                    ['average', 'average', 'average']
                    >>> restitutions
                    ['average', 'average', 'average']
                    >>> dampings
                    ['average', 'average', 'average']
                
        """
    def get_compliant_contact_gains(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the compliant contact gains (stiffnesses and dampings) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The stiffnesses (shape ``(N, 1)``).
                    2) The dampings (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the compliant contact gains of all prims
                    >>> stiffnesses, dampings = prims.get_compliant_contact_gains()
                    >>> stiffnesses.shape, dampings.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the compliant contact gains of the first and last prims
                    >>> stiffnesses, dampings = prims.get_compliant_contact_gains(indices=[0, 2])
                    >>> stiffnesses.shape, dampings.shape
                    ((2, 1), (2, 1))
                
        """
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
    def get_enabled_compliant_contacts(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the compliant spring-damper contact effects of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the compliant contact effects are enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the compliant contact enabled state of all prims after enabling it for the second prim
                    >>> prims.set_enabled_compliant_contacts([True], indices=[1])
                    >>> print(prims.get_enabled_compliant_contacts())
                    [[False]
                     [ True]
                     [False]]
                
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
    def get_restitution_coefficients(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the restitution coefficients of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The restitution coefficients (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the restitution coefficients of all prims
                    >>> restitutions = prims.get_restitution_coefficients()
                    >>> restitutions.shape
                    (3, 1)
                    >>>
                    >>> # get the restitution coefficients of the first and last prims
                    >>> restitutions = prims.get_restitution_coefficients(indices=[0, 2])
                    >>> restitutions.shape
                    (2, 1)
                
        """
    def set_combine_modes(self, frictions: typing.Literal['average', 'max', 'min', 'multiply'] | list[typing.Literal['average', 'max', 'min', 'multiply']] | None = None, restitutions: typing.Literal['average', 'max', 'min', 'multiply'] | list[typing.Literal['average', 'max', 'min', 'multiply']] | None = None, dampings: typing.Literal['average', 'max', 'min', 'multiply'] | list[typing.Literal['average', 'max', 'min', 'multiply']] | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the way two material properties will be combined to yield a coefficient for a collision.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    frictions: Friction combine modes (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    restitutions: Restitution combine modes (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dampings: Damping combine modes (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                        This argument is only relevant for compliant contact interactions.
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither frictions, restitutions nor dampings are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the combine modes (frictions: 'average', restitutions: 'max', dampings: 'min') for all prims
                    >>> prims.set_combine_modes(frictions=["average"], restitutions=["max"], dampings=["min"])
                
        """
    def set_compliant_contact_gains(self, stiffnesses: list | np.ndarray | wp.array | None = None, dampings: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the compliant contact gains (stiffnesses and dampings) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    The spring stiffnesses must be set to a value greater than 0 before enabling compliant contact effects.
        
                Args:
                    stiffnesses: Stiffnesses (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dampings: Dampings (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither stiffnesses nor dampings are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same compliant contact gains (stiffnesses: 100.0, dampings: 10.0) for all prims
                    >>> prims.set_compliant_contact_gains(stiffnesses=[100.0], dampings=[10.0])
                    >>>
                    >>> # set only the damping for the second prim
                    >>> prims.set_compliant_contact_gains(dampings=[15.0], indices=[1])
                
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
    def set_enabled_compliant_contacts(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the compliant spring-damper contact effects of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    The spring stiffnesses (see :py:meth:`set_compliant_contact_gains`) must be set to a value greater than 0
                    before enabling compliant contact effects.
        
                Args:
                    enabled: Boolean flags to enable/disable compliant contact effects (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the compliant contact effects for all prims
                    >>> prims.set_enabled_compliant_contacts([True])
                    >>>
                    >>> # disable the compliant contact effects for the first and last prims
                    >>> prims.set_enabled_compliant_contacts([False], indices=[0, 2])
                
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
    def set_restitution_coefficients(self, restitutions: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the restitution coefficients of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    restitutions: Restitution coefficients (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same restitution coefficients for all prims
                    >>> prims.set_restitution_coefficients(restitutions=[0.005])
                    >>>
                    >>> # set only the restitution coefficient for the second prim
                    >>> prims.set_restitution_coefficients(restitutions=[0.002], indices=[1])
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
