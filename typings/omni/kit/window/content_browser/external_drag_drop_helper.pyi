from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.window.drop_support.drop_support import ExternalDragDrop
from omni import ui
import os as os
__all__ = ['ExternalDragDrop', 'asyncio', 'carb', 'destroy_external_drag_drop', 'external_drag_drop', 'omni', 'os', 'setup_external_drag_drop', 'ui']
def _cleanup_slashes(path: str, is_directory: bool = False) -> str:
    """
    
        Makes path/slashes uniform
    
        Args:
            path: path
            is_directory is path a directory, so final slash can be added
    
        Returns:
            path
        
    """
def _on_ext_drag_drop(edd: omni.kit.window.drop_support.drop_support.ExternalDragDrop, payload: typing.List[str], api, frame: omni.ui._ui.Frame):
    ...
def destroy_external_drag_drop():
    ...
def setup_external_drag_drop(window_name: str, browser_widget, window_frame: omni.ui._ui.Frame):
    ...
external_drag_drop: omni.kit.window.drop_support.drop_support.ExternalDragDrop  # value = <omni.kit.window.drop_support.drop_support.ExternalDragDrop object>
