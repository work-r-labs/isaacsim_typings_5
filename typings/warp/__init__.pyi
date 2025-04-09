from __future__ import annotations
import typing
from warp.build import clear_kernel_cache
from warp.builtins import static
from warp.context import Event
from warp.context import Function
from warp.context import Kernel
from warp.context import Launch
from warp.context import RegisteredGLBuffer
from warp.context import Stream
from warp.context import capture_begin
from warp.context import capture_end
from warp.context import capture_launch
from warp.context import clone
from warp.context import copy
from warp.context import empty
from warp.context import empty_like
from warp.context import force_load
from warp.context import from_numpy
from warp.context import full
from warp.context import full_like
from warp.context import func
from warp.context import func_grad
from warp.context import func_native
from warp.context import func_replay
from warp.context import get_cuda_device
from warp.context import get_cuda_device_count
from warp.context import get_cuda_devices
from warp.context import get_device
from warp.context import get_devices
from warp.context import get_event_elapsed_time
from warp.context import get_mempool_release_threshold
from warp.context import get_module
from warp.context import get_module_options
from warp.context import get_preferred_device
from warp.context import get_stream
from warp.context import init
from warp.context import is_cpu_available
from warp.context import is_cuda_available
from warp.context import is_device_available
from warp.context import is_mempool_access_enabled
from warp.context import is_mempool_access_supported
from warp.context import is_mempool_enabled
from warp.context import is_mempool_supported
from warp.context import is_peer_access_enabled
from warp.context import is_peer_access_supported
from warp.context import kernel
from warp.context import launch
from warp.context import launch_tiled
from warp.context import load_module
from warp.context import map_cuda_device
from warp.context import ones
from warp.context import ones_like
from warp.context import overload
from warp.context import record_event
from warp.context import set_device
from warp.context import set_mempool_access_enabled
from warp.context import set_mempool_enabled
from warp.context import set_mempool_release_threshold
from warp.context import set_module_options
from warp.context import set_peer_access_enabled
from warp.context import set_stream
from warp.context import struct
from warp.context import synchronize
from warp.context import synchronize_device
from warp.context import synchronize_event
from warp.context import synchronize_stream
from warp.context import unmap_cuda_device
from warp.context import wait_event
from warp.context import wait_stream
from warp.context import zeros
from warp.context import zeros_like
from warp.dlpack import from_dlpack
from warp.dlpack import to_dlpack
from warp.fabric import fabricarray
from warp.fabric import fabricarrayarray
from warp.fabric import indexedfabricarray
from warp.fabric import indexedfabricarrayarray
from warp.jax import device_from_jax
from warp.jax import device_to_jax
from warp.jax import dtype_from_jax
from warp.jax import dtype_to_jax
from warp.jax import from_jax
from warp.jax import to_jax
from warp.paddle import device_from_paddle
from warp.paddle import device_to_paddle
from warp.paddle import dtype_from_paddle
from warp.paddle import dtype_to_paddle
from warp.paddle import from_paddle
from warp.paddle import stream_from_paddle
from warp.paddle import to_paddle
from warp.tape import Tape
from warp.torch import device_from_torch
from warp.torch import device_to_torch
from warp.torch import dtype_from_torch
from warp.torch import dtype_to_torch
from warp.torch import from_torch
from warp.torch import stream_from_torch
from warp.torch import stream_to_torch
from warp.torch import to_torch
from warp.types import Bvh
from warp.types import HashGrid
from warp.types import MarchingCubes
from warp.types import Mesh
from warp.types import Volume
from warp.types import adj_batched_matmul
from warp.types import adj_matmul
from warp.types import array
from warp.types import array1d
from warp.types import array2d
from warp.types import array3d
from warp.types import array4d
from warp.types import batched_matmul
from warp.types import bool
from warp.types import bvh_query_t as BvhQuery
from warp.types import constant
from warp.types import dtype_from_numpy
from warp.types import dtype_to_numpy
from warp.types import float16
from warp.types import float32
from warp.types import float64
from warp.types import from_ptr
from warp.types import hash_grid_query_t as HashGridQuery
from warp.types import indexedarray
from warp.types import indexedarray1d
from warp.types import indexedarray2d
from warp.types import indexedarray3d
from warp.types import indexedarray4d
from warp.types import int16
from warp.types import int32
from warp.types import int64
from warp.types import int8
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
from warp.types import matmul
from warp.types import matrix as mat
from warp.types import mesh_query_aabb_t as MeshQueryAABB
from warp.types import mesh_query_point_t as MeshQueryPoint
from warp.types import mesh_query_ray_t as MeshQueryRay
from warp.types import quatd
from warp.types import quatf
from warp.types import quatf as quat
from warp.types import quath
from warp.types import spatial_matrixd
from warp.types import spatial_matrixf
from warp.types import spatial_matrixf as spatial_matrix
from warp.types import spatial_matrixh
from warp.types import spatial_vectord
from warp.types import spatial_vectorf as spatial_vector
from warp.types import spatial_vectorf
from warp.types import spatial_vectorh
from warp.types import transformd
from warp.types import transformf
from warp.types import transformf as transform
from warp.types import transformh
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
from warp.types import vector as vec
from warp.utils import ScopedCapture
from warp.utils import ScopedDevice
from warp.utils import ScopedMempool
from warp.utils import ScopedMempoolAccess
from warp.utils import ScopedPeerAccess
from warp.utils import ScopedStream
from warp.utils import ScopedTimer
from warp.utils import TimingResult
from warp.utils import timing_begin
from warp.utils import timing_end
from warp.utils import timing_print
from warp.utils import transform_expand
from . import build
from . import builtins
from . import codegen
from . import config
from . import constants
from . import context
from . import dlpack
from . import fabric
from . import jax
from . import paddle
from . import tape
from . import thirdparty
from . import torch
from . import types
from . import utils
__all__ = ['Bvh', 'BvhQuery', 'E', 'Event', 'Float', 'Function', 'HALF_PI', 'HashGrid', 'HashGridQuery', 'INF', 'Int', 'Kernel', 'LN10', 'LN2', 'LOG10E', 'LOG2E', 'Launch', 'MarchingCubes', 'Mesh', 'MeshQueryAABB', 'MeshQueryPoint', 'MeshQueryRay', 'NAN', 'PHI', 'PI', 'RegisteredGLBuffer', 'Scalar', 'ScopedCapture', 'ScopedDevice', 'ScopedMempool', 'ScopedMempoolAccess', 'ScopedPeerAccess', 'ScopedStream', 'ScopedTimer', 'Stream', 'TAU', 'TIMING_ALL', 'TIMING_GRAPH', 'TIMING_KERNEL', 'TIMING_KERNEL_BUILTIN', 'TIMING_MEMCPY', 'TIMING_MEMSET', 'Tape', 'TimingResult', 'Volume', 'abs', 'acos', 'add', 'address', 'adj_batched_matmul', 'adj_matmul', 'argmax', 'argmin', 'array', 'array1d', 'array2d', 'array3d', 'array4d', 'array_store', 'asin', 'atan', 'atan2', 'atomic_add', 'atomic_max', 'atomic_min', 'atomic_sub', 'batched_matmul', 'bit_and', 'bit_or', 'bit_xor', 'bool', 'build', 'builtins', 'capture_begin', 'capture_end', 'capture_launch', 'cbrt', 'ceil', 'clamp', 'clear_kernel_cache', 'clone', 'codegen', 'config', 'constant', 'constants', 'context', 'copy', 'cos', 'cosh', 'cross', 'curlnoise', 'cw_div', 'cw_mul', 'ddot', 'degrees', 'dense_chol', 'dense_chol_batched', 'dense_gemm', 'dense_gemm_batched', 'dense_solve', 'dense_solve_batched', 'dense_subs', 'determinant', 'device_from_jax', 'device_from_paddle', 'device_from_torch', 'device_to_jax', 'device_to_paddle', 'device_to_torch', 'diag', 'div', 'dlpack', 'dot', 'dtype_from_jax', 'dtype_from_numpy', 'dtype_from_paddle', 'dtype_from_torch', 'dtype_to_jax', 'dtype_to_numpy', 'dtype_to_paddle', 'dtype_to_torch', 'e', 'empty', 'empty_like', 'exp', 'expect_eq', 'expect_near', 'expect_neq', 'extract', 'fabric', 'fabricarray', 'fabricarrayarray', 'float16', 'float32', 'float64', 'floor', 'floordiv', 'force_load', 'frac', 'from_dlpack', 'from_jax', 'from_numpy', 'from_paddle', 'from_ptr', 'from_torch', 'full', 'full_like', 'func', 'func_grad', 'func_native', 'func_replay', 'get_cuda_device', 'get_cuda_device_count', 'get_cuda_devices', 'get_device', 'get_devices', 'get_diag', 'get_event_elapsed_time', 'get_mempool_release_threshold', 'get_module', 'get_module_options', 'get_preferred_device', 'get_stream', 'half_pi', 'index', 'indexedarray', 'indexedarray1d', 'indexedarray2d', 'indexedarray3d', 'indexedarray4d', 'indexedfabricarray', 'indexedfabricarrayarray', 'indexref', 'inf', 'init', 'int16', 'int32', 'int64', 'int8', 'inverse', 'invert', 'is_cpu_available', 'is_cuda_available', 'is_device_available', 'is_mempool_access_enabled', 'is_mempool_access_supported', 'is_mempool_enabled', 'is_mempool_supported', 'is_peer_access_enabled', 'is_peer_access_supported', 'isfinite', 'isinf', 'isnan', 'jax', 'kernel', 'launch', 'launch_tiled', 'length', 'length_sq', 'lerp', 'ln10', 'ln2', 'load', 'load_module', 'log', 'log10', 'log10e', 'log2', 'log2e', 'lower_bound', 'lshift', 'map_cuda_device', 'mat', 'mat22', 'mat22d', 'mat22f', 'mat22h', 'mat33', 'mat33d', 'mat33f', 'mat33h', 'mat44', 'mat44d', 'mat44f', 'mat44h', 'matmul', 'max', 'min', 'mlp', 'mod', 'mul', 'nan', 'neg', 'noise', 'nonzero', 'normalize', 'ones', 'ones_like', 'outer', 'overload', 'paddle', 'phi', 'pi', 'pnoise', 'poisson', 'pos', 'pow', 'printf', 'quat', 'quat_between_vectors', 'quat_from_axis_angle', 'quat_from_matrix', 'quat_identity', 'quat_inverse', 'quat_rotate', 'quat_rotate_inv', 'quat_rpy', 'quat_slerp', 'quat_to_axis_angle', 'quat_to_matrix', 'quatd', 'quatf', 'quath', 'radians', 'rand_init', 'randf', 'randi', 'randn', 'record_event', 'rint', 'round', 'rshift', 'sample_cdf', 'sample_triangle', 'sample_unit_cube', 'sample_unit_disk', 'sample_unit_hemisphere', 'sample_unit_hemisphere_surface', 'sample_unit_ring', 'sample_unit_sphere', 'sample_unit_sphere_surface', 'sample_unit_square', 'select', 'set_device', 'set_mempool_access_enabled', 'set_mempool_enabled', 'set_mempool_release_threshold', 'set_module_options', 'set_peer_access_enabled', 'set_stream', 'sign', 'sin', 'sinh', 'skew', 'smoothstep', 'spatial_bottom', 'spatial_cross', 'spatial_cross_dual', 'spatial_dot', 'spatial_jacobian', 'spatial_mass', 'spatial_matrix', 'spatial_matrixd', 'spatial_matrixf', 'spatial_matrixh', 'spatial_top', 'spatial_vector', 'spatial_vectord', 'spatial_vectorf', 'spatial_vectorh', 'sqrt', 'static', 'step', 'store', 'stream_from_paddle', 'stream_from_torch', 'stream_to_torch', 'struct', 'sub', 'synchronize', 'synchronize_device', 'synchronize_event', 'synchronize_stream', 'tan', 'tanh', 'tape', 'tau', 'thirdparty', 'timing_begin', 'timing_end', 'timing_print', 'to_dlpack', 'to_jax', 'to_paddle', 'to_torch', 'torch', 'trace', 'transform', 'transform_expand', 'transform_get_rotation', 'transform_get_translation', 'transform_identity', 'transform_inverse', 'transform_multiply', 'transform_point', 'transform_vector', 'transformd', 'transformf', 'transformh', 'transpose', 'trunc', 'types', 'uint16', 'uint32', 'uint64', 'uint8', 'unmap_cuda_device', 'unot', 'utils', 'vec', 'vec2', 'vec2b', 'vec2d', 'vec2f', 'vec2h', 'vec2i', 'vec2l', 'vec2s', 'vec2ub', 'vec2ui', 'vec2ul', 'vec2us', 'vec3', 'vec3b', 'vec3d', 'vec3f', 'vec3h', 'vec3i', 'vec3l', 'vec3s', 'vec3ub', 'vec3ui', 'vec3ul', 'vec3us', 'vec4', 'vec4b', 'vec4d', 'vec4f', 'vec4h', 'vec4i', 'vec4l', 'vec4s', 'vec4ub', 'vec4ui', 'vec4ul', 'vec4us', 'view', 'volume_index_to_world', 'volume_index_to_world_dir', 'volume_lookup_f', 'volume_lookup_i', 'volume_lookup_index', 'volume_lookup_v', 'volume_sample_f', 'volume_sample_grad_f', 'volume_sample_i', 'volume_sample_v', 'volume_store_f', 'volume_store_i', 'volume_store_v', 'volume_world_to_index', 'volume_world_to_index_dir', 'wait_event', 'wait_stream', 'zeros', 'zeros_like']
E: float = 2.718281828459045
Float: typing.TypeVar  # value = ~Float
HALF_PI: float = 1.5707963267948966
INF: float  # value = inf
Int: typing.TypeVar  # value = ~Int
LN10: float = 2.302585092994046
LN2: float = 0.6931471805599453
LOG10E: float = 0.4342944819032518
LOG2E: float = 1.4426950408889634
NAN: float  # value = nan
PHI: float = 1.618033988749895
PI: float = 3.141592653589793
Scalar: typing.TypeVar  # value = ~Scalar
TAU: float = 6.283185307179586
TIMING_ALL: int = 4294967295
TIMING_GRAPH: int = 16
TIMING_KERNEL: int = 1
TIMING_KERNEL_BUILTIN: int = 2
TIMING_MEMCPY: int = 4
TIMING_MEMSET: int = 8
__version__: str = '1.5.0'
abs: context.Function  # value = <Function abs(x: float16)>
acos: context.Function  # value = <Function acos(x: float16)>
add: context.Function  # value = <Function add(a: float16, b: float16)>
address: context.Function  # value = <Function address(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int, l: warp.types.Int)>
argmax: context.Function  # value = <Function argmax(a: vector(length=2, dtype=<class 'warp.types.float16'>))>
argmin: context.Function  # value = <Function argmin(a: vector(length=2, dtype=<class 'warp.types.float16'>))>
array_store: context.Function  # value = <Function array_store(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, value: typing.Any)>
asin: context.Function  # value = <Function asin(x: float16)>
atan: context.Function  # value = <Function atan(x: float16)>
atan2: context.Function  # value = <Function atan2(y: float16, x: float16)>
atomic_add: context.Function  # value = <Function atomic_add(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>
atomic_max: context.Function  # value = <Function atomic_max(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>
atomic_min: context.Function  # value = <Function atomic_min(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>
atomic_sub: context.Function  # value = <Function atomic_sub(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>
bit_and: context.Function  # value = <Function bit_and(a: int16, b: int16)>
bit_or: context.Function  # value = <Function bit_or(a: int16, b: int16)>
bit_xor: context.Function  # value = <Function bit_xor(a: int16, b: int16)>
cbrt: context.Function  # value = <Function cbrt(x: float16)>
ceil: context.Function  # value = <Function ceil(x: float16)>
clamp: context.Function  # value = <Function clamp(x: float16, low: float16, high: float16)>
cos: context.Function  # value = <Function cos(x: float16)>
cosh: context.Function  # value = <Function cosh(x: float16)>
cross: context.Function  # value = <Function cross(a: vector(length=3, dtype=<class 'warp.types.float16'>), b: vector(length=3, dtype=<class 'warp.types.float16'>))>
curlnoise: context.Function  # value = <Function curlnoise(state: uint32, xy: vector(length=2, dtype=<class 'warp.types.float32'>), octaves: uint32, lacunarity: float32, gain: float32)>
cw_div: context.Function  # value = <Function cw_div(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>
cw_mul: context.Function  # value = <Function cw_mul(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>
ddot: context.Function  # value = <Function ddot(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>), b: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
degrees: context.Function  # value = <Function degrees(x: float16)>
dense_chol: context.Function  # value = <Function dense_chol(n: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), regularization: float32, L: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_chol_batched: context.Function  # value = <Function dense_chol_batched(A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_dim: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), regularization: float32, L: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_gemm: context.Function  # value = <Function dense_gemm(m: int32, n: int32, p: int32, t1: int32, t2: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), B: array(ndim=1, dtype=<class 'warp.types.float32'>), C: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_gemm_batched: context.Function  # value = <Function dense_gemm_batched(m: array(ndim=1, dtype=<class 'warp.types.int32'>), n: array(ndim=1, dtype=<class 'warp.types.int32'>), p: array(ndim=1, dtype=<class 'warp.types.int32'>), t1: int32, t2: int32, A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), B_start: array(ndim=1, dtype=<class 'warp.types.int32'>), C_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), B: array(ndim=1, dtype=<class 'warp.types.float32'>), C: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_solve: context.Function  # value = <Function dense_solve(n: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_solve_batched: context.Function  # value = <Function dense_solve_batched(b_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_dim: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>
dense_subs: context.Function  # value = <Function dense_subs(n: int32, L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>
determinant: context.Function  # value = <Function determinant(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
diag: context.Function  # value = <Function diag(vec: vector(length=2, dtype=<class 'warp.types.float16'>))>
div: context.Function  # value = <Function div(a: float16, b: float16)>
dot: context.Function  # value = <Function dot(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>
e: float = 2.718281828459045
exp: context.Function  # value = <Function exp(x: float16)>
expect_eq: context.Function  # value = <Function expect_eq(a: int8, b: int8)>
expect_near: context.Function  # value = <Function expect_near(a: float16, b: float16, tolerance: float16)>
expect_neq: context.Function  # value = <Function expect_neq(a: int8, b: int8)>
extract: context.Function  # value = <Function extract(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>
floor: context.Function  # value = <Function floor(x: float16)>
floordiv: context.Function  # value = <Function floordiv(a: float16, b: float16)>
frac: context.Function  # value = <Function frac(x: float16)>
get_diag: context.Function  # value = <Function get_diag(mat: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
half_pi: float = 1.5707963267948966
index: context.Function  # value = <Function index(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>
indexref: context.Function  # value = <Function indexref(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>
inf: float  # value = inf
inverse: context.Function  # value = <Function inverse(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
invert: context.Function  # value = <Function invert(a: int16)>
isfinite: context.Function  # value = <Function isfinite(a: float16)>
isinf: context.Function  # value = <Function isinf(a: float16)>
isnan: context.Function  # value = <Function isnan(a: float16)>
length: context.Function  # value = <Function length(a: vector(length=2, dtype=<class 'warp.types.float16'>))>
length_sq: context.Function  # value = <Function length_sq(a: vector(length=2, dtype=<class 'warp.types.float16'>))>
lerp: context.Function  # value = <Function lerp(a: float16, b: float16, t: float16)>
ln10: float = 2.302585092994046
ln2: float = 0.6931471805599453
load: context.Function  # value = <Function load(address: typing.Any)>
log: context.Function  # value = <Function log(x: float16)>
log10: context.Function  # value = <Function log10(x: float16)>
log10e: float = 0.4342944819032518
log2: context.Function  # value = <Function log2(x: float16)>
log2e: float = 1.4426950408889634
lower_bound: context.Function  # value = <Function lower_bound(arr: array(ndim=1, dtype=~Scalar), value: float16)>
lshift: context.Function  # value = <Function lshift(a: int16, b: int16)>
max: context.Function  # value = <Function max(a: float16, b: float16)>
min: context.Function  # value = <Function min(a: float16, b: float16)>
mlp: context.Function  # value = <Function mlp(weights: array(ndim=2, dtype=<class 'warp.types.float32'>), bias: array(ndim=1, dtype=<class 'warp.types.float32'>), activation: typing.Callable, index: int32, x: array(ndim=2, dtype=<class 'warp.types.float32'>), out: array(ndim=2, dtype=<class 'warp.types.float32'>))>
mod: context.Function  # value = <Function mod(a: float16, b: float16)>
mul: context.Function  # value = <Function mul(a: float16, b: float16)>
nan: float  # value = nan
neg: context.Function  # value = <Function neg(x: float16)>
noise: context.Function  # value = <Function noise(state: uint32, x: float32)>
nonzero: context.Function  # value = <Function nonzero(x: float16)>
normalize: context.Function  # value = <Function normalize(a: vector(length=2, dtype=<class 'warp.types.float16'>))>
outer: context.Function  # value = <Function outer(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>
phi: float = 1.618033988749895
pi: float = 3.141592653589793
pnoise: context.Function  # value = <Function pnoise(state: uint32, x: float32, px: int32)>
poisson: context.Function  # value = <Function poisson(state: uint32, lam: float32)>
pos: context.Function  # value = <Function pos(x: float16)>
pow: context.Function  # value = <Function pow(x: float16, y: float16)>
printf: context.Function  # value = <Function printf(fmt: builtins.str, *args: typing.Any)>
quat_between_vectors: context.Function  # value = <Function quat_between_vectors(a: vector(length=3, dtype=<class 'warp.types.float32'>), b: vector(length=3, dtype=<class 'warp.types.float32'>))>
quat_from_axis_angle: context.Function  # value = <Function quat_from_axis_angle(axis: vector(length=3, dtype=<class 'warp.types.float16'>), angle: float16)>
quat_from_matrix: context.Function  # value = <Function quat_from_matrix(mat: matrix(shape=(3, 3), dtype=<class 'warp.types.float16'>))>
quat_identity: context.Function  # value = <Function quat_identity(dtype: warp.types.Float)>
quat_inverse: context.Function  # value = <Function quat_inverse(quat: warp.types.quath)>
quat_rotate: context.Function  # value = <Function quat_rotate(quat: warp.types.quath, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>
quat_rotate_inv: context.Function  # value = <Function quat_rotate_inv(quat: warp.types.quath, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>
quat_rpy: context.Function  # value = <Function quat_rpy(roll: float16, pitch: float16, yaw: float16)>
quat_slerp: context.Function  # value = <Function quat_slerp(a: warp.types.quath, b: warp.types.quath, t: float16)>
quat_to_axis_angle: context.Function  # value = <Function quat_to_axis_angle(quat: warp.types.quath, axis: vector(length=3, dtype=<class 'warp.types.float16'>), angle: float16)>
quat_to_matrix: context.Function  # value = <Function quat_to_matrix(quat: warp.types.quath)>
radians: context.Function  # value = <Function radians(x: float16)>
rand_init: context.Function  # value = <Function rand_init(seed: int32)>
randf: context.Function  # value = <Function randf(state: uint32)>
randi: context.Function  # value = <Function randi(state: uint32)>
randn: context.Function  # value = <Function randn(state: uint32)>
rint: context.Function  # value = <Function rint(x: float16)>
round: context.Function  # value = <Function round(x: float16)>
rshift: context.Function  # value = <Function rshift(a: int16, b: int16)>
sample_cdf: context.Function  # value = <Function sample_cdf(state: uint32, cdf: array(ndim=1, dtype=<class 'warp.types.float32'>))>
sample_triangle: context.Function  # value = <Function sample_triangle(state: uint32)>
sample_unit_cube: context.Function  # value = <Function sample_unit_cube(state: uint32)>
sample_unit_disk: context.Function  # value = <Function sample_unit_disk(state: uint32)>
sample_unit_hemisphere: context.Function  # value = <Function sample_unit_hemisphere(state: uint32)>
sample_unit_hemisphere_surface: context.Function  # value = <Function sample_unit_hemisphere_surface(state: uint32)>
sample_unit_ring: context.Function  # value = <Function sample_unit_ring(state: uint32)>
sample_unit_sphere: context.Function  # value = <Function sample_unit_sphere(state: uint32)>
sample_unit_sphere_surface: context.Function  # value = <Function sample_unit_sphere_surface(state: uint32)>
sample_unit_square: context.Function  # value = <Function sample_unit_square(state: uint32)>
select: context.Function  # value = <Function select(cond: warp.types.bool, value_if_false: typing.Any, value_if_true: typing.Any)>
sign: context.Function  # value = <Function sign(x: float16)>
sin: context.Function  # value = <Function sin(x: float16)>
sinh: context.Function  # value = <Function sinh(x: float16)>
skew: context.Function  # value = <Function skew(vec: vector(length=3, dtype=<class 'warp.types.float16'>))>
smoothstep: context.Function  # value = <Function smoothstep(a: float16, b: float16, x: float16)>
spatial_bottom: context.Function  # value = <Function spatial_bottom(svec: vector(length=6, dtype=<class 'warp.types.float16'>))>
spatial_cross: context.Function  # value = <Function spatial_cross(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>
spatial_cross_dual: context.Function  # value = <Function spatial_cross_dual(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>
spatial_dot: context.Function  # value = <Function spatial_dot(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>
spatial_jacobian: context.Function  # value = <Function spatial_jacobian(S: array(ndim=1, dtype=<class 'warp.types.vector.<locals>.vec_t'>), joint_parents: array(ndim=1, dtype=<class 'warp.types.int32'>), joint_qd_start: array(ndim=1, dtype=<class 'warp.types.int32'>), joint_start: int32, joint_count: int32, J_start: int32, J_out: array(ndim=1, dtype=~Float))>
spatial_mass: context.Function  # value = <Function spatial_mass(I_s: array(ndim=1, dtype=<class 'warp.types.matrix.<locals>.mat_t'>), joint_start: int32, joint_count: int32, M_start: int32, M: array(ndim=1, dtype=~Float))>
spatial_top: context.Function  # value = <Function spatial_top(svec: vector(length=6, dtype=<class 'warp.types.float16'>))>
sqrt: context.Function  # value = <Function sqrt(x: float16)>
step: context.Function  # value = <Function step(x: float16)>
store: context.Function  # value = <Function store(address: typing.Any, value: typing.Any)>
sub: context.Function  # value = <Function sub(a: float16, b: float16)>
tan: context.Function  # value = <Function tan(x: float16)>
tanh: context.Function  # value = <Function tanh(x: float16)>
tau: float = 6.283185307179586
trace: context.Function  # value = <Function trace(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
transform_get_rotation: context.Function  # value = <Function transform_get_rotation(xform: warp.types.transformh)>
transform_get_translation: context.Function  # value = <Function transform_get_translation(xform: warp.types.transformh)>
transform_identity: context.Function  # value = <Function transform_identity(dtype: warp.types.Float)>
transform_inverse: context.Function  # value = <Function transform_inverse(xform: warp.types.transformh)>
transform_multiply: context.Function  # value = <Function transform_multiply(a: warp.types.transformh, b: warp.types.transformh)>
transform_point: context.Function  # value = <Function transform_point(xform: warp.types.transformh, point: vector(length=3, dtype=<class 'warp.types.float16'>))>
transform_vector: context.Function  # value = <Function transform_vector(xform: warp.types.transformh, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>
transpose: context.Function  # value = <Function transpose(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>
trunc: context.Function  # value = <Function trunc(x: float16)>
unot: context.Function  # value = <Function unot(a: warp.types.bool)>
view: context.Function  # value = <Function view(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int)>
volume_index_to_world: context.Function  # value = <Function volume_index_to_world(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_index_to_world_dir: context.Function  # value = <Function volume_index_to_world_dir(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_lookup_f: context.Function  # value = <Function volume_lookup_f(id: uint64, i: int32, j: int32, k: int32)>
volume_lookup_i: context.Function  # value = <Function volume_lookup_i(id: uint64, i: int32, j: int32, k: int32)>
volume_lookup_index: context.Function  # value = <Function volume_lookup_index(id: uint64, i: int32, j: int32, k: int32)>
volume_lookup_v: context.Function  # value = <Function volume_lookup_v(id: uint64, i: int32, j: int32, k: int32)>
volume_sample_f: context.Function  # value = <Function volume_sample_f(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32)>
volume_sample_grad_f: context.Function  # value = <Function volume_sample_grad_f(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, grad: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_sample_i: context.Function  # value = <Function volume_sample_i(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_sample_v: context.Function  # value = <Function volume_sample_v(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32)>
volume_store_f: context.Function  # value = <Function volume_store_f(id: uint64, i: int32, j: int32, k: int32, value: float32)>
volume_store_i: context.Function  # value = <Function volume_store_i(id: uint64, i: int32, j: int32, k: int32, value: int32)>
volume_store_v: context.Function  # value = <Function volume_store_v(id: uint64, i: int32, j: int32, k: int32, value: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_world_to_index: context.Function  # value = <Function volume_world_to_index(id: uint64, xyz: vector(length=3, dtype=<class 'warp.types.float32'>))>
volume_world_to_index_dir: context.Function  # value = <Function volume_world_to_index_dir(id: uint64, xyz: vector(length=3, dtype=<class 'warp.types.float32'>))>
