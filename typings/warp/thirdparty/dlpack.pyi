from __future__ import annotations
import _ctypes
import ctypes as ctypes
import typing
__all__ = ['DLDataType', 'DLDataTypeCode', 'DLDevice', 'DLDeviceType', 'DLManagedTensor', 'DLTensor', 'ctypes']
class DLDataType(_ctypes.Structure):
    """
    Descriptor of data type for elements of DLTensor.
        The data type is described by a triple, `DLDataType.type_code`,
        `DLDataType.bits`, and `DLDataType.lanes`.
    
        The element is understood as packed `lanes` repetitions of
        elements from `type_code` data-category of width `bits`.
        
    """
    TYPE_MAP: typing.ClassVar[dict] = {'bool': (6, 8, 1), 'int8': (0, 8, 1), 'int16': (0, 16, 1), 'int32': (0, 32, 1), 'int64': (0, 64, 1), 'uint8': (1, 8, 1), 'uint16': (1, 16, 1), 'uint32': (1, 32, 1), 'uint64': (1, 64, 1), 'float16': (2, 16, 1), 'float32': (2, 32, 1), 'float64': (2, 64, 1), 'complex64': (5, 64, 1), 'complex128': (5, 128, 1)}
    _fields_: typing.ClassVar[list] = [('type_code', DLDataTypeCode), ('bits', ctypes.c_ubyte), ('lanes', ctypes.c_ushort)]
class DLDataTypeCode(ctypes.c_ubyte):
    """
    An integer that encodes the category of DLTensor elements' data type.
    """
    kDLBfloat: typing.ClassVar[int] = 4
    kDLBool: typing.ClassVar[int] = 6
    kDLComplex: typing.ClassVar[int] = 5
    kDLFloat: typing.ClassVar[int] = 2
    kDLInt: typing.ClassVar[int] = 0
    kDLOpaquePointer: typing.ClassVar[int] = 3
    kDLUInt: typing.ClassVar[int] = 1
    def __str__(self):
        ...
class DLDevice(_ctypes.Structure):
    """
    Represents the device where DLTensor memory is allocated.
        The device is represented by the pair of fields:
           device_type: DLDeviceType
           device_id: c_int
        
    """
    _fields_: typing.ClassVar[list] = [('device_type', DLDeviceType), ('device_id', ctypes.c_int)]
class DLDeviceType(ctypes.c_int):
    """
    The enum that encodes the type of the device where
        DLTensor memory is allocated.
        
    """
    kDLCPU: typing.ClassVar[int] = 1
    kDLCUDA: typing.ClassVar[int] = 2
    kDLCUDAHost: typing.ClassVar[int] = 3
    kDLCUDAManaged: typing.ClassVar[int] = 13
    kDLMetal: typing.ClassVar[int] = 8
    kDLOneAPI: typing.ClassVar[int] = 14
    kDLOpenCL: typing.ClassVar[int] = 4
    kDLROCM: typing.ClassVar[int] = 10
    kDLROCMHost: typing.ClassVar[int] = 11
    kDLVPI: typing.ClassVar[int] = 9
    kDLVulkan: typing.ClassVar[int] = 7
    __ctype_be__ = DLDeviceType
    __ctype_le__ = DLDeviceType
    def __str__(self):
        ...
class DLManagedTensor(_ctypes.Structure):
    """
    Structure storing the pointer to the tensor descriptor,
        deleter callable for the tensor descriptor, and pointer to
        some additional data. These are stored in fields `dl_tensor`,
        `deleter`, and `manager_ctx`.
    """
    _fields_: typing.ClassVar[list] = [('dl_tensor', DLTensor), ('manager_ctx', ctypes.c_void_p), ('deleter', ctypes.CFUNCTYPE.<locals>.CFunctionType)]
class DLTensor(_ctypes.Structure):
    """
    Structure describing strided layout of DLTensor.
        Fields are:
           data:  void pointer
           device: DLDevice
           ndim: number of indices needed to reference an
                 element of the tensor
           dtype: data type descriptor
           shape: tuple with lengths of the corresponding
                  tensor dimensions
           strides: tuple of numbers of array elements to
                    step in each dimension when traversing
                    the tensor
           byte_offset: data + byte_offset gives the address of
                    tensor element with index (0,) * ndim
        
    """
    _fields_: typing.ClassVar[list] = [('data', ctypes.c_void_p), ('device', DLDevice), ('ndim', ctypes.c_int), ('dtype', DLDataType), ('shape', LP_c_long), ('strides', LP_c_long), ('byte_offset', ctypes.c_ulong)]
_c_str_dltensor: bytes  # value = b'dltensor'
