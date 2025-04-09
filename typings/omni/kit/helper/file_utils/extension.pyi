from __future__ import annotations
import carb as carb
from carb import events
from carb import log_warn
import collections
from collections import OrderedDict
import dataclasses
from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime
import omni as omni
from omni.kit.helper.file_utils import asset_types
import typing
from urllib import parse
__all__ = ['FILE_EVENT_QUEUE_UPDATED', 'FILE_OPENED_EVENT', 'FILE_SAVED_EVENT', 'FileEventHistoryExtension', 'FileEventModel', 'OrderedDict', 'asdict', 'asset_types', 'carb', 'dataclass', 'datetime', 'events', 'g_singleton', 'get_instance', 'log_warn', 'omni', 'parse']
class FileEventHistoryExtension(omni.ext._extensions.IExt):
    """
    A class for managing the history of file events within an application.
    
        This class subscribes to file events, maintains a queue of these events up to a specified maximum size, and provides methods for querying and manipulating this event history. It is designed to integrate with an application's event system, capturing information about file operations such as opening and saving files.
    
        Args:
            max_queue_size (int): The maximum number of events to retain in the queue.
    """
    FILE_EVENT_QUEUE_SETTING: typing.ClassVar[str] = '/persistent/app/omniverse/fileEventHistory'
    def __init__(self, max_queue_size: int = 100):
        ...
    def _adjust_queue_size(self, queue: collections.OrderedDict):
        ...
    def _deserialize_uri(self, uri: str) -> typing.Tuple[str, omni.kit.helper.file_utils.extension.FileEventModel]:
        ...
    def _load_queue_from_settings(self) -> collections.OrderedDict:
        ...
    def _on_file_event(self, event: carb.events._events.IEvent):
        ...
    def _save_queue_to_settings(self, queue: collections.OrderedDict):
        ...
    def _serialize_uri(self, file_event: FileEventModel) -> str:
        ...
    def clear_event_queue(self):
        ...
    def get_latest_urls_from_event_queue(self, num_latest: int = 1, asset_type: str = None, event_type: int = 0, tag: str = None) -> typing.List[str]:
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
    @property
    def event_queue(self):
        ...
class FileEventModel:
    """
    A data model representing a file event within the application.
    
        This class holds information about a file-related event, such as opening or saving a file.
    
        Args:
            url: str
                The URL of the file associated with the event.
            asset_type: Optional[str]
                The type of asset involved in the event (e.g., image, model).
            is_folder: Optional[bool]
                Flag indicating whether the URL points to a folder.
            event_type: Optional[int]
                Numerical ID representing the type of event (e.g., opened, saved).
            tag: Optional[str]
                An optional tag providing additional context for the event.
            datetime: Optional[datetime]
                Timestamp of when the event occurred.
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'url': Field(name='url',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'asset_type': Field(name='asset_type',type=typing.Optional[str],default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'is_folder': Field(name='is_folder',type=typing.Optional[bool],default=False,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'event_type': Field(name='event_type',type=typing.Optional[int],default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'tag': Field(name='tag',type=typing.Optional[str],default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'datetime': Field(name='datetime',type=<class 'NoneType'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('url', 'asset_type', 'is_folder', 'event_type', 'tag', 'datetime')
    asset_type = None
    datetime = None
    event_type = None
    is_folder: typing.ClassVar[bool] = False
    tag = None
    def __eq__(self, other):
        ...
    def __init__(self, url: str, asset_type: typing.Optional[str] = None, is_folder: typing.Optional[bool] = False, event_type: typing.Optional[int] = None, tag: typing.Optional[str] = None, datetime: None = None) -> None:
        ...
    def __repr__(self):
        ...
    def dict(self):
        """
        
                Returns a dictionary representation of FileEventModel object.
        
                Returns:
                    dict: A dictionary containing the object's attributes as key-value pairs.
                
        """
def get_instance():
    ...
FILE_EVENT_QUEUE_UPDATED: int = 4806079216508642737
FILE_OPENED_EVENT: int = 3872619916304892462
FILE_SAVED_EVENT: int = 8148521607818097614
g_singleton: FileEventHistoryExtension  # value = <omni.kit.helper.file_utils.extension.FileEventHistoryExtension object>
