"""
This module defines the PrimDataAccessorRegistry class, which manages the registration and unregistration of data accessor functions for specific data tags.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.prim.core.settings_constants import DataRegistryEventTypes as da_ev_c
__all__ = ['PrimDataAccessorRegistry', 'carb', 'da_ev_c', 'omni']
class PrimDataAccessorRegistry:
    """
    A registry for managing data accessors within the application.
    
        This class serves as a central hub to register and unregister data accessors, which are functions responsible for manipulating and accessing data associated with specific tags. It provides methods to add and remove data accessors, retrieve the current list of registered data accessors, and manage an event stream to notify about changes in data accessor registration.
    
        The class maintains an internal dictionary to map data tags to their corresponding data accessor functions. It also holds an event stream object to emit events when data accessors are added or removed.
        
    """
    def __init__(self):
        """
        Initializes the PrimDataAccessorRegistry with default values.
        """
    def destroy(self):
        """
        Cleans up resources and references, preparing the registry for destruction.
        """
    def get_data_accessors_func(self):
        """
        Returns the dictionary of registered data accessor functions.
        """
    def get_event_stream(self):
        """
        Returns the event stream associated with the registry.
        """
    def register_data_accessor(self, func, data_tag):
        """
        Registers a new data accessor function.
        
                Args:
                    func (Callable): The function to be registered as a data accessor.
                    data_tag (str): Identifier for the data accessor.
        """
    def unregister_data_accessor(self, data_tag):
        """
        Unregisters an existing data accessor.
        
                Args:
                    data_tag (str): Identifier for the data accessor to be unregistered.
        """
