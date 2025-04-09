from __future__ import annotations
import omni as omni
from omni.kit.menu.stage.content_browser_options import ContentBrowserOptions
__all__ = ['ContentBrowserOptions', 'StageMenusExtension', 'omni']
class StageMenusExtension(omni.ext._extensions.IExt):
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
