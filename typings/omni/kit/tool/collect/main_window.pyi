"""
This module provides a user interface for managing the collection of assets, allowing users to specify various collection options and initiate the collection process.
"""
from __future__ import annotations
import omni as omni
from omni.kit.window.file_exporter import get_file_exporter
from omni import ui
import os as os
__all__ = ['CollectMainWindow', 'get_file_exporter', 'omni', 'os', 'ui']
class CollectMainWindow:
    """
    A user interface window for managing the collection of assets.
    
        This class provides a main window interface for users to specify options for asset collection, including the file location and asset filtering preferences. The options are applied when the Start button is clicked, triggering the collection process.
    
        Args:
            collect_button_fn (callable, optional): Function to call when the Start button is clicked.
            cancel_button_fn (callable, optional): Function to call when the Cancel button is clicked.
    """
    def __init__(self, collect_button_fn = None, cancel_button_fn = None):
        ...
    def _build_content_ui(self):
        ...
    def _on_cancel_button_clicked(self):
        ...
    def _on_collect_button_clicked(self):
        ...
    def _on_default_prim_toggled(self, model):
        ...
    def _on_flat_collection_toggled(self, model):
        ...
    def _show_file_picker(self):
        ...
    def destroy(self):
        ...
    def hide(self):
        ...
    def set_cancel_fn(self, cancel_fn):
        ...
    def set_collect_fn(self, collect_fn):
        ...
    def show(self, export_folder = None):
        ...
