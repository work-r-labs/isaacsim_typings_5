from __future__ import annotations
from functools import partial
from omni import ui
__all__ = ['GraphEditorCoreSplitter', 'partial', 'ui']
class GraphEditorCoreSplitter:
    def __init__(self, build_left_fn: typing.Callable[[], NoneType], build_right_fn: typing.Callable[[], NoneType]):
        ...
    def destroy(self):
        ...
    def on_build(self):
        ...
