from __future__ import annotations
import _ctypes
import cProfile as cProfile
import ctypes as ctypes
import numpy as np
import os as os
import sys as sys
import time as time
import typing
from typing import Any
import warnings as warnings
import warp as wp
import warp as warp
__all__: list[str] = ['Any', 'Devicelike', 'MeshAdjacency', 'MeshEdge', 'ScopedCapture', 'ScopedDevice', 'ScopedMempool', 'ScopedMempoolAccess', 'ScopedPeerAccess', 'ScopedStream', 'ScopedTimer', 'TIMING_ALL', 'TIMING_GRAPH', 'TIMING_KERNEL', 'TIMING_KERNEL_BUILTIN', 'TIMING_MEMCPY', 'TIMING_MEMSET', 'TimingResult', 'array_cast', 'array_inner', 'array_scan', 'array_sum', 'cProfile', 'check_p2p', 'copy_dense_volume_to_nano_vdb_f', 'copy_dense_volume_to_nano_vdb_i', 'copy_dense_volume_to_nano_vdb_v', 'ctypes', 'mem_report', 'np', 'os', 'quat_between_vectors', 'radix_sort_pairs', 'runlength_encode', 'segmented_sort_pairs', 'sys', 'time', 'timing_begin', 'timing_end', 'timing_print', 'timing_result_t', 'transform_expand', 'warn', 'warnings', 'warnings_seen', 'warp', 'warp_showwarning', 'wp']
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
    def __init__(self, device: Devicelike = None, stream = None, force_module_load = None, external = False):
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
    def __init__(self, device: Devicelike):
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
    def __init__(self, device: Devicelike, enable: bool):
        ...
class ScopedMempoolAccess:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, target_device: Devicelike, peer_device: Devicelike, enable: bool):
        ...
class ScopedPeerAccess:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, target_device: Devicelike, peer_device: Devicelike, enable: bool):
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
    def __init__(self, stream: wp.Stream | None, sync_enter: bool = True, sync_exit: bool = False):
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
    def __init__(self, name: str, active: bool = True, print: bool = True, detailed: bool = False, dict: dict[str, list[float]] | None = None, use_nvtx: bool = False, color: int | str = 'rapids', synchronize: bool = False, cuda_filter: int = 0, report_func: typing.Callable[[list[TimingResult], str], None] | None = None, skip_tape: bool = False):
        """
        Context manager object for a timer
        
                Parameters:
                    name: Name of timer
                    active: Enables this timer
                    print: At context manager exit, print elapsed time to ``sys.stdout``
                    detailed: Collects additional profiling data using cProfile and calls ``print_stats()`` at context exit
                    dict: A dictionary of lists to which the elapsed time will be appended using ``name`` as a key
                    use_nvtx: If true, timing functionality is replaced by an NVTX range
                    color: ARGB value (e.g. 0x00FFFF) or color name (e.g. 'cyan') associated with the NVTX range
                    synchronize: Synchronize the CPU thread with any outstanding CUDA work to return accurate GPU timings
                    cuda_filter: Filter flags for CUDA activity timing, e.g. ``warp.TIMING_KERNEL`` or ``warp.TIMING_ALL``
                    report_func: A callback function to print the activity report.
                      If ``None``,  :func:`wp.timing_print() <timing_print>` will be used.
                    skip_tape: If true, the timer will not be recorded in the tape
        
                Attributes:
                    extra_msg (str): Can be set to a string that will be added to the printout at context exit.
                    elapsed (float): The duration of the ``with`` block used with this object
                    timing_results (List[TimingResult]): The list of activity timing results, if collection was requested using ``cuda_filter``
                
        """
class TimingResult:
    """
    Timing result for a single activity.
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
def segmented_sort_pairs(keys, values, count: int, segment_start_indices: wp.array(dtype=wp.int32), segment_end_indices: wp.array(dtype=wp.int32) = None):
    """
    Sort key-value pairs within segments.
    
        This function performs a segmented sort of key-value pairs, where the sorting is done independently within each segment.
        The segments are defined by their start and optionally end indices.
    
        Args:
            keys: Array of keys to sort. Must be of type int32 or float32.
            values: Array of values to sort along with keys. Must be of type int32.
            count: Number of elements to sort.
            segment_start_indices: Array containing start index of each segment. Must be of type int32.
                If segment_end_indices is None, this array must have length at least num_segments + 1,
                and segment_end_indices will be inferred as segment_start_indices[1:].
                If segment_end_indices is provided, this array must have length at least num_segments.
            segment_end_indices: Optional array containing end index of each segment. Must be of type int32 if provided.
                If None, segment_end_indices will be inferred from segment_start_indices[1:].
                If provided, must have length at least num_segments.
    
        Raises:
            RuntimeError: If array storage devices don't match, if storage size is insufficient,
                         if segment_start_indices is not of type int32, or if data types are unsupported.
        
    """
def timing_begin(cuda_filter: int = 4294967295, synchronize: bool = True) -> None:
    """
    Begin detailed activity timing.
    
        Parameters:
            cuda_filter: Filter flags for CUDA activity timing, e.g. ``warp.TIMING_KERNEL`` or ``warp.TIMING_ALL``
            synchronize: Whether to synchronize all CUDA devices before timing starts
        
    """
def timing_end(synchronize: bool = True) -> list[TimingResult]:
    """
    End detailed activity timing.
    
        Parameters:
            synchronize: Whether to synchronize all CUDA devices before timing ends
    
        Returns:
            A list of :class:`TimingResult` objects for all recorded activities.
        
    """
def timing_print(results: list[TimingResult], indent: str = '') -> None:
    """
    Print timing results.
    
        Parameters:
            results: List of :class:`TimingResult` objects to print.
            indent: Optional indentation to prepend to all output lines.
        
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
copy_dense_volume_to_nano_vdb_f: warp.context.Kernel  # value = <warp.context.Kernel object>
copy_dense_volume_to_nano_vdb_i: warp.context.Kernel  # value = <warp.context.Kernel object>
copy_dense_volume_to_nano_vdb_v: warp.context.Kernel  # value = <warp.context.Kernel object>
quat_between_vectors: warp.context.Function  # value = <Function quat_between_vectors(a: vec3f, b: vec3f)>
warnings_seen: set = set()
