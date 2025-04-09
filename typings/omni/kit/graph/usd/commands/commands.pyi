from __future__ import annotations
import omni as omni
from omni.usd.commands.stage_helper import UsdStageHelper
from omni.usd.commands.usd_commands import DeletePrimsCommand
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdUI
import typing
__all__: list = ['CreateUsdUIBackdropCommand', 'CreateUsdUINoteCommand', 'UsdUINodeGraphNodeSetCommand', 'UsdUIRemovePositionCommand']
class CreateUsdUIBackdropCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path: pxr.Sdf.Path, identifier: str, position: typing.Optional[typing.Tuple[float]] = None, size: typing.Optional[typing.Tuple[float]] = None, display_color: typing.Optional[typing.Tuple[float]] = None, stage: typing.Optional[pxr.Usd.Stage] = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CreateUsdUINoteCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path: pxr.Sdf.Path, identifier: str, position: typing.Optional[typing.Tuple[float]] = None, size: typing.Optional[typing.Tuple[float]] = None, display_color: typing.Optional[typing.Tuple[float]] = None, stage: typing.Optional[pxr.Usd.Stage] = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class UsdUINodeGraphNodeSetCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    
        Set UsdUINodeGraphNode attribute value.
    
        Args:
            attribute (str): Name of the UsdUINodeGraphNode attribute to set.
            prim_path (Sdf.Path): Prim path.
            value: Value to change to.
            prev: Value to undo to.
            stage (Usd.Stage): Stage on which to perform the action.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, attribute: str, prim_path: pxr.Sdf.Path, value, prev, stage: pxr.Usd.Stage = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class UsdUIRemovePositionCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    
        Remove UsdUI position attribute from prim.
    
        Args:
            prim_path (Sdf.Path): Prim path.
            stage (Usd.Stage): Stage on which to perform the action.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: pxr.Sdf.Path, stage: pxr.Usd.Stage = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
def get_first_available_path(stage, parent_path, identifier):
    ...
