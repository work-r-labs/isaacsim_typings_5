"""
This module provides a SearchWidget with a customizable searchable combobox and a SearchModel for managing search functionality in UI components.
"""
from __future__ import annotations
import asyncio as asyncio
from enum import IntFlag
import omni as omni
from omni import ui
__all__: list = ['SearchModel', 'SearchWidget']
class SearchModel(omni.ui._ui.AbstractValueModel):
    """
    A model to support searching functionality in UI components.
    
        This class provides methods to set and retrieve search strings, and to determine if a given string is part of the current search string. It is designed to be used within UI components that require search capabilities, such as searchable combo boxes or lists.
    
        Args:
            modified_fn (callable): A function to be called when the search string is modified.
    """
    def __init__(self, modified_fn):
        """
        Initializes the SearchModel with a function to call when the model is modified.
        """
    def get_value_as_string(self):
        """
        Retrieves the current value of the model as a string.
        
                Returns:
                    str: The current value of the model.
        """
    def is_in_string(self, string: str):
        """
        Checks if the model's current string is a substring of the provided string.
        
                Args:
                    string (str): The string to check against.
        
                Returns:
                    bool: True if the model's string is a substring of `string`, False otherwise.
        """
    def set_value(self, value):
        """
        Sets the value of the model and triggers the modified callback if it's provided.
        
                Args:
                    value: The new value to set for the model.
        """
class SearchWidget:
    """
    A widget that provides a searchable combobox with customizable styles.
    
        Args:
            theme (str): The theme to apply to the combobox.
            icon_path (str): Path to the directory containing the icons.
            modified_fn (callable, optional): Function to call when search input is modified.
    """
    def __init__(self, theme: str, icon_path: str, modified_fn: callable = None):
        """
        A widget that provides a searchable combobox with customizable styles.
        
                Args:
                    theme (str): The theme to apply to the combobox.
                    icon_path (str): Path to the directory containing the icons.
                    modified_fn (callable, optional): Function to call when search input is modified.
        """
    def build_ui(self, width, search_size):
        """
        Build UI for SearchWidget.
        """
    def build_ui_popup(self, search_size: float, default_value: str, popup_text: str, index: int, update_fn: callable):
        """
        Builds Combobox like widget when 'open' button is clicked.
        """
    def clean(self):
        """
        Cleans up the SearchWidget and destroys models.
        """
    def destroy(self):
        """
        Destroys the SearchWidget widget.
        """
    def focus(self):
        """
        Focus caret on search string.
        """
    def get_text(self):
        """
        Gets selected item in items list.
        """
    def set_placeholder_text(self, msg: str):
        """
        Sets string when search field is empty.
        """
    def set_text(self, new_text: str):
        """
        Sets selected item in items list.
        """
    def update(self, string):
        """
        Update search string.
        """
