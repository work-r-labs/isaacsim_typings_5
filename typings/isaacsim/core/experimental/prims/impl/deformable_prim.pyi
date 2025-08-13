from __future__ import annotations
import carb as carb
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import backend as backend_utils
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import prim as prim_utils
from isaacsim.core.experimental.utils import stage as stage_utils
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
import numpy as np
import omni as omni
from omni.physx.bindings import _physx as physx_bindings
from omni.physx import get_physx_cooking_interface
from omni.physx.scripts import deformableUtils
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
import typing
import warp as wp
import weakref as weakref
__all__: list[str] = ['DeformablePrim', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdShade', 'XformPrim', 'backend_utils', 'carb', 'deformableUtils', 'get_physx_cooking_interface', 'np', 'omni', 'ops_utils', 'physx_bindings', 'prim_utils', 'stage_utils', 'weakref', 'wp']
class DeformablePrim(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    High level wrapper for manipulating prims (that have Deformable Schema applied) and their attributes.
    
        .. warning::
    
            The deformable prims require the Deformable feature (beta) to be enabled.
            Deformable feature (beta) can be enabled in *apps/.kit* experience files by setting
            ``physics.enableDeformableBeta = true`` under the ``[settings.persistent]`` section.
    
        .. warning::
    
            The current ``omni.physics.tensors`` implementation does not support ``list[str]``
            as input for deformable body paths. This limitation will be fixed in the future releases.
            An error message will be logged if a list of paths is provided.
    
        This class is a wrapper over one or more USD prims in the stage to provide
        high-level functionality for manipulating deformable body properties, and other attributes.
        The prims are specified using paths that can include regular expressions for matching multiple prims.
    
        .. note::
    
            If the prims do not already have the Deformable Schema applied to them, it will be applied.
    
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
            deformable_type: Type of deformable body.
                If not defined, the type will be inferred from the prims.
    
        Raises:
            RuntimeError: If the Deformable feature (beta) is disabled.
            ValueError: If no prims are found matching the specified path(s).
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> import omni.timeline
            >>> from isaacsim.core.experimental.prims import DeformablePrim
            >>>
            >>> # given a USD stage with the tetrahedral mesh prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # - create wrapper over single prim (volume deformable body)
            >>> prim = DeformablePrim("/World/prim_0", deformable_type="volume")  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex (volume deformable body)
            >>> prims = DeformablePrim("/World/prim_.*", deformable_type="volume")  # doctest: +NO_CHECK
            >>>
            >>> # play the simulation so that the Physics tensor entity becomes valid
            >>> omni.timeline.get_timeline_interface().play()
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = False, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False, deformable_type: typing.Literal['surface', 'volume'] | None = None) -> None:
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
    def _query_deformable_properties(self) -> None:
        """
        Query deformable properties.
        """
    def apply_physics_materials(self, materials: type['PhysicsMaterial'] | list[type['PhysicsMaterial']], *, weaker_than_descendants: list | np.ndarray | wp.array | None = None, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Apply physics materials to the prims, and optionally, to their descendants.
        
                Backends: :guilabel:`usd`.
        
                Physics materials define properties like friction and restitution that affect how objects interact during collisions.
                If no physics material is defined, default values from Physics will be used.
        
                Args:
                    materials: Physics materials to be applied to the prims (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    weaker_than_descendants: Boolean flags to indicate whether descendant materials should be overridden (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.experimental.materials import VolumeDeformableMaterial
                    >>>
                    >>> # create a volume deformable physics material
                    >>> material = VolumeDeformableMaterial(
                    ...     "/World/physics_material/deformable_material",
                    ...     static_frictions=[1.1],
                    ...     dynamic_frictions=[0.4],
                    ...     poissons_ratios=[0.1],
                    ...     youngs_moduli=[1000000.0],
                    ... )
                    >>>
                    >>> # apply the material to all prims
                    >>> prims.apply_physics_materials(material)  # or [material]  # doctest: +SKIP
                
        """
    def get_applied_physics_materials(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[type['PhysicsMaterial'] | None]:
        """
        Get the applied physics materials.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    List of applied physics materials (shape ``(N,)``). If a prim does not have a material, ``None`` is returned.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the applied material path of the first prim
                    >>> physics_material = prims.get_applied_physics_materials(indices=[0])[0]
                    >>> physics_material.paths[0]  # doctest: +SKIP
                    '/World/physics_material/deformable_material'
                
        """
    def get_element_indices(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array, wp.array]:
        """
        Get the element (triangular faces for surface, tetrahedrons for volume) indices
                of the simulation, collision and rest meshes of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Three-elements tuple.
                    1) The simulation mesh's element indices (shape ``(N, num_elements_per_body, num_nodes_per_element)``).
                    2) The collision mesh's element indices (shape ``(N, num_elements_per_body, num_nodes_per_element)``).
                    3) The rest mesh's element indices (shape ``(N, num_elements_per_body, num_nodes_per_element)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_indices, collision_indices, rest_indices = prims.get_element_indices()
                    >>> print(simulation_indices)
                    [[[0 1 2 3]]
                     [[0 1 2 3]]
                     [[0 1 2 3]]]
                    >>> print(collision_indices)
                    [[[0 1 2 3]]
                     [[0 1 2 3]]
                     [[0 1 2 3]]]
                    >>> print(rest_indices)
                    [[[0 1 2 3]]
                     [[0 1 2 3]]
                     [[0 1 2 3]]]
                
        """
    def get_nodal_kinematic_position_targets(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the nodal (mesh points) kinematic position targets of the simulation mesh of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`volume`.
        
                .. note::
        
                    This method is only supported for volume deformable bodies.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple.
                    1) The simulation mesh's nodal kinematic position targets (shape ``(N, num_nodes_per_body, 3)``).
                    2) Boolean flags indicating whether the kinematic (true) or dynamic (false) control
                    is enabled (shape ``(N, num_nodes_per_body, 1)``).
        
                Raises:
                    AssertionError: When the deformable body is not a volume.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the nodal kinematic position targets of all prims
                    >>> positions, enabled = prims.get_nodal_kinematic_position_targets()
                    >>> positions.shape, enabled.shape
                    ((3, 4, 3), (3, 4, 1))
                    >>>
                    >>> # get the nodal kinematic position targets of the first and last prims
                    >>> positions, enabled = prims.get_nodal_kinematic_position_targets(indices=[0, 2])
                    >>> positions.shape, enabled.shape
                    ((2, 4, 3), (2, 4, 1))
                
        """
    def get_nodal_positions(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array, wp.array]:
        """
        Get the nodal (mesh points) positions of the simulation, collision and rest meshes of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Three-elements tuple.
                    1) The simulation mesh's nodal positions (shape ``(N, num_nodes_per_body, 3)``).
                    2) The collision mesh's nodal positions (shape ``(N, num_nodes_per_body, 3)``).
                    3) The rest mesh's nodal positions (shape ``(N, num_nodes_per_body, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the nodal positions of all prims
                    >>> simulation_positions, collision_positions, rest_positions = prims.get_nodal_positions()
                    >>> simulation_positions.shape, collision_positions.shape, rest_positions.shape
                    ((3, 4, 3), (3, 4, 3), (3, 4, 3))
                    >>>
                    >>> # get the nodal positions of the first and last prims
                    >>> simulation_positions, collision_positions, rest_positions = prims.get_nodal_positions(indices=[0, 2])
                    >>> simulation_positions.shape, collision_positions.shape, rest_positions.shape
                    ((2, 4, 3), (2, 4, 3), (2, 4, 3))
                
        """
    def get_nodal_velocities(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the nodal (mesh points) velocities of the simulation mesh of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    The simulation mesh's nodal velocities (shape ``(N, num_nodes_per_body, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the nodal velocities of all prims
                    >>> simulation_velocities = prims.get_nodal_velocities()
                    >>> simulation_velocities.shape
                    (3, 4, 3)
                    >>>
                    >>> # get the nodal velocities of the first and last prims
                    >>> simulation_velocities = prims.get_nodal_velocities(indices=[0, 2])
                    >>> simulation_velocities.shape
                    (2, 4, 3)
                
        """
    def is_physics_tensor_entity_valid(self) -> bool:
        """
        Check if the physics tensor entity is valid.
        
                Returns:
                    Whether the physics tensor entity is valid.
                
        """
    def set_nodal_kinematic_position_targets(self, positions: list | np.ndarray | wp.array | None = None, enabled: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the nodal (mesh points) kinematic position targets of the simulation mesh of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`volume`.
        
                .. note::
        
                    This method is only supported for volume deformable bodies.
        
                Args:
                    positions: Nodal positions (shape ``(N, num_nodes_per_body, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    enabled: Boolean flags to enable the kinematic (true) or dynamic (false) control (shape ``(N, num_nodes_per_body, 1)``).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: When the deformable body is not a volume.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random nodal kinematic position targets for the first and last prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(2, 4, 3))
                    >>> prims.set_nodal_kinematic_position_targets(positions, enabled=[True], indices=[0, 2])
                
        """
    def set_nodal_positions(self, positions: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the nodal (mesh points) positions of the simulation mesh of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Args:
                    positions: Nodal positions (shape ``(N, num_nodes_per_body, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random nodal positions for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 4, 3))
                    >>> prims.set_nodal_positions(positions)
                
        """
    def set_nodal_velocities(self, velocities: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the nodal (mesh points) velocities of the simulation mesh of the prims.
        
                Backends: :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Args:
                    velocities: Nodal velocities (shape ``(N, num_nodes_per_body, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: Physics tensor entity is not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random nodal velocities for all prims
                    >>> velocities = np.random.uniform(low=-1, high=1, size=(3, 4, 3))
                    >>> prims.set_nodal_velocities(velocities)
                
        """
    @property
    def collision_mesh_paths(self) -> list[str]:
        """
        Collision mesh paths of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Returns:
                    Ordered list of collision mesh paths.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.collision_mesh_paths
                    ['/World/prim_0', '/World/prim_1', '/World/prim_2']
                
        """
    @property
    def deformable_type(self) -> typing.Literal['surface', 'volume']:
        """
        Type of deformable body.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Returns:
                    Type of deformable body.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.deformable_type
                    'volume'
                
        """
    @property
    def num_elements_per_body(self) -> tuple[int, int, int]:
        """
        Number of elements (triangular faces for surface, tetrahedrons for volume) per body (mesh prim).
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                .. note::
        
                    In the current implementation, the rest mesh is limited to the same topology as the simulation mesh.
                    This means that the number of elements per body is the same for the simulation and rest meshes.
        
                Returns:
                    Tuple of three elements. 1) Number of elements per body (simulation mesh).
                    2) Number of elements per body (collision mesh).
                    3) Number of elements per body (rest mesh).
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_elements_per_body
                    (1, 1, 1)
                
        """
    @property
    def num_nodes_per_body(self) -> tuple[int, int, int]:
        """
        Number of nodes (mesh points) per body (mesh prim).
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Returns:
                    Tuple of three elements. 1) Number of nodes per body (simulation mesh).
                    2) Number of nodes per body (collision mesh).
                    3) Number of nodes per body (rest mesh).
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_nodes_per_body
                    (4, 4, 4)
                
        """
    @property
    def num_nodes_per_element(self) -> int:
        """
        Number of nodes (mesh points) per element (triangular face for surface, tetrahedron for volume).
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                The number of nodes per element is 3 (triangle) for surface and 4 (tetrahedron) for volume.
        
                Returns:
                    Number of nodes per element.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_nodes_per_element
                    4
                
        """
    @property
    def simulation_mesh_paths(self) -> list[str]:
        """
        Simulation mesh paths of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`tensor`. |br|
                Deformable type: :guilabel:`surface`, :guilabel:`volume`.
        
                Returns:
                    Ordered list of simulation mesh paths.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.simulation_mesh_paths
                    ['/World/prim_0', '/World/prim_1', '/World/prim_2']
                
        """
def _check_or_apply_deformable_schema(stage: Usd.Stage, path: str, deformable_type: typing.Literal['surface', 'volume'] | None) -> tuple[typing.Literal['wrap', 'create'], typing.Literal['surface', 'volume']]:
    ...
_MSG_PHYSICS_TENSOR_ENTITY_NOT_VALID: str = "Instance's physics tensor entity is not valid. Play the simulation/timeline to re-initialize it"
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
