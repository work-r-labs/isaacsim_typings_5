"""
This module provides a Singleton pattern implementation that ensures a class has only one instance and provides a global point of access to it.
"""
from __future__ import annotations
__all__ = ['Singleton']
def Singleton(class_):
    """
    Ensures a class has only one instance and provides a global point of access to it.
    
        Args:
            class_ (type): The class to be instantiated as a singleton.
    """
