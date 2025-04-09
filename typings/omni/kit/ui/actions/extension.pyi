from __future__ import annotations
import omni as omni
from omni.kit.ui.actions.actions import deregister_actions
from omni.kit.ui.actions.actions import register_actions
from omni.kit.ui.actions.hotkeys import deregister_hotkeys
from omni.kit.ui.actions.hotkeys import register_hotkeys
__all__: list = ['UIActionsExtension', 'get_instance']
class UIActionsExtension(omni.ext._extensions.IExt):
    """
    Actions and Hotkeys related to the Viewport
    """
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
_extension_instance: UIActionsExtension  # value = <omni.kit.ui.actions.extension.UIActionsExtension object>
