from __future__ import annotations
from collections import namedtuple
from functools import partial
from omni import ui
import typing
__all__ = ['GraphEditorCoreBreadcrumbs', 'namedtuple', 'partial', 'ui']
class GraphEditorCoreBreadcrumbs:
    class _Item(tuple):
        """
        _Item(id, name)
        """
        __match_args__: typing.ClassVar[tuple] = ('id', 'name')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('id', 'name')
        @staticmethod
        def __new__(_cls, id, name):
            """
            Create new instance of _Item(id, name)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new _Item object from a sequence or iterable
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
            Return a new _Item object replacing specified fields with new values
            """
    def __init__(self, selected_fn = ..., navigation: typing.Optional[typing.List[str]] = None, **kwargs):
        ...
    def destroy(self):
        ...
    def on_build(self):
        ...
