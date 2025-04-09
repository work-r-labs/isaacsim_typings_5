from __future__ import annotations
import ctypes as ctypes
import os as os
import warp as warp
from warp.thirdparty import appdirs
__all__ = ['appdirs', 'build_cpu', 'build_cuda', 'clear_kernel_cache', 'ctypes', 'init_kernel_cache', 'load_cuda', 'os', 'warp']
def build_cpu(obj_path, cpp_path, mode = 'release', verify_fp = False, fast_math = False):
    ...
def build_cuda(cu_path, arch, output_path, config = 'release', verify_fp = False, fast_math = False, ltoirs = None):
    ...
def clear_kernel_cache() -> None:
    """
    Clear the kernel cache directory of previously generated source code and compiler artifacts.
    
        Only directories beginning with ``wp_`` will be deleted.
        This function only clears the cache for the current Warp version.
        
    """
def init_kernel_cache(path = None):
    """
    Initialize kernel cache directory.
    
        This function is used during Warp initialization, but it can also be called directly to change the cache location.
        If the path is not explicitly specified, a default location will be chosen based on OS-specific conventions.
    
        To change the default cache location, set warp.config.kernel_cache_dir before calling warp.init().
        
    """
def load_cuda(input_path, device):
    ...
