from __future__ import annotations
import _ctypes
import builtins as builtins
import ctypes as ctypes
import inspect as inspect
import numpy as np
import numpy
from numpy import typing as npt
import struct as struct
import typing
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
import warp as warp
from warp.fabric import fabricarray
from warp.fabric import indexedfabricarray
import zlib as zlib
__all__ = ['ARRAY_MAX_DIMS', 'ARRAY_TYPE_FABRIC', 'ARRAY_TYPE_FABRIC_INDEXED', 'ARRAY_TYPE_INDEXED', 'ARRAY_TYPE_REGULAR', 'Array', 'Bvh', 'BvhQuery', 'Cols', 'DType', 'Float', 'Generic', 'HashGrid', 'HashGridQuery', 'Int', 'LAUNCH_MAX_DIMS', 'Length', 'MarchingCubes', 'Matrix', 'Mesh', 'MeshQueryAABB', 'MeshQueryPoint', 'MeshQueryRay', 'NamedTuple', 'Quaternion', 'Rows', 'Scalar', 'T', 'Tile', 'TileBinaryMap', 'TileConstant', 'TileLoad', 'TileRange', 'TileShared', 'TileUnaryMap', 'TileZeros', 'Transformation', 'TypeVar', 'Vector', 'Volume', 'adj_batched_matmul', 'adj_matmul', 'array', 'array1d', 'array2d', 'array3d', 'array4d', 'array_ctype_from_interface', 'array_t', 'array_type_id', 'array_types', 'batched_matmul', 'bool', 'builtins', 'bvh_query_t', 'check_array_shape', 'check_index_array', 'constant', 'ctypes', 'dtype_from_numpy', 'dtype_to_numpy', 'fabricarray', 'float16', 'float32', 'float64', 'float_base', 'float_to_half_bits', 'float_types', 'from_ptr', 'generic_types', 'get_signature', 'get_type_code', 'half_bits_to_float', 'hash_grid_query_t', 'indexedarray', 'indexedarray1d', 'indexedarray2d', 'indexedarray3d', 'indexedarray4d', 'indexedarray_t', 'indexedfabricarray', 'infer_argument_types', 'inspect', 'int16', 'int32', 'int64', 'int8', 'int_base', 'int_tuple_type_hints', 'int_types', 'is_array', 'is_float', 'is_generic_signature', 'is_int', 'is_tile', 'is_value', 'launch_bounds_t', 'mat22', 'mat22d', 'mat22f', 'mat22h', 'mat33', 'mat33d', 'mat33f', 'mat33h', 'mat44', 'mat44d', 'mat44f', 'mat44h', 'matmul', 'matrix', 'mesh_query_aabb_t', 'mesh_query_point_t', 'mesh_query_ray_t', 'non_atomic_types', 'noncontiguous_array_base', 'np', 'np_dtype_to_warp_type', 'npt', 'quat', 'quatd', 'quaternion', 'quatf', 'quath', 'range_t', 'scalar_and_bool_types', 'scalar_base', 'scalar_types', 'scalars_equal', 'shape_t', 'simple_type_codes', 'spatial_matrix', 'spatial_matrixd', 'spatial_matrixf', 'spatial_matrixh', 'spatial_vector', 'spatial_vectord', 'spatial_vectorf', 'spatial_vectorh', 'strides_from_shape', 'struct', 'transform', 'transformation', 'transformd', 'transformf', 'transformh', 'type_ctype', 'type_is_float', 'type_is_generic', 'type_is_generic_scalar', 'type_is_int', 'type_is_matrix', 'type_is_quaternion', 'type_is_value', 'type_is_vector', 'type_length', 'type_matches_template', 'type_repr', 'type_scalar_type', 'type_size_in_bytes', 'type_to_warp', 'type_typestr', 'types_equal', 'uint16', 'uint32', 'uint64', 'uint8', 'value_types', 'vec2', 'vec2b', 'vec2d', 'vec2f', 'vec2h', 'vec2i', 'vec2l', 'vec2s', 'vec2ub', 'vec2ui', 'vec2ul', 'vec2us', 'vec3', 'vec3b', 'vec3d', 'vec3f', 'vec3h', 'vec3i', 'vec3l', 'vec3s', 'vec3ub', 'vec3ui', 'vec3ul', 'vec3us', 'vec4', 'vec4b', 'vec4d', 'vec4f', 'vec4h', 'vec4i', 'vec4l', 'vec4s', 'vec4ub', 'vec4ui', 'vec4ul', 'vec4us', 'vector', 'vector_types', 'void', 'warp', 'warp_type_to_np_dtype', 'zlib']
class Array(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~DType])
    __parameters__: typing.ClassVar[tuple]  # value = (~DType)
class Bvh:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, lowers, uppers):
        """
        Class representing a bounding volume hierarchy.
        
                Attributes:
                    id: Unique identifier for this bvh object, can be passed to kernels.
                    device: Device this object lives on, all buffers must live on the same device.
        
                Args:
                    lowers (:class:`warp.array`): Array of lower bounds :class:`warp.vec3`
                    uppers (:class:`warp.array`): Array of upper bounds :class:`warp.vec3`
                
        """
    def refit(self):
        """
        Refit the BVH. This should be called after users modify the `lowers` and `uppers` arrays.
        """
class HashGrid:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, dim_x, dim_y, dim_z, device = None):
        """
        Class representing a hash grid object for accelerated point queries.
        
                Attributes:
                    id: Unique identifier for this mesh object, can be passed to kernels.
                    device: Device this object lives on, all buffers must live on the same device.
        
                Args:
                    dim_x (int): Number of cells in x-axis
                    dim_y (int): Number of cells in y-axis
                    dim_z (int): Number of cells in z-axis
                
        """
    def build(self, points, radius):
        """
        Updates the hash grid data structure.
        
                This method rebuilds the underlying datastructure and should be called any time the set
                of points changes.
        
                Args:
                    points (:class:`warp.array`): Array of points of type :class:`warp.vec3`
                    radius (float): The cell size to use for bucketing points, cells are cubes with edges of this width.
                                    For best performance the radius used to construct the grid should match closely to
                                    the radius used when performing queries.
                
        """
    def reserve(self, num_points):
        ...
class MarchingCubes:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, nx: int, ny: int, nz: int, max_verts: int, max_tris: int, device = None):
        """
        CUDA-based Marching Cubes algorithm to extract a 2D surface mesh from a 3D volume.
        
                Attributes:
                    id: Unique identifier for this object.
                    verts (:class:`warp.array`): Array of vertex positions of type :class:`warp.vec3f`
                      for the output surface mesh.
                      This is populated after running :func:`surface`.
                    indices (:class:`warp.array`): Array containing indices of type :class:`warp.int32`
                      defining triangles for the output surface mesh.
                      This is populated after running :func:`surface`.
        
                      Each set of three consecutive integers in the array represents a single triangle,
                      in which each integer is an index referring to a vertex in the :attr:`verts` array.
        
                Args:
                    nx: Number of cubes in the x-direction.
                    ny: Number of cubes in the y-direction.
                    nz: Number of cubes in the z-direction.
                    max_verts: Maximum expected number of vertices (used for array preallocation).
                    max_tris: Maximum expected number of triangles (used for array preallocation).
                    device (Devicelike): CUDA device on which to run marching cubes and allocate memory.
        
                Raises:
                    RuntimeError: ``device`` not a CUDA device.
        
                .. note::
                    The shape of the marching cubes should match the shape of the scalar field being surfaced.
        
                
        """
    def resize(self, nx: int, ny: int, nz: int, max_verts: int, max_tris: int) -> None:
        """
        Update the expected input and maximum output sizes for the marching cubes calculation.
        
                This function has no immediate effect on the underlying buffers.
                The new values take effect on the next :func:`surface` call.
        
                Args:
                  nx: Number of cubes in the x-direction.
                  ny: Number of cubes in the y-direction.
                  nz: Number of cubes in the z-direction.
                  max_verts: Maximum expected number of vertices (used for array preallocation).
                  max_tris: Maximum expected number of triangles (used for array preallocation).
                
        """
    def surface(self, field: array(dtype=float, ndim=3), threshold: float) -> None:
        """
        Compute a 2D surface mesh of a given isosurface from a 3D scalar field.
        
                The triangles and vertices defining the output mesh are written to the
                :attr:`indices` and :attr:`verts` arrays.
        
                Args:
                  field: Scalar field from which to generate a mesh.
                  threshold: Target isosurface value.
        
                Raises:
                  ValueError: ``field`` is not a 3D array.
                  ValueError: Marching cubes shape does not match the shape of ``field``.
                  RuntimeError: :attr:`max_verts` and/or :attr:`max_tris` might be too small to hold the surface mesh.
                
        """
class Matrix(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~Rows, ~Cols, ~Scalar])
    __parameters__: typing.ClassVar[tuple]  # value = (~Rows, ~Cols, ~Scalar)
class Mesh:
    class Var:
        @staticmethod
        def type_to_ctype(t, value_type = False):
            ...
        def __init__(self, label, type, requires_grad = False, constant = None, prefix = True):
            ...
        def __str__(self):
            ...
        def ctype(self, value_type = False):
            ...
        def emit(self, prefix: str = 'var'):
            ...
        def emit_adj(self):
            ...
        def mark_read(self):
            """
            Marks this Var as having been read from in a kernel (array only).
            """
        def mark_write(self, **kwargs):
            """
            Marks this Var has having been written to in a kernel (array only).
            """
    vars: typing.ClassVar[dict]  # value = {'points': <warp.codegen.Var object>, 'velocities': <warp.codegen.Var object>, 'indices': <warp.codegen.Var object>}
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, points = None, indices = None, velocities = None, support_winding_number = False):
        """
        Class representing a triangle mesh.
        
                Attributes:
                    id: Unique identifier for this mesh object, can be passed to kernels.
                    device: Device this object lives on, all buffers must live on the same device.
        
                Args:
                    points (:class:`warp.array`): Array of vertex positions of type :class:`warp.vec3`
                    indices (:class:`warp.array`): Array of triangle indices of type :class:`warp.int32`, should be a 1d array with shape (num_tris * 3)
                    velocities (:class:`warp.array`): Array of vertex velocities of type :class:`warp.vec3` (optional)
                    support_winding_number (bool): If true the mesh will build additional datastructures to support `wp.mesh_query_point_sign_winding_number()` queries
                
        """
    def refit(self):
        """
        Refit the BVH to points. This should be called after users modify the `points` data.
        """
    @property
    def points(self):
        """
        The array of mesh's vertex positions of type :class:`warp.vec3`.
        
                The `Mesh.points` property has a custom setter method. Users can modify the vertex positions in-place,
                but the `refit()` method must be called manually after such modifications. Alternatively, assigning a new array
                to this property is also supported. The new array must have the same shape as the original, and once assigned,
                the `Mesh` class will automatically perform a refit operation based on the new vertex positions.
                
        """
    @points.setter
    def points(self, points_new):
        ...
    @property
    def velocities(self):
        """
        The array of mesh's velocities of type :class:`warp.vec3`.
        
                This is a property with a custom setter method. Users can modify the velocities in-place,
                or assigning a new array to this property. No refitting is needed for changing velocities.
                
        """
    @velocities.setter
    def velocities(self, velocities_new):
        ...
class Quaternion(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~Float])
    __parameters__: typing.ClassVar[tuple]  # value = (~Float)
class Tile:
    alignment: typing.ClassVar[int] = 16
    def __init__(self, dtype, M, N, op = None, storage = 'register', layout = 'rowmajor', strides = None, owner = True):
        ...
    def align(self, bytes):
        ...
    def cinit(self, requires_grad = False):
        ...
    def ctype(self):
        ...
    def size_in_bytes(self):
        ...
class TileBinaryMap(Tile):
    def __init__(self, a, b, storage = 'register'):
        ...
class TileConstant(Tile):
    def __init__(self, dtype, M, N):
        ...
class TileLoad(Tile):
    def __init__(self, array, M, N, storage = 'register'):
        ...
class TileRange(Tile):
    def __init__(self, dtype, start, stop, step, storage = 'register'):
        ...
class TileShared(Tile):
    def __init__(self, t):
        ...
class TileUnaryMap(Tile):
    def __init__(self, t, storage = 'register'):
        ...
class TileZeros(Tile):
    def __init__(self, dtype, M, N, storage = 'register'):
        ...
class Transformation(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~Float])
    __parameters__: typing.ClassVar[tuple]  # value = (~Float)
class Vector(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~Length, ~Scalar])
    __parameters__: typing.ClassVar[tuple]  # value = (~Length, ~Scalar)
class Volume:
    class FeatureArrayInfo(tuple):
        """
        Metadata for a supplemental data array
        """
        __match_args__: typing.ClassVar[tuple] = ('name', 'ptr', 'value_size', 'value_count', 'type_str')
        __orig_bases__: typing.ClassVar[tuple] = (typing.NamedTuple)
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('name', 'ptr', 'value_size', 'value_count', 'type_str')
        @staticmethod
        def __new__(_cls, name: ForwardRef('str'), ptr: ForwardRef('int'), value_size: ForwardRef('int'), value_count: ForwardRef('int'), type_str: ForwardRef('str')):
            """
            Create new instance of FeatureArrayInfo(name, ptr, value_size, value_count, type_str)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new FeatureArrayInfo object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new FeatureArrayInfo object replacing specified fields with new values
            """
    class GridInfo(tuple):
        """
        Grid metadata
        """
        __match_args__: typing.ClassVar[tuple] = ('name', 'size_in_bytes', 'grid_index', 'grid_count', 'type_str', 'translation', 'transform_matrix')
        __orig_bases__: typing.ClassVar[tuple] = (typing.NamedTuple)
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('name', 'size_in_bytes', 'grid_index', 'grid_count', 'type_str', 'translation', 'transform_matrix')
        @staticmethod
        def __new__(_cls, name: ForwardRef('str'), size_in_bytes: ForwardRef('int'), grid_index: ForwardRef('int'), grid_count: ForwardRef('int'), type_str: ForwardRef('str'), translation: ForwardRef('vec3f'), transform_matrix: ForwardRef('mat33f')):
            """
            Create new instance of GridInfo(name, size_in_bytes, grid_index, grid_count, type_str, translation, transform_matrix)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new GridInfo object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new GridInfo object replacing specified fields with new values
            """
    CLOSEST: typing.ClassVar[int] = 0
    LINEAR: typing.ClassVar[int] = 1
    _nvdb_index_types: typing.ClassVar[tuple] = ('Index', 'OnIndex', 'IndexMask', 'OnIndexMask')
    _nvdb_type_to_dtype: typing.ClassVar[dict] = {'float': float32, 'double': float64, 'int16': int16, 'int32': int32, 'int64': int64, 'Vec3f': vec3f, 'Vec3d': vec3d, 'Half': float16, 'uint32': uint32, 'bool': bool, 'Vec4f': vec4f, 'Vec4d': vec4d, 'Vec3u8': vec3ub, 'Vec3u16': vec3us, 'uint8': uint8}
    @staticmethod
    def _fill_transform_buffers(voxel_size: float | list[float], translation, transform):
        ...
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    @classmethod
    def allocate(cls, min: list[int], max: list[int], voxel_size: float, bg_value = 0.0, translation = (0.0, 0.0, 0.0), points_in_world_space = False, device = None) -> Volume:
        """
        Allocate a new Volume based on the bounding box defined by min and max.
        
                This function is only supported for CUDA devices.
        
                Allocate a volume that is large enough to contain voxels [min[0], min[1], min[2]] - [max[0], max[1], max[2]], inclusive.
                If points_in_world_space is true, then min and max are first converted to index space with the given voxel size and
                translation, and the volume is allocated with those.
        
                The smallest unit of allocation is a dense tile of 8x8x8 voxels, the requested bounding box is rounded up to tiles, and
                the resulting tiles will be available in the new volume.
        
                Args:
                    min (array-like): Lower 3D coordinates of the bounding box in index space or world space, inclusive.
                    max (array-like): Upper 3D coordinates of the bounding box in index space or world space, inclusive.
                    voxel_size (float): Voxel size of the new volume.
                    bg_value (float or array-like): Value of unallocated voxels of the volume, also defines the volume's type, a :class:`warp.vec3` volume is created if this is `array-like`, otherwise a float volume is created
                    translation (array-like): translation between the index and world spaces.
                    device (Devicelike): The CUDA device to create the volume on, e.g.: "cuda" or "cuda:0".
        
                
        """
    @classmethod
    def allocate_by_tiles(cls, tile_points: array, voxel_size: float | list[float] = None, bg_value = 0.0, translation = (0.0, 0.0, 0.0), device = None, transform = None) -> Volume:
        """
        Allocate a new Volume with active tiles for each point tile_points.
        
                This function is only supported for CUDA devices.
        
                The smallest unit of allocation is a dense tile of 8x8x8 voxels.
                This is the primary method for allocating sparse volumes. It uses an array of points indicating the tiles that must be allocated.
        
                Example use cases:
                    * `tile_points` can mark tiles directly in index space as in the case this method is called by `allocate`.
                    * `tile_points` can be a list of points used in a simulation that needs to transfer data to a volume.
        
                Args:
                    tile_points (:class:`warp.array`): Array of positions that define the tiles to be allocated.
                        The array may use an integer scalar type (2D N-by-3 array of :class:`warp.int32` or 1D array of `warp.vec3i` values), indicating index space positions,
                        or a floating point scalar type (2D N-by-3 array of :class:`warp.float32` or 1D array of `warp.vec3f` values), indicating world space positions.
                        Repeated points per tile are allowed and will be efficiently deduplicated.
                    voxel_size (float or array-like): Voxel size(s) of the new volume. Ignored if `transform` is given.
                    bg_value (array-like, float, int or None): Value of unallocated voxels of the volume, also defines the volume's type. A :class:`warp.vec3` volume is created if this is `array-like`, an index volume will be created if `bg_value` is ``None``.
                    translation (array-like): Translation between the index and world spaces.
                    transform (array-like): Linear transform between the index and world spaces. If ``None``, deduced from `voxel_size`.
                    device (Devicelike): The CUDA device to create the volume on, e.g.: "cuda" or "cuda:0".
        
                
        """
    @classmethod
    def allocate_by_voxels(cls, voxel_points: array, voxel_size: float | list[float] = None, translation = (0.0, 0.0, 0.0), device = None, transform = None) -> Volume:
        """
        Allocate a new Volume with active voxel for each point voxel_points.
        
                This function creates an *index* Volume, a special kind of volume that does not any store any
                explicit payload but encodes a linearized index for each active voxel, allowing to lookup and
                sample data from arbitrary external arrays.
        
                This function is only supported for CUDA devices.
        
                Args:
                    voxel_points (:class:`warp.array`): Array of positions that define the voxels to be allocated.
                        The array may use an integer scalar type (2D N-by-3 array of :class:`warp.int32` or 1D array of `warp.vec3i` values), indicating index space positions,
                        or a floating point scalar type (2D N-by-3 array of :class:`warp.float32` or 1D array of `warp.vec3f` values), indicating world space positions.
                        Repeated points per tile are allowed and will be efficiently deduplicated.
                    voxel_size (float or array-like): Voxel size(s) of the new volume. Ignored if `transform` is given.
                    translation (array-like): Translation between the index and world spaces.
                    transform (array-like): Linear transform between the index and world spaces. If ``None``, deduced from `voxel_size`.
                    device (Devicelike): The CUDA device to create the volume on, e.g.: "cuda" or "cuda:0".
        
                
        """
    @classmethod
    def load_from_address(cls, grid_ptr: int, buffer_size: int = 0, device = None) -> Volume:
        """
        
                Creates a new :class:`Volume` aliasing an in-memory grid buffer.
        
                In contrast to :meth:`load_from_nvdb` which should be used to load serialized NanoVDB grids,
                here the buffer must be uncompressed and must not contain file header information.
                If the passed address does not contain a NanoVDB grid, the behavior of this function is undefined.
        
                Args:
                    grid_ptr: Integer address of the start of the grid buffer
                    buffer_size: Size of the buffer, in bytes. If not provided, the size will be assumed to be that of the single grid starting at `grid_ptr`.
                    device: Device of the buffer, and of the returned Volume. If not provided, the current Warp device is assumed.
        
                Returns the newly created Volume.
                
        """
    @classmethod
    def load_from_numpy(cls, ndarray: np.array, min_world = (0.0, 0.0, 0.0), voxel_size = 1.0, bg_value = 0.0, device = None) -> Volume:
        """
        Creates a Volume object from a dense 3D NumPy array.
        
                This function is only supported for CUDA devices.
        
                Args:
                    min_world: The 3D coordinate of the lower corner of the volume.
                    voxel_size: The size of each voxel in spatial coordinates.
                    bg_value: Background value
                    device: The CUDA device to create the volume on, e.g.: "cuda" or "cuda:0".
        
                Returns:
        
                    A ``warp.Volume`` object.
                
        """
    @classmethod
    def load_from_nvdb(cls, file_or_buffer, device = None) -> Volume:
        """
        Creates a Volume object from a serialized NanoVDB file or in-memory buffer.
        
                Returns:
        
                    A ``warp.Volume`` object.
                
        """
    def __del__(self):
        ...
    def __init__(self, data: array, copy: bool = True):
        """
        Class representing a sparse grid.
        
                Args:
                    data (:class:`warp.array`): Array of bytes representing the volume in NanoVDB format
                    copy (bool): Whether the incoming data will be copied or aliased
                
        """
    def array(self) -> array:
        """
        Returns the raw memory buffer of the Volume as an array
        """
    def feature_array(self, feature_index: int, dtype = None) -> array:
        """
        Returns one the grid's feature data arrays as a Warp array
        
                Args:
                    feature_index: Index of the supplemental data array in the grid
                    dtype: Type for the returned Warp array. If not provided, will be deduced from the array metadata.
                
        """
    def get_feature_array_count(self) -> int:
        """
        Returns the number of supplemental data arrays stored alongside the grid
        """
    def get_feature_array_info(self, feature_index: int) -> Volume.FeatureArrayInfo:
        """
        Returns the metadata associated to the feature array at `feature_index`
        """
    def get_grid_info(self) -> Volume.GridInfo:
        """
        Returns the metadata associated with this Volume
        """
    def get_tile_count(self) -> int:
        """
        Returns the number of tiles (NanoVDB leaf nodes) of the volume
        """
    def get_tiles(self, out: array | None = None) -> array:
        """
        Returns the integer coordinates of all allocated tiles for this volume.
        
                Args:
                    out (:class:`warp.array`, optional): If provided, use the `out` array to store the tile coordinates, otherwise
                        a new array will be allocated. `out` must be a contiguous array of ``tile_count`` ``vec3i`` or ``tile_count x 3`` ``int32``
                        on the same device as this volume.
                
        """
    def get_voxel_count(self) -> int:
        """
        Returns the total number of allocated voxels for this volume
        """
    def get_voxel_size(self) -> tuple[float, float, float]:
        """
        Voxel size, i.e, world coordinates of voxel's diagonal vector
        """
    def get_voxels(self, out: array | None = None) -> array:
        """
        Returns the integer coordinates of all allocated voxels for this volume.
        
                Args:
                    out (:class:`warp.array`, optional): If provided, use the `out` array to store the voxel coordinates, otherwise
                        a new array will be allocated. `out` must be a contiguous array of ``voxel_count`` ``vec3i`` or ``voxel_count x 3`` ``int32``
                        on the same device as this volume.
                
        """
    def load_next_grid(self) -> Volume:
        """
        
                Tries to create a new warp Volume for the next grid that is linked to by this Volume.
        
                The existence of a next grid is deduced from the `grid_index` and `grid_count` metadata
                as well as the size of this Volume's in-memory buffer.
        
                Returns the newly created Volume, or None if there is no next grid.
                
        """
    def save_to_nvdb(self, path, codec: typing.Literal['none', 'zip', 'blosc'] = 'none'):
        """
        Serialize the Volume into a NanoVDB (.nvdb) file.
        
                Args:
                    path: File path to save.
                    codec: Compression codec used
                        "none" - no compression
                        "zip" - ZIP compression
                        "blosc" - BLOSC compression, requires the blosc module to be installed
                
        """
    @property
    def dtype(self) -> type:
        """
        Type of the Volume's values as a Warp type.
        
                If the grid does not contain values (e.g. index grids) or if the NanoVDB type is not
                representable as a Warp type, returns ``None``.
                
        """
    @property
    def is_index(self) -> bool:
        """
        Whether this Volume contains an index grid, that is, a type of grid that does
                not explicitly store values but associates each voxel to linearized index.
                
        """
class array(Array):
    """
    A fixed-size multi-dimensional array containing values of the same type.
    
        Attributes:
            dtype (DType): The data type of the array.
            ndim (int): The number of array dimensions.
            size (int): The number of items in the array.
            capacity (int): The amount of memory in bytes allocated for this array.
            shape (Tuple[int]): Dimensions of the array.
            strides (Tuple[int]): Number of bytes in each dimension between successive elements of the array.
            ptr (int): Pointer to underlying memory allocation backing the array.
            device (Device): The device where the array's memory allocation resides.
            pinned (bool): Indicates whether the array was allocated in pinned host memory.
            is_contiguous (bool): Indicates whether this array has a contiguous memory layout.
            deleter (Callable[[int, int], None]): A function to be called when the array is deleted,
                taking two arguments: pointer and size. If ``None``, then no function is called.
        
    """
    __parameters__: typing.ClassVar[tuple] = tuple()
    _vars = None
    grad = ...
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __ctype__(self):
        ...
    def __del__(self):
        ...
    def __dlpack__(self, stream = None):
        ...
    def __dlpack_device__(self):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, data: list | tuple | npt.NDArray | None = None, dtype: DType | typing.Any = ..., shape: tuple[int, ...] | None = None, strides: tuple[int, ...] | None = None, length: int | None = None, ptr: int | None = None, capacity: int | None = None, device = None, pinned: bool = False, copy: bool = True, owner: bool = False, deleter: typing.Callable[[int, int], None] | None = None, ndim: int | None = None, grad: array | None = None, requires_grad: bool = False):
        """
        Constructs a new Warp array object
        
                When the ``data`` argument is a valid list, tuple, or ndarray the array will be constructed from this object's data.
                For objects that are not stored sequentially in memory (e.g.: a list), then the data will first
                be flattened before being transferred to the memory space given by device.
        
                The second construction path occurs when the ``ptr`` argument is a non-zero uint64 value representing the
                start address in memory where existing array data resides, e.g.: from an external or C-library. The memory
                allocation should reside on the same device given by the device argument, and the user should set the length
                and dtype parameter appropriately.
        
                If neither ``data`` nor ``ptr`` are specified, the ``shape`` or ``length`` arguments are checked next.
                This construction path can be used to create new uninitialized arrays, but users are encouraged to call
                ``wp.empty()``, ``wp.zeros()``, or ``wp.full()`` instead to create new arrays.
        
                If none of the above arguments are specified, a simple type annotation is constructed.  This is used when annotating
                kernel arguments or struct members (e.g.,``arr: wp.array(dtype=float)``).  In this case, only ``dtype`` and ``ndim``
                are taken into account and no memory is allocated for the array.
        
                Args:
                    data: An object to construct the array from, can be a Tuple, List, or generally any type convertible to an np.array
                    dtype: One of the available `data types <#data-types>`_, such as :class:`warp.float32`, :class:`warp.mat33`, or a custom `struct <#structs>`_. If dtype is ``Any`` and data is an ndarray, then it will be inferred from the array data type
                    shape: Dimensions of the array
                    strides: Number of bytes in each dimension between successive elements of the array
                    length: Number of elements of the data type (deprecated, users should use ``shape`` argument)
                    ptr: Address of an external memory address to alias (``data`` should be ``None``)
                    capacity: Maximum size in bytes of the ``ptr`` allocation (``data`` should be ``None``)
                    device (Devicelike): Device the array lives on
                    copy: Whether the incoming ``data`` will be copied or aliased. Aliasing requires that
                        the incoming ``data`` already lives on the ``device`` specified and the data types match.
                    owner: Whether the array will try to deallocate the underlying memory when it is deleted
                        (deprecated, pass ``deleter`` if you wish to transfer ownership to Warp)
                    deleter: Function to be called when the array is deleted, taking two arguments: pointer and size
                    requires_grad: Whether or not gradients will be tracked for this array, see :class:`warp.Tape` for details
                    grad: The array in which to accumulate gradients in the backward pass. If ``None`` and ``requires_grad`` is ``True``,
                        then a gradient array will be allocated automatically.
                    pinned: Whether to allocate pinned host memory, which allows asynchronous host–device transfers
                        (only applicable with ``device="cpu"``)
        
                
        """
    def __len__(self):
        ...
    def __matmul__(self, other):
        """
        
                Enables A @ B syntax for matrix multiplication
                
        """
    def __str__(self):
        ...
    def _alloc_grad(self):
        ...
    def _init_annotation(self, dtype, ndim):
        ...
    def _init_from_data(self, data, dtype, shape, device, copy, pinned):
        ...
    def _init_from_ptr(self, ptr, dtype, shape, strides, capacity, device, pinned, deleter):
        ...
    def _init_new(self, dtype, shape, strides, device, pinned):
        ...
    def assign(self, src):
        """
        Wraps ``src`` in an :class:`warp.array` if it is not already one and copies the contents to ``self``.
        """
    def contiguous(self):
        """
        Returns a contiguous array with this array's data. No-op if array is already contiguous.
        """
    def cptr(self):
        """
        Return a ctypes cast of the array address.
        
                Notes:
        
                #. Only CPU arrays support this method.
                #. The array must be contiguous.
                #. Accesses to this object are **not** bounds checked.
                #. For ``float16`` types, a pointer to the internal ``uint16`` representation is returned.
                
        """
    def fill_(self, value):
        """
        Set all array entries to `value`
        
                args:
                    value: The value to set every array entry to. Must be convertible to the array's ``dtype``.
        
                Raises:
                    ValueError: If `value` cannot be converted to the array's ``dtype``.
        
                Examples:
                    ``fill_()`` can take lists or other sequences when filling arrays of vectors or matrices.
        
                    >>> arr = wp.zeros(2, dtype=wp.mat22)
                    >>> arr.numpy()
                    array([[[0., 0.],
                            [0., 0.]],
                    <BLANKLINE>
                           [[0., 0.],
                            [0., 0.]]], dtype=float32)
                    >>> arr.fill_([[1, 2], [3, 4]])
                    >>> arr.numpy()
                    array([[[1., 2.],
                            [3., 4.]],
                    <BLANKLINE>
                           [[1., 2.],
                            [3., 4.]]], dtype=float32)
                
        """
    def flatten(self):
        """
        Returns a zero-copy view of the array collapsed to 1-D. Only supported for contiguous arrays.
        """
    def list(self):
        """
        Returns a flattened list of items in the array as a Python list.
        """
    def mark_init(self):
        """
        Resets this array's read flag
        """
    def mark_read(self):
        """
        Marks this array as having been read from in a kernel or recorded function on the tape.
        """
    def mark_write(self, **kwargs):
        """
        Detect if we are writing to an array that has already been read from
        """
    def numpy(self):
        """
        Converts the array to a :class:`numpy.ndarray` (aliasing memory through the array interface protocol)
                If the array is on the GPU, a synchronous device-to-host copy (on the CUDA default stream) will be
                automatically performed to ensure that any outstanding work is completed.
                
        """
    def reshape(self, shape):
        """
        Returns a reshaped array. Only supported for contiguous arrays.
        
                Args:
                    shape : An int or tuple of ints specifying the shape of the returned array.
                
        """
    def to(self, device, requires_grad = None):
        """
        Returns a Warp array with this array's data moved to the specified device, no-op if already on device.
        """
    def transpose(self, axes = None):
        """
        Returns an zero-copy view of the array with axes transposed.
        
                Note: The transpose operation will return an array with a non-contiguous access pattern.
        
                Args:
                    axes (optional): Specifies the how the axes are permuted. If not specified, the axes order will be reversed.
                
        """
    def view(self, dtype):
        """
        Returns a zero-copy view of this array's memory with a different data type.
                ``dtype`` must have the same byte size of the array's native ``dtype``.
                
        """
    def zero_(self):
        """
        Zeroes-out the array entries.
        """
    @property
    def __array_interface__(self):
        ...
    @property
    def __cuda_array_interface__(self):
        ...
    @property
    def requires_grad(self):
        ...
    @requires_grad.setter
    def requires_grad(self, value: builtins.bool):
        ...
    @property
    def vars(self):
        ...
class array_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('data', ctypes.c_ulong), ('grad', ctypes.c_ulong), ('shape', c_int_Array_4), ('strides', c_int_Array_4), ('ndim', ctypes.c_int)]
    _numpy_dtype_: typing.ClassVar[dict] = {'names': ['data', 'grad', 'shape', 'strides', 'ndim'], 'formats': ['u8', 'u8', '4i4', '4i4', 'i4'], 'offsets': [0, 8, 16, 32, 48], 'itemsize': 56}
    @classmethod
    def numpy_dtype(cls):
        ...
    def __init__(self, data = 0, grad = 0, ndim = 0, shape = (0), strides = (0)):
        ...
    def numpy_value(self):
        ...
class bool:
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_bool
    def __bool__(self) -> builtins.bool:
        ...
    def __float__(self) -> float:
        ...
    def __init__(self, x = False):
        ...
    def __int__(self) -> int:
        ...
class bvh_query_t:
    """
    Object used to track state during BVH traversal.
    """
    def __init__(self):
        ...
class float16(float_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_ushort
class float32(float_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_float
class float64(float_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_double
class float_base(scalar_base):
    pass
class hash_grid_query_t:
    """
    Object used to track state during neighbor traversal.
    """
    def __init__(self):
        ...
class indexedarray(noncontiguous_array_base):
    __orig_bases__: typing.ClassVar[tuple]  # value = (warp.types.noncontiguous_array_base[~T])
    __parameters__: typing.ClassVar[tuple]  # value = (~T)
    _vars = None
    def __ctype__(self):
        ...
    def __init__(self, data: array = None, indices: array | list[array] = None, dtype = None, ndim = None):
        ...
    def __len__(self):
        ...
    def __str__(self):
        ...
    @property
    def vars(self):
        ...
class indexedarray_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('data', array_t), ('indices', c_void_p_Array_4), ('shape', c_int_Array_4)]
    def __init__(self, data, indices, shape):
        ...
class int16(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_short
class int32(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_int
class int64(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_long
class int8(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_byte
class int_base(scalar_base):
    def __index__(self) -> int:
        ...
class launch_bounds_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('shape', c_int_Array_4), ('ndim', ctypes.c_int), ('size', ctypes.c_ulong)]
    def __init__(self, shape):
        ...
class mat22d(matrix.<locals>.mat_t):
    pass
class mat22f(matrix.<locals>.mat_t):
    pass
class mat22h(matrix.<locals>.mat_t):
    pass
class mat33d(matrix.<locals>.mat_t):
    pass
class mat33f(matrix.<locals>.mat_t):
    pass
class mat33h(matrix.<locals>.mat_t):
    pass
class mat44d(matrix.<locals>.mat_t):
    pass
class mat44f(matrix.<locals>.mat_t):
    pass
class mat44h(matrix.<locals>.mat_t):
    pass
class mesh_query_aabb_t:
    """
    Object used to track state during mesh traversal.
    """
    def __init__(self):
        ...
class mesh_query_point_t:
    """
    Output for the mesh query point functions.
    
        Attributes:
            result (bool): Whether a point is found within the given constraints.
            sign (float32): A value < 0 if query point is inside the mesh, >=0 otherwise.
                            Note that mesh must be watertight for this to be robust
            face (int32): Index of the closest face.
            u (float32): Barycentric u coordinate of the closest point.
            v (float32): Barycentric v coordinate of the closest point.
    
        See Also:
            :func:`mesh_query_point`, :func:`mesh_query_point_no_sign`,
            :func:`mesh_query_furthest_point_no_sign`,
            :func:`mesh_query_point_sign_normal`,
            and :func:`mesh_query_point_sign_winding_number`.
        
    """
    class Var:
        @staticmethod
        def type_to_ctype(t, value_type = False):
            ...
        def __init__(self, label, type, requires_grad = False, constant = None, prefix = True):
            ...
        def __str__(self):
            ...
        def ctype(self, value_type = False):
            ...
        def emit(self, prefix: str = 'var'):
            ...
        def emit_adj(self):
            ...
        def mark_read(self):
            """
            Marks this Var as having been read from in a kernel (array only).
            """
        def mark_write(self, **kwargs):
            """
            Marks this Var has having been written to in a kernel (array only).
            """
    vars: typing.ClassVar[dict]  # value = {'result': <warp.codegen.Var object>, 'sign': <warp.codegen.Var object>, 'face': <warp.codegen.Var object>, 'u': <warp.codegen.Var object>, 'v': <warp.codegen.Var object>}
class mesh_query_ray_t:
    """
    Output for the mesh query ray functions.
    
        Attributes:
            result (bool): Whether a hit is found within the given constraints.
            sign (float32): A value > 0 if the ray hit in front of the face, returns < 0 otherwise.
            face (int32): Index of the closest face.
            t (float32): Distance of the closest hit along the ray.
            u (float32): Barycentric u coordinate of the closest hit.
            v (float32): Barycentric v coordinate of the closest hit.
            normal (vec3f): Face normal.
    
        See Also:
            :func:`mesh_query_ray`.
        
    """
    class Var:
        @staticmethod
        def type_to_ctype(t, value_type = False):
            ...
        def __init__(self, label, type, requires_grad = False, constant = None, prefix = True):
            ...
        def __str__(self):
            ...
        def ctype(self, value_type = False):
            ...
        def emit(self, prefix: str = 'var'):
            ...
        def emit_adj(self):
            ...
        def mark_read(self):
            """
            Marks this Var as having been read from in a kernel (array only).
            """
        def mark_write(self, **kwargs):
            """
            Marks this Var has having been written to in a kernel (array only).
            """
    vars: typing.ClassVar[dict]  # value = {'result': <warp.codegen.Var object>, 'sign': <warp.codegen.Var object>, 'face': <warp.codegen.Var object>, 't': <warp.codegen.Var object>, 'u': <warp.codegen.Var object>, 'v': <warp.codegen.Var object>, 'normal': <warp.codegen.Var object>}
class noncontiguous_array_base(typing.Generic):
    __orig_bases__: typing.ClassVar[tuple]  # value = (typing.Generic[~T])
    __parameters__: typing.ClassVar[tuple]  # value = (~T)
    def __init__(self, array_type_id):
        ...
    def assign(self, src):
        ...
    def contiguous(self):
        ...
    def fill_(self, value):
        ...
    def list(self):
        ...
    def numpy(self):
        ...
    def to(self, device):
        ...
    def zero_(self):
        ...
class quatd(quaternion.<locals>.quat_t):
    pass
class quatf(quaternion.<locals>.quat_t):
    pass
class quath(quaternion.<locals>.quat_t):
    pass
class range_t:
    def __init__(self):
        ...
class scalar_base:
    def __add__(self, y):
        ...
    def __bool__(self) -> builtins.bool:
        ...
    def __float__(self) -> float:
        ...
    def __init__(self, x = 0):
        ...
    def __int__(self) -> int:
        ...
    def __mod__(self, x):
        ...
    def __mul__(self, y):
        ...
    def __neg__(self):
        ...
    def __pos__(self):
        ...
    def __radd__(self, y):
        ...
    def __rmod__(self, x):
        ...
    def __rmul__(self, x):
        ...
    def __rsub__(self, y):
        ...
    def __rtruediv__(self, x):
        ...
    def __sub__(self, y):
        ...
    def __truediv__(self, y):
        ...
class shape_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('dims', c_int_Array_4)]
    def __init__(self):
        ...
class spatial_matrixd(matrix.<locals>.mat_t):
    pass
class spatial_matrixf(matrix.<locals>.mat_t):
    pass
class spatial_matrixh(matrix.<locals>.mat_t):
    pass
class spatial_vectord(vector.<locals>.vec_t):
    pass
class spatial_vectorf(vector.<locals>.vec_t):
    pass
class spatial_vectorh(vector.<locals>.vec_t):
    pass
class transformd(transformation.<locals>.transform_t):
    pass
class transformf(transformation.<locals>.transform_t):
    pass
class transformh(transformation.<locals>.transform_t):
    pass
class uint16(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_ushort
class uint32(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_uint
class uint64(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_ulong
class uint8(int_base):
    _length_: typing.ClassVar[int] = 1
    _type_ = ctypes.c_ubyte
class vec2b(vector.<locals>.vec_t):
    pass
class vec2d(vector.<locals>.vec_t):
    pass
class vec2f(vector.<locals>.vec_t):
    pass
class vec2h(vector.<locals>.vec_t):
    pass
class vec2i(vector.<locals>.vec_t):
    pass
class vec2l(vector.<locals>.vec_t):
    pass
class vec2s(vector.<locals>.vec_t):
    pass
class vec2ub(vector.<locals>.vec_t):
    pass
class vec2ui(vector.<locals>.vec_t):
    pass
class vec2ul(vector.<locals>.vec_t):
    pass
class vec2us(vector.<locals>.vec_t):
    pass
class vec3b(vector.<locals>.vec_t):
    pass
class vec3d(vector.<locals>.vec_t):
    pass
class vec3f(vector.<locals>.vec_t):
    pass
class vec3h(vector.<locals>.vec_t):
    pass
class vec3i(vector.<locals>.vec_t):
    pass
class vec3l(vector.<locals>.vec_t):
    pass
class vec3s(vector.<locals>.vec_t):
    pass
class vec3ub(vector.<locals>.vec_t):
    pass
class vec3ui(vector.<locals>.vec_t):
    pass
class vec3ul(vector.<locals>.vec_t):
    pass
class vec3us(vector.<locals>.vec_t):
    pass
class vec4b(vector.<locals>.vec_t):
    pass
class vec4d(vector.<locals>.vec_t):
    pass
class vec4f(vector.<locals>.vec_t):
    pass
class vec4h(vector.<locals>.vec_t):
    pass
class vec4i(vector.<locals>.vec_t):
    pass
class vec4l(vector.<locals>.vec_t):
    pass
class vec4s(vector.<locals>.vec_t):
    pass
class vec4ub(vector.<locals>.vec_t):
    pass
class vec4ui(vector.<locals>.vec_t):
    pass
class vec4ul(vector.<locals>.vec_t):
    pass
class vec4us(vector.<locals>.vec_t):
    pass
class void:
    def __init__(self):
        ...
def _is_contiguous_vec_like_array(array, vec_length: int, scalar_types: tuple[type]) -> bool:
    ...
def adj_batched_matmul(a: array3d, b: array3d, c: array3d, adj_a: array3d, adj_b: array3d, adj_c: array3d, adj_d: array3d, alpha: float = 1.0, beta: float = 0.0, allow_tf32x3_arith: builtins.bool = False):
    """
    Computes the adjoint of a batched generic matrix-matrix multiplication (GEMM) of the form: `d = alpha * (a @ b) + beta * c`.
    
        Args:
            a (array3d): three-dimensional array containing A matrices. Overall array dimension is {batch_count, M, K}
            b (array3d): three-dimensional array containing B matrices. Overall array dimension is {batch_count, K, N}
            c (array3d): three-dimensional array containing C matrices. Overall array dimension is {batch_count, M, N}
            adj_a (array3d): three-dimensional array to which the adjoints of A matrices are written. Overall array dimension is {batch_count, M, K}
            adj_b (array3d): three-dimensional array to which the adjoints of B matrices are written. Overall array dimension is {batch_count, K, N}
            adj_c (array3d): three-dimensional array to which the adjoints of C matrices are written. Overall array dimension is {batch_count, M, N}
            adj_d (array3d): three-dimensional array containing adjoints of D matrices. Overall array dimension is {batch_count, M, N}
            alpha (float): parameter alpha of GEMM
            beta (float): parameter beta of GEMM
            allow_tf32x3_arith (bool): whether to use CUTLASS's 3xTF32 GEMMs, which enable accuracy similar to FP32
                                       while using Tensor Cores
        
    """
def adj_matmul(a: array2d, b: array2d, c: array2d, adj_a: array2d, adj_b: array2d, adj_c: array2d, adj_d: array2d, alpha: float = 1.0, beta: float = 0.0, allow_tf32x3_arith: builtins.bool = False):
    """
    Computes the adjoint of a generic matrix-matrix multiplication (GEMM) of the form: `d = alpha * (a @ b) + beta * c`.
            note: the adjoint of parameter alpha is not included but can be computed as `adj_alpha = np.sum(np.concatenate(np.multiply(a @ b, adj_d)))`.
            note: the adjoint of parameter beta is not included but can be computed as `adj_beta = np.sum(np.concatenate(np.multiply(c, adj_d)))`.
    
        Args:
            a (array2d): two-dimensional array containing matrix A
            b (array2d): two-dimensional array containing matrix B
            c (array2d): two-dimensional array containing matrix C
            adj_a (array2d): two-dimensional array to which the adjoint of matrix A is written
            adj_b (array2d): two-dimensional array to which the adjoint of matrix B is written
            adj_c (array2d): two-dimensional array to which the adjoint of matrix C is written
            adj_d (array2d): two-dimensional array containing the adjoint of matrix D
            alpha (float): parameter alpha of GEMM
            beta (float): parameter beta of GEMM
            allow_tf32x3_arith (bool): whether to use CUTLASS's 3xTF32 GEMMs, which enable accuracy similar to FP32
                                       while using Tensor Cores
        
    """
def array1d(*args, **kwargs):
    ...
def array2d(*args, **kwargs):
    ...
def array3d(*args, **kwargs):
    ...
def array4d(*args, **kwargs):
    ...
def array_ctype_from_interface(interface: dict, dtype = None, owner = None):
    """
    Get native array descriptor (array_t) from __array_interface__ or __cuda_array_interface__ dictionary
    """
def array_type_id(a):
    ...
def batched_matmul(a: array3d, b: array3d, c: array3d, d: array3d, alpha: float = 1.0, beta: float = 0.0, allow_tf32x3_arith: builtins.bool = False):
    """
    Computes a batched generic matrix-matrix multiplication (GEMM) of the form: `d = alpha * (a @ b) + beta * c`.
    
        Args:
            a (array3d): three-dimensional array containing A matrices. Overall array dimension is {batch_count, M, K}
            b (array3d): three-dimensional array containing B matrices. Overall array dimension is {batch_count, K, N}
            c (array3d): three-dimensional array containing C matrices. Overall array dimension is {batch_count, M, N}
            d (array3d): three-dimensional array to which output D is written. Overall array dimension is {batch_count, M, N}
            alpha (float): parameter alpha of GEMM
            beta (float): parameter beta of GEMM
            allow_tf32x3_arith (bool): whether to use CUTLASS's 3xTF32 GEMMs, which enable accuracy similar to FP32
                                       while using Tensor Cores
        
    """
def check_array_shape(shape: tuple):
    """
    Checks that the size in each dimension is positive and less than 2^32.
    """
def check_index_array(indices, expected_device):
    ...
def constant(x):
    """
    Function to declare compile-time constants accessible from Warp kernels
    
        Args:
            x: Compile-time constant value, can be any of the built-in math types.
        
    """
def dtype_from_numpy(numpy_dtype):
    """
    Return the Warp dtype corresponding to a NumPy dtype.
    """
def dtype_to_numpy(warp_dtype):
    """
    Return the NumPy dtype corresponding to a Warp dtype.
    """
def float_to_half_bits(value):
    ...
def from_ptr(ptr, length, dtype = None, shape = None, device = None):
    ...
def get_signature(arg_types, func_name = None, arg_names = None):
    ...
def get_type_code(arg_type):
    ...
def half_bits_to_float(value):
    ...
def indexedarray1d(*args, **kwargs):
    ...
def indexedarray2d(*args, **kwargs):
    ...
def indexedarray3d(*args, **kwargs):
    ...
def indexedarray4d(*args, **kwargs):
    ...
def infer_argument_types(args, template_types, arg_names = None):
    """
    Resolve argument types with the given list of template types.
    """
def is_array(a):
    ...
def is_float(x):
    ...
def is_generic_signature(sig):
    ...
def is_int(x):
    ...
def is_tile(t):
    ...
def is_value(x):
    ...
def matmul(a: array2d, b: array2d, c: array2d, d: array2d, alpha: float = 1.0, beta: float = 0.0, allow_tf32x3_arith: builtins.bool = False):
    """
    Computes a generic matrix-matrix multiplication (GEMM) of the form: `d = alpha * (a @ b) + beta * c`.
    
        Args:
            a (array2d): two-dimensional array containing matrix A
            b (array2d): two-dimensional array containing matrix B
            c (array2d): two-dimensional array containing matrix C
            d (array2d): two-dimensional array to which output D is written
            alpha (float): parameter alpha of GEMM
            beta (float): parameter beta of GEMM
            allow_tf32x3_arith (bool): whether to use CUTLASS's 3xTF32 GEMMs, which enable accuracy similar to FP32
                                       while using Tensor Cores
        
    """
def matrix(shape, dtype):
    ...
def quaternion(dtype = ...):
    ...
def scalars_equal(a, b, match_generic):
    ...
def strides_from_shape(shape: tuple, dtype):
    ...
def transformation(dtype = ...):
    ...
def type_ctype(dtype):
    ...
def type_is_float(t):
    ...
def type_is_generic(t):
    ...
def type_is_generic_scalar(t):
    ...
def type_is_int(t):
    ...
def type_is_matrix(t):
    ...
def type_is_quaternion(t):
    ...
def type_is_value(x):
    ...
def type_is_vector(t):
    ...
def type_length(dtype):
    ...
def type_matches_template(arg_type, template_type):
    """
    Check if an argument type matches a template.
    
        This function is used to test whether the arguments passed to a generic @wp.kernel or @wp.func
        match the template type annotations.  The template_type can be generic, but the arg_type must be concrete.
        
    """
def type_repr(t):
    ...
def type_scalar_type(dtype):
    ...
def type_size_in_bytes(dtype):
    ...
def type_to_warp(dtype):
    ...
def type_typestr(dtype):
    ...
def types_equal(a, b, match_generic = False):
    ...
def vector(length, dtype):
    ...
ARRAY_MAX_DIMS: int = 4
ARRAY_TYPE_FABRIC: int = 2
ARRAY_TYPE_FABRIC_INDEXED: int = 3
ARRAY_TYPE_INDEXED: int = 1
ARRAY_TYPE_REGULAR: int = 0
Cols: typing.TypeVar  # value = ~Cols
DType: typing.TypeVar  # value = ~DType
Float: typing.TypeVar  # value = ~Float
Int: typing.TypeVar  # value = ~Int
LAUNCH_MAX_DIMS: int = 4
Length: typing.TypeVar  # value = ~Length
Rows: typing.TypeVar  # value = ~Rows
Scalar: typing.TypeVar  # value = ~Scalar
T: typing.TypeVar  # value = ~T
_type_size_cache: dict = {float: 4, int: 4}
array_types: tuple = (array, indexedarray, warp.fabric.fabricarray, warp.fabric.indexedfabricarray)
float_types: tuple = (float16, float32, float64)
generic_types: tuple  # value = (typing.Any, ~Scalar, ~Float, ~Int)
int_tuple_type_hints: dict  # value = {typing.Tuple[int]: 1, typing.Tuple[int, int]: 2, typing.Tuple[int, int, int]: 3, typing.Tuple[int, int, int, int]: 4, typing.Tuple[int, ...]: -1}
int_types: tuple = (int8, uint8, int16, uint16, int32, uint32, int64, uint64)
non_atomic_types: tuple = (int8, uint8, int16, uint16, int64)
np_dtype_to_warp_type: dict  # value = {numpy.bool_: bool, numpy.int8: int8, numpy.uint8: uint8, numpy.int16: int16, numpy.uint16: uint16, numpy.int32: int32, numpy.int64: int64, numpy.uint32: uint32, numpy.uint64: uint64, numpy.float16: float16, numpy.float32: float32, numpy.float64: float64, dtype('bool'): bool, dtype('int8'): int8, dtype('uint8'): uint8, dtype('int16'): int16, dtype('uint16'): uint16, dtype('int32'): int32, dtype('int64'): int64, dtype('uint32'): uint32, dtype('uint64'): uint64, dtype('float16'): float16, dtype('float32'): float32, dtype('float64'): float64}
scalar_and_bool_types: tuple = (int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float32, float64, bool)
scalar_types: tuple = (int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float32, float64)
simple_type_codes: dict = {int: 'i4', float: 'f4', bool: 'b', bool: 'b', str: 'str', int8: 'i1', int16: 'i2', int32: 'i4', int64: 'i8', uint8: 'u1', uint16: 'u2', uint32: 'u4', uint64: 'u8', float16: 'f2', float32: 'f4', float64: 'f8', shape_t: 'sh', range_t: 'rg', launch_bounds_t: 'lb', hash_grid_query_t: 'hgq', mesh_query_aabb_t: 'mqa', mesh_query_point_t: 'mqp', mesh_query_ray_t: 'mqr', bvh_query_t: 'bvhq'}
value_types: tuple = (int, float, bool, int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float32, float64)
vector_types: tuple = (vec2b, vec2ub, vec2s, vec2us, vec2i, vec2ui, vec2l, vec2ul, vec2h, vec2f, vec2d, vec3b, vec3ub, vec3s, vec3us, vec3i, vec3ui, vec3l, vec3ul, vec3h, vec3f, vec3d, vec4b, vec4ub, vec4s, vec4us, vec4i, vec4ui, vec4l, vec4ul, vec4h, vec4f, vec4d, mat22h, mat22f, mat22d, mat33h, mat33f, mat33d, mat44h, mat44f, mat44d, quath, quatf, quatd, transformh, transformf, transformd, spatial_vectorh, spatial_vectorf, spatial_vectord, spatial_matrixh, spatial_matrixf, spatial_matrixd)
warp_type_to_np_dtype: dict = {bool: numpy.bool_, int8: numpy.int8, int16: numpy.int16, int32: numpy.int32, int64: numpy.int64, uint8: numpy.uint8, uint16: numpy.uint16, uint32: numpy.uint32, uint64: numpy.uint64, float16: numpy.float16, float32: numpy.float32, float64: numpy.float64}
BvhQuery = bvh_query_t
HashGridQuery = hash_grid_query_t
MeshQueryAABB = mesh_query_aabb_t
MeshQueryPoint = mesh_query_point_t
MeshQueryRay = mesh_query_ray_t
mat22 = mat22f
mat33 = mat33f
mat44 = mat44f
quat = quatf
spatial_matrix = spatial_matrixf
spatial_vector = spatial_vectorf
transform = transformf
vec2 = vec2f
vec3 = vec3f
vec4 = vec4f
