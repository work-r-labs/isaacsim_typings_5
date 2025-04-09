"""
This module provides the ExtsWindow class for managing and displaying extensions alongside additional UI components for visualization of extension information, dependencies, and properties.
"""
from __future__ import annotations
import asyncio as asyncio
from omni.kit.window.extensions.ext_info_widget import ExtInfoWidget
from omni.kit.window.extensions.ext_status_bar import ExtStatusBar
from omni.kit.window.extensions.exts_dependency_window import ExtsDependenciesWindow
from omni.kit.window.extensions.exts_list_widget import ExtsListWidget
from omni.kit.window.extensions.exts_properties_widget import ExtsPropertiesWidget
from omni.kit.window.extensions.styles import get_style
from omni import ui
__all__: list = ['PageSwitcher', 'ExtsWindow']
class ExtsWindow:
    """
    Extensions window
    
        Args:
            on_visibility_changed_fn (Callable): Function called when window visibility changes.
    """
    def __init__(self, on_visibility_changed_fn: typing.Callable):
        """
        Initializes the ExtsWindow with UI components and callback functions.
        """
    def _select_ext(self, ext_summary):
        ...
    def _show_dependencies(self, ext_id: str):
        ...
    def _show_properties(self):
        ...
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def rebuild(self):
        ...
class PageSwitcher:
    """
    A class to manage the visibility of different pages in a UI environment.
    
        The class maintains a collection of pages, allowing only one to be visible at a time. It provides methods to add new pages, select a page to be visible, and remove all pages upon destruction.
        
    """
    def __init__(self):
        """
        Initializes a new instance of the PageSwitcher, which manages switching between UI pages.
        """
    def add_page(self, name, widget):
        """
        Adds a new page to the PageSwitcher.
        
                Args:
                    name (str): The unique name of the page to add.
                    widget (:obj:`ui.Widget`): The UI widget that represents the page content.
        """
    def destroy(self):
        """
        Destroys all pages managed by the PageSwitcher and resets its state.
        """
    def select_page(self, name, force = False):
        """
        Selects a page to be displayed in the PageSwitcher.
        
                Args:
                    name (str): The name of the page to select.
                    force (bool): If True, forces the page to be selected even if it is already selected.
        """
PAGE_DEPENDENCIES: str = 'dependencies'
PAGE_INFO: str = 'info'
PAGE_PROPERTIES: str = 'properties'
