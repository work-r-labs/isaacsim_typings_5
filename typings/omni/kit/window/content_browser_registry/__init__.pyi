"""
This module provides an interface for registering and managing custom menus, selection handlers, search delegates, and file open handlers within the Content Browser of NVIDIA's Omniverse Kit.
"""
from __future__ import annotations
import collections
from collections import OrderedDict
from omni.kit.window.content_browser_registry.extension import ContentBrowserRegistryExtension
from omni.kit.window.content_browser_registry.extension import get_instance
from . import extension
__all__: list = ['get_instance', 'custom_menus', 'selection_handlers', 'search_delegate', 'register_context_menu', 'deregister_context_menu', 'register_listview_menu', 'deregister_listview_menu', 'register_import_menu', 'deregister_import_menu', 'register_file_open_handler', 'deregister_file_open_handler', 'register_selection_handler', 'deregister_selection_handler', 'register_search_delegate', 'deregister_search_delegate', 'register_checkpoint_menu', 'deregister_checkpoint_menu']
def custom_menus() -> collections.OrderedDict:
    """
    Retrieves an ordered dictionary of custom menus registered within the application.
    
    Returns:
        OrderedDict: An ordered dictionary where keys are menu identifiers and values
        are specific menu configurations. If no menus are registered, an empty OrderedDict is returned.
    """
def deregister_checkpoint_menu(name: str):
    """
    Deregisters a previously registered checkpoint menu.
    
        Args:
            name (str): The name of the checkpoint menu to deregister.
    """
def deregister_context_menu(name: str):
    """
    Removes a previously registered context menu.
    
        Args:
            name (str): The name of the menu to deregister.
    """
def deregister_file_open_handler(name: str):
    """
    Removes a previously registered file open handler.
    
        Args:
            name (str): The name of the handler to deregister.
    """
def deregister_import_menu(name: str):
    """
    Removes a custom menu item from the import menu.
    
        Args:
            name (str): The name of the menu item to remove.
    """
def deregister_listview_menu(name: str):
    """
    Removes a previously registered listview menu.
    
        Args:
            name (str): The name of the menu to deregister.
    """
def deregister_search_delegate(search_delegate: SearchDelegate):
    """
    Removes a previously registered search delegate.
    
        Args:
            search_delegate (SearchDelegate): The delegate to remove from the registry.
    """
def deregister_selection_handler(handler: typing.Callable):
    """
    Removes a selection handler from the registry.
    
        Args:
            handler (Callable): The function to be removed from the selection handlers.
    """
def register_checkpoint_menu(name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index = -1):
    """
    Registers a custom menu item under the 'checkpoint' category.
    
        Args:
            name (str): The unique name for the checkpoint menu item.
            glyph (str): Glyph icon associated with the menu item.
            click_fn (Callable): Function to call when the menu item is clicked.
            show_fn (Callable): Function to determine visibility of the menu item.
            index (int, optional): Position in the menu to insert the item at. Defaults to -1.
    """
def register_context_menu(name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1):
    """
    Adds a new context menu option.
    
        Args:
            name (str): Identifier for the menu option.
            glyph (str): Icon representation for the menu option.
            click_fn (Callable): Function to execute on menu option click.
            show_fn (Callable): Function to determine if the menu option should be shown.
            index (int, optional): Position in the menu to insert the option. Defaults to -1.
    """
def register_file_open_handler(name: str, open_fn: typing.Callable, file_type: typing.Union[int, typing.Callable]):
    """
    Registers a handler for opening files.
    
        Args:
            name (str): Identifier for the open handler.
            open_fn (Callable): Function to call when opening a file.
            file_type (Union[int, Callable]): Type of file or function determining the file type.
        
    """
def register_import_menu(name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable):
    """
    Registers a custom menu item for the import context.
    
        Args:
            name (str): The unique name for the menu item.
            glyph (str): The icon glyph for the menu item.
            click_fn (Callable): The function to call when the menu item is clicked.
            show_fn (Callable): The function to determine if the menu should be shown.
        
    """
def register_listview_menu(name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1):
    """
    Registers a menu item to the listview context menu.
    
        Args:
            name (str): The unique name for the menu item.
            glyph (str): The icon glyph associated with the menu item.
            click_fn (Callable): The function to call when the item is clicked.
            show_fn (Callable): The function to determine menu item visibility.
            index (int, optional): Position to insert the item into the menu. Defaults to -1.
    """
def register_search_delegate(search_delegate: SearchDelegate):
    """
    Registers a search delegate.
    
        Args:
            search_delegate (SearchDelegate): The delegate to handle search queries.
    """
def register_selection_handler(handler: typing.Callable):
    """
    Registers a selection handler to the registry.
    
        Args:
            handler (Callable): Function to handle selection events.
    """
def search_delegate() -> SearchDelegate:
    """
    Retrieves the current search delegate instance from the content browser registry.
    
        Returns:
            SearchDelegate: The search delegate object if the registry is initialized, otherwise None.
    """
def selection_handlers() -> typing.Set:
    """
    Retrieves the set of registered selection handlers from the Content Browser Registry.
    
        Returns:
            Set: A set of registered selection handlers, or an empty set if the registry is not available.
    """
