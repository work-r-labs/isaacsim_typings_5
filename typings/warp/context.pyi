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
import numpy
import numpy as np
import operator as operator
import os as os
from pathlib import Path
import platform as platform
import sys as sys
import types as types
import typing as typing
import warp as warp
import weakref as weakref
__all__ = ['ContextGuard', 'CpuDefaultAllocator', 'CpuPinnedAllocator', 'CudaDefaultAllocator', 'CudaMempoolAllocator', 'Device', 'Devicelike', 'Event', 'Function', 'Graph', 'Kernel', 'KernelHooks', 'Launch', 'Module', 'ModuleBuilder', 'ModuleExec', 'ModuleHasher', 'Path', 'RegisteredGLBuffer', 'Runtime', 'Stream', 'add_builtin', 'adj_copy', 'ast', 'builtin_functions', 'call_builtin', 'capture_begin', 'capture_end', 'capture_launch', 'clone', 'complex_type_hints', 'copy', 'create_value_func', 'ctypes', 'empty', 'empty_like', 'export_builtins', 'export_functions_rst', 'export_stubs', 'force_load', 'from_numpy', 'full', 'full_like', 'func', 'func_grad', 'func_native', 'func_replay', 'function_key_counts', 'functools', 'generate_unique_function_identifier', 'generic_vtypes', 'get_cuda_device', 'get_cuda_device_count', 'get_cuda_devices', 'get_device', 'get_devices', 'get_event_elapsed_time', 'get_function_args', 'get_generic_vtypes', 'get_mempool_release_threshold', 'get_module', 'get_module_options', 'get_preferred_device', 'get_stream', 'hashlib', 'init', 'inspect', 'io', 'is_cpu_available', 'is_cuda_available', 'is_cuda_driver_initialized', 'is_device_available', 'is_mempool_access_enabled', 'is_mempool_access_supported', 'is_mempool_enabled', 'is_mempool_supported', 'is_peer_access_enabled', 'is_peer_access_supported', 'itertools', 'json', 'kernel', 'launch', 'launch_tiled', 'load_module', 'map_cuda_device', 'np', 'ones', 'ones_like', 'operator', 'os', 'overload', 'pack_arg', 'platform', 'print_function', 'record_event', 'runtime', 'scalar_types', 'sequence_types', 'set_device', 'set_mempool_access_enabled', 'set_mempool_enabled', 'set_mempool_release_threshold', 'set_module_options', 'set_peer_access_enabled', 'set_stream', 'shallowcopy', 'struct', 'synchronize', 'synchronize_device', 'synchronize_event', 'synchronize_stream', 'sys', 'type_str', 'types', 'typing', 'unmap_cuda_device', 'user_modules', 'wait_event', 'wait_stream', 'warp', 'weakref', 'zeros', 'zeros_like']
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
            ordinal: A Warp-specific integer label for the device. ``-1`` for CPU devices.
            name: A string label for the device. By default, CPU devices will be named according to the processor name,
                or ``"CPU"`` if the processor name cannot be determined.
            arch: An integer representing the compute capability version number calculated as
                ``10 * major + minor``. ``0`` for CPU devices.
            is_uva: A boolean indicating whether the device supports unified addressing.
                ``False`` for CPU devices.
            is_cubin_supported: A boolean indicating whether Warp's version of NVRTC can directly
                generate CUDA binary files (cubin) for this device's architecture. ``False`` for CPU devices.
            is_mempool_supported: A boolean indicating whether the device supports using the
                ``cuMemAllocAsync`` and ``cuMemPool`` family of APIs for stream-ordered memory allocations. ``False`` for
                CPU devices.
            is_primary: A boolean indicating whether this device's CUDA context is also the
                device's primary context.
            uuid: A string representing the UUID of the CUDA device. The UUID is in the same format used by
                ``nvidia-smi -L``. ``None`` for CPU devices.
            pci_bus_id: A string identifier for the CUDA device in the format ``[domain]:[bus]:[device]``, in which
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
    @classmethod
    def __new__(cls, *args, **kwargs):
        """
        Creates a new event instance.
        """
    def __del__(self):
        ...
    def __init__(self, device: Devicelike = None, cuda_event = None, enable_timing: bool = False):
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
                
        """
class Function:
    def __call__(self, *args, **kwargs):
        ...
    def __init__(self, func, key, namespace, input_types = None, value_type = None, value_func = None, export_func = None, dispatch_func = None, lto_dispatch_func = None, module = None, variadic = False, initializer_list_func = None, export = False, doc = '', group = '', hidden = False, skip_replay = False, missing_grad = False, generic = False, native_func = None, defaults = None, custom_replay_func = None, native_snippet = None, adj_native_snippet = None, replay_snippet = None, skip_forward_codegen = False, skip_reverse_codegen = False, custom_reverse_num_input_args = -1, custom_reverse_mode = False, overloaded_annotations = None, code_transformers = None, skip_adding_overload = False, require_original_output_arg = False, scope_locals = None):
        ...
    def __repr__(self):
        ...
    def add_overload(self, f):
        ...
    def get_overload(self, arg_types, kwarg_types):
        ...
    def is_builtin(self):
        ...
    def is_simple(self):
        ...
    def mangle(self):
        ...
class Graph:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, device: Device, capture_id: int):
        ...
    def retain_module_exec(self, module_exec: ModuleExec):
        ...
class Kernel:
    __slotnames__: typing.ClassVar[list] = list()
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
    def __init__(self, kernel, device, hooks = None, params = None, params_addr = None, bounds = None, max_blocks = 0, block_dim = 256):
        ...
    def launch(self, stream = None) -> typing.Any:
        ...
    def set_dim(self, dim):
        ...
    def set_param_at_index(self, index, value):
        ...
    def set_param_at_index_from_ctype(self, index, value):
        ...
    def set_param_by_name(self, name, value):
        ...
    def set_param_by_name_from_ctype(self, name, value):
        ...
    def set_params(self, values):
        ...
    def set_params_from_ctypes(self, values):
        ...
class Module:
    def __init__(self, name, loader):
        ...
    def find_kernel(self, func):
        ...
    def find_references(self, adj):
        ...
    def get_kernel_hooks(self, kernel, device):
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
    def get_kernel_hooks(self, kernel):
        ...
class ModuleHasher:
    def __init__(self, module):
        ...
    def get_constant_bytes(self, value):
        ...
    def get_module_hash(self):
        ...
    def get_unique_kernels(self):
        ...
    def hash_adjoint(self, adj):
        ...
    def hash_function(self, func):
        ...
    def hash_kernel(self, kernel):
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
    def __init__(self, gl_buffer_id: int, device: typing.Union[warp.context.Device, str, NoneType] = None, flags: int = 0, fallback_to_copy: bool = True):
        """
        
                Args:
                    gl_buffer_id: The OpenGL buffer id (GLuint).
                    device: The device to register the buffer with.  If None, the current device will be used.
                    flags: A combination of the flags constants :attr:`NONE`, :attr:`READ_ONLY`, and :attr:`WRITE_DISCARD`.
                    fallback_to_copy: If True and CUDA/OpenGL interop is not available, fall back to copy operations between the Warp array and the OpenGL buffer. Otherwise, a ``RuntimeError`` will be raised.
        
                Note:
        
                    The ``fallback_to_copy`` option (to use copy operations if CUDA graphics interop functionality is not available) requires pyglet version 2.0 or later. Install via ``pip install pyglet==2.*``.
                
        """
    def map(self, dtype, shape) -> warp.types.array:
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
    def get_device(self, ident: typing.Union[warp.context.Device, str, NoneType] = None) -> Device:
        ...
    def get_error_string(self):
        ...
    def load_dll(self, dll_path):
        ...
    def map_cuda_device(self, alias, context = None) -> Device:
        ...
    def rename_device(self, device, alias) -> Device:
        ...
    def set_default_device(self, ident: typing.Union[warp.context.Device, str, NoneType]) -> None:
        ...
    def unmap_cuda_device(self, alias) -> None:
        ...
    def verify_cuda_device(self, device: typing.Union[warp.context.Device, str, NoneType] = None) -> None:
        ...
class Stream:
    @classmethod
    def __new__(cls, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, device: typing.Union[ForwardRef('Device'), str, NoneType] = None, priority: int = 0, **kwargs):
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
                      :class:`Device``.
                    RuntimeError: ``device`` is not a CUDA Device.
                    RuntimeError: The stream could not be created on the device.
                    TypeError: The requested stream priority is not an integer.
                
        """
    def record_event(self, event: typing.Optional[warp.context.Event] = None) -> Event:
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
    def wait_stream(self, other_stream: Stream, event: typing.Optional[warp.context.Event] = None):
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
    def priority(self) -> int:
        """
        An integer representing the priority of the stream.
        """
def add_builtin(key, input_types = None, constraint = None, value_type = None, value_func = None, export_func = None, dispatch_func = None, lto_dispatch_func = None, doc = '', namespace = 'wp::', variadic = False, initializer_list_func = None, export = True, group = 'Other', hidden = False, skip_replay = False, missing_grad = False, native_func = None, defaults = None, require_original_output_arg = False):
    """
    Main entry point to register a new built-in function.
    
        Args:
            key (str): Function name. Multiple overloaded functions can be registered
                under the same name as long as their signature differ.
            input_types (Mapping[str, Any]): Signature of the user-facing function.
                Variadic arguments are supported by prefixing the parameter names
                with asterisks as in `*args` and `**kwargs`. Generic arguments are
                supported with types such as `Any`, `Float`, `Scalar`, etc.
            constraint (Callable): For functions that define generic arguments and
                are to be exported, this callback is used to specify whether some
                combination of inferred arguments are valid or not.
            value_type (Any): Type returned by the function.
            value_func (Callable): Callback used to specify the return type when
                `value_type` isn't enough.
            export_func (Callable): Callback used during the context stage to specify
                the signature of the underlying C++ function, not accounting for
                the template parameters.
                If not provided, `input_types` is used.
            dispatch_func (Callable): Callback used during the codegen stage to specify
                the runtime and template arguments to be passed to the underlying C++
                function. In other words, this allows defining a mapping between
                the signatures of the user-facing and the C++ functions, and even to
                dynamically create new arguments on the fly.
                The arguments returned must be of type `codegen.Var`.
                If not provided, all arguments passed by the users when calling
                the built-in are passed as-is as runtime arguments to the C++ function.
            lto_dispatch_func (Callable): Same as dispatch_func, but takes an 'option' dict
                as extra argument (indicating tile_size and target architecture) and returns
                an LTO-IR buffer as extra return value
            doc (str): Used to generate the Python's docstring and the HTML documentation.
            namespace: Namespace for the underlying C++ function.
            variadic (bool): Whether the function declares variadic arguments.
            initializer_list_func (bool): Whether to use the initializer list syntax
                when passing the arguments to the underlying C++ function.
            export (bool): Whether the function is to be exposed to the Python
                interpreter so that it becomes available from within the `warp`
                module.
            group (str): Classification used for the documentation.
            hidden (bool): Whether to add that function into the documentation.
            skip_replay (bool): Whether operation will be performed during
                the forward replay in the backward pass.
            missing_grad (bool): Whether the function is missing a corresponding
                adjoint.
            native_func (str): Name of the underlying C++ function.
            defaults (Mapping[str, Any]): Default values for the parameters defined
                in `input_types`.
            require_original_output_arg (bool): Used during the codegen stage to
                specify whether an adjoint parameter corresponding to the return
                value should be included in the signature of the backward function.
        
    """
def adj_copy(adj_dest: warp.types.array, adj_src: warp.types.array, dest_offset: int, src_offset: int, count: int, stream: Stream = None):
    """
    Copy adjoint operation for wp.copy() calls on the tape.
    
        Args:
            adj_dest: Destination array adjoint
            adj_src: Source array adjoint
            stream: The stream on which the copy was performed in the forward pass
        
    """
def call_builtin(func: Function, *params) -> typing.Tuple[bool, typing.Any]:
    ...
def capture_begin(device: typing.Union[warp.context.Device, str, NoneType] = None, stream = None, force_module_load = None, external = False):
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
def capture_end(device: typing.Union[warp.context.Device, str, NoneType] = None, stream: Stream = None) -> Graph:
    """
    Ends the capture of a CUDA graph
    
        Args:
    
            device: The CUDA device where capture began
            stream: The CUDA stream where capture began
    
        Returns:
            A Graph object that can be launched with :func:`~warp.capture_launch()`
        
    """
def capture_launch(graph: Graph, stream: Stream = None):
    """
    Launch a previously captured CUDA graph
    
        Args:
            graph: A Graph as returned by :func:`~warp.capture_end()`
            stream: A Stream to launch the graph on (optional)
        
    """
def clone(src: warp.types.array, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = None, pinned: bool = None) -> warp.types.array:
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
def copy(dest: warp.types.array, src: warp.types.array, dest_offset: int = 0, src_offset: int = 0, count: int = 0, stream: Stream = None):
    """
    Copy array contents from `src` to `dest`.
    
        Args:
            dest: Destination array, must be at least as big as source buffer
            src: Source array
            dest_offset: Element offset in the destination array
            src_offset: Element offset in the source array
            count: Number of array elements to copy (will copy all elements if set to 0)
            stream: The stream on which to perform the copy (optional)
    
        The stream, if specified, can be from any device.  If the stream is omitted, then Warp selects a stream based on the following rules:
        (1) If the destination array is on a CUDA device, use the current stream on the destination device.
        (2) Otherwise, if the source array is on a CUDA device, use the current stream on the source device.
    
        If neither source nor destination are on a CUDA device, no stream is used for the copy.
    
        
    """
def create_value_func(type):
    ...
def empty(shape: typing.Tuple = None, dtype = float, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.types.array:
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
def empty_like(src: warp.types.array, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = None, pinned: bool = None) -> warp.types.array:
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
def export_builtins(file: io.TextIOBase):
    ...
def export_functions_rst(file):
    ...
def export_stubs(file):
    """
    Generates stub file for auto-complete of builtin functions
    """
def force_load(device: typing.Union[warp.context.Device, str, typing.List[warp.context.Device], typing.List[str]] = None, modules: typing.List[warp.context.Module] = None):
    """
    Force user-defined kernels to be compiled and loaded
    
        Args:
            device: The device or list of devices to load the modules on.  If None, load on all devices.
            modules: List of modules to load.  If None, load all imported modules.
        
    """
def from_numpy(arr: numpy.ndarray, dtype: typing.Optional[type] = None, shape: typing.Optional[typing.Sequence[int]] = None, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = False) -> warp.types.array:
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
def full(shape: typing.Tuple = None, value = 0, dtype = ..., device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.types.array:
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
def full_like(src: warp.types.array, value: typing.Any, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = None, pinned: bool = None) -> warp.types.array:
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
def func(f):
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
def func_native(snippet, adj_snippet = None, replay_snippet = None):
    """
    
        Decorator to register native code snippet, @func_native
        
    """
def func_replay(forward_fn):
    """
    
        Decorator to register a custom replay function for a given forward function.
        The replay function is the function version that is called in the forward phase of the backward pass (replay mode) and corresponds to the forward function by default.
        The provided function has to match the signature of one of the original forward function overloads.
        
    """
def generate_unique_function_identifier(key):
    ...
def get_cuda_device(ordinal: typing.Optional[int] = None) -> Device:
    """
    Returns the CUDA device with the given ordinal or the current CUDA device if ordinal is None.
    """
def get_cuda_device_count() -> int:
    """
    Returns the number of CUDA devices supported in this environment.
    """
def get_cuda_devices() -> typing.List[warp.context.Device]:
    """
    Returns a list of CUDA devices supported in this environment.
    """
def get_device(ident: typing.Union[warp.context.Device, str, NoneType] = None) -> Device:
    """
    Returns the device identified by the argument.
    """
def get_devices() -> typing.List[warp.context.Device]:
    """
    Returns a list of devices supported in this environment.
    """
def get_event_elapsed_time(start_event: Event, end_event: Event, synchronize: typing.Optional[bool] = True):
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
def get_mempool_release_threshold(device: typing.Union[warp.context.Device, str, NoneType]) -> int:
    """
    Get the CUDA memory pool release threshold on the device in bytes.
    """
def get_module(name):
    ...
def get_module_options(module: typing.Optional[typing.Any] = None) -> typing.Dict[str, typing.Any]:
    """
    Returns a list of options for the current module.
    """
def get_preferred_device() -> Device:
    """
    Returns the preferred compute device, ``cuda:0`` if available and ``cpu`` otherwise.
    """
def get_stream(device: typing.Union[warp.context.Device, str, NoneType] = None) -> Stream:
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
def is_mempool_access_enabled(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if `peer_device` can currently access the memory pool of `target_device`.
    
        This applies to memory allocated using CUDA pooled allocators.  For memory allocated using
        default CUDA allocators, use :func:`is_peer_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this peer access is currently enabled.
        
    """
def is_mempool_access_supported(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if `peer_device` can directly access the memory pool of `target_device`.
    
        If mempool access is possible, it can be managed using :func:`set_mempool_access_enabled()`
        and :func:`is_mempool_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this memory pool access is supported by the system.
        
    """
def is_mempool_enabled(device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if CUDA memory pool allocators are enabled on the device.
    """
def is_mempool_supported(device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if CUDA memory pool allocators are available on the device.
    """
def is_peer_access_enabled(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if `peer_device` can currently access the memory of `target_device`.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`is_mempool_access_enabled()`.
    
        Returns:
            A Boolean value indicating if this peer access is currently enabled.
        
    """
def is_peer_access_supported(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType]) -> bool:
    """
    Check if `peer_device` can directly access the memory of `target_device` on this system.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`is_mempool_access_supported()`.
    
        Returns:
            A Boolean value indicating if this peer access is supported by the system.
        
    """
def kernel(f = None, *, enable_backward = None):
    ...
def launch(kernel, dim: typing.Tuple[int], inputs: typing.Sequence = list(), outputs: typing.Sequence = list(), adj_inputs: typing.Sequence = list(), adj_outputs: typing.Sequence = list(), device: typing.Union[warp.context.Device, str, NoneType] = None, stream: Stream = None, adjoint = False, record_tape = True, record_cmd = False, max_blocks = 0, block_dim = 256):
    """
    Launch a Warp kernel on the target device
    
        Kernel launches are asynchronous with respect to the calling Python thread.
    
        Args:
            kernel: The name of a Warp kernel function, decorated with the ``@wp.kernel`` decorator
            dim: The number of threads to launch the kernel, can be an integer, or a Tuple of ints with max of 4 dimensions
            inputs: The input parameters to the kernel (optional)
            outputs: The output parameters (optional)
            adj_inputs: The adjoint inputs (optional)
            adj_outputs: The adjoint outputs (optional)
            device: The device to launch on (optional)
            stream: The stream to launch on (optional)
            adjoint: Whether to run forward or backward pass (typically use False)
            record_tape: When true the launch will be recorded the global wp.Tape() object when present
            record_cmd: When True the launch will be returned as a ``Launch`` command object, the launch will not occur until the user calls ``cmd.launch()``
            max_blocks: The maximum number of CUDA thread blocks to use. Only has an effect for CUDA kernel launches.
                If negative or zero, the maximum hardware value will be used.
            block_dim: The number of threads per block.
        
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
def load_module(module: typing.Union[warp.context.Module, module, str] = None, device: typing.Union[warp.context.Device, str] = None, recursive: bool = False):
    """
    Force user-defined module to be compiled and loaded
    
        Args:
            module: The module to load.  If None, load the current module.
            device: The device to load the modules on.  If None, load on all devices.
            recursive: Whether to load submodules.  E.g., if the given module is `warp.sim`, this will also load `warp.sim.model`, `warp.sim.articulation`, etc.
    
        Note: A module must be imported before it can be loaded by this function.
        
    """
def map_cuda_device(alias: str, context: ctypes.c_void_p = None) -> Device:
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
def ones(shape: typing.Tuple = None, dtype = float, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.types.array:
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
def ones_like(src: warp.types.array, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = None, pinned: bool = None) -> warp.types.array:
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
def record_event(event: typing.Optional[warp.context.Event] = None):
    """
    Convenience function for calling :meth:`Stream.record_event` on the current stream.
    
        Args:
            event: :class:`Event` instance to record. If ``None``, a new :class:`Event`
              instance will be created.
    
        Returns:
            The recorded event.
        
    """
def set_device(ident: typing.Union[warp.context.Device, str, NoneType]) -> None:
    """
    Sets the default device identified by the argument.
    """
def set_mempool_access_enabled(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType], enable: bool) -> None:
    """
    Enable or disable access from `peer_device` to the memory pool of `target_device`.
    
        This applies to memory allocated using CUDA pooled allocators.  For memory allocated using
        default CUDA allocators, use :func:`set_peer_access_enabled()`.
        
    """
def set_mempool_enabled(device: typing.Union[warp.context.Device, str, NoneType], enable: bool) -> None:
    """
    Enable or disable CUDA memory pool allocators on the device.
    
        Pooled allocators are typically faster and allow allocating memory during graph capture.
    
        They should generally be enabled, but there is a rare caveat.  Copying data between different GPUs
        may fail during graph capture if the memory was allocated using pooled allocators and memory pool
        access is not enabled between the two GPUs.  This is an internal CUDA limitation that is not related
        to Warp.  The preferred solution is to enable memory pool access using `warp.set_mempool_access_enabled()`.
        If peer access is not supported, then the default CUDA allocators must be used to pre-allocate the memory
        prior to graph capture.
        
    """
def set_mempool_release_threshold(device: typing.Union[warp.context.Device, str, NoneType], threshold: typing.Union[int, float]) -> None:
    """
    Set the CUDA memory pool release threshold on the device.
    
        This is the amount of reserved memory to hold onto before trying to release memory back to the OS.
        When more than this amount of bytes is held by the memory pool, the allocator will try to release
        memory back to the OS on the next call to stream, event, or device synchronize.
    
        Values between 0 and 1 are interpreted as fractions of available memory.  For example, 0.5 means
        half of the device's physical memory.  Greater values are interpreted as an absolute number of bytes.
        For example, 1024**3 means one GiB of memory.
        
    """
def set_module_options(options: typing.Dict[str, typing.Any], module: typing.Optional[typing.Any] = None):
    """
    Set options for the current module.
    
        Options can be used to control runtime compilation and code-generation
        for the current module individually. Available options are listed below.
    
        * **mode**: The compilation mode to use, can be "debug", or "release", defaults to the value of ``warp.config.mode``.
        * **max_unroll**: The maximum fixed-size loop to unroll, defaults to the value of ``warp.config.max_unroll``.
    
        Args:
    
            options: Set of key-value option pairs
        
    """
def set_peer_access_enabled(target_device: typing.Union[warp.context.Device, str, NoneType], peer_device: typing.Union[warp.context.Device, str, NoneType], enable: bool) -> None:
    """
    Enable or disable direct access from `peer_device` to the memory of `target_device`.
    
        Enabling peer access can improve the speed of peer-to-peer memory transfers, but can have
        a negative impact on memory consumption and allocation performance.
    
        This applies to memory allocated using default CUDA allocators.  For memory allocated using
        CUDA pooled allocators, use :func:`set_mempool_access_enabled()`.
        
    """
def set_stream(stream: Stream, device: typing.Union[warp.context.Device, str, NoneType] = None, sync: bool = False) -> None:
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
def struct(c):
    ...
def synchronize():
    """
    Manually synchronize the calling CPU thread with any outstanding CUDA work on all devices
    
        This method allows the host application code to ensure that any kernel launches
        or memory copies have completed.
        
    """
def synchronize_device(device: typing.Union[warp.context.Device, str, NoneType] = None):
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
def synchronize_stream(stream_or_device: typing.Union[warp.context.Stream, warp.context.Device, str, NoneType] = None):
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
def wait_stream(other_stream: Stream, event: Event = None):
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
def zeros(shape: typing.Tuple = None, dtype = float, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = False, pinned: bool = False, **kwargs) -> warp.types.array:
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
def zeros_like(src: warp.types.array, device: typing.Union[warp.context.Device, str, NoneType] = None, requires_grad: bool = None, pinned: bool = None) -> warp.types.array:
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
builtin_functions: dict  # value = {'min': <Function min(a: float16, b: float16)>, 'max': <Function max(a: float16, b: float16)>, 'clamp': <Function clamp(x: float16, low: float16, high: float16)>, 'abs': <Function abs(x: float16)>, 'sign': <Function sign(x: float16)>, 'step': <Function step(x: float16)>, 'nonzero': <Function nonzero(x: float16)>, 'sin': <Function sin(x: float16)>, 'cos': <Function cos(x: float16)>, 'acos': <Function acos(x: float16)>, 'asin': <Function asin(x: float16)>, 'sqrt': <Function sqrt(x: float16)>, 'cbrt': <Function cbrt(x: float16)>, 'tan': <Function tan(x: float16)>, 'atan': <Function atan(x: float16)>, 'atan2': <Function atan2(y: float16, x: float16)>, 'sinh': <Function sinh(x: float16)>, 'cosh': <Function cosh(x: float16)>, 'tanh': <Function tanh(x: float16)>, 'degrees': <Function degrees(x: float16)>, 'radians': <Function radians(x: float16)>, 'log': <Function log(x: float16)>, 'log2': <Function log2(x: float16)>, 'log10': <Function log10(x: float16)>, 'exp': <Function exp(x: float16)>, 'pow': <Function pow(x: float16, y: float16)>, 'round': <Function round(x: float16)>, 'rint': <Function rint(x: float16)>, 'trunc': <Function trunc(x: float16)>, 'floor': <Function floor(x: float16)>, 'ceil': <Function ceil(x: float16)>, 'frac': <Function frac(x: float16)>, 'isfinite': <Function isfinite(a: float16)>, 'isnan': <Function isnan(a: float16)>, 'isinf': <Function isinf(a: float16)>, 'dot': <Function dot(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'ddot': <Function ddot(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>), b: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'argmin': <Function argmin(a: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'argmax': <Function argmax(a: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'outer': <Function outer(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'cross': <Function cross(a: vector(length=3, dtype=<class 'warp.types.float16'>), b: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'skew': <Function skew(vec: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'length': <Function length(a: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'length_sq': <Function length_sq(a: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'normalize': <Function normalize(a: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'transpose': <Function transpose(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'inverse': <Function inverse(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'determinant': <Function determinant(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'trace': <Function trace(a: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'diag': <Function diag(vec: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'get_diag': <Function get_diag(mat: matrix(shape=(2, 2), dtype=<class 'warp.types.float16'>))>, 'cw_mul': <Function cw_mul(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'cw_div': <Function cw_div(a: vector(length=2, dtype=<class 'warp.types.float16'>), b: vector(length=2, dtype=<class 'warp.types.float16'>))>, 'int8': <Function int8(a: int8)>, 'uint8': <Function uint8(a: int8)>, 'int16': <Function int16(a: int8)>, 'uint16': <Function uint16(a: int8)>, 'int32': <Function int32(a: int8)>, 'uint32': <Function uint32(a: int8)>, 'int64': <Function int64(a: int8)>, 'uint64': <Function uint64(a: int8)>, 'float16': <Function float16(a: int8)>, 'float32': <Function float32(a: int8)>, 'float64': <Function float64(a: int8)>, 'bool': <Function bool(a: int8)>, 'int': <Function int(a: int8)>, 'float': <Function float(a: int8)>, 'vector': <Function vector(*args: warp.types.Scalar, length: int32, dtype: warp.types.Scalar)>, 'matrix': <Function matrix(*args: warp.types.Scalar, shape: typing.Tuple, dtype: warp.types.Scalar)>, 'identity': <Function identity(n: int32, dtype: warp.types.Scalar)>, 'svd3': <Function svd3(A: matrix(shape=(3, 3), dtype=~Float), U: matrix(shape=(3, 3), dtype=~Float), sigma: vector(length=3, dtype=~Float), V: matrix(shape=(3, 3), dtype=~Scalar))>, 'qr3': <Function qr3(A: matrix(shape=(3, 3), dtype=~Float), Q: matrix(shape=(3, 3), dtype=~Float), R: matrix(shape=(3, 3), dtype=~Float))>, 'eig3': <Function eig3(A: matrix(shape=(3, 3), dtype=~Float), Q: matrix(shape=(3, 3), dtype=~Float), d: vector(length=3, dtype=~Float))>, 'quaternion': <Function quaternion(dtype: warp.types.Float)>, 'quat_identity': <Function quat_identity(dtype: warp.types.Float)>, 'quat_from_axis_angle': <Function quat_from_axis_angle(axis: vector(length=3, dtype=<class 'warp.types.float16'>), angle: float16)>, 'quat_to_axis_angle': <Function quat_to_axis_angle(quat: warp.types.quath, axis: vector(length=3, dtype=<class 'warp.types.float16'>), angle: float16)>, 'quat_from_matrix': <Function quat_from_matrix(mat: matrix(shape=(3, 3), dtype=<class 'warp.types.float16'>))>, 'quat_rpy': <Function quat_rpy(roll: float16, pitch: float16, yaw: float16)>, 'quat_inverse': <Function quat_inverse(quat: warp.types.quath)>, 'quat_rotate': <Function quat_rotate(quat: warp.types.quath, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'quat_rotate_inv': <Function quat_rotate_inv(quat: warp.types.quath, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'quat_slerp': <Function quat_slerp(a: warp.types.quath, b: warp.types.quath, t: float16)>, 'quat_to_matrix': <Function quat_to_matrix(quat: warp.types.quath)>, 'transformation': <Function transformation(pos: vector(length=3, dtype=~Float), rot: warp.types.quaternion.<locals>.quat_t, dtype: warp.types.Float)>, 'transform_identity': <Function transform_identity(dtype: warp.types.Float)>, 'transform_get_translation': <Function transform_get_translation(xform: warp.types.transformh)>, 'transform_get_rotation': <Function transform_get_rotation(xform: warp.types.transformh)>, 'transform_multiply': <Function transform_multiply(a: warp.types.transformh, b: warp.types.transformh)>, 'transform_point': <Function transform_point(xform: warp.types.transformh, point: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'transform_vector': <Function transform_vector(xform: warp.types.transformh, vec: vector(length=3, dtype=<class 'warp.types.float16'>))>, 'transform_inverse': <Function transform_inverse(xform: warp.types.transformh)>, 'spatial_vector': <Function spatial_vector(dtype: warp.types.Float)>, 'spatial_adjoint': <Function spatial_adjoint(r: matrix(shape=(3, 3), dtype=~Float), s: matrix(shape=(3, 3), dtype=~Float))>, 'spatial_dot': <Function spatial_dot(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>, 'spatial_cross': <Function spatial_cross(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>, 'spatial_cross_dual': <Function spatial_cross_dual(a: vector(length=6, dtype=<class 'warp.types.float16'>), b: vector(length=6, dtype=<class 'warp.types.float16'>))>, 'spatial_top': <Function spatial_top(svec: vector(length=6, dtype=<class 'warp.types.float16'>))>, 'spatial_bottom': <Function spatial_bottom(svec: vector(length=6, dtype=<class 'warp.types.float16'>))>, 'spatial_jacobian': <Function spatial_jacobian(S: array(ndim=1, dtype=<class 'warp.types.vector.<locals>.vec_t'>), joint_parents: array(ndim=1, dtype=<class 'warp.types.int32'>), joint_qd_start: array(ndim=1, dtype=<class 'warp.types.int32'>), joint_start: int32, joint_count: int32, J_start: int32, J_out: array(ndim=1, dtype=~Float))>, 'spatial_mass': <Function spatial_mass(I_s: array(ndim=1, dtype=<class 'warp.types.matrix.<locals>.mat_t'>), joint_start: int32, joint_count: int32, M_start: int32, M: array(ndim=1, dtype=~Float))>, 'tile_zeros': <Function tile_zeros(m: int32, n: int32, dtype: typing.Any, storage: builtins.str)>, 'tile_ones': <Function tile_ones(m: int32, n: int32, dtype: typing.Any, storage: builtins.str)>, 'tile_arange': <Function tile_arange(*args: warp.types.Scalar, dtype: typing.Any, storage: builtins.str)>, 'tile_load': <Function tile_load(a: array(ndim=1, dtype=typing.Any), i: int32, n: int32, storage: builtins.str)>, 'tile_store': <Function tile_store(a: array(ndim=1, dtype=typing.Any), i: int32, t: typing.Any)>, 'tile_atomic_add': <Function tile_atomic_add(a: array(ndim=1, dtype=typing.Any), x: int32, y: int32, t: typing.Any)>, 'tile_view': <Function tile_view(t: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), i: int32, j: int32, m: int32, n: int32)>, 'tile_assign': <Function tile_assign(dst: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), i: int32, j: int32, src: tile(dtype=typing.Any, m=typing.Any, n=typing.Any))>, 'tile': <Function tile(x: typing.Any)>, 'untile': <Function untile(a: typing.Any)>, 'tile_extract': <Function tile_extract(a: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), i: int32, j: int32)>, 'tile_transpose': <Function tile_transpose(a: tile(dtype=typing.Any, m=typing.Any, n=typing.Any))>, 'tile_broadcast': <Function tile_broadcast(a: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), m: int32, n: int32)>, 'tile_matmul_scalar': <Function tile_matmul_scalar(a: warp.types.Tile, b: warp.types.Tile, out: warp.types.Tile)>, 'tile_sum': <Function tile_sum(a: warp.types.Tile)>, 'tile_min': <Function tile_min(a: warp.types.Tile)>, 'tile_max': <Function tile_max(a: warp.types.Tile)>, 'tile_reduce': <Function tile_reduce(op: typing.Callable, a: typing.Any)>, 'tile_map': <Function tile_map(op: typing.Callable, a: typing.Any)>, 'dense_gemm': <Function dense_gemm(m: int32, n: int32, p: int32, t1: int32, t2: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), B: array(ndim=1, dtype=<class 'warp.types.float32'>), C: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_gemm_batched': <Function dense_gemm_batched(m: array(ndim=1, dtype=<class 'warp.types.int32'>), n: array(ndim=1, dtype=<class 'warp.types.int32'>), p: array(ndim=1, dtype=<class 'warp.types.int32'>), t1: int32, t2: int32, A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), B_start: array(ndim=1, dtype=<class 'warp.types.int32'>), C_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), B: array(ndim=1, dtype=<class 'warp.types.float32'>), C: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_chol': <Function dense_chol(n: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), regularization: float32, L: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_chol_batched': <Function dense_chol_batched(A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_dim: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), regularization: float32, L: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_subs': <Function dense_subs(n: int32, L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_solve': <Function dense_solve(n: int32, A: array(ndim=1, dtype=<class 'warp.types.float32'>), L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'dense_solve_batched': <Function dense_solve_batched(b_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_start: array(ndim=1, dtype=<class 'warp.types.int32'>), A_dim: array(ndim=1, dtype=<class 'warp.types.int32'>), A: array(ndim=1, dtype=<class 'warp.types.float32'>), L: array(ndim=1, dtype=<class 'warp.types.float32'>), b: array(ndim=1, dtype=<class 'warp.types.float32'>), x: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'mlp': <Function mlp(weights: array(ndim=2, dtype=<class 'warp.types.float32'>), bias: array(ndim=1, dtype=<class 'warp.types.float32'>), activation: typing.Callable, index: int32, x: array(ndim=2, dtype=<class 'warp.types.float32'>), out: array(ndim=2, dtype=<class 'warp.types.float32'>))>, 'bvh_query_aabb': <Function bvh_query_aabb(id: uint64, low: vector(length=3, dtype=<class 'warp.types.float32'>), high: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'bvh_query_ray': <Function bvh_query_ray(id: uint64, start: vector(length=3, dtype=<class 'warp.types.float32'>), dir: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'bvh_query_next': <Function bvh_query_next(query: warp.types.bvh_query_t, index: int32)>, 'mesh_query_point': <Function mesh_query_point(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_point_no_sign': <Function mesh_query_point_no_sign(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), max_dist: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_furthest_point_no_sign': <Function mesh_query_furthest_point_no_sign(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), min_dist: float32, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_query_point_sign_normal': <Function mesh_query_point_sign_normal(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32, epsilon: float32)>, 'mesh_query_point_sign_winding_number': <Function mesh_query_point_sign_winding_number(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32, accuracy: float32, threshold: float32)>, 'mesh_query_ray': <Function mesh_query_ray(id: uint64, start: vector(length=3, dtype=<class 'warp.types.float32'>), dir: vector(length=3, dtype=<class 'warp.types.float32'>), max_t: float32, t: float32, bary_u: float32, bary_v: float32, sign: float32, normal: vector(length=3, dtype=<class 'warp.types.float32'>), face: int32)>, 'mesh_query_aabb': <Function mesh_query_aabb(id: uint64, low: vector(length=3, dtype=<class 'warp.types.float32'>), high: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'mesh_query_aabb_next': <Function mesh_query_aabb_next(query: warp.types.mesh_query_aabb_t, index: int32)>, 'mesh_eval_position': <Function mesh_eval_position(id: uint64, face: int32, bary_u: float32, bary_v: float32)>, 'mesh_eval_velocity': <Function mesh_eval_velocity(id: uint64, face: int32, bary_u: float32, bary_v: float32)>, 'hash_grid_query': <Function hash_grid_query(id: uint64, point: vector(length=3, dtype=<class 'warp.types.float32'>), max_dist: float32)>, 'hash_grid_query_next': <Function hash_grid_query_next(query: warp.types.hash_grid_query_t, index: int32)>, 'hash_grid_point_id': <Function hash_grid_point_id(id: uint64, index: int32)>, 'intersect_tri_tri': <Function intersect_tri_tri(v0: vector(length=3, dtype=<class 'warp.types.float32'>), v1: vector(length=3, dtype=<class 'warp.types.float32'>), v2: vector(length=3, dtype=<class 'warp.types.float32'>), u0: vector(length=3, dtype=<class 'warp.types.float32'>), u1: vector(length=3, dtype=<class 'warp.types.float32'>), u2: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'mesh_get': <Function mesh_get(id: uint64)>, 'mesh_eval_face_normal': <Function mesh_eval_face_normal(id: uint64, face: int32)>, 'mesh_get_point': <Function mesh_get_point(id: uint64, index: int32)>, 'mesh_get_velocity': <Function mesh_get_velocity(id: uint64, index: int32)>, 'mesh_get_index': <Function mesh_get_index(id: uint64, index: int32)>, 'closest_point_edge_edge': <Function closest_point_edge_edge(p1: vector(length=3, dtype=<class 'warp.types.float32'>), q1: vector(length=3, dtype=<class 'warp.types.float32'>), p2: vector(length=3, dtype=<class 'warp.types.float32'>), q2: vector(length=3, dtype=<class 'warp.types.float32'>), epsilon: float32)>, 'range': <Function range(end: int32)>, 'iter_next': <Function iter_next(range: warp.types.range_t)>, 'reversed': <Function reversed(range: warp.types.range_t)>, 'volume_sample': <Function volume_sample(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, dtype: typing.Any)>, 'volume_sample_grad': <Function volume_sample_grad(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, grad: typing.Any, dtype: typing.Any)>, 'volume_lookup': <Function volume_lookup(id: uint64, i: int32, j: int32, k: int32, dtype: typing.Any)>, 'volume_store': <Function volume_store(id: uint64, i: int32, j: int32, k: int32, value: typing.Any)>, 'volume_sample_f': <Function volume_sample_f(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32)>, 'volume_sample_grad_f': <Function volume_sample_grad_f(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, grad: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_lookup_f': <Function volume_lookup_f(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_f': <Function volume_store_f(id: uint64, i: int32, j: int32, k: int32, value: float32)>, 'volume_sample_v': <Function volume_sample_v(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32)>, 'volume_lookup_v': <Function volume_lookup_v(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_v': <Function volume_store_v(id: uint64, i: int32, j: int32, k: int32, value: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_sample_i': <Function volume_sample_i(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_lookup_i': <Function volume_lookup_i(id: uint64, i: int32, j: int32, k: int32)>, 'volume_store_i': <Function volume_store_i(id: uint64, i: int32, j: int32, k: int32, value: int32)>, 'volume_sample_index': <Function volume_sample_index(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, voxel_data: array(ndim=1, dtype=typing.Any), background: typing.Any)>, 'volume_sample_grad_index': <Function volume_sample_grad_index(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>), sampling_mode: int32, voxel_data: array(ndim=1, dtype=typing.Any), background: typing.Any, grad: typing.Any)>, 'volume_lookup_index': <Function volume_lookup_index(id: uint64, i: int32, j: int32, k: int32)>, 'volume_index_to_world': <Function volume_index_to_world(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_world_to_index': <Function volume_world_to_index(id: uint64, xyz: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_index_to_world_dir': <Function volume_index_to_world_dir(id: uint64, uvw: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'volume_world_to_index_dir': <Function volume_world_to_index_dir(id: uint64, xyz: vector(length=3, dtype=<class 'warp.types.float32'>))>, 'rand_init': <Function rand_init(seed: int32)>, 'randi': <Function randi(state: uint32)>, 'randf': <Function randf(state: uint32)>, 'randn': <Function randn(state: uint32)>, 'sample_cdf': <Function sample_cdf(state: uint32, cdf: array(ndim=1, dtype=<class 'warp.types.float32'>))>, 'sample_triangle': <Function sample_triangle(state: uint32)>, 'sample_unit_ring': <Function sample_unit_ring(state: uint32)>, 'sample_unit_disk': <Function sample_unit_disk(state: uint32)>, 'sample_unit_sphere_surface': <Function sample_unit_sphere_surface(state: uint32)>, 'sample_unit_sphere': <Function sample_unit_sphere(state: uint32)>, 'sample_unit_hemisphere_surface': <Function sample_unit_hemisphere_surface(state: uint32)>, 'sample_unit_hemisphere': <Function sample_unit_hemisphere(state: uint32)>, 'sample_unit_square': <Function sample_unit_square(state: uint32)>, 'sample_unit_cube': <Function sample_unit_cube(state: uint32)>, 'poisson': <Function poisson(state: uint32, lam: float32)>, 'noise': <Function noise(state: uint32, x: float32)>, 'pnoise': <Function pnoise(state: uint32, x: float32, px: int32)>, 'curlnoise': <Function curlnoise(state: uint32, xy: vector(length=2, dtype=<class 'warp.types.float32'>), octaves: uint32, lacunarity: float32, gain: float32)>, 'printf': <Function printf(fmt: builtins.str, *args: typing.Any)>, 'print': <Function print(value: typing.Any)>, 'breakpoint': <Function breakpoint()>, 'tid': <Function tid()>, 'copy': <Function copy(a: typing.Any)>, 'assign': <Function assign(dest: typing.Any, src: typing.Any)>, 'select': <Function select(cond: warp.types.bool, value_if_false: typing.Any, value_if_true: typing.Any)>, 'array': <Function array(ptr: uint64, shape: typing.Tuple, dtype: warp.types.Scalar)>, 'address': <Function address(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int, l: warp.types.Int)>, 'view': <Function view(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, j: warp.types.Int, k: warp.types.Int)>, 'array_store': <Function array_store(arr: array(ndim=1, dtype=typing.Any), i: warp.types.Int, value: typing.Any)>, 'store': <Function store(address: typing.Any, value: typing.Any)>, 'load': <Function load(address: typing.Any)>, 'atomic_add': <Function atomic_add(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_sub': <Function atomic_sub(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_min': <Function atomic_min(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'atomic_max': <Function atomic_max(arr: array(ndim=1, dtype=typing.Any), i: int16, value: typing.Any)>, 'extract': <Function extract(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>, 'index': <Function index(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>, 'indexref': <Function indexref(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>, 'expect_eq': <Function expect_eq(a: int8, b: int8)>, 'expect_neq': <Function expect_neq(a: int8, b: int8)>, 'lerp': <Function lerp(a: float16, b: float16, t: float16)>, 'smoothstep': <Function smoothstep(a: float16, b: float16, x: float16)>, 'expect_near': <Function expect_near(a: float16, b: float16, tolerance: float16)>, 'lower_bound': <Function lower_bound(arr: array(ndim=1, dtype=~Scalar), value: float16)>, 'add': <Function add(a: float16, b: float16)>, 'sub': <Function sub(a: float16, b: float16)>, 'bit_and': <Function bit_and(a: int16, b: int16)>, 'bit_or': <Function bit_or(a: int16, b: int16)>, 'bit_xor': <Function bit_xor(a: int16, b: int16)>, 'lshift': <Function lshift(a: int16, b: int16)>, 'rshift': <Function rshift(a: int16, b: int16)>, 'invert': <Function invert(a: int16)>, 'mul': <Function mul(a: float16, b: float16)>, 'mod': <Function mod(a: float16, b: float16)>, 'div': <Function div(a: float16, b: float16)>, 'floordiv': <Function floordiv(a: float16, b: float16)>, 'pos': <Function pos(x: float16)>, 'neg': <Function neg(x: float16)>, 'unot': <Function unot(a: warp.types.bool)>, 'tile_matmul': <Function tile_matmul(a: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), b: tile(dtype=typing.Any, m=typing.Any, n=typing.Any), out: tile(dtype=typing.Any, m=typing.Any, n=typing.Any))>, 'tile_fft': <Function tile_fft(inout: warp.types.Tile)>, 'tile_ifft': <Function tile_ifft(inout: warp.types.Tile)>, 'static': <Function static(expr: typing.Any)>}
complex_type_hints: tuple  # value = (typing.Any, typing.Callable, typing.Tuple)
function_key_counts: dict = {'quat_between_vectors': 1, 'frac': 1, 'sqr': 1, 'alpha_beta_spectrum': 1, 'jonswap_peak_sharpening': 1, 'jonswap_spectrum': 1, 'TMA_spectrum': 1, '_define_face': 1, '_set_face_normals': 1, '_set_face_uvs': 1, 'sdf_create_box': 1, 'sdf_create_torus': 1, 'sdf_translate': 1, 'sdf_rotate': 1, 'sdf_smooth_min': 1, 'intersect_ray_sphere': 1, 'sample_height': 1, 'laplacian': 1, 'lookup_float': 3, 'sample_float': 3, 'clip_segment': 1, 'clip_normal': 1}
generic_vtypes: tuple = (warp.types.mat22h, warp.types.mat22f, warp.types.mat22d, warp.types.mat33h, warp.types.mat33f, warp.types.mat33d, warp.types.mat44h, warp.types.mat44f, warp.types.mat44d, warp.types.spatial_matrixh, warp.types.spatial_matrixf, warp.types.spatial_matrixd, warp.types.quath, warp.types.quatf, warp.types.quatd, warp.types.transformh, warp.types.transformf, warp.types.transformd, warp.types.vec2h, warp.types.vec2f, warp.types.vec2d, warp.types.vec2s, warp.types.vec2i, warp.types.vec2l, warp.types.vec2b, warp.types.vec2us, warp.types.vec2ui, warp.types.vec2ul, warp.types.vec2ub, warp.types.vec3h, warp.types.vec3f, warp.types.vec3d, warp.types.vec3s, warp.types.vec3i, warp.types.vec3l, warp.types.vec3b, warp.types.vec3us, warp.types.vec3ui, warp.types.vec3ul, warp.types.vec3ub, warp.types.vec4h, warp.types.vec4f, warp.types.vec4d, warp.types.vec4s, warp.types.vec4i, warp.types.vec4l, warp.types.vec4b, warp.types.vec4us, warp.types.vec4ui, warp.types.vec4ul, warp.types.vec4ub, warp.types.spatial_vectorh, warp.types.spatial_vectorf, warp.types.spatial_vectord)
runtime: Runtime  # value = <warp.context.Runtime object>
scalar_types: dict = {warp.types.int8: warp.types.int8, warp.types.uint8: warp.types.uint8, warp.types.int16: warp.types.int16, warp.types.uint16: warp.types.uint16, warp.types.int32: warp.types.int32, warp.types.uint32: warp.types.uint32, warp.types.int64: warp.types.int64, warp.types.uint64: warp.types.uint64, warp.types.float16: warp.types.float16, warp.types.float32: warp.types.float32, warp.types.float64: warp.types.float64, warp.types.vec2b: warp.types.int8, warp.types.vec2ub: warp.types.uint8, warp.types.vec2s: warp.types.int16, warp.types.vec2us: warp.types.uint16, warp.types.vec2i: warp.types.int32, warp.types.vec2ui: warp.types.uint32, warp.types.vec2l: warp.types.int64, warp.types.vec2ul: warp.types.uint64, warp.types.vec2h: warp.types.float16, warp.types.vec2f: warp.types.float32, warp.types.vec2d: warp.types.float64, warp.types.vec3b: warp.types.int8, warp.types.vec3ub: warp.types.uint8, warp.types.vec3s: warp.types.int16, warp.types.vec3us: warp.types.uint16, warp.types.vec3i: warp.types.int32, warp.types.vec3ui: warp.types.uint32, warp.types.vec3l: warp.types.int64, warp.types.vec3ul: warp.types.uint64, warp.types.vec3h: warp.types.float16, warp.types.vec3f: warp.types.float32, warp.types.vec3d: warp.types.float64, warp.types.vec4b: warp.types.int8, warp.types.vec4ub: warp.types.uint8, warp.types.vec4s: warp.types.int16, warp.types.vec4us: warp.types.uint16, warp.types.vec4i: warp.types.int32, warp.types.vec4ui: warp.types.uint32, warp.types.vec4l: warp.types.int64, warp.types.vec4ul: warp.types.uint64, warp.types.vec4h: warp.types.float16, warp.types.vec4f: warp.types.float32, warp.types.vec4d: warp.types.float64, warp.types.mat22h: warp.types.float16, warp.types.mat22f: warp.types.float32, warp.types.mat22d: warp.types.float64, warp.types.mat33h: warp.types.float16, warp.types.mat33f: warp.types.float32, warp.types.mat33d: warp.types.float64, warp.types.mat44h: warp.types.float16, warp.types.mat44f: warp.types.float32, warp.types.mat44d: warp.types.float64, warp.types.quath: warp.types.float16, warp.types.quatf: warp.types.float32, warp.types.quatd: warp.types.float64, warp.types.transformh: warp.types.float16, warp.types.transformf: warp.types.float32, warp.types.transformd: warp.types.float64, warp.types.spatial_vectorh: warp.types.float16, warp.types.spatial_vectorf: warp.types.float32, warp.types.spatial_vectord: warp.types.float64, warp.types.spatial_matrixh: warp.types.float16, warp.types.spatial_matrixf: warp.types.float32, warp.types.spatial_matrixd: warp.types.float64}
sequence_types: tuple = (list, tuple)
user_modules: dict  # value = {'warp.utils': <warp.context.Module object>, 'omni.warp.nodes._impl.points': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleOceanDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.kernels.grid_create': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnParticlesSimulate': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleProceduralVolume': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnClothSimulate': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnNoiseDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSamplePrimFlocking': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnSampleMeshDeform': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnWaveSolve': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnParticlesFromMesh': <warp.context.Module object>, 'omni.warp.nodes._impl.OgnMeshFromVolume': <warp.context.Module object>, 'isaacsim.core.utils.warp.rotations': <warp.context.Module object>, 'isaacsim.core.utils.warp.tensor': <warp.context.Module object>, 'isaacsim.core.utils.warp.transformations': <warp.context.Module object>, 'isaacsim.core.utils.fabric': <warp.context.Module object>, 'omni.replicator.core.scripts.utils.wp_utils': <warp.context.Module object>, 'omni.replicator.core.scripts.augmentations_default': <warp.context.Module object>, 'omni.replicator.core.scripts.utils.mesh_decal': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugCutMixExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugCropResizeExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnSemanticSegmentation': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugRotateExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugContrastExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnPointCloudGenerator': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugBgRandExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugPixellateExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugConv2dExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugMotionBlurExp': <warp.context.Module object>, 'omni.replicator.core.ogn.python._impl.nodes.OgnAugImgBlendExp': <warp.context.Module object>, 'isaacsim.sensors.camera.camera_view': <warp.context.Module object>}
