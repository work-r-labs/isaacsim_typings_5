from __future__ import annotations
import carb as carb
import collections
from collections import OrderedDict
from collections import namedtuple
from functools import lru_cache
from itertools import islice
import typing
__all__ = ['HistoryEntry', 'MAX_HISTORY_SIZE', 'OrderedDict', 'PRIMITIVE_TYPES', 'add_history', 'carb', 'change_history', 'clear_history', 'get_history', 'get_history_item', 'islice', 'lru_cache', 'namedtuple']
class HistoryEntry(tuple):
    """
    HistoryEntry(name, kwargs, level, error)
    """
    __match_args__: typing.ClassVar[tuple] = ('name', 'kwargs', 'level', 'error')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('name', 'kwargs', 'level', 'error')
    @staticmethod
    def __new__(_cls, name, kwargs, level, error):
        """
        Create new instance of HistoryEntry(name, kwargs, level, error)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new HistoryEntry object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new HistoryEntry object replacing specified fields with new values
        """
def _format_history_entry(history: HistoryEntry):
    ...
def _get_crash_report_history_count(*args, **kwargs):
    ...
def add_history(name: str, kwargs: dict, level: int):
    """
    Add a **Command** execution to the history.
    
        Takes: (Command name, Arguments, Groupping level).
        Return: index that can be used to modify it later
    """
def change_history(key: int, **kwargs):
    """
    Update the history entry for **key**.
    
        key: Index of the history entry to modify.
        kwargs: any of the properties of HistoryEntry.
    """
def clear_history():
    """
    Clear **Command** execution history.
    """
def get_history():
    """
    Get **Command** execution history.
    
        Returns a list of tuples: HistoryEntry(Command name, Arguments, Groupping level, Error status).
    """
def get_history_item(history_key: int) -> HistoryEntry:
    ...
MAX_HISTORY_SIZE: int = 1000000
PRIMITIVE_TYPES: set = {"<class 'int'>", "<class 'bool'>", "<class 'str'>", "<class 'pxr.Sdf.Path'>", "<class 'float'>"}
_history: collections.OrderedDict  # value = OrderedDict()
_history_index: int = 2
