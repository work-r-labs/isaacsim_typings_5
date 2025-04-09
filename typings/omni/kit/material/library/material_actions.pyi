"""
Register material actions class.
"""
from __future__ import annotations
import omni as omni
__all__: list = ['register_actions', 'deregister_actions']
def deregister_actions(extension_id):
    """
    
        Unregister material actions.
    
        Arg:
            extension_id (str): extensions id.
        
    """
def register_actions(extension_id, cls):
    """
    
        Register material actions.
    
        Arg:
            extension_id (str): extensions id.
            cls (class): callers class for function calls.
        
    """
