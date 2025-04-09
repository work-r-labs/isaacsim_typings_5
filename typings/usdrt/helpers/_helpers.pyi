from __future__ import annotations
__all__ = ['FabricId', 'PathC', 'StageReaderWriterId', 'UsdStageId']
class FabricId:
    @property
    def id(self) -> int:
        ...
class PathC:
    def __init__(self, path: ...) -> None:
        ...
    @property
    def path(self) -> int:
        ...
class StageReaderWriterId:
    @property
    def id(self) -> int:
        ...
class UsdStageId:
    def __init__(self, arg0: int) -> None:
        ...
    @property
    def id(self) -> int:
        ...
