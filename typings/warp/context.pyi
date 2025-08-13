from __future__ import annotations
import ast as ast
from copy import copy as shallowcopy
import ctypes as ctypes
import functools as functools
import hashlib as hashlib
import inspect as inspect
import io as io
import itertools as itertools
import json as json
import numpy as np
import operator as operator
import os as os
from pathlib import Path
import platform as platform
import sys as sys
import types as types
import typing as typing
from typing import Any
from typing import TypeVar
from typing import get_args
from typing import get_origin
import warp as warp
from warp.types import Array
from warp.types import launch_bounds_t
import weakref as weakref
__all__: list[str] = ['Any', 'Array', 'ContextGuard', 'CpuDefaultAllocator', 'CpuPinnedAllocator', 'CudaDefaultAllocator', 'CudaMempoolAllocator', 'Device', 'Devicelike', 'Event', 'Function', 'Graph', 'Kernel', 'KernelHooks', 'Launch', 'Module', 'ModuleBuilder', 'ModuleExec', 'ModuleHasher', 'Path', 'RegisteredGLBuffer', 'Runtime', 'Stream', 'TypeVar', 'add_builtin', 'adj_copy', 'ast', 'builtin_functions', 'call_builtin', 'capture_begin', 'capture_end', 'capture_launch', 'clone', 'complex_type_hints', 'copy', 'create_value_func', 'ctypes', 'empty', 'empty_like', 'event_from_ipc_handle', 'export_builtins', 'export_functions_rst', 'export_stubs', 'force_load', 'from_numpy', 'full', 'full_like', 'func', 'func_grad', 'func_native', 'func_replay', 'function_key_counts', 'functools', 'generate_unique_function_identifier', 'generic_vtypes', 'get_args', 'get_cuda_device', 'get_cuda_device_count', 'get_cuda_devices', 'get_device', 'get_devices', 'get_event_elapsed_time', 'get_function_args', 'get_generic_vtypes', 'get_mempool_release_threshold', 'get_mempool_used_mem_current', 'get_mempool_used_mem_high', 'get_module', 'get_module_options', 'get_origin', 'get_preferred_device', 'get_stream', 'hashlib', 'init', 'inspect', 'io', 'is_cpu_available', 'is_cuda_available', 'is_cuda_driver_initialized', 'is_device_available', 'is_mempool_access_enabled', 'is_mempool_access_supported', 'is_mempool_enabled', 'is_mempool_supported', 'is_peer_access_enabled', 'is_peer_access_supported', 'itertools', 'json', 'kernel', 'launch', 'launch_bounds_t', 'launch_tiled', 'load_module', 'map_cuda_device', 'np', 'ones', 'ones_like', 'operator', 'os', 'overload', 'pack_arg', 'platform', 'print_function', 'record_event', 'register_api_function', 'runtime', 'scalar_types', 'sequence_types', 'set_device', 'set_mempool_access_enabled', 'set_mempool_enabled', 'set_mempool_release_threshold', 'set_module_options', 'set_peer_access_enabled', 'set_stream', 'shallowcopy', 'struct', 'synchronize', 'synchronize_device', 'synchronize_event', 'synchronize_stream', 'sys', 'type_str', 'types', 'typing', 'unmap_cuda_device', 'user_modules', 'wait_event', 'wait_stream', 'warp', 'weakref', 'zeros', 'zeros_like']
class ContextGuard:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, device):
        ...
class CpuDefaultAllocator:
    def __init__(self, device):
        ...
    def alloc(self, size_in_bytes):
        ...
    def free(self, ptr, size_in_bytes):
        ...
class CpuPinnedAllocator:
    def __init__(self, device):
        ...
    def alloc(self, size_in_bytes):
        ...
    def free(self, ptr, size_in_bytes):
        ...
class CudaDefaultAllocator:
    def __init__(self, device):
        ...
    def alloc(self, size_in_bytes):
        ...
    def free(self, ptr, size_in_bytes):
        ...
class CudaMempoolAllocator:
    def __init__(self, device):
        ...
    def alloc(self, size_in_bytes):
        ...
    def free(self, ptr, size_in_bytes):
        ...
class Device:
    """
    A device to allocate Warp arrays and to launch kernels on.
    
        Attributes:
            ordinal (int): A Warp-specific label for the device. ``-1`` for CPU devices.
            name (str): A label for the device. By default, CPU devices will be named according to the processor name,
                or ``"CPU"`` if the processor name cannot be determined.
            arch (int): The compute capability version number calculated as ``10 * major + minor``.
                ``0`` for CPU devices.
            is_uva (bool): Indicates whether the device supports unified addressing.
                ``False`` for CPU devices.
            is_cubin_supported (bool): Indicates whether Warp's version of NVRTC can directly
                generate CUDA binary files (cubin) for this device's architecture. ``False`` for CPU devices.
            is_mempool_supported (bool): Indicates whether the device supports using the ``cuMemAllocAsync`` and
                ``cuMemPool`` family of APIs for stream-ordered memory allocations. ``False`` for CPU devices.
            is_ipc_supported (Optional[bool]): Indicates whether the device supports IPC.
    
                - ``True`` if supported.
                - ``False`` if not supported.
                - ``None`` if IPC support could not be determined (e.g. CUDA 11).
    
            is_primary (bool): Indicates whether this device's CUDA context is also the device's primary context.
            uuid (str): The UUID of the CUDA device. The UUID is in the same format used by ``nvidia-smi -L``.
                ``None`` for CPU devices.
            pci_bus_id (str): An identifier for the CUDA device in the format ``[domain]:[bus]:[device]``, in which
                ``domain``, ``bus``, and ``device`` are all hexadecimal values. ``None`` for CPU devices.
        
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, other):
        ...
    def __init__(self, runtime, alias, ordinal = -1, is_primary = False, context = None):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def _init_streams(self):
        """
        Initializes the device's current stream and the device's null stream.
        """
    def can_access(self, other):
        ...
    def get_allocator(self, pinned: bool = False):
        """
        Get the memory allocator for this device.
        
                Args:
                    pinned: If ``True``, an allocator for pinned memory will be
                      returned. Only applicable when this device is a CPU device.
                
        """
    def make_current(self):
        ...
    def set_stream(self, stream: Stream, sync: bool = True) -> None:
        """
        Set the current stream for this CUDA device.
        
                The current stream will be used by default for all kernel launches and
                memory operations on this device.
        
                If this is an external stream, the caller is responsible for
                guaranteeing the lifetime of the stream.
        
                Consider using :class:`warp.ScopedStream` instead.
        
                Args:
                    stream: The stream to set as this device's current stream.
                    sync: If ``True``, then ``stream`` will perform a device-side
                      synchronization with the device's previous current stream.
                
        """
    @property
    def context(self):
        """
        The context associated with the device.
        """
    @property
    def free_memory(self) -> int:
        """
        The amount of memory on the device that is free according to the OS in bytes.
        
                This function is currently only implemented for CUDA devices. 0 will be returned if called on a CPU device.
                
        """
    @property
    def has_context(self) -> bool:
        """
        A boolean indicating whether the device has a CUDA context associated with it.
        """
    @property
    def has_stream(self) -> bool:
        """
        A boolean indicating whether the device has a stream associated with it.
        """
    @property
    def is_capturing(self) -> bool:
        """
        A boolean indicating whether this device's default stream is currently capturing a graph.
        """
    @property
    def is_cpu(self) -> bool:
        """
        A boolean indicating whether the device is a CPU device.
        """
    @property
    def is_cuda(self) -> bool:
        """
        A boolean indicating whether the device is a CUDA device.
        """
    @property
    def stream(self) -> Stream:
        """
        The stream associated with a CUDA device.
        
                Raises:
                    RuntimeError: The device is not a CUDA device.
                
        """
    @stream.setter
    def stream(self, stream):
        ...
    @property
    def total_memory(self) -> int:
        """
        The total amount of device memory available in bytes.
        
                This function is currently only implemented for CUDA devices. 0 will be returned if called on a CPU device.
                
        """
class Event:
    """
    A CUDA event that can be recorded onto a stream.
    
        Events can be used for device-side synchronization, which do not block
        the host thread.
        
    """
    class Flags:
        BLOCKING_SYNC: typing.ClassVar[int] = 1
        DEFAULT: typing.ClassVar[int] = 0
        DISABLE_TIMING: typing.ClassVar[int] = 2
        INTERPROCESS: typing.ClassVar[int] = 4
    @classmethod
    def __new__(cls, *args, **kwargs):
        """
        Creates a new event instance.
        """
    def __del__(self):
        ...
    def __init__(self, device: 'Devicelike' = None, cuda_event = None, enable_timing: bool = False, interprocess: bool = False):
        """
        Initializes the event on a CUDA device.
        
                Args:
                    device: The CUDA device whose streams this event may be recorded onto.
                      If ``None``, then the current default device will be used.
                    cuda_event: A pointer to a previously allocated CUDA event. If
                      `None`, then a new event will be allocated on the associated device.
                    enable_timing: If ``True`` this event will record timing data.
                      :func:`~warp.get_event_elapsed_time` can be used to measure the
                      time between two events created with ``enable_timing=True`` and
                      recorded onto streams.
                    interprocess: If ``True`` this event may be used as an interprocess event.
        
                Raises:
                    RuntimeError: The event could not be created.
                    ValueError: The combination of ``enable_timing=True`` and
                        ``interprocess=True`` is not allowed.
                
        """
    def ipc_handle(self) -> bytes:
        """
        Return a CUDA IPC handle of the event as a 64-byte ``bytes`` object.
        
                The event must have been created with ``interprocess=True`` in order to
                obtain a valid interprocess handle.
        
                IPC is currently only supported on Linux.
        
                Example:
                    Create an event and get its IPC handle::
        
                        e1 = wp.Event(interprocess=True)
                        event_handle = e1.ipc_handle()
        
                Raises:
                    RuntimeError: Device does not support IPC.
                
        """
    @property
    def is_complete(self) -> bool:
        """
        A boolean indicating whether all work on the stream when the event was recorded has completed.
        
                This property may not be accessed during a graph capture on any stream.
                
        """
class Function:
    def __call__(self, *args, **kwargs):
        ...
    def __init__(self, func: typing.Callable | None, key: str, namespace: str, input_types: dict[str, type | TypeVar] | None = None, value_type: type | None = None, value_func: typing.Callable[[Mapping[str, type], Mapping[str, typing.Any]], type] | None = None, export_func: typing.Callable[[dict[str, type]], dict[str, type]] | None = None, dispatch_func: typing.Callable | None = None, lto_dispatch_func: typing.Callable | None = None, module: Module | None = None, variadic: bool = False, initializer_list_func: typing.Callable[[dict[str, typing.Any], type], bool] | None = None, export: bool = False, doc: str = '', group: str = '', hidden: bool = False, skip_replay: bool = False, missing_grad: bool = False, generic: bool = False, native_func: str | None = None, defaults: dict[str, typing.Any] | None = None, custom_replay_func: Function | None = None, native_snippet: str | None = None, adj_native_snippet: str | None = None, replay_snippet: str | None = None, skip_forward_codegen: bool = False, skip_reverse_codegen: bool = False, custom_reverse_num_input_args: int = -1, custom_reverse_mode: bool = False, overloaded_annotations: dict[str, type] | None = None, code_transformers: list[ast.NodeTransformer] | None = None, skip_adding_overload: bool = False, require_original_output_arg: bool = False, scope_locals: dict[str, typing.Any] | None = None):
        ...
    def __repr__(self):
        ...
    def add_overload(self, f: Function) -> None:
        ...
    def get_overload(self, arg_types: list[type], kwarg_types: Mapping[str, type]) -> Function | None:
        ...
    def is_builtin(self) -> bool:
        ...
    def is_simple(self) -> bool:
        ...
    def mangle(self) -> str:
        """
        Build a mangled name for the C-exported function, e.g.: `builtin_normalize_vec3()`.
        """
class Graph:
    def __del__(self):
        ...
    def __init__(self, device: Device, capture_id: int):
        ...
    def retain_module_exec(self, module_exec: ModuleExec):
        ...
class Kernel:
    __slotnames__: typing.ClassVar[list] = list()
    def __call__(self, *args, **kwargs):
        ...
    def __init__(self, func, key = None, module = None, options = None, code_transformers = None):
        ...
    def add_overload(self, arg_types):
        ...
    def get_mangled_name(self):
        ...
    def get_overload(self, arg_types):
        ...
    def infer_argument_types(self, args):
        ...
class KernelHooks:
    def __init__(self, forward, backward, forward_smem_bytes = 0, backward_smem_bytes = 0):
        ...
class Launch:
    """
    Represents all data required for a kernel launch so that launches can be replayed quickly.
    
        Users should not directly instantiate this class, instead use
        ``wp.launch(..., record_cmd=True)`` to record a launch.
        
    """
    def __init__(self, kernel, device: Device, hooks: KernelHooks | None = None, params: typing.Sequence[typing.Any] | None = None, params_addr: typing.Sequence[ctypes.c_void_p] | None = None, bounds: launch_bounds_t | None = None, max_blocks: int = 0, block_dim: int = 256, adjoint: bool = False):
        ...
    def launch(self, stream: Stream | None = None) -> None:
        """
        Launch the kernel.
        
                Args:
                    stream: The stream to launch on.
                
        """
    def set_dim(self, dim: int | list[int] | tuple[int, ...]):
        """
        Set the launch dimensions.
        
                Args:
                    dim: The dimensions of the launch.
                
        """
    def set_param_at_index(self, index: int, value: typing.Any, adjoint: bool = False):
        """
        Set a kernel parameter at an index.
        
                Args:
                    index: The index of the param to set.
                    value: The value to set the param to.
                
        """
    def set_param_at_index_from_ctype(self, index: int, value: ctypes.Structure | int | float):
        """
        Set a kernel parameter at an index without any type conversion.
        
                Args:
                    index: The index of the param to set.
                    value: The value to set the param to.
                
        """
    def set_param_by_name(self, name: str, value: typing.Any, adjoint: bool = False):
        """
        Set a kernel parameter by argument name.
        
                Args:
                    name: The name of the argument to set.
                    value: The value to set the argument to.
                    adjoint: If ``True``, set the adjoint of this parameter instead of the forward parameter.
                
        """
    def set_param_by_name_from_ctype(self, name: str, value: ctypes.Structure):
        """
        Set a kernel parameter by argument name with no type conversions.
        
                Args:
                    name: The name of the argument to set.
                    value: The value to set the argument to.
                
        """
    def set_params(self, values: typing.Sequence[typing.Any]):
        """
        Set all parameters.
        
                Args:
                    values: A list of values to set the params to.
                
        """
    def set_params_from_ctypes(self, values: typing.Sequence[ctypes.Structure]):
        """
        Set all parameters without performing type-conversions.
        
                Args:
                    values: A list of ctypes or basic int / float types.
                
        """
class Module:
    def __init__(self, name: str | None, loader = None):
        ...
    def find_kernel(self, func):
        ...
    def find_references(self, adj):
        ...
    def get_kernel_hooks(self, kernel, device: Device) -> KernelHooks:
        ...
    def hash_module(self):
        ...
    def load(self, device, block_dim = None) -> ModuleExec:
        ...
    def mark_modified(self):
        ...
    def register_function(self, func, scope_locals, skip_adding_overload = False):
        ...
    def register_kernel(self, kernel):
        ...
    def register_struct(self, struct):
        ...
    def unload(self):
        ...
    @property
    def live_kernels(self):
        ...
class ModuleBuilder:
    def __init__(self, module, options, hasher = None):
        ...
    def build_function(self, func):
        ...
    def build_kernel(self, kernel):
        ...
    def build_meta(self):
        ...
    def build_struct(self, struct):
        ...
    def build_struct_recursive(self, struct: warp.codegen.Struct):
        ...
    def codegen(self, device):
        ...
class ModuleExec:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, handle, module_hash, device, meta):
        ...
    def get_kernel_hooks(self, kernel) -> KernelHooks:
        ...
class ModuleHasher:
    def __init__(self, module):
        ...
    def get_constant_bytes(self, value) -> bytes:
        ...
    def get_module_hash(self) -> bytes:
        ...
    def get_unique_kernels(self):
        ...
    def hash_adjoint(self, adj: warp.codegen.Adjoint) -> bytes:
        ...
    def hash_function(self, func: Function) -> bytes:
        ...
    def hash_kernel(self, kernel: Kernel) -> bytes:
        ...
class RegisteredGLBuffer:
    """
    
        Helper class to register a GL buffer with CUDA so that it can be mapped to a Warp array.
    
        Example usage::
    
            import warp as wp
            import numpy as np
            from pyglet.gl import *
    
            wp.init()
    
            # create a GL buffer
            gl_buffer_id = GLuint()
            glGenBuffers(1, gl_buffer_id)
    
            # copy some data to the GL buffer
            glBindBuffer(GL_ARRAY_BUFFER, gl_buffer_id)
            gl_data = np.arange(1024, dtype=np.float32)
            glBufferData(GL_ARRAY_BUFFER, gl_data.nbytes, gl_data.ctypes.data, GL_DYNAMIC_DRAW)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
    
            # register the GL buffer with CUDA
            cuda_gl_buffer = wp.RegisteredGLBuffer(gl_buffer_id)
    
            # map the GL buffer to a Warp array
            arr = cuda_gl_buffer.map(dtype=wp.float32, shape=(1024,))
            # launch a Warp kernel to manipulate or read the array
            wp.launch(my_kernel, dim=1024, inputs=[arr])
            # unmap the GL buffer
            cuda_gl_buffer.unmap()
        
    """
    NONE: typing.ClassVar[int] = 0
    READ_ONLY: typing.ClassVar[int] = 1
    WRITE_DISCARD: typing.ClassVar[int] = 2
    _RegisteredGLBuffer__fallback_warning_shown: typing.ClassVar[bool] = False
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, gl_buffer_id: int, device: Devicelike = None, flags: int = 0, fallback_to_copy: bool = True):
        """
        
                Args:
                    gl_buffer_id: The OpenGL buffer id (GLuint).
                    device: The device to register the buffer with.  If None, the current device will be used.
                    flags: A combination of the flags constants :attr:`NONE`, :attr:`READ_ONLY`, and :attr:`WRITE_DISCARD`.
                    fallback_to_copy: If True and CUDA/OpenGL interop is not available, fall back to copy operations between the Warp array and the OpenGL buffer. Otherwise, a ``RuntimeError`` will be raised.
        
                Note:
        
                    The ``fallback_to_copy`` option (to use copy operations if CUDA graphics interop functionality is not available) requires pyglet version 2.0 or later. Install via ``pip install pyglet==2.*``.
                
        """
    def map(self, dtype, shape) -> warp.array:
        """
        Map the OpenGL buffer to a Warp array.
        
                Args:
                    dtype: The type of each element in the array.
                    shape: The shape of the array.
        
                Returns:
                    A Warp array object representing the mapped OpenGL buffer.
                
        """
    def unmap(self):
        """
        Unmap the OpenGL buffer.
        """
class Runtime:
    def __init__(self):
        ...
    def get_current_cuda_device(self) -> Device:
        ...
    def get_device(self, ident: Devicelike = None) -> Device:
        ...
    def get_error_string(self):
        ...
    def load_dll(self, dll_path):
        ...
    def map_cuda_device(self, alias, context = None) -> Device:
        ...
    def rename_device(self, device, alias) -> Device:
        ...
    def set_default_device(self, ident: Devicelike) -> None:
        ...
    def unmap_cuda_device(self, alias) -> None:
        ...
    def verify_cuda_device(self, device: Devicelike = None) -> None:
        ...
class Stream:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, device: 'Device' | str | None = None, priority: int = 0, **kwargs):
        """
        Initialize the stream on a device with an optional specified priority.
        
                Args:
                    device: The CUDA device on which this stream will be created.
                    priority: An optional integer specifying the requested stream priority.
                      Can be -1 (high priority) or 0 (low/default priority).
                      Values outside this range will be clamped.
                    cuda_stream (int): A optional external stream handle passed as an
                      integer. The caller is responsible for ensuring that the external
                      stream does not get destroyed while it is referenced by this
                      object.
        
                Raises:
                    RuntimeError: If function is called before Warp has completed
                      initialization with a ``device`` that is not an instance of
                      :class:`Device <warp.context.Device>`.
                    RuntimeError: ``device`` is not a CUDA Device.
                    RuntimeError: The stream could not be created on the device.
                    TypeError: The requested stream priority is not an integer.
                
        """
    def record_event(self, event: Event | None = None) -> Event:
        """
        Record an event onto the stream.
        
                Args:
                    event: A warp.Event instance to be recorded onto the stream. If not
                      provided, an :class:`~warp.Event` on the same device will be created.
        
                Raises:
                    RuntimeError: The provided :class:`~warp.Event` is from a different device than
                        the recording stream.
                
        """
    def wait_event(self, event: Event):
        """
        Makes all future work in this stream wait until `event` has completed.
        
                This function does not block the host thread.
                
        """
    def wait_stream(self, other_stream: 'Stream', event: Event | None = None):
        """
        Records an event on `other_stream` and makes this stream wait on it.
        
                All work added to this stream after this function has been called will
                delay their execution until all preceding commands in `other_stream`
                have completed.
        
                This function does not block the host thread.
        
                Args:
                    other_stream: The stream on which the calling stream will wait for
                      previously issued commands to complete before executing subsequent
                      commands.
                    event: An optional :class:`Event` instance that will be used to
                      record an event onto ``other_stream``. If ``None``, an internally
                      managed :class:`Event` instance will be used.
                
        """
    @property
    def cached_event(self) -> Event:
        ...
    @property
    def is_capturing(self) -> bool:
        """
        A boolean indicating whether a graph capture is currently ongoing on this stream.
        """
    @property
    def is_complete(self) -> bool:
        """
        A boolean indicating whether all work on the stream has completed.
        
                This property may not be accessed during a graph capture on any stream.
                
        """
    @property
    def priority(self) -> int:
        """
        An integer representing the priority of the stream.
        """
def add_builtin(key: str, input_types: dict[str, type | TypeVar] | None = None, constraint: typing.Callable[[Mapping[str, type]], bool] | None = None, value_type: type | None = None, value_func: typing.Callable | None = None, export_func: typing.Callable | None = None, dispatch_func: typing.Callable | None = None, lto_dispatch_func: typing.Callable | None = None, doc: str = '', namespace: str = 'wp::', variadic: bool = False, initializer_list_func = None, export: bool = True, group: str = 'Other', hidden: bool = False, skip_replay: bool = False, missing_grad: bool = False, native_func: str | None = None, defaults: dict[str, typing.Any] | None = None, require_original_output_arg: bool = False):
    """
    Main entry point to register a new built-in function.
    
        Args:
            key: Function name. Multiple overloaded functions can be registered
                under the same name as long as their signature differ.
            input_types: Signature of the user-facing function.
                Variadic arguments are supported by prefixing the parameter names
                with asterisks as in `*args` and `**kwargs`. Generic arguments are
                supported with types such as `Any`, `Float`, `Scalar`, etc.
            constraint: For functions that define generic arguments and
                are to be exported, this callback is used to specify whether some
                combination of inferred arguments are valid or not.
            value_type: Type returned by the function.
            value_func: Callback used to specify the return type when
                `value_type` isn't enough.
            export_func: Callback used during the context stage to specify
                the signature of the underlying C++ function, not accounting for
                the template parameters.
                If not provided, `input_types` is used.
            dispatch_func: Callback used during the codegen stage to specify
                the runtime and template arguments to be passed to the underlying C++
                function. In other words, this allows defining a mapping between
                the signatures of the user-facing and the C++ functions, and even to
                dynamically create new arguments on the fly.
                The arguments returned must be of type `codegen.Var`.
                If not provided, all arguments passed by the users when calling
                the built-in are passed as-is as runtime arguments to the C++ function.
            lto_dispatch_func: Same as dispatch_func, but takes an 'option' dict
                as extra argument (indicating tile_size and target architecture) and returns
                an LTO-IR buffer as extra return value
            doc: Used to generate the Python's docstring and the HTML documentation.
            namespace: Namespace for the underlying C++ function.
            variadic: Whether the function declares variadic arguments.
            initializer_list_func: Callback to determine whether to use the
                initializer list syntax when passing the arguments to the underlying
                C++ function.
            export: Whether the function is to be exposed to the Python
                interpreter so that it becomes available from within the `warp`
                module.
            group: Classification used for the documentation.
            hidden: Whether to add that function into the documentation.
            skip_replay: Whether operation will be performed during
                the forward replay in the backward pass.
            missing_grad: Whether the function is missing a corresponding adjoint.
            native_func: Name of the underlying C++ function.
            defaults: Default values for the parameters defined in `input_types`.
            require_original_output_arg: Used during the codegen stage to
                specify whether an adjoint parameter corresponding to the return
                value should be included in the signature of the backward function.
        
    """
def adj_copy(adj_dest: warp.array, adj_src: warp.array, dest_offset: int, src_offset: int, count: int, stream: Stream = None):
    """
    Copy adjoint operation for wp.copy() calls on the tape.
    
        Args:
            adj_dest: Destination array adjoint
            adj_src: Source array adjoint
            stream: The stream on which the copy was performed in the forward pass
        
    """
def call_builtin(func: Function, *params: typing.Any) -> tuple[bool, typing.Any]:
    ...
def capture_begin(device: Devicelike = None, stream: Stream | None = None, force_module_load: bool | None = None, external: bool = False):
    """
    Begin capture of a CUDA graph
    
        Captures all subsequent kernel launches and memory operations on CUDA devices.
        This can be used to record large numbers of kernels and replay them with low overhead.
    
        If `device` is specified, the capture will begin on the CUDA stream currently
        associated with the device.  If `stream` is specified, the capture will begin
        on the given stream.  If both are omitted, the capture will begin on the current
        stream of the current device.
    
        Args:
            device: The CUDA device to capture on
            stream: The CUDA stream to capture on
            force_module_load: Whether to force loading of all kernels before capture.
              In general it is better to use :func:`~warp.load_module()` to selectively load kernels.
              When running with CUDA drivers that support CUDA 12.3 or newer, this option is not recommended to be set to
              ``True`` because kernels can be loaded during graph capture on more recent drivers. If this argument is
              ``None``, then the behavior inherits from ``wp.config.enable_graph_capture_module_load_by_default`` if the
              driver is older than CUDA 12.3.
            external: Whether the capture was already started externally
    
        
    """
def capture_end(device: Devicelike = None, stream: Stream | None = None) -> Graph:
    """
    End the capture of a CUDA graph.
    
        Args:
            device: The CUDA device where capture began
            stream: The CUDA stream where capture began
    
        Returns:
            A :class:`Graph` object that can be launched with :func:`~warp.capture_launch()`
        
    """
def capture_launch(graph: Graph, stream: Stream | None = None):
    """
    Launch a previously captured CUDA graph
    
        Args:
            graph: A :class:`Graph` as returned by :func:`~warp.capture_end()`
            stream: A :class:`Stream` to launch the graph on
        
    """
def clone(src: warp.array, device: Devicelike = None, requires_grad: bool | None = None, pinned: bool | None = None) -> warp.array:
    """
    Clone an existing array, allocates a copy of the src memory
    
        Args:
            src: The source array to copy
            device: The device where the new array will be created (defaults to src.device)
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def copy(dest: warp.array, src: warp.array, dest_offset: int = 0, src_offset: int = 0, count: int = 0, stream: Stream | None = None):
    """
    Copy array contents from `src` to `dest`.
    
        Args:
            dest: Destination array, must be at least as large as source buffer
            src: Source array
            dest_offset: Element offset in the destination array
            src_offset: Element offset in the source array
            count: Number of array elements to copy (will copy all elements if set to 0)
            stream: The stream on which to perform the copy
    
        The stream, if specified, can be from any device.  If the stream is omitted, then Warp selects a stream based on the following rules:
        (1) If the destination array is on a CUDA device, use the current stream on the destination device.
        (2) Otherwise, if the source array is on a CUDA device, use the current stream on the source device.
    
        If neither source nor destination are on a CUDA device, no stream is used for the copy.
        
    """
def create_value_func(type):
    ...
def empty(shape: int | tuple[int, ...] | list[int] | None = None, dtype = float, device: Devicelike = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.array:
    """
    Returns an uninitialized array
    
        Args:
            shape: Array dimensions
            dtype: Type of each element, e.g.: `warp.vec3`, `warp.mat33`, etc
            device: Device that array will live on
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def empty_like(src: Array, device: Devicelike = None, requires_grad: bool | None = None, pinned: bool | None = None) -> warp.array:
    """
    Return an uninitialized array with the same type and dimension of another array
    
        Args:
            src: The template array to use for shape, data type, and device
            device: The device where the new array will be created (defaults to src.device)
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def event_from_ipc_handle(handle, device: 'Devicelike' = None) -> Event:
    """
    Create an event from an IPC handle.
    
        Args:
            handle: The interprocess event handle for an existing CUDA event.
            device (Devicelike): Device to associate with the array.
    
        Returns:
            An event created from the interprocess event handle ``handle``.
    
        Raises:
            RuntimeError: IPC is not supported on ``device``.
        
    """
def export_builtins(file: io.TextIOBase):
    ...
def export_functions_rst(file):
    ...
def export_stubs(file):
    """
    Generates stub file for auto-complete of builtin functions
    """
def force_load(device: Device | str | list[Device] | list[str] = None, modules: list[Module] = None):
    """
    Force user-defined kernels to be compiled and loaded
    
        Args:
            device: The device or list of devices to load the modules on.  If None, load on all devices.
            modules: List of modules to load.  If None, load all imported modules.
        
    """
def from_numpy(arr: np.ndarray, dtype: type | None = None, shape: typing.Sequence[int] | None = None, device: Devicelike | None = None, requires_grad: bool = False) -> warp.array:
    """
    Returns a Warp array created from a NumPy array.
    
        Args:
            arr: The NumPy array providing the data to construct the Warp array.
            dtype: The data type of the new Warp array. If this is not provided, the data type will be inferred.
            shape: The shape of the Warp array.
            device: The device on which the Warp array will be constructed.
            requires_grad: Whether gradients will be tracked for this array.
    
        Raises:
            RuntimeError: The data type of the NumPy array is not supported.
        
    """
def full(shape: int | tuple[int, ...] | list[int] | None = None, value = 0, dtype = typing.Any, device: Devicelike = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.array:
    """
    Return an array with all elements initialized to the given value
    
        Args:
            shape: Array dimensions
            value: Element value
            dtype: Type of each element, e.g.: float, warp.vec3, warp.mat33, etc
            device: Device that array will live on
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def full_like(src: Array, value: typing.Any, device: Devicelike = None, requires_grad: bool | None = None, pinned: bool | None = None) -> warp.array:
    """
    Return an array with all elements initialized to the given value with the same type and dimension of another array
    
        Args:
            src: The template array to use for shape, data type, and device
            value: Element value
            device: The device where the new array will be created (defaults to src.device)
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def func(f: typing.Callable | None = None, *, name: str | None = None):
    ...
def func_grad(forward_fn):
    """
    
        Decorator to register a custom gradient function for a given forward function.
        The function signature must correspond to one of the function overloads in the following way:
        the first part of the input arguments are the original input variables with the same types as their
        corresponding arguments in the original function, and the second part of the input arguments are the
        adjoint variables of the output variables (if available) of the original function with the same types as the
        output variables. The function must not return anything.
        
    """
def func_native(snippet: str, adj_snippet: str | None = None, replay_snippet: str | None = None):
    """
    
        Decorator to register native code snippet, @func_native
        
    """
def func_replay(forward_fn):
    """
    
        Decorator to register a custom replay function for a given forward function.
        The replay function is the function version that is called in the forward phase of the backward pass (replay mode) and corresponds to the forward function by default.
        The provided function has to match the signature of one of the original forward function overloads.
        
    """
def generate_unique_function_identifier(key: str) -> str:
    ...
def get_cuda_device(ordinal: int | None = None) -> Device:
    """
    Returns the CUDA device with the given ordinal or the current CUDA device if ordinal is None.
    """
def get_cuda_device_count() -> int:
    """
    Returns the number of CUDA devices supported in this environment.
    """
def get_cuda_devices() -> list[Device]:
    """
    Returns a list of CUDA devices supported in this environment.
    """
def get_device(ident: Devicelike = None) -> Device:
    """
    Returns the device identified by the argument.
    """
def get_devices() -> list[Device]:
    """
    Returns a list of devices supported in this environment.
    """
def get_event_elapsed_time(start_event: Event, end_event: Event, synchronize: bool = True):
    """
    Get the elapsed time between two recorded events.
    
        Both events must have been previously recorded with
        :func:`~warp.record_event()` or :meth:`warp.Stream.record_event()`.
    
        If ``synchronize`` is False, the caller must ensure that device execution has reached ``end_event``
        prior to calling ``get_event_elapsed_time()``.
    
        Args:
            start_event: The start event.
            end_event: The end event.
            synchronize: Whether Warp should synchronize on the ``end_event``.
    
        Returns:
            The elapsed time in milliseconds with a resolution about 0.5 ms.
        
    """
def get_function_args(func):
    """
    Ensures that all function arguments are annotated and returns a dictionary mapping from argument name to its type.
    """
def get_generic_vtypes():
    ...
def get_mempool_release_threshold(device: Devicelike = None) -> int:
    """
    Get the CUDA memory pool release threshold on the device.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the query is to be performed.
              If ``None``, the default device will be used.
    
        Returns:
            The memory pool release threshold in bytes.
    
        Raises:
            ValueError: If ``device`` is not a CUDA device.
            RuntimeError: If ``device`` is a CUDA device, but does not support memory pools.
        
    """
def get_mempool_used_mem_current(device: Devicelike = None) -> int:
    """
    Get the amount of memory from the device's memory pool that is currently in use by the application.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the query is to be performed.
              If ``None``, the default device will be used.
    
        Returns:
            The amount of memory used in bytes.
    
        Raises:
            ValueError: If ``device`` is not a CUDA device.
            RuntimeError: If ``device`` is a CUDA device, but does not support memory pools.
        
    """
def get_mempool_used_mem_high(device: Devicelike = None) -> int:
    """
    Get the application's memory usage high-water mark from the device's CUDA memory pool.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the query is to be performed.
              If ``None``, the default device will be used.
    
        Returns:
            The high-water mark of memory used from the memory pool in bytes.
    
        Raises:
            ValueError: If ``device`` is not a CUDA device.
            RuntimeError: If ``device`` is a CUDA device, but does not support memory pools.
        
    """
def get_module(name: str) -> Module:
    ...
def get_module_options(module: typing.Any | None = None) -> dict[str, typing.Any]:
    """
    Returns a list of options for the current module.
    """
def get_preferred_device() -> Device:
    """
    Returns the preferred compute device, ``cuda:0`` if available and ``cpu`` otherwise.
    """
def get_stream(device: Devicelike = None) -> Stream:
    """
    Return the stream currently used by the given device.
    
        Args:
            device: An optional :class:`Device` instance or device alias
              (e.g. "cuda:0") for which the current stream will be returned.
              If ``None``, the default device will be used.
    
        Raises:
            RuntimeError: The device is not a CUDA device.
        
    """
def init():
    """
    Initialize the Warp runtime. This function must be called before any other API call. If an error occurs an exception will be raised.
    """
def is_cpu_available() -> bool:
    ...
def is_cuda_available() -> bool:
    ...
def is_cuda_driver_initialized() -> bool:
    """
    Returns ``True`` if the CUDA driver is initialized.
    
        This is a stricter test than ``is_cuda_available()`` since a CUDA driver
        call to ``cuCtxGetCurrent`` is made, and the result is compared to
        `CUDA_SUCCESS`. Note that `CUDA_SUCCESS` is returned by ``cuCtxGetCurrent``
        even if there is no context bound to the calling CPU thread.
    
        This can be helpful in cases in which ``cuInit()`` was called before a fork.
        
    """
def is_device_available(device: Device) -> bool:
    ...
def is_mempool_access_enabled(target_device: Devicelike, peer_device: Devicelike) -> bool:
    """
    Check if `peer_device` can currently access the memory pool of `target_device`.
    
        This applies to memory allocated using CUDA pooled allocators.  For memory allocated using
        default CUDA allocators, use :func:`is_peer_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this peer access is currently enabled.
        
    """
def is_mempool_access_supported(target_device: Devicelike, peer_device: Devicelike) -> bool:
    """
    Check if `peer_device` can directly access the memory pool of `target_device`.
    
        If mempool access is possible, it can be managed using :func:`set_mempool_access_enabled()`
        and :func:`is_mempool_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this memory pool access is supported by the system.
        
    """
def is_mempool_enabled(device: Devicelike) -> bool:
    """
    Check if CUDA memory pool allocators are enabled on the device.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the query is to be performed.
              If ``None``, the default device will be used.
        
    """
def is_mempool_supported(device: Devicelike) -> bool:
    """
    Check if CUDA memory pool allocators are available on the device.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the query is to be performed.
              If ``None``, the default device will be used.
        
    """
def is_peer_access_enabled(target_device: Devicelike, peer_device: Devicelike) -> bool:
    """
    Check if `peer_device` can currently access the memory of `target_device`.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`is_mempool_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this peer access is currently enabled.
        
    """
def is_peer_access_supported(target_device: Devicelike, peer_device: Devicelike) -> bool:
    """
    Check if `peer_device` can directly access the memory of `target_device` on this system.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`is_mempool_access_supported()`.
    
        Returns:
            A Boolean value indicating if this peer access is supported by the system.
        
    """
def kernel(f: typing.Callable | None = None, *, enable_backward: bool | None = None, module: Module | typing.Literal['unique'] | None = None):
    """
    
        Decorator to register a Warp kernel from a Python function.
        The function must be defined with type annotations for all arguments.
        The function must not return anything.
    
        Example::
    
            @wp.kernel
            def my_kernel(a: wp.array(dtype=float), b: wp.array(dtype=float)):
                tid = wp.tid()
                b[tid] = a[tid] + 1.0
    
    
            @wp.kernel(enable_backward=False)
            def my_kernel_no_backward(a: wp.array(dtype=float, ndim=2), x: float):
                # the backward pass will not be generated
                i, j = wp.tid()
                a[i, j] = x
    
    
            @wp.kernel(module="unique")
            def my_kernel_unique_module(a: wp.array(dtype=float), b: wp.array(dtype=float)):
                # the kernel will be registered in new unique module created just for this
                # kernel and its dependent functions and structs
                tid = wp.tid()
                b[tid] = a[tid] + 1.0
    
        Args:
            f: The function to be registered as a kernel.
            enable_backward: If False, the backward pass will not be generated.
            module: The :class:`warp.context.Module` to which the kernel belongs. Alternatively, if a string `"unique"` is provided, the kernel is assigned to a new module named after the kernel name and hash. If None, the module is inferred from the function's module.
    
        Returns:
            The registered kernel.
        
    """
def launch(kernel, dim: int | typing.Sequence[int], inputs: typing.Sequence = list(), outputs: typing.Sequence = list(), adj_inputs: typing.Sequence = list(), adj_outputs: typing.Sequence = list(), device: Devicelike = None, stream: Stream | None = None, adjoint: bool = False, record_tape: bool = True, record_cmd: bool = False, max_blocks: int = 0, block_dim: int = 256):
    """
    Launch a Warp kernel on the target device
    
        Kernel launches are asynchronous with respect to the calling Python thread.
    
        Args:
            kernel: The name of a Warp kernel function, decorated with the ``@wp.kernel`` decorator
            dim: The number of threads to launch the kernel, can be an integer or a
              sequence of integers with a maximum of 4 dimensions.
            inputs: The input parameters to the kernel (optional)
            outputs: The output parameters (optional)
            adj_inputs: The adjoint inputs (optional)
            adj_outputs: The adjoint outputs (optional)
            device: The device to launch on.
            stream: The stream to launch on.
            adjoint: Whether to run forward or backward pass (typically use ``False``).
            record_tape: When ``True``, the launch will be recorded the global
              :class:`wp.Tape() <warp.Tape>` object when present.
            record_cmd: When ``True``, the launch will return a :class:`Launch`
              object. The launch will not occur until the user calls
              :meth:`Launch.launch()`.
            max_blocks: The maximum number of CUDA thread blocks to use.
              Only has an effect for CUDA kernel launches.
              If negative or zero, the maximum hardware value will be used.
            block_dim: The number of threads per block (always 1 for "cpu" devices).
        
    """
def launch_tiled(*args, **kwargs):
    """
    A helper method for launching a grid with an extra trailing dimension equal to the block size.
    
        For example, to launch a 2D grid, where each element has 64 threads assigned you would use the following:
    
        .. code-block:: python
    
            wp.launch_tiled(kernel, [M, N], inputs=[...], block_dim=64)
    
        Which is equivalent to the following:
    
        .. code-block:: python
    
            wp.launch(kernel, [M, N, 64], inputs=[...], block_dim=64)
    
        Inside your kernel code you can retrieve the first two indices of the thread as usual, ignoring the implicit third dimension if desired:
    
        .. code-block:: python
    
            @wp.kernel
            def compute()
    
                i, j = wp.tid()
    
                ...
        
    """
def load_module(module: Module | types.ModuleType | str = None, device: Device | str = None, recursive: bool = False):
    """
    Force user-defined module to be compiled and loaded
    
        Args:
            module: The module to load.  If None, load the current module.
            device: The device to load the modules on.  If None, load on all devices.
            recursive: Whether to load submodules.  E.g., if the given module is `warp.sim`, this will also load `warp.sim.model`, `warp.sim.articulation`, etc.
    
        Note: A module must be imported before it can be loaded by this function.
        
    """
def map_cuda_device(alias: str, context: ctypes.c_void_p | None = None) -> Device:
    """
    Assign a device alias to a CUDA context.
    
        This function can be used to create a wp.Device for an external CUDA context.
        If a wp.Device already exists for the given context, it's alias will change to the given value.
    
        Args:
            alias: A unique string to identify the device.
            context: A CUDA context pointer (CUcontext).  If None, the currently bound CUDA context will be used.
    
        Returns:
            The associated wp.Device.
        
    """
def ones(shape: int | tuple[int, ...] | list[int] | None = None, dtype = float, device: Devicelike = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.array:
    """
    Return a one-initialized array
    
        Args:
            shape: Array dimensions
            dtype: Type of each element, e.g.: warp.vec3, warp.mat33, etc
            device: Device that array will live on
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def ones_like(src: Array, device: Devicelike = None, requires_grad: bool | None = None, pinned: bool | None = None) -> warp.array:
    """
    Return a one-initialized array with the same type and dimension of another array
    
        Args:
            src: The template array to use for shape, data type, and device
            device: The device where the new array will be created (defaults to src.device)
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def overload(kernel, arg_types = ...):
    """
    Overload a generic kernel with the given argument types.
    
        Can be called directly or used as a function decorator.
    
        Args:
            kernel: The generic kernel to be instantiated with concrete types.
            arg_types: A list of concrete argument types for the kernel or a
                dictionary specifying generic argument names as keys and concrete
                types as variables.
        
    """
def pack_arg(kernel, arg_type, arg_name, value, device, adjoint = False):
    ...
def print_function(f, file, noentry = False):
    """
    Writes a function definition to a file for use in reST documentation
    
        Args:
            f: The function being written
            file: The file object for output
            noentry: If True, then the :noindex: and :nocontentsentry: directive
              options will be added
    
        Returns:
            A bool indicating True if f was written to file
        
    """
def record_event(event: Event | None = None):
    """
    Convenience function for calling :meth:`Stream.record_event` on the current stream.
    
        Args:
            event: :class:`Event` instance to record. If ``None``, a new :class:`Event`
              instance will be created.
    
        Returns:
            The recorded event.
        
    """
def register_api_function(function: Function, group: str = 'Other', hidden: bool = False):
    """
    Main entry point to register a Warp Python function to be part of the Warp API and appear in the documentation.
    
        Args:
            function: Warp function to be registered.
            group: Classification used for the documentation.
            hidden: Whether to add that function into the documentation.
        
    """
def set_device(ident: Devicelike) -> None:
    """
    Sets the default device identified by the argument.
    """
def set_mempool_access_enabled(target_device: Devicelike, peer_device: Devicelike, enable: bool) -> None:
    """
    Enable or disable access from `peer_device` to the memory pool of `target_device`.
    
        This applies to memory allocated using CUDA pooled allocators.  For memory allocated using
        default CUDA allocators, use :func:`set_peer_access_enabled()`.
        
    """
def set_mempool_enabled(device: Devicelike, enable: bool) -> None:
    """
    Enable or disable CUDA memory pool allocators on the device.
    
        Pooled allocators are typically faster and allow allocating memory during graph capture.
    
        They should generally be enabled, but there is a rare caveat.  Copying data between different GPUs
        may fail during graph capture if the memory was allocated using pooled allocators and memory pool
        access is not enabled between the two GPUs.  This is an internal CUDA limitation that is not related
        to Warp.  The preferred solution is to enable memory pool access using :func:`set_mempool_access_enabled`.
        If peer access is not supported, then the default CUDA allocators must be used to pre-allocate the memory
        prior to graph capture.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the operation is to be performed.
              If ``None``, the default device will be used.
        
    """
def set_mempool_release_threshold(device: Devicelike, threshold: int | float) -> None:
    """
    Set the CUDA memory pool release threshold on the device.
    
        This is the amount of reserved memory to hold onto before trying to release memory back to the OS.
        When more than this amount of bytes is held by the memory pool, the allocator will try to release
        memory back to the OS on the next call to stream, event, or device synchronize.
    
        Values between 0 and 1 are interpreted as fractions of available memory.  For example, 0.5 means
        half of the device's physical memory.  Greater values are interpreted as an absolute number of bytes.
        For example, 1024**3 means one GiB of memory.
    
        Parameters:
            device: The :class:`Device <warp.context.Device>` or device identifier
              for which the operation is to be performed.
              If ``None``, the default device will be used.
            threshold: An integer representing a number of bytes, or a ``float`` between 0 and 1,
              specifying the desired release threshold.
    
        Raises:
            ValueError: If ``device`` is not a CUDA device.
            RuntimeError: If ``device`` is a CUDA device, but does not support memory pools.
            RuntimeError: Failed to set the memory pool release threshold.
        
    """
def set_module_options(options: dict[str, typing.Any], module: typing.Any | None = None):
    """
    Set options for the current module.
    
        Options can be used to control runtime compilation and code-generation
        for the current module individually. Available options are listed below.
    
        * **mode**: The compilation mode to use, can be "debug", or "release", defaults to the value of ``warp.config.mode``.
        * **max_unroll**: The maximum fixed-size loop to unroll, defaults to the value of ``warp.config.max_unroll``.
        * **block_dim**: The default number of threads to assign to each block
    
        Args:
    
            options: Set of key-value option pairs
        
    """
def set_peer_access_enabled(target_device: Devicelike, peer_device: Devicelike, enable: bool) -> None:
    """
    Enable or disable direct access from `peer_device` to the memory of `target_device`.
    
        Enabling peer access can improve the speed of peer-to-peer memory transfers, but can have
        a negative impact on memory consumption and allocation performance.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`set_mempool_access_enabled()`.
        
    """
def set_stream(stream: Stream, device: Devicelike = None, sync: bool = False) -> None:
    """
    Convenience function for calling :meth:`Device.set_stream` on the given ``device``.
    
        Args:
            device: An optional :class:`Device` instance or device alias
              (e.g. "cuda:0") for which the current stream is to be replaced with
              ``stream``. If ``None``, the default device will be used.
            stream: The stream to set as this device's current stream.
            sync: If ``True``, then ``stream`` will perform a device-side
              synchronization with the device's previous current stream.
        
    """
def struct(c: type):
    ...
def synchronize():
    """
    Manually synchronize the calling CPU thread with any outstanding CUDA work on all devices
    
        This method allows the host application code to ensure that any kernel launches
        or memory copies have completed.
        
    """
def synchronize_device(device: Devicelike = None):
    """
    Synchronize the calling CPU thread with any outstanding CUDA work on the specified device
    
        This function allows the host application code to ensure that all kernel launches
        and memory copies have completed on the device.
    
        Args:
            device: Device to synchronize.
        
    """
def synchronize_event(event: Event):
    """
    Synchronize the calling CPU thread with an event recorded on a CUDA stream.
    
        This function allows the host application code to ensure that a specific synchronization point was reached.
    
        Args:
            event: Event to wait for.
        
    """
def synchronize_stream(stream_or_device: Stream | Devicelike | None = None):
    """
    Synchronize the calling CPU thread with any outstanding CUDA work on the specified stream.
    
        This function allows the host application code to ensure that all kernel launches
        and memory copies have completed on the stream.
    
        Args:
            stream_or_device: `wp.Stream` or a device.  If the argument is a device, synchronize the device's current stream.
        
    """
def type_str(t):
    ...
def unmap_cuda_device(alias: str) -> None:
    """
    Remove a CUDA device with the given alias.
    """
def wait_event(event: Event):
    """
    Convenience function for calling :meth:`Stream.wait_event` on the current stream.
    
        Args:
            event: :class:`Event` instance to wait for.
        
    """
def wait_stream(other_stream: Stream, event: Event | None = None):
    """
    Convenience function for calling :meth:`Stream.wait_stream` on the current stream.
    
        Args:
            other_stream: The stream on which the calling stream will wait for
              previously issued commands to complete before executing subsequent
              commands.
            event: An optional :class:`Event` instance that will be used to
              record an event onto ``other_stream``. If ``None``, an internally
              managed :class:`Event` instance will be used.
        
    """
def zeros(shape: int | tuple[int, ...] | list[int] | None = None, dtype = float, device: Devicelike = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.array:
    """
    Return a zero-initialized array
    
        Args:
            shape: Array dimensions
            dtype: Type of each element, e.g.: warp.vec3, warp.mat33, etc
            device: Device that array will live on
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
def zeros_like(src: Array, device: Devicelike = None, requires_grad: bool | None = None, pinned: bool | None = None) -> warp.array:
    """
    Return a zero-initialized array with the same type and dimension of another array
    
        Args:
            src: The template array to use for shape, data type, and device
            device: The device where the new array will be created (defaults to src.device)
            requires_grad: Whether the array will be tracked for back propagation
            pinned: Whether the array uses pinned host memory (only applicable to CPU arrays)
    
        Returns:
            A warp.array object representing the allocation
        
    """
Devicelike: typing._UnionGenericAlias  # value = typing.Union[warp.context.Device, str, NoneType]
builtin_functions: dict  # value = {'min': <Function min(a: float16, b: float16)>, 'max': <Function max(a: float16, b: float16)>, 'clamp': <Function clamp(x: float16, low: float16, high: float16)>, 'abs': <Function abs(x: float16)>, 'sign': <Function sign(x: float16)>, 'step': <Function step(x: float16)>, 'nonzero': <Function nonzero(x: float16)>, 'sin': <Function sin(x: float16)>, 'cos': <Function cos(x: float16)>, 'acos': <Function acos(x: float16)>, 'asin': <Function asin(x: float16)>, 'sqrt': <Function sqrt(x: float16)>, 'cbrt': <Function cbrt(x: float16)>, 'tan': <Function tan(x: float16)>, 'atan': <Function atan(x: float16)>, 'atan2': <Function atan2(y: float16, x: float16)>, 'sinh': <Function sinh(x: float16)>, 'cosh': <Function cosh(x: float16)>, 'tanh': <Function tanh(x: float16)>, 'degrees': <Function degrees(x: float16)>, 'radians': <Function radians(x: float16)>, 'log': <Function log(x: float16)>, 'log2': <Function log2(x: float16)>, 'log10': <Function log10(x: float16)>, 'exp': <Function exp(x: float16)>, 'pow': <Function pow(x: float16, y: float16)>, 'round': <Function round(x: float16)>, 'rint': <Function rint(x: float16)>, 'trunc': <Function trunc(x: float16)>, 'floor': <Function floor(x: float16)>, 'ceil': <Function ceil(x: float16)>, 'frac': <Function frac(x: float16)>, 'isfinite': <Function isfinite(a: float16)>, 'isnan': <Function isnan(a: float16)>, 'isinf': <Function isinf(a: float16)>, 'dot': <Function dot(a: vector(length=2, dtype=float16), b: vector(length=2, dtype=float16))>, 'ddot': <Function ddot(a: matrix(shape=(2, 2), dtype=float16), b: matrix(shape=(2, 2), dtype=float16))>, 'argmin': <Function argmin(a: vector(length=2, dtype=float16))>, 'argmax': <Function argmax(a: vector(length=2, dtype=float16))>, 'outer': <Function outer(a: vector(length=2, dtype=float16), b: vector(length=2, dtype=float16))>, 'cross': <Function cross(a: vector(length=3, dtype=float16), b: vector(length=3, dtype=float16))>, 'skew': <Function skew(vec: vector(length=3, dtype=float16))>, 'length': <Function length(a: vector(length=2, dtype=float16))>, 'length_sq': <Function length_sq(a: vector(length=2, dtype=float16))>, 'normalize': <Function normalize(a: vector(length=2, dtype=float16))>, 'transpose': <Function transpose(a: matrix(shape=(2, 2), dtype=float16))>, 'inverse': <Function inverse(a: matrix(shape=(2, 2), dtype=float16))>, 'determinant': <Function determinant(a: matrix(shape=(2, 2), dtype=float16))>, 'trace': <Function trace(a: matrix(shape=(2, 2), dtype=float16))>, 'diag': <Function diag(vec: vector(length=2, dtype=float16))>, 'get_diag': <Function get_diag(mat: matrix(shape=(2, 2), dtype=float16))>, 'cw_mul': <Function cw_mul(a: vector(length=2, dtype=float16), b: vector(length=2, dtype=float16))>, 'cw_div': <Function cw_div(a: vector(length=2, dtype=float16), b: vector(length=2, dtype=float16))>, 'int8': <Function int8(a: int8)>, 'uint8': <Function uint8(a: int8)>, 'int16': <Function int16(a: int8)>, 'uint16': <Function uint16(a: int8)>, 'int32': <Function int32(a: int8)>, 'uint32': <Function uint32(a: int8)>, 'int64': <Function int64(a: int8)>, 'uint64': <Function uint64(a: int8)>, 'float16': <Function float16(a: int8)>, 'float32': <Function float32(a: int8)>, 'float64': <Function float64(a: int8)>, 'bool': <Function bool(a: int8)>, 'int': <Function int(a: int8)>, 'float': <Function float(a: int8)>, 'vector': <Function vector(*args: warp.types.Scalar, length: int32, dtype: warp.types.Scalar)>, 'matrix': <Function matrix(*args: warp.types.Scalar, shape: typing.Tuple, dtype: warp.types.Scalar)>, 'matrix_from_cols': <Function matrix_from_cols(*args: vector(length=0, dtype=warp.types.Scalar))>, 'matrix_from_rows': <Function matrix_from_rows(*args: vector(length=0, dtype=warp.types.Scalar))>, 'identity': <Function identity(n: int32, dtype: warp.types.Scalar)>, 'svd3': <Function svd3(A: matrix(shape=(3, 3), dtype=warp.types.Float), U: matrix(shape=(3, 3), dtype=warp.types.Float), sigma: vector(length=3, dtype=warp.types.Float), V: matrix(shape=(3, 3), dtype=warp.types.Scalar))>, 'svd2': <Function svd2(A: matrix(shape=(2, 2), dtype=warp.types.Float), U: matrix(shape=(2, 2), dtype=warp.types.Float), sigma: vector(length=2, dtype=warp.types.Float), V: matrix(shape=(2, 2), dtype=warp.types.Scalar))>, 'qr3': <Function qr3(A: matrix(shape=(3, 3), dtype=warp.types.Float), Q: matrix(shape=(3, 3), dtype=warp.types.Float), R: matrix(shape=(3, 3), dtype=warp.types.Float))>, 'eig3': <Function eig3(A: matrix(shape=(3, 3), dtype=warp.types.Float), Q: matrix(shape=(3, 3), dtype=warp.types.Float), d: vector(length=3, dtype=warp.types.Float))>, 'quaternion': <Function quaternion(dtype: warp.types.Float)>, 'quat_identity': <Function quat_identity(dtype: warp.types.Float)>, 'quat_from_axis_angle': <Function quat_from_axis_angle(axis: vector(length=3, dtype=float16), angle: float16)>, 'quat_to_axis_angle': <Function quat_to_axis_angle(quat: quat(dtype=float16), axis: vector(length=3, dtype=float16), angle: float16)>, 'quat_from_matrix': <Function quat_from_matrix(mat: matrix(shape=(3, 3), dtype=float16))>, 'quat_rpy': <Function quat_rpy(roll: float16, pitch: float16, yaw: float16)>, 'quat_inverse': <Function quat_inverse(quat: quat(dtype=float16))>, 'quat_rotate': <Function quat_rotate(quat: quat(dtype=float16), vec: vector(length=3, dtype=float16))>, 'quat_rotate_inv': <Function quat_rotate_inv(quat: quat(dtype=float16), vec: vector(length=3, dtype=float16))>, 'quat_slerp': <Function quat_slerp(a: quat(dtype=float16), b: quat(dtype=float16), t: float16)>, 'quat_to_matrix': <Function quat_to_matrix(quat: quat(dtype=float16))>, 'transformation': <Function transformation(pos: vector(length=3, dtype=warp.types.Float), rot: quat(dtype=warp.types.Float), dtype: warp.types.Float)>, 'transform_identity': <Function transform_identity(dtype: warp.types.Float)>, 'transform_get_translation': <Function transform_get_translation(xform: transform(dtype=float16))>, 'transform_get_rotation': <Function transform_get_rotation(xform: transform(dtype=float16))>, 'transform_multiply': <Function transform_multiply(a: transform(dtype=float16), b: transform(dtype=float16))>, 'transform_point': <Function transform_point(xform: transform(dtype=float16), point: vector(length=3, dtype=float16))>, 'transform_vector': <Function transform_vector(xform: transform(dtype=float16), vec: vector(length=3, dtype=float16))>, 'transform_inverse': <Function transform_inverse(xform: transform(dtype=float16))>, 'spatial_vector': <Function spatial_vector(dtype: warp.types.Float)>, 'spatial_adjoint': <Function spatial_adjoint(r: matrix(shape=(3, 3), dtype=warp.types.Float), s: matrix(shape=(3, 3), dtype=warp.types.Float))>, 'spatial_dot': <Function spatial_dot(a: vector(length=6, dtype=float16), b: vector(length=6, dtype=float16))>, 'spatial_cross': <Function spatial_cross(a: vector(length=6, dtype=float16), b: vector(length=6, dtype=float16))>, 'spatial_cross_dual': <Function spatial_cross_dual(a: vector(length=6, dtype=float16), b: vector(length=6, dtype=float16))>, 'spatial_top': <Function spatial_top(svec: vector(length=6, dtype=float16))>, 'spatial_bottom': <Function spatial_bottom(svec: vector(length=6, dtype=float16))>, 'spatial_jacobian': <Function spatial_jacobian(S: array(ndim=1, dtype=vector(length=6, dtype=warp.types.Float)), joint_parents: array(ndim=1, dtype=int32), joint_qd_start: array(ndim=1, dtype=int32), joint_start: int32, joint_count: int32, J_start: int32, J_out: array(ndim=1, dtype=warp.types.Float))>, 'spatial_mass': <Function spatial_mass(I_s: array(ndim=1, dtype=matrix(shape=(6, 6), dtype=warp.types.Float)), joint_start: int32, joint_count: int32, M_start: int32, M: array(ndim=1, dtype=warp.types.Float))>, 'tile_zeros': <Function tile_zeros(shape: typing.Tuple, dtype: typing.Any, storage: builtins.str)>, 'tile_ones': <Function tile_ones(shape: typing.Tuple, dtype: typing.Any, storage: builtins.str)>, 'tile_arange': <Function tile_arange(*args: warp.types.Scalar, dtype: typing.Any, storage: builtins.str)>, 'tile_load': <Function tile_load(a: array(ndim=1, dtype=typing.Any), shape: typing.Tuple, offset: typing.Tuple, storage: builtins.str)>, 'tile_store': <Function tile_store(a: array(ndim=1, dtype=typing.Any), t: tile(shape=typing.Any, dtype=typing.Any), offset: typing.Tuple)>, 'tile_atomic_add': <Function tile_atomic_add(a: array(ndim=1, dtype=typing.Any), t: tile(shape=typing.Any, dtype=typing.Any), offset: typing.Tuple)>, 'tile_view': <Function tile_view(t: tile(shape=typing.Any, dtype=typing.Any), offset: typing.Tuple, shape: typing.Tuple)>, 'tile_assign': <Function tile_assign(dst: tile(shape=typing.Any, dtype=typing.Any), src: tile(shape=typing.Any, dtype=typing.Any), offset: typing.Tuple)>, 'assign': <Function assign(dst: tile(shape=typing.Any, dtype=typing.Any), i: int32, src: warp.types.Scalar)>, 'tile': <Function tile(x: typing.Any)>, 'untile': <Function untile(a: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_extract': <Function tile_extract(a: tile(shape=typing.Any, dtype=typing.Any), i: int32)>, 'tile_transpose': <Function tile_transpose(a: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_broadcast': <Function tile_broadcast(a: tile(shape=typing.Any, dtype=typing.Any), shape: typing.Tuple)>, 'tile_sum': <Function tile_sum(a: warp.types.Tile)>, 'tile_min': <Function tile_min(a: warp.types.Tile)>, 'tile_max': <Function tile_max(a: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_reduce': <Function tile_reduce(op: typing.Callable, a: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_map': <Function tile_map(op: typing.Callable, a: tile(shape=typing.Any, dtype=typing.Any))>, 'dense_gemm': <Function dense_gemm(m: int32, n: int32, p: int32, t1: int32, t2: int32, A: array(ndim=1, dtype=float32), B: array(ndim=1, dtype=float32), C: array(ndim=1, dtype=float32))>, 'dense_gemm_batched': <Function dense_gemm_batched(m: array(ndim=1, dtype=int32), n: array(ndim=1, dtype=int32), p: array(ndim=1, dtype=int32), t1: int32, t2: int32, A_start: array(ndim=1, dtype=int32), B_start: array(ndim=1, dtype=int32), C_start: array(ndim=1, dtype=int32), A: array(ndim=1, dtype=float32), B: array(ndim=1, dtype=float32), C: array(ndim=1, dtype=float32))>, 'dense_chol': <Function dense_chol(n: int32, A: array(ndim=1, dtype=float32), regularization: float32, L: array(ndim=1, dtype=float32))>, 'dense_chol_batched': <Function dense_chol_batched(A_start: array(ndim=1, dtype=int32), A_dim: array(ndim=1, dtype=int32), A: array(ndim=1, dtype=float32), regularization: float32, L: array(ndim=1, dtype=float32))>, 'dense_subs': <Function dense_subs(n: int32, L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32))>, 'dense_solve': <Function dense_solve(n: int32, A: array(ndim=1, dtype=float32), L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32))>, 'dense_solve_batched': <Function dense_solve_batched(b_start: array(ndim=1, dtype=int32), A_start: array(ndim=1, dtype=int32), A_dim: array(ndim=1, dtype=int32), A: array(ndim=1, dtype=float32), L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32))>, 'mlp': <Function mlp(weights: array(ndim=2, dtype=float32), bias: array(ndim=1, dtype=float32), activation: typing.Callable, index: int32, x: array(ndim=2, dtype=float32), out: array(ndim=2, dtype=float32))>, 'bvh_query_aabb': <Function bvh_query_aabb(id: uint64, low: vec3f, high: vec3f)>, 'bvh_query_ray': <Function bvh_query_ray(id: uint64, start: vec3f, dir: vec3f)>, 'bvh_query_next': <Function bvh_query_next(query: warp.types.bvh_query_t, index: int32)>, 'mesh_query_point': <Function mesh_query_point(id: uint64, point: vec3f, max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_point_no_sign': <Function mesh_query_point_no_sign(id: uint64, point: vec3f, max_dist: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_furthest_point_no_sign': <Function mesh_query_furthest_point_no_sign(id: uint64, point: vec3f, min_dist: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_point_sign_normal': <Function mesh_query_point_sign_normal(id: uint64, point: vec3f, max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32, epsilon: float32)>, 'mesh_query_point_sign_winding_number': <Function mesh_query_point_sign_winding_number(id: uint64, point: vec3f, max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32, accuracy: float32, threshold: float32)>, 'mesh_query_ray': <Function mesh_query_ray(id: uint64, start: vec3f, dir: vec3f, max_t: float32, t: float32, bary_u: float32, bary_v: float32, sign: float32, normal: vec3f, face: int32)>, 'mesh_query_aabb': <Function mesh_query_aabb(id: uint64, low: vec3f, high: vec3f)>, 'mesh_query_aabb_next': <Function mesh_query_aabb_next(query: warp.types.mesh_query_aabb_t, index: int32)>, 'mesh_eval_position': <Function mesh_eval_position(id: uint64, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_eval_velocity': <Function mesh_eval_velocity(id: uint64, face: int32, bary_u: float32, bary_v: float32)>, 'hash_grid_query': <Function hash_grid_query(id: uint64, point: vec3f, max_dist: float32)>, 'hash_grid_query_next': <Function hash_grid_query_next(query: warp.types.hash_grid_query_t, index: int32)>, 'hash_grid_point_id': <Function hash_grid_point_id(id: uint64, index: int32)>, 'intersect_tri_tri': <Function intersect_tri_tri(v0: vec3f, v1: vec3f, v2: vec3f, u0: vec3f, u1: vec3f, u2: vec3f)>, 'mesh_get': <Function mesh_get(id: uint64)>, 'mesh_eval_face_normal': <Function mesh_eval_face_normal(id: uint64, face: int32)>, 'mesh_get_point': <Function mesh_get_point(id: uint64, index: int32)>, 'mesh_get_velocity': <Function mesh_get_velocity(id: uint64, index: int32)>, 'mesh_get_index': <Function mesh_get_index(id: uint64, index: int32)>, 'closest_point_edge_edge': <Function closest_point_edge_edge(p1: vec3f, q1: vec3f, p2: vec3f, q2: vec3f, epsilon: float32)>, 'range': <Function range(end: int32)>, 'iter_next': <Function iter_next(range: warp.types.range_t)>, 'reversed': <Function reversed(range: warp.types.range_t)>, 'volume_sample': <Function volume_sample(id: uint64, uvw: vec3f, sampling_mode: int32, dtype: typing.Any)>, 'volume_sample_grad': <Function volume_sample_grad(id: uint64, uvw: vec3f, sampling_mode: int32, grad: typing.Any, dtype: typing.Any)>, 'volume_lookup': <Function volume_lookup(id: uint64, i: int32, j: int32, k: int32, dtype: typing.Any)>, 'volume_store': <Function volume_store(id: uint64, i: int32, j: int32, k: int32, value: typing.Any)>, 'volume_sample_f': <Function volume_sample_f(id: uint64, uvw: vec3f, sampling_mode: int32)>, 'volume_sample_grad_f': <Function volume_sample_grad_f(id: uint64, uvw: vec3f, sampling_mode: int32, grad: vec3f)>, 'volume_lookup_f': <Function volume_lookup_f(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_f': <Function volume_store_f(id: uint64, i: int32, j: int32, k: int32, value: float32)>, 'volume_sample_v': <Function volume_sample_v(id: uint64, uvw: vec3f, sampling_mode: int32)>, 'volume_lookup_v': <Function volume_lookup_v(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_v': <Function volume_store_v(id: uint64, i: int32, j: int32, k: int32, value: vec3f)>, 'volume_sample_i': <Function volume_sample_i(id: uint64, uvw: vec3f)>, 'volume_lookup_i': <Function volume_lookup_i(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_i': <Function volume_store_i(id: uint64, i: int32, j: int32, k: int32, value: int32)>, 'volume_sample_index': <Function volume_sample_index(id: uint64, uvw: vec3f, sampling_mode: int32, voxel_data: array(ndim=1, dtype=typing.Any), background: typing.Any)>, 'volume_sample_grad_index': <Function volume_sample_grad_index(id: uint64, uvw: vec3f, sampling_mode: int32, voxel_data: array(ndim=1, dtype=typing.Any), background: typing.Any, grad: typing.Any)>, 'volume_lookup_index': <Function volume_lookup_index(id: uint64, i: int32, j: int32, k: int32)>, 'volume_index_to_world': <Function volume_index_to_world(id: uint64, uvw: vec3f)>, 'volume_world_to_index': <Function volume_world_to_index(id: uint64, xyz: vec3f)>, 'volume_index_to_world_dir': <Function volume_index_to_world_dir(id: uint64, uvw: vec3f)>, 'volume_world_to_index_dir': <Function volume_world_to_index_dir(id: uint64, xyz: vec3f)>, 'rand_init': <Function rand_init(seed: int32)>, 'randi': <Function randi(state: uint32)>, 'randu': <Function randu(state: uint32)>, 'randf': <Function randf(state: uint32)>, 'randn': <Function randn(state: uint32)>, 'sample_cdf': <Function sample_cdf(state: uint32, cdf: array(ndim=1, dtype=float32))>, 'sample_triangle': <Function sample_triangle(state: uint32)>, 'sample_unit_ring': <Function sample_unit_ring(state: uint32)>, 'sample_unit_disk': <Function sample_unit_disk(state: uint32)>, 'sample_unit_sphere_surface': <Function sample_unit_sphere_surface(state: uint32)>, 'sample_unit_sphere': <Function sample_unit_sphere(state: uint32)>, 'sample_unit_hemisphere_surface': <Function sample_unit_hemisphere_surface(state: uint32)>, 'sample_unit_hemisphere': <Function sample_unit_hemisphere(state: uint32)>, 'sample_unit_square': <Function sample_unit_square(state: uint32)>, 'sample_unit_cube': <Function sample_unit_cube(state: uint32)>, 'poisson': <Function poisson(state: uint32, lam: float32)>, 'noise': <Function noise(state: uint32, x: float32)>, 'pnoise': <Function pnoise(state: uint32, x: float32, px: int32)>, 'curlnoise': <Function curlnoise(state: uint32, xy: vec2f, octaves: uint32, lacunarity: float32, gain: float32)>, 'printf': <Function printf(fmt: builtins.str, *args: typing.Any)>, 'print': <Function print(value: typing.Any)>, 'breakpoint': <Function breakpoint()>, 'tid': <Function tid()>, 'copy': <Function copy(a: typing.Any)>, 'select': <Function select(cond: warp.types.bool, value_if_false: typing.Any, value_if_true: typing.Any)>, 'where': <Function where(cond: warp.types.bool, value_if_true: typing.Any, value_if_false: typing.Any)>, 'array': <Function array(ptr: uint64, shape: typing.Tuple, dtype: warp.types.Scalar)>, 'address': <Function address(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int, l: warp.types.Int)>, 'view': <Function view(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int)>, 'array_store': <Function array_store(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, value: typing.Any)>, 'store': <Function store(address: typing.Any, value: typing.Any)>, 'load': <Function load(address: typing.Any)>, 'atomic_add': <Function atomic_add(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_sub': <Function atomic_sub(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_min': <Function atomic_min(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_max': <Function atomic_max(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'extract': <Function extract(a: vector(length=2, dtype=float16), i: int32)>, 'index': <Function index(a: vector(length=2, dtype=float16), i: int32)>, 'indexref': <Function indexref(a: vector(length=2, dtype=float16), i: int32)>, 'assign_inplace': <Function assign_inplace(a: vector(length=2, dtype=float16), i: int32, value: float16)>, 'assign_copy': <Function assign_copy(a: vector(length=2, dtype=float16), i: int32, value: float16)>, 'add_inplace': <Function add_inplace(a: vector(length=2, dtype=float16), i: int32, value: float16)>, 'sub_inplace': <Function sub_inplace(a: vector(length=2, dtype=float16), i: int32, value: float16)>, 'expect_eq': <Function expect_eq(a: int8, b: int8)>, 'expect_neq': <Function expect_neq(a: int8, b: int8)>, 'lerp': <Function lerp(a: float16, b: float16, t: float16)>, 'smoothstep': <Function smoothstep(a: float16, b: float16, x: float16)>, 'expect_near': <Function expect_near(a: float16, b: float16, tolerance: float16)>, 'lower_bound': <Function lower_bound(arr: array(ndim=1, dtype=warp.types.Scalar), value: float16)>, 'add': <Function add(a: float16, b: float16)>, 'sub': <Function sub(a: float16, b: float16)>, 'bit_and': <Function bit_and(a: int16, b: int16)>, 'bit_or': <Function bit_or(a: int16, b: int16)>, 'bit_xor': <Function bit_xor(a: int16, b: int16)>, 'lshift': <Function lshift(a: int16, b: int16)>, 'rshift': <Function rshift(a: int16, b: int16)>, 'invert': <Function invert(a: int16)>, 'mul': <Function mul(a: float16, b: float16)>, 'mod': <Function mod(a: float16, b: float16)>, 'div': <Function div(a: float16, b: float16)>, 'floordiv': <Function floordiv(a: float16, b: float16)>, 'pos': <Function pos(x: float16)>, 'neg': <Function neg(x: float16)>, 'unot': <Function unot(a: warp.types.bool)>, 'tile_diag_add': <Function tile_diag_add(a: tile(shape=typing.Any, dtype=typing.Any), d: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_matmul': <Function tile_matmul(a: tile(shape=typing.Any, dtype=typing.Any), b: tile(shape=typing.Any, dtype=typing.Any), out: tile(shape=typing.Any, dtype=typing.Any))>, 'tile_fft': <Function tile_fft(inout: warp.types.Tile)>, 'tile_ifft': <Function tile_ifft(inout: warp.types.Tile)>, 'tile_cholesky': <Function tile_cholesky(A: warp.types.Tile)>, 'tile_cholesky_solve': <Function tile_cholesky_solve(L: warp.types.Tile, x: warp.types.Tile)>, 'static': <Function static(expr: typing.Any)>, 'len': <Function len(a: vector(length=0, dtype=warp.types.Scalar))>, 'norm_l1': <Function norm_l1(v: typing.Any)>, 'norm_l2': <Function norm_l2(v: typing.Any)>, 'norm_huber': <Function norm_huber(v: typing.Any, delta: builtins.float)>, 'norm_pseudo_huber': <Function norm_pseudo_huber(v: typing.Any, delta: builtins.float)>, 'smooth_normalize': <Function smooth_normalize(v: typing.Any, delta: builtins.float)>, 'transform_from_matrix': <Function transform_from_matrix(mat: mat44(f))>, 'transform_to_matrix': <Function transform_to_matrix(xform: transformf)>}
complex_type_hints: tuple  # value = (typing.Any, typing.Callable, typing.Tuple)
function_key_counts: dict = {'quat_between_vectors': 1, 'norm_l1': 1, 'norm_l2': 1, 'norm_huber': 1, 'norm_pseudo_huber': 1, 'smooth_normalize': 1, 'transform_from_matrix': 3, 'transform_to_matrix': 3, '_decompose': 1, 'frac': 1, 'sqr': 1, 'alpha_beta_spectrum': 1, 'jonswap_peak_sharpening': 1, 'jonswap_spectrum': 1, 'TMA_spectrum': 1, '_define_face': 1, '_set_face_normals': 1, '_set_face_uvs': 1, 'sdf_create_box': 1, 'sdf_create_torus': 1, 'sdf_translate': 1, 'sdf_rotate': 1, 'sdf_smooth_min': 1, 'intersect_ray_sphere': 1, 'sample_height': 1, 'laplacian': 1, 'lookup_float': 3, 'sample_float': 3, 'clip_segment': 2, 'clip_normal': 2, 'velocity_at_point': 1, 'quat_twist': 1, 'quat_twist_angle': 1, 'quat_decompose': 1, 'quat_to_rpy': 1, 'quat_to_euler': 1, 'quat_from_euler': 1, 'transform_twist': 2, 'transform_wrench': 2, 'transform_inertia': 1, 'boltzmann': 1, 'smooth_max': 1, 'smooth_min': 1, 'leaky_max': 1, 'leaky_min': 1, 'vec_min': 1, 'vec_max': 1, 'vec_leaky_min': 1, 'vec_leaky_max': 1, 'vec_abs': 1, 'compute_2d_rotational_dofs': 1, 'invert_2d_rotational_dofs': 1, 'compute_3d_rotational_dofs': 1, 'invert_3d_rotational_dofs': 1, 'eval_single_articulation_fk': 1, 'reconstruct_angular_q_qd': 1, 'triangle_inertia': 1, 'build_orthonormal_basis': 2, 'triangle_closest_point_barycentric': 1, 'triangle_closest_point': 1, 'sphere_sdf': 1, 'sphere_sdf_grad': 1, 'box_sdf': 1, 'box_sdf_grad': 1, 'capsule_sdf': 1, 'capsule_sdf_grad': 1, 'cylinder_sdf': 1, 'cylinder_sdf_grad': 1, 'cone_sdf': 1, 'cone_sdf_grad': 1, 'plane_sdf': 1, 'closest_point_plane': 1, 'closest_point_line_segment': 1, 'closest_point_box': 1, 'get_box_vertex': 1, 'get_box_edge': 1, 'get_plane_edge': 1, 'closest_edge_coordinate_box': 1, 'closest_edge_coordinate_plane': 1, 'closest_edge_coordinate_capsule': 1, 'mesh_sdf': 1, 'closest_point_mesh': 1, 'closest_edge_coordinate_mesh': 1, 'volume_grad': 1, 'counter_increment': 1, 'replay_counter_increment': 1, 'limited_counter_increment': 1, 'replay_limited_counter_increment': 1, 'compute_tri_aabb': 1, 'tri_is_neighbor': 1, 'vertex_adjacent_to_triangle': 1, 'get_vertex_colliding_triangles_count': 1, 'get_vertex_colliding_triangles': 1, 'get_triangle_colliding_vertices_count': 1, 'get_triangle_colliding_vertices': 1, 'get_edge_colliding_edges_count': 1, 'get_edge_colliding_edges': 1, 'integrate_rigid_body': 1, 'particle_force': 1, 'eval_joint_force': 1, 'compute_muscle_force': 1, 'spatial_adjoint': 1, 'spatial_transform_inertia': 1, 'jcalc_transform': 1, 'jcalc_motion': 1, 'jcalc_tau': 1, 'jcalc_integrate': 1, 'compute_link_transform': 1, 'spatial_cross': 1, 'spatial_cross_dual': 1, 'dense_index': 1, 'compute_link_velocity': 1, 'spatial_mass': 1, 'dense_gemm': 1, 'dense_cholesky': 1, 'dense_subs': 1, 'dense_solve': 1, 'get_vertex_num_adjacent_edges': 1, 'get_vertex_adjacent_edge_id_order': 1, 'get_vertex_num_adjacent_faces': 1, 'get_vertex_adjacent_face_id_order': 1, 'calculate_triangle_deformation_gradient': 1, 'green_strain': 1, 'assemble_membrane_hessian': 1, 'evaluate_stvk_force_hessian': 1, 'mat_vec_cross_from_3_basis': 1, 'mat_vec_cross': 1, 'evaluate_dihedral_angle_based_bending_force_hessian': 1, 'evaluate_ground_contact_force_hessian': 1, 'evaluate_body_particle_contact': 1, 'evaluate_self_contact_force_norm': 1, 'evaluate_edge_edge_contact': 1, 'evaluate_vertex_triangle_collision_force_hessian': 1, 'compute_friction': 1, 'apply_conservative_bound_truncation': 1, 'update_joint_axis_mode': 1, 'update_joint_axis_limits': 1, 'update_joint_axis_target_ke_kd': 1, 'compute_linear_correction_3d': 1, 'compute_angular_correction_3d': 1, 'compute_contact_constraint_delta': 1, 'compute_positional_correction': 1, 'compute_angular_correction': 1}
generic_vtypes: tuple = (warp.types.mat22h, warp.types.mat22f, warp.types.mat22d, warp.types.mat33h, warp.types.mat33f, warp.types.mat33d, warp.types.mat44h, warp.types.mat44f, warp.types.mat44d, warp.types.spatial_matrixh, warp.types.spatial_matrixf, warp.types.spatial_matrixd, warp.types.quath, warp.types.quatf, warp.types.quatd, warp.types.transformh, warp.types.transformf, warp.types.transformd, warp.types.vec2h, warp.types.vec2f, warp.types.vec2d, warp.types.vec2s, warp.types.vec2i, warp.types.vec2l, warp.types.vec2b, warp.types.vec2us, warp.types.vec2ui, warp.types.vec2ul, warp.types.vec2ub, warp.types.vec3h, warp.types.vec3f, warp.types.vec3d, warp.types.vec3s, warp.types.vec3i, warp.types.vec3l, warp.types.vec3b, warp.types.vec3us, warp.types.vec3ui, warp.types.vec3ul, warp.types.vec3ub, warp.types.vec4h, warp.types.vec4f, warp.types.vec4d, warp.types.vec4s, warp.types.vec4i, warp.types.vec4l, warp.types.vec4b, warp.types.vec4us, warp.types.vec4ui, warp.types.vec4ul, warp.types.vec4ub, warp.types.spatial_vectorh, warp.types.spatial_vectorf, warp.types.spatial_vectord)
runtime: Runtime  # value = <warp.context.Runtime object>
scalar_types: dict = {warp.types.int8: warp.types.int8, warp.types.uint8: warp.types.uint8, warp.types.int16: warp.types.int16, warp.types.uint16: warp.types.uint16, warp.types.int32: warp.types.int32, warp.types.uint32: warp.types.uint32, warp.types.int64: warp.types.int64, warp.types.uint64: warp.types.uint64, warp.types.float16: warp.types.float16, warp.types.float32: warp.types.float32, warp.types.float64: warp.types.float64, warp.types.vec2b: warp.types.int8, warp.types.vec2ub: warp.types.uint8, warp.types.vec2s: warp.types.int16, warp.types.vec2us: warp.types.uint16, warp.types.vec2i: warp.types.int32, warp.types.vec2ui: warp.types.uint32, warp.types.vec2l: warp.types.int64, warp.types.vec2ul: warp.types.uint64, warp.types.vec2h: warp.types.float16, warp.types.vec2f: warp.types.float32, warp.types.vec2d: warp.types.float64, warp.types.vec3b: warp.types.int8, warp.types.vec3ub: warp.types.uint8, warp.types.vec3s: warp.types.int16, warp.types.vec3us: warp.types.uint16, warp.types.vec3i: warp.types.int32, warp.types.vec3ui: warp.types.uint32, warp.types.vec3l: warp.types.int64, warp.types.vec3ul: warp.types.uint64, warp.types.vec3h: warp.types.float16, warp.types.vec3f: warp.types.float32, warp.types.vec3d: warp.types.float64, warp.types.vec4b: warp.types.int8, warp.types.vec4ub: warp.types.uint8, warp.types.vec4s: warp.types.int16, warp.types.vec4us: warp.types.uint16, warp.types.vec4i: warp.types.int32, warp.types.vec4ui: warp.types.uint32, warp.types.vec4l: warp.types.int64, warp.types.vec4ul: warp.types.uint64, warp.types.vec4h: warp.types.float16, warp.types.vec4f: warp.types.float32, warp.types.vec4d: warp.types.float64, warp.types.mat22h: warp.types.float16, warp.types.mat22f: warp.types.float32, warp.types.mat22d: warp.types.float64, warp.types.mat33h: warp.types.float16, warp.types.mat33f: warp.types.float32, warp.types.mat33d: warp.types.float64, warp.types.mat44h: warp.types.float16, warp.types.mat44f: warp.types.float32, warp.types.mat44d: warp.types.float64, warp.types.quath: warp.types.float16, warp.types.quatf: warp.types.float32, warp.types.quatd: warp.types.float64, warp.types.transformh: warp.types.float16, warp.types.transformf: warp.types.float32, warp.types.transformd: warp.types.float64, warp.types.spatial_vectorh: warp.types.float16, warp.types.spatial_vectorf: warp.types.float32, warp.types.spatial_vectord: warp.types.float64, warp.types.spatial_matrixh: warp.types.float16, warp.types.spatial_matrixf: warp.types.float32, warp.types.spatial_matrixd: warp.types.float64}
sequence_types: tuple = (list, tuple)
user_modules: dict  # value = {'warp.utils': <warp.context.Module object>, 'warp.math': <warp.context.Module object>, 'isaacsim.core.utils.warp.rotations': <warp.context.Module object>, 'isaacsim.core.utils.warp.tensor': <warp.context.Module object>, 'isaacsim.core.utils.warp.transformations': <warp.context.Module object>, 'isaacsim.core.experimental.utils.impl.ops': <warp.context.Module object>, 'isaacsim.core.experimental.prims.impl._fabric': <warp.context.Module object>, 'isaacsim.core.utils.fabric': <warp.context.Module object>, 'omni.warp.nodes._impl.points': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleOceanDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.kernels.grid_create': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnParticlesSimulate': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleProceduralVolume': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnClothSimulate': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnNoiseDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSamplePrimFlocking': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleMeshDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnWaveSolve': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnParticlesFromMesh': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnMeshFromVolume': <warp.context.Module object>, 'omni.replicator.core.scripts.utils.wp_utils': <warp.context.Module object>, 'omni.replicator.core.scripts.augmentations_default': <warp.context.Module object>, 'omni.replicator.core.scripts.functional.modify': <warp.context.Module object>, 'omni.replicator.core.scripts.utils.mesh_decal': <warp.context.Module object>, 'warp.sim.utils': <warp.context.Module object>, 'warp.sim.articulation': <warp.context.Module object>, 'warp.sim.graph_coloring': <warp.context.Module object>, 'warp.sim.inertia': <warp.context.Module object>, 'warp.sim.model': <warp.context.Module object>, 'warp.sim.collide': <warp.context.Module object>, 'warp.sim.integrator': <warp.context.Module object>, 'warp.sim.particles': <warp.context.Module object>, 'warp.sim.integrator_euler': <warp.context.Module object>, 'warp.sim.integrator_featherstone': <warp.context.Module object>, 'isaacsim.sensors.camera.camera_view': <warp.context.Module object>, 'warp.sim.integrator_vbd': <warp.context.Module object>, 'warp.sim.integrator_xpbd': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnDecal': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugImgBlendExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugCutMixExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugShadeSegmentation': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugBgRandExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugCropResizeExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnSemanticSegmentation': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugRotateExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugContrastExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugCanny': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnPointCloudGenerator': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugPixellateExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugConv2dExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugMotionBlurExp': <warp.context.Module object>}
