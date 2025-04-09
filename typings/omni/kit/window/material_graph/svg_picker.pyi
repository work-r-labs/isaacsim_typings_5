from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.dialog import FilePickerDialog
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Usd
import traceback as traceback
__all__: list = ['ATTRIBUTE_EMBEDDED_ICON', 'SvgPicker']
class SvgPicker:
    def _SvgPicker__get_svg_dir(self) -> str:
        """
        Return the workspace file
        """
    def _SvgPicker__on_cancel(self, filename: str, dir: str):
        ...
    def _SvgPicker__on_filter_item(self, prim: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        ...
    def _SvgPicker__on_open(self, filename: str, dir: str):
        """
        Called when the user presses the Save button in the dialog
        """
    def __init__(self):
        ...
    def destroy(self):
        ...
    def set_icon(self, prim):
        ...
def _set_svg_icon(*args, **kwargs):
    """
    Opens SVG file and saves its content to the prim
    """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
ATTRIBUTE_EMBEDDED_ICON: str = 'ui:nodegraph:node:embeddedIcon'
