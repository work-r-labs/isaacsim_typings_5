from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import Enum
from functools import lru_cache
import omni as omni
from pxr import Gf
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import typing as typing
__all__ = ['Enum', 'EventDispatcher', 'EventType', 'Gf', 'Sdf', 'Tf', 'Trace', 'Usd', 'UsdWatcher', 'asyncio', 'carb', 'get_watcher', 'lru_cache', 'omni', 'typing']
class EventDispatcher:
    def _EventDispatcher__async_pump(self):
        ...
    def __init__(self):
        ...
    def _dispatch_changed(self, path):
        ...
    def _send_callbacks(self, cb_path, changed_path):
        ...
    def destroy(self):
        ...
    def on_changes(self, paths):
        ...
    def pump(self):
        ...
    def subscribe_on_change(self, path, on_change: typing.Callable) -> carb._carb.Subscription:
        ...
class EventType(enum.Enum):
    """
    An enumeration.
    """
    CHANGE_INFO_ONLY: typing.ClassVar[EventType]  # value = <EventType.CHANGE_INFO_ONLY: 0>
    RESYNC: typing.ClassVar[EventType]  # value = <EventType.RESYNC: 1>
class UsdWatcher:
    """
    Internal. Utility class to wrap UsdNotice handling.
    
        It supports to subscribe specific paths.
        
    """
    _is_watcher_instanced: typing.ClassVar[bool] = True
    @staticmethod
    def _is_instantiated():
        ...
    @staticmethod
    def _on_prim_change(*args, **kwargs):
        ...
    def __init__(self):
        ...
    def _attach_stage(self, stage):
        """
        Internal: called when stage is attached.
        """
    def _detach_stage(self):
        """
        Internal: called when stage is closing.
        """
    def _get_dispatcher(self, event_type: EventType):
        ...
    def destroy(self):
        ...
    def subscribe_to_change_info_path(self, path: pxr.Sdf.Path, on_change: typing.Callable) -> carb._carb.Subscription:
        ...
    def subscribe_to_resync_path(self, path: pxr.Sdf.Path, on_change: typing.Callable) -> carb._carb.Subscription:
        ...
def get_watcher(*args, **kwargs):
    """
    Singleton of UsdWatcher omni.usd module.
    """
