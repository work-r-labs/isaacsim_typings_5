"""
This module defines a ContentBrowserRegistryExtension class for monitoring and managing customizations in the Content Browser, including custom menus, selection handlers, and search delegates, and provides a mechanism to retrieve its singleton instance.
"""
from __future__ import annotations
from collections import OrderedDict
import omni as omni
__all__ = ['ContentBrowserRegistryExtension', 'OrderedDict', 'g_singleton', 'get_instance', 'omni']
class ContentBrowserRegistryExtension(omni.ext._extensions.IExt):
    """
    A registry extension that monitors functional customizations applied to the Content Browser.
    
        This class tracks custom menus, selection handlers, and search delegates, allowing them to be reapplied if the Content Browser is restarted.
        
    """
    def __init__(self):
        ...
    def deregister_custom_menu(self, context: str, name: str):
        ...
    def deregister_search_delegate(self, search_delegate: SearchDelegate):
        ...
    def deregister_selection_handler(self, handler: typing.Callable):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def register_custom_menu(self, context: str, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1):
        ...
    def register_search_delegate(self, search_delegate: SearchDelegate):
        ...
    def register_selection_handler(self, handler: typing.Callable):
        ...
def get_instance():
    """
    Retrieves the singleton instance of the ContentBrowserRegistryExtension.
    
        Returns:
            ContentBrowserRegistryExtension: The singleton instance if it exists, otherwise None.
    """
g_singleton: ContentBrowserRegistryExtension  # value = <omni.kit.window.content_browser_registry.extension.ContentBrowserRegistryExtension object>
