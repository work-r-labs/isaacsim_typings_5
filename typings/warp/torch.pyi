from __future__ import annotations
import ctypes as ctypes
import numpy as numpy
import warp as warp
__all__ = ['ctypes', 'device_from_torch', 'device_to_torch', 'dtype_from_torch', 'dtype_is_compatible', 'dtype_to_torch', 'from_torch', 'numpy', 'stream_from_torch', 'stream_to_torch', 'to_torch', 'warp']
def device_from_torch(torch_device) -> warp.context.Device:
    """
    Return the Warp device corresponding to a Torch device.
    
        Args:
            torch_device (`torch.device` or `str`): Torch device identifier
    
        Raises:
            RuntimeError: Torch device does not have a corresponding Warp device
        
    """
def device_to_torch(warp_device: typing.Union[warp.context.Device, str, NoneType]) -> str:
    """
    Return the Torch device string corresponding to a Warp device.
    
        Args:
            warp_device: An identifier that can be resolved to a :class:`warp.context.Device`.
    
        Raises:
            RuntimeError: The Warp device is not compatible with PyTorch.
        
    """
def dtype_from_torch(torch_dtype):
    """
    Return the Warp dtype corresponding to a Torch dtype.
    
        Args:
            torch_dtype: A ``torch.dtype`` that has a corresponding Warp data type.
                Currently ``torch.bfloat16``, ``torch.complex64``, and
                ``torch.complex128`` are not supported.
    
        Raises:
            TypeError: Unable to find a corresponding Warp data type.
        
    """
def dtype_is_compatible(torch_dtype, warp_dtype) -> bool:
    """
    Evaluates whether the given torch dtype is compatible with the given Warp dtype.
    """
def dtype_to_torch(warp_dtype):
    """
    Return the Torch dtype corresponding to a Warp dtype.
    
        Args:
            warp_dtype: A Warp data type that has a corresponding ``torch.dtype``.
                ``warp.uint16``, ``warp.uint32``, and ``warp.uint64`` are mapped
                to the signed integer ``torch.dtype`` of the same width.
        Raises:
            TypeError: Unable to find a corresponding PyTorch data type.
        
    """
def from_torch(t, dtype = None, requires_grad = None, grad = None, return_ctype = False):
    """
    Convert a Torch tensor to a Warp array without copying the data.
    
        Args:
            t (torch.Tensor): The torch tensor to wrap.
            dtype (warp.dtype, optional): The target data type of the resulting Warp array. Defaults to the tensor value type mapped to a Warp array value type.
            requires_grad (bool, optional): Whether the resulting array should wrap the tensor's gradient, if it exists (the grad tensor will be allocated otherwise). Defaults to the tensor's `requires_grad` value.
            return_ctype (bool, optional): Whether to return a low-level array descriptor instead of a ``wp.array`` object (faster).  The descriptor can be passed to Warp kernels.
    
        Returns:
            warp.array: The wrapped array or array descriptor.
        
    """
def stream_from_torch(stream_or_device = None):
    """
    Convert from a Torch CUDA stream to a Warp CUDA stream.
    """
def stream_to_torch(stream_or_device = None):
    """
    Convert from a Warp CUDA stream to a Torch CUDA stream.
    """
def to_torch(a, requires_grad = None):
    """
    
        Convert a Warp array to a Torch tensor without copying the data.
    
        Args:
            a (warp.array): The Warp array to convert.
            requires_grad (bool, optional): Whether the resulting tensor should convert the array's gradient, if it exists, to a grad tensor. Defaults to the array's `requires_grad` value.
    
        Returns:
            torch.Tensor: The converted tensor.
        
    """
