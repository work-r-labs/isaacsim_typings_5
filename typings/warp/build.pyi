from __future__ import annotations
import builtins as builtins
import ctypes as ctypes
import errno as errno
import hashlib as hashlib
import inspect as inspect
import json as json
import numpy
import numpy as np
from numpy import typing as npt
import os as os
from pathlib import Path
import struct as struct
import time as time
import typing
from typing import Any
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
from typing import get_args
from typing import get_origin
import warp as warp
from warp.fabric import fabricarray
from warp.fabric import indexedfabricarray
from warp.thirdparty import appdirs
from warp.types import Array
from warp.types import Bvh
from warp.types import HashGrid
from warp.types import MarchingCubes
from warp.types import Matrix
from warp.types import Mesh
from warp.types import Quaternion
from warp.types import Tile
from warp.types import TileBinaryMap
from warp.types import TileConstant
from warp.types import TileLoad
from warp.types import TileOnes
from warp.types import TileRange
from warp.types import TileShared
from warp.types import TileUnaryMap
from warp.types import TileZeros
from warp.types import Transformation
from warp.types import Vector
from warp.types import Volume
from warp.types import adj_batched_matmul
from warp.types import adj_matmul
from warp.types import array
from warp.types import array1d
from warp.types import array2d
from warp.types import array3d
from warp.types import array4d
from warp.types import array_ctype_from_interface
from warp.types import array_t
from warp.types import array_type_id
from warp.types import batched_matmul
from warp.types import bool
from warp.types import bvh_query_t as BvhQuery
from warp.types import bvh_query_t
from warp.types import check_array_shape
from warp.types import check_index_array
from warp.types import constant
from warp.types import dtype_from_numpy
from warp.types import dtype_to_numpy
from warp.types import float16
from warp.types import float32
from warp.types import float64
from warp.types import float_base
from warp.types import float_to_half_bits
from warp.types import from_ipc_handle
from warp.types import from_ptr
from warp.types import get_signature
from warp.types import get_type_code
from warp.types import half_bits_to_float
from warp.types import hash_grid_query_t as HashGridQuery
from warp.types import hash_grid_query_t
from warp.types import indexedarray
from warp.types import indexedarray1d
from warp.types import indexedarray2d
from warp.types import indexedarray3d
from warp.types import indexedarray4d
from warp.types import indexedarray_t
from warp.types import infer_argument_types
from warp.types import int16
from warp.types import int32
from warp.types import int64
from warp.types import int8
from warp.types import int_base
from warp.types import is_array
from warp.types import is_float
from warp.types import is_generic_signature
from warp.types import is_int
from warp.types import is_tile
from warp.types import is_value
from warp.types import launch_bounds_t
from warp.types import mat22d
from warp.types import mat22f as mat22
from warp.types import mat22f
from warp.types import mat22h
from warp.types import mat33d
from warp.types import mat33f as mat33
from warp.types import mat33f
from warp.types import mat33h
from warp.types import mat44d
from warp.types import mat44f
from warp.types import mat44f as mat44
from warp.types import mat44h
from warp.types import matmul
from warp.types import matrix
from warp.types import mesh_query_aabb_t
from warp.types import mesh_query_aabb_t as MeshQueryAABB
from warp.types import mesh_query_point_t
from warp.types import mesh_query_point_t as MeshQueryPoint
from warp.types import mesh_query_ray_t
from warp.types import mesh_query_ray_t as MeshQueryRay
from warp.types import noncontiguous_array_base
from warp.types import quatd
from warp.types import quaternion
from warp.types import quatf as quat
from warp.types import quatf
from warp.types import quath
from warp.types import range_t
from warp.types import scalar_base
from warp.types import scalar_short_name
from warp.types import scalars_equal
from warp.types import shape_t
from warp.types import spatial_matrixd
from warp.types import spatial_matrixf
from warp.types import spatial_matrixf as spatial_matrix
from warp.types import spatial_matrixh
from warp.types import spatial_vectord
from warp.types import spatial_vectorf as spatial_vector
from warp.types import spatial_vectorf
from warp.types import spatial_vectorh
from warp.types import strides_from_shape
from warp.types import transformation
from warp.types import transformd
from warp.types import transformf as transform
from warp.types import transformf
from warp.types import transformh
from warp.types import type_ctype
from warp.types import type_is_float
from warp.types import type_is_generic
from warp.types import type_is_generic_scalar
from warp.types import type_is_int
from warp.types import type_is_matrix
from warp.types import type_is_quaternion
from warp.types import type_is_transformation
from warp.types import type_is_value
from warp.types import type_is_vector
from warp.types import type_length
from warp.types import type_matches_template
from warp.types import type_repr
from warp.types import type_scalar_type
from warp.types import type_size_in_bytes
from warp.types import type_to_warp
from warp.types import type_typestr
from warp.types import types_equal
from warp.types import uint16
from warp.types import uint32
from warp.types import uint64
from warp.types import uint8
from warp.types import vec2b
from warp.types import vec2d
from warp.types import vec2f
from warp.types import vec2f as vec2
from warp.types import vec2h
from warp.types import vec2i
from warp.types import vec2l
from warp.types import vec2s
from warp.types import vec2ub
from warp.types import vec2ui
from warp.types import vec2ul
from warp.types import vec2us
from warp.types import vec3b
from warp.types import vec3d
from warp.types import vec3f
from warp.types import vec3f as vec3
from warp.types import vec3h
from warp.types import vec3i
from warp.types import vec3l
from warp.types import vec3s
from warp.types import vec3ub
from warp.types import vec3ui
from warp.types import vec3ul
from warp.types import vec3us
from warp.types import vec4b
from warp.types import vec4d
from warp.types import vec4f as vec4
from warp.types import vec4f
from warp.types import vec4h
from warp.types import vec4i
from warp.types import vec4l
from warp.types import vec4s
from warp.types import vec4ub
from warp.types import vec4ui
from warp.types import vec4ul
from warp.types import vec4us
from warp.types import vector
from warp.types import void
import zlib as zlib
__all__: list[str] = ['ARRAY_MAX_DIMS', 'ARRAY_TYPE_FABRIC', 'ARRAY_TYPE_FABRIC_INDEXED', 'ARRAY_TYPE_INDEXED', 'ARRAY_TYPE_REGULAR', 'Any', 'Array', 'Bvh', 'BvhQuery', 'Cols', 'DType', 'Float', 'Generic', 'HashGrid', 'HashGridQuery', 'Int', 'LAUNCH_MAX_DIMS', 'Length', 'MarchingCubes', 'Matrix', 'Mesh', 'MeshQueryAABB', 'MeshQueryPoint', 'MeshQueryRay', 'NamedTuple', 'Path', 'Quaternion', 'Rows', 'Scalar', 'T', 'Tile', 'TileBinaryMap', 'TileConstant', 'TileLoad', 'TileOnes', 'TileRange', 'TileShared', 'TileUnaryMap', 'TileZeros', 'Transformation', 'TypeVar', 'Vector', 'Volume', 'adj_batched_matmul', 'adj_matmul', 'appdirs', 'array', 'array1d', 'array2d', 'array3d', 'array4d', 'array_ctype_from_interface', 'array_t', 'array_type_id', 'array_types', 'batched_matmul', 'bool', 'build_cpu', 'build_cuda', 'build_lto_dot', 'build_lto_fft', 'build_lto_solver', 'builtins', 'bvh_constructor_values', 'bvh_query_t', 'check_array_shape', 'check_index_array', 'clear_kernel_cache', 'clear_lto_cache', 'constant', 'ctypes', 'dtype_from_numpy', 'dtype_to_numpy', 'errno', 'fabricarray', 'float16', 'float32', 'float64', 'float_base', 'float_to_half_bits', 'float_types', 'from_ipc_handle', 'from_ptr', 'generic_types', 'get_args', 'get_cached_lto', 'get_cached_lto_meta', 'get_lto_cache_dir', 'get_origin', 'get_signature', 'get_type_code', 'half_bits_to_float', 'hash_grid_query_t', 'hash_symbol', 'hashlib', 'indexedarray', 'indexedarray1d', 'indexedarray2d', 'indexedarray3d', 'indexedarray4d', 'indexedarray_t', 'indexedfabricarray', 'infer_argument_types', 'init_kernel_cache', 'inspect', 'int16', 'int32', 'int64', 'int8', 'int_base', 'int_tuple_type_hints', 'int_types', 'is_array', 'is_float', 'is_generic_signature', 'is_int', 'is_tile', 'is_value', 'json', 'launch_bounds_t', 'load_cuda', 'mat22', 'mat22d', 'mat22f', 'mat22h', 'mat33', 'mat33d', 'mat33f', 'mat33h', 'mat44', 'mat44d', 'mat44f', 'mat44h', 'matmul', 'matrix', 'mesh_query_aabb_t', 'mesh_query_point_t', 'mesh_query_ray_t', 'non_atomic_types', 'noncontiguous_array_base', 'np', 'np_dtype_to_warp_type', 'npt', 'nvJitLink_input_type', 'os', 'quat', 'quatd', 'quaternion', 'quatf', 'quath', 'range_t', 'safe_rename', 'scalar_and_bool_types', 'scalar_base', 'scalar_short_name', 'scalar_types', 'scalars_equal', 'shape_t', 'simple_type_codes', 'spatial_matrix', 'spatial_matrixd', 'spatial_matrixf', 'spatial_matrixh', 'spatial_vector', 'spatial_vectord', 'spatial_vectorf', 'spatial_vectorh', 'strides_from_shape', 'struct', 'time', 'transform', 'transformation', 'transformd', 'transformf', 'transformh', 'type_ctype', 'type_is_float', 'type_is_generic', 'type_is_generic_scalar', 'type_is_int', 'type_is_matrix', 'type_is_quaternion', 'type_is_transformation', 'type_is_value', 'type_is_vector', 'type_length', 'type_matches_template', 'type_repr', 'type_scalar_type', 'type_size_in_bytes', 'type_to_warp', 'type_typestr', 'types_equal', 'uint16', 'uint32', 'uint64', 'uint8', 'value_types', 'vec2', 'vec2b', 'vec2d', 'vec2f', 'vec2h', 'vec2i', 'vec2l', 'vec2s', 'vec2ub', 'vec2ui', 'vec2ul', 'vec2us', 'vec3', 'vec3b', 'vec3d', 'vec3f', 'vec3h', 'vec3i', 'vec3l', 'vec3s', 'vec3ub', 'vec3ui', 'vec3ul', 'vec3us', 'vec4', 'vec4b', 'vec4d', 'vec4f', 'vec4h', 'vec4i', 'vec4l', 'vec4s', 'vec4ub', 'vec4ui', 'vec4ul', 'vec4us', 'vector', 'vector_types', 'void', 'warp', 'warp_type_to_np_dtype', 'zlib']
def build_cpu(obj_path, cpp_path, mode = 'release', verify_fp = False, fast_math = False, fuse_fp = True):
    ...
def build_cuda(cu_path, arch, output_path, config = 'release', verify_fp = False, fast_math = False, fuse_fp = True, lineinfo = False, ltoirs = None, fatbins = None) -> None:
    ...
def build_lto_dot(M, N, K, adtype, bdtype, cdtype, alayout, blayout, clayout, arch, num_threads, builder):
    ...
def build_lto_fft(arch, size, ept, direction, dir, precision, builder):
    ...
def build_lto_solver(M, N, solver, solver_enum, fill_mode, arch, precision_enum, num_threads, parameter_list, builder):
    ...
def clear_kernel_cache() -> None:
    """
    Clear the kernel cache directory of previously generated source code and compiler artifacts.
    
        Only directories beginning with ``wp_`` will be deleted.
        This function only clears the cache for the current Warp version.
        LTO artifacts are not affected.
        
    """
def clear_lto_cache() -> None:
    """
    Clear the LTO cache directory of previously generated LTO code.
    
        The LTO cache is stored within a subdirectory of the kernel cache directory.
        This function only clears the cache for the current Warp version.
        
    """
def get_cached_lto(path):
    ...
def get_cached_lto_meta(path, symbol):
    ...
def get_lto_cache_dir():
    ...
def hash_symbol(symbol):
    ...
def init_kernel_cache(path = None):
    """
    Initialize kernel cache directory.
    
        This function is used during Warp initialization, but it can also be called directly to change the cache location.
        If the path is not explicitly specified, a default location will be chosen based on OS-specific conventions.
    
        To change the default cache location, set warp.config.kernel_cache_dir before calling warp.init().
        
    """
def load_cuda(input_path, device):
    ...
def safe_rename(src, dst, attempts = 5, delay = 0.1):
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
array_types: tuple = (warp.types.array, warp.types.indexedarray, warp.fabric.fabricarray, warp.fabric.indexedfabricarray)
bvh_constructor_values: dict = {'sah': 0, 'median': 1, 'lbvh': 2}
float_types: tuple = (warp.types.float16, warp.types.float32, warp.types.float64)
generic_types: tuple  # value = (typing.Any, ~Scalar, ~Float, ~Int)
int_tuple_type_hints: dict  # value = {typing.Tuple[int]: 1, typing.Tuple[int, int]: 2, typing.Tuple[int, int, int]: 3, typing.Tuple[int, int, int, int]: 4, typing.Tuple[int, ...]: -1}
int_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64)
non_atomic_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int64)
np_dtype_to_warp_type: dict  # value = {numpy.bool_: warp.types.bool, numpy.int8: warp.types.int8, numpy.uint8: warp.types.uint8, numpy.int16: warp.types.int16, numpy.uint16: warp.types.uint16, numpy.int32: warp.types.int32, numpy.int64: warp.types.int64, numpy.uint32: warp.types.uint32, numpy.uint64: warp.types.uint64, numpy.float16: warp.types.float16, numpy.float32: warp.types.float32, numpy.float64: warp.types.float64, dtype('bool'): warp.types.bool, dtype('int8'): warp.types.int8, dtype('uint8'): warp.types.uint8, dtype('int16'): warp.types.int16, dtype('uint16'): warp.types.uint16, dtype('int32'): warp.types.int32, dtype('int64'): warp.types.int64, dtype('uint32'): warp.types.uint32, dtype('uint64'): warp.types.uint64, dtype('float16'): warp.types.float16, dtype('float32'): warp.types.float32, dtype('float64'): warp.types.float64}
nvJitLink_input_type: dict = {'cubin': 1, 'ptx': 2, 'ltoir': 3, 'fatbin': 4, 'object': 5, 'library': 6}
scalar_and_bool_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64, warp.types.bool)
scalar_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64)
simple_type_codes: dict = {int: 'i4', float: 'f4', bool: 'b', warp.types.bool: 'b', str: 'str', warp.types.int8: 'i1', warp.types.int16: 'i2', warp.types.int32: 'i4', warp.types.int64: 'i8', warp.types.uint8: 'u1', warp.types.uint16: 'u2', warp.types.uint32: 'u4', warp.types.uint64: 'u8', warp.types.float16: 'f2', warp.types.float32: 'f4', warp.types.float64: 'f8', warp.types.shape_t: 'sh', warp.types.range_t: 'rg', warp.types.launch_bounds_t: 'lb', warp.types.hash_grid_query_t: 'hgq', warp.types.mesh_query_aabb_t: 'mqa', warp.types.mesh_query_point_t: 'mqp', warp.types.mesh_query_ray_t: 'mqr', warp.types.bvh_query_t: 'bvhq'}
value_types: tuple = (int, float, bool, warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64, warp.types.bool)
vector_types: tuple = (warp.types.vec2b, warp.types.vec2ub, warp.types.vec2s, warp.types.vec2us, warp.types.vec2i, warp.types.vec2ui, warp.types.vec2l, warp.types.vec2ul, warp.types.vec2h, warp.types.vec2f, warp.types.vec2d, warp.types.vec3b, warp.types.vec3ub, warp.types.vec3s, warp.types.vec3us, warp.types.vec3i, warp.types.vec3ui, warp.types.vec3l, warp.types.vec3ul, warp.types.vec3h, warp.types.vec3f, warp.types.vec3d, warp.types.vec4b, warp.types.vec4ub, warp.types.vec4s, warp.types.vec4us, warp.types.vec4i, warp.types.vec4ui, warp.types.vec4l, warp.types.vec4ul, warp.types.vec4h, warp.types.vec4f, warp.types.vec4d, warp.types.mat22h, warp.types.mat22f, warp.types.mat22d, warp.types.mat33h, warp.types.mat33f, warp.types.mat33d, warp.types.mat44h, warp.types.mat44f, warp.types.mat44d, warp.types.quath, warp.types.quatf, warp.types.quatd, warp.types.transformh, warp.types.transformf, warp.types.transformd, warp.types.spatial_vectorh, warp.types.spatial_vectorf, warp.types.spatial_vectord, warp.types.spatial_matrixh, warp.types.spatial_matrixf, warp.types.spatial_matrixd)
warp_type_to_np_dtype: dict = {warp.types.bool: numpy.bool_, warp.types.int8: numpy.int8, warp.types.int16: numpy.int16, warp.types.int32: numpy.int32, warp.types.int64: numpy.int64, warp.types.uint8: numpy.uint8, warp.types.uint16: numpy.uint16, warp.types.uint32: numpy.uint32, warp.types.uint64: numpy.uint64, warp.types.float16: numpy.float16, warp.types.float32: numpy.float32, warp.types.float64: numpy.float64}
