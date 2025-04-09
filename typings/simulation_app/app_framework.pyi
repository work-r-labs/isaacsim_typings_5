from __future__ import annotations
import builtins as builtins
import carb as carb
import omni as omni
import os as os
import sys as sys
import typing as typing
__all__ = ['AppFramework', 'builtins', 'carb', 'omni', 'os', 'sys', 'typing']
class AppFramework:
    """
    Minimal omniverse application that launches without any application config
    """
    def __init__(self, name: str = 'kit', argv = list()):
        ...
    def close(self):
        """
        Close the running Omniverse Toolkit.
        """
    def update(self) -> None:
        """
        
                Convenience function to step the application forward one frame
                
        """
    @property
    def app(self) -> omni.kit.app._app.IApp:
        """
        
                omni.kit.app.IApp: omniverse kit application object
                
        """
    @property
    def framework(self) -> typing.Any:
        """
        
                omni.kit.app.IApp: omniverse kit application object
                
        """
