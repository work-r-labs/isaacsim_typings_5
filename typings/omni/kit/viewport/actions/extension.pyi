from __future__ import annotations
import omni as omni
from omni.kit.viewport.actions.actions import deregister_actions
from omni.kit.viewport.actions.actions import register_actions
from omni.kit.viewport.actions.hotkeys import deregister_hotkeys
from omni.kit.viewport.actions.hotkeys import register_hotkeys
__all__: list = ['ViewportActionsExtension', 'get_instance']
class ViewportActionsExtension(omni.ext._extensions.IExt):
    """
    Actions and Hotkeys related to the Viewport
    """
    _ViewportActionsExtension__g_usd_context_streams = None
    @staticmethod
    def _watch_stage_open(usd_context_name: str, open_callback: typing.Callable):
        ...
    def __init__(self):
        ...
    def _on_hotkey_ext_changed(self, ext_id: str, ext_change_type: omni.ext._extensions.ExtensionStateChangeType):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_instance():
    ...
_extension_instance: ViewportActionsExtension  # value = <omni.kit.viewport.actions.extension.ViewportActionsExtension object>
