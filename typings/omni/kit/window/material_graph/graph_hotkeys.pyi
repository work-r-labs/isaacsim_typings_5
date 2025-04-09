from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.actions.core.actions import get_action_registry
__all__ = ['app', 'carb', 'deregister_hotkeys', 'g_action_registry', 'g_ext_manager', 'get_action_registry', 'omni', 'register_hotkeys']
def deregister_hotkeys(extension_id: str):
    ...
def register_hotkeys(extension_id: str, window_name: typing.Optional[str] = None):
    ...
_DEFAULT_HOTKEY_MAP: dict = {'layout_all_nodes': 'CTRL+L', 'focus_on_nodes': 'F', 'copy_nodes': 'CTRL+C', 'paste_nodes': 'CTRL+V', 'expand_all_nodes': 'KEY_1', 'minimize_all_nodes': 'KEY_2', 'close_all_nodes': 'KEY_3', 'material_unpause_and_pause': 'CTRL+R'}
_HOTKEYS_EXT: str = 'omni.kit.hotkeys.core'
app: omni.kit.app._app.IApp  # value = <omni.kit.app._app.IApp object>
g_action_registry: omni.kit.actions.core._kit_actions_core.IActionRegistry  # value = <omni.kit.actions.core._kit_actions_core.IActionRegistry object>
g_ext_manager: omni.ext._extensions.ExtensionManager  # value = <omni.ext._extensions.ExtensionManager object>
