from __future__ import annotations
import isaacsim.asset.importer.mjcf._mjcf
from isaacsim.asset.importer.mjcf import _mjcf
import omni as omni
from omni.client.impl._omniclient import Result
import os as os
from pxr import Usd
import typing
__all__ = ['MJCFCreateAsset', 'MJCFCreateImportConfig', 'Result', 'Usd', 'omni', 'os']
class MJCFCreateAsset(omni.kit.commands.command.Command):
    """
    
        This command parses and imports a given mjcf file.
    
        Args:
            arg0 (:obj:`str`): The absolute path the mjcf file
    
            arg1 (:obj:`isaacsim.asset.importer.mjcf._mjcf.ImportConfig`): Import configuration
    
            arg2 (:obj:`str`): Path to the robot on the USD stage
    
            arg3 (:obj:`str`): destination path for robot usd. Default is "" which will load the robot in-memory on the open stage.
    
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mjcf_path: str = '', import_config = ..., prim_path: str = '', dest_path: str = '') -> None:
        ...
    def do(self) -> str:
        ...
    def undo(self) -> None:
        ...
class MJCFCreateImportConfig(omni.kit.commands.command.Command):
    """
    
        Returns an ImportConfig object that can be used while parsing and importing.
        Should be used with the `MJCFCreateAsset` command
    
        Returns:
            :obj:`isaacsim.asset.importer.mjcf._mjcf.ImportConfig`: Parsed MJCF stored in an internal structure.
    
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self) -> None:
        ...
    def do(self) -> isaacsim.asset.importer.mjcf._mjcf.ImportConfig:
        ...
    def undo(self) -> None:
        ...
