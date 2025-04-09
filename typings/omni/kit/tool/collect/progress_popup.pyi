"""
This module provides a custom progress tracking model and a popup UI component for displaying progress within the Omniverse Kit.
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['CustomProgressModel', 'ProgressPopup', 'ui']
class CustomProgressModel(omni.ui._ui.AbstractValueModel):
    """
    A model to track and manage progress information for UI components.
    
        This model is designed to work with progress bars or similar UI components in need of displaying progress. It maintains current progress value and total steps, allowing for the dynamic adjustment of the progress displayed. The model ensures that the progress value is always within the bounds of the total steps and provides functionalities to convert and retrieve the progress as both a float ratio and a formatted string.
        
    """
    total_steps = ...
    def __init__(self):
        ...
    def get_value_as_float(self):
        ...
    def get_value_as_string(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set
        """
    @property
    def progress(self):
        ...
class ProgressPopup:
    """
    Creates a modal window with a status label and a progress bar inside.
    
        Args:
            title (str): Title of the window.
            cancel_button_text (str): Text for the cancel button.
            cancel_button_fn (callable): Callback function for the cancel button.
            status_text (str): Initial text to display as status.
            modal (bool): Determines if the window is modal.
        
    """
    progress = ...
    status_text = ...
    total_steps = ...
    def __enter__(self):
        ...
    def __exit__(self, type, value, trace):
        ...
    def __init__(self, title, cancel_button_text = 'Cancel', cancel_button_fn = None, status_text = '', modal = False):
        ...
    def _build_ui(self):
        ...
    def _on_cancel_button_fn(self):
        ...
    def destroy(self):
        ...
    def hide(self):
        ...
    def is_visible(self):
        ...
    def set_cancel_fn(self, on_cancel_button_clicked):
        ...
    def show(self):
        ...
