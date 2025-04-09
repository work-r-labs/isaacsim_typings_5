from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.actions.core.actions import get_action_registry
__all__ = ['carb', 'deregister_hotkeys', 'get_action_registry', 'omni', 'register_hotkeys']
def deregister_hotkeys(extension_id: str):
    ...
def register_hotkeys(extension_id: str, window_name: typing.Optional[str] = None):
    ...
_DEFAULT_HOTKEY_MAP: dict = {'perspective_camera': 'ALT+P', 'top_camera': 'ALT+T', 'front_camera': 'ALT+F', 'right_camera': 'ALT+R', 'toggle_grid_visibility': 'G', 'toggle_camera_visibility': 'SHIFT+C', 'toggle_light_visibility': 'SHIFT+L', 'toggle_global_visibility': 'SHIFT+H', 'toggle_wireframe': 'SHIFT+W'}
_HOTKEYS_EXT: str = 'omni.kit.hotkeys.core'
