from __future__ import annotations
import numpy as np
import os as os
import random as random
import torch as torch
import warp as wp
__all__ = ['copysign', 'cos', 'inverse', 'matmul', 'normalize', 'np', 'os', 'random', 'scale', 'scale_transform', 'set_seed', 'sin', 'tensor_clamp', 'torch', 'torch_rand_float', 'torch_random_dir_2', 'transpose_2d', 'unscale', 'unscale_np', 'unscale_transform', 'wp']
def cos(data):
    ...
def inverse(data):
    ...
def matmul(matrix_a, matrix_b):
    ...
def set_seed(seed, torch_deterministic = False):
    """
    set seed across modules
    """
def sin(data):
    ...
def transpose_2d(data):
    ...
def unscale_np(x, lower, upper):
    ...
copysign: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
normalize: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
scale: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
scale_transform: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tensor_clamp: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
torch_rand_float: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
torch_random_dir_2: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
unscale: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
unscale_transform: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
