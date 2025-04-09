"""
This module provides a user interface for managing and displaying extensions in an application, allowing users to list, select, and view details about extensions, including their associated dependencies and properties.
"""
from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.window.extensions import common
from omni.kit.window.extensions import ext_controller
from omni.kit.window.extensions import ext_info_widget
from omni.kit.window.extensions.exts_list_widget import ExtsListWidget
from omni.kit.window.extensions.utils import get_setting
from omni.kit.window.extensions.window import ExtsWindow
from omni import ui
import weakref as weakref
__all__ = ['ExtsListWidget', 'ExtsWindow', 'ExtsWindowExtension', 'MENU_GROUP', 'MenuHelperExtension', 'WINDOW_NAME', 'asyncio', 'common', 'ext_controller', 'ext_info_widget', 'get_instance', 'get_setting', 'omni', 'show_window', 'ui', 'weakref']
class ExtsWindowExtension(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    """
    The entry point exts 2.0 window
    
        This extension integrates into the omni.ext.IExt interface and provides a user interface for managing and interacting with extensions in the application. It features a window that lists available extensions and allows users to control their activation state, view detailed information, and manage extension-specific settings. Additionally, it offers a menu integration that allows easy access to the extensions window from the application's main menu.
        
    """
    @classmethod
    def add_menu_to_info_widget(cls, tab: omni.kit.window.extensions.common.PageBase):
        """
        Adds a new menu to the extension information widget.
        
                Args:
                    tab (:obj:`ext_info_widget.PageBase`): The tab to add to the info widget.
        """
    @classmethod
    def add_searchable_keyword(cls, keyword: str, description: str, filter_on_keyword: typing.Callable, clear_cache: typing.Callable):
        """
        Adds a new searchable keyword to the extensions list widget.
        
                Args:
                    keyword (str): The keyword to be added.
                    description (str): A brief description of the keyword.
                    filter_on_keyword (Callable): The callback for filtering based on the keyword.
                    clear_cache (Callable): The callback to clear the cache when needed.
        """
    @classmethod
    def add_tab_to_info_widget(cls, tab: omni.kit.window.extensions.common.PageBase):
        """
        Adds a new tab to the extension information widget.
        
                Args:
                    tab (:obj:`ext_info_widget.PageBase`): The tab to add to the info widget.
        """
    @classmethod
    def refresh_extension_info_widget(cls):
        """
        Refreshes the contents of the extension information widget.
        """
    @classmethod
    def refresh_menu_items(cls):
        """
        Refreshes the list of search items in the extension list widget.
        """
    @classmethod
    def refresh_search_items(cls):
        """
        Refreshes the list of search items in the extension list widget.
        """
    @classmethod
    def remove_menu_from_info_widget(cls, tab: omni.kit.window.extensions.common.PageBase):
        """
        Removes a menu from the extension information widget.
        
                Args:
                    tab (:obj:`ext_info_widget.PageBase`): The tab to remove from the info widget.
        """
    @classmethod
    def remove_searchable_keyword(cls, keyword_to_remove: str):
        """
        Removes a searchable keyword from the extensions list widget.
        
                Args:
                    keyword_to_remove (str): The keyword to be removed.
        """
    @classmethod
    def remove_tab_from_info_widget(cls, tab: omni.kit.window.extensions.common.PageBase):
        """
        Removes a tab from the extension information widget.
        
                Args:
                    tab (:obj:`ext_info_widget.PageBase`): The tab to remove from the info widget.
        """
    def on_shutdown(self):
        """
        Performs cleanup operations when the extension is shutting down.
        """
    def on_startup(self, ext_id):
        """
        Initializes the extension with the given extension ID.
        """
    def show_window(self, value):
        """
        Controls the visibility of the window based on the given value.
        
                Args:
                    value (bool): Determines whether to show or hide the window.
        """
def get_instance() -> weakref.ReferenceType[ExtsWindowExtension]:
    """
    Returns a weak reference to the singleton instance of ExtsWindowExtension.
    
        Returns:
            weakref.ReferenceType[:obj:`ExtsWindowExtension`]: A weak reference to the ExtsWindowExtension instance.
    """
def show_window(value: bool):
    """
    Show/Hide Extensions window
    """
MENU_GROUP: str = 'Window'
WINDOW_NAME: str = 'Extensions'
_ext_instance: ExtsWindowExtension  # value = <omni.kit.window.extensions.extension.ExtsWindowExtension object>
