from __future__ import annotations
__all__ = ['AddCmdlineArgs']
def AddCmdlineArgs(argsParser, defaultValue = None, altHelpText = ''):
    """
    
        Adds camera-related command line arguments to argsParser.
    
        The resulting 'camera' argument will be an Sdf.Path. If no value is given
        and defaultValue is not overridden, 'camera' will be a single-element path
        containing the primary camera name.
        
    """
