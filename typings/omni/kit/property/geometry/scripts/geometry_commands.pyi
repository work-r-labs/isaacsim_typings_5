from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
from pxr import UsdGeom
import typing
from typing import Any
__all__: list[str] = ['Any', 'PrimVarCommand', 'Sdf', 'ToggleInstanceableCommand', 'TogglePrimVarCommand', 'UsdGeom', 'carb', 'omni']
class PrimVarCommand(omni.kit.commands.command.Command):
    """
    Set undoable primvar command.
    
        Args:
            prim_path (list): List of paths of prims.
            prim_name (str): Primvar name.
            prim_type (str): Primvar variable type (E.g. Sdf.ValueTypeNames.Bool).
            value (any): New primvar value. If primvar does not exist, it will be created.
            usd_context_name (Optional[str]): USD context name.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], prim_name: str, prim_type: str, value: typing.Any, usd_context_name: typing.Optional[str] = ''):
        """
        Initializes a PrimVarCommand instance for updating primvar values. Sets up internal state for execution.
        """
    def do(self):
        """
        Performs the update of primvar values on the specified prim paths and stores the original values for undo.
        """
    def undo(self):
        """
        Reverts the primvar values to their original state by using the stored undo information.
        """
class ToggleInstanceableCommand(omni.kit.commands.command.Command):
    """
    Toggle instanceable undoable **Command**.
    
        Args:
            prim_path (list): List of paths of prims.
            usd_context_name (str, optional): USD context name. Defaults to ""
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], usd_context_name: typing.Optional[str] = ''):
        """
        Initializes a new ToggleInstanceableCommand. This command sets up the internal state to toggle the instanceable property for each prim in the provided prim_path.
        """
    def do(self):
        """
        Executes the command by toggling the instanceable property of each prim specified in prim_path.
        """
    def undo(self):
        """
        Reverses the command by restoring the original instanceable state for each prim in prim_path.
        """
class TogglePrimVarCommand(omni.kit.commands.command.Command):
    """
    Toggle primvar undoable Command.
    
        Args:
            prim_path (list): List of paths of prims.
            prim_name (str): Primvar name.
            usd_context_name (str): USD context name.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], prim_name: str, usd_context_name: typing.Optional[str] = ''):
        """
        Initializes the TogglePrimVarCommand which toggles a boolean primvar for the specified prims.
        """
    def do(self):
        """
        Executes the TogglePrimVarCommand, toggling the boolean primvar value for each prim.
        """
    def undo(self):
        """
        Reverts the changes made by the TogglePrimVarCommand, restoring the original primvar values.
        """
