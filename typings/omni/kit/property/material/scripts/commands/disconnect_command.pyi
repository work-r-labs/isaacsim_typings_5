"""
This module provides a command to disconnect inputs from their sources within the USD shading system.
"""
from __future__ import annotations
import omni as omni
import pxr.UsdShade
from pxr import UsdShade
import typing
__all__: list = ['UsdShadeDisconnectCommand']
class UsdShadeDisconnectCommand(omni.kit.commands.command.Command):
    """
    A command to disconnect a target input from its source in USD's shading system.
    
        This command handles the disconnection of a UsdShade Input from either an Output or another Input that it is connected to. It is capable of storing the source information for undo operations.
    
        Args:
            target (:obj:`UsdShade.Input`): The input to be disconnected from its source.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, target: pxr.UsdShade.Input):
        """
        Initializes the command to disconnect a shading input.
        """
    def do(self):
        """
        Executes the disconnection of a shading input.
        """
    def undo(self):
        """
        Reverts the disconnection of a shading input.
        """
