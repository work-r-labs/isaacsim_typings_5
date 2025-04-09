from __future__ import annotations
import asyncio as asyncio
from collections import defaultdict
import concurrent as concurrent
import dataclasses
from dataclasses import dataclass
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
from pxr import Trace
import pxr.Usd
from pxr import Usd
import typing
import weakref as weakref
__all__: list = ['start', 'stop', 'subscribe']
class _USDWatch:
    """
    
        The object that holds a single Tf.Notice.Listener and executes callbacks
        when specific attribute is changed.
        
    """
    class _USDWatchCallbackHandler:
        """
        Holds the callbacks
        """
        __dataclass_fields__: typing.ClassVar[dict]  # value = {'changed_fn': Field(name='changed_fn',type=typing.Callable[[], NoneType],default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
        __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
        __hash__: typing.ClassVar[None] = None
        __match_args__: typing.ClassVar[tuple] = ('changed_fn')
        def __eq__(self, other):
            ...
        def __init__(self, changed_fn: typing.Callable[[], NoneType]) -> None:
            ...
        def __repr__(self):
            ...
    @staticmethod
    def _USDWatch__delayed_prim_changed(*args, **kwargs):
        ...
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        """
        Called by Usd.Notice.ObjectsChanged
        """
    def __init__(self):
        ...
    def _unsubscribe(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, dead):
        """
        Stop the subscription of the given attribute
        """
    def _update_dirty(self):
        """
        
                Execute the callbacks for the dirty items that was collected from
                TfNotice. It can be called any time to pump changes.
                
        """
    def clear_all(self):
        """
        Stop Tf.Notice and clear callbacks
        """
    def destroy(self):
        """
        Should be executed before the object is killed
        """
    def subscribe(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, callback: typing.Callable[[], NoneType]):
        """
        
                Lets execute the callback when the given attribute is changed. The
                callback will be executed while the returned object is alive.
                
        """
def start():
    """
    Starts watch
    """
def stop():
    """
    Stops watch
    """
def subscribe(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, callback: typing.Callable[[], NoneType]):
    """
    
        Lets execute the callback when the given attribute is changed. The
        callback will be executed while the returned object is alive. If returned
        object is None, the watch is not started.
        
    """
__watch: _USDWatch  # value = <omni.kit.viewport.menubar.core.utils.usd_watch._USDWatch object>
