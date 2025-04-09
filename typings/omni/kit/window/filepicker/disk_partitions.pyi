from __future__ import annotations
import dataclasses
from dataclasses import dataclass
import platform as platform
import typing
__all__: list = ['Partition', 'disk_partitions']
class Partition:
    """
    Partition(device: str, mountpoint: str, fstype: str, opts: list[str])
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'device': Field(name='device',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'mountpoint': Field(name='mountpoint',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'fstype': Field(name='fstype',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'opts': Field(name='opts',type=list[str],default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('device', 'mountpoint', 'fstype', 'opts')
    def __eq__(self, other):
        ...
    def __init__(self, device: str, mountpoint: str, fstype: str, opts: list[str]) -> None:
        ...
    def __repr__(self):
        ...
def disk_partitions():
    """
    Minimal implementation of disk_partitions from psutil.
    """
