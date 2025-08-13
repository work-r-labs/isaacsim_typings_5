from __future__ import annotations
from pxr import Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
__all__: list[str] = ['Sdf', 'Tf', 'TfNoticeWrapper', 'Usd']
class TfNoticeWrapper:
    def __del__(self):
        ...
    def __init__(self, attr_names: list[str], prim_paths: list[pxr.Sdf.Path], callback: typing.Callable[[pxr.Usd.ObjectsChanged, pxr.Usd.Stage], NoneType], stage: pxr.Usd.Stage):
        ...
    def destroy(self):
        ...
