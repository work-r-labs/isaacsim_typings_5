from __future__ import annotations
import abc as abc
import omni as omni
from omni.usd.commands.stage_helper import UsdStageHelper
from omni.usd.commands.usd_commands import CreateShaderPrimFromSdrCommand
from omni.usd.commands.usd_commands import DeletePrimsCommand
from pxr import Sdf
import pxr.Sdf
from pxr import Sdr
from pxr import Tf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
import pxr.UsdShade
from pxr import UsdUI
import typing
__all__: list = ['ConnectUsdShadeToSourceCommand', 'CreateInputPortCommand', 'CreateOutputPortCommand', 'ImportCompoundCommand', 'NewUsdShadeMaterialCommand', 'NewUsdShadeNodeCommand', 'NewUsdShadeNodeGraphCommand', 'UsdShadeDisconnectSourceCommand']
class ConnectUsdShadeToSourceCommand(omni.kit.commands.command.Command):
    """
    Undoable UsdShade.Input.ConnectToSource
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, target: pxr.UsdShade.Input, source: pxr.UsdShade.Output):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CreateAbstractPortCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    
        Base class for CreateInputPortCommand and for CreateOutputPortCommand
        that has the shared code for both.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'_create_port'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: pxr.Sdf.Path, port_name: str, port_type: pxr.Sdf.ValueTypeName, stage = None):
        ...
    def _create_port(self, prim):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CreateInputPortCommand(CreateAbstractPortCommand):
    """
    
        Create connectable input on the prim
    
        ### Arguments:
    
            `prim_path : Sdf.Path`
                The path of the prim we need to add the new port.
    
            `port_name : str`
                The name of the port. The attribute name will be `inputs:port_name`.
    
            `port_type : Sdf.ValueTypeName`
                The type of the port.
    
            `stage : Optional[int]`
                The stage it's necessary to add the new prim. If None, it takes
                the stage from the USD Context.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: pxr.Sdf.Path, port_name: str, port_type: pxr.Sdf.ValueTypeName, stage = None):
        ...
    def _create_port(self, prim):
        ...
class CreateOutputPortCommand(CreateAbstractPortCommand):
    """
    
        Create connectable output on the prim
    
        ### Arguments:
    
            `prim_path : Sdf.Path`
                The path of the prim we need to add the new port.
    
            `port_name : str`
                The name of the port. The attribute name will be `outputs:port_name`.
    
            `port_type : Sdf.ValueTypeName`
                The type of the port.
    
            `stage : Optional[int]`
                The stage it's necessary to add the new prim. If None, it takes
                the stage from the USD Context.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: pxr.Sdf.Path, port_name: str, port_type: pxr.Sdf.ValueTypeName, stage = None):
        ...
    def _create_port(self, prim):
        ...
class ImportCompoundCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    
        Import compound shader from external USD file.
    
        ### Arguments:
    
            `parent_path : Sdf.Path`
                The path of the prim we need to add the new compound to.
    
            `source_asset : str`
                The path of the external usd file. It's important the default
                prim in this layer is the NodeGraph prim.
    
            `identifier : str`
                The name of the new prim.
    
            `position : Optional[List[int]]`
                The position of the new node in the canvas.
    
            `stage : Optional[int]`
                The stage it's necessary to add the new prim. If None, it takes
                the stage from the USD Context.
    
            `attributes_to_set: Optional[Dict[Sdf.Path, Any]]`
                Dict that has the list of attributes and values to set after the
                prim is imported.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path: pxr.Sdf.Path, source_asset: str, identifier: str, position: typing.Optional[typing.List[int]] = None, stage = None, path = None, attributes_to_set: typing.Optional[typing.Dict[pxr.Sdf.Path, typing.Any]] = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class NewUsdShadeMaterialCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path: pxr.Sdf.Path, identifier: str, position: typing.Optional[typing.Tuple[int]] = None, select_new_prim: bool = False, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class NewUsdShadeNodeCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path, source_asset, sub_identifier, position, node, stage = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class NewUsdShadeNodeFromSdrCommand(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path, identifier, position):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class NewUsdShadeNodeGraphCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path, identifier, position, stage = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class UsdShadeDisconnectSourceCommand(omni.kit.commands.command.Command):
    """
    Undoable UsdShade.Input.DisconnectSource
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, target: pxr.UsdShade.Input):
        ...
    def do(self):
        ...
    def undo(self):
        ...
