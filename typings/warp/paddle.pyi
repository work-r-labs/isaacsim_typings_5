from __future__ import annotations
import ctypes as ctypes
import numpy as numpy
import typing
import warp as warp
__all__ = ['ctypes', 'device_from_paddle', 'device_to_paddle', 'dtype_from_paddle', 'dtype_is_compatible', 'dtype_to_paddle', 'from_paddle', 'numpy', 'stream_from_paddle', 'to_paddle', 'warp']
def device_from_paddle(paddle_device: Place | CPUPlace | CUDAPinnedPlace | CUDAPlace | str) -> warp.context.Device:
    """
    Return the Warp device corresponding to a Paddle device.
    
        Args:
            paddle_device (`Place`, `CPUPlace`, `CUDAPinnedPlace`, `CUDAPlace`, or `str`): Paddle device identifier
    
        Raises:
            RuntimeError: Paddle device does not have a corresponding Warp device
        
    """
def device_to_paddle(warp_device: warp.context.Devicelike) -> str:
    """
    Return the Paddle device string corresponding to a Warp device.
    
        Args:
            warp_device: An identifier that can be resolved to a :class:`warp.context.Device`.
    
        Raises:
            RuntimeError: The Warp device is not compatible with PyPaddle.
        
    """
def dtype_from_paddle(paddle_dtype):
    """
    Return the Warp dtype corresponding to a Paddle dtype.
    
        Args:
            paddle_dtype: A ``paddle.dtype`` that has a corresponding Warp data type.
                Currently ``paddle.bfloat16``, ``paddle.complex64``, and
                ``paddle.complex128`` are not supported.
    
        Raises:
            TypeError: Unable to find a corresponding Warp data type.
        
    """
def dtype_is_compatible(paddle_dtype: paddle.dtype, warp_dtype) -> bool:
    """
    Evaluates whether the given paddle dtype is compatible with the given Warp dtype.
    """
def dtype_to_paddle(warp_dtype):
    """
    Return the Paddle dtype corresponding to a Warp dtype.
    
        Args:
            warp_dtype: A Warp data type that has a corresponding ``paddle.dtype``.
                ``warp.uint16``, ``warp.uint32``, and ``warp.uint64`` are mapped
                to the signed integer ``paddle.dtype`` of the same width.
        Raises:
            TypeError: Unable to find a corresponding PyPaddle data type.
        
    """
def from_paddle(t: paddle.Tensor, dtype: paddle.dtype | None = None, requires_grad: bool | None = None, grad: paddle.Tensor | None = None, return_ctype: bool = False) -> warp.array:
    """
    Convert a Paddle tensor to a Warp array without copying the data.
    
        Args:
            t (paddle.Tensor): The paddle tensor to wrap.
            dtype (warp.dtype, optional): The target data type of the resulting Warp array. Defaults to the tensor value type mapped to a Warp array value type.
            requires_grad (bool, optional): Whether the resulting array should wrap the tensor's gradient, if it exists (the grad tensor will be allocated otherwise). Defaults to the tensor's `requires_grad` value.
            grad (paddle.Tensor, optional): The grad attached to given tensor. Defaults to None.
            return_ctype (bool, optional): Whether to return a low-level array descriptor instead of a ``wp.array`` object (faster).  The descriptor can be passed to Warp kernels.
    
        Returns:
            warp.array: The wrapped array or array descriptor.
        
    """
def stream_from_paddle(stream_or_device = None):
    """
    Convert from a Paddle CUDA stream to a Warp CUDA stream.
    """
def to_paddle(a: warp.array, requires_grad: bool = None) -> paddle.Tensor:
    """
    
        Convert a Warp array to a Paddle tensor without copying the data.
    
        Args:
            a (warp.array): The Warp array to convert.
            requires_grad (bool, optional): Whether the resulting tensor should convert the array's gradient, if it exists, to a grad tensor. Defaults to the array's `requires_grad` value.
    
        Returns:
            paddle.Tensor: The converted tensor.
        
    """
