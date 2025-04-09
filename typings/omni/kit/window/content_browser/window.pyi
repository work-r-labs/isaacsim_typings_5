from __future__ import annotations
from omni.kit.window.content_browser.external_drag_drop_helper import destroy_external_drag_drop
from omni.kit.window.content_browser.external_drag_drop_helper import setup_external_drag_drop
import omni.kit.window.content_browser.widget
from omni.kit.window.content_browser.widget import ContentBrowserWidget
from omni import ui
import weakref as weakref
__all__ = ['ContentBrowserWidget', 'ContentBrowserWindow', 'destroy_external_drag_drop', 'setup_external_drag_drop', 'ui', 'weakref']
class ContentBrowserWindow:
    """
    The Content Browser window
    """
    def __init__(self):
        ...
    def _build_ui(self, title, width, height):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def destroy(self):
        ...
    def get_visible(self):
        ...
    def set_visibility_changed_listener(self, listener):
        ...
    def set_visible(self, value):
        ...
    @property
    def widget(self) -> omni.kit.window.content_browser.widget.ContentBrowserWidget:
        ...
