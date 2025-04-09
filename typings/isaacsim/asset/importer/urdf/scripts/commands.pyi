from __future__ import annotations
import isaacsim.asset.importer.urdf._urdf
from isaacsim.asset.importer.urdf import _urdf
import omni as omni
from omni.client.impl._omniclient import Result
import os as os
from pxr import Usd
import typing
__all__ = ['Result', 'URDFCreateImportConfig', 'URDFImportRobot', 'URDFParseAndImportFile', 'URDFParseFile', 'URDFParseText', 'Usd', 'omni', 'os']
class URDFCreateImportConfig(omni.kit.commands.command.Command):
    """
    
        Returns an ImportConfig object that can be used while parsing and importing.
        Should be used with `URDFParseFile` and `URDFParseAndImportFile` commands
    
        Returns:
            :obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`: Parsed URDF stored in an internal structure.
    
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self) -> None:
        ...
    def do(self) -> isaacsim.asset.importer.urdf._urdf.ImportConfig:
        ...
    def undo(self) -> None:
        ...
class URDFImportRobot(omni.kit.commands.command.Command):
    """
    
        This command parses and imports a given urdf and returns a UrdfRobot object
    
        Args:
            arg0 (:obj:`str`): The absolute path to where the urdf file is
    
            arg1 (:obj:`UrdfRobot`): The parsed URDF Robot
    
            arg2 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import Configuration
    
            arg3 (:obj:`str`): destination path for robot usd. Default is "" which will load the robot in-memory on the open stage.
    
            arg4 (:obj:`bool`): if True, return the articulation Root prim path instead of the object's base path.
    
        Returns:
            :obj:`str`: Path to the robot on the USD stage.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, urdf_path: str = '', urdf_robot: isaacsim.asset.importer.urdf._urdf.UrdfRobot = None, import_config = ..., dest_path: str = '', get_articulation_root: bool = False) -> None:
        ...
    def do(self) -> str:
        ...
    def undo(self) -> None:
        ...
class URDFParseAndImportFile(omni.kit.commands.command.Command):
    """
    
        This command parses and imports a given urdf and returns a UrdfRobot object
    
        Args:
            arg0 (:obj:`str`): The absolute path to where the urdf file is
    
            arg1 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import Configuration
    
            arg2 (:obj:`str`): destination path for robot usd. Default is "" which will load the robot in-memory on the open stage.
    
            arg3 (:obj:`bool`): if True, return the articulation Root prim path instead of the object's base path.
    
        Returns:
            :obj:`str`: Path to the robot on the USD stage.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, urdf_path: str = '', import_config = ..., dest_path: str = '', get_articulation_root: bool = False) -> None:
        ...
    def do(self) -> str:
        ...
    def undo(self) -> None:
        ...
class URDFParseFile(omni.kit.commands.command.Command):
    """
    
        This command parses a given urdf and returns a UrdfRobot object
    
        Args:
            arg0 (:obj:`str`): The absolute path to where the urdf file is
    
            arg1 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import Configuration
    
        Returns:
            :obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`: Parsed URDF stored in an internal structure.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, urdf_path: str = '', import_config: isaacsim.asset.importer.urdf._urdf.ImportConfig = ...) -> None:
        ...
    def do(self) -> isaacsim.asset.importer.urdf._urdf.UrdfRobot:
        ...
    def undo(self) -> None:
        ...
class URDFParseText(omni.kit.commands.command.Command):
    """
    
        This command parses a given urdf and returns a UrdfRobot object
    
        Args:
            arg0 (:obj:`str`): The absolute path to where the urdf file is
    
            arg1 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import Configuration
    
        Returns:
            :obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`: Parsed URDF stored in an internal structure.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, urdf_string: str = '', import_config: isaacsim.asset.importer.urdf._urdf.ImportConfig = ...) -> None:
        ...
    def do(self) -> isaacsim.asset.importer.urdf._urdf.UrdfRobot:
        ...
    def undo(self) -> None:
        ...
