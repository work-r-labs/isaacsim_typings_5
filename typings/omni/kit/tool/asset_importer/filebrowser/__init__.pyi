from __future__ import annotations
import typing
from . import app_filebrowser
__all__ = ['FileBrowserMode', 'FileBrowserSelectionType', 'app_filebrowser']
class FileBrowserMode:
    OPEN: typing.ClassVar[int] = 0
    SAVE: typing.ClassVar[int] = 1
class FileBrowserSelectionType:
    ALL: typing.ClassVar[int] = 2
    DIRECTORY_ONLY: typing.ClassVar[int] = 1
    FILE_ONLY: typing.ClassVar[int] = 0
