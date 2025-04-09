from __future__ import annotations
import copy as copy
import numpy as np
import numpy
__all__ = ['copy', 'cross', 'normalize', 'normalized', 'np', 'radians_to_degrees']
def cross(a: typing.Union[numpy.ndarray, list], b: typing.Union[numpy.ndarray, list]) -> list:
    """
    Computes the cross-product between two 3-dimensional vectors.
    
        Args:
            a (np.ndarray, list): A 3-dimensional vector
            b (np.ndarray, list): A 3-dimensional vector
    
        Returns:
            np.ndarray: Cross product between input vectors.
        
    """
def normalize(v):
    """
    Normalizes the vector inline (and also returns it).
    """
def normalized(v):
    """
    Returns a normalized copy of the provided vector.
    """
def radians_to_degrees(rad_angles: numpy.ndarray) -> numpy.ndarray:
    """
    Converts input angles from radians to degrees.
    
        Args:
            rad_angles (np.ndarray): Input array of angles (in radians).
    
        Returns:
            np.ndarray: Array of angles in degrees.
        
    """
