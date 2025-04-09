"""

garch

"""
from __future__ import annotations
__all__ = ['GLPlatformDebugContext']
class GLPlatformDebugContext(Boost.Python.instance):
    """
    
    Platform specific context (e.g. X11/GLX) which supports debug output.
    
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(majorVersion, minorVersion, coreProfile, directRenderering)
        
        
        Parameters
        ----------
        majorVersion : int
        
        minorVersion : int
        
        coreProfile : bool
        
        directRenderering : bool
        
        
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def makeCurrent(*args, **kwargs):
        """
        
        makeCurrent() -> None
        
        
        
        """
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
__MFB_FULL_PACKAGE_NAME: str = 'garch'
