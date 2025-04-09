from __future__ import annotations
import warp as warp
__all__ = ['device_from_jax', 'device_to_jax', 'dtype_from_jax', 'dtype_to_jax', 'from_jax', 'to_jax', 'warp']
def device_from_jax(jax_device) -> warp.context.Device:
    """
    Return the Warp device corresponding to a Jax device.
    
        Args:
            jax_device (jax.Device): A Jax device descriptor.
    
        Raises:
            RuntimeError: The Jax device is neither a CPU nor GPU device.
        
    """
def device_to_jax(warp_device: typing.Union[warp.context.Device, str, NoneType]):
    """
    Return the Jax device corresponding to a Warp device.
    
        Returns:
            :class:`jax.Device`
    
        Raises:
            RuntimeError: Failed to find the corresponding Jax device.
        
    """
def dtype_from_jax(jax_dtype):
    """
    Return the Warp dtype corresponding to a Jax dtype.
    
        Raises:
            TypeError: Unable to find a corresponding Warp data type.
        
    """
def dtype_to_jax(warp_dtype):
    """
    Return the Jax dtype corresponding to a Warp dtype.
    
        Args:
            warp_dtype: A Warp data type that has a corresponding Jax data type.
    
        Raises:
            TypeError: Unable to find a corresponding Jax data type.
        
    """
def from_jax(jax_array, dtype = None) -> warp.types.array:
    """
    Convert a Jax array to a Warp array without copying the data.
    
        Args:
            jax_array (jax.Array): The Jax array to convert.
            dtype (optional): The target data type of the resulting Warp array. Defaults to the Jax array's data type mapped to a Warp data type.
    
        Returns:
            warp.array: The converted Warp array.
        
    """
def to_jax(warp_array):
    """
    
        Convert a Warp array to a Jax array without copying the data.
    
        Args:
            warp_array (warp.array): The Warp array to convert.
    
        Returns:
            jax.Array: The converted Jax array.
        
    """
