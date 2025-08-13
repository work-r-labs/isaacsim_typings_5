from __future__ import annotations
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
import omni as omni
from pxr import Usd
from pxr import UsdGeom
from pxr import Vt
import typing
import warp as wp
__all__: list[str] = ['Mesh', 'Usd', 'UsdGeom', 'Vt', 'XformPrim', 'np', 'omni', 'ops_utils', 'stage_utils', 'wp']
class Mesh(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    High level class for creating/wrapping USD Mesh (points that are connected into edges and faces) prims.
    
        .. note::
    
            This class creates or wraps (one of both) USD Mesh prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Mesh prims.
            * If the prim paths do not exist, USD Mesh prims are created at each path and a wrapper is placed over them.
    
        Args:
            paths: Single path or list of paths to existing or non-existing (one of both) USD prims.
                Can include regular expressions for matching multiple prims.
            primitives: Primitives to be created (shape ``(N,)``). If not defined, an empty mesh is created.
                Primitives are used only for *creating* operations. For *wrapping* operations, primitives are ignored.
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
            AssertionError: If wrapped prims are not USD Mesh.
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import Mesh
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create Plane meshes at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = Mesh(paths, primitives="Plane")  # doctest: +NO_CHECK
    
        Example (create mesh from external package: trimesh):
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.objects import Mesh
            >>> import trimeshx  # doctest: +SKIP
            >>>
            >>> # icosahedron mesh (20 faces)
            >>> mesh = trimesh.creation.icosahedron()  # doctest: +SKIP
            >>>
            >>> # create an USD Mesh from the icosahedron defined by trimesh
            >>> mesh_prim = Mesh("/World/icosahedron")  # doctest: +SKIP
            >>> mesh_prim.set_points([mesh.vertices])  # doctest: +SKIP
            >>> mesh_prim.set_face_specs(
            ...    vertex_indices=[mesh.faces.flatten()],
            ...    vertex_counts=[[3] * len(mesh.faces)]
            ... )  # doctest: +SKIP
            >>> mesh_prim.set_subdivision_specs(subdivision_schemes=["bilinear"])  # doctest: +SKIP
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating Mesh instances of this type.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Since this method is static, the output is always on the CPU.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating Mesh instances.
        
                Example:
        
                .. code-block:: python
        
                    >>> # check if the following prims at paths are valid for creating instances
                    >>> result = Mesh.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [False  True]
                
        """
    @staticmethod
    def fetch_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Mesh | None]:
        """
        Fetch instances of Mesh from prims (or prim paths) at the given paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Prim paths (or prims) to get Mesh instances from.
        
                Returns:
                    List of Mesh instances or ``None`` if the prim is not a supported Mesh type.
        
                Example:
        
                .. code-block:: python
        
                    >>> import isaacsim.core.experimental.utils.stage as stage_utils
                    >>> from isaacsim.core.experimental.objects import Mesh
                    >>>
                    >>> # given a USD stage with the prims at paths /World, /World/A (Mesh)
                    >>> stage_utils.define_prim(f"/World/A", "Mesh")  # doctest: +NO_CHECK
                    >>>
                    >>> # fetch mesh instances
                    >>> Mesh.fetch_instances(["/World", "/World/A"])
                    [None, <isaacsim.core.experimental.objects.impl.mesh.Mesh object at 0x...>]
                
        """
    @staticmethod
    def update_extents(geoms: list[UsdGeom.Mesh]) -> None:
        """
        Update the gprims' extents.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    geoms: Geoms to process.
                
        """
    def __init__(self, paths: str | list[str], *, primitives: typing.Literal['Cone', 'Cube', 'Cylinder', 'Disk', 'Plane', 'Sphere', 'Torus'] | list[typing.Literal['Cone', 'Cube', 'Cylinder', 'Disk', 'Plane', 'Sphere', 'Torus']] | None = None, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def get_corner_specs(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[wp.array], list[wp.array]]:
        """
        Get the corner specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) List (shape ``(N,)``) of indices of points (shape ``(number of target points,)``).
                    2) List (shape ``(N,)``) of sharpness values (shape ``(number of target points,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the corner specifications of all prims
                    >>> corner_indices, corner_sharpnesses = prims.get_corner_specs()
                
        """
    def get_crease_specs(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[wp.array], list[wp.array], list[wp.array]]:
        """
        Get the crease (set of adjacent sharpened edges) specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Three-elements tuple.
                    1) List (shape ``(N,)``) of indices of points (shape ``(sum of all elements of the creaseLengths,)``).
                    2) List (shape ``(N,)``) of number of points of each crease (shape ``(number of creases,)``).
                    3) List (shape ``(N,)``) of sharpness values (shape ``(number of creases,)`` or
                    ``(sum over all X of (creaseLengths[X] - 1),)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the crease specifications of all prims
                    >>> crease_indices, crease_lengths, crease_sharpnesses = prims.get_crease_specs()
                
        """
    def get_face_specs(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[wp.array], list[wp.array], list[typing.Literal['none', 'cornersOnly', 'cornersPlus1', 'cornersPlus2', 'boundaries', 'all']], list[wp.array]]:
        """
        Get the face (3D model flat surface) specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Four-elements tuple. 1) List (shape ``(N,)``) of indices (of points) of each vertex
                    of each face (shape ``(sum of all elements of the vertexCounts,)``).
                    2) List (shape ``(N,)``) of number of vertices in each face (shape ``(number of faces,)``).
                    3) List (shape ``(N,)``) of face-varying interpolation rules.
                    4) List (shape ``(N,)``) of indices of all face holes (shape ``(up to the number of faces,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the face specifications of all prims
                    >>> face_indices, face_counts, face_interpolations, face_holes = prims.get_face_specs()
                    >>> # print the first prim's face specifications (Plane mesh composed of 4 points with 1 face)
                    >>> print(face_indices[0])  # points indices of the face
                    [0 1 3 2]
                    >>> print(face_counts[0])  # number of points in the face
                    [4]
                    >>> face_interpolations[0]  # face-varying interpolation rule
                    'cornersPlus1'
                    >>> print(face_holes[0])  # indices of the face holes (empty: no face holes)
                    []
                
        """
    def get_normals(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[wp.array]:
        """
        Get the mesh normals (object-space orientation for individual points) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    List (shape ``(N,)``) of mesh normals (shape ``(number of normals, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the normals of all prims
                    >>> normals = prims.get_normals()
                    >>> normals[0].shape  # normals' shape of the first prim
                    (4, 3)
                
        """
    def get_points(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[wp.array]:
        """
        Get the mesh points (in local space) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    List (shape ``(N,)``) of mesh points (shape ``(number of points, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the points of all prims
                    >>> points = prims.get_points()
                    >>> points[0].shape  # points' shape of the first prim
                    (4, 3)
                
        """
    def get_subdivision_specs(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[typing.Literal['catmullClark', 'loop', 'bilinear', 'none']], list[typing.Literal['none', 'edgeOnly', 'edgeAndCorner']], list[typing.Literal['catmullClark', 'smooth']]]:
        """
        Get the subdivision specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Three-elements tuple. 1) Subdivision schemes (shape ``(N,)``).
                    2) Boundary interpolation rules (shape ``(N,)``).
                    3) Triangle subdivision rules (shape ``(N,)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the subdivision specifications of all prims
                    >>> subdivision_schemes, interpolate_boundaries, triangle_subdivision_rules = prims.get_subdivision_specs()
                    >>> # print the first prim's subdivision specifications
                    >>> subdivision_schemes[0]  # subdivision scheme
                    'none'
                    >>> interpolate_boundaries[0]  # boundary interpolation rule
                    'edgeAndCorner'
                    >>> triangle_subdivision_rules[0]  # triangle subdivision rule
                    'catmullClark'
                
        """
    def set_corner_specs(self, corner_indices: list[list | np.ndarray | wp.array], corner_sharpnesses: list[list | np.ndarray | wp.array], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the corner specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    corner_indices: List (shape ``(N,)``) of indices of points (shape ``(number of target points,)``) for which
                        a corresponding sharpness value is specified in ``cornerSharpnesses``.
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    corner_sharpnesses: List (shape ``(N,)``) of sharpness values (shape ``(number of target points,)``)
                        associated with a corresponding set of points specified in ``cornerIndices``.
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If each respective pair of items (from ``corner_indices`` and ``corner_sharpnesses``)
                        has a different shape.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the corner specifications (mesh points: 1, 2) for the second prim
                    >>> prims.set_corner_specs(corner_indices=[[1, 2]], corner_sharpnesses=[[5.0, 10.0]], indices=[1])
                
        """
    def set_crease_specs(self, crease_indices: list[list | np.ndarray | wp.array], crease_lengths: list[list | np.ndarray | wp.array], crease_sharpnesses: list[list | np.ndarray | wp.array], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the crease (set of adjacent sharpened edges) specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    crease_indices: List (shape ``(N,)``) of indices of points grouped into sets of successive pairs that identify
                        edges to be creased (shape ``(sum of all elements of the creaseLengths,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    crease_lengths: List (shape ``(N,)``) of number of points of each crease, whose indices are successively laid
                        out in the ``creaseIndices`` attribute (shape ``(number of creases,)``).
                        Since each crease must be at least one edge long, each element of this array must be at least two.
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    crease_sharpnesses: List (shape ``(N,)``) of per-crease or per-edge sharpness values
                        (shape ``(number of creases,)`` or ``(sum over all X of (creaseLengths[X] - 1),)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If the sum of the elements of ``crease_lengths`` is not equal to the number of elements
                        of ``crease_indices``.
                    AssertionError: If the number of elements of ``crease_sharpnesses`` is not equal to the number of elements
                        of ``crease_lengths`` or the sum over all X of ``(crease_lengths[X] - 1)``.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the crease specifications (mesh points: 0, 3) for the second prim
                    >>> prims.set_crease_specs(
                    ...     crease_indices=[[0, 3]],
                    ...     crease_lengths=[[2]],
                    ...     crease_sharpnesses=[[10.0]],
                    ...     indices=[1]
                    ... )
                
        """
    def set_face_specs(self, vertex_indices: list[list | np.ndarray | wp.array] | None = None, vertex_counts: list[list | np.ndarray | wp.array] | None = None, varying_linear_interpolations: list[typing.Literal['none', 'cornersOnly', 'cornersPlus1', 'cornersPlus2', 'boundaries', 'all']] | None = None, hole_indices: list[list | np.ndarray | wp.array] | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the face (3D model flat surface) specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    vertex_indices: List (shape ``(N,)``) of indices (of points) of each vertex of each face
                        (shape ``(sum of all elements of the vertexCounts,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    vertex_counts: List (shape ``(N,)``) of number of vertices in each face, which is also the number of consecutive
                        indices in ``faceVertexIndices`` that define the face (shape ``(number of faces,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    varying_linear_interpolations: Face-varying interpolation rules in the interior of face-varying regions
                        (smooth or linear) and at the boundaries for subdivision surfaces (shape ``(N,)``).
                    hole_indices: List (shape ``(N,)``) of indices of all faces that should be treated as holes, e.g.:
                        made invisible (shape ``(up to the number of faces,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither vertex_indices, vertex_counts, varying_linear_interpolations nor
                        hole_indices are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the face specifications (2 triangles) for the second prim
                    >>> prims.set_face_specs(vertex_indices=[[0, 1, 3, 0, 2, 3]], vertex_counts=[[3, 3]], indices=[1])
                
        """
    def set_normals(self, normals: list[list | np.ndarray | wp.array], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the mesh normals (object-space orientation for individual points) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. note::
        
                    Normals should not be authored on any USD Mesh that is subdivided,
                    since the subdivision algorithm will define its own normals.
        
                Args:
                    normals: List (shape ``(N,)``) of mesh normals (shape ``(number of normals, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # clear the normals for the second prim
                    >>> prims.set_normals([[]], indices=[1])
                
        """
    def set_points(self, points: list[list | np.ndarray | wp.array], *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the mesh points (in local space) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    points: List (shape ``(N,)``) of mesh points (shape ``(number of points, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the points (fold each face diagonally) for the second prim
                    >>> prims.set_points([[(-0.5, -0.5, 0.0), (0.5, -0.5, 1.0), (-0.5, 0.5, 1.0), (0.5, 0.5, 0.0)]], indices=[1])
                
        """
    def set_subdivision_specs(self, subdivision_schemes: list[typing.Literal['catmullClark', 'loop', 'bilinear', 'none']] | None = None, interpolate_boundaries: list[typing.Literal['none', 'edgeOnly', 'edgeAndCorner']] | None = None, triangle_subdivision_rules: list[typing.Literal['catmullClark', 'smooth']] | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the subdivision specifications of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    subdivision_schemes: Subdivision schemes (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    interpolate_boundaries: Boundary interpolation rules for faces adjacent to boundary edges and points (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    triangle_subdivision_rules: Subdivision rules for the *Catmull-Clark* scheme to try and improve undesirable
                        artifacts when subdividing triangles (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither subdivision_schemes, interpolate_boundaries nor triangle_subdivision_rules are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the subdivision specifications for the second prim
                    >>> prims.set_subdivision_specs(subdivision_schemes=["bilinear"], indices=[1])
                
        """
    @property
    def geoms(self) -> list[UsdGeom.Mesh]:
        """
        USD Mesh encapsulated by the wrapper.
        
                Returns:
                    List of USD Mesh.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.geoms
                    [UsdGeom.Mesh(Usd.Prim(</World/prim_0>)),
                     UsdGeom.Mesh(Usd.Prim(</World/prim_1>)),
                     UsdGeom.Mesh(Usd.Prim(</World/prim_2>))]
                
        """
    @property
    def num_faces(self) -> list[int]:
        """
        Number of faces of the meshes.
        
                Returns:
                    List of number of faces as defined by the size of the ``faceVertexCounts`` array.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_faces
                    [1, 1, 1]
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
