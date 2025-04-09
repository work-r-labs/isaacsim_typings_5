from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import enum
from enum import Enum
from enum import auto
import typing
__all__ = ['ABC', 'AttributeAdapter', 'Enum', 'PrimAdapter', 'PropertyType', 'StageAdapter', 'abstractmethod', 'auto']
class AttributeAdapter(abc.ABC):
    """
    
        Attribute Adapter
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'GetPrim', 'GetPropertyType'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def GetPrim(self):
        ...
    def GetPropertyType(self):
        ...
    def __getattr__(self, attr):
        ...
    def __init__(self, attribute) -> None:
        ...
    @property
    def attribute(self):
        ...
class PrimAdapter(abc.ABC):
    """
    
        Prim Adapter
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __getattr__(self, attr):
        ...
    def __init__(self, prim) -> None:
        ...
    @property
    def prim(self):
        ...
class PropertyType(enum.Enum):
    """
    An enumeration.
    """
    ATTRIBUTE: typing.ClassVar[PropertyType]  # value = <PropertyType.ATTRIBUTE: (<enum.auto object>,)>
    RELATIONSHIP: typing.ClassVar[PropertyType]  # value = <PropertyType.RELATIONSHIP: 1>
class StageAdapter(abc.ABC):
    """
    
        Stage Adapter
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'GetPrimAtPath', 'resolve_path_array', 'GetAttributeAtPath', 'get_notice_paths', 'convert_data', 'CreateChangeTracker'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def CreateChangeTracker(self, attr_names: list, prim_paths: list, callback: typing.Callable) -> typing.Any:
        ...
    def GetAttributeAtPath(self, path):
        ...
    def GetPrimAtPath(self, path):
        ...
    def __getattr__(self, attr):
        ...
    def __init__(self, stage) -> None:
        ...
    def convert_data(self, data, dst_adapter_name: str):
        ...
    def get_notice_paths(self, stage, notice):
        ...
    def resolve_path_array(self, path, resolve_path: str, path_list, index):
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def priority_read(self) -> int:
        ...
    @property
    def priority_write(self) -> int:
        ...
    @property
    def stage(self):
        ...
    @property
    def usd_stage(self):
        ...
