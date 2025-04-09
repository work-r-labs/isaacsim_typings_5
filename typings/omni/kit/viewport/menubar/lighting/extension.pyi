from __future__ import annotations
import omni as omni
__all__: list = ['ViewportLightingMenuBarExtension']
class ViewportLightingMenuBarExtension(omni.ext._extensions.IExt):
    """
    The Entry Point for the Lighting item in Viewport Menu Bar
    """
    def _ViewportLightingMenuBarExtension__no_menu_setup(self, menu_container: MenuContainer):
        ...
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id, *args, **kwargs):
        ...
