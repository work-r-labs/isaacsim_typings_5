"""
Module implementing the StageMenusExtension that manages the startup and shutdown of ContentBrowserOptions for stage menu customization in Omni UI.
"""
from __future__ import annotations
import omni as omni
from omni.kit.menu.stage.content_browser_options import ContentBrowserOptions
__all__: list[str] = ['ContentBrowserOptions', 'StageMenusExtension', 'omni']
class StageMenusExtension(omni.ext._extensions.IExt):
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
