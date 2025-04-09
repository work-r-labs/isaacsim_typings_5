"""
This module provides UI components and utility functions for managing and interacting with extensions in the Omni Kit window, including widgets for toggling extension states, searching, and selecting extension sources.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.widget.searchfield.searchfield import SearchField
from omni.kit.window.extensions.common import ExtSource
from omni.kit.window.extensions.common import ExtensionCommonInfo
from omni.kit.window.extensions.common import build_doc_urls
from omni.kit.window.extensions.common import pull_extension_async_by_name
from omni.kit.window.extensions.common import toggle_extension
from omni.kit.window.extensions.styles import get_style
from omni.kit.window.extensions.utils import get_setting
from omni.kit.window.extensions.utils import open_url
from omni.kit.window.extensions.utils import run_process
from omni import ui
import sys as sys
__all__ = ['ExtSource', 'ExtSourceSelector', 'ExtensionCommonInfo', 'ExtensionToggle', 'SearchField', 'SearchWidget', 'SimpleCheckBox', 'add_doc_link_button', 'add_icon_button', 'asyncio', 'build_doc_urls', 'carb', 'get_setting', 'get_style', 'omni', 'open_url', 'pull_extension_async_by_name', 'run_process', 'sys', 'toggle_extension', 'ui']
class ExtSourceSelector:
    """
    A class for selecting an extension source.
    
        Handles UI logic for selecting an extension source from a list of options.
    
        Args:
            on_selected_fn (Callable): Callback function invoked when a source is selected.
    """
    def __init__(self, on_selected_fn):
        """
        Initializes the ExtSourceSelector with a callback for selection events.
        """
    def set_badge_number(self, source, number):
        """
        Sets the badge number for a given extension source.
        
                Args:
                    source (:obj:`ExtSource`): The source for which to set the badge number.
                    number (int): The number to display on the badge.
        """
    def set_tab(self, source):
        """
        Activates the tab corresponding to the given source.
        
                Args:
                    source (:obj:`ExtSource`): The source for which to activate the tab.
        """
class ExtensionToggle:
    """
    A widget to toggle the state of an extension.
    
        This UI component is part of the extension management system, allowing users to install, enable, or disable extensions. It can also optionally display a label to indicate the current state of the extension.
    
        Args:
            item (:obj:`ExtensionCommonInfo`): The extension item to be managed.
            with_label (bool): Whether to display the label next to the toggle.
            show_install_button (bool): Whether to show the install button for non-local extensions.
            refresh_cb (Callable): Optional callback to invoke when the extension state changes.
    """
    def __init__(self, item: omni.kit.window.extensions.common.ExtensionCommonInfo, with_label = False, show_install_button = True, refresh_cb = None):
        """
        Initializes the extension toggle widget with various UI elements based on the extension's state and properties.
        """
class SearchWidget(omni.kit.widget.searchfield.searchfield.SearchField):
    """
    String field with a label overlay to type search string into.
    
        Args:
            on_search_fn (Callable[[str], None]): Function called with the search string.
    """
    def __init__(self, on_search_fn: typing.Callable[[typing.List[str]], NoneType]):
        """
        Initializes the search widget and sets up the search field with callback.
        """
    def clear_filters(self):
        """
        Clears all filters currently applied to the search.
        """
    def get_filters(self):
        """
        Gets the current set of filters applied to the search.
        
                Returns:
                    list: The list of current filters.
        """
    def toggle_filter(self, filter_to_toggle):
        """
        Toggles a filter on or off in the current search filters.
        
                Args:
                    filter_to_toggle (str): The filter to toggle.
        """
class SimpleCheckBox:
    """
    A simple check box UI element with an optional text label.
    
        This class creates a checkbox with a label, and allows for a callback function to
        be executed when the checkbox state changes. It can be enabled or disabled and
        can have a bound data model.
    
        Args:
            checked (bool): Initial checked state of the checkbox.
            on_checked_fn (Callable): Function to call when checkbox state changes.
            text (str, optional): Text to display next to the checkbox. Defaults to None.
            model (:obj:`ui.SimpleBoolModel`, optional): Data model to bind to the checkbox. Defaults to None.
            enabled (bool, optional): Specifies if the checkbox is interactable. Defaults to True.
    """
    def __init__(self, checked: bool, on_checked_fn: typing.Callable, text: str = None, model = None, enabled = True):
        """
        Initializes a simple checkbox with a label and a callback function.
        """
def add_doc_link_button(ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo, package_dict: typing.Dict, docs_dict: typing.Dict):
    """
    Adds a documentation link button to the UI if valid URLs are found.
    
        Args:
            ext_item (:obj:`ExtensionCommonInfo`): The extension item to get documentation URLs for.
            package_dict (Dict): Dictionary containing package information.
            docs_dict (Dict): Dictionary containing documentation information.
    """
def add_icon_button(name, on_click):
    """
    Creates a button with an icon.
    
        Args:
            name (str): The name of the button.
            on_click (Callable): The function to call when the button is clicked.
    """
