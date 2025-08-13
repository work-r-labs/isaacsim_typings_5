from __future__ import annotations
__all__: list[str] = ['AddCmdlineArgs']
def AddCmdlineArgs(argsParser, defaultValue = 'sRGB', altHelpText = ''):
    """
    
        Adds color-related command line arguments to argsParser.
    
        The resulting 'colorCorrectionMode' argument will be a Python string.
        
    """
