"""

omni.kit.window.property PropertySchemeDelegate base class
"""
from __future__ import annotations
from abc import abstractmethod
__all__: list = ['PropertySchemeDelegate']
class PropertySchemeDelegate:
    """
    
        PropertySchemeDelegate is a class to test given payload and determine what widgets to be drawn in what order.
        
    """
    def get_unwanted_widgets(self, payload) -> typing.List[str]:
        """
        
                Tests the payload and returns a list of widget names which this delegate does not want to include.
                Note that if there is another PropertySchemeDelegate returning widget in its get_widgets that conflicts with
                names in get_unwanted_widgets, get_widgets always wins (i.e. the Widget will be drawn).
        
                This function is optional.
        
                Args:
                    payload (PrimSelectionPayload): payload.
        
                Returns:
                    list: list of unwanted widgets.
                
        """
    def get_widgets(self, payload) -> typing.List[str]:
        """
        
                Tests the payload and gathers widgets in interest to be drawn in specific order.
        
                Args:
                    payload (PrimSelectionPayload): payload.
        
                Returns:
                    list: list of widgets to build.
                
        """
