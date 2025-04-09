from __future__ import annotations
import numpy
import torch
import warp
__all__: list = ['warp2torch', 'warp2jax', 'warp2tensorflow', 'warp2numpy', 'torch2warp', 'torch2jax', 'torch2tensorflow', 'torch2numpy', 'jax2warp', 'jax2torch', 'jax2tensorflow', 'jax2numpy', 'tensorflow2warp', 'tensorflow2torch', 'tensorflow2jax', 'tensorflow2numpy', 'numpy2warp', 'numpy2torch', 'numpy2jax', 'numpy2tensorflow']
def jax2numpy(array: jax.Array) -> numpy.ndarray:
    """
    Convert JAX array to NumPy array
    
        Args:
            array (jax.Array): JAX array
    
        Returns:
            numpy.ndarray: NumPy array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import jax
            >>> import jax.numpy as jnp
            >>>
            >>> with jax.default_device(jax.devices("cuda")[0]):
            ...     jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
            ...
            >>> numpy_array = interops_utils.jax2numpy(jax_array)
            >>> type(numpy_array)
            <class 'numpy.ndarray'>
        
    """
def jax2tensorflow(array: jax.Array) -> tensorflow.Tensor:
    """
    Convert JAX array to TensorFlow tensor
    
        Args:
            array (jax.Array): JAX array
    
        Returns:
            tensorflow.Tensor: TensorFlow tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import jax
            >>> import jax.numpy as jnp
            >>>
            >>> with jax.default_device(jax.devices("cuda")[0]):
            ...     jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
            ...
            >>> tensorflow_tensor = interops_utils.jax2tensorflow(jax_array)
            >>> type(tensorflow_tensor)
            <class 'tensorflow.python...Tensor'>
        
    """
def jax2torch(array: jax.Array) -> torch.Tensor:
    """
    Convert JAX array to PyTorch tensor
    
        Args:
            array (jax.Array): JAX array
    
        Returns:
            torch.Tensor: PyTorch tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import jax
            >>> import jax.numpy as jnp
            >>>
            >>> with jax.default_device(jax.devices("cuda")[0]):
            ...     jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
            ...
            >>> torch_tensor = interops_utils.jax2torch(jax_array)
            >>> type(torch_tensor)
            <class 'torch.Tensor'>
        
    """
def jax2warp(array: jax.Array) -> warp.array:
    """
    Convert JAX array to Warp array
    
        Args:
            array (jax.Array): JAX array
    
        Returns:
            warp.array: Warp array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import jax
            >>> import jax.numpy as jnp
            >>>
            >>> with jax.default_device(jax.devices("cuda")[0]):
            ...     jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
            ...
            >>> warp_array = interops_utils.jax2warp(jax_array)
            >>> type(warp_array)
            <class 'warp.types.array'>
        
    """
def numpy2jax(array: numpy.ndarray) -> jax.Array:
    """
    Convert NumPy array to JAX array
    
        Args:
            array (numpy.ndarray): NumPy array
    
        Returns:
            jax.Array: JAX array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import numpy as np
            >>>
            >>> numpy_array = np.zeros((100, 10), dtype=np.float32)
            >>> jax_array = interops_utils.numpy2jax(numpy_array)
            >>> type(jax_array)
            <class 'jaxlib.xla_extension.ArrayImpl'>
        
    """
def numpy2tensorflow(array: numpy.ndarray) -> tensorflow.Tensor:
    """
    Convert NumPy array to TensorFlow tensor
    
        Args:
            array (numpy.ndarray): NumPy array
    
        Returns:
            tensorflow.Tensor: TensorFlow tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import numpy as np
            >>>
            >>> numpy_array = np.zeros((100, 10), dtype=np.float32)
            >>> tensorflow_tensor = interops_utils.numpy2tensorflow(numpy_array)
            >>> type(tensorflow_tensor)
            <class 'tensorflow.python...Tensor'>
        
    """
def numpy2torch(array: numpy.ndarray) -> torch.Tensor:
    """
    Convert NumPy array to PyTorch tensor
    
        Args:
            array (numpy.ndarray): NumPy array
    
        Returns:
            torch.Tensor: PyTorch tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import numpy as np
            >>>
            >>> numpy_array = np.zeros((100, 10), dtype=np.float32)
            >>> torch_tensor = interops_utils.numpy2torch(numpy_array)
            >>> type(torch_tensor)
            <class 'torch.Tensor'>
        
    """
def numpy2warp(array: numpy.ndarray) -> warp.array:
    """
    Convert NumPy array to Warp array
    
        Args:
            array (numpy.ndarray): NumPy array
    
        Returns:
            warp.array: Warp array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import numpy as np
            >>>
            >>> numpy_array = np.zeros((100, 10), dtype=np.float32)
            >>> warp_array = interops_utils.numpy2warp(numpy_array)
            >>> type(warp_array)
            <class 'warp.types.array'>
        
    """
def tensorflow2jax(tensor: tensorflow.Tensor) -> jax.Array:
    """
    Convert TensorFlow tensor to JAX array
    
        Args:
            tensor (tensorflow.Tensor): TensorFlow tensor
    
        Returns:
            jax.Array: JAX array
    
        .. warning::
    
            It is expected that the conversion of ``int32`` TensorFlow tensors to other backends will be on the CPU,
            regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import tensorflow as tf  # doctest: +NO_CHECK
            >>>
            >>> with tf.device("/GPU:0"):
            ...     tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
            ...
            >>> jax_array = interops_utils.tensorflow2jax(tensorflow_tensor)
            >>> type(jax_array)
            <class 'jaxlib.xla_extension.Array...'>
        
    """
def tensorflow2numpy(tensor: tensorflow.Tensor) -> numpy.ndarray:
    """
    Convert TensorFlow tensor to NumPy array
    
        Args:
            tensor (tensorflow.Tensor): TensorFlow tensor
    
        Returns:
            numpy.ndarray: NumPy array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import tensorflow as tf  # doctest: +NO_CHECK
            >>>
            >>> with tf.device("/GPU:0"):
            ...     tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
            ...
            >>> numpy_array = interops_utils.tensorflow2numpy(tensorflow_tensor)
            >>> type(numpy_array)
            <class 'numpy.ndarray'>
        
    """
def tensorflow2torch(tensor: tensorflow.Tensor) -> torch.Tensor:
    """
    Convert TensorFlow tensor to PyTorch tensor
    
        Args:
            tensor (tensorflow.Tensor): TensorFlow tensor
    
        Returns:
            torch.Tensor: PyTorch tensor
    
        .. warning::
    
            It is expected that the conversion of ``int32`` TensorFlow tensors to other backends will be on the CPU,
            regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import tensorflow as tf  # doctest: +NO_CHECK
            >>>
            >>> with tf.device("/GPU:0"):
            ...     tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
            ...
            >>> torch_tensor = interops_utils.tensorflow2torch(tensorflow_tensor)
            >>> type(torch_tensor)
            <class 'torch.Tensor'>
        
    """
def tensorflow2warp(tensor: tensorflow.Tensor) -> warp.array:
    """
    Convert TensorFlow tensor to Warp array
    
        Args:
            tensor (tensorflow.Tensor): TensorFlow tensor
    
        Returns:
            warp.array: Warp array
    
        .. warning::
    
            It is expected that the conversion of ``int32`` TensorFlow tensors to other backends will be on the CPU,
            regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import tensorflow as tf  # doctest: +NO_CHECK
            >>>
            >>> with tf.device("/GPU:0"):
            ...     tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
            ...
            >>> warp_array = interops_utils.tensorflow2warp(tensorflow_tensor)
            >>> type(warp_array)
            <class 'warp.types.array'>
        
    """
def torch2jax(tensor: torch.Tensor) -> jax.Array:
    """
    Convert PyTorch tensor to JAX array
    
        Args:
            tensor (torch.Tensor): PyTorch tensor
    
        Returns:
            jax.Array: JAX array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import torch
            >>>
            >>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
            >>> jax_array = interops_utils.torch2jax(torch_tensor)
            >>> type(jax_array)
            <class 'jaxlib.xla_extension.Array...'>
        
    """
def torch2numpy(tensor: torch.Tensor) -> numpy.ndarray:
    """
    Convert PyTorch tensor to NumPy array
    
        Args:
            tensor (torch.Tensor): PyTorch tensor
    
        Returns:
            numpy.ndarray: NumPy array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import torch
            >>>
            >>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
            >>> numpy_array = interops_utils.torch2numpy(torch_tensor)
            >>> print(type(numpy_array))
            <class 'numpy.ndarray'>
        
    """
def torch2tensorflow(tensor: torch.Tensor) -> tensorflow.Tensor:
    """
    Convert PyTorch tensor to TensorFlow tensor
    
        Args:
            tensor (torch.Tensor): PyTorch tensor
    
        Returns:
            tensorflow.Tensor: TensorFlow tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import torch
            >>>
            >>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
            >>> tensorflow_tensor = interops_utils.torch2tensorflow(torch_tensor)
            >>> type(tensorflow_tensor)
            <class 'tensorflow.python...Tensor'>
        
    """
def torch2warp(tensor: torch.Tensor) -> warp.array:
    """
    Convert PyTorch tensor to Warp array
    
        Args:
            tensor (torch.Tensor): PyTorch tensor
    
        Returns:
            warp.array: Warp array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import torch
            >>>
            >>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
            >>> warp_array = interops_utils.torch2warp(torch_tensor)
            >>> type(warp_array)
            <class 'warp.types.array'>
        
    """
def warp2jax(array: warp.array) -> jax.Array:
    """
    Convert Warp array to JAX array
    
        Args:
            array (warp.array): Warp array
    
        Returns:
            jax.Array: JAX array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import warp as wp
            >>>
            >>> wp.init()  # doctest: +NO_CHECK
            >>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
            >>> jax_array = interops_utils.warp2jax(warp_array)
            >>> type(jax_array)
            <class 'jaxlib.xla_extension.Array...'>
        
    """
def warp2numpy(array: warp.array) -> numpy.ndarray:
    """
    Convert Warp array to NumPy array
    
        Args:
            array (warp.array): Warp array
    
        Returns:
            numpy.ndarray: NumPy array
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import warp as wp
            >>>
            >>> wp.init()  # doctest: +NO_CHECK
            >>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
            >>> numpy_array = interops_utils.warp2numpy(warp_array)
            >>> type(numpy_array)
            <class 'numpy.ndarray'>
        
    """
def warp2tensorflow(array: warp.array) -> tensorflow.Tensor:
    """
    Convert Warp array to TensorFlow tensor
    
        Args:
            array (warp.array): Warp array
    
        Returns:
            tensorflow.Tensor: TensorFlow tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import warp as wp
            >>>
            >>> wp.init()  # doctest: +NO_CHECK
            >>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
            >>> tensorflow_tensor = interops_utils.warp2tensorflow(warp_array)
            >>> type(tensorflow_tensor)
            <class 'tensorflow.python...Tensor'>
        
    """
def warp2torch(array: warp.array) -> torch.Tensor:
    """
    Convert Warp array to PyTorch tensor
    
        Args:
            array (warp.array): Warp array
    
        Returns:
            torch.Tensor: PyTorch tensor
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.interops as interops_utils
            >>> import warp as wp
            >>>
            >>> wp.init()  # doctest: +NO_CHECK
            >>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
            >>> torch_tensor = interops_utils.warp2torch(warp_array)
            >>> type(torch_tensor)
            <class 'torch.Tensor'>
        
    """
_c_warp_torch_interop: bool = True
_jax_cpu_device_context = None
_jax_from_dlpack = None
_jax_to_dlpack = None
_numpy_array = None
_numpy_from_tensorflow = None
_numpy_to_jax = None
_numpy_to_tensorflow = None
_numpy_to_torch = None
_numpy_to_warp = None
_numpy_to_warp_dtype = None
_tensorflow_cpu_device_context = None
_tensorflow_from_dlpack = None
_tensorflow_make_tensor_proto = None
_tensorflow_to_dlpack = None
_torch_from_dlpack = None
_torch_to_dlpack = None
_torch_to_warp = None
_warp_from_dlpack = None
_warp_to_dlpack = None
_warp_to_torch = None
