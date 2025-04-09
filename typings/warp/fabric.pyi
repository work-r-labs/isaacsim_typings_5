from __future__ import annotations
import _ctypes
import builtins as builtins
import ctypes as ctypes
import inspect as inspect
import math as math
import numpy
import numpy as np
from numpy import typing as npt
import struct as struct
import typing
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
import warp as warp
from warp.types import Array
from warp.types import Matrix
from warp.types import Quaternion
from warp.types import Transformation
from warp.types import Vector
from warp.types import array
from warp.types import array1d
from warp.types import array2d
from warp.types import array3d
from warp.types import array4d
from warp.types import array_ctype_from_interface
from warp.types import array_t
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
from warp.types import from_ptr
from warp.types import half_bits_to_float
from warp.types import hash_grid_query_t
from warp.types import hash_grid_query_t as HashGridQuery
from warp.types import indexedarray
from warp.types import indexedarray1d
from warp.types import indexedarray2d
from warp.types import indexedarray3d
from warp.types import indexedarray4d
from warp.types import indexedarray_t
from warp.types import int16
from warp.types import int32
from warp.types import int64
from warp.types import int8
from warp.types import int_base
from warp.types import is_array
from warp.types import is_float
from warp.types import is_int
from warp.types import is_value
from warp.types import launch_bounds_t
from warp.types import mat22d
from warp.types import mat22f as mat22
from warp.types import mat22f
from warp.types import mat22h
from warp.types import mat33d
from warp.types import mat33f
from warp.types import mat33f as mat33
from warp.types import mat33h
from warp.types import mat44d
from warp.types import mat44f as mat44
from warp.types import mat44f
from warp.types import mat44h
from warp.types import matrix
from warp.types import mesh_query_aabb_t as MeshQueryAABB
from warp.types import mesh_query_aabb_t
from warp.types import noncontiguous_array_base
from warp.types import quatd
from warp.types import quaternion
from warp.types import quatf
from warp.types import quatf as quat
from warp.types import quath
from warp.types import range_t
from warp.types import scalar_base
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
from warp.types import transformf
from warp.types import transformf as transform
from warp.types import transformh
from warp.types import type_ctype
from warp.types import type_is_float
from warp.types import type_is_int
from warp.types import type_is_matrix
from warp.types import type_is_quaternion
from warp.types import type_is_value
from warp.types import type_is_vector
from warp.types import type_length
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
from warp.types import vec3f as vec3
from warp.types import vec3f
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
from warp.types import vec4f
from warp.types import vec4f as vec4
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
__all__ = ['ARRAY_MAX_DIMS', 'ARRAY_TYPE_FABRIC', 'ARRAY_TYPE_FABRIC_INDEXED', 'ARRAY_TYPE_INDEXED', 'ARRAY_TYPE_REGULAR', 'Array', 'BvhQuery', 'Cols', 'DType', 'Float', 'Generic', 'HashGridQuery', 'Int', 'LAUNCH_MAX_DIMS', 'Length', 'Matrix', 'MeshQueryAABB', 'NamedTuple', 'Quaternion', 'Rows', 'Scalar', 'T', 'Transformation', 'TypeVar', 'Vector', 'array', 'array1d', 'array2d', 'array3d', 'array4d', 'array_ctype_from_interface', 'array_t', 'bool', 'builtins', 'bvh_query_t', 'check_array_shape', 'check_index_array', 'constant', 'ctypes', 'dtype_from_numpy', 'dtype_to_numpy', 'fabric_to_warp_dtype', 'fabricarray', 'fabricarray_t', 'fabricarrayarray', 'fabricbucket_t', 'float16', 'float32', 'float64', 'float_base', 'float_to_half_bits', 'float_types', 'from_ptr', 'half_bits_to_float', 'hash_grid_query_t', 'indexedarray', 'indexedarray1d', 'indexedarray2d', 'indexedarray3d', 'indexedarray4d', 'indexedarray_t', 'indexedfabricarray', 'indexedfabricarray_t', 'indexedfabricarrayarray', 'inspect', 'int16', 'int32', 'int64', 'int8', 'int_base', 'int_tuple_type_hints', 'int_types', 'is_array', 'is_float', 'is_int', 'is_value', 'launch_bounds_t', 'mat22', 'mat22d', 'mat22f', 'mat22h', 'mat33', 'mat33d', 'mat33f', 'mat33h', 'mat44', 'mat44d', 'mat44f', 'mat44h', 'math', 'matrix', 'mesh_query_aabb_t', 'non_atomic_types', 'noncontiguous_array_base', 'np', 'np_dtype_to_warp_type', 'npt', 'quat', 'quatd', 'quaternion', 'quatf', 'quath', 'range_t', 'scalar_and_bool_types', 'scalar_base', 'scalar_types', 'scalars_equal', 'shape_t', 'spatial_matrix', 'spatial_matrixd', 'spatial_matrixf', 'spatial_matrixh', 'spatial_vector', 'spatial_vectord', 'spatial_vectorf', 'spatial_vectorh', 'strides_from_shape', 'struct', 'transform', 'transformation', 'transformd', 'transformf', 'transformh', 'type_ctype', 'type_is_float', 'type_is_int', 'type_is_matrix', 'type_is_quaternion', 'type_is_value', 'type_is_vector', 'type_length', 'type_repr', 'type_scalar_type', 'type_size_in_bytes', 'type_to_warp', 'type_typestr', 'types_equal', 'uint16', 'uint32', 'uint64', 'uint8', 'value_types', 'vec2', 'vec2b', 'vec2d', 'vec2f', 'vec2h', 'vec2i', 'vec2l', 'vec2s', 'vec2ub', 'vec2ui', 'vec2ul', 'vec2us', 'vec3', 'vec3b', 'vec3d', 'vec3f', 'vec3h', 'vec3i', 'vec3l', 'vec3s', 'vec3ub', 'vec3ui', 'vec3ul', 'vec3us', 'vec4', 'vec4b', 'vec4d', 'vec4f', 'vec4h', 'vec4i', 'vec4l', 'vec4s', 'vec4ub', 'vec4ui', 'vec4ul', 'vec4us', 'vector', 'vector_types', 'void', 'warp', 'warp_type_to_np_dtype', 'zlib']
class fabricarray(warp.types.noncontiguous_array_base):
    __orig_bases__: typing.ClassVar[tuple]  # value = (warp.types.noncontiguous_array_base[~T])
    __parameters__: typing.ClassVar[tuple]  # value = (~T)
    _vars = None
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __ctype__(self):
        ...
    def __del__(self):
        ...
    def __getitem__(self, key):
        ...
    def __init__(self, data = None, attrib = None, dtype = ..., ndim = None):
        ...
    def __len__(self):
        ...
    def __str__(self):
        ...
    def fill_(self, value):
        ...
    @property
    def vars(self):
        ...
class fabricarray_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('buckets', ctypes.c_void_p), ('nbuckets', ctypes.c_ulong), ('size', ctypes.c_ulong)]
    def __init__(self, buckets = None, nbuckets = 0, size = 0):
        ...
class fabricbucket_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('index_start', ctypes.c_ulong), ('index_end', ctypes.c_ulong), ('ptr', ctypes.c_void_p), ('lengths', ctypes.c_void_p)]
    def __init__(self, index_start = 0, index_end = 0, ptr = None, lengths = None):
        ...
class indexedfabricarray(warp.types.noncontiguous_array_base):
    __orig_bases__: typing.ClassVar[tuple]  # value = (warp.types.noncontiguous_array_base[~T])
    __parameters__: typing.ClassVar[tuple]  # value = (~T)
    _vars = None
    def __ctype__(self):
        ...
    def __init__(self, fa = None, indices = None, dtype = None, ndim = None):
        ...
    def __len__(self):
        ...
    def __str__(self):
        ...
    def fill_(self, value):
        ...
    @property
    def vars(self):
        ...
class indexedfabricarray_t(_ctypes.Structure):
    _fields_: typing.ClassVar[list] = [('fa', fabricarray_t), ('indices', ctypes.c_void_p), ('size', ctypes.c_ulong)]
    def __init__(self, fa = None, indices = None):
        ...
def fabric_to_warp_dtype(type_info, attrib_name):
    ...
def fabricarrayarray(**kwargs):
    ...
def indexedfabricarrayarray(**kwargs):
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
float_types: tuple = (warp.types.float16, warp.types.float32, warp.types.float64)
int_tuple_type_hints: dict  # value = {typing.Tuple[int]: 1, typing.Tuple[int, int]: 2, typing.Tuple[int, int, int]: 3, typing.Tuple[int, int, int, int]: 4, typing.Tuple[int, ...]: -1}
int_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64)
non_atomic_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int64)
np_dtype_to_warp_type: dict  # value = {numpy.bool_: warp.types.bool, numpy.int8: warp.types.int8, numpy.uint8: warp.types.uint8, numpy.int16: warp.types.int16, numpy.uint16: warp.types.uint16, numpy.int32: warp.types.int32, numpy.int64: warp.types.int64, numpy.uint32: warp.types.uint32, numpy.uint64: warp.types.uint64, numpy.float16: warp.types.float16, numpy.float32: warp.types.float32, numpy.float64: warp.types.float64, dtype('bool'): warp.types.bool, dtype('int8'): warp.types.int8, dtype('uint8'): warp.types.uint8, dtype('int16'): warp.types.int16, dtype('uint16'): warp.types.uint16, dtype('int32'): warp.types.int32, dtype('int64'): warp.types.int64, dtype('uint32'): warp.types.uint32, dtype('uint64'): warp.types.uint64, dtype('float16'): warp.types.float16, dtype('float32'): warp.types.float32, dtype('float64'): warp.types.float64}
scalar_and_bool_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64, warp.types.bool)
scalar_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64)
value_types: tuple = (int, float, bool, warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64)
vector_types: tuple = (warp.types.vec2b, warp.types.vec2ub, warp.types.vec2s, warp.types.vec2us, warp.types.vec2i, warp.types.vec2ui, warp.types.vec2l, warp.types.vec2ul, warp.types.vec2h, warp.types.vec2f, warp.types.vec2d, warp.types.vec3b, warp.types.vec3ub, warp.types.vec3s, warp.types.vec3us, warp.types.vec3i, warp.types.vec3ui, warp.types.vec3l, warp.types.vec3ul, warp.types.vec3h, warp.types.vec3f, warp.types.vec3d, warp.types.vec4b, warp.types.vec4ub, warp.types.vec4s, warp.types.vec4us, warp.types.vec4i, warp.types.vec4ui, warp.types.vec4l, warp.types.vec4ul, warp.types.vec4h, warp.types.vec4f, warp.types.vec4d, warp.types.mat22h, warp.types.mat22f, warp.types.mat22d, warp.types.mat33h, warp.types.mat33f, warp.types.mat33d, warp.types.mat44h, warp.types.mat44f, warp.types.mat44d, warp.types.quath, warp.types.quatf, warp.types.quatd, warp.types.transformh, warp.types.transformf, warp.types.transformd, warp.types.spatial_vectorh, warp.types.spatial_vectorf, warp.types.spatial_vectord, warp.types.spatial_matrixh, warp.types.spatial_matrixf, warp.types.spatial_matrixd)
warp_type_to_np_dtype: dict = {warp.types.bool: numpy.bool_, warp.types.int8: numpy.int8, warp.types.int16: numpy.int16, warp.types.int32: numpy.int32, warp.types.int64: numpy.int64, warp.types.uint8: numpy.uint8, warp.types.uint16: numpy.uint16, warp.types.uint32: numpy.uint32, warp.types.uint64: numpy.uint64, warp.types.float16: numpy.float16, warp.types.float32: numpy.float32, warp.types.float64: numpy.float64}
