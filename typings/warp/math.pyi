from __future__ import annotations
from typing import Any
import warp as wp
import warp.context
__all__: list = ['norm_l1', 'norm_l2', 'norm_huber', 'norm_pseudo_huber', 'smooth_normalize', 'transform_from_matrix', 'transform_to_matrix']
def create_transform_from_matrix_func(dtype):
    ...
def create_transform_to_matrix_func(dtype):
    ...
norm_huber: warp.context.Function  # value = <Function norm_huber(v: typing.Any, delta: builtins.float)>
norm_l1: warp.context.Function  # value = <Function norm_l1(v: typing.Any)>
norm_l2: warp.context.Function  # value = <Function norm_l2(v: typing.Any)>
norm_pseudo_huber: warp.context.Function  # value = <Function norm_pseudo_huber(v: typing.Any, delta: builtins.float)>
smooth_normalize: warp.context.Function  # value = <Function smooth_normalize(v: typing.Any, delta: builtins.float)>
transform_from_matrix: warp.context.Function  # value = <Function transform_from_matrix(mat: mat44(f))>
transform_to_matrix: warp.context.Function  # value = <Function transform_to_matrix(xform: transformf)>
