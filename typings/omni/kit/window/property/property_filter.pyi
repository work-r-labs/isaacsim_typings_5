"""

omni.kit.window.property PropertyFilter base class.
"""
from __future__ import annotations
from omni import ui
__all__: list = ['PropertyFilter']
class PropertyFilter:
    """
    User defined filters for properties. For now, just a substring filter on property names.
    """
    def __init__(self):
        """
        Initialize class function.
        """
    def matches(self, name: str) -> bool:
        """
        Returns True if name matches filter, so property should be visible.
        
                Args:
                    name: name to match.
        
                Returns:
                    bool: True if matched
                
        """
    @property
    def name(self):
        """
        Name getter function.
        
                Returns:
                    str: name
                
        """
    @name.setter
    def name(self, name: str):
        """
        Name setter function.
        
                Args:
                    name: name.
                
        """
    @property
    def name_model(self):
        """
        Model name getter function.
        
                Returns:
                    str: name model.
                
        """
