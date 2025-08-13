from __future__ import annotations
import numpy as np
import numpy
import typing
import warp as wp
import warp.context
import warp.types
__all__: list[str] = ['broadcast_to', 'np', 'np_dtype_to_warp_type', 'place', 'resolve_indices', 'wp']
def _astype(src: wp.array, dtype: type) -> wp.array:
    ...
def _broadcastable_shape(src: tuple[int], dst: tuple[int]) -> tuple[tuple[int] | None, tuple[bool] | None]:
    ...
def broadcast_to(x: list | np.ndarray | wp.array, *, shape: list[int], dtype: type | None = None, device: str | wp.context.Device | None = None) -> wp.array:
    """
    Broadcast a list, a NumPy array, or a Warp array to a Warp array with a new shape.
    
        .. note::
    
            Broadcasting follows NumPy's rules: Two shapes are compatible if by comparing their dimensions element-wise,
            starting with the trailing dimension (i.e., rightmost) and moving leftward
    
            * they are equal, or
            * one of them is 1.
    
        Args:
            x: List, NumPy array, or Warp array.
            shape: Shape of the desired array.
            dtype: Data type of the output array. If ``None``, the data type of the input is used.
            device: Device to place the output array on. If ``None``, the default device is used,
                unless the input is a Warp array (in which case the input device is used).
    
        Returns:
            Warp array with the given shape.
    
        Raises:
            ValueError: If the input list or array is not compatible with the new shape according to the broadcasting rules.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.ops as ops_utils
            >>> import numpy as np
            >>> import warp as wp
            >>>
            >>> # list
            >>> array = ops_utils.broadcast_to([1, 2, 3], shape=(1, 3))  # doctest: +NO_CHECK
            >>> print(array)
            [[1 2 3]]
            >>>
            >>> # NumPy array (with shape (1, 3))
            >>> array = ops_utils.broadcast_to(np.array([[1, 2, 3]]), shape=(2, 3))  # doctest: +NO_CHECK
            >>> print(array)
            [[1 2 3]
             [1 2 3]]
            >>>
            >>> # Warp array (with different device)
            >>> array = ops_utils.broadcast_to(wp.array([1, 2, 3], device="cpu"), shape=(3, 3), device="cuda")  # doctest: +NO_CHECK
            >>> print(array)
            [[1 2 3]
             [1 2 3]
             [1 2 3]]
        
    """
def place(x: list | np.ndarray | wp.array, *, dtype: type | None = None, device: str | wp.context.Device | None = None) -> wp.array:
    """
    Create a Warp array from a list, a NumPy array, or a Warp array.
    
        Args:
            x: List, NumPy array, or Warp array.
                If the input is a Warp array with the same device and dtype, it is returned as is.
            dtype: Data type of the output array. If not provided, the data type of the input is used.
            device: Device to place the output array on. If ``None``, the default device is used,
                unless the input is a Warp array (in which case the input device is used).
    
        Returns:
            Warp array instance.
    
        Raises:
            TypeError: If the input argument ``x`` is not a supported data container.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.ops as ops_utils
            >>> import numpy as np
            >>> import warp as wp
            >>>
            >>> # list
            >>> array = ops_utils.place([1.0, 2.0, 3.0], device="cpu")  # doctest: +NO_CHECK
            >>> print(array, array.dtype, array.device, array.shape)
            [1. 2. 3.] <class 'warp.types.float64'> cpu (3,)
            >>>
            >>> # NumPy array (with shape (3, 1))
            >>> array = ops_utils.place(np.array([[1], [2], [3]], dtype=np.uint8), dtype=wp.float32)  # doctest: +NO_CHECK
            >>> print(array, array.dtype, array.device, array.shape)
            [[1.] [2.] [3.]] <class 'warp.types.float32'> cuda:0 (3, 1)
            >>>
            >>> # Warp array (with different device)
            >>> array = ops_utils.place(wp.array([1.0, 2.0, 3.0], device="cpu"), device="cuda")  # doctest: +NO_CHECK
            >>> print(array, array.dtype, array.device, array.shape)
            [1. 2. 3.] <class 'warp.types.float64'> cuda:0 (3,)
        
    """
def resolve_indices(x: list | np.ndarray | wp.array | None, *, count: int | None = None, dtype: type | None = warp.types.int32, device: str | wp.context.Device | None = None) -> wp.array:
    """
    Create a flattened (1D) Warp array to be used as indices from a list, a NumPy array, or a Warp array.
    
        Args:
            x: List, NumPy array, or Warp array.
            count: Number of indices to resolve.
                If input argument ``x`` is ``None``, the indices are generated from 0 to ``count - 1``.
                If the input is not ``None``, this value is ignored.
            dtype: Data type of the output array. If ``None``, ``wp.int32`` is used.
            device: Device to place the output array on. If ``None``, the default device is used,
                unless the input is a Warp array (in which case the input device is used).
    
        Returns:
            Flattened (1D) Warp array instance.
    
        Raises:
            ValueError: If input argument ``x`` is ``None`` and ``count`` is not provided.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.ops as ops_utils
            >>> import numpy as np
            >>> import warp as wp
            >>>
            >>> # list
            >>> indices = ops_utils.resolve_indices([1, 2, 3], device="cpu")  # doctest: +NO_CHECK
            >>> print(indices, indices.dtype, indices.device, indices.shape)
            [1 2 3] <class 'warp.types.int32'> cpu (3,)
            >>>
            >>> # NumPy array (with shape (3, 1))
            >>> indices = ops_utils.resolve_indices(np.array([[1], [2], [3]], dtype=np.uint8))  # doctest: +NO_CHECK
            >>> print(indices, indices.dtype, indices.device, indices.shape)
            [1 2 3] <class 'warp.types.int32'> cuda:0 (3,)
            >>>
            >>> # Warp array (with different device)
            >>> indices = ops_utils.resolve_indices(wp.array([1, 2, 3], device="cpu"), device="cuda")  # doctest: +NO_CHECK
            >>> print(indices, indices.dtype, indices.device, indices.shape)
            [1 2 3] <class 'warp.types.int32'> cuda:0 (3,)
        
    """
_WK_BROADCAST: list  # value = [None, <warp.context.Kernel object>, <warp.context.Kernel object>, <warp.context.Kernel object>, <warp.context.Kernel object>]
_WK_CAST: list  # value = [None, <warp.context.Kernel object>, <warp.context.Kernel object>, <warp.context.Kernel object>, <warp.context.Kernel object>]
_wk_broadcast_1d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_broadcast_2d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_broadcast_3d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_broadcast_4d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_cast_1d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_cast_2d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_cast_3d: warp.context.Kernel  # value = <warp.context.Kernel object>
_wk_cast_4d: warp.context.Kernel  # value = <warp.context.Kernel object>
np_dtype_to_warp_type: dict  # value = {numpy.bool_: warp.types.bool, numpy.int8: warp.types.int8, numpy.uint8: warp.types.uint8, numpy.int16: warp.types.int16, numpy.uint16: warp.types.uint16, numpy.int32: warp.types.int32, numpy.int64: warp.types.int64, numpy.uint32: warp.types.uint32, numpy.uint64: warp.types.uint64, numpy.float16: warp.types.float16, numpy.float32: warp.types.float32, numpy.float64: warp.types.float64, dtype('bool'): warp.types.bool, dtype('int8'): warp.types.int8, dtype('uint8'): warp.types.uint8, dtype('int16'): warp.types.int16, dtype('uint16'): warp.types.uint16, dtype('int32'): warp.types.int32, dtype('int64'): warp.types.int64, dtype('uint32'): warp.types.uint32, dtype('uint64'): warp.types.uint64, dtype('float16'): warp.types.float16, dtype('float32'): warp.types.float32, dtype('float64'): warp.types.float64}
