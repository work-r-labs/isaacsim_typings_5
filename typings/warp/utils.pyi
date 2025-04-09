from __future__ import annotations
import _ctypes
import cProfile as cProfile
import ctypes as ctypes
import numpy as np
import os as os
import sys as sys
import time as time
import typing
import warnings as warnings
import warp as wp
import warp as warp
from warp.types import float64 as T
__all__ = ['Devicelike', 'MeshAdjacency', 'MeshEdge', 'ScopedCapture', 'ScopedDevice', 'ScopedMempool', 'ScopedMempoolAccess', 'ScopedPeerAccess', 'ScopedStream', 'ScopedTimer', 'T', 'TIMING_ALL', 'TIMING_GRAPH', 'TIMING_KERNEL', 'TIMING_KERNEL_BUILTIN', 'TIMING_MEMCPY', 'TIMING_MEMSET', 'TimingResult', 'add_kernel_2d', 'add_kernel_3d', 'array_cast', 'array_inner', 'array_scan', 'array_sum', 'cProfile', 'check_p2p', 'copy_dense_volume_to_nano_vdb_f', 'copy_dense_volume_to_nano_vdb_i', 'copy_dense_volume_to_nano_vdb_v', 'ctypes', 'mem_report', 'np', 'os', 'quat_between_vectors', 'radix_sort_pairs', 'runlength_encode', 'sys', 'time', 'timing_begin', 'timing_end', 'timing_print', 'timing_result_t', 'transform_expand', 'warn', 'warnings', 'warnings_seen', 'warp', 'warp_showwarning', 'wp']
class MeshAdjacency:
    def __init__(self, indices, num_tris):
        ...
    def add_edge(self, i0, i1, o, f):
        ...
class MeshEdge:
    def __init__(self, v0, v1, o0, o1, f0, f1):
        ...
class ScopedCapture:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, device = None, stream = None, force_module_load = None, external = False):
        ...
class ScopedDevice:
    """
    A context manager to temporarily change the current default device.
    
        For CUDA devices, this context manager makes the device's CUDA context
        current and restores the previous CUDA context on exit. This is handy when
        running Warp scripts as part of a bigger pipeline because it avoids any side
        effects of changing the CUDA context in the enclosed code.
    
        Attributes:
            device (Device): The device that will temporarily become the default
              device within the context.
            saved_device (Device): The previous default device. This is restored as
              the default device on exiting the context.
        
    """
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, device: typing.Union[warp.context.Device, str, NoneType]):
        """
        Initializes the context manager with a device.
        
                Args:
                    device: The device that will temporarily become the default device
                      within the context.
                
        """
class ScopedMempool:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, device, enable: bool):
        ...
class ScopedMempoolAccess:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, target_device, peer_device, enable: bool):
        ...
class ScopedPeerAccess:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, target_device, peer_device, enable: bool):
        ...
class ScopedStream:
    """
    A context manager to temporarily change the current stream on a device.
    
        Attributes:
            stream (Stream or None): The stream that will temporarily become the device's
              default stream within the context.
            saved_stream (Stream): The device's previous current stream. This is
              restored as the device's current stream on exiting the context.
            sync_enter (bool): Whether to synchronize this context's stream with
              the device's previous current stream on entering the context.
            sync_exit (bool): Whether to synchronize the device's previous current
              with this context's stream on exiting the context.
            device (Device): The device associated with the stream.
        
    """
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, stream: typing.Optional[warp.context.Stream], sync_enter: bool = True, sync_exit: bool = False):
        """
        Initializes the context manager with a stream and synchronization options.
        
                Args:
                    stream: The stream that will temporarily become the device's
                      default stream within the context.
                    sync_enter (bool): Whether to synchronize this context's stream with
                      the device's previous current stream on entering the context.
                    sync_exit (bool): Whether to synchronize the device's previous current
                      with this context's stream on exiting the context.
                
        """
class ScopedTimer:
    enabled: typing.ClassVar[bool] = True
    indent: typing.ClassVar[int] = -1
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, name, active = True, print = True, detailed = False, dict = None, use_nvtx = False, color = 'rapids', synchronize = False, cuda_filter = 0, report_func = None, skip_tape = False):
        """
        Context manager object for a timer
        
                Parameters:
                    name (str): Name of timer
                    active (bool): Enables this timer
                    print (bool): At context manager exit, print elapsed time to sys.stdout
                    detailed (bool): Collects additional profiling data using cProfile and calls ``print_stats()`` at context exit
                    dict (dict): A dictionary of lists to which the elapsed time will be appended using ``name`` as a key
                    use_nvtx (bool): If true, timing functionality is replaced by an NVTX range
                    color (int or str): ARGB value (e.g. 0x00FFFF) or color name (e.g. 'cyan') associated with the NVTX range
                    synchronize (bool): Synchronize the CPU thread with any outstanding CUDA work to return accurate GPU timings
                    cuda_filter (int): Filter flags for CUDA activity timing, e.g. ``warp.TIMING_KERNEL`` or ``warp.TIMING_ALL``
                    report_func (Callable): A callback function to print the activity report (``wp.timing_print()`` is used by default)
                    skip_tape (bool): If true, the timer will not be recorded in the tape
        
                Attributes:
                    extra_msg (str): Can be set to a string that will be added to the printout at context exit.
                    elapsed (float): The duration of the ``with`` block used with this object
                    timing_results (list[TimingResult]): The list of activity timing results, if collection was requested using ``cuda_filter``
                
        """
class TimingResult:
    """
    Timing result for a single activity.
    
        Parameters:
            raw_result (warp.utils.timing_result_t): The result structure obtained from C++ (internal use only)
    
        Attributes:
            device (warp.Device): The device where the activity was recorded.
            name (str): The activity name.
            filter (int): The type of activity (e.g., ``warp.TIMING_KERNEL``).
            elapsed (float): The elapsed time in milliseconds.
        
    """
    def __init__(self, device, name, filter, elapsed):
        ...
class timing_result_t(_ctypes.Structure):
    """
    CUDA timing struct for fetching values from C++
    """
    _fields_: typing.ClassVar[list] = [('context', ctypes.c_void_p), ('name', ctypes.c_char_p), ('filter', ctypes.c_int), ('elapsed', ctypes.c_float)]
def array_cast(in_array, out_array, count = None):
    ...
def array_inner(a, b, out = None, count = None, axis = None):
    ...
def array_scan(in_array, out_array, inclusive = True):
    ...
def array_sum(values, out = None, value_count = None, axis = None):
    ...
def check_p2p():
    """
    Check if the machine is configured properly for peer-to-peer transfers.
    
        Returns:
            A Boolean indicating whether the machine is configured properly for peer-to-peer transfers.
            On Linux, this function attempts to determine if IOMMU is enabled and will return `False` if IOMMU is detected.
            On other operating systems, it always return `True`.
        
    """
def mem_report():
    ...
def radix_sort_pairs(keys, values, count: int):
    ...
def runlength_encode(values, run_values, run_lengths, run_count = None, value_count = None):
    ...
def timing_begin(cuda_filter = 4294967295, synchronize = True):
    """
    Begin detailed activity timing.
    
        Parameters:
            cuda_filter (int): Filter flags for CUDA activity timing, e.g. ``warp.TIMING_KERNEL`` or ``warp.TIMING_ALL``
            synchronize (bool): Whether to synchronize all CUDA devices before timing starts
        
    """
def timing_end(synchronize = True):
    """
    End detailed activity timing.
    
        Parameters:
            synchronize (bool): Whether to synchronize all CUDA devices before timing ends
    
        Returns:
            list[TimingResult]: A list of ``TimingResult`` objects for all recorded activities.
        
    """
def timing_print(results, indent = ''):
    """
    Print timing results.
    
        Parameters:
            results (list[TimingResult]): List of ``TimingResult`` objects.
            indent (str): Optional indentation for the output.
        
    """
def transform_expand(t):
    ...
def warn(message, category = None, stacklevel = 1):
    ...
def warp_showwarning(message, category, filename, lineno, file = None, line = None):
    """
    Version of warnings.showwarning that always prints to sys.stdout.
    """
Devicelike: typing._UnionGenericAlias  # value = typing.Union[warp.context.Device, str, NoneType]
TIMING_ALL: int = 4294967295
TIMING_GRAPH: int = 16
TIMING_KERNEL: int = 1
TIMING_KERNEL_BUILTIN: int = 2
TIMING_MEMCPY: int = 4
TIMING_MEMSET: int = 8
_array_cast_kernel: warp.context.Kernel  # value = <warp.context.Kernel object>
add_kernel_2d: warp.context.Kernel  # value = <warp.context.Kernel object>
add_kernel_3d: warp.context.Kernel  # value = <warp.context.Kernel object>
copy_dense_volume_to_nano_vdb_f: warp.context.Kernel  # value = <warp.context.Kernel object>
copy_dense_volume_to_nano_vdb_i: warp.context.Kernel  # value = <warp.context.Kernel object>
copy_dense_volume_to_nano_vdb_v: warp.context.Kernel  # value = <warp.context.Kernel object>
quat_between_vectors: warp.context.Function  # value = <Function quat_between_vectors(a: vector(length=3, dtype=<class 'warp.types.float32'>), b: vector(length=3, dtype=<class 'warp.types.float32'>))>
warnings_seen: set = set()
