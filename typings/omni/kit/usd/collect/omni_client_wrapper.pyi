from __future__ import annotations
import carb as carb
import omni as omni
import os as os
import stat as stat
__all__: list = ['OmniClientWrapper']
class OmniClientWrapper:
    @staticmethod
    def copy(src_path: str, dest_path: str, set_target_writable_if_read_only = False):
        ...
    @staticmethod
    def create_folder(path):
        ...
    @staticmethod
    def delete(path: str):
        ...
    @staticmethod
    def exists(path):
        ...
    @staticmethod
    def exists_sync(path):
        ...
    @staticmethod
    def read(src_path: str):
        ...
    @staticmethod
    def set_write_permission(src_path: str):
        ...
    @staticmethod
    def write(path: str, content):
        ...
def _encode_content(content):
    ...
