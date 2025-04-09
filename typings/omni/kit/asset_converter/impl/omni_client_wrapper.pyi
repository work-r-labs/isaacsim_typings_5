from __future__ import annotations
import carb as carb
import omni as omni
from pathlib import PurePosixPath
import traceback as traceback
__all__: list = ['OmniClientWrapper']
class OmniClientWrapper:
    @staticmethod
    def copy(src_path: str, dest_path: str):
        ...
    @staticmethod
    def create_folder(path):
        ...
    @staticmethod
    def exists(path):
        ...
    @staticmethod
    def exists_sync(path):
        ...
    @staticmethod
    def parent(path: str) -> str:
        ...
    @staticmethod
    def read(src_path: str):
        ...
    @staticmethod
    def write(path: str, content):
        ...
    @staticmethod
    def writeable(path: str):
        ...
    @staticmethod
    def writeable_async(path: str) -> bool:
        ...
def _encode_content(content):
    ...
