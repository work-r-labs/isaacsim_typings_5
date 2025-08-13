from __future__ import annotations
import carb as carb
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import backend as backend_utils
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import numpy as numpy_utils
import numpy as np
import omni as omni
from pxr import Gf
from pxr import PhysxSchema
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import typing
import warp as wp
import weakref as weakref
__all__: list[str] = ['Gf', 'PhysxSchema', 'RigidPrim', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdPhysics', 'XformPrim', 'backend_utils', 'carb', 'np', 'numpy_utils', 'omni', 'ops_utils', 'weakref', 'wp']
class RigidPrim(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    High level wrapper for manipulating prims (that have Rigid Body API applied) and their attributes.
    
        This class is a wrapper over one or more USD prims in the stage to provide
        high-level functionality for manipulating rigid body properties, and other attributes.
        The prims are specified using paths that can include regular expressions for matching multiple prims.
    
        .. note::
    
            If the prims do not already have the Rigid Body API applied to them, it will be applied.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
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
            masses: Masses of the rigid bodies (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            densities: Densities of the rigid bodies (shape ``(N, 1)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
    
        Raises:
            ValueError: If no prims are found matching the specified path(s).
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> import omni.timeline
            >>> from isaacsim.core.experimental.prims import RigidPrim
            >>>
            >>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # - create wrapper over single prim (with masses)
            >>> prim = RigidPrim("/World/prim_0", masses=[1.0])  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex (with masses)
            >>> prims = RigidPrim("/World/prim_.*", masses=[1.0])  # doctest: +NO_CHECK
            >>>
            >>> # play the simulation so that the Physics tensor entity becomes valid
            >>> omni.timeline.get_timeline_interface().play()
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False, masses: list | np.ndarray | wp.array | None = None, densities: list | np.ndarray | wp.array | None = None) -> None:
        ...
    def _check_for_tensor_backend(self, backend: str, *, fallback_backend: str = 'usd') -> str:
        """
        Check if the tensor backend is valid.
        """
    def _on_physics_ready(self, event) -> None:
        """
        Handle physics ready event.
        """
    def _on_timeline_stop(self, event) -> None:
        """
        Handle timeline stop event.
        """
    def apply_forces(self, forces: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, local_frame: bool = False) -> None:
        """
        Apply forces at the link transforms on the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    forces: Forces to apply (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    local_frame: Whether to apply forces in the local frame (true) or world frame (false).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # apply an external force to all prims
                    >>> forces = np.random.uniform(low=0, high=100, size=(3, 3))
                    >>> prims.apply_forces(forces)
                
        """
    def apply_forces_and_torques_at_pos(self, forces: list | np.ndarray | wp.array | None = None, torques: list | np.ndarray | wp.array | None = None, *, positions: list | np.ndarray | wp.array | None = None, indices: list | np.ndarray | wp.array | None = None, local_frame: bool = False) -> None:
        """
        Apply forces and torques at specified positions on the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    forces: Forces to apply (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    torques: Torques to apply (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    positions: Positions to apply forces and torques at (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    local_frame: Whether to apply forces and torques in the local frame (true) or world frame (false).
        
                Raises:
                    AssertionError: If neither forces nor torques are specified.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # apply an external force and torque to all prims at a specific position
                    >>> forces = np.random.uniform(low=0, high=100, size=(3, 3))
                    >>> torques = np.random.uniform(low=0, high=100, size=(3, 3))
                    >>> prims.apply_forces_and_torques_at_pos(forces, torques, positions=[0.1, 0.0, 0.0])
                
        """
    def get_coms(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the center of mass (COM) pose (position and orientation) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The center of mass positions (shape ``(N, 3)``).
                    2) The center of mass orientations (shape ``(N, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the COM poses of all prims
                    >>> positions, orientations = prims.get_coms()
                    >>> positions.shape, orientations.shape
                    ((3, 3), (3, 4))
                    >>>
                    >>> # get the COM poses of the first and last prims
                    >>> positions, orientations = prims.get_coms(indices=[0, 2])
                    >>> positions.shape, orientations.shape
                    ((2, 3), (2, 4))
                
        """
    def get_default_state(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array | None, wp.array | None, wp.array | None, wp.array | None]:
        """
        Get the default state (positions, orientations, linear velocities and angular velocities) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Four-elements tuple. 1) The default positions in the world frame (shape ``(N, 3)``).
                    2) The default orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                    3) The default linear velocities (shape ``(N, 3)``). 4) The default angular velocities (shape ``(N, 3)``).
                    If the default state is not set using the :py:meth:`set_default_state` method, ``None`` is returned.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If prims are non-root articulation links.
                
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
                    >>> # get densities of the first and last prims
                    >>> densities = prims.get_densities(indices=[0, 2])
                    >>> densities.shape
                    (2, 1)
                
        """
    def get_enabled_gravities(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the gravity on the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the gravity is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the gravity enabled state of all prims after disabling it for the second prim
                    >>> prims.set_enabled_gravities([False], indices=[1])
                    >>> print(prims.get_enabled_gravities())
                    [[ True]
                     [False]
                     [ True]]
                
        """
    def get_enabled_rigid_bodies(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the rigid body dynamics of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the rigid body dynamics is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the rigid body dynamics enabled state of all prims
                    >>> print(prims.get_enabled_rigid_bodies())
                    [[ True]
                     [ True]
                     [ True]]
                
        """
    def get_inertias(self, *, indices: list | np.ndarray | wp.array | None = None, inverse: bool = False) -> wp.array:
        """
        Get the inertia tensors of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    inverse: Whether to return inverse inertia tensors (true) or inertia tensors (false).
        
                Returns:
                    The inertia tensors or inverse inertia tensors (shape ``(N, 9)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the inertia tensors of all prims
                    >>> inertias = prims.get_inertias()
                    >>> inertias.shape
                    (3, 9)
                    >>>
                    >>> # get the inverse inertia tensors of the first and last prims
                    >>> inertias = prims.get_inertias(indices=[0, 2], inverse=True)
                    >>> inertias.shape
                    (2, 9)
                
        """
    def get_local_poses(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The translations in the local frame (shape ``(N, 3)``).
                    2) The orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the local poses of all prims
                    >>> translations, orientations = prims.get_local_poses()
                    >>> translations.shape, orientations.shape
                    ((3, 3), (3, 4))
                    >>>
                    >>> # get the local pose of the first prim
                    >>> translations, orientations = prims.get_local_poses(indices=[0])
                    >>> translations.shape, orientations.shape
                    ((1, 3), (1, 4))
                
        """
    def get_masses(self, *, indices: list | np.ndarray | wp.array | None = None, inverse: bool = False) -> wp.array:
        """
        Get the masses of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    inverse: Whether to return inverse masses (true) or masses (false).
        
                Returns:
                    The masses or inverse masses (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the masses of all prims
                    >>> masses = prims.get_masses()
                    >>> masses.shape
                    (3, 1)
                    >>>
                    >>> # get the masses of the first and last prims
                    >>> masses = prims.get_masses(indices=[0, 2])
                    >>> masses.shape
                    (2, 1)
                
        """
    def get_sleep_thresholds(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the sleep thresholds of the prims.
        
                Backends: :guilabel:`usd`.
        
                Search for *Rigid Body Dynamics* > *Sleeping* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The sleep thresholds (shape ``(N, 1)``).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the sleep thresholds of all prims
                    >>> thresholds = prims.get_sleep_thresholds()
                    >>> thresholds.shape
                    (3, 1)
                    >>>
                    >>> # get the sleep threshold of the first and last prims
                    >>> thresholds = prims.get_sleep_thresholds(indices=[0, 2])
                    >>> thresholds.shape
                    (2, 1)
                
        """
    def get_velocities(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the velocities (linear and angular) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The linear velocities (shape ``(N, 3)``). 2) The angular velocities (shape ``(N, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the velocities of all prims
                    >>> linear_velocities, angular_velocities = prims.get_velocities()
                    >>> linear_velocities.shape, angular_velocities.shape
                    ((3, 3), (3, 3))
                    >>>
                    >>> # get the velocities of the first prim
                    >>> linear_velocities, angular_velocities = prims.get_velocities(indices=[0])
                    >>> linear_velocities.shape, angular_velocities.shape
                    ((1, 3), (1, 3))
                
        """
    def get_world_poses(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The positions in the world frame (shape ``(N, 3)``).
                    2) The orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the world poses of all prims
                    >>> positions, orientations = prims.get_world_poses()
                    >>> positions.shape, orientations.shape
                    ((3, 3), (3, 4))
                    >>>
                    >>> # get the world pose of the first prim
                    >>> positions, orientations = prims.get_world_poses(indices=[0])
                    >>> positions.shape, orientations.shape
                    ((1, 3), (1, 4))
                
        """
    def is_physics_tensor_entity_valid(self) -> bool:
        """
        Check if the physics tensor entity is valid.
        
                Returns:
                    Whether the physics tensor entity is valid.
                
        """
    def reset_to_default_state(self, *, warn_on_non_default_state: bool = False) -> None:
        """
        Reset the prims to the specified default state.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                This method applies the default state defined using the :py:meth:`set_default_state` method.
        
                .. note::
        
                    This method *teleports* prims to the specified default state (positions and orientations)
                    and sets the linear and angular velocities immediately.
        
                .. warning::
        
                    This method has no effect on non-root articulation links or when no default state is set.
                    In this case, a warning message is logged if ``warn_on_non_default_state`` is ``True``.
        
                Args:
                    warn_on_non_default_state: Whether to log a warning message when no default state is set.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get default state (no default state set at this point)
                    >>> prims.get_default_state()
                    (None, None, None, None)
                    >>>
                    >>> # set default state
                    >>> # - random positions for each prim
                    >>> # - same fixed orientation for all prims
                    >>> # - zero velocities for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> prims.set_default_state(
                    ...     positions=positions,
                    ...     orientations=[1.0, 0.0, 0.0, 0.0],
                    ...     linear_velocities=np.zeros(3),
                    ...     angular_velocities=np.zeros(3),
                    ... )
                    >>>
                    >>> # get default state (default state is set)
                    >>> prims.get_default_state()
                    (array(shape=(3, 3), dtype=float32),
                     array(shape=(3, 4), dtype=float32),
                     array(shape=(3, 3), dtype=float32),
                     array(shape=(3, 3), dtype=float32))
                    >>>
                    >>> # reset prims to default state
                    >>> prims.reset_to_default_state()
                
        """
    def set_coms(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the center of mass (COM) pose (position and orientation) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    positions: Center of mass positions (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Center of mass orientations (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random COM poses for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_coms(positions, orientations)
                
        """
    def set_default_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, linear_velocities: list | np.ndarray | wp.array | None = None, angular_velocities: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the default state (positions, orientations, linear velocities and angular velocities) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. hint::
        
                    Prims can be reset to their default state by calling the :py:meth:`reset_to_default_state` method.
        
                Args:
                    positions: Default positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Default orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    linear_velocities: Default linear velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    angular_velocities: Default angular velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If prims are non-root articulation links.
                
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
        
                    >>> # set the densities for all prims
                    >>> prims.set_densities([100])
                    >>>
                    >>> # set the densities for the first and last prims
                    >>> prims.set_densities([200], indices=[0, 2])
                
        """
    def set_enabled_gravities(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the gravity on the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                When disabled, the prims will not be affected by the gravity.
        
                Args:
                    enabled: Boolean flags to enable/disable gravity (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the gravity for all prims
                    >>> prims.set_enabled_gravities([True])
                    >>>
                    >>> # disable the gravity for the first and last prims
                    >>> prims.set_enabled_gravities([False], indices=[0, 2])
                
        """
    def set_enabled_rigid_bodies(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the rigid body dynamics of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                When disabled, the prims will not participate in the physics simulation.
        
                Args:
                    enabled: Boolean flags to enable/disable rigid body dynamics (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the rigid body dynamics for all prims
                    >>> prims.set_enabled_rigid_bodies([True])
                
        """
    def set_inertias(self, inertias: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the inertia tensors of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    inertias: Inertia tensors (shape ``(N, 9)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the inertia tensors for all prims
                    >>> inertias = np.diag([0.1, 0.1, 0.1]).flatten()  # shape: (9,)
                    >>> prims.set_inertias(inertias)
                    >>>
                    >>> # set the inertia tensors for the first and last prims
                    >>> inertias = np.diag([0.2, 0.2, 0.2]).flatten()  # shape: (9,)
                    >>> prims.set_inertias(inertias, indices=[0, 2])
                
        """
    def set_local_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    translations: Translations in the local frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither translations nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random poses for all prims
                    >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_local_poses(translations, orientations)
                
        """
    def set_masses(self, masses: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the masses of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    masses: Masses (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the masses for all prims
                    >>> prims.set_masses([10.0])
                    >>>
                    >>> # set the masses for the first and last prims
                    >>> prims.set_masses([20.0], indices=[0, 2])
                
        """
    def set_sleep_thresholds(self, thresholds: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the sleep thresholds of the prims.
        
                Backends: :guilabel:`usd`.
        
                Search for *Rigid Body Dynamics* > *Sleeping* in |physx_docs| for more details.
        
                Args:
                    thresholds: Sleep thresholds (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the sleep thresholds for all prims
                    >>> prims.set_sleep_thresholds([1e-5])
                    >>>
                    >>> # set the sleep thresholds for the first and last prims
                    >>> prims.set_sleep_thresholds([1.5e-5], indices=[0, 2])
                
        """
    def set_velocities(self, linear_velocities: list | np.ndarray | wp.array | None = None, angular_velocities: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the velocities (linear and angular) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    linear_velocities: Linear velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    angular_velocities: Angular velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither linear_velocities nor angular_velocities are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random velocities for all prims
                    >>> linear_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> angular_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> prims.set_velocities(linear_velocities, angular_velocities)
                
        """
    def set_world_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    positions: Positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random poses for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_world_poses(positions, orientations)
                
        """
    @property
    def num_shapes(self) -> int:
        """
        Number of shapes in the rigid body.
        
                Backends: :guilabel:`tensor`.
        
                Returns:
                    Number of shapes in the rigid body.
        
                Raises:
                    AssertionError: Physics tensor entity is not valid.
                
        """
_MSG_PHYSICS_TENSOR_ENTITY_NOT_VALID: str = "Instance's physics tensor entity is not valid. Play the simulation/timeline to re-initialize it"
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
