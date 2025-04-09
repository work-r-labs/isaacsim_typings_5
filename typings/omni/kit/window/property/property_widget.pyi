"""

omni.kit.window.property PropertyWidget base class
"""
from __future__ import annotations
from abc import abstractmethod
from omni.kit.window.property.property_filter import PropertyFilter
__all__: list = ['PropertyWidget']
class PropertyWidget:
    """
    
        Base class to create a group of widgets in Property Window
        
    """
    def __init__(self, title: str):
        """
        Initialize class function
        """
    def build(self, filter_cls: typing.Optional[omni.kit.window.property.property_filter.PropertyFilter] = None):
        """
        UI builder function.
        
                Args:
                    filter_cls (PropertyFilter): filter to use while building UI.
                
        """
    def build_impl(self):
        """
        Main function to creates the UI elements.
        """
    def clean(self):
        """
        Clean up function to be called before destroying the object.
        """
    def on_new_payload(self, payload) -> bool:
        """
        
                Called when a new payload is delivered. PropertyWidget can take this opportunity to update its ui models,
                or schedule full UI rebuild.
        
                Args:
                    payload: The new payload to refresh UI or update model.
        
                Return:
                    True if the UI needs to be rebuilt. build_impl will be called as a result.
                    False if the UI does not need to be rebuilt. build_impl will not be called.
                
        """
    def reset(self):
        """
        Clean up function to be called when previously built widget is no longer visible given new scheme/payload.
        """
