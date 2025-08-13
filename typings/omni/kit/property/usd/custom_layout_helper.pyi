from __future__ import annotations
from collections import OrderedDict
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
__all__: list = list()
class Container:
    """
    
        Class that represents a container in the custom layout.
        
    """
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, tb):
        """
        
                Exits the container.
        
                Args:
                    exc_type (type): The type of the exception.
                    exc_value (Exception): The exception.
                    tb (traceback): The traceback.
                
        """
    def __init__(self, hide_if_true = None, show_if_true = None):
        ...
    def add_child(self, item):
        """
        
                Adds a child to the container.
        
                Args:
                    item: The child to add.
                
        """
    def get_collapsed(self):
        """
        
                Gets the collapsed state of the container.
        
                Returns:
                    bool: The collapsed state of the container.
                
        """
    def get_name(self):
        """
        
                Gets the name of the container.
        
                Returns:
                    str: The name of the container.
                
        """
    def is_visible(self):
        """
        
                Gets the visibility of the container.
        
                Returns:
                    bool: The visibility of the container.
                
        """
class CustomLayoutFrame(Container):
    """
    
        Class that represents a frame in the custom layout.
        
    """
    def __init__(self, hide_extra = False):
        ...
    def _process_container(self, container, props_dict, customized_props, group_name):
        """
        
                Processes the container.
        
                Args:
                    container: The container to process.
                    props_dict: The dictionary of properties.
                    customized_props: The list of customized properties.
                    group_name: The name of the group.
                
        """
    def apply(self, props):
        """
        
                Applies the custom layout to the properties.
        
                Args:
                    props: The properties to apply the custom layout to.
                
        """
class CustomLayoutGroup(Container):
    """
    
        Class that represents a group in the custom layout.
        
    """
    def __init__(self, container_name, collapsed = False, hide_if_true = None, show_if_true = None):
        ...
class CustomLayoutProperty:
    """
    
        Class that represents a property in the custom layout.
        
    """
    def __init__(self, prop_name, display_name = None, build_fn = None, hide_if_true = None, show_if_true = None):
        ...
    def get_build_fn(self):
        """
        
                Gets the build function of the property.
        
                Returns:
                    Callable: The build function of the property.
                
        """
    def get_display_name(self):
        """
        
                Gets the display name of the property.
        
                Returns:
                    str: The display name of the property.
                
        """
    def get_property_name(self):
        """
        
                Gets the name of the property.
        
                Returns:
                    str: The name of the property.
                
        """
    def is_visible(self):
        """
        
                Gets the visibility of the property.
        
                Returns:
                    bool: The visibility of the property.
                
        """
stack: list = list()
