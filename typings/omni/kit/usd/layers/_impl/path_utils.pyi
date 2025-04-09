from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
import traceback as traceback
__all__: list = ['PathUtils']
class PathUtils:
    @staticmethod
    def compute_absolute_path(base_path, path):
        """
        Computes absolute path.
        
                Args:
                    base_path (str): Absolute path that path will be based on.
                    path (str): Path to be combined.
                
        """
    @staticmethod
    def compute_relative_path(base_path, file_path):
        """
        Computes relative path given base path.
        
                Args:
                    base_path (str): Absolute path that file path will be relative to.
                    file_path (str): Absolute path.
        
                Return:
                    Relative path of file_path that is relative to base_path. If base_path
                    and file_path are not in the same domain or server, it will return file_path
                    directly.
                
        """
    @staticmethod
    def exists_async(path):
        ...
    @staticmethod
    def exists_sync(path):
        ...
    @staticmethod
    def is_omni_path(path: str):
        ...
