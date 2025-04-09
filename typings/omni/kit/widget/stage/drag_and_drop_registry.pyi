from __future__ import annotations
from carb import log_warn
import dataclasses
from dataclasses import dataclass
from omni.kit.widget.stage.singleton import Singleton
import typing
__all__: list = ['DragAndDropRegistry']
class DropHandler:
    """
    DropHandler(filter_fn: Callable[[Any], bool], handler_fn: Callable[[Any, Any], NoneType])
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'filter_fn': Field(name='filter_fn',type=typing.Callable[[typing.Any], bool],default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'handler_fn': Field(name='handler_fn',type=typing.Callable[[typing.Any, typing.Any], NoneType],default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('filter_fn', 'handler_fn')
    def __eq__(self, other):
        ...
    def __init__(self, filter_fn: typing.Callable[[typing.Any], bool], handler_fn: typing.Callable[[typing.Any, typing.Any], NoneType]) -> None:
        ...
    def __repr__(self):
        ...
