"""
A standardized dialog for importing files
"""
from __future__ import annotations
from carb import log_warn
from omni.kit.window.file_importer.extension import FileImporterExtension
from omni.kit.window.file_importer.extension import get_instance
from omni.kit.window.filepicker.detail_view import DetailFrameController as ImportOptionsDelegate
from . import extension
__all__: list = ['FileImporterExtension', 'ImportOptionsDelegate', 'get_file_importer']
def get_file_importer() -> extension.FileImporterExtension:
    """
    Returns the singleton file_importer extension instance
    """
