from __future__ import annotations
import carb as carb
from functools import lru_cache
import omni as omni
from omni.kit.widget.toolbar.toolbar import Toolbar
from pathlib import Path
__all__: list = ['get_instance', 'get_data_path', 'get_data_path_internal', 'WidgetToolBarExtension']
class WidgetToolBarExtension(omni.ext._extensions.IExt):
    """
    omni.kit.widget.toolbar ext
    """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_data_path_internal(*args, **kwargs):
    ...
def get_instance() -> omni.kit.widget.toolbar.toolbar.Toolbar:
    """
    Get the instance of the toolbar.
    """
_toolbar_instance: omni.kit.widget.toolbar.toolbar.Toolbar  # value = <omni.kit.widget.toolbar.toolbar.Toolbar object>
