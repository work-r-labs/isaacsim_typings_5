from __future__ import annotations
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
__all__ = ['Sdf', 'Tf', 'TfNoticeWrapper', 'Usd']
class TfNoticeWrapper:
    def __del__(self):
        ...
    def __init__(self, attr_names: list[str], prim_paths: list[pxr.Sdf.Path], callback: typing.Callable[[pxr.Usd.ObjectsChanged, pxr.Usd.Stage], NoneType], stage: pxr.Usd.Stage):
        ...
    def destroy(self):
        ...
