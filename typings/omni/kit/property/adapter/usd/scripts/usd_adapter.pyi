from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.property.adapter.core.scripts.core_adapter import AttributeAdapter
from omni.kit.property.adapter.core.scripts.core_adapter import PrimAdapter
from omni.kit.property.adapter.core.scripts.core_adapter import PropertyType
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
from omni.kit.property.adapter.usd.scripts.notice_wrapper import TfNoticeWrapper
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
import typing
__all__ = ['AttributeAdapter', 'PrimAdapter', 'PropertyType', 'READ_PRIORITY_SETTINGS', 'Sdf', 'StageAdapter', 'TfNoticeWrapper', 'Usd', 'UsdAttributeAdapter', 'UsdPrimAdapter', 'UsdStageAdapter', 'WRITE_PRIORITY_SETTINGS', 'carb', 'omni']
class UsdAttributeAdapter(omni.kit.property.adapter.core.scripts.core_adapter.AttributeAdapter):
    """
    
        Adapter to provide usd attributes with a unified interface so
        that Fabric property can work with UsdProperty code.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def GetPrim(self) -> UsdPrimAdapter:
        ...
    def GetPropertyType(self):
        ...
    def __getattr__(self, attr):
        ...
    def __init__(self, attribute: pxr.Usd.Attribute):
        ...
    @property
    def attribute(self):
        ...
class UsdPrimAdapter(omni.kit.property.adapter.core.scripts.core_adapter.PrimAdapter):
    """
    
        Adapter to provide usd attributes with a unified interface so
        that Fabric property can work with UsdProperty code.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __getattr__(self, attr):
        ...
    def __init__(self, prim: pxr.Usd.Prim):
        ...
    @property
    def prim(self):
        ...
class UsdStageAdapter(omni.kit.property.adapter.core.scripts.core_adapter.StageAdapter):
    """
    
        Adapter to provide usd attributes with a unified interface so
        that Fabric property can work with UsdProperty code.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def CreateChangeTracker(self, attr_names: list[str], prim_paths: list[pxr.Sdf.Path], callback: typing.Callable[[pxr.Usd.ObjectsChanged, pxr.Usd.Stage], NoneType]) -> omni.kit.property.adapter.usd.scripts.notice_wrapper.TfNoticeWrapper:
        ...
    def GetAttributeAtPath(self, path: pxr.Sdf.Path) -> UsdAttributeAdapter:
        ...
    def GetChangeAttributeArgs(self, path, new_value, old_value):
        ...
    def GetPrimAtPath(self, path: pxr.Sdf.Path) -> UsdPrimAdapter:
        ...
    def __getattr__(self, attr):
        ...
    def __init__(self, stage: pxr.Usd.Stage):
        ...
    def convert_data(self, value, dst_adapter_name: str):
        ...
    def get_frame_time_code(self, current_time):
        ...
    def get_notice_paths(self, stage, notice):
        ...
    def resolve_path_array(self, path, resolved_path: str, path_list, index):
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
READ_PRIORITY_SETTINGS: str = '/exts/omni.kit.property.adapter.usd/priority_read'
WRITE_PRIORITY_SETTINGS: str = '/exts/omni.kit.property.adapter.usd/priority_write'
