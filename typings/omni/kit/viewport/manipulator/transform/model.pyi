from __future__ import annotations
import carb as carb
import enum
from enum import Enum
from enum import Flag
from enum import IntEnum
from enum import auto
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.transform.model import AbstractTransformManipulatorModel
from omni.kit.manipulator.transform.types import Operation
import typing
__all__: list = ['ManipulationMode', 'Viewport1WindowState', 'DataAccessorRegistry', 'DataAccessor', 'ViewportTransformModel']
class DataAccessor:
    """
    An abstract class for accessing and manipulating transformation data.
    
        This class provides methods to retrieve and clear transformation data, such as local-to-world and parent-to-world transforms for objects within a 3D environment. It is designed to interface with other components that require transformation data handling and manipulation.
        
    """
    def __init__(self):
        """
        Initializes the DataAccessor instance.
        """
    def clear_xform_cache(self):
        """
        Clears the transformation cache.
        """
    def get_local_to_world_transform(self, obj):
        """
        Calculates the local-to-world transform for the given object.
        
                Args:
                    obj (object): The object to calculate the transform for.
                
        """
    def get_parent_to_world_transform(self, obj):
        """
        Calculates the parent-to-world transform for the given object.
        
                Args:
                    obj (object): The object to calculate the transform for.
                
        """
class DataAccessorRegistry:
    """
    A registry for managing data accessors.
    
        This class provides mechanisms to retrieve and manage instances of data accessors, facilitating the access to various data operations and transformations.
        
    """
    def __init__(self):
        """
        Initializes the DataAccessorRegistry instance.
        """
    def getDataAccessor(self):
        """
        Creates and returns a new DataAccessor instance.
        
                Returns:
                    DataAccessor: A new instance of DataAccessor.
                
        """
class ManipulationMode(enum.IntEnum):
    """
    An enumeration.
    
        This enumeration defines different manipulation modes for transforming objects.
        
    """
    INDIVIDUAL: typing.ClassVar[ManipulationMode]  # value = <ManipulationMode.INDIVIDUAL: 2>
    PIVOT: typing.ClassVar[ManipulationMode]  # value = <ManipulationMode.PIVOT: 0>
    UNIFORM: typing.ClassVar[ManipulationMode]  # value = <ManipulationMode.UNIFORM: 1>
class Viewport1WindowState:
    """
    A class for managing the state of Viewport-1 windows.
    
        This class provides functionality to handle multiple Viewport-1 window instances, focusing on manipulating their states such as disabling selection rectangles, enabling picking, and retrieving picked world positions. It also manages the USD context name for the focused windows.
        
    """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the Viewport1WindowState instance.
        """
    def destroy(self):
        """
        Destroys the state by resetting focused windows.
        """
    def get_picked_world_pos(self):
        """
        Gets the picked world position from the focused viewport window.
        
                Returns:
                    tuple or None: The picked world position or None if not available.
                
        """
    def get_usd_context_name(self):
        """
        Gets the USD context name from the focused viewport window.
        
                Returns:
                    str: The USD context name or an empty string.
                
        """
class ViewportTransformModel(omni.kit.manipulator.transform.model.AbstractTransformManipulatorModel):
    """
    A class for managing viewport transformations in a 3D manipulation context.
    
        This class is responsible for handling transformations within a viewport, utilizing the USD context and viewport API provided during initialization. It extends the AbstractTransformManipulatorModel to provide specific functionalities for viewport transformations.
    
        Args:
            usd_context_name (str): The name of the USD context associated with the viewport.
            viewport_api: The API interface for interacting with the viewport.
        
    """
    def __init__(self, usd_context_name: str = '', viewport_api = None):
        """
        Initializes the ViewportTransformModel instance.
        """
