from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit import notification_manager as nm
from omni.kit.usd import collect
from omni.kit.usdz_export.utils import copy
from omni.kit.usdz_export.utils import is_extension_loaded
from omni.kit.usdz_export.utils import list_folder_async
from omni.kit.widget.prompt.prompt import PromptManager
from omni.kit.window.file_exporter import get_file_exporter
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Usd
import tempfile as tempfile
from zipfile import ZipFile
__all__: list[str] = ['LayersMenu', 'Path', 'PromptManager', 'Sdf', 'Usd', 'ZipFile', 'asyncio', 'carb', 'collect', 'copy', 'export', 'get_file_exporter', 'is_extension_loaded', 'layers_available', 'list_folder_async', 'nm', 'omni', 'os', 'partial', 'tempfile', 'usdz_export']
class LayersMenu:
    """
    
        When this object is alive, Layers 2.0 has an additional action
        for exporting the layer to USDZ.
        
    """
    def __init__(self):
        ...
    def destroy(self):
        """
        Remove the menu from Layers 2.0
        """
def export(objects):
    """
    Export the target layer to USDZ.
    
        Args:
            objects (dict): A dictionary containing selected layer item information.
        
    """
def layers_available() -> bool:
    """
    Returns True if the extension "omni.kit.widget.layers" is loaded
    """
def usdz_export(identifier, export_path):
    """
    Export a layer to USDZ using a temporary directory for file collection and packaging.
    
        Args:
            identifier (str): Layer identifier to export.
            export_path (str): Destination path for the exported USDZ file.
        
    """
