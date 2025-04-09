from __future__ import annotations
import typing
__all__ = ['LayerGlobals']
class LayerGlobals:
    _missing_layer_map: typing.ClassVar[set] = set()
    @staticmethod
    def add_missing_layer(layer_identifier: str):
        ...
    @staticmethod
    def is_layer_missing(layer_identifier: str) -> bool:
        ...
    @staticmethod
    def on_stage_attached(stage):
        ...
    @staticmethod
    def on_stage_detached():
        ...
