from __future__ import annotations
import carb as carb
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import ops as ops_utils
import numpy as np
from pxr import PhysxSchema
from pxr import UsdGeom
from pxr import UsdPhysics
from pxr import UsdShade
import typing
import warp as wp
__all__: list[str] = ['GeomPrim', 'PhysxSchema', 'UsdGeom', 'UsdPhysics', 'UsdShade', 'XformPrim', 'carb', 'np', 'ops_utils', 'wp']
class GeomPrim(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    High level wrapper for manipulating geometric prims and their attributes.
    
        This class is a wrapper over one or more USD geometric prims in the stage to provide
        high-level functionality for manipulating collision properties, and other attributes.
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
            apply_collision_apis: Whether to apply collision APIs to the prims during initialization.
    
        Raises:
            ValueError: If no prims are found matching the specified path(s).
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> from isaacsim.core.experimental.prims import GeomPrim
            >>>
            >>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # - create wrapper over single prim (with collision APIs enabled)
            >>> prim = GeomPrim("/World/prim_0", apply_collision_apis=True)  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex (with collision APIs enabled)
            >>> prims = GeomPrim("/World/prim_.*", apply_collision_apis=True)  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False, apply_collision_apis: bool = False) -> None:
        ...
    def apply_collision_apis(self, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Apply collision APIs to enable collision detection for prims.
        
                Backends: :guilabel:`usd`.
        
                This method applies the following APIs to enable collision detection:
        
                - USD: ``UsdPhysics.CollisionAPI`` and ``UsdPhysics.MeshCollisionAPI``
                - PhysX: ``PhysxSchema.PhysxCollisionAPI``
        
                .. note::
        
                    If a prim in the parent hierarchy has the ``RigidBodyAPI`` applied, the collider is a part of that body.
                    If there is no body in the parent hierarchy, the collider is considered to be static.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Example:
        
                .. code-block:: python
        
                    >>> # apply the collision API to all prims
                    >>> prims.apply_collision_apis()
                
        """
    def apply_physics_materials(self, materials: type['PhysicsMaterial'] | list[type['PhysicsMaterial']], *, weaker_than_descendants: list | np.ndarray | wp.array | None = None, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Apply physics materials to the prims, and optionally, to their descendants.
        
                Backends: :guilabel:`usd`.
        
                Physics materials define properties like friction and restitution that affect how objects interact during collisions.
                If no physics material is defined, default values from Physics will be used.
        
                Args:
                    materials: Physics materials to be applied to the prims (shape ``(N)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    weaker_than_descendants: Boolean flags to indicate whether descendant materials should be overridden (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.experimental.materials import RigidBodyMaterial
                    >>>
                    >>> # create a rigid body physics material
                    >>> material = RigidBodyMaterial(
                    ...     "/World/physics_material/aluminum",
                    ...     static_frictions=[1.1],
                    ...     dynamic_frictions=[0.4],
                    ...     restitutions=[0.1],
                    ... )
                    >>>
                    >>> # apply the material to all prims
                    >>> prims.apply_physics_materials(material)  # or [material]
                
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
                    >>> physics_material.paths[0]
                    '/World/physics_material/aluminum'
                
        """
    def get_collision_approximations(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[str]:
        """
        Get the collision approximation types for mesh collision detection.
        
                Backends: :guilabel:`usd`.
        
                The collision approximation type determines how the mesh geometry is approximated for collision detection.
                Different approximations offer trade-offs between accuracy and performance.
        
                .. list-table::
                    :header-rows: 1
        
                    * - Approximation
                      - Full name
                      - Description
                    * - ``"none"``
                      - Triangle Mesh
                      - The mesh geometry is used directly as a collider without any approximation.
                    * - ``"convexDecomposition"``
                      - Convex Decomposition
                      - A convex mesh decomposition is performed. This results in a set of convex mesh colliders.
                    * - ``"convexHull"``
                      - Convex Hull
                      - A convex hull of the mesh is generated and used as the collider.
                    * - ``"boundingSphere"``
                      - Bounding Sphere
                      - A bounding sphere is computed around the mesh and used as a collider.
                    * - ``"boundingCube"``
                      - Bounding Cube
                      - An optimally fitting box collider is computed around the mesh.
                    * - ``"meshSimplification"``
                      - Mesh Simplification
                      - A mesh simplification step is performed, resulting in a simplified triangle mesh collider.
                    * - ``"sdf"``
                      - SDF Mesh
                      - SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape.
                    * - ``"sphereFill"``
                      - Sphere Approximation
                      - A sphere mesh decomposition is performed. This results in a set of sphere colliders.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    List of collision approximation types (shape ``(N,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the collision approximation of all prims after setting them to different types
                    >>> prims.set_collision_approximations(["convexDecomposition", "convexHull", "boundingSphere"])
                    >>> prims.get_collision_approximations()
                    ['convexDecomposition', 'convexHull', 'boundingSphere']
                
        """
    def get_enabled_collisions(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the enabled state of the collision API of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating if the collision API is enabled (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the collision enabled state of all prims after disabling it for the second prim
                    >>> prims.set_enabled_collisions([False], indices=[1])
                    >>> print(prims.get_enabled_collisions())
                    [[ True]
                     [False]
                     [ True]]
                
        """
    def get_offsets(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the contact and rest offsets for collision detection between prims.
        
                Backends: :guilabel:`usd`.
        
                Shapes whose distance is less than the sum of their contact offset values will generate contacts.
                The rest offset determines the distance at which two shapes will come to rest.
                Search for *Advanced Collision Detection* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The contact offsets (shape ``(N, 1)``). 2) The rest offsets (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the offsets of all prims
                    >>> contact_offsets, rest_offsets = prims.get_offsets()
                    >>> contact_offsets.shape, rest_offsets.shape
                    ((3, 1), (3, 1))
                    >>>
                    >>> # get the offsets of the second prim
                    >>> contact_offsets, rest_offsets = prims.get_offsets(indices=[1])
                    >>> contact_offsets.shape, rest_offsets.shape
                    ((1, 1), (1, 1))
                
        """
    def get_torsional_patch_radii(self, *, indices: list | np.ndarray | wp.array | None = None, minimum: bool = False) -> wp.array:
        """
        Get the torsional patch radii of the contact patches used to apply torsional frictions.
        
                Backends: :guilabel:`usd`.
        
                Search for *Torsional Patch Radius* in |physx_docs| for more details.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    minimum: Whether to get the minimum torsional patch radii instead of the standard ones.
        
                Returns:
                    The (minimum) torsional patch radii (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the torsional patch radii of all prims
                    >>> radii = prims.get_torsional_patch_radii()
                    >>> radii.shape
                    (3, 1)
                    >>>
                    >>> # get the torsional patch radii of second prim
                    >>> radii = prims.get_torsional_patch_radii(indices=[1])
                    >>> radii.shape
                    (1, 1)
                
        """
    def set_collision_approximations(self, approximations: str | list[str], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the collision approximation types for mesh collision detection.
        
                Backends: :guilabel:`usd`.
        
                The collision approximation type determines how the mesh geometry is approximated for collision detection.
                Different approximations offer trade-offs between accuracy and performance.
        
                .. list-table::
                    :header-rows: 1
        
                    * - Approximation
                      - Full name
                      - Description
                    * - ``"none"``
                      - Triangle Mesh
                      - The mesh geometry is used directly as a collider without any approximation.
                    * - ``"convexDecomposition"``
                      - Convex Decomposition
                      - A convex mesh decomposition is performed. This results in a set of convex mesh colliders.
                    * - ``"convexHull"``
                      - Convex Hull
                      - A convex hull of the mesh is generated and used as the collider.
                    * - ``"boundingSphere"``
                      - Bounding Sphere
                      - A bounding sphere is computed around the mesh and used as a collider.
                    * - ``"boundingCube"``
                      - Bounding Cube
                      - An optimally fitting box collider is computed around the mesh.
                    * - ``"meshSimplification"``
                      - Mesh Simplification
                      - A mesh simplification step is performed, resulting in a simplified triangle mesh collider.
                    * - ``"sdf"``
                      - SDF Mesh
                      - SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape.
                    * - ``"sphereFill"``
                      - Sphere Approximation
                      - A sphere mesh decomposition is performed. This results in a set of sphere colliders.
        
                Args:
                    approximations: Approximation types to use for collision detection (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the collision approximations for all prims to 'convexDecomposition'
                    >>> prims.set_collision_approximations(["convexDecomposition"])
                
        """
    def set_enabled_collisions(self, enabled: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Enable or disable the collision API of the prims.
        
                Backends: :guilabel:`usd`.
        
                When disabled, the prims will not participate in collision detection.
        
                Args:
                    enabled: Boolean flags to enable/disable collision APIs (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the collision API for all prims
                    >>> prims.set_enabled_collisions([True])
                    >>>
                    >>> # disable the collision API for the first and last prims
                    >>> prims.set_enabled_collisions([False], indices=[0, 2])
                
        """
    def set_offsets(self, contact_offsets: list | np.ndarray | wp.array = None, rest_offsets: list | np.ndarray | wp.array = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the contact and rest offsets for collision detection between prims.
        
                Backends: :guilabel:`usd`.
        
                Shapes whose distance is less than the sum of their contact offset values will generate contacts.
                The rest offset determines the distance at which two shapes will come to rest.
                Search for *Advanced Collision Detection* in |physx_docs| for more details.
        
                .. warning::
        
                    The contact offset must be positive and greater than the rest offset.
        
                Args:
                    contact_offsets: Contact offsets of the collision shapes (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    rest_offsets: Rest offsets of the collision shapes (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither contact_offsets nor rest_offsets are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set same offsets (contact: 0.005, rest: 0.001) for all prims
                    >>> prims.set_offsets(contact_offsets=[0.005], rest_offsets=[0.001])
                    >>>
                    >>> # set only the rest offsets for the second prim
                    >>> prims.set_offsets(rest_offsets=[0.002], indices=[1])
                
        """
    def set_torsional_patch_radii(self, radii: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None, minimum: bool = False) -> None:
        """
        Set the torsional patch radii of the contact patches used to apply torsional frictions.
        
                Backends: :guilabel:`usd`.
        
                Search for *Torsional Patch Radius* in |physx_docs| for more details.
        
                Args:
                    radii: Torsional patch radii (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
                    minimum: Whether to set the minimum torsional patch radii instead of the standard ones.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the torsional patch radii for all prims
                    >>> prims.set_torsional_patch_radii([0.1])
                    >>>
                    >>> # set the torsional patch radii for the first and last prims
                    >>> prims.set_torsional_patch_radii([0.2], indices=np.array([0, 2]))
                
        """
    @property
    def geoms(self) -> list[UsdGeom.Gprim]:
        """
        USD geometric primitives encapsulated by the wrapper.
        
                Returns:
                    List of USD geometric primitives.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.geoms
                    [UsdGeom.Gprim(Usd.Prim(</World/prim_0>)),
                     UsdGeom.Gprim(Usd.Prim(</World/prim_1>)),
                     UsdGeom.Gprim(Usd.Prim(</World/prim_2>))]
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
