from __future__ import annotations
import carb as carb
import enum
from enum import IntEnum
from enum import auto
import omni as omni
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
import pxr.Usd
from pxr import Usd
import typing
__all__ = ['CorePropertyAdapterExtension', 'IntEnum', 'RegistryEventType', 'SceneDescriptionAdapterRegistry', 'StageAdapter', 'Usd', 'auto', 'carb', 'get_adapter_registry', 'omni']
class CorePropertyAdapterExtension(omni.ext._extensions.IExt):
    _core_instance: typing.ClassVar[CorePropertyAdapterExtension]  # value = <omni.kit.property.adapter.core.scripts.extension.CorePropertyAdapterExtension object>
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    @property
    def adapter_registry(self) -> SceneDescriptionAdapterRegistry:
        ...
class RegistryEventType(enum.IntEnum):
    """
    An enumeration.
    """
    ADAPTER_ADDED: typing.ClassVar[RegistryEventType]  # value = <RegistryEventType.ADAPTER_ADDED: 1>
    ADAPTER_REMOVED: typing.ClassVar[RegistryEventType]  # value = <RegistryEventType.ADAPTER_REMOVED: 2>
class SceneDescriptionAdapterRegistry:
    """
    
        Registry for stage adapters.
        
    """
    def __init__(self):
        ...
    def instantiate_all_stage_adapters(self, stage: pxr.Usd.Stage) -> typing.Dict[str, omni.kit.property.adapter.core.scripts.core_adapter.StageAdapter]:
        """
        
                Returns a dictionary of valid registered adapters where the key is the adapter and the value is the name (str).
                
        """
    def register_stage_adapter(self, name: str, adapter_type: typing.Callable[[pxr.Usd.Stage], omni.kit.property.adapter.core.scripts.core_adapter.StageAdapter]):
        """
        
                Register a stage adapter. Sends out an event after an adapter is added.
                
        """
    def unregister_stage_adapter(self, name: str):
        """
        
                Unregister a stage adapter given a name. Sends out an event after an adapter is removed.
                
        """
    @property
    def event_stream(self) -> carb.events._events.IEventStream:
        ...
    @property
    def registered_adapters(self) -> typing.Dict[str, typing.Callable[[pxr.Usd.Stage], omni.kit.property.adapter.core.scripts.core_adapter.StageAdapter]]:
        ...
def get_adapter_registry():
    """
    
        Returns the adapter registry.
        
    """
