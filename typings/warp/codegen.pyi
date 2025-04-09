from __future__ import annotations
import ast as ast
import builtins as builtins
import ctypes as ctypes
import functools as functools
import hashlib as hashlib
import inspect as inspect
import math as math
import numpy
import numpy as np
from numpy import typing as npt
import re as re
import struct as struct
import sys as sys
import textwrap as textwrap
import types as types
import typing
from typing import Generic
from typing import NamedTuple
from typing import TypeVar
import warp as warp
from warp.fabric import fabricarray
from warp.fabric import indexedfabricarray
from warp.types import Array
from warp.types import Bvh
from warp.types import Matrix
from warp.types import Quaternion
from warp.types import Tile
from warp.types import TileBinaryMap
from warp.types import TileConstant
from warp.types import TileLoad
from warp.types import TileRange
from warp.types import TileShared
from warp.types import TileUnaryMap
from warp.types import TileZeros
from warp.types import Transformation
from warp.types import Vector
from warp.types import array
from warp.types import array1d
from warp.types import array2d
from warp.types import array3d
from warp.types import array4d
from warp.types import array_ctype_from_interface
from warp.types import array_t
from warp.types import array_type_id
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
from warp.types import is_tile
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
__all__ = ['ARRAY_MAX_DIMS', 'ARRAY_TYPE_FABRIC', 'ARRAY_TYPE_FABRIC_INDEXED', 'ARRAY_TYPE_INDEXED', 'ARRAY_TYPE_REGULAR', 'Adjoint', 'Array', 'Block', 'Bvh', 'BvhQuery', 'Cols', 'DType', 'Float', 'Generic', 'HashGridQuery', 'Int', 'LAUNCH_MAX_DIMS', 'Length', 'Matrix', 'MeshQueryAABB', 'NamedTuple', 'Quaternion', 'Reference', 'Rows', 'Scalar', 'Struct', 'StructInstance', 'T', 'Tile', 'TileBinaryMap', 'TileConstant', 'TileLoad', 'TileRange', 'TileShared', 'TileUnaryMap', 'TileZeros', 'Transformation', 'TypeVar', 'Var', 'Vector', 'WarpCodegenAttributeError', 'WarpCodegenError', 'WarpCodegenKeyError', 'WarpCodegenTypeError', 'apply_defaults', 'array', 'array1d', 'array2d', 'array3d', 'array4d', 'array_ctype_from_interface', 'array_t', 'array_type_id', 'array_types', 'ast', 'bool', 'builtin_operators', 'builtins', 'bvh_query_t', 'check_array_shape', 'check_index_array', 'codegen_func', 'codegen_func_forward', 'codegen_func_reverse', 'codegen_kernel', 'codegen_module', 'codegen_snippet', 'codegen_struct', 'comparison_chain_strings', 'compute_type_str', 'constant', 'constant_str', 'cpu_forward_function_template', 'cpu_kernel_template', 'cpu_module_header', 'cpu_module_header_template', 'cpu_module_template', 'cpu_reverse_function_template', 'ctypes', 'cuda_forward_function_template', 'cuda_kernel_template', 'cuda_module_header', 'cuda_module_header_template', 'cuda_reverse_function_template', 'dtype_from_numpy', 'dtype_to_numpy', 'eval_annotations', 'fabricarray', 'float16', 'float32', 'float64', 'float_base', 'float_to_half_bits', 'float_types', 'from_ptr', 'func_match_args', 'functools', 'get_annotations', 'get_arg_type', 'get_arg_value', 'get_closure_cell_contents', 'get_full_arg_spec', 'get_type_args', 'get_type_origin', 'half_bits_to_float', 'hash_grid_query_t', 'hashlib', 'indent', 'indexedarray', 'indexedarray1d', 'indexedarray2d', 'indexedarray3d', 'indexedarray4d', 'indexedarray_t', 'indexedfabricarray', 'inspect', 'int16', 'int32', 'int64', 'int8', 'int_base', 'int_tuple_type_hints', 'int_types', 'is_array', 'is_float', 'is_int', 'is_reference', 'is_tile', 'is_value', 'launch_bounds_t', 'make_full_qualified_name', 'mat22', 'mat22d', 'mat22f', 'mat22h', 'mat33', 'mat33d', 'mat33f', 'mat33h', 'mat44', 'mat44d', 'mat44f', 'mat44h', 'math', 'matrix', 'mesh_query_aabb_t', 'non_atomic_types', 'noncontiguous_array_base', 'np', 'np_dtype_to_warp_type', 'npt', 'op_str_is_chainable', 'options', 'quat', 'quatd', 'quaternion', 'quatf', 'quath', 'range_t', 're', 'scalar_and_bool_types', 'scalar_base', 'scalar_types', 'scalars_equal', 'shape_t', 'spatial_matrix', 'spatial_matrixd', 'spatial_matrixf', 'spatial_matrixh', 'spatial_vector', 'spatial_vectord', 'spatial_vectorf', 'spatial_vectorh', 'strides_from_shape', 'strip_reference', 'struct', 'struct_instance_repr_recursive', 'struct_template', 'sys', 'textwrap', 'transform', 'transformation', 'transformd', 'transformf', 'transformh', 'type_ctype', 'type_is_float', 'type_is_int', 'type_is_matrix', 'type_is_quaternion', 'type_is_value', 'type_is_vector', 'type_length', 'type_repr', 'type_scalar_type', 'type_size_in_bytes', 'type_to_warp', 'type_typestr', 'types', 'types_equal', 'uint16', 'uint32', 'uint64', 'uint8', 'value_types', 'values_check_equal', 'vec2', 'vec2b', 'vec2d', 'vec2f', 'vec2h', 'vec2i', 'vec2l', 'vec2s', 'vec2ub', 'vec2ui', 'vec2ul', 'vec2us', 'vec3', 'vec3b', 'vec3d', 'vec3f', 'vec3h', 'vec3i', 'vec3l', 'vec3s', 'vec3ub', 'vec3ui', 'vec3ul', 'vec3us', 'vec4', 'vec4b', 'vec4d', 'vec4f', 'vec4h', 'vec4i', 'vec4l', 'vec4s', 'vec4ub', 'vec4ui', 'vec4ul', 'vec4us', 'vector', 'vector_types', 'void', 'warp', 'warp_type_to_np_dtype', 'zlib']
class Adjoint:
    node_visitors: typing.ClassVar[dict] = {ast.FunctionDef: Adjoint.emit_FunctionDef, ast.If: Adjoint.emit_If, ast.Compare: Adjoint.emit_Compare, ast.BoolOp: Adjoint.emit_BoolOp, ast.Name: Adjoint.emit_Name, ast.Attribute: Adjoint.emit_Attribute, ast.Str: Adjoint.emit_String, ast.Num: Adjoint.emit_Num, ast.NameConstant: Adjoint.emit_NameConstant, ast.Constant: Adjoint.emit_Constant, ast.BinOp: Adjoint.emit_BinOp, ast.UnaryOp: Adjoint.emit_UnaryOp, ast.While: Adjoint.emit_While, ast.For: Adjoint.emit_For, ast.Break: Adjoint.emit_Break, ast.Continue: Adjoint.emit_Continue, ast.Expr: Adjoint.emit_Expr, ast.Call: Adjoint.emit_Call, ast.Index: Adjoint.emit_Index, ast.Subscript: Adjoint.emit_Subscript, ast.Assign: Adjoint.emit_Assign, ast.Return: Adjoint.emit_Return, ast.AugAssign: Adjoint.emit_AugAssign, ast.Tuple: Adjoint.emit_Tuple, ast.Pass: Adjoint.emit_Pass, ast.Ellipsis: Adjoint.emit_Ellipsis}
    @staticmethod
    def __init__(adj, func: typing.Callable[..., typing.Any], overload_annotations = None, is_user_function = False, skip_forward_codegen = False, skip_reverse_codegen = False, custom_reverse_mode = False, custom_reverse_num_input_args = -1, transformers: list[ast.NodeTransformer] | None = None):
        ...
    @staticmethod
    def add_bool_op(adj, op_string, exprs):
        ...
    @staticmethod
    def add_builtin_call(adj, func_name, args, min_outputs = None):
        ...
    @staticmethod
    def add_call(adj, func, args, kwargs, type_args, min_outputs = None):
        ...
    @staticmethod
    def add_comp(adj, op_strings, left, comps):
        ...
    @staticmethod
    def add_constant(adj, n):
        ...
    @staticmethod
    def add_forward(adj, statement, replay = None, skip_replay = False):
        ...
    @staticmethod
    def add_return(adj, var):
        ...
    @staticmethod
    def add_reverse(adj, statement):
        ...
    @staticmethod
    def add_var(adj, type = None, constant = None):
        ...
    @staticmethod
    def alloc_shared_extra(adj, num_bytes):
        ...
    @staticmethod
    def begin_block(adj, name = 'block'):
        ...
    @staticmethod
    def begin_else(adj, cond):
        ...
    @staticmethod
    def begin_for(adj, iter):
        ...
    @staticmethod
    def begin_if(adj, cond):
        ...
    @staticmethod
    def begin_while(adj, cond):
        ...
    @staticmethod
    def build(adj, builder, default_builder_options = None):
        ...
    @staticmethod
    def check_tid_in_func_error(adj, node):
        ...
    @staticmethod
    def contains_break(adj, body):
        ...
    @staticmethod
    def dedent(adj):
        ...
    @staticmethod
    def emit_Assign(adj, node):
        ...
    @staticmethod
    def emit_Attribute(adj, node):
        ...
    @staticmethod
    def emit_AugAssign(adj, node):
        ...
    @staticmethod
    def emit_BinOp(adj, node):
        ...
    @staticmethod
    def emit_BoolOp(adj, node):
        ...
    @staticmethod
    def emit_Break(adj, node):
        ...
    @staticmethod
    def emit_Call(adj, node):
        ...
    @staticmethod
    def emit_Compare(adj, node):
        ...
    @staticmethod
    def emit_Constant(adj, node):
        ...
    @staticmethod
    def emit_Continue(adj, node):
        ...
    @staticmethod
    def emit_Ellipsis(adj, node):
        ...
    @staticmethod
    def emit_Expr(adj, node):
        ...
    @staticmethod
    def emit_For(adj, node):
        ...
    @staticmethod
    def emit_FunctionDef(adj, node):
        ...
    @staticmethod
    def emit_If(adj, node):
        ...
    @staticmethod
    def emit_Index(adj, node):
        ...
    @staticmethod
    def emit_Name(adj, node):
        ...
    @staticmethod
    def emit_NameConstant(adj, node):
        ...
    @staticmethod
    def emit_Num(adj, node):
        ...
    @staticmethod
    def emit_Pass(adj, node):
        ...
    @staticmethod
    def emit_Return(adj, node):
        ...
    @staticmethod
    def emit_String(adj, node):
        ...
    @staticmethod
    def emit_Subscript(adj, node):
        ...
    @staticmethod
    def emit_Tuple(adj, node):
        ...
    @staticmethod
    def emit_UnaryOp(adj, node):
        ...
    @staticmethod
    def emit_While(adj, node):
        ...
    @staticmethod
    def end_block(adj):
        ...
    @staticmethod
    def end_else(adj, cond):
        ...
    @staticmethod
    def end_for(adj, iter):
        ...
    @staticmethod
    def end_if(adj, cond):
        ...
    @staticmethod
    def end_while(adj):
        ...
    @staticmethod
    def eval(adj, node):
        ...
    @staticmethod
    def eval_num(adj, a):
        ...
    @staticmethod
    def eval_subscript(adj, node):
        ...
    @staticmethod
    def evaluate_static_expression(adj, node) -> tuple[typing.Any, str]:
        ...
    @staticmethod
    def extract_node_source(adj, node) -> str | None:
        ...
    @staticmethod
    def format_args(adj, prefix, args):
        ...
    @staticmethod
    def format_forward_call_args(adj, args, use_initializer_list):
        ...
    @staticmethod
    def format_reverse_call_args(adj, args_var, args, args_out, use_initializer_list, has_output_args = True, require_original_output_arg = False):
        ...
    @staticmethod
    def format_template(adj, template, input_vars, output_var):
        ...
    @staticmethod
    def get_node_source(adj, node):
        ...
    @staticmethod
    def get_references(adj) -> tuple[dict[str, typing.Any], dict[typing.Any, typing.Any], dict[warp.context.Function, typing.Any]]:
        """
        Traverses ``adj.tree`` and returns referenced constants, types, and user-defined functions.
        """
    @staticmethod
    def get_static_evaluation_context(adj):
        ...
    @staticmethod
    def get_total_required_shared(adj):
        ...
    @staticmethod
    def get_unroll_range(adj, loop):
        ...
    @staticmethod
    def indent(adj):
        ...
    @staticmethod
    def is_constant_iter_symbol(adj, sym):
        ...
    @staticmethod
    def is_differentiable_value_type(var_type):
        ...
    @staticmethod
    def is_static_expression(adj, func):
        ...
    @staticmethod
    def load(adj, var):
        ...
    @staticmethod
    def materialize_redefinitions(adj, symbols):
        ...
    @staticmethod
    def record_constant_iter_symbol(adj, sym):
        ...
    @staticmethod
    def register_var(adj, var):
        ...
    @staticmethod
    def replace_static_expressions(adj):
        ...
    @staticmethod
    def resolve_arg(adj, arg):
        ...
    @staticmethod
    def resolve_external_reference(adj, name: str):
        ...
    @staticmethod
    def resolve_func(adj, func, arg_types, kwarg_types, min_outputs):
        ...
    @staticmethod
    def resolve_path(adj, path):
        ...
    @staticmethod
    def resolve_static_expression(adj, root_node, eval_types = True):
        ...
    @staticmethod
    def resolve_type_attribute(var_type: type, attr: str):
        ...
    @staticmethod
    def set_lineno(adj, lineno):
        ...
    @staticmethod
    def vector_component_index(adj, component, vector_type):
        ...
    @staticmethod
    def verify_static_return_value(adj, value):
        ...
class Block:
    def __init__(self):
        ...
class Reference:
    def __init__(self, value_type):
        ...
class Struct:
    def __call__(self):
        """
        
                This function returns s = StructInstance(self)
                s uses self.cls as template.
                To enable autocomplete on s, we inherit from self.cls.
                For example,
        
                @wp.struct
                class A:
                    # annotations
                    ...
        
                The type annotations are inherited in A(), allowing autocomplete in kernels
                
        """
    def __init__(self, cls, key, module):
        ...
    def from_ptr(self, ptr):
        ...
    def initializer(self):
        ...
    def numpy_dtype(self):
        ...
class StructInstance:
    def __ctype__(self):
        ...
    def __getattribute__(self, name):
        ...
    def __init__(self, cls: Struct, ctype):
        ...
    def __repr__(self):
        ...
    def __setattr__(self, name, value):
        ...
    def numpy_dtype(self):
        ...
    def numpy_value(self):
        ...
    def to(self, device):
        """
        Copies this struct with all array members moved onto the given device.
        
                Arrays already living on the desired device are referenced as-is, while
                arrays being moved are copied.
                
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
class WarpCodegenAttributeError(AttributeError):
    def __init__(self, message):
        ...
class WarpCodegenError(RuntimeError):
    def __init__(self, message):
        ...
class WarpCodegenKeyError(KeyError):
    def __init__(self, message):
        ...
class WarpCodegenTypeError(TypeError):
    def __init__(self, message):
        ...
def apply_defaults(bound_args: inspect.BoundArguments, values: Mapping[str, typing.Any]):
    ...
def codegen_func(adj, c_func_name: str, device = 'cpu', options = None):
    ...
def codegen_func_forward(adj, func_type = 'kernel', device = 'cpu'):
    ...
def codegen_func_reverse(adj, func_type = 'kernel', device = 'cpu'):
    ...
def codegen_kernel(kernel, device, options):
    ...
def codegen_module(kernel, device = 'cpu'):
    ...
def codegen_snippet(adj, name, snippet, adj_snippet, replay_snippet):
    ...
def codegen_struct(struct, device = 'cpu', indent_size = 4):
    ...
def compute_type_str(base_name, template_params):
    ...
def constant_str(value):
    ...
def eval_annotations(annotations: Mapping[str, typing.Any], obj: typing.Any) -> Mapping[str, typing.Any]:
    """
    Un-stringize annotations caused by `from __future__ import annotations` of PEP 563.
    """
def func_match_args(func, arg_types, kwarg_types):
    ...
def get_annotations(obj: typing.Any) -> Mapping[str, typing.Any]:
    """
    Same as `inspect.get_annotations()` but always returning un-stringized annotations.
    """
def get_arg_type(arg: Var | typing.Any):
    ...
def get_arg_value(arg: Var | typing.Any):
    ...
def get_closure_cell_contents(obj):
    """
    Retrieve a closure's cell contents or `None` if it's empty.
    """
def get_full_arg_spec(func: typing.Callable) -> inspect.FullArgSpec:
    """
    Same as `inspect.getfullargspec()` but always returning un-stringized annotations.
    """
def get_type_args(tp):
    ...
def get_type_origin(tp):
    ...
def indent(args, stops = 1):
    ...
def is_reference(type):
    ...
def make_full_qualified_name(func):
    ...
def op_str_is_chainable(op: str) -> builtins.bool:
    ...
def strip_reference(arg):
    ...
def struct_instance_repr_recursive(inst: StructInstance, depth: int) -> str:
    ...
def values_check_equal(a, b):
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
builtin_operators: dict = {ast.Add: 'add', ast.Sub: 'sub', ast.Mult: 'mul', ast.MatMult: 'mul', ast.Div: 'div', ast.FloorDiv: 'floordiv', ast.Pow: 'pow', ast.Mod: 'mod', ast.UAdd: 'pos', ast.USub: 'neg', ast.Not: 'unot', ast.Gt: '>', ast.Lt: '<', ast.GtE: '>=', ast.LtE: '<=', ast.Eq: '==', ast.NotEq: '!=', ast.BitAnd: 'bit_and', ast.BitOr: 'bit_or', ast.BitXor: 'bit_xor', ast.Invert: 'invert', ast.LShift: 'lshift', ast.RShift: 'rshift'}
comparison_chain_strings: list = ['>', '<', '<=', '>=', '==', '!=']
cpu_forward_function_template: str = '\n// {filename}:{lineno}\nstatic {return_type} {name}(\n    {forward_args})\n{{\n{forward_body}}}\n\n'
cpu_kernel_template: str = '\n\nvoid {name}_cpu_kernel_forward(\n    {forward_args})\n{{\n{forward_body}}}\n\nvoid {name}_cpu_kernel_backward(\n    {reverse_args})\n{{\n{reverse_body}}}\n\n'
cpu_module_header: str = '\n#define WP_TILE_BLOCK_DIM {tile_size}\n#define WP_NO_CRT\n#include "builtin.h"\n\n// avoid namespacing of float type for casting to float type, this is to avoid wp::float(x), which is not valid in C++\n#define float(x) cast_float(x)\n#define adj_float(x, adj_x, adj_ret) adj_cast_float(x, adj_x, adj_ret)\n\n#define int(x) cast_int(x)\n#define adj_int(x, adj_x, adj_ret) adj_cast_int(x, adj_x, adj_ret)\n\n#define builtin_tid1d() wp::tid(task_index, dim)\n#define builtin_tid2d(x, y) wp::tid(x, y, task_index, dim)\n#define builtin_tid3d(x, y, z) wp::tid(x, y, z, task_index, dim)\n#define builtin_tid4d(x, y, z, w) wp::tid(x, y, z, w, task_index, dim)\n\n'
cpu_module_header_template: str = '\n\nextern "C" {{\n\n// Python CPU entry points\nWP_API void {name}_cpu_forward(\n    {forward_args});\n\nWP_API void {name}_cpu_backward(\n    {reverse_args});\n\n}} // extern C\n'
cpu_module_template: str = '\n\nextern "C" {{\n\n// Python CPU entry points\nWP_API void {name}_cpu_forward(\n    {forward_args})\n{{\n    for (size_t task_index = 0; task_index < dim.size; ++task_index)\n    {{\n        {name}_cpu_kernel_forward(\n            {forward_params});\n    }}\n}}\n\nWP_API void {name}_cpu_backward(\n    {reverse_args})\n{{\n    for (size_t task_index = 0; task_index < dim.size; ++task_index)\n    {{\n        {name}_cpu_kernel_backward(\n            {reverse_params});\n    }}\n}}\n\n}} // extern C\n\n'
cpu_reverse_function_template: str = '\n// {filename}:{lineno}\nstatic void adj_{name}(\n    {reverse_args})\n{{\n{reverse_body}}}\n\n'
cuda_forward_function_template: str = '\n// {filename}:{lineno}\nstatic CUDA_CALLABLE {return_type} {name}(\n    {forward_args})\n{{\n{forward_body}}}\n\n'
cuda_kernel_template: str = '\n\nextern "C" __global__ void {name}_cuda_kernel_forward(\n    {forward_args})\n{{\n    for (size_t _idx = static_cast<size_t>(blockDim.x) * static_cast<size_t>(blockIdx.x) + static_cast<size_t>(threadIdx.x);\n         _idx < dim.size;\n         _idx += static_cast<size_t>(blockDim.x) * static_cast<size_t>(gridDim.x))\n    {{\n        // reset shared memory allocator\n        wp::tile_alloc_shared(0, true);\n\n{forward_body}    }}\n}}\n\nextern "C" __global__ void {name}_cuda_kernel_backward(\n    {reverse_args})\n{{\n    for (size_t _idx = static_cast<size_t>(blockDim.x) * static_cast<size_t>(blockIdx.x) + static_cast<size_t>(threadIdx.x);\n         _idx < dim.size;\n         _idx += static_cast<size_t>(blockDim.x) * static_cast<size_t>(gridDim.x))\n    {{\n        // reset shared memory allocator\n        wp::tile_alloc_shared(0, true);\n\n{reverse_body}    }}\n}}\n\n'
cuda_module_header: str = '\n#define WP_TILE_BLOCK_DIM {tile_size}\n#define WP_NO_CRT\n#include "builtin.h"\n\n// avoid namespacing of float type for casting to float type, this is to avoid wp::float(x), which is not valid in C++\n#define float(x) cast_float(x)\n#define adj_float(x, adj_x, adj_ret) adj_cast_float(x, adj_x, adj_ret)\n\n#define int(x) cast_int(x)\n#define adj_int(x, adj_x, adj_ret) adj_cast_int(x, adj_x, adj_ret)\n\n#define builtin_tid1d() wp::tid(_idx, dim)\n#define builtin_tid2d(x, y) wp::tid(x, y, _idx, dim)\n#define builtin_tid3d(x, y, z) wp::tid(x, y, z, _idx, dim)\n#define builtin_tid4d(x, y, z, w) wp::tid(x, y, z, w, _idx, dim)\n\n'
cuda_module_header_template: str = '\n\nextern "C" {{\n\n// Python CUDA entry points\nWP_API void {name}_cuda_forward(\n    void* stream,\n    {forward_args});\n\nWP_API void {name}_cuda_backward(\n    void* stream,\n    {reverse_args});\n\n}} // extern C\n'
cuda_reverse_function_template: str = '\n// {filename}:{lineno}\nstatic CUDA_CALLABLE void adj_{name}(\n    {reverse_args})\n{{\n{reverse_body}}}\n\n'
float_types: tuple = (warp.types.float16, warp.types.float32, warp.types.float64)
int_tuple_type_hints: dict  # value = {typing.Tuple[int]: 1, typing.Tuple[int, int]: 2, typing.Tuple[int, int, int]: 3, typing.Tuple[int, int, int, int]: 4, typing.Tuple[int, ...]: -1}
int_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64)
non_atomic_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int64)
np_dtype_to_warp_type: dict  # value = {numpy.bool_: warp.types.bool, numpy.int8: warp.types.int8, numpy.uint8: warp.types.uint8, numpy.int16: warp.types.int16, numpy.uint16: warp.types.uint16, numpy.int32: warp.types.int32, numpy.int64: warp.types.int64, numpy.uint32: warp.types.uint32, numpy.uint64: warp.types.uint64, numpy.float16: warp.types.float16, numpy.float32: warp.types.float32, numpy.float64: warp.types.float64, dtype('bool'): warp.types.bool, dtype('int8'): warp.types.int8, dtype('uint8'): warp.types.uint8, dtype('int16'): warp.types.int16, dtype('uint16'): warp.types.uint16, dtype('int32'): warp.types.int32, dtype('int64'): warp.types.int64, dtype('uint32'): warp.types.uint32, dtype('uint64'): warp.types.uint64, dtype('float16'): warp.types.float16, dtype('float32'): warp.types.float32, dtype('float64'): warp.types.float64}
options: dict = {}
scalar_and_bool_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64, warp.types.bool)
scalar_types: tuple = (warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64)
struct_template: str = '\nstruct {name}\n{{\n{struct_body}\n\n    CUDA_CALLABLE {name}({forward_args})\n    {forward_initializers}\n    {{\n    }}\n\n    CUDA_CALLABLE {name}& operator += (const {name}& rhs)\n    {{{prefix_add_body}\n        return *this;}}\n\n}};\n\nstatic CUDA_CALLABLE void adj_{name}({reverse_args})\n{{\n{reverse_body}}}\n\nCUDA_CALLABLE void adj_atomic_add({name}* p, {name} t)\n{{\n{atomic_add_body}}}\n\n\n'
value_types: tuple = (int, float, bool, warp.types.int8, warp.types.uint8, warp.types.int16, warp.types.uint16, warp.types.int32, warp.types.uint32, warp.types.int64, warp.types.uint64, warp.types.float16, warp.types.float32, warp.types.float64)
vector_types: tuple = (warp.types.vec2b, warp.types.vec2ub, warp.types.vec2s, warp.types.vec2us, warp.types.vec2i, warp.types.vec2ui, warp.types.vec2l, warp.types.vec2ul, warp.types.vec2h, warp.types.vec2f, warp.types.vec2d, warp.types.vec3b, warp.types.vec3ub, warp.types.vec3s, warp.types.vec3us, warp.types.vec3i, warp.types.vec3ui, warp.types.vec3l, warp.types.vec3ul, warp.types.vec3h, warp.types.vec3f, warp.types.vec3d, warp.types.vec4b, warp.types.vec4ub, warp.types.vec4s, warp.types.vec4us, warp.types.vec4i, warp.types.vec4ui, warp.types.vec4l, warp.types.vec4ul, warp.types.vec4h, warp.types.vec4f, warp.types.vec4d, warp.types.mat22h, warp.types.mat22f, warp.types.mat22d, warp.types.mat33h, warp.types.mat33f, warp.types.mat33d, warp.types.mat44h, warp.types.mat44f, warp.types.mat44d, warp.types.quath, warp.types.quatf, warp.types.quatd, warp.types.transformh, warp.types.transformf, warp.types.transformd, warp.types.spatial_vectorh, warp.types.spatial_vectorf, warp.types.spatial_vectord, warp.types.spatial_matrixh, warp.types.spatial_matrixf, warp.types.spatial_matrixd)
warp_type_to_np_dtype: dict = {warp.types.bool: numpy.bool_, warp.types.int8: numpy.int8, warp.types.int16: numpy.int16, warp.types.int32: numpy.int32, warp.types.int64: numpy.int64, warp.types.uint8: numpy.uint8, warp.types.uint16: numpy.uint16, warp.types.uint32: numpy.uint32, warp.types.uint64: numpy.uint64, warp.types.float16: numpy.float16, warp.types.float32: numpy.float32, warp.types.float64: numpy.float64}
