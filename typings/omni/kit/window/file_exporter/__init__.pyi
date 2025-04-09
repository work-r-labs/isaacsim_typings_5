"""
A standardized dialog for exporting files
"""
from __future__ import annotations
from carb import log_warn
from omni.kit.window.file_exporter.extension import FileExporterExtension
from omni.kit.window.file_exporter.extension import get_instance
from omni.kit.window.filepicker.detail_view import DetailFrameController as ExportOptionsDelegate
from . import extension
__all__: list = ['FileExporterExtension', 'ExportOptionsDelegate', 'get_file_exporter']
def get_file_exporter() -> extension.FileExporterExtension:
    """
    Returns the singleton file_exporter extension instance
    """
