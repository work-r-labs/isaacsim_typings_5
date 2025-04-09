from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
from pxr import UsdGeom
import typing
__all__ = ['PrimVarCommand', 'Sdf', 'ToggleInstanceableCommand', 'TogglePrimVarCommand', 'UsdGeom', 'carb', 'omni']
class PrimVarCommand(omni.kit.commands.command.Command):
    """
    
        Set primvar undoable **Command**.
    
        Args:
            prim_path (list): List of paths of prims.
            prim_name (str): Primvar name.
            prim_type (): Primvar variable type (EG. Sdf.ValueTypeNames.Bool)
            value (any): New primvar value. If primvar doesn't exist, it will be created
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], prim_name: str, prim_type: str, value: typing.Any, usd_context_name: typing.Optional[str] = ''):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ToggleInstanceableCommand(omni.kit.commands.command.Command):
    """
    
        Toggle instanceable undoable **Command**.
    
        Args:
            prim_path (list): List of paths of prims.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], usd_context_name: typing.Optional[str] = ''):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class TogglePrimVarCommand(omni.kit.commands.command.Command):
    """
    
        Toggle primvar undoable **Command**.
    
        Args:
            prim_path (list): List of paths of prims.
            prim_name (str): Primvar name.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: typing.List[str], prim_name: str, usd_context_name: typing.Optional[str] = ''):
        ...
    def do(self):
        ...
    def undo(self):
        ...
