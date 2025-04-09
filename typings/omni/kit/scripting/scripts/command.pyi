import OmniScriptingSchema as OmniScriptingSchema
import OmniScriptingSchemaTools as OmniScriptingSchemaTools
from __future__ import annotations
import omni as omni
from omni.kit.scripting.scripts.utils import refresh_property_window
from omni.kit.usd_undo.layer_undo import UsdLayerUndo
import pxr.Sdf
from pxr import Sdf
import typing
__all__ = ['ApplyScriptingAPICommand', 'OmniScriptingSchema', 'OmniScriptingSchemaTools', 'RefreshScriptingPropertyWindowCommand', 'RemoveScriptingAPICommand', 'SCRIPTS_ATTR', 'Sdf', 'UsdLayerUndo', 'omni', 'refresh_property_window']
class ApplyScriptingAPICommand(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer: pxr.Sdf.Layer = None, paths: typing.List[pxr.Sdf.Path] = list()):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class RefreshScriptingPropertyWindowCommand(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class RemoveScriptingAPICommand(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer: pxr.Sdf.Layer = None, paths: typing.List[pxr.Sdf.Path] = list()):
        ...
    def do(self):
        ...
    def undo(self):
        ...
SCRIPTS_ATTR: str = 'omni:scripting:scripts'
