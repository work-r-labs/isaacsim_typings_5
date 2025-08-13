from __future__ import annotations
import carb as carb
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import backend as backend_utils
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import numpy as numpy_utils
from isaacsim.core.utils.prims import get_articulation_root_api_prim_path
import numpy as np
import omni as omni
from pxr import PhysicsSchemaTools
from pxr import PhysxSchema
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import typing
import warp as wp
import weakref as weakref
__all__: list[str] = ['Articulation', 'PhysicsSchemaTools', 'PhysxSchema', 'Sdf', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdPhysics', 'XformPrim', 'backend_utils', 'carb', 'get_articulation_root_api_prim_path', 'np', 'numpy_utils', 'omni', 'ops_utils', 'stage_utils', 'weakref', 'wp']
class Articulation(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    High level wrapper for manipulating prims (that have the Root Articulation API applied) and their attributes.
    
        This class is a wrapper over one or more USD prims in the stage to provide
        high-level functionality for manipulating articulation properties, and other attributes.
        The prims are specified using paths that can include regular expressions for matching multiple prims.
    
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
            enable_residual_reports: Whether to enable residual reporting for the articulations.
    
        Raises:
            ValueError: If no prims are found matching the specified path(s).
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> import omni.timeline
            >>> from isaacsim.core.experimental.prims import Articulation
            >>>
            >>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # where each prim is a reference to the Isaac Sim's Franka Panda USD asset
            >>> # - create wrapper over single prim
            >>> prim = Articulation("/World/prim_0")  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex
            >>> prims = Articulation(
            ...     "/World/prim_.*",
            ...     positions=[[x, 0, 0] for x in range(3)],
            ...     reset_xform_op_properties=True,
            ...     enable_residual_reports=True,
            ... )  # doctest: +NO_CHECK
            >>>
            >>> # play the simulation so that the Physics tensor entity becomes valid
            >>> omni.timeline.get_timeline_interface().play()
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        """
        Clean up instance by deregistering callbacks and resetting internal state.
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False, enable_residual_reports: bool = False) -> None:
        ...
    def _check_for_tensor_backend(self, backend: str, *, fallback_backend: str = 'usd') -> str:
        """
        Check if the tensor backend is valid.
        """
    def _get_drive_api_and_type(self, index: int, dof_index: int) -> tuple[UsdPhysics.DriveAPI, str]:
        """
        Get the drive API and type for a given degree of freedom (DOF).
        
                Args:
                    index: Index of the prim to process.
                    dof_index: Index of the DOF to process.
        
                Returns:
                    Two-elements tuple. 1) The drive API. 2) The type of the DOF.
                
        """
    def _on_physics_ready(self, event) -> None:
        """
        Handle physics ready event.
        """
    def _on_timeline_stop(self, event):
        """
        Handle timeline stop event.
        """
    def _query_articulation_properties(self) -> None:
        """
        Query articulation properties.
        """
    def get_default_state(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None]:
        """
        Get the default state (root positions, orientations, linear velocities and angular velocities,
                and DOF positions, velocities and efforts) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Seven-elements tuple. 1) The default root positions in the world frame (shape ``(N, 3)``).
                    2) The default root orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                    3) The default root linear velocities (shape ``(N, 3)``). 4) The default root angular velocities (shape ``(N, 3)``).
                    5) The default DOF positions (shape ``(N, D)``). 6) The default DOF velocities (shape ``(N, D)``).
                    7) The default DOF efforts (shape ``(N, D)``).
                    If the default state is not set using the :py:meth:`set_default_state` method, ``None`` is returned.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not initialized.
                
        """
    def get_dof_armatures(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the armatures of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Search for *Armature* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Armatures (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF armatures of all prims
                    >>> armatures = prims.get_dof_armatures()
                    >>> armatures.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF armatures of the first and last prims' finger DOFs
                    >>> armatures = prims.get_dof_armatures(indices=[0, 2], dof_indices=[7, 8])
                    >>> armatures.shape
                    (2, 2)
                
        """
    def get_dof_coriolis_and_centrifugal_compensation_forces(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the Coriolis and centrifugal compensation forces (DOF forces required to counteract Coriolis and
                centrifugal forces for the given articulation state) of the prims
        
                Backends: :guilabel:`tensor`.
        
                Search for *Coriolis and Centrifugal Compensation Force* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    The Coriolis and centrifugal compensation forces of the prims.
                    For fixed articulation base shape is ``(N, D)``. For non-fixed (floating) articulation base shape
                    is ``(N, D + 6)`` since the forces acting on the root are also provided.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the coriolis and centrifugal compensation forces (fixed articulation base) of all prims
                    >>> forces = prims.get_dof_coriolis_and_centrifugal_compensation_forces()
                    >>> forces.shape
                    (3, 9)
                
        """
    def get_dof_drive_model_properties(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array, wp.array]:
        """
        Get the drive model properties of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Three-element tuple. 1) Speed effort gradients (shape ``(N, D)``).
                    2) Maximum actuator velocities (shape ``(N, D)``). 3) Velocity-dependent resistances (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF drive model properties of all prims
                    >>> speed_effort_gradients, maximum_actuator_velocities, velocity_dependent_resistances = prims.get_dof_drive_model_properties()
                    >>> speed_effort_gradients.shape, maximum_actuator_velocities.shape, velocity_dependent_resistances.shape
                    ((3, 9), (3, 9), (3, 9))
                    >>>
                    >>> # get the DOF drive model properties of the first and last prims
                    >>> speed_effort_gradients, maximum_actuator_velocities, velocity_dependent_resistances = prims.get_dof_drive_model_properties(indices=[0, 2])
                    >>> speed_effort_gradients.shape, maximum_actuator_velocities.shape, velocity_dependent_resistances.shape
                    ((2, 9), (2, 9), (2, 9))
                
        """
    def get_dof_drive_types(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> list[list[str]]:
        """
        Get the drive types of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    The drive types. Possible values are ``acceleration`` or ``force`` (shape ``(N, D)``).
                    If the drive type is not set, ``None`` is returned.
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the drive types of the first prim
                    >>> drive_types = prims.get_dof_drive_types(indices=[0])
                    >>> print(drive_types)
                    [['force', 'force', 'force', 'force', 'force', 'force', 'force', 'force', 'none']]
                
        """
    def get_dof_efforts(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the efforts of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF efforts (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF efforts of all prims
                    >>> efforts = prims.get_dof_efforts()
                    >>> efforts.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF efforts of the first and last prims' finger DOFs
                    >>> efforts = prims.get_dof_efforts(indices=[0, 2], dof_indices=[7, 8])
                    >>> efforts.shape
                    (2, 2)
                
        """
    def get_dof_friction_properties(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array, wp.array]:
        """
        Get the friction properties of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Three-element tuple. 1) Static friction efforts (shape ``(N, D)``).
                    2) Dynamic friction efforts (shape ``(N, D)``). 3) Viscous friction coefficients (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF friction properties of all prims
                    >>> static_frictions, dynamic_frictions, viscous_frictions = prims.get_dof_friction_properties()
                    >>> static_frictions.shape, dynamic_frictions.shape, viscous_frictions.shape
                    ((3, 9), (3, 9), (3, 9))
                    >>>
                    >>> # get the DOF friction properties of the first and last prims
                    >>> static_frictions, dynamic_frictions, viscous_frictions = prims.get_dof_friction_properties(indices=[0, 2])
                    >>> static_frictions.shape, dynamic_frictions.shape, viscous_frictions.shape
                    ((2, 9), (2, 9), (2, 9))
                
        """
    def get_dof_gains(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the implicit Proportional-Derivative (PD) controller's gains (stiffnesses and dampings)
                of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Two-elements tuple. 1) Stiffnesses (shape ``(N, D)``). 2) Dampings (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF gains of all prims
                    >>> stiffnesses, dampings = prims.get_dof_gains()
                    >>> stiffnesses.shape, dampings.shape
                    ((3, 9), (3, 9))
                    >>>
                    >>> # get the DOF gains of the first and last prims' finger DOFs
                    >>> stiffnesses, dampings = prims.get_dof_gains(indices=[0, 2], dof_indices=[7, 8])
                    >>> stiffnesses.shape, dampings.shape
                    ((2, 2), (2, 2))
                
        """
    def get_dof_gravity_compensation_forces(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the gravity compensation forces (DOF forces required to counteract gravitational
                forces for the given articulation pose) of the prims
        
                Backends: :guilabel:`tensor`.
        
                Search for *Gravity Compensation Force* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    The gravity compensation forces of the prims.
                    For fixed articulation base shape is ``(N, D)``. For non-fixed (floating) articulation base shape
                    is ``(N, D + 6)`` since the forces acting on the root are also provided.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the gravity compensation forces of all prims
                    >>> forces = prims.get_dof_gravity_compensation_forces()
                    >>> forces.shape
                    (3, 9)
                    >>>
                    >>> # get the gravity compensation forces of the first and last prims' finger DOFs
                    >>> forces = prims.get_dof_gravity_compensation_forces(indices=[0, 2], dof_indices=[7, 8])
                    >>> forces.shape
                    (2, 2)
                
        """
    def get_dof_indices(self, names: str | list[str]) -> wp.array:
        """
        Get the indices of one or more degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Args:
                    names: Single name or list of names of DOFs to get indices for.
        
                Returns:
                    Indices of the specified DOF names.
        
                Example:
        
                .. code-block:: python
        
                    >>> # show all DOF names and their indices
                    >>> for name in prims.dof_names:
                    ...     print(prims.get_dof_indices(name), name)
                    [0] panda_joint1
                    [1] panda_joint2
                    [2] panda_joint3
                    [3] panda_joint4
                    [4] panda_joint5
                    [5] panda_joint6
                    [6] panda_joint7
                    [7] panda_finger_joint1
                    [8] panda_finger_joint2
                    >>>
                    >>> # get the indices of Franka Panda's finger DOFs
                    >>> indices = prims.get_dof_indices(["panda_finger_joint1", "panda_finger_joint2"])
                    >>> print(indices)
                    [7 8]
                
        """
    def get_dof_limits(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the limits of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Two-element tuple: 1) Lower limits (shape ``(N, D)``). 2) Upper limits (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF limits of all prims
                    >>> lower, upper = prims.get_dof_limits()
                    >>> lower.shape, upper.shape
                    ((3, 9), (3, 9))
                    >>>
                    >>> # get the DOF limits of the first and last prims
                    >>> lower, upper = prims.get_dof_limits(indices=[0, 2])
                    >>> lower.shape, upper.shape
                    ((2, 9), (2, 9))
                
        """
    def get_dof_max_efforts(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the maximum forces applied by the drive of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Maximum forces applied by the drive (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF maximum efforts of all prims
                    >>> max_efforts = prims.get_dof_max_efforts()
                    >>> max_efforts.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF maximum efforts of the first and last prims' finger DOFs
                    >>> max_efforts = prims.get_dof_max_efforts(indices=[0, 2], dof_indices=[7, 8])
                    >>> max_efforts.shape
                    (2, 2)
                
        """
    def get_dof_max_velocities(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the maximum velocities of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    Maximum velocities (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF maximum velocities of all prims
                    >>> max_velocities = prims.get_dof_max_velocities()
                    >>> max_velocities.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF maximum velocities of the first and last prims' finger DOFs
                    >>> max_velocities = prims.get_dof_max_velocities(indices=[0, 2], dof_indices=[7, 8])
                    >>> max_velocities.shape
                    (2, 2)
                
        """
    def get_dof_position_targets(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the position targets of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF position targets (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF position targets of all prims
                    >>> position_targets = prims.get_dof_position_targets()
                    >>> position_targets.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF position targets of the first and last prims' finger DOFs
                    >>> position_targets = prims.get_dof_position_targets(indices=[0, 2], dof_indices=[7, 8])
                    >>> position_targets.shape
                    (2, 2)
                
        """
    def get_dof_positions(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the positions of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF positions (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF position of all prims
                    >>> positions = prims.get_dof_positions()
                    >>> positions.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF position of the first and last prims' finger DOFs
                    >>> positions = prims.get_dof_positions(indices=[0, 2], dof_indices=[7, 8])
                    >>> positions.shape
                    (2, 2)
                
        """
    def get_dof_projected_joint_forces(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the degrees of freedom (DOF) projected joint forces of the prims.
        
                Backends: :guilabel:`tensor`.
        
                This method projects the links incoming joint forces in the motion direction
                and hence is the active component of the force.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF projected joint forces (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF projected joint forces of all prims
                    >>> forces = prims.get_dof_projected_joint_forces()
                    >>> forces.shape
                    (3, 9)
                    >>>
                    >>> # get the projected joint forces of the first and last prims' finger DOFs
                    >>> forces = prims.get_dof_projected_joint_forces(indices=[0, 2], dof_indices=[7, 8])
                    >>> forces.shape
                    (2, 2)
                
        """
    def get_dof_velocities(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the velocities of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF velocities (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF velocities of all prims
                    >>> velocities = prims.get_dof_velocities()
                    >>> velocities.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF velocity of the first and last prims' finger DOFs
                    >>> velocities = prims.get_dof_velocities(indices=[0, 2], dof_indices=[7, 8])
                    >>> velocities.shape
                    (2, 2)
                
        """
    def get_dof_velocity_targets(self, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the velocity targets of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Returns:
                    DOF velocity targets (shape ``(N, D)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the DOF velocity targets of all prims
                    >>> velocity_targets = prims.get_dof_velocity_targets()
                    >>> velocity_targets.shape
                    (3, 9)
                    >>>
                    >>> # get the DOF velocity target of the first and last prims' finger DOFs
                    >>> velocity_targets = prims.get_dof_velocity_targets(indices=[0, 2], dof_indices=[7, 8])
                    >>> velocity_targets.shape
                    (2, 2)
                
        """
    def get_enabled_self_collisions(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enable state of the self-collisions processing of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the self-collisions processing is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the self-collisions enabled state of all prims
                    >>> print(prims.get_enabled_self_collisions())
                    [[False]
                     [False]
                     [False]]
                
        """
    def get_fixed_tendon_dampings(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the dampings of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The dampings of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_fixed_tendon_limit_stiffnesses(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the limit stiffnesses of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The limit stiffnesses of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_fixed_tendon_limits(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the limits of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The lower limits of the fixed tendons (shape ``(N, T)``).
                    2) The upper limits of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_fixed_tendon_offsets(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the offsets of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The offsets of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_fixed_tendon_rest_lengths(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the rest length of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The rest lengths of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_fixed_tendon_stiffnesses(self, *, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the stiffness of the fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The stiffnesses of the fixed tendons (shape ``(N, T)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def get_jacobian_matrices(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the Jacobian matrices of the prims.
        
                Backends: :guilabel:`tensor`.
        
                .. note::
        
                    The first dimension corresponds to the amount of wrapped prims while the last 3 dimensions are the
                    Jacobian matrix shape. Refer to the :py:attr:`jacobian_matrix_shape` property for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The Jacobian matrices of the prims (shape ``(N, *jacobian_matrix_shape)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the Jacobian matrices of all prims
                    >>> jacobians = prims.get_jacobian_matrices()
                    >>> jacobians.shape
                    (3, 10, 6, 9)
                
        """
    def get_joint_indices(self, names: str | list[str]) -> wp.array:
        """
        Get the indices of one or more joints of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Args:
                    names: Single name or list of names of joints to get indices for.
        
                Returns:
                    Indices of the specified joint names.
        
                Example:
        
                .. code-block:: python
        
                    >>> # show all joint names and their indices
                    >>> for name in prims.joint_names:
                    ...     print(prims.get_joint_indices(name), name)
                    [0] panda_joint1
                    [1] panda_joint2
                    [2] panda_joint3
                    [3] panda_joint4
                    [4] panda_joint5
                    [5] panda_joint6
                    [6] panda_joint7
                    [7] panda_hand_joint
                    [8] panda_finger_joint1
                    [9] panda_finger_joint2
                    >>>
                    >>> # get the indices of Franka Panda's finger joints
                    >>> indices = prims.get_joint_indices(["panda_finger_joint1", "panda_finger_joint2"])
                    >>> print(indices)
                    [8 9]
                
        """
    def get_link_coms(self, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the center of mass (COM) pose (position and orientation) of the links of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Returns:
                    Two-elements tuple. 1) The center of mass positions (shape ``(N, L, 3)``).
                    2) The center of mass orientations (shape ``(N, L, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the COM poses of the links of all prims
                    >>> positions, orientations = prims.get_link_coms()
                    >>> positions.shape, orientations.shape
                    ((3, 11, 3), (3, 11, 4))
                    >>>
                    >>> # get the COM poses of the first and last prims' finger links
                    >>> positions, orientations = prims.get_link_coms(indices=[0, 2], link_indices=[9, 10])
                    >>> positions.shape, orientations.shape
                    ((2, 2, 3), (2, 2, 4))
                
        """
    def get_link_enabled_gravities(self, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the gravity on the links of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Returns:
                    Boolean flags indicating if the gravity is enabled on the links (shape ``(N, L)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the gravity enabled state of the links of all prims
                    >>> enabled = prims.get_link_enabled_gravities()
                    >>> enabled.shape
                    (3, 11)
                    >>>
                    >>> # get the gravity enabled state of the first and last prims' finger links
                    >>> enabled = prims.get_link_enabled_gravities(indices=[0, 2], link_indices=[9, 10])
                    >>> enabled.shape
                    (2, 2)
                
        """
    def get_link_incoming_joint_force(self, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the link incoming joint forces and torques to external loads of the prims.
        
                Backends: :guilabel:`tensor`.
        
                In a kinematic tree, each link has a single incoming joint.
                This method provides the total 6D force/torque of links incoming joints.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Returns:
                    Two-elements tuple. 1) The link incoming joint forces (shape ``(N, L, 3)``).
                    2) The link incoming joint torques (shape ``(N, L, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the incoming joint forces and torques of the links of all prims
                    >>> forces, torques = prims.get_link_incoming_joint_force()
                    >>> forces.shape, torques.shape
                    ((3, 11, 3), (3, 11, 3))
                    >>>
                    >>> # get the incoming joint forces and torques of the first and last prims' finger links
                    >>> forces, torques = prims.get_link_incoming_joint_force(indices=[0, 2], link_indices=[9, 10])
                    >>> forces.shape, torques.shape
                    ((2, 2, 3), (2, 2, 3))
                
        """
    def get_link_indices(self, names: str | list[str]) -> wp.array:
        """
        Get the indices of one or more links of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Args:
                    names: Single name or list of names of links to get indices for.
        
                Returns:
                    Indices of the specified link names.
        
                Example:
        
                .. code-block:: python
        
                    >>> # show all link names and their indices
                    >>> for name in prims.link_names:
                    ...     print(prims.get_link_indices(name), name)
                    [0] panda_link0
                    [1] panda_link1
                    [2] panda_link2
                    [3] panda_link3
                    [4] panda_link4
                    [5] panda_link5
                    [6] panda_link6
                    [7] panda_link7
                    [8] panda_hand
                    [9] panda_leftfinger
                    [10] panda_rightfinger
                    >>>
                    >>> # get the indices of Franka Panda's finger links
                    >>> indices = prims.get_link_indices(["panda_leftfinger", "panda_rightfinger"])
                    >>> print(indices)
                    [ 9 10]
                
        """
    def get_link_inertias(self, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None, inverse: bool = False) -> wp.array:
        """
        Get the inertias tensors of the links of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
                    inverse: Whether to return inverse inertia tensors (true) or inertia tensors (false).
        
                Returns:
                    The inertia tensors or inverse inertia tensors (shape ``(N, L, 9)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the inertia tensors of the links of all prims
                    >>> inertias = prims.get_link_inertias()
                    >>> inertias.shape
                    (3, 11, 9)
                    >>>
                    >>> # get the inverse inertia tensors of the first and last prims' finger links
                    >>> inertias = prims.get_link_inertias(indices=[0, 2], link_indices=[9, 10], inverse=True)
                    >>> inertias.shape
                    (2, 2, 9)
                
        """
    def get_link_masses(self, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None, inverse: bool = False) -> wp.array:
        """
        Get the masses of the links of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
                    inverse: Whether to return inverse masses (true) or masses (false).
        
                Returns:
                    The link masses (shape ``(N, L)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the masses of the links of all prims
                    >>> masses = prims.get_link_masses()
                    >>> masses.shape
                    (3, 11)
                    >>>
                    >>> # get the inverse masses of the first and last prims' finger links
                    >>> inverse_masses = prims.get_link_masses(indices=[0, 2], link_indices=[9, 10], inverse=True)
                    >>> inverse_masses.shape
                    (2, 2)
                
        """
    def get_local_poses(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the root poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The root translations in the local frame (shape ``(N, 3)``).
                    2) The root orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
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
    def get_mass_matrices(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the mass matrices of the prims.
        
                Backends: :guilabel:`tensor`.
        
                .. note::
        
                    The first dimension corresponds to the amount of wrapped prims while the last 2 dimensions are the
                    mass matrix shape. Refer to the :py:attr:`mass_matrix_shape` property for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The mass matrices of the prims (shape ``(N, *mass_matrix_shape)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the mass matrices of all prims
                    >>> mass_matrices = prims.get_mass_matrices()
                    >>> mass_matrices.shape
                    (3, 9, 9)
                
        """
    def get_sleep_thresholds(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the sleep thresholds of the prims.
        
                Backends: :guilabel:`usd`.
        
                Search for *Articulations and Sleeping* in |physx_docs| for more details
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The sleep thresholds (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
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
    def get_solver_iteration_counts(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the physics solver iteration counts (position and velocity) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-element tuple: 1) Position iteration counts (shape ``(N, 1)``).
                    2) Velocity iteration counts (shape ``(N, 1)``).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the solver iteration counts of all prims
                    >>> position_counts, velocity_counts = prims.get_solver_iteration_counts()
                    >>> position_counts.shape, velocity_counts.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the solver iteration counts of the first and last prims
                    >>> position_counts, velocity_counts = prims.get_solver_iteration_counts(indices=[0, 2])
                    >>> position_counts.shape, velocity_counts.shape
                    ((2, 1), (2, 1))
                
        """
    def get_solver_residual_reports(self, *, indices: list | np.ndarray | wp.array | None = None, report_maximum: bool = True) -> tuple[wp.array, wp.array]:
        """
        Get the physics solver residuals (position and velocity) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The solver residual quantifies the convergence of the iterative physics solver.
                A perfectly converged solution has a residual value of zero.
                For articulations, the solver residual is computed across all joints that are part of the articulations.
        
                Search for *Solver Residual* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    report_maximum: Whether to report the maximum (true) or the root mean square (false) residual.
        
                Returns:
                    Two-elements tuple. 1) The solver residuals for position (shape ``(N, 1)``).
                    2) The solver residuals for velocity (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Residual reporting is not enabled.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the solver residuals of all prims
                    >>> position_residuals, velocity_residuals = prims.get_solver_residual_reports()
                    >>> position_residuals.shape, velocity_residuals.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the solver residuals of the first and last prims
                    >>> position_residuals, velocity_residuals = prims.get_solver_residual_reports(indices=[0, 2])
                    >>> position_residuals.shape, velocity_residuals.shape
                    ((2, 1), (2, 1))
                
        """
    def get_stabilization_thresholds(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the mass-normalized kinetic energy below which the prims may participate in stabilization.
        
                Backends: :guilabel:`usd`.
        
                Search for *Stabilization Threshold* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Stabilization thresholds (shape ``(N, 1)``).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the stabilization thresholds of all prims
                    >>> thresholds = prims.get_stabilization_thresholds()
                    >>> thresholds.shape
                    (3, 1)
                    >>>
                    >>> # get the stabilization threshold of the first and last prims
                    >>> thresholds = prims.get_stabilization_thresholds(indices=[0, 2])
                    >>> thresholds.shape
                    (2, 1)
                
        """
    def get_velocities(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the root velocities (linear and angular) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The root linear velocities (shape ``(N, 3)``).
                    2) The root angular velocities (shape ``(N, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
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
        Get the root poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The root positions in the world frame (shape ``(N, 3)``).
                    2) The root orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
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
    def is_physics_tensor_entity_initialized(self) -> bool:
        """
        Check if the physics tensor entity is initialized.
        
                Returns:
                    Whether the physics tensor entity is initialized.
                
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
        
                Backends: :guilabel:`tensor`.
        
                This method applies the default state defined using the :py:meth:`set_default_state` method.
        
                .. note::
        
                    This method *teleports* prims to the specified default state (positions and orientations)
                    and sets the linear and angular velocities and the DOF positions, velocities and efforts immediately.
        
                .. warning::
        
                    This method has no effect when no default state is set.
                    In this case, a warning message is logged if ``warn_on_non_default_state`` is ``True``.
        
                Args:
                    warn_on_non_default_state: Whether to log a warning message when no default state is set.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get default state (no default state set at this point)
                    >>> prims.get_default_state()
                    (None, None, None, None, None, None, None)
                    >>>
                    >>> # set default state
                    >>> # - random root positions for each prim
                    >>> # - same fixed orientation for all prims
                    >>> # - zero root velocities for all prims
                    >>> # - random DOF positions for all DOFs
                    >>> # - zero DOF velocities for all DOFs
                    >>> # - zero DOF efforts for all DOFs
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> prims.set_default_state(
                    ...     positions=positions,
                    ...     orientations=[1.0, 0.0, 0.0, 0.0],
                    ...     linear_velocities=np.zeros(3),
                    ...     angular_velocities=np.zeros(3),
                    ...     dof_positions=np.random.uniform(low=-0.25, high=0.25, size=(3, 9)),
                    ...     dof_velocities=np.zeros(9),
                    ...     dof_efforts=np.zeros(9),
                    ... )
                    >>>
                    >>> # get default state (default state is set)
                    >>> prims.get_default_state()
                    (array(shape=(3, 3), dtype=float32),
                     array(shape=(3, 4), dtype=float32),
                     array(shape=(3, 3), dtype=float32),
                     array(shape=(3, 3), dtype=float32),
                     array(shape=(3, 9), dtype=float32),
                     array(shape=(3, 9), dtype=float32),
                     array(shape=(3, 9), dtype=float32))
                    >>>
                    >>> # reset prims to default state
                    >>> prims.reset_to_default_state()
                
        """
    def set_default_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, linear_velocities: list | np.ndarray | wp.array | None = None, angular_velocities: list | np.ndarray | wp.array | None = None, dof_positions: list | np.ndarray | wp.array | None = None, dof_velocities: list | np.ndarray | wp.array | None = None, dof_efforts: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the default state (root positions, orientations, linear velocities and angular velocities,
                and DOF positions, velocities and efforts) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. hint::
        
                    Prims can be reset to their default state by calling the :py:meth:`reset_to_default_state` method.
        
                Args:
                    positions: Default root positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Default root orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    linear_velocities: Default root linear velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    angular_velocities: Default root angular velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dof_positions: Default DOF positions (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dof_velocities: Default DOF velocities (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dof_efforts: Default DOF efforts (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                
        """
    def set_dof_armatures(self, armatures: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the armatures of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Search for *Armature* in |physx_docs| for more details.
        
                Args:
                    armatures: Armatures (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF armatures for all prims
                    >>> prims.set_dof_armatures([0.5])
                    >>>
                    >>> # set the armatures for the first and last prims' finger DOFs
                    >>> prims.set_dof_armatures([1.5], indices=[0, 2], dof_indices=[7, 8])
                
        """
    def set_dof_drive_model_properties(self, speed_effort_gradients: list | np.ndarray | wp.array | None = None, maximum_actuator_velocities: list | np.ndarray | wp.array | None = None, velocity_dependent_resistances: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the drive model properties of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    speed_effort_gradients: Speed effort gradients (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    maximum_actuator_velocities: Maximum actuator velocities (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    velocity_dependent_resistances: Velocity-dependent resistances (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: If neither speed_effort_gradients, maximum_actuator_velocities,
                        or velocity_dependent_resistances are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF drive model properties for all prims
                    >>> prims.set_dof_drive_model_properties(
                    ...     speed_effort_gradients=[2.0],
                    ...     maximum_actuator_velocities=[1.0],
                    ...     velocity_dependent_resistances=[1.5],
                    ... )
                
        """
    def set_dof_drive_types(self, types: str | list[list[str]], *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the drive types of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    types: Drive types. Can be a single string or list of strings (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF drive types for all prims to 'acceleration'
                    >>> # note that dof indices 8 is a mimic joint, it does not have a DOF drive
                    >>> prims.set_dof_drive_types("acceleration", dof_indices=[0, 1, 2, 3, 4, 5, 6, 7])
                    >>>
                    >>> # set the drive types for the all prims' finger DOFs to 'force'
                    >>> prims.set_dof_drive_types("force", dof_indices=[7])
                
        """
    def set_dof_efforts(self, efforts: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the efforts of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                .. note::
        
                    For effort control, this method must be used.
                    In contrast to the methods that set a target for DOF position/velocity,
                    this method must be called at every update step to ensure effort control.
        
                .. hint::
        
                    For effort control, set zero stiffness and damping, or remove DOF's drive.
        
                Args:
                    efforts: Efforts (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random DOF efforts for all prims
                    >>> prims.set_dof_efforts(np.random.randn(3, 9))
                    >>>
                    >>> # set random efforts for the first and last prims' finger DOFs
                    >>> prims.set_dof_efforts(np.random.randn(2, 2), indices=[0, 2], dof_indices=[7, 8])
                
        """
    def set_dof_friction_properties(self, static_frictions: list | np.ndarray | wp.array | None = None, dynamic_frictions: list | np.ndarray | wp.array | None = None, viscous_frictions: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the friction properties of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                .. warning::
        
                    The ``static_frictions`` must be greater than or equal to the ``dynamic_frictions``.
        
                Args:
                    static_frictions: Static friction efforts (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dynamic_frictions: Dynamic friction efforts (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    viscous_frictions: Viscous friction coefficients (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: If neither static_frictions, dynamic_frictions, or viscous_frictions are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF friction properties for all prims
                    >>> prims.set_dof_friction_properties(static_frictions=[0.5], dynamic_frictions=[0.2], viscous_frictions=[0.1])
                
        """
    def set_dof_gains(self, stiffnesses: list | np.ndarray | wp.array | None = None, dampings: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None, update_default_gains: bool = True) -> None:
        """
        Set the implicit Proportional-Derivative (PD) controller's gains (stiffnesses and dampings)
                of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    stiffnesses: Stiffnesses (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dampings: Dampings (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
                    update_default_gains: Whether to update the default gains with the given values.
        
                Raises:
                    AssertionError: If neither stiffnesses nor dampings are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF gains for all prims
                    >>> stiffnesses = np.array([100000, 100000, 100000, 100000, 80000, 80000, 80000, 50000, 50000])
                    >>> dampings = np.array([8000, 8000, 8000, 8000, 5000, 5000, 5000, 2000, 2000])
                    >>> prims.set_dof_gains(stiffnesses, dampings)
                
        """
    def set_dof_limits(self, lower: list | np.ndarray | wp.array | None = None, upper: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the limits of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    lower: Lower limits (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    upper: Upper limits (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: If neither lower nor upper limits are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the DOF lower limits for all prims to -0.25
                    >>> prims.set_dof_limits(lower=[-0.25])
                
        """
    def set_dof_max_efforts(self, max_efforts: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the maximum forces applied by the drive of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    max_efforts: Maximum forces (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the maximum DOF efforts for all prims to 1000
                    >>> prims.set_dof_max_efforts([1000])
                
        """
    def set_dof_max_velocities(self, max_velocities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the maximum velocities of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    max_velocities: Maximum velocities (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the maximum DOF velocities for all prims to 100
                    >>> prims.set_dof_max_velocities([100])
                
        """
    def set_dof_position_targets(self, positions: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the position targets of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                .. note::
        
                    This method set the desired target position for the DOFs, not the instantaneous positions.
                    It may take several simulation steps to reach the target position
                    (depending on the DOFs' stiffness and damping values).
        
                .. hint::
        
                    High stiffness causes the DOF to move faster and harder towards the desired target,
                    while high damping softens but also slows the DOF's movement towards the target.
        
                    * For position control, set relatively high stiffness and non-zero low damping (to reduce vibrations).
        
                Args:
                    positions: Position targets (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random DOF position targets for all prims
                    >>> prims.set_dof_position_targets(np.random.uniform(low=-0.25, high=0.25, size=(3, 9)))
                    >>>
                    >>> # open all the Franka Panda fingers (finger DOFs to 0.04)
                    >>> prims.set_dof_position_targets([0.04], dof_indices=[7, 8])
                
        """
    def set_dof_positions(self, positions: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the positions of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                .. warning::
        
                    This method *teleports* prims to the specified DOF positions.
                    Use the :py:meth:`set_dof_position_targets` method to control the DOFs' positions.
        
                Args:
                    positions: Positions (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random DOF positions for all prims
                    >>> prims.set_dof_positions(np.random.uniform(low=-0.25, high=0.25, size=(3, 9)))
                    >>>
                    >>> # set all the Franka Panda fingers to closed position immediately (finger DOFs to 0.0)
                    >>> prims.set_dof_positions([0.0], dof_indices=[7, 8])
                
        """
    def set_dof_velocities(self, velocities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the velocities of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                .. warning::
        
                    This method set the specified DOF velocities immediately.
                    Use the :py:meth:`set_dof_velocity_targets` method to control the DOFs' velocities.
        
                Args:
                    velocities: Velocities (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random DOF velocities for all prims
                    >>> prims.set_dof_velocities(np.random.uniform(low=-10, high=10, size=(3, 9)))
                
        """
    def set_dof_velocity_targets(self, velocities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the velocity targets of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                .. note::
        
                    This method set the desired target velocity for the DOFs, not the instantaneous velocities.
                    It may take several simulation steps to reach the target velocity
                    (depending on the DOFs' stiffness and damping values).
        
                .. hint::
        
                    High stiffness causes the DOF to move faster and harder towards the desired target,
                    while high damping softens but also slows the DOF's movement towards the target.
        
                    * For velocity control, set zero stiffness and non-zero damping.
        
                Args:
                    velocities: Velocity targets (shape ``(N, D)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random DOF velocity targets for all prims
                    >>> prims.set_dof_velocity_targets(np.random.uniform(low=-10, high=10, size=(3, 9)))
                
        """
    def set_enabled_self_collisions(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the self-collisions processing of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    enabled: Boolean flags to enable/disable self-collisions (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # disable the self-collisions for all prims
                    >>> prims.set_enabled_self_collisions([False])
                
        """
    def set_fixed_tendon_properties(self, *, stiffnesses: list | np.ndarray | wp.array | None = None, dampings: list | np.ndarray | wp.array | None = None, limit_stiffnesses: list | np.ndarray | wp.array | None = None, lower_limits: list | np.ndarray | wp.array | None = None, upper_limits: list | np.ndarray | wp.array | None = None, rest_lengths: list | np.ndarray | wp.array | None = None, offsets: list | np.ndarray | wp.array | None = None, indices: list | np.ndarray | wp.array | None = None, tendon_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the fixed tendon properties of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Search for *Fixed Tendons* in |physx_docs| for more details.
        
                Args:
                    stiffnesses: The stiffnesses (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    dampings: The dampings (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    limit_stiffnesses: The limit stiffnesses (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    lower_limits: The lower limits (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    upper_limits: The upper limits (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    rest_lengths: The rest lengths (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    offsets: The offsets (shape ``(N, T)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    tendon_indices: Indices of tendons to process (shape ``(T,)``). If not defined, all tendons are processed.
        
                Raises:
                    AssertionError: None of the fixed tendon properties are defined.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
                
        """
    def set_link_coms(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the center of mass (COM) pose (position and orientation) of the links of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    positions: Center of mass positions (shape ``(N, L, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Center of mass orientations (shape ``(N, L, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random COM link positions for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 11, 3))
                    >>> prims.set_link_coms(positions)
                
        """
    def set_link_enabled_gravities(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the enabled state of the gravity on the links of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    enabled: Boolean flags to enable/disable gravity on the links (shape ``(N, L)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the gravity of the links for all prims
                    >>> prims.set_link_enabled_gravities([True])
                    >>>
                    >>> # disable the gravity for the first and last prims' finger links
                    >>> prims.set_link_enabled_gravities([False], indices=[0, 2], link_indices=[9, 10])
                
        """
    def set_link_inertias(self, inertias: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the inertias of the links of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    inertias: The link inertias (shape ``(N, L, 9)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the inertia tensors of the links for all prims
                    >>> inertias = np.diag([0.1, 0.1, 0.1]).flatten()  # shape: (9,)
                    >>> prims.set_link_inertias(inertias)
                    >>>
                    >>> # set the inertia tensors for the first and last prims' finger links
                    >>> inertias = np.diag([0.2, 0.2, 0.2]).flatten()  # shape: (9,)
                    >>> prims.set_link_inertias(inertias, indices=[0, 2], link_indices=[9, 10])
                
        """
    def set_link_masses(self, masses: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, link_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the masses of the links of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                Args:
                    masses: The link masses (shape ``(N, L)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    link_indices: Indices of links to process (shape ``(L,)``). If not defined, all links are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the masses of the links for all prims
                    >>> prims.set_link_masses([10.0])
                    >>>
                    >>> # set the masses for the first and last prims' finger links
                    >>> prims.set_link_masses([0.5], indices=[0, 2], link_indices=[9, 10])
                
        """
    def set_local_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the root poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    translations: Root translations in the local frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Root orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither translations nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set poses (fixed translations and random orientations) for all prims
                    >>> translations = [[0, y, 0] for y in range(3)]
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_local_poses(translations, orientations)
                
        """
    def set_sleep_thresholds(self, thresholds: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the sleep thresholds of the prims.
        
                Backends: :guilabel:`usd`.
        
                Search for *Articulations and Sleeping* in |physx_docs| for more details.
        
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
    def set_solver_iteration_counts(self, position_counts: list | np.ndarray | wp.array | None = None, velocity_counts: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the physics solver iteration counts (position and velocity) of the prims.
        
                Backends: :guilabel:`usd`.
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                .. warning::
        
                    The more iterations, the more accurate the results, at the cost of decreasing simulation performance.
        
                Args:
                    position_counts: Number of iterations for the position solver (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    velocity_counts: Number of iterations for the velocity solver (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Neither ``position_counts`` nor ``velocity_counts`` are defined.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the solver iteration counts (position: 16, velocity: 4) for all prims
                    >>> prims.set_solver_iteration_counts([16], [4])
                
        """
    def set_stabilization_thresholds(self, thresholds: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the mass-normalized kinetic energy below which the prims may participate in stabilization.
        
                Backends: :guilabel:`usd`.
        
                Search for *Stabilization Threshold* in |physx_docs| for more details.
        
                Args:
                    thresholds: Stabilization thresholds to be applied (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the stabilization thresholds for all prims
                    >>> prims.set_stabilization_thresholds([1e-5])
                    >>>
                    >>> # set the stabilization thresholds for the first and last prims
                    >>> prims.set_stabilization_thresholds([1.5e-5], indices=[0, 2])
                
        """
    def set_velocities(self, linear_velocities: list | np.ndarray | wp.array | None = None, angular_velocities: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the root velocities (linear and angular) of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Args:
                    linear_velocities: Root linear velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    angular_velocities: Root angular velocities (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither linear_velocities nor angular_velocities are specified.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random velocities for all prims
                    >>> linear_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> angular_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> prims.set_velocities(linear_velocities, angular_velocities)
                
        """
    def set_world_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the root poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    positions: Root positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Root orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set poses (fixed positions and random orientations) for all prims
                    >>> positions = [[0, y, 0] for y in range(3)]
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_world_poses(positions, orientations)
                
        """
    def switch_dof_control_mode(self, mode: str, *, indices: list | np.ndarray | wp.array | None = None, dof_indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Switch the control mode (understood as the gain adjustment) of the degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`tensor`, :guilabel:`usd`.
        
                This method sets the implicit Proportional-Derivative (PD) controller's gains (stiffnesses and dampings)
                according to the following rules:
        
                .. list-table::
                    :header-rows: 1
        
                    * - Control mode
                      - Stiffnesses
                      - Dampings
                    * - ``"position"``
                      - default stiffnesses
                      - default dampings
                    * - ``"velocity"``
                      - 0.0
                      - default dampings
                    * - ``"effort"``
                      - 0.0
                      - 0.0
        
                Args:
                    mode: Control mode. Supported modes are ``"position"``, ``"velocity"`` and ``"effort"``.
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    dof_indices: Indices of DOFs to process (shape ``(D,)``). If not defined, all DOFs are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    ValueError: Invalid control mode.
        
                Example:
        
                .. code-block:: python
        
                    >>> # switch to 'velocity' control mode for all prims' arm DOFs (except for the fingers)
                    >>> prims.switch_dof_control_mode("velocity", dof_indices=np.arange(7))
                    >>>
                    >>> # switch to 'effort' control mode for all prims' fingers (last 2 DOFs)
                    >>> prims.switch_dof_control_mode("effort", dof_indices=[7, 8])
                
        """
    @property
    def dof_names(self) -> list[str]:
        """
        Degree of freedom (DOFs) names of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of DOF names.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.dof_names
                    ['panda_joint1', 'panda_joint2', 'panda_joint3',
                     'panda_joint4', 'panda_joint5', 'panda_joint6',
                     'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
                
        """
    @property
    def dof_paths(self) -> list[list[str]]:
        """
        Degree of freedom (DOFs) paths of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of DOF names.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.dof_paths
                    [['/World/prim_0/panda_link0/panda_joint1', '/World/prim_0/panda_link1/panda_joint2', '/World/prim_0/panda_link2/panda_joint3',
                      '/World/prim_0/panda_link3/panda_joint4', '/World/prim_0/panda_link4/panda_joint5', '/World/prim_0/panda_link5/panda_joint6',
                      '/World/prim_0/panda_link6/panda_joint7', '/World/prim_0/panda_hand/panda_finger_joint1', '/World/prim_0/panda_hand/panda_finger_joint2'],
                     ['/World/prim_1/panda_link0/panda_joint1', '/World/prim_1/panda_link1/panda_joint2', '/World/prim_1/panda_link2/panda_joint3',
                      '/World/prim_1/panda_link3/panda_joint4', '/World/prim_1/panda_link4/panda_joint5', '/World/prim_1/panda_link5/panda_joint6',
                      '/World/prim_1/panda_link6/panda_joint7', '/World/prim_1/panda_hand/panda_finger_joint1', '/World/prim_1/panda_hand/panda_finger_joint2'],
                     ['/World/prim_2/panda_link0/panda_joint1', '/World/prim_2/panda_link1/panda_joint2', '/World/prim_2/panda_link2/panda_joint3',
                      '/World/prim_2/panda_link3/panda_joint4', '/World/prim_2/panda_link4/panda_joint5', '/World/prim_2/panda_link5/panda_joint6',
                      '/World/prim_2/panda_link6/panda_joint7', '/World/prim_2/panda_hand/panda_finger_joint1', '/World/prim_2/panda_hand/panda_finger_joint2']]
                
        """
    @property
    def dof_types(self) -> list[omni.physics.tensors.DofType]:
        """
        Degree of freedom (DOFs) types of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of DOF types.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.dof_types
                    [<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
                     <DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
                     <DofType.Rotation: 0>, <DofType.Translation: 1>, <DofType.Translation: 1>]
                
        """
    @property
    def jacobian_matrix_shape(self) -> tuple[int, int, int]:
        """
        Jacobian matrix shape.
        
                Backends: :guilabel:`tensor`.
        
                The Jacobian matrix shape depends on the number of links, DOFs, and whether the articulation base is fixed
                (e.g.: robotic manipulators) or not (e.g.: mobile robots).
        
                * Fixed articulation base: ``(num_links - 1, 6, num_dofs)``
                * Non-fixed (floating) articulation base: ``(num_links, 6, num_dofs + 6)``
        
                Each link has 6 values in the Jacobian representing its linear and angular motion along the
                three coordinate axes. The extra 6 DOFs in the last dimension, for floating bases,
                correspond to the linear and angular degrees of freedom of the free root link.
        
                Returns:
                    Shape of Jacobian matrix (for one prim).
        
                Raises:
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # for the Franka Panda (a robotic manipulator with fixed base):
                    >>> # - num_links: 11
                    >>> # - num_dofs: 9
                    >>> prims.jacobian_matrix_shape
                    (10, 6, 9)
                
        """
    @property
    def joint_names(self) -> list[str]:
        """
        Joint names of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of joint names.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.joint_names
                    ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4',
                     'panda_joint5', 'panda_joint6', 'panda_joint7',
                     'panda_hand_joint', 'panda_finger_joint1', 'panda_finger_joint2']
                
        """
    @property
    def joint_paths(self) -> list[list[str]]:
        """
        Joint paths of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of joint paths.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.joint_paths
                    [['/World/prim_0/panda_link0/panda_joint1', '/World/prim_0/panda_link1/panda_joint2', '/World/prim_0/panda_link2/panda_joint3',
                      '/World/prim_0/panda_link3/panda_joint4', '/World/prim_0/panda_link4/panda_joint5', '/World/prim_0/panda_link5/panda_joint6',
                      '/World/prim_0/panda_link6/panda_joint7', '/World/prim_0/panda_link7/panda_hand_joint',
                      '/World/prim_0/panda_hand/panda_finger_joint1', '/World/prim_0/panda_hand/panda_finger_joint2'],
                     ['/World/prim_1/panda_link0/panda_joint1', '/World/prim_1/panda_link1/panda_joint2', '/World/prim_1/panda_link2/panda_joint3',
                      '/World/prim_1/panda_link3/panda_joint4', '/World/prim_1/panda_link4/panda_joint5', '/World/prim_1/panda_link5/panda_joint6',
                      '/World/prim_1/panda_link6/panda_joint7', '/World/prim_1/panda_link7/panda_hand_joint',
                      '/World/prim_1/panda_hand/panda_finger_joint1', '/World/prim_1/panda_hand/panda_finger_joint2'],
                     ['/World/prim_2/panda_link0/panda_joint1', '/World/prim_2/panda_link1/panda_joint2', '/World/prim_2/panda_link2/panda_joint3',
                      '/World/prim_2/panda_link3/panda_joint4', '/World/prim_2/panda_link4/panda_joint5', '/World/prim_2/panda_link5/panda_joint6',
                      '/World/prim_2/panda_link6/panda_joint7', '/World/prim_2/panda_link7/panda_hand_joint',
                      '/World/prim_2/panda_hand/panda_finger_joint1', '/World/prim_2/panda_hand/panda_finger_joint2']]
                
        """
    @property
    def joint_types(self) -> list[omni.physics.tensors.JointType]:
        """
        Joint types of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Returns:
                    Ordered list of joint types.
        
                Raises:
                    AssertionError: Physics tensor entity is not initialized.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.joint_types
                    [<JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>,
                     <JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>,
                     <JointType.Fixed: 0>, <JointType.Prismatic: 2>, <JointType.Prismatic: 2>]
                
        """
    @property
    def link_names(self) -> list[str]:
        """
        Link names of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of link names.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.link_names
                    ['panda_link0', 'panda_link1', 'panda_link2', 'panda_link3',
                     'panda_link4', 'panda_link5', 'panda_link6', 'panda_link7',
                     'panda_hand', 'panda_leftfinger', 'panda_rightfinger']
                
        """
    @property
    def link_paths(self) -> list[list[str]]:
        """
        Link paths of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Ordered list of link paths.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.link_paths
                    [['/World/prim_0/panda_link0', '/World/prim_0/panda_link1', '/World/prim_0/panda_link2', '/World/prim_0/panda_link3',
                      '/World/prim_0/panda_link4', '/World/prim_0/panda_link5', '/World/prim_0/panda_link6', '/World/prim_0/panda_link7',
                      '/World/prim_0/panda_hand', '/World/prim_0/panda_leftfinger', '/World/prim_0/panda_rightfinger'],
                     ['/World/prim_1/panda_link0', '/World/prim_1/panda_link1', '/World/prim_1/panda_link2', '/World/prim_1/panda_link3',
                      '/World/prim_1/panda_link4', '/World/prim_1/panda_link5', '/World/prim_1/panda_link6', '/World/prim_1/panda_link7',
                      '/World/prim_1/panda_hand', '/World/prim_1/panda_leftfinger', '/World/prim_1/panda_rightfinger'],
                     ['/World/prim_2/panda_link0', '/World/prim_2/panda_link1', '/World/prim_2/panda_link2', '/World/prim_2/panda_link3',
                      '/World/prim_2/panda_link4', '/World/prim_2/panda_link5', '/World/prim_2/panda_link6', '/World/prim_2/panda_link7',
                      '/World/prim_2/panda_hand', '/World/prim_2/panda_leftfinger', '/World/prim_2/panda_rightfinger']]
                
        """
    @property
    def mass_matrix_shape(self) -> tuple[int, int]:
        """
        Mass matrix shape.
        
                Backends: :guilabel:`tensor`.
        
                The mass matrix shape depends on the number of DOFs, and whether the articulation base is fixed
                (e.g.: robotic manipulators) or not (e.g.: mobile robots).
        
                * Fixed articulation base: ``(num_dofs, num_dofs)``
                * Non-fixed (floating) articulation base: ``(num_dofs + 6, num_dofs + 6)``
        
                Returns:
                    Shape of mass matrix (for one prim).
        
                Raises:
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # for the Franka Panda:
                    >>> # - num_dofs: 9
                    >>> prims.mass_matrix_shape
                    (9, 9)
                
        """
    @property
    def num_dofs(self) -> int:
        """
        Number of degrees of freedom (DOFs) of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Number of DOFs.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_dofs
                    9
                
        """
    @property
    def num_fixed_tendons(self) -> int:
        """
        Number of fixed tendons of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Returns:
                    Number of fixed tendons.
        
                Raises:
                    AssertionError: Physics tensor entity is not initialized.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_fixed_tendons
                    0
                
        """
    @property
    def num_joints(self) -> int:
        """
        Number of joints of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Number of joints.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_joints
                    10
                
        """
    @property
    def num_links(self) -> int:
        """
        Number of links of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`.
        
                Returns:
                    Number of links.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_links
                    11
                
        """
    @property
    def num_shapes(self) -> int:
        """
        Number of rigid shapes of the prims.
        
                Backends: :guilabel:`tensor`.
        
                Returns:
                    Number of rigid shapes.
        
                Raises:
                    AssertionError: Physics tensor entity is not initialized.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_shapes
                    13
                
        """
_MSG_PHYSICS_TENSOR_ENTITY_NOT_INITIALIZED: str = "Instance's physics tensor entity is not initialized. Play the simulation/timeline to initialize it"
_MSG_PHYSICS_TENSOR_ENTITY_NOT_VALID: str = "Instance's physics tensor entity is not valid. Play the simulation/timeline to re-initialize it"
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
