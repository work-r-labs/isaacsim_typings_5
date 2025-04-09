from __future__ import annotations
import ctypes as ctypes
import warp as warp
from warp.thirdparty.dlpack import DLDataType
from warp.thirdparty.dlpack import DLDataTypeCode
from warp.thirdparty.dlpack import DLDevice
from warp.thirdparty.dlpack import DLDeviceType
from warp.thirdparty.dlpack import DLManagedTensor
__all__ = ['DLDataType', 'DLDataTypeCode', 'DLDevice', 'DLDeviceType', 'DLManagedTensor', 'PyCapsule_GetPointer', 'PyCapsule_IsValid', 'PyCapsule_New', 'PyCapsule_SetName', 'PyMem_RawFree', 'PyMem_RawMalloc', 'Py_DecRef', 'Py_IncRef', 'ctypes', 'device_from_dlpack', 'device_to_dlpack', 'dtype_from_dlpack', 'dtype_is_compatible', 'dtype_to_dlpack', 'from_dlpack', 'shape_to_dlpack', 'strides_to_dlpack', 'to_dlpack', 'warp']
class _DLPackTensorHolder:
    """
    Class responsible for deleting DLManagedTensor memory after ownership is transferred from a capsule.
    """
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, mem_ptr):
        ...
def _device_to_dlpack(wp_device: warp.context.Device) -> warp.thirdparty.dlpack.DLDevice:
    ...
def _from_dlpack(capsule, dtype = None) -> warp.types.array:
    """
    Convert a DLPack capsule into a Warp array without copying.
    
        Args:
            capsule: A DLPack capsule wrapping an external array or tensor.
            dtype: An optional Warp data type to interpret the source data.
    
        Returns:
            A new Warp array that uses the same underlying memory as the input capsule.
        
    """
def device_from_dlpack(dl_device):
    ...
def device_to_dlpack(wp_device) -> warp.thirdparty.dlpack.DLDevice:
    ...
def dtype_from_dlpack(dl_dtype):
    ...
def dtype_is_compatible(dl_dtype, wp_dtype):
    ...
def dtype_to_dlpack(wp_dtype) -> warp.thirdparty.dlpack.DLDataType:
    ...
def from_dlpack(source, dtype = None) -> warp.types.array:
    """
    Convert a source array or DLPack capsule into a Warp array without copying.
    
        Args:
            source: A DLPack-compatible array or PyCapsule
            dtype: An optional Warp data type to interpret the source data.
    
        Returns:
            A new Warp array that uses the same underlying memory as the input
            pycapsule.
        
    """
def shape_to_dlpack(shape):
    ...
def strides_to_dlpack(strides, dtype):
    ...
def to_dlpack(wp_array: warp.types.array):
    """
    Convert a Warp array to another type of DLPack-compatible array.
    
        Args:
            wp_array: The source Warp array that will be converted.
    
        Returns:
            A capsule containing a DLManagedTensor that can be converted
            to another array type without copying the underlying memory.
        
    """
PyCapsule_GetPointer: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
PyCapsule_IsValid: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
PyCapsule_New: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
PyCapsule_SetName: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
PyMem_RawFree: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
PyMem_RawMalloc: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
Py_DecRef: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
Py_IncRef: ctypes.CDLL.__init__.<locals>._FuncPtr  # value = <_FuncPtr object>
_c_str_dltensor: bytes  # value = b'dltensor'
_c_str_used_dltensor: bytes  # value = b'used_dltensor'
_dlpack_capsule_deleter: ctypes.CFUNCTYPE.<locals>.CFunctionType  # value = <CFunctionType object>
_dlpack_tensor_deleter: ctypes.CFUNCTYPE.<locals>.CFunctionType  # value = <CFunctionType object>
