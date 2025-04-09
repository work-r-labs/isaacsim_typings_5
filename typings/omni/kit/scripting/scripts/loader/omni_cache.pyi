from __future__ import annotations
import asyncio as asyncio
import carb as carb
from omni import client as oc
import omni.client.impl._omniclient
from omni.kit.scripting.scripts.loader import io
import os as os
import pathlib
from pathlib import Path
import shutil as shutil
import typing
__all__ = ['EVENT_TYPE_SCRIPT_FILE_DELETED', 'EVENT_TYPE_SCRIPT_FILE_UPDATED', 'OmniCache', 'Path', 'asyncio', 'carb', 'io', 'oc', 'os', 'shutil']
class OmniCache:
    _event_stream: typing.ClassVar[carb.events._events.IEventStream]  # value = <carb.events._events.IEventStream object>
    _file_watches: typing.ClassVar[dict] = {}
    _file_watches_info: typing.ClassVar[dict] = {}
    _file_watches_remote: typing.ClassVar[dict] = {}
    _loop: typing.ClassVar[asyncio.unix_events._UnixSelectorEventLoop]  # value = <_UnixSelectorEventLoop running=True closed=False debug=False>
    _path: typing.ClassVar[pathlib.PosixPath]  # value = PosixPath('/home/chris/.nvidia-omniverse/pycache')
    _path_cache: typing.ClassVar[dict] = {}
    @classmethod
    def _on_omni_event_local(cls, result: omni.client.impl._omniclient.Result, event: omni.client.impl._omniclient.ListEvent, entry: omni.client.impl._omniclient.ListEntry, src: str, dst: str) -> None:
        ...
    @classmethod
    def _on_omni_event_remote(cls, result: omni.client.impl._omniclient.Result, event: omni.client.impl._omniclient.ListEvent, entry: omni.client.impl._omniclient.ListEntry, src: str, dst: str) -> None:
        ...
    @classmethod
    def _on_omni_sub_local(cls, result: omni.client.impl._omniclient.Result, entry: omni.client.impl._omniclient.ListEntry, path: str) -> None:
        ...
    @classmethod
    def _sanitize_name(cls, name: str) -> str:
        ...
    @classmethod
    def add_script(cls, path: str) -> str:
        ...
    @classmethod
    def convert_path(cls, path: str) -> str:
        ...
    @classmethod
    def get_event_stream(cls):
        ...
    @classmethod
    def initialize(cls) -> None:
        ...
    @classmethod
    def shutdown(cls) -> None:
        ...
    @classmethod
    def source_path(cls, cache_path: str) -> str:
        ...
EVENT_TYPE_SCRIPT_FILE_DELETED: int = 683852953784394755
EVENT_TYPE_SCRIPT_FILE_UPDATED: int = 11220903237346331397
